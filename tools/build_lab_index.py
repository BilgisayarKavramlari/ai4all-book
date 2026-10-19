#!/usr/bin/env python3
"""Build Appendix B (Compass Lab Index) from the lab files' own headers.

Usage (from the book root):
    python3 tools/build_lab_index.py            # writes appendix/b-lab-index.qmd
    python3 tools/build_lab_index.py --check    # only prints the cross-check report

What it reads
  labs/chNN-labK.md   one file per lab. The first line is "# Lab N.K — Title" and a
                      Field | Value table follows (Type, Objectives, Time, Materials,
                      and sometimes Grouping, Groups, AI tools). Files that are not
                      labs (for example the A9 scenario briefs, labs/ch11-a9-*.md)
                      do not match the pattern and are skipped.
  chapters/NN-*.qmd   only for a cross-check: each chapter's "### Lab N.K: Title
                      (Type · duration · status)" heading. Differences are printed,
                      never written into the appendix; the lab file is the source.

What it derives
  duration   the first "N minutes" phrase of the Time field, with its parenthetical
             (for example "(10-minute version available)") and any "plus about N
             minutes before class" or "then a ... check" clause.
  status     "Optional" if the title, Type or Time says optional, or the lab is Deep
             or belongs to a Deep chapter (6, 13, 17; decision D20); otherwise
             "Required" ("in a lab session" added when the header says so).
  tools      short phrases matched in the Materials and AI tools fields (see TOOL_RULES);
             "No device or AI account needed" and no-device routes are reported as stated.
  compass    every row's "In Compass (optional)" column reads "link to be added";
             the [COMPASS: chNN-labK] keys are listed in an HTML comment so the
             editor can replace them when the short links exist.

Standard library only. Re-run after any lab file changes.
"""
import argparse
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LABS = os.path.join(ROOT, "labs")
CHAPTERS = os.path.join(ROOT, "chapters")
OUT = os.path.join(ROOT, "appendix", "b-lab-index.qmd")

LAB_FILE = re.compile(r"^ch(\d\d)-lab(\d+)\.md$")
DEEP_CHAPTERS = {6, 13, 17}          # docs/decisions.md D20; Chapters 22 and 23 have no labs
PARTS = [
    ("Part I — Understanding AI", range(1, 5)),
    ("Part II — Working with AI", range(5, 11)),
    ("Part III — Deciding and Building with AI", range(11, 15)),
    ("Part IV — Using AI Responsibly", range(15, 19)),
    ("Part V — AI in Your Field and Your Future", range(19, 22)),
]

# (pattern in the Materials / AI tools text, short phrase for the table), checked in order.
TOOL_RULES = [
    (r"image-classifier", "browser-based no-code image classifier"),
    (r"camera", "phone or laptop camera"),
    (r"The Lab 2\.1 tool", "the Lab 2.1 classifier tool and photos"),
    (r"Lab 2\.1 dataset", "your Lab 2.1 dataset or the provided card dataset"),
    (r"tokenizer", "browser-based tokenizer page"),
    (r"accepts images", "AI tool that accepts images"),
    (r"reverse image search", "reverse image search tool"),
    (r"content-credential viewer", "content-credential viewer"),
    (r"provided short clips", "provided audio clips and answer sheet"),
    (r"browser notebook", "browser notebook (Python)"),
    (r"standing instructions, project spaces or memory", "AI tool with standing instructions or memory, or the provided sample list"),
    (r"agent mode", "a tool with web access or an agent mode, if available"),
    (r"accepts a pasted or uploaded document", "AI tool that accepts a document"),
    (r"Optional: a university-provided tool", "provided sample sheet; AI chat tool optional"),
    (r"no-AI route", "AI chat tool, or the no-AI route"),
    (r"(?<![Nn]o )\b(AI (chat )?tools?|chat tool|Copilot)\b(?! you use)(?! you used)", "AI chat tool"),
    (r"provided dated AI output", "provided dated AI output"),
    (r"dated AI analysis", "provided dataset and dated AI analysis"),
    (r"own terms|privacy pages|help or privacy|terms and help pages", "providers' own terms, help or privacy pages"),
    (r"published model cards", "two published model cards (links)"),
    (r"classmate's A13 prototype", "a classmate's A13 prototype and card"),
    (r"A3 iteration log", "your A3 iteration log and an AI chat tool"),
    (r"websites", "web browser"),
    (r"spreadsheet", "spreadsheet"),
    (r"library catalog|library database|scholarly search|DOI lookup|search engine", "library or search tools"),
    (r"timer", "timer"),
]
PRINTED = re.compile(r"print|handout|card set|cards?\b|sheet", re.I)
NO_AI = [
    (r"No device or AI account (is )?needed", "No device or AI account needed"),
    (r"No AI tool needed", "No AI tool needed"),
    (r"AI tools: None needed", "No AI tool needed"),
]
NO_DEVICE_ROUTE = re.compile(
    r"no-device route|no-AI route|pen and paper|printed sample trace|printed, dated outputs|"
    r"provided dated outputs|dated sample outputs|dated sample summaries|dated sample log|"
    r"printed, dated excerpts|numbered printed outputs", re.I)


