"""Build Appendix E (appendix/e-answers.qmd) from appendix/answers.md.

Usage (from the repo root):  python3 tools/build_appendix_e.py

appendix/answers.md stays the working file (tools/merge_handoff.py writes each chapter's block there).
This script:
  - drops code fences that wrap a whole "## Chapter N" block (a merge artifact);
  - merges repeated "## Chapter N" headings into one section per chapter, in the order 1, 2, 3 ...;
  - titles each section "## Chapter N — Title", with the title read from the chapter file's first heading;
  - keeps every answer line and the order of the subsections inside each chapter;
  - marks subsections .unnumbered and adds a placeholder for chapters with no answers yet.
Rerun after every merge. Never edit e-answers.qmd by hand.
"""
import glob
import re

SRC = "appendix/answers.md"
OUT = "appendix/e-answers.qmd"
LAST_CHAPTER = 21  # Chapters 22-23 are Deep chapters without end-of-chapter answers


def chapter_titles():
    titles = {}
    for f in glob.glob("chapters/[0-9][0-9]-*.qmd"):
        n = int(f.split("/")[1][:2])
        first = open(f, encoding="utf8").readline()
        titles[n] = re.sub(r"\s*\{.*\}\s*$", "", first.lstrip("# ").strip())
    return titles


def strip_wrapper_fences(lines):
    out, i = [], 0
    while i < len(lines):
        if lines[i].strip() == "```":
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.match(r"^## Chapter \d+", lines[j]):
                k = j
                while k < len(lines) and lines[k].strip() != "```":
                    k += 1
                out.extend(lines[i + 1:k])
                i = k + 1
                continue
        out.append(lines[i])
        i += 1
    return out


def main():
    lines = open(SRC, encoding="utf8").read().split("\n")
    lines = strip_wrapper_fences(lines)
    blocks, cur = {}, None
    for line in lines:
        m = re.match(r"^## Chapter (\d+)\b", line)
        if m:
            cur = int(m.group(1))
            blocks.setdefault(cur, [])
            continue
        if line.startswith("# "):  # the file's title
            continue
        if cur is None:
            continue
        hm = re.match(r"^(#{3,6}) (.+?)\s*$", line)
        if hm:
            text = hm.group(2)
            if "{" not in text:
                text += " {.unnumbered}"
            line = f"{hm.group(1)} {text}"
        blocks[cur].append(line)

    titles = chapter_titles()
    out = [
        "<!-- Generated from appendix/answers.md by tools/build_appendix_e.py. Do not edit by hand; edit answers.md (or the chapter handoff) and rerun. -->",
        "",
        "# Answers {#sec-appendix-e}",
        "",
        "This appendix gives model answers to the odd-numbered end-of-chapter questions and, "
        "where a chapter provides them, keys to its Check Yourself items and faded examples. "
        "Answers to even-numbered questions are not printed in this book. For written questions, "
        "the answers here are models and scoring guidance, not the only acceptable wording.",
        "",
    ]
    for n in range(1, max([LAST_CHAPTER] + list(blocks)) + 1):
        if n not in blocks and n > LAST_CHAPTER:
            continue
        title = titles.get(n, "")
        out.append(f"## Chapter {n} — {title} {{#sec-appendix-e-ch{n:02d} .unnumbered}}")
        out.append("")
        body = "\n".join(blocks.get(n, [])).strip("\n")
        out.append(body if body else "In preparation.")
        out.append("")
    open(OUT, "w", encoding="utf8").write(re.sub(r"\n{3,}", "\n\n", "\n".join(out)))
    have = sorted(n for n, b in blocks.items() if "".join(b).strip())
    print(f"wrote {OUT}: chapters with answers {have}")


if __name__ == "__main__":
    main()
