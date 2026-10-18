"""Build Appendix G (appendix/g-case-index.qmd) from cases/index.csv.

Usage (from the repo root):  python3 tools/build_case_index.py [--csv-only]

Source of truth: cases/index.csv (columns id,title,year,chapter,field,failure_type,outcome,...).
Case files cases/CNN-*.md whose id is not yet in the CSV are added from the file's own
first two lines ("# Case: title (year)" and "Chapter: … · Field: … · Failure label: … · Outcome: …")
and flagged with a dagger, so the index is complete while the CSV catches up.
Pass --csv-only to leave them out. Rerun after cases/index.csv changes; never edit the .qmd by hand.

Tables: cases by chapter (lookup + full table with all seven columns), by field, by failure type
(branches of the Failure Taxonomy Tree, Chapter 4; a case can sit on more than one branch).
"""
import csv
import glob
import re
import sys

CSV = "cases/index.csv"
OUT = "appendix/g-case-index.qmd"
CSV_ONLY = "--csv-only" in sys.argv

BRANCHES = [
    ("Hallucination", r"\bhallucination\b"),
    ("Bias", r"(?<!automation )\bbias\b"),
    ("Context loss", r"\bcontext loss\b"),
    ("Overconfidence", r"\boverconfidence\b"),
    ("Security vulnerability", r"\bsecurity vulnerability\b"),
    ("Other (including misuse)", r"^other\b|[;+,]\s*other\b|\bother leaf\b|\bother \("),
]
NOT_ON_TREE = "Not on the tree"


def clean(s):
    s = (s or "").replace("**", "").strip()
    return re.sub(r"\s+", " ", s)


def cell(s):
    return clean(s).replace("|", "\\|")


def chapters_of(s):
    return [int(x) for x in re.findall(r"\d+", s.split("(")[0])] if s else []


def from_csv():
    rows = []
    with open(CSV, encoding="utf8", newline="") as f:
        for r in csv.DictReader(f):
            if not r.get("id"):
                continue
            rows.append({
                "id": r["id"].strip(), "title": clean(r["title"]), "year": clean(r["year"]),
                "chapters": [int(x) for x in re.findall(r"\d+", r["chapter"])],
                "field": clean(r["field"]), "failure": clean(r["failure_type"]),
                "outcome": clean(r["outcome"]), "from_file": False,
            })
    return rows


def from_case_files(known):
    rows = []
    for path in sorted(glob.glob("cases/C[0-9][0-9]-*.md")):
        cid = path.split("/")[-1][:3]
        if cid in known:
            continue
        lines = open(path, encoding="utf8").read().split("\n")
        head = lines[0]
        meta = next((l for l in lines[1:6] if l.startswith("Chapter:")), "")
        m = re.match(r"^# Case:\s*(.+?)\s*\(([^()]*\d{4}[^()]*)\)\s*$", head)
        title, year = (m.group(1), m.group(2)) if m else (head.replace("# Case:", "").strip(), "")
        fields = {}
        for part in re.split(r"\s+·\s+", meta):
            k, _, v = part.partition(":")
            fields[k.strip().lower()] = v.strip()
        rows.append({
            "id": cid, "title": clean(title), "year": clean(year),
            "chapters": chapters_of(fields.get("chapter", "")),
            "field": clean(fields.get("field", "")), "failure": clean(fields.get("failure label", "")),
            "outcome": clean(fields.get("outcome", "")), "from_file": True,
        })
    return rows


def field_group(f):
    g = re.split(r"\s*[/(]\s*", f)[0].strip()
    return g[:1].upper() + g[1:] if g else "Unspecified"


def branches_of(label):
    low = label.lower()
    found = [name for name, pat in BRANCHES if re.search(pat, low)]
    if not found or re.search(r"\bnone\b|not applicable|^copyright", low):
        found.append(NOT_ON_TREE)
    return found


def ch_str(chs):
    return ", ".join(map(str, chs)) if chs else "—"


