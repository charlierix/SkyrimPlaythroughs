import re, sys, datetime
from pathlib import Path
try:
    from bs4 import BeautifulSoup
except Exception:
    BeautifulSoup = None

BAD = ('http','www.','©','all rights','posted on','posted in','login','register','permalink','share this','like loading','related posts','post navigation','leave a','reply','originally posted','moderator','joined:','posts:','location:','read more','tags:','post subject','board index','print view','unread','jump to','faq','logout','the team','back to top','months ago','years ago','weeks ago','days ago','hours ago','minutes ago','edited by','quote:','view public profile','send a private','find more posts','add comment','page 1 of','](http','![')
FORUMGLYPHS = ('ᵁᵀᴵ','🔗')

def norm(t):
    return re.sub(r'\s+', ' ', t).strip().strip('"').strip()

def keep(t):
    if not (20 <= len(t) <= 650) or t.count(' ') < 3: return False
    low = t.lower()
    if any(b in low for b in BAD): return False
    if any(g in t for g in FORUMGLYPHS): return False
    return sum(c.isalpha() for c in t) / max(1, len(t)) >= 0.6

def extract(path):
    txt = Path(path).read_text(errors='ignore')
    p = Path(path)
    if p.suffix == '.txt':
        return [norm(re.sub(r'<[^>]+>', ' ', ln)) for ln in txt.splitlines()]
    elems, flat = [], []
    if BeautifulSoup is not None:
        s = BeautifulSoup(txt, 'html.parser')
        for t in s(['script','style','noscript','header','footer','nav','aside','form']):
            t.decompose()
        for e in s.find_all(['p','li','blockquote','dd','pre','td']):
            k = norm(e.get_text(' ', strip=True))
            if k: elems.append(k)
        flat = [norm(x) for x in s.get_text('\n').splitlines()]
    else:
        txt2 = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', txt, flags=re.S|re.I)
        for m in re.findall(r'<(?:p|li|blockquote|dd|pre|td)[^>]*>(.*?)</(?:p|li|blockquote|dd|pre|td)>', txt2, flags=re.S|re.I):
            k = norm(re.sub(r'<[^>]+>', ' ', m))
            if k: elems.append(k)
        flat = [norm(x) for x in re.sub(r'<[^>]+>', '\n', txt2).splitlines()]
    return elems + flat

def run(comedian):
    rawd = Path('raw') / comedian
    outd = Path('candidates') / comedian
    outd.mkdir(parents=True, exist_ok=True)
    seen = set(); total = 0; lines = []
    for f in sorted(rawd.iterdir()):
        if f.suffix == '.err' or not f.is_file() or f.stat().st_size < 200: continue
        per = []; sset = set()
        for c in extract(f):
            k = norm(c)
            if not keep(k): continue
            key = re.sub(r'[^a-z0-9]', '', k.lower())
            if not key or key in sset: continue
            sset.add(key); per.append(k)
            if key not in seen:
                seen.add(key); total += 1
        (outd / (f.stem + '.txt')).write_text('\n'.join(per) + '\n')
        lines.append(comedian + '/' + f.stem + ': ' + str(len(per)))
    lines.append('>> ' + comedian + ' unique across sources: ' + str(total))
    return lines

if __name__ == '__main__':
    comics = sys.argv[1:] or ['jack-handey','steven-wright','mitch-hedberg']
    stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    for c in comics:
        ls = run(c)
        print('\n'.join(ls)); print()
        with (Path('plans') / (c + '.md')).open('a') as fh:
            fh.write('\n## Re-extract (' + stamp + ')\n')
            for l in ls: fh.write('- ' + l + '\n')
