"""Merge a chapter handoff file (docs/production/handoff/chNN.md) into the shared files.

Usage (from the repo root):  python3 tools/merge_handoff.py NN [--dry-run]

Sections (by '## ' heading prefix) and targets:
  Glossary rows        -> docs/glossary.md (3-column rows add/replace by term; a 4-column
                          "changed definitions" table applies its Proposed column unless it starts
                          with "Unchanged")
  Characters log rows  -> docs/characters.md (rows inserted after the last log row)
  Figure index rows    -> figures/index.csv (replace by id, else append)
  Case index row       -> cases/index.csv (replace by id, else append)
  Refresh-list rows    -> docs/refresh-list.md (append data rows)
  Decisions            -> docs/decisions.md, section "## Chapter-level decisions (from handoffs)"
  Appendix E           -> appendix/answers.md (the '## Chapter NN' block; replaced if present)
  Author-only items    -> docs/production/author-items.md (replaced per chapter)
  Instructor package   -> docs/production/instructor-package.md (replaced per chapter)
"""
import csv
import io
import re
import sys

NN = sys.argv[1].zfill(2)
DRY = "--dry-run" in sys.argv
HO = open(f"docs/production/handoff/ch{NN}.md", encoding="utf8").read()


def sections(text):
    out, cur, buf = {}, None, []
    for line in text.split("\n"):
        m = re.match(r"^## (.+)$", line)
        if m and not re.match(r"^## Chapter \d+", line):
            if cur:
                out[cur] = "\n".join(buf)
            cur, buf = m.group(1).strip(), []
        else:
            buf.append(line)
    if cur:
        out[cur] = "\n".join(buf)
    return out


def find(secs, prefix):
    for k, v in secs.items():
        if k.lower().startswith(prefix.lower()):
            return v
    return ""


def table_rows(block):
    rows = []
    for line in block.split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        rows.append((line.rstrip(), cells))
    return rows


def write(path, text):
    if DRY:
        print(f"[dry] would write {path}")
    else:
        open(path, "w", encoding="utf8").write(text)


secs = sections(HO)
log = []

# ---- glossary
g_block = find(secs, "Glossary")
if g_block:
    gpath = "docs/glossary.md"
    g = open(gpath, encoding="utf8").read().rstrip("\n").split("\n")
    def term_key(cells):
        return re.sub(r"\s*\(.*?\)\s*$", "", cells[0]).strip().lower() if cells else ""
    idx = {}
    for i, line in enumerate(g):
        if line.startswith("| ") and not line.startswith("| Term") and not line.startswith("|---"):
            idx[[c.strip() for c in line.strip().strip("|").split("|")][0].lower()] = i
    added = changed = 0
    for line, cells in table_rows(g_block):
        if cells[0].lower() in ("term",):
            continue
        if len(cells) == 3:
            key = cells[0].lower()
            new = f"| {cells[0]} | {cells[1]} | {cells[2]} |"
            if key in idx:
                g[idx[key]] = new
                changed += 1
            else:
                g.append(new)
                idx[key] = len(g) - 1
                added += 1
        elif len(cells) == 4 and not cells[2].lower().startswith("unchanged"):
            key = cells[0].lower()
            if key in idx:
                old = [c.strip() for c in g[idx[key]].strip().strip("|").split("|")]
                g[idx[key]] = f"| {old[0]} | {cells[2]} | {old[2] if len(old) > 2 else ''} |"
                changed += 1
    write(gpath, "\n".join(g) + "\n")
    log.append(f"glossary +{added} ~{changed}")

# ---- characters
c_block = find(secs, "Characters")
if c_block:
    cpath = "docs/characters.md"
    c = open(cpath, encoding="utf8").read().split("\n")
    rows = [l for l, cells in table_rows(c_block) if re.match(r"\|\s*20\d\d-", l)]
    last = max(i for i, l in enumerate(c) if re.match(r"\|\s*20\d\d-\d\d-\d\d \|", l))
    existing = set(c)
    rows = [r for r in rows if r not in existing]
    c[last + 1:last + 1] = rows
    write(cpath, "\n".join(c))
    log.append(f"characters +{len(rows)}")

