"""Check an instruction document against the Simplified Technical English limits.
Usage: python3 ste_check.py file.md
Reports: sentences over the word limit (20 in numbered or bulleted steps, 25 elsewhere), dashes, banned words.
Text inside code fences, block quotes that start with '>' and table rows is checked with the 25-word limit only."""
import re, sys
BANNED = ['utilize','utilise','leverage','ensure','facilitate','initiate','terminate','approximately','prior to',
          'subsequent to','in order to','attempt','additional','commence','modify','require','verify','obtain',
          'perform','via','due to the fact','in the event that','a number of','basically','essentially']
def sentences(t):
    t = re.sub(r'https?://\S+', 'URL', t)
    t = re.sub(r'"[^"]{0,400}"', 'QUOTE', t)
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"\[(])', t) if s.strip()]
def main(p):
    lines = open(p).read().split('\n'); fence = False; bad = []; total = 0; dash = 0; banned = {}
    for n, l in enumerate(lines, 1):
        if l.strip().startswith('```'): fence = not fence; continue
        if fence: continue
        if '\u2014' in l or '\u2013' in l: dash += 1
        if l.startswith('#') or not l.strip(): continue
        is_table = l.strip().startswith('|'); is_quote = l.strip().startswith('>')
        is_step = bool(re.match(r'\s*(\d+\.|[-*])\s', l))
        body = re.sub(r'^\s*(\d+\.|[-*]|>)\s*', '', l)
        cells = [c for c in body.split('|') if c.strip()] if is_table else [body]
        for c in cells:
            for s in sentences(c):
                w = len(re.findall(r"[A-Za-z0-9'/\-]+", s)); total += 1
                lim = 20 if (is_step and not is_table and not is_quote) else 25
                if w > lim: bad.append((n, w, lim, s[:110]))
            low = c.lower()
            for b in BANNED:
                if re.search(r'\b' + re.escape(b) + r'\b', low): banned[b] = banned.get(b, 0) + 1
    print(f'{p}: {len(lines)} lines, {total} sentences, {len(bad)} over the limit, {dash} lines with dashes')
    for n, w, lim, s in bad[:60]: print(f'  line {n}: {w} words (limit {lim}): {s}')
    if banned: print('  words to replace:', ', '.join(f'{k} x{v}' for k, v in sorted(banned.items())))
if __name__ == '__main__':
    for f in sys.argv[1:]: main(f)
