"""Chapter 22 data charts (color + gray SVG). Run from the repo root:
    python3 figures/scripts/ch22_charts.py
Published values and downloaded data (provenance and SHA-256 in data/ch22_meta.txt):
  F22.6  data/ch22_personqa.csv     OpenAI (2025) system card, Table 4 (developer's own test: reported)
  F22.7  data/ch22_benchmarks.csv   AI Index 2025 (Stanford HAI)
  F22.8  data/ch22_metr.csv         METR Time Horizon 1.1 raw results (downloaded 2026-10-18)
  F22.11 data/ch22_open_closed.csv  AI Index 2025; Epoch AI Data Insights (2025, 2026)
  F22.12 data/ch22_compute.csv      Epoch AI, Data on AI models (CC BY 4.0)
  F22.14 data/ch22_energy.csv       IEA (2025; 2026b report summary); LBNL via DOE (2024)
Fitted trend lines are this book's calculation, drawn dotted and labeled "trend, not data" (book-wide rule);
dashes are never used for data. Provider is shown by marker shape and label, never by color alone.
Every title is written from the CSV values at run time.
"""
import csv
import math
import os
from datetime import date

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
for fam in ("Source Sans 3", "Source Sans Pro"):
    if any(fam in f.name for f in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = fam
        break
plt.rcParams.update({"font.size": 12.5, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "svg.hashsalt": "ch22"})
plt.rcParams["font.sans-serif"] = ["Source Sans 3", "STIXGeneral", "DejaVu Sans"]  # no system-font fallback in print (D29)


def _solid(hex_color, alpha):
    """The color hex_color would show at this alpha over white, as an opaque color (no transparency in PDF/X)."""
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02X%02X%02X" % tuple(round(c * alpha + 255 * (1 - alpha)) for c in (r, g, b))

STYLE = {
    "color": {"main": "#1C3D6E", "accent": "#FCE38A", "risk": "#C2410C", "ok": "#4CAF84", "ink": "#1D1D1F",
              "light": "#EEF2F7", "muted": "#5C5C66", "hatch": None},
    "gray": {"main": "#3A3A3A", "accent": "#FFFFFF", "risk": "#FFFFFF", "ok": "#BDBDBD", "ink": "#000000",
             "light": "#FFFFFF", "muted": "#444444", "hatch": "///"},
}
WORDS = {2: "two", 3: "three", 4: "four", 5: "five"}


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf8") as fh:
        return list(csv.DictReader(line for line in fh if not line.startswith("#") and line.strip()))


def save(fig, fid, mode):
    out = os.path.join(ROOT, "figures", "out", mode, f"{fid}.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def source(fig, text, y=-0.06):
    fig.text(0.01, y, text, fontsize=10.5, color="#1D1D1F", wrap=True)


def year_frac(s):
    y, m, d = (int(p) for p in s.split("-"))
    return y + (date(y, m, d).timetuple().tm_yday - 1) / 366


def ols(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return b, my - b * mx


# ---------------------------------------------------------------- F22.6 PersonQA
def personqa():
    rows = read("ch22_personqa.csv")
    by = {r["model"]: r for r in rows}
    more_acc = float(by["o3"]["accuracy"]) > float(by["o1"]["accuracy"])
    more_hal = float(by["o3"]["hallucination_rate"]) > float(by["o1"]["hallucination_rate"])
    assert more_acc and more_hal, "title no longer matches the data"
    title = ("In its developer's 2025 test, the newer o3 was more often accurate and more often wrong "
             "about people than the older o1")
    for mode, st in STYLE.items():
        fig, ax = plt.subplots(figsize=(8, 3.9))
        names = [r["model"] for r in rows]
        xs = range(len(rows))
        acc = [float(r["accuracy"]) for r in rows]
        hal = [float(r["hallucination_rate"]) for r in rows]
        ax.bar([x - 0.2 for x in xs], acc, 0.38, color=st["ok"], edgecolor=st["ink"], label="accuracy (higher is better)")
        ax.bar([x + 0.2 for x in xs], hal, 0.38, color=st["risk"], edgecolor=st["ink"], hatch=st["hatch"],
               label="hallucination rate (lower is better)")
        for x, a, h in zip(xs, acc, hal):
            ax.text(x - 0.2, a + 0.02, f"{a:.2f}", ha="center", fontsize=12)
            ax.text(x + 0.2, h + 0.02, f"{h:.2f}", ha="center", fontsize=12)
        ax.set_xticks(list(xs))
        short = {"o1": "o1 (older)", "o3": "o3 (newer)", "o4-mini": "o4-mini (newer, smaller)"}
        ax.set_xticklabels([short.get(n, n) for n in names])
        ax.set_ylim(0, 0.85)
        ax.set_ylabel("share of answers")
        ax.legend(frameon=False, loc="upper left", ncol=2)
        ax.set_title(title, fontsize=13.5, loc="left", wrap=True)
        source(fig, "Source: OpenAI (2025a), o3 and o4-mini System Card, Table 4, PersonQA. The developer's own "
               "test (reported); it says o3 makes more claims overall and that more research is needed. "
               "As of October 2026.")
        save(fig, "f22-06-personqa", mode)
    return title


# ---------------------------------------------------------------- F22.7 benchmark jumps
def benchmarks():
    rows = read("ch22_benchmarks.csv")
    top = max(rows, key=lambda r: float(r["gain_points_2023_2024"]))
    title = (f"On three hard tests introduced in 2023, top scores rose {min(float(r['gain_points_2023_2024']) for r in rows):.1f} to "
             f"{float(top['gain_points_2023_2024']):.1f} points in one year")
    for mode, st in STYLE.items():
        fig, ax = plt.subplots(figsize=(8, 3.4))
        names = [f"{r['benchmark']}\n{r['what_it_tests']}" for r in rows]
        vals = [float(r["gain_points_2023_2024"]) for r in rows]
        ax.barh(names, vals, color=st["main"], edgecolor=st["ink"])
        for i, v in enumerate(vals):
            ax.text(v + 1, i, f"+{v:.1f} points", va="center", fontsize=12)
        ax.set_xlim(0, 85)
        ax.set_xlabel("gain in score, percentage points, 2023 to 2024")
        ax.invert_yaxis()
        ax.set_title(title, fontsize=13.5, loc="left", wrap=True)
        source(fig, "Source: Stanford HAI (2025), AI Index Report 2025, top takeaways: compiled by an outside "
               "tracker; many scores were reported by developers. SWE-bench: 4.4% to 71.7% (this book's "
               "subtraction). As of October 2026.", y=-0.2)
        save(fig, "f22-07-benchmark-jumps", mode)
    return title


# ---------------------------------------------------------------- F22.8 METR horizons
MARK = {"OpenAI": "o", "Anthropic": "s", "Google": "^", "other": "D"}


def horizons():
    rows = read("ch22_metr.csv")
    sota = [r for r in rows if r["is_sota"] == "True" and r["release_date"] >= "2023-01-01"
            and r["above_16h_flag"] == "False"]
    b, a = ols([year_frac(r["release_date"]) for r in sota], [math.log2(float(r["p50_min"])) for r in sota])
    doubling_days = 365.25 / b
    latest = {}
    for r in rows:
        if r["provider"] in ("OpenAI", "Anthropic", "Google"):
            if r["provider"] not in latest or r["release_date"] > latest[r["provider"]]["release_date"]:
                latest[r["provider"]] = r
    title = ("METR's measured 50% horizon for frontier agents rose from minutes in 2023 to hours in 2026; "
             "80% horizons stay several times shorter")
    for mode, st in STYLE.items():
        fig, ax = plt.subplots(figsize=(8.4, 4.8))
        for prov, mk in MARK.items():
            pr = [r for r in rows if r["provider"] == prov and r["release_date"] >= "2023-01-01"]
            if not pr:
                continue
            ax.scatter([year_frac(r["release_date"]) for r in pr], [float(r["p50_min"]) / 60 for r in pr],
                       marker=mk, s=46, facecolor=st["main"], edgecolor=st["ink"], label=f"{prov}: 50% horizon",
                       zorder=3)
            ax.scatter([year_frac(r["release_date"]) for r in pr], [float(r["p80_min"]) / 60 for r in pr],
                       marker=mk, s=40, facecolor="white", edgecolor=st["ink"], label=f"{prov}: 80% horizon",
                       zorder=3)
        xs = [2023.0, 2026.4]
        ax.plot(xs, [2 ** (a + b * x) / 60 for x in xs], linestyle=":", color=st["ink"], linewidth=1.8)
        ax.text(2024.95, 1.15 / 60,
                f"dotted: trend, not data\n(METR's fit, about 129 days per doubling;\nthis book's "
                f"recalculation agrees: {doubling_days:.0f} days)", fontsize=11.5, color=st["ink"])
        ax.axhline(16, color=st["muted"], linewidth=1.0)
        ax.text(2023.75, 24, "above 16 hours: METR calls its estimates unreliable", fontsize=11.5,
                color=st["ink"])
        ax.set_yscale("log")
        ax.set_ylim(0.5 / 60, 45)
        ax.set_xticks([2023, 2024, 2025, 2026])
        ax.set_xticklabels(["2023", "2024", "2025", "2026"])
        ax.set_yticks([1 / 60, 4 / 60, 0.25, 1, 4, 16])
        ax.set_yticklabels(["1 min", "4 min", "15 min", "1 h", "4 h", "16 h"])  # about ×4 per tick
        ax.set_ylabel("task length for skilled people\n(log scale: each step is a multiple, not a fixed amount)")
        ax.set_xlabel("model release date")
        ax.legend(frameon=False, fontsize=10.5, ncol=1, loc="upper left", bbox_to_anchor=(0, 0.9))
        ax.set_title(title, fontsize=13.5, loc="left", wrap=True)
        source(fig, "Source: METR (2026), Time Horizon 1.1 raw results (downloaded October 18, 2026; the page is no "
               "longer actively updated, last updated September 8, 2026). Filled = 50% horizon, open = 80%. "
               "METR's own fit from 2023 on, leaving out estimates above 16 h: about 129 days (range 104–158).",
               y=-0.1)
        save(fig, "f22-08-horizons", mode)
    return title, doubling_days, latest


# ---------------------------------------------------------------- F22.11 open vs closed
def open_closed():
    rows = {r["measure"]: r for r in read("ch22_open_closed.csv")}
    title = (f"The measured gap between the best open-weight and best closed models: "
             f"{float(rows['leaderboard_gap_end']['value']):g}% on a leaderboard in 2025; about "
             f"{float(rows['time_gap_2026']['value']):g} months on Epoch's index in 2026")
    for mode, st in STYLE.items():
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 3.6), gridspec_kw={"width_ratios": [1, 1.2]})
        a1.bar(["Jan 2024", "Feb 2025"], [float(rows["leaderboard_gap_start"]["value"]),
                                         float(rows["leaderboard_gap_end"]["value"])],
               color=st["main"], edgecolor=st["ink"], width=0.55)
        for i, k in enumerate(["leaderboard_gap_start", "leaderboard_gap_end"]):
            a1.text(i, float(rows[k]["value"]) + 0.2, f"{float(rows[k]['value']):g}%", ha="center")
        a1.set_ylabel("score gap (%)")
        a1.set_ylim(0, 10)
        a1.set_title("AI Index 2025 (Chatbot Arena)", fontsize=12.5)
        t25, t26 = rows["time_gap_2025"], rows["time_gap_2026"]
        a2.bar(["as of Oct 30, 2025\n(90% range 1.1–5.3)", "Jan to May 2026"], [float(t25["value"]), float(t26["value"])],
               color=st["light"], edgecolor=st["ink"], width=0.55)
        a2.errorbar([0], [float(t25["value"])], yerr=[[float(t25["value"]) - float(t25["ci_low"])],
                                                      [float(t25["ci_high"]) - float(t25["value"])]],
                    color=st["ink"], capsize=5)
        a2.text(0.12, float(t25["value"]) + 0.15, f"{float(t25['value']):g}", fontsize=12)
        a2.text(1, float(t26["value"]) + 0.2, f"about {float(t26['value']):g}", ha="center")
        a2.set_ylabel("months behind")
        a2.set_ylim(0, 7)
        a2.set_title("Epoch AI, Capabilities Index", fontsize=12.5)
        fig.suptitle(title, fontsize=13.5, x=0.01, ha="left", wrap=True)
        fig.tight_layout(rect=(0, 0, 1, 0.88))
        source(fig, "Sources: Stanford HAI (2025), AI Index Report 2025; Epoch AI Data Insights (October 30, 2025; "
               "May 29, 2026). Left: crowd votes, compiled by the AI Index (a score gap); right: Epoch's own index "
               "(a time gap). As of October 2026.", y=-0.08)
        save(fig, "f22-11-open-closed", mode)
    return title


# ---------------------------------------------------------------- F22.12 training compute
def compute():
    rows = read("ch22_compute.csv")
    xs = [year_frac(r["publication_date"]) for r in rows]
    ys = [float(r["training_compute_flop"]) for r in rows]
    b, a = ols(xs, [math.log10(y) for y in ys])
    factor = 10 ** b
    title = (f"Training compute for notable AI models grew about {factor:.1f} times a year from 2010 to 2026 "
             f"(this book's fit to Epoch AI's data)")
    for mode, st in STYLE.items():
        fig, ax = plt.subplots(figsize=(8.4, 4.4))
        ax.scatter(xs, ys, s=10, facecolor=_solid(st["main"], 0.75), edgecolor="none")
        line_x = [2010, 2026.8]
        ax.plot(line_x, [10 ** (a + b * x) for x in line_x], linestyle=":", color=st["ink"], linewidth=2)
        ax.text(2010.3, 1e25, f"dotted: trend, not data\n(this book's fit: about {factor:.1f}× a year)",
                fontsize=11.5)
        ax.set_yscale("log")
        ax.set_ylabel("training compute (FLOP)\nlog scale: each step is ten times the last")
        ax.set_xlabel("publication date")
        ax.set_xticks(list(range(2010, 2027, 2)))
        ax.set_xticklabels([str(y) for y in range(2010, 2027, 2)])
        ax.set_title(title, fontsize=13.5, loc="left", wrap=True)
        source(fig, f"Source: Epoch AI (2026), Data on AI models, notable models with a compute estimate (n = {len(rows)}; "
               "downloaded October 18, 2026; CC BY 4.0); compute values are Epoch's outside estimates. Epoch's figure "
               "for frontier models: 4–5× a year. FLOP = a count of arithmetic operations.", y=-0.13)
        save(fig, "f22-12-compute", mode)
    return title, factor, len(rows)


# ---------------------------------------------------------------- F22.14 electricity
def electricity():
    rows = read("ch22_energy.csv")
    w24 = next(r for r in rows if r["scope"] == "world" and r["year"] == "2024")
    w25 = next(r for r in rows if r["scope"] == "world" and r["year"] == "2025" and r["unit"] == "TWh")
    w30 = next(r for r in rows if r["scope"] == "world" and r["year"] == "2030" and r["source"] == "IEA (2026b)")
    u23 = next(r for r in rows if r["scope"] == "us" and r["year"] == "2023")
    u28 = next(r for r in rows if r["scope"] == "us" and r["year"] == "2028")
    ratio = float(w30["value_low"]) / float(w25["value_low"])
    assert 1.8 < ratio < 2.2, "title says about twice"
    title = (f"World data centers used about {w25['value_low']} TWh in 2025; the IEA expects about twice "
             f"that by 2030")
    for mode, st in STYLE.items():
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 3.9), gridspec_kw={"width_ratios": [1.4, 1]})
        a1.bar(["2024\nestimate"], [float(w24["value_low"])], color=st["main"], edgecolor=st["ink"], width=0.55)
        a1.bar(["2025\nestimate"], [float(w25["value_low"])], color=st["main"], edgecolor=st["ink"], width=0.55)
        a1.bar(["2030\nforecast"], [float(w30["value_low"])], color=st["light"], edgecolor=st["ink"], width=0.55,
               linewidth=1.6)
        a1.text(0, float(w24["value_low"]) + 25, f"{w24['value_low']} TWh", ha="center")
        a1.text(1, float(w25["value_low"]) + 25, f"{w25['value_low']} TWh", ha="center")
        a1.text(2, float(w30["value_low"]) + 25, f"forecast:\n{w30['value_low']} TWh", ha="center")
        a1.set_ylim(0, 1200)
        a1.set_ylabel("terawatt-hours a year")
        a1.set_title("World (IEA: 2024 from the 2025 edition;\n2025 and 2030 from the 2026 edition)", fontsize=12)
        a2.bar(["2023\nestimate"], [float(u23["value_low"])], color=st["main"], edgecolor=st["ink"], width=0.5)
        lo, hi = float(u28["value_low"]), float(u28["value_high"])
        a2.bar(["2028\nscenarios"], [hi - lo], bottom=[lo], color=st["light"], edgecolor=st["ink"], width=0.5,
               linewidth=1.6)
        a2.text(0, float(u23["value_low"]) + 18, f"{u23['value_low']} TWh", ha="center")
        a2.text(1, hi + 18, f"forecast:\n{int(lo)}–{int(hi)} TWh", ha="center")
        a2.set_ylim(0, 760)
        a2.set_title("United States (LBNL, 2024)", fontsize=12)
        fig.suptitle(title, fontsize=13.5, x=0.01, ha="left", wrap=True)
        fig.tight_layout(rect=(0, 0, 1, 0.9))
        source(fig, "Sources: IEA (2025), Energy and AI; IEA (2026b), Key Questions on Energy and AI, executive summary; "
               "LBNL (Shehabi et al., 2024) as summarized by DOE (2024), 2028 totals. Filled = outside estimate of the "
               "past; light boxes labeled forecast. The 2025 edition's 2030 base case was 945 TWh. As of October 2026.",
               y=-0.12)
        save(fig, "f22-14-electricity", mode)
    return title


if __name__ == "__main__":
    print(personqa())
    print(benchmarks())
    print(horizons())
    print(open_closed())
    print(compute())
    print(electricity())