# ---- figure index
f_block = find(secs, "Figure index")
if f_block:
    fpath = "figures/index.csv"
    lines = open(fpath, encoding="utf8").read().rstrip("\n").split("\n")
    byid = {l.split(",")[0]: i for i, l in enumerate(lines)}
    n = 0
    for l in f_block.split("\n"):
        l = l.strip()
        if re.match(r"^F\d+\.\w+,", l):
            fid = l.split(",")[0]
            if fid in byid:
                lines[byid[fid]] = l
            else:
                lines.append(l)
                byid[fid] = len(lines) - 1
            n += 1
    write(fpath, "\n".join(lines) + "\n")
    log.append(f"figures/index {n}")

# ---- case index
k_block = find(secs, "Case index")
if k_block:
    kpath = "cases/index.csv"
    lines = open(kpath, encoding="utf8").read().rstrip("\n").split("\n")
    byid = {l.split(",")[0]: i for i, l in enumerate(lines)}
    n = 0
    for l in k_block.split("\n"):
        l = l.strip().strip("`")
        if re.match(r"^C\d\d,", l):
            list(csv.reader(io.StringIO(l)))  # validates quoting
            cid = l.split(",")[0]
            if cid in byid:
                lines[byid[cid]] = l
            else:
                lines.append(l)
            n += 1
    write(kpath, "\n".join(lines) + "\n")
    log.append(f"cases/index {n}")

# ---- refresh list
r_block = find(secs, "Refresh")
if r_block:
    rpath = "docs/refresh-list.md"
    r = open(rpath, encoding="utf8").read().rstrip("\n")
    rows = [l for l, cells in table_rows(r_block) if cells and cells[0].lower() not in ("ch", "chapter", "row", "id")]
    rows = [l for l in rows if l not in r]
    write(rpath, r + "\n" + "\n".join(rows) + "\n")
    log.append(f"refresh +{len(rows)}")

# ---- decisions
d_block = find(secs, "Decisions")
if d_block and d_block.strip():
    dpath = "docs/decisions.md"
    d = open(dpath, encoding="utf8").read().rstrip("\n")
    head = "## Chapter-level decisions (from handoffs)"
    marker_s, marker_e = f"<!-- ch{NN}-decisions -->", f"<!-- /ch{NN}-decisions -->"
    body = f"{marker_s}\n### Chapter {int(NN)}\n{d_block.strip()}\n{marker_e}"
    if marker_s in d:
        d = re.sub(re.escape(marker_s) + r".*?" + re.escape(marker_e), body, d, flags=re.S)
    else:
        if head not in d:
            d += "\n\n" + head + "\n"
        d += "\n" + body
    write(dpath, d + "\n")
    log.append("decisions")

# ---- appendix E
m = re.search(r"^## Appendix E.*?$\n(.*?)(?=^## (?!Chapter \d)|\Z)", HO, flags=re.S | re.M)
if m:
    block = m.group(1).strip()
    if not block.startswith("## Chapter"):
        block = f"## Chapter {int(NN)}\n\n" + block
    apath = "appendix/answers.md"
    a = open(apath, encoding="utf8").read().rstrip("\n")
    pat = re.compile(rf"^## Chapter {int(NN)}\b.*?(?=^## Chapter |\Z)", re.S | re.M)
    if pat.search(a):
        a = pat.sub(block + "\n\n", a).rstrip("\n")
    else:
        a += "\n\n" + block
    write(apath, a + "\n")
    log.append("appendix E")

# ---- author items / instructor package
for prefix, path, title in (("Author-only", "docs/production/author-items.md", "# Author-only items (collected from chapter handoffs)"),
                            ("Instructor package", "docs/production/instructor-package.md", "# Instructor package (eLearning and Compass assets promised by the chapters)")):
    blk = find(secs, prefix)
    if not blk.strip():
        continue
    try:
        t = open(path, encoding="utf8").read().rstrip("\n")
    except FileNotFoundError:
        t = title
    s_, e_ = f"<!-- ch{NN} -->", f"<!-- /ch{NN} -->"
    body = f"{s_}\n## Chapter {int(NN)}\n{blk.strip()}\n{e_}"
    if s_ in t:
        t = re.sub(re.escape(s_) + r".*?" + re.escape(e_), body, t, flags=re.S)
    else:
        t += "\n\n" + body
    write(path, t + "\n")
    log.append(prefix)

print(f"ch{NN}: " + "; ".join(log))