def ident(r):
    return r["id"] + ("†" if r["from_file"] else "")


def main():
    rows = from_csv()
    if not CSV_ONLY:
        rows += from_case_files({r["id"] for r in rows})
    rows.sort(key=lambda r: (min(r["chapters"] or [99]), r["id"]))
    flagged = [r["id"] for r in rows if r["from_file"]]

    out = [
        "<!-- Generated from cases/index.csv by tools/build_case_index.py. Do not edit by hand; rerun the script. -->",
        "",
        "# Case Index {#sec-appendix-g}",
        "",
        f"This index lists the {len(rows)} documented cases the book analyzes: by chapter, by field and "
        "by failure type. The failure label follows the Failure Taxonomy Tree (Chapter 4): *documented* "
        "means the record shows the branch's defining feature, *inferred* means it does not; "
        "\"chain link\" refers to the failure-to-harm chain. Cases in which no output was wrong "
        "(input-side harms, policies, training-data disputes, positive results) are not placed on the tree.",
        "",
    ]
    if flagged:
        out += [
            "† Taken from the case file; not yet in the book's case register (cases/index.csv).",
            "",
        ]

    # ---- by chapter
    out += ["## Cases by Chapter {#sec-appendix-g-chapter .unnumbered}", ""]
    by_ch = {}
    for r in rows:
        for c in r["chapters"]:
            by_ch.setdefault(c, []).append(ident(r))
    out += ["| Chapter | Cases |", "|----|------------------------------|"]
    for c in sorted(by_ch):
        out.append(f"| {c} | {', '.join(sorted(by_ch[c]))} |")
    out += ["", "| ID | Title | Year | Chapter(s) | Field | Failure label | Outcome |",
            "|----|------------------|-----|-----|----------|----------------------------|--------|"]
    for r in rows:
        out.append(f"| {ident(r)} | {cell(r['title'])} | {cell(r['year'])} | {ch_str(r['chapters'])} | "
                   f"{cell(r['field'])} | {cell(r['failure'])} | {cell(r['outcome'])} |")
    out.append("")

    # ---- by field
    out += ["## Cases by Field {#sec-appendix-g-field .unnumbered}", "",
            "| Field | ID | Title | Year | Chapter(s) | Outcome |",
            "|------------|----|---------------------------|-----|-----|----------|"]
    for r in sorted(rows, key=lambda r: (field_group(r["field"]).lower(), r["id"])):
        out.append(f"| {cell(r['field'])} | {ident(r)} | {cell(r['title'])} | {cell(r['year'])} | "
                   f"{ch_str(r['chapters'])} | {cell(r['outcome'])} |")
    out.append("")

    # ---- by failure type
    out += ["## Cases by Failure Type {#sec-appendix-g-failure .unnumbered}", "",
            "A case appears once for each branch its label names; \"Not on the tree\" collects input-side harms, "
            "policies, training-data disputes and positive results. The full label is in the table by chapter.", "",
            "| Failure type | ID | Title | Year | Chapter(s) | Outcome |",
            "|----------|----|-----------------------------|-----|-----|----------|"]
    order = [b for b, _ in BRANCHES] + [NOT_ON_TREE]
    pairs = [(b, r) for r in rows for b in branches_of(r["failure"])]
    for b, r in sorted(pairs, key=lambda p: (order.index(p[0]), p[1]["id"])):
        out.append(f"| {b} | {ident(r)} | {cell(r['title'])} | {cell(r['year'])} | "
                   f"{ch_str(r['chapters'])} | {cell(r['outcome'])} |")
    out.append("")

    open(OUT, "w", encoding="utf8").write("\n".join(out))
    print(f"wrote {OUT}: {len(rows)} cases ({len(rows) - len(flagged)} from the CSV, "
          f"{len(flagged)} from case files: {', '.join(flagged) or 'none'})")


if __name__ == "__main__":
    main()
