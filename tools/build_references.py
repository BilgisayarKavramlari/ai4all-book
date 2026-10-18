"""Build the whole-book bibliography (appendix/references.qmd) from every "## References" section.

Usage (from the repo root):  python3 tools/build_references.py [--report]

Reads the "## References" section of index.qmd, front/*.qmd, chapters/*.qmd and appendix/*.qmd
(except the generated references.qmd itself). Each chapter keeps its own list; this script only
compiles them. Steps:
  1. Split each section into entries (one paragraph each). An entry broken over two paragraphs
     (authors or "(year)." alone, then the rest) is rejoined and reported.
  2. Exact duplicates (after normalizing whitespace, italics, quotes and dashes) are merged.
  3. Near duplicates are merged: same DOI or URL, or same first author and year with very similar
     text. The most complete version (the longest) is kept; every merge with differing text is
     reported as a conflict so the chapter lists can be aligned.
  4. Same-author, same-year letters (2025a, 2025b) are reassigned for the whole-book list, APA style
     (ordered by title); changed letters are reported (in-text letters stay per chapter).
  5. Entries are sorted APA style (author, then year: n.d. first, then by year) and each is followed by
     the chapters (or other sections) that cite it.
Rerun after chapters change. Never edit references.qmd by hand.
"""
import difflib
import glob
import re
import sys
import unicodedata
from collections import defaultdict

OUT = "appendix/references.qmd"
REPORT = "--report" in sys.argv
NEAR = 0.85  # similarity threshold (text without URLs) for same first author + year
TITLE_NEAR = 0.9  # ... and the titles (first 60 characters after the date) must match this closely


def sources():
    files = ["index.qmd"] + sorted(glob.glob("front/*.qmd")) + sorted(glob.glob("chapters/*.qmd")) \
        + sorted(f for f in glob.glob("appendix/*.qmd") if not f.endswith("references.qmd"))
    for f in files:
        name = f.split("/")[-1]
        if f.startswith("chapters/"):
            label = ("ch", int(name[:2]))
        elif f.startswith("appendix/"):
            m = re.match(r"([a-z])-", name)
            label = ("app", m.group(1).upper() if m else name)
        else:
            first = open(f, encoding="utf8").readline()
            label = ("front", re.sub(r"\s*\{.*\}\s*$", "", first.lstrip("# ").strip()))
        yield f, label


YEAR = r"\((\d{4})([a-z]?)(?=[,)\s])|\((n\.d\.)(?:-([a-z]))?\)"


