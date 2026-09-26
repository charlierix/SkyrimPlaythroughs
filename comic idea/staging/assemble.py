import re, datetime
from pathlib import Path
try:
    from bs4 import BeautifulSoup
except Exception:
    BeautifulSoup = None

STAGE = Path(__file__).resolve().parent
ROOT = STAGE.parent
RAW = STAGE / 'raw'
CAND = STAGE / 'candidates'
PLANS = STAGE / 'plans'

CHROME = [
    'skip to content', 'buzzfeed homepage', 'buzzfeed tasty', 'best of the internet',
    'straight to your inbox', 'make a quiz', 'huffpost news', 'stories that matter',
    'sign in', 'log in', 'sign up', 'create account', 'have an account', 'forgot password',
    'newsletter', 'subscribe', 'follow us', 'share this', 'tweet this', 'post navigation',
    'related posts', 'post comment', 'leave a', 'posted on', 'posted in', 'permalink',
    'read more', 'next post', 'previous post', 'recent posts', 'proudly powered',
    'search for', 'search this', 'about us', 'contact us', 'all rights reserved',
    'privacy policy', 'terms of use', 'terms of service', 'cookie policy', 'advertise',
    'sponsored', 'read next', 'more from', 'click here', 'enter your email',
    'quotes toggle', 'toggle quotes', 'subsection', 'switch to legacy', 'external links',
    'further reading', 'see also', 'edit source', 'view history', 'retrieved',
    'was an american', 'is an american', 'academy award', 'stand-up comic known',
    'users online', 'projects of the month', 'open topic', 'united-ti', 'minecraft',
    'cemetech', 'board index', 'the team', 'view unanswered', 'view active',
    'mark forums read', 'who is online', 'advanced search', 'quick links', 'print view',
    'jump to', 'back to top', 'top of page', 'powered by', 'originally posted',
    'quote from', 'view public profile', 'send a private', 'find more posts',
    'last edited', 'edited by', 'reply with quote', 'view full version', 'page 1 of',
    'crossposted', 'hide report', 'report save', 'save report', 'give award',
    'no comments', 'comments share', 'moderator', 'joined:', 'posts:', 'location:',
    'http', 'www.', 'wikiquote', 'wikipedia', 'cinemablend', 'buzzfeed', 'freeology',
    'gcfl', 'quotefancy', 'goodreads', 'brainyquote', 'azquotes', 'reddit',
]
FORUM_GLYPHS = ('ᵁᵀᴵ', '🔗')
TERMINAL = re.compile(r'[.!?…"\'”’]$')
TOC_RE = re.compile(r'^\d+(\.\d+)*\s+[A-Z]')
NUM_RE = re.compile(r'^\d{1,3}[.)]\s+')


def key(t):
    return re.sub(r'[^a-z0-9]', '', t.lower())


def is_junk(t):
    if not (15 <= len(t) <= 800):
        return True
    words = t.split()
    if len(words) < 4 and not (len(t) >= 18 and t[-1] in '.!?' ):
        return True
    low = t.lower()
    if any(b in low for b in CHROME):
        return True
    if any(g in t for g in FORUM_GLYPHS):
        return True
    if re.search(r'\(\s*born', low):
        return True
    if TOC_RE.match(t):
        return True
    alpha = sum(c.isalpha() for c in t) / max(1, len(t))
    if alpha < 0.55:
        return True
    if len(t) <= 45 and len(words) <= 6 and t[-1] not in '.!?':
        return True
    return False


def flat_join(soup):
    lines = []
    for l in soup.get_text('\n').splitlines():
        l = re.sub(r'\s+', ' ', l).strip()
        if not l or len(l) <= 3:
            continue
        low = l.lower()
        if any(b in low for b in CHROME) or any(g in l for g in FORUM_GLYPHS):
            continue
        lines.append(l)
    out, buf = [], ''
    for l in lines:
        buf = (buf + ' ' + l).strip() if buf else l
        if TERMINAL.search(l):
            out.append(buf)
            buf = ''
    if buf:
        out.append(buf)
    return out


def html_flat_lines(txt):
    txt2 = re.sub(r'<(script|style|noscript)[^>]*>.*?</\1>', ' ', txt, flags=re.S | re.I)
    lines = []
    for x in re.sub(r'<[^>]+>', '\n', txt2).splitlines():
        k = re.sub(r'\s+', ' ', x).strip()
        if len(k) > 3:
            lines.append(k)
    return lines


def extract_segments(f, era):
    txt = f.read_text(errors='ignore')
    if f.suffix == '.txt':
        return [l.strip() for l in txt.splitlines() if l.strip()]
    if BeautifulSoup is not None:
        soup = BeautifulSoup(txt, 'html.parser')
        for t in soup(['script', 'style', 'noscript', 'header', 'footer', 'nav', 'aside',
                       'form', 'svg', 'button', 'iframe']):
            t.decompose()
        if era:
            return flat_join(soup)
        segs = []
        for e in soup.find_all(['p', 'li', 'blockquote', 'dd', 'pre', 'td']):
            k = re.sub(r'\s+', ' ', e.get_text(' ', strip=True)).strip()
            if k:
                segs.append(k)
        segs += flat_join(soup)
        return segs
    flat = html_flat_lines(txt)
    if era:
        lines = []
        for l in flat:
            low = l.lower()
            if any(b in low for b in CHROME) or any(g in l for g in FORUM_GLYPHS):
                continue
            lines.append(l)
        out, buf = [], ''
        for l in lines:
            buf = (buf + ' ' + l).strip() if buf else l
            if TERMINAL.search(l):
                out.append(buf)
                buf = ''
        if buf:
            out.append(buf)
        return out
    return flat