def md_plain(text):
    """Drop Markdown emphasis so cells stay short and clean."""
    return re.sub(r"\*\*?([^*]+)\*\*?", r"\1", text).strip()


def parse_lab(path):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    head = lines[0].lstrip("# ").strip()
    m = re.match(r"(Lab \d+\.\d+(?:, Station \d+)?)\s+—\s+(.*)$", head)
    if not m:
        raise ValueError(f"{path}: first line is not '# Lab N.K — Title'")
    code, title = m.group(1), m.group(2)
    fields = {}
    for line in lines[1:]:
        if not line.startswith("|"):
            if fields:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0] not in ("Field", "") and not set(cells[0]) <= set("-: "):
            fields[cells[0]] = "|".join(cells[1:]).strip()
    return code, title, fields


def duration(time_text):
    t = md_plain(time_text)
    m = re.search(r"(?:[Aa]bout )?\d+(?:–\d+)?\s*minutes(?:\s*\([^)]*\))?", t)
    if not m:
        return "not stated"
    out = m.group(0)
    if out.lower().startswith("about"):
        out = "About" + out[5:]
    for extra in (r"then a \d+-minute check[^,;.]*",
                  r"plus about \d+(?:–\d+)? minutes before class",
                  r"up to an hour[^;.]*"):
        e = re.search(extra, t)
        if e:
            out += "; " + e.group(0)
    return out


def status(chapter, title, fields):
    text = " ".join([title, fields.get("Type", ""), fields.get("Time", "")])
    deep = bool(re.search(r"\bDeep\b", title + " " + fields.get("Type", "")))
    optional = bool(re.search(r"\boptional\b(?! if)", text, re.I)) or deep or chapter in DEEP_CHAPTERS
    if not optional:
        return "Required, in a lab session" if re.search(r"in class|class session|lab session", text) else "Required"
    out = "Optional"
    if re.search(r"recommended", text):
        out += ", recommended"
    if deep:
        out += "; Deep, not examinable"
    elif chapter in DEEP_CHAPTERS:
        out += "; Deep chapter, not examinable"
    return out


def tools(fields):
    text = md_plain(fields.get("Materials", ""))
    if "AI tools" in fields:
        text += " AI tools: " + md_plain(fields["AI tools"])
    found = []
    for pat, phrase in NO_AI:
        if re.search(pat, text, re.I):
            found.append(phrase)
            break
    if not found:
        for pat, phrase in TOOL_RULES:
            if re.search(pat, text) and phrase not in found:
                # "AI chat tool" is redundant once a more specific AI tool is named
                if phrase == "AI chat tool" and any("AI" in p or p.startswith("a tool") for p in found):
                    continue
                found.append(phrase)
    if not found:
        if PRINTED.search(text):
            found.append("printed or provided sheets; no AI tool named")
        else:   # fall back to the Materials field's first item, without asides
            first = re.split(r"[;:]", text)[0]
            found.append(re.sub(r"\s*\([^)]*\)", "", first).strip().rstrip("."))
    out = "; ".join(found)
    if NO_DEVICE_ROUTE.search(text) and not found[0].startswith("No ") and not any("route" in p for p in found):
        out += "; no-device route stated"
    return out[0].upper() + out[1:]


def chapter_headings():
    """Map 'Lab N.K' (or 'Lab 15.1, Station 3') -> (title, parenthetical) from chapter headings."""
    heads = {}
    for name in sorted(os.listdir(CHAPTERS)):
        if not name.endswith(".qmd"):
            continue
        with open(os.path.join(CHAPTERS, name), encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r"^### (Lab \d+\.\d+(?:, Station \d+)?): (.*?) \((.*)\) \{\.unnumbered\}", line)
                if m:
                    heads[m.group(1)] = (m.group(2), m.group(3))
    return heads


def collect():
    rows = []
    for name in sorted(os.listdir(LABS)):
        m = LAB_FILE.match(name)
        if not m:
            continue
        chapter = int(m.group(1))
        code, title, fields = parse_lab(os.path.join(LABS, name))
        rows.append({
            "file": name, "key": name[:-3], "chapter": chapter, "code": code,
            "title": re.sub(r"\s*\((optional|Deep)\)$", "", md_plain(title)), "type": md_plain(fields.get("Type", "")),
            "duration": duration(fields.get("Time", "")),
            "status": status(chapter, title, fields), "tools": tools(fields),
        })
    return rows