def split_entries(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    paras = [re.sub(r"\s*\n\s*", " ", p.strip()) for p in re.split(r"\n\s*\n", text) if p.strip()]
    out, joins = [], []
    for p in paras:
        if out:
            prev = out[-1]
            # rejoin "Authors (2015)." + "Title. Journal ..." and "Authors" + "(2023). Title ..."
            ends_with_year = (re.search(r"\((\d{4}[a-z]?|n\.d\.)[^)]*\)\.$", prev)
                              and len(re.findall(YEAR, prev)) == 1 and not prev.startswith("*")
                              and not re.search(YEAR, p) and not p.startswith("*"))
            authors_only = not re.search(YEAR, prev) and re.match(r"^" + YEAR, p)
            if ends_with_year or authors_only:
                out[-1] = prev + " " + p
                joins.append(out[-1][:90])
                continue
        out.append(p)
    return out, joins


def norm(s):
    s = s.replace("*", "").replace("\\", "")
    s = s.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = s.replace("—", "-").replace("–", "-").replace(" ", " ")
    s = re.sub(r"\[VERIFY[^\]]*\]", "", s)
    s = re.sub(r"\s+", " ", s).strip().rstrip(".").lower()
    return s


def ids(entry):
    out = set()
    for m in re.finditer(r"https?://\S+", entry):
        u = m.group(0).rstrip(".,;)]").lower()
        u = re.sub(r"^https?://(www\.|dx\.)?", "", u).rstrip("/")
        eli = re.search(r"/eli/([a-z]+/\d{4}/\d+)", u)  # EU legislation: one ELI, several hosts
        arx = re.search(r"arxiv[./:](?:abs/|org/abs/)?(\d{4}\.\d{4,5})", u)
        if eli:
            out.add("eli:" + eli.group(1))
        elif arx:
            out.add("arxiv:" + arx.group(1))
        elif u.startswith("doi.org/"):
            out.add(u)
        elif "/" in u and len(u.split("/", 1)[1]) > 3:  # a page, not a bare home page
            out.add(u)
    return out


def author_year(entry):
    m = re.search(YEAR, entry)
    if not m:
        y = re.findall(r"\b(1[89]\d{2}|20\d{2})\b", entry)
        return norm(re.split(r"[,(]", entry)[0]), (y[0] if y else ""), "", None
    year = m.group(1) or m.group(3)
    letter = m.group(2) or m.group(4) or ""
    return norm(entry[: m.start()]), year, letter, m


def first_author(entry):
    a = norm(entry)
    return re.split(r"[,.(]", a)[0].strip()


def title_of(entry):
    _, _, _, m = author_year(entry)
    if not m:
        return norm(entry)[:80]
    rest = re.sub(r"^[^)]*\)\.?\s*", "", entry[m.start():])
    rest = norm(re.sub(r"https?://\S+", "", rest))
    return re.split(r"\.\s", rest)[0][:60]  # the title: first sentence after the date


def no_urls(entry):
    return norm(re.sub(r"https?://\S+", "", entry))


def strip_letter(entry):
    return re.sub(r"\((\d{4})[a-z](?=[,)\s])", r"(\1", re.sub(r"\(n\.d\.-[a-z]\)", "(n.d.)", entry), count=1)


MONTHS = {m: i for i, m in enumerate(
    "january february march april may june july august september october november december".split(), 1)}


def within_year_key(entry):
    """APA order for the same author and year: year-only first, then specific dates in
    chronological order, then title (ignoring a leading A, An or The)."""
    _, _, _, m = author_year(entry)
    if not m:
        return (0, 0, 0, ascii_key(entry))
    close = entry.find(")", m.start())
    inside = entry[m.start() + 1: close] if close > 0 else ""
    dm = re.search(r",\s*([A-Z][a-z]+)\.?\s*(\d{1,2})?", inside)
    month = MONTHS.get(dm.group(1).lower(), 0) if dm else 0
    day = int(dm.group(2)) if dm and dm.group(2) else 0
    title = ascii_key(entry[close + 1:] if close > 0 else entry)
    title = re.sub(r"^\s*(a|an|the)\s+", "", title.strip())
    return (1 if month else 0, month, day, title)


def ascii_key(s):
    s = unicodedata.normalize("NFKD", s.replace("*", "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]", "", s)


def cite_label(labels):
    chs = sorted(n for k, n in labels if k == "ch")
    other = sorted({(k, str(n)) for k, n in labels if k != "ch"})
    parts = []
    if chs:
        parts.append(("Ch. " if len(chs) == 1 else "Ch. ") + ", ".join(map(str, chs)))
    for k, n in other:
        parts.append(f"Appendix {n}" if k == "app" else n)
    return "Cited in " + "; ".join(parts) + "."


def main():
    raw, joins_all = [], []
    for f, label in sources():
        t = open(f, encoding="utf8").read()
        m = re.search(r"^## References[^\n]*\n(.*?)(?=^#{1,2} |\Z)", t, flags=re.S | re.M)
        if not m:
            continue
        entries, joins = split_entries(m.group(1))
        joins_all += [(label, j) for j in joins]
        raw += [(e, label) for e in entries]

    # 1-2. exact duplicates
    groups = {}
    for e, label in raw:
        k = norm(strip_letter(e))
        g = groups.setdefault(k, {"versions": defaultdict(set), "labels": set()})
        g["versions"][e].add(label)
        g["labels"].add(label)
    exact_unique = len(groups)

    # 3. near duplicates (union-find over exact groups)
    keys = list(groups)
    parent = {k: k for k in keys}

    def find(k):
        while parent[k] != k:
            parent[k] = parent[parent[k]]
            k = parent[k]
        return k

    rep = {k: max(groups[k]["versions"], key=len) for k in keys}
    by_id = defaultdict(list)
    for k in keys:
        for i in ids(rep[k]):
            by_id[i].append(k)
    reasons = {}
    for i, ks in by_id.items():
        for k in ks[1:]:
            if find(k) != find(ks[0]):
                parent[find(k)] = find(ks[0])
                reasons[(ks[0], k)] = f"same identifier {i}"
    by_fa = defaultdict(list)
    for k in keys:
        a, y, _, _ = author_year(rep[k])
        by_fa[(first_author(rep[k]), y)].append(k)
    close_unmerged = []
    for (fa, y), ks in by_fa.items():
        for i in range(len(ks)):
            for j in range(i + 1, len(ks)):
                r = difflib.SequenceMatcher(None, no_urls(strip_letter(rep[ks[i]])),
                                            no_urls(strip_letter(rep[ks[j]]))).ratio()
                tr = difflib.SequenceMatcher(None, title_of(rep[ks[i]]), title_of(rep[ks[j]])).ratio()
                if (r >= NEAR and tr >= TITLE_NEAR) or (tr >= 0.97 and r >= 0.7):
                    if find(ks[j]) != find(ks[i]):
                        parent[find(ks[j])] = find(ks[i])
                        reasons[(ks[i], ks[j])] = f"same first author and year, similarity {r:.2f}"
                elif r >= 0.7:
                    close_unmerged.append((r, ks[i], ks[j]))

    merged = defaultdict(lambda: {"versions": defaultdict(set), "labels": set()})
    for k in keys:
        m = merged[find(k)]
        for v, ls in groups[k]["versions"].items():
            m["versions"][v] |= ls
        m["labels"] |= groups[k]["labels"]

    final, conflicts = [], []
    for m in merged.values():
        versions = m["versions"]
        keep = max(versions, key=lambda v: (len(norm(v)), len(versions[v])))
        distinct = {norm(strip_letter(v)) for v in versions}
        if len(distinct) > 1:
            conflicts.append((keep, {v: sorted(map(str, (n for _, n in ls))) for v, ls in versions.items()}))
        final.append({"text": keep, "labels": m["labels"]})

    # 4. reassign same-author same-year letters
    letter_changes = []
    bucket = defaultdict(list)
    for r in final:
        a, y, _, _ = author_year(r["text"])
        bucket[(a, y)].append(r)
    for (a, y), rs in bucket.items():
        rs.sort(key=lambda r: within_year_key(r["text"]))
        for idx, r in enumerate(rs):
            _, _, old, m = author_year(r["text"])
            if not m:
                continue
            new = chr(ord("a") + idx) if len(rs) > 1 else ""
            if new != old:
                t = r["text"]
                if m.group(3):  # n.d.
                    rep_ = f"(n.d.-{new})" if new else "(n.d.)"
                    t = t[: m.start()] + rep_ + t[m.end():]
                else:
                    t = t[: m.start()] + f"({m.group(1)}{new}" + t[m.end():]
                letter_changes.append((r["text"][:80], old or "-", new or "-"))
                r["text"] = t

    # 5. APA sort: author string, then n.d. before years, then year, then letter/title
    def sort_key(r):
        a, y, _, _ = author_year(r["text"])
        ykey = (0, 0) if y == "n.d." else ((1, int(y)) if y.isdigit() else (2, 0))
        return (ascii_key(a), ykey, within_year_key(r["text"]))

    final.sort(key=sort_key)
    lines = [
        "<!-- Generated by tools/build_references.py from the chapters' References sections. Do not edit by hand; rerun the script. -->",
        "",
        "# References {#sec-appendix-references .unnumbered}",
        "",
        "This list combines the reference lists at the end of each chapter. Each entry ends with the "
        "chapters that cite it. Within a chapter, in-text citations follow that chapter's own list, "
        "so a year letter (such as 2025a) can differ between a chapter's list and this one.",
        "",
    ]
    for r in final:
        lines += [f"{r['text']} *{cite_label(r['labels'])}*", ""]
    open(OUT, "w", encoding="utf8").write("\n".join(lines))
    print(f"wrote {OUT}: {len(raw)} entries read, {exact_unique} after exact dedupe, "
          f"{len(final)} after near-duplicate merge")

    if REPORT:
        print(f"\n== entries rejoined (broken over two paragraphs): {len(joins_all)}")
        for label, j in joins_all:
            print(f"  {label}: {j}")
        print(f"\n== merged groups whose versions differ (kept the longest): {len(conflicts)}")
        for keep, vs in conflicts:
            print(f"  KEPT: {keep[:150]}")
            for v, chs in vs.items():
                print(f"     [{', '.join(chs)}] {v[:150]}")
        print(f"\n== close pairs NOT merged (0.70 <= similarity < {NEAR}): {len(close_unmerged)}")
        for r, a, b in sorted(close_unmerged, reverse=True):
            if find(a) != find(b):
                print(f"  {r:.2f}\n     {rep[a][:140]}\n     {rep[b][:140]}")
        print(f"\n== year letters changed for the whole-book list: {len(letter_changes)}")
        for t, o, n in letter_changes:
            print(f"  {o} -> {n}: {t}")


if __name__ == "__main__":
    main()