SOURCES = {
    'jack-handey': [
        ('thefirsthundred', 'thefirsthundred.wordpress.com ("The First Hundred")',
         'https://thefirsthundred.wordpress.com/2009/01/23/jack-handy-deep-thoughts/'),
        ('wikiquote', 'Wikiquote', 'https://en.wikiquote.org/wiki/Jack_Handey'),
        ('gcfl', 'GCFL.net archive', 'https://gcfl.net/archive.php?funny=981'),
        ('cemetech', 'Cemetech forum thread (user-posted collection)',
         'https://www.cemetech.net/uti/t8395-deep-thoughts-by-jack-handy'),
    ],
    'steven-wright': [
        ('wikiquote', 'Wikiquote', 'https://en.wikiquote.org/wiki/Steven_Wright'),
        ('cmu', 'CMU canonical list (N. Papernick)',
         'https://www.contrib.andrew.cmu.edu/~norm/SteveQuotes.html'),
        ('colorado', 'CU Boulder list', 'https://spot.colorado.edu/~huemer/wright.htm'),
        ('mcom', 'Netscape-era list', 'http://home.mcom.com/people/mtoy/steven_wright.html'),
        ('whynot100', 'The Why Not 100',
         'http://thewhynot100.blogspot.com/2014/02/72-smart-steven-wright-one-liners.html'),
        ('standupclinic', 'Stand Up Comedy Clinic',
         'https://www.standupcomedyclinic.com/65-funny-one-liners-by-steven-wright/'),
        ('freeology', 'Freeology', 'https://freeology.com/fun/13-one-liners-steven-wright/'),
    ],
    'mitch-hedberg': [
        ('wikiquote', 'Wikiquote', 'https://en.wikiquote.org/wiki/Mitch_Hedberg'),
        ('buzzfeed', 'BuzzFeed complete ranking',
         'https://www.buzzfeed.com/mrloganrhoades/a-complete-ranking-of-almost-every-single-mitch-hedberg-joke'),
        ('cinemablend', 'CinemaBlend',
         'https://www.cinemablend.com/television/hilarious-mitch-hedberg-jokes'),
        ('eve-forum', 'EVE Online forum archive',
         'https://forums-archive.eveonline.com/topic/361761'),
        ('funny2', 'Funny2', 'http://www.funny2.com/hedberg.htm'),
    ],
}
TITLE = {
    'jack-handey': 'Jack Handey — Deep Thoughts',
    'steven-wright': 'Steven Wright — One-Liners',
    'mitch-hedberg': 'Mitch Hedberg — One-Liners',
}
EXCLUDE = {'jack-handey': {'adminjitsu'}}
ERA = {'steven-wright': {'cmu', 'colorado', 'mcom'}}

stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
for comedian in ['jack-handey', 'steven-wright', 'mitch-hedberg']:
    srcs = SOURCES[comedian]
    valid = {s for s, _, _ in srcs} - EXCLUDE.get(comedian, set())
    for stale in (CAND / comedian).glob('*.txt'):
        if stale.stem not in valid:
            stale.unlink()
    seen, sections, total = set(), [], 0
    for stem, label, url in srcs:
        if stem in EXCLUDE.get(comedian, set()):
            continue
        f = RAW / comedian / (stem + '.html')
        if not f.exists():
            continue
        loc, lseen = [], set()
        for seg in extract_segments(f, stem in ERA.get(comedian, set())):
            k = NUM_RE.sub('', seg).strip(' "\'“”').strip()
            k = re.sub(r'\s+', ' ', k)
            if not k or is_junk(k):
                continue
            kk = key(k)
            if kk and kk not in lseen:
                lseen.add(kk)
                loc.append(k)
        (CAND / comedian / (stem + '.txt')).write_text('\n'.join(loc) + '\n')
        per = []
        for k in loc:
            kk = key(k)
            if kk not in seen:
                seen.add(kk)
                per.append(k)
        if per:
            sections.append((label, url, per))
            total += len(per)
        print(comedian + '/' + stem + ': local ' + str(len(loc)) + ', new ' + str(len(per)))
    lines = ['# ' + TITLE[comedian], '',
             '_Raw source-material compilation gathered 2026-09-22. One joke per line; '
             'text reproduced as published on each listed source (fan lists may contain '
             'minor transcription variants). Not yet formatted for SkyrimNet._', '']
    for label, url, per in sections:
        lines += ['## ' + label, '', 'Source: ' + url, '']
        lines += per + ['']
    lines.append('Total unique: ' + str(total))
    out = ROOT / (comedian + '.md')
    out.write_text('\n'.join(lines) + '\n')
    print('>> ' + comedian + ' FINAL: ' + str(total) + ' unique -> ' + str(out))
    with (PLANS / (comedian + '.md')).open('a') as fh:
        fh.write('\n## Assembly (' + stamp + ')\n')
        fh.write('- final file: ' + str(out) + ' | unique: ' + str(total) + '\n')
        if comedian == 'jack-handey':
            fh.write('- fortune-file hunt dead end: forfaxx/fortune-files 404, '
                     'renamed forfaxx/fortune has no deep-thoughts blob\n')
            fh.write('- adminjitsu excluded from final (mixed fortune content, attribution risk)\n')