def cross_check(rows):
    heads = chapter_headings()
    notes = []
    for r in rows:
        h = heads.get(r["code"])
        if not h:
            notes.append(f"{r['code']} ({r['file']}): no matching '### {r['code']}:' heading in the chapter")
            continue
        ch_title, paren = h
        base = re.sub(r"\s*\((optional|Deep|inside Lab[^)]*)\)$", "", r["title"])
        base = re.sub(r"\s*\(supplied by Chapter \d+\)$", "", base)
        if not ch_title.startswith(base.split(":")[0]):
            notes.append(f"{r['code']}: title differs — lab file '{r['title']}', chapter '{ch_title}'")
        nums = re.findall(r"\d+(?:–\d+)?(?= ?minutes)", r["duration"])
        ch_nums = re.findall(r"\d+(?:–\d+)?(?= ?minutes)", paren)
        if nums and ch_nums and nums[0] != ch_nums[0]:
            notes.append(f"{r['code']}: duration differs — lab file '{r['duration']}', chapter heading '({paren})'")
        if not ch_nums:
            notes.append(f"{r['code']}: chapter heading states no duration ('({paren})'); lab file says '{r['duration']}'")
        ch_opt = "optional" in paren.lower()
        if ch_opt != r["status"].startswith("Optional"):
            notes.append(f"{r['code']}: status differs — lab file '{r['status']}', chapter heading '({paren})'")
    return notes


def cell(text):
    return text.replace("|", "/")


def render(rows):
    n_req = sum(r["status"].startswith("Required") for r in rows)
    out = [
        "<!-- Generated from the headers of labs/chNN-labK.md by tools/build_lab_index.py. "
        "Do not edit by hand; change the lab file and rerun the script. -->",
        "",
        "# Compass Lab Index {#sec-appendix-b}",
        "",
        f"This index lists every hands-on lab in the book: {len(rows)} labs in Chapters 1 to 21, "
        f"{n_req} of them required (each is designed for a lab session) "
        f"and {len(rows) - n_req} optional. Chapters 22 and 23 have no labs. Each row repeats what the lab's own "
        "page states: its time, whether it is required, and what you need. The full steps, expected "
        "observations and debrief questions are in the chapter's Hands-on Labs section and in the lab sheet.",
        "",
        "**How to read the table.** *Time* is the lab sheet's own estimate; where a shorter version exists, "
        "it is named. *Status* follows the lab sheet: required labs are designed for a lab session, "
        "and optional labs are practice. Labs in Deep chapters (6, 13 and 17) and labs marked Deep are "
        "not examinable (decision D20). *What you need* names the kinds of tools, never a product: tool "
        "neutrality is a rule of this book, and current tools and click paths live in Compass. "
        "\"No-device route stated\" means the lab sheet offers a way to do it without your own device or "
        "an AI account, usually with printed, dated sample outputs.",
        "",
        "**Compass.** Compass, the book's digital companion, is optional and never part of a course grade; "
        "no student data moves between a course and Compass, and every lab can be done from the book. Each "
        "row's last column will carry a short link to the lab's Compass page; until the links exist, it reads "
        "\"In Compass (optional): link to be added\".",
        "",
    ]
    for part, chapters in PARTS:
        part_rows = [r for r in rows if r["chapter"] in chapters]
        if not part_rows:
            continue
        out += [f"## {part} {{.unnumbered}}", "",
                "| Lab | Title | Ch. | Time | Status | What you need | In Compass (optional) |",
                "|------|------------|--|---------|-------|-------------|--------|"]
        for r in part_rows:
            out.append("| " + " | ".join(cell(x) for x in [
                r["code"], r["title"], str(r["chapter"]), r["duration"], r["status"], r["tools"],
                "link to be added"]) + " |")
        out.append("")
    out += [
        "Lab 15.1, Station 3 (the bias probe) is written in Chapter 16 but run inside Chapter 15's red-team "
        "lab; Lab 21.1 (the code peer check) is a named 15-minute slot inside Lab 20.1. The A9 scenario "
        "briefs and the scenario C template (Chapter 11) are assignment materials, not labs, and are not listed.",
        "",
        "<!-- Compass placeholders, one per lab, for the editor to replace with short links:",
    ]
    out += [f"     {r['code']}: [COMPASS: {r['key']}]" for r in rows]
    out += ["-->", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="print the cross-check report only")
    args = ap.parse_args()
    rows = collect()
    notes = cross_check(rows)
    print(f"{len(rows)} labs read from labs/; "
          f"{sum(r['status'].startswith('Required') for r in rows)} required")
    for n in notes:
        print("  CHECK:", n, file=sys.stderr)
    if not args.check:
        with open(OUT, "w", encoding="utf-8") as fh:
            fh.write(render(rows))
        print("wrote", os.path.relpath(OUT, ROOT))


if __name__ == "__main__":
    main()
