import json, re, urllib.request, urllib.parse
from pathlib import Path

STAGE = Path(__file__).resolve().parent
RAW = STAGE / 'raw' / 'jack-handey'
RAW.mkdir(parents=True, exist_ok=True)
HDR = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)', 'Accept': 'application/vnd.github+json'}


def get(url, timeout=15):
    req = urllib.request.Request(url, headers=HDR)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def save_blob(repo, path):
    if not path.lower().endswith(('.txt', '.dat')):
        return False
    url = 'https://raw.githubusercontent.com/' + repo + '/HEAD/' + urllib.parse.quote(path)
    try:
        data = get(url, 20)
    except Exception as e:
        print('raw fail:', repo, path, '->', e)
        return False
    if len(data) < 300:
        return False
    slug = re.sub(r'[^A-Za-z0-9]+', '-', repo.replace('/', '-') + '-' + path)[:60].strip('-')
    out = RAW / ('fortune-' + slug + '.txt')
    out.write_bytes(data)
    print('SAVED:', out.name, len(data), 'bytes')
    print('  head:', data[:240].decode(errors='ignore').replace('\n', ' | '))
    return True


def tree_paths(repo):
    url = 'https://api.github.com/repos/' + repo + '/git/trees/HEAD?recursive=1'
    try:
        data = json.loads(get(url).decode())
        return [t['path'] for t in data.get('tree', []) if t.get('type') == 'blob']
    except Exception as e:
        print('tree fail:', repo, '->', e)
        return []


PAT = re.compile(r'deep.?thought|handey', re.I)
got = 0

print('--- repo 1: forfaxx/fortune-files ---')
paths = tree_paths('forfaxx/fortune-files')
print('blobs:', len(paths))
hits = [p for p in paths if PAT.search(p)]
print('matches:', hits[:10])
for p in hits[:5]:
    if save_blob('forfaxx/fortune-files', p):
        got += 1
    if got >= 3:
        break

if got == 0:
    print('--- fallback repo search ---')
    try:
        q = urllib.parse.quote('deep thoughts handey fortune')
        res = json.loads(get('https://api.github.com/search/repositories?q=' + q, 15).decode())
        repos = [it['full_name'] for it in res.get('items', [])][:5]
        print('repos:', repos)
        for repo in repos:
            for p in [x for x in tree_paths(repo) if PAT.search(x)][:3]:
                if save_blob(repo, p):
                    got += 1
            if got:
                break
    except Exception as e:
        print('search fail:', e)

print('fortune files saved:', got)
