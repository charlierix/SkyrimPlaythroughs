import html, re
from pathlib import Path

STAGE = Path(__file__).resolve().parent
ROOT = STAGE.parent
PLANS = STAGE / 'plans'

JUNK = [
    'oh my gosh', 'do another page', 'wholeheartedly', 'my favorite one',
    'thanks oh, wait', 'mizner', 'the first hundred', 'jack handy deep thoughts |',
    'do you believe in gosh', 'strategic grill locations', 'just for laughs',
    'unenthusiastically', 'intesting', 'darth android', 'cracked me up',
]


def structural(t):
    return (not t.strip() or t.startswith('#') or t.startswith('Source:')
            or t.startswith('_') or t.startswith('Total unique'))


def is_junk(t):
    low = t.lower()
    if any(j in low for j in JUNK):
        return True
    if t.startswith('[') and t.endswith(']'):
        return True
    return False


def key(t):
    return re.sub(r'[^a-z0-9]', '', t.lower())


for comedian in ['jack-handey', 'steven-wright', 'mitch-hedberg']:
    p = ROOT / (comedian + '.md')
    lines = p.read_text(encoding='utf-8').splitlines()
    out, seen, kept, removed = [], set(), 0, 0
    for ln in lines:
        if structural(ln):
            out.append(ln)
            continue
        t = html.unescape(html.unescape(ln))
        t = re.sub(r'\s+', ' ', t).strip()
        if not t or is_junk(t):
            removed += 1
            continue
        kk = key(t)
        if kk in seen:
            removed += 1
            continue
        seen.add(kk)
        out.append(t)
        kept += 1
    out = [l for l in out if not l.startswith('Total unique')]
    while out and out[-1] == '':
        out.pop()
    out.append('')
    out.append('Total unique: ' + str(kept))
    p.write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(comedian + ': kept ' + str(kept) + ', removed/merged ' + str(removed))
    with (PLANS / (comedian + '.md')).open('a') as fh:
        fh.write('- postprocess: entities unescaped, comment/album junk filtered, '
                 'cross-section dupes merged; final unique: ' + str(kept) + '\n')
