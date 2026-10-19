"""Build Appendix A (appendix/a-glossary.qmd) from docs/glossary.md.

Usage (from the repo root):  python3 tools/build_glossary.py [--report]

- Every row of docs/glossary.md, alphabetized, definition copied exactly (sense labels kept).
- "Defined in" chapter: the lowest-numbered chapter whose "### Key Terms" list names the term
  (items marked "(Ch. N)" or listed under "From Chapter N:" are cross-references and skipped);
  if no Key Terms list names it, the lowest chapter whose text bolds it (**term**).
  Other chapters that also list it as their own Key Term are shown as "also".
- Then a Turkish equivalents index (Türkçe column -> English term), in Turkish alphabetical order.
- --report prints duplicates, shared Turkish equivalents and the chapter-assignment fallbacks.

Rerun after merging new chapter handoffs into docs/glossary.md. Never edit a-glossary.qmd by hand.
"""
INCLUDE_TURKISH_INDEX = False
import glob
import re
import sys
import unicodedata
from collections import defaultdict

GLOSSARY = "docs/glossary.md"
OUT = "appendix/a-glossary.qmd"
REPORT = "--report" in sys.argv


def read_glossary():
    rows = []
    for line in open(GLOSSARY, encoding="utf8"):
        if not line.startswith("| "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 3 or cells[0] == "Term" or set(cells[0]) <= set("-:"):
            continue
        rows.append(tuple(cells))
    return rows


def strip_deep(s):
    """Remove 'Deep' markers inside parentheses: 'X (Deep)' -> 'X', 'X (text; Deep)' -> 'X (text)'."""
    def fix(m):
        parts = [p.strip() for p in re.split(r"[;,]", m.group(1))]
        keep = [p for p in parts if p.lower() != "deep" and p]
        if len(keep) == len(parts):
            return m.group(0)
        return f" ({', '.join(keep)})" if keep else ""
    return re.sub(r"\s*\(([^()]*)\)", fix, s).strip()


def norm(s):
    s = s.replace("*", "").replace("’", "'").replace("–", "-").strip().rstrip(".").lower()
    return re.sub(r"\s+", " ", strip_deep(s))


def parts(s):
    """full, base (before the first parenthesis), aliases inside the parenthesis."""
    full = norm(s)
    m = re.match(r"^(.*?)\s*\((.*)\)\s*$", full)
    if not m:
        return full, full, set()
    base, inner = m.group(1).strip(), m.group(2)
    return full, base, {p.strip() for p in re.split(r"[;,]", inner) if p.strip()}


def aliases(s):
    """Loose names for matching: base, 'base sense' joined, parenthesis parts, comma-split parts."""
    full, base, al = parts(s)
    out = {full, base} | al
    if al:
        out.add(base + " " + " ".join(sorted(al)))
    for piece in base.split(", "):
        out.add(piece.strip())
    return out


def chapter_files():
    out = {}
    for f in sorted(glob.glob("chapters/[0-9][0-9]-*.qmd")):
        out[int(f.split("/")[1][:2])] = f
    return out


def key_terms(text):
    m = re.search(r"^### Key Terms[^\n]*\n+(.+?)\n", text, flags=re.M)
    if not m:
        return []
    line = m.group(1)
    own, cross = line, ""
    cm = re.search(r"\.\s*From Chapter \d+:", line)
    if cm:
        own, cross = line[: cm.start()], line[cm.end():]
    items = []
    for it in own.split(" · "):
        it = re.sub(r"^\*Deep:\*\s*", "", it.strip()).strip()
        if not it:
            continue
        if re.search(r"\bCh\. \d+", it):  # "(Ch. 3)" or "(product feature, Ch. 3)": cross-reference
            continue
        items.append(it)
    return items


def assign_chapters(rows):
    chap = chapter_files()
    texts = {n: open(f, encoding="utf8").read() for n, f in chap.items()}
    kt = {n: [parts(i) for i in key_terms(t)] for n, t in texts.items()}
    gfulls = {parts(t)[0] for t, _, _ in rows}
    base_count = defaultdict(int)
    for t, _, _ in rows:
        base_count[parts(t)[1]] += 1
    aliases_item = {}
    for n, t in texts.items():
        for i in key_terms(t):
            aliases_item[(n, parts(i)[0])] = aliases(i)
    result, notes = {}, []
    for term, _, _ in rows:
        full, base, al = parts(term)
        exact, loose = set(), set()
        for n, items in kt.items():
            for ifull, ibase, ial in items:
                if full == ifull:
                    exact.add(n)
                elif ifull in gfulls:  # that item is another glossary entry (another sense)
                    continue
                elif al and ial and not (al & ial) and base == ibase:  # different sense labels
                    continue
                elif al and not ial and base_count[base] > 1:  # unlabeled item, several senses
                    continue
                elif aliases(term) & aliases_item[(n, ifull)]:
                    loose.add(n)
        found = exact | loose
        how = "key terms" if found else ""
        if not found:
            pat = re.compile(r"\*\*" + re.escape(base) + r"[^*]{0,40}\*\*", re.I)
            found = {n for n, t in texts.items() if pat.search(t)}
            how = "bold in text" if found else "not found"
        chs = sorted(found)
        result[term] = chs
        if how != "key terms" or (not exact and len(loose) > 1):
            notes.append((term, how, chs))
    return result, notes


# Hand overrides, each with its reason (keep this list short; prefer fixing the chapter's Key Terms).
OVERRIDES = {
    # Defined in Ch. 1 (section 1.x list of failure types, bold); Ch. 1's Key Terms list omits it.
    "Outdated information": [1, 4],
    # Ch. 10's Key Terms list "watermark (Deep)" without a sense label; the text sense is Ch. 10's.
    "Watermark (text; Deep)": [10],
    # Ch. 20 lists it as "Deep 20.A: extrapolation (in labor-market forecasts)", which the parser skips.
    "Extrapolation (in labor-market forecasts; Deep)": [20],
}

TR_ORDER = "aâbcçdefgğhıiîjklmnoöprsştuûüvyz"


def tr_key(s):
    s = re.sub(r"^\([^)]*\)\s*", "", s)  # "(Üretilen çıktıda) yanlılık" sorts under y
    s = s.replace("I", "ı").replace("İ", "i").lower()
    key = []
    for ch in s:
        if ch in TR_ORDER:
            key.append((0, TR_ORDER.index(ch)))
        elif ch.isalnum():
            key.append((1, ord(ch)))
        else:
            key.append((-1, 0))  # spaces and punctuation sort before letters ("Açık a…" < "Açıkl…")
    return key


def en_key(s):
    s = unicodedata.normalize("NFKD", s.replace("*", "")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9 ]", "", s.lower())


def ch_label(chs):
    if not chs:
        return "[VERIFY: chapter]"
    first = f"Ch. {chs[0]}"
    return first + (f" (also {', '.join(map(str, chs[1:]))})" if len(chs) > 1 else "")


def main():
    rows = read_glossary()
    chapters, notes = assign_chapters(rows)
    for t, chs in OVERRIDES.items():
        if t in chapters:
            chapters[t] = chs

    # duplicates: same normalized term twice
    seen = defaultdict(list)
    for t, d, tr in rows:
        seen[norm(t)].append(d)
    dups = {k: v for k, v in seen.items() if len(v) > 1}

    tr_map = defaultdict(list)
    for t, _, tr in rows:
        tr_map[tr].append(t)

    out = [
        "<!-- Generated by tools/build_glossary.py from docs/glossary.md. Do not edit by hand; rerun the script. -->",
        "",
        "# Glossary {#sec-appendix-a}",
        "",
        "Each entry gives the book's definition, word for word as it appears where the term is "
        "defined, and the chapter that defines it (\"also\" marks other chapters that list the term "
        "among their Key Terms). Labels in parentheses, such as *(of a model)* or *(Deep)*, "
        "separate different senses of a word or mark a term from an optional Deep section.",
        "",
    ]
    letter = None
    for t, d, tr in sorted(rows, key=lambda r: en_key(r[0])):
        first = en_key(t)[:1].upper()
        if first != letter:
            letter = first
            out += [f"## {letter} {{.unnumbered .unlisted}}", ""]
        out += [f"**{t}** · {ch_label(chapters[t])}", f":   {d}", ""]

    # The book is ASCII-only (author's rule, 2026-10-19); the Turkish index is kept for a
    # future Turkish edition and is off for this one.
    if INCLUDE_TURKISH_INDEX:
      out += [
        "## Turkish Equivalents Index {#sec-appendix-a-turkish .unnumbered}",
        "",
        "*Türkçe karşılıklar dizini.* Each Turkish equivalent points to the English term above, "
        "for readers of the planned Turkish edition.",
        "",
        "| Türkçe | English term |",
        "|------------------|------------------|",
    ]
      for tr in sorted(tr_map, key=tr_key):
        out.append(f"| {tr} | {'; '.join(sorted(tr_map[tr], key=en_key))} |")
    out.append("")
    open(OUT, "w", encoding="utf8").write("\n".join(out))
    print(f"wrote {OUT}: {len(rows)} terms, {len(tr_map)} Turkish entries")

    if REPORT:
        print("\n== duplicate terms")
        for k, v in dups.items():
            print(f"  {k}: {len(v)} rows; definitions {'identical' if len(set(v)) == 1 else 'DIFFER'}")
        print("\n== Turkish equivalents shared by more than one term")
        for tr, ts in tr_map.items():
            if len(ts) > 1:
                print(f"  {tr}: {ts}")
        print("\n== chapter assignment notes (fallback or several loose matches)")
        for t, how, chs in notes:
            print(f"  {t}: {how} -> {chs}")


if __name__ == "__main__":
    main()
