# Style sheet

Fixed before writing begins. Every chapter, box, caption and lab follows these rules. Source: the book design guide (October 16, 2026), section 9, and the repository rules in CLAUDE.md. Terminology decisions go in docs/glossary.md.

## 1. Language and voice

| Rule | Why | Wrong → Right |
|---|---|---|
| American English. Address the reader as "you"; author asides in "I". | Personalization principle (Mayer) | "Students should verify…" → "You should verify…" |
| Average sentence under 20 words; paragraphs of at most 4 sentences. | Readers from every major, no prerequisites | — |
| Define every acronym at first use in every chapter. | Chapters must be readable on their own | "RAG" → "retrieval-augmented generation (RAG)" |
| No anthropomorphic verbs for AI systems (knows, thinks, wants, understands, believes, lies). | They feed a misconception about how models work | "The AI knows the answer" → "The model generates a likely answer" |
| Neither hype nor doom: every claim tied to evidence and a date. | The point of literacy is critical judgment | "AI will replace all jobs" → "A 2026 study estimates … (Source, 2026)" |
| Definitions short and encyclopedic; narration conversational. | Definition box = formal; main text = personal | — |
| The author's own anecdotes appear only when the author supplies them. | Never invent an anecdote, quotation or "From the Field" case | — |

## 2. Terminology and consistency

| Rule | Application |
|---|---|
| Terms first, text second | Decide once (for example "hallucination" vs. "confabulation", "agent" vs. "AI agent"), record it in docs/glossary.md, use it everywhere |
| Bilingual mapping | Fill in the Turkish equivalent for every glossary term while writing (fine-tuning → ince ayar, prompt → istem) |
| Framework terms in their original form | Delegation, Description, Discernment, Diligence stay in English |
| One definition per term | The wording in the glossary and in the chapter's definition box is identical |

## 3. Tool and brand neutrality

| Rule | Why |
|---|---|
| The main text explains concepts, not a specific product's menus | Interfaces change within months; the book must last years |
| If a product example is needed, show at least two providers | Neutrality; students under institutional purchasing limits |
| Label every screenshot and model output with model name and date | Reproducibility: "Output from Model X, accessed Feb 2027" |
| Prefer exercises that work on free tiers or university-provided tools | "AI for All" cannot depend on paid access |
| Tool-specific click paths go to Compass notes | Compass is updated; the book is not |

## 4. Examples and inclusion

| Rule | Application |
|---|---|
| Rotate examples across at least six fields | Health, business and finance, arts and design, social sciences, engineering, education |
| Vary names, geography and culture | Use the OpenStax diversity and inclusion guidelines as a checklist |
| Anonymize field cases | No company names or personal data in author field cases; written permission where needed |
| Recurring characters | Only those approved in docs/characters.md (not yet decided) |

## 5. Citations, numbers, figures and code

| Topic | Rule |
|---|---|
| Citation style | APA 7, including in technical deep-dive boxes |
| Numbers and claims | Every factual claim has a source and a year; prefer peer-reviewed or official sources. Unknown or unverified → [VERIFY]. Never invent a citation, quotation, statistic or study. |
| Quotations | Paraphrase. At most one short quotation (under 15 words) per source |
| Figures | Each figure serves a learning objective; short caption; title states the finding; follows docs/visual-guide.md |
| Generative imagery | Not used in main figures; if used elsewhere, labeled in the caption |
| Code | Only in Deep boxes; Python; link to a browser notebook; pin library versions |
| Prompt examples | In a monospace box; below it the sample output, model name and date |
| Placeholders while drafting | [FIG n.m: title that states the finding] · [CITE: source, year] · [VERIFY] |

## 6. Dated content

| Layer | Example | Expected shelf life | Where it lives |
|---|---|---|---|
| Core | Machine-learning intuition, the probabilistic nature of LLMs, sources of bias, the 4D competencies, explainability principles | 5+ years | Main text |
| Practice | Prompt patterns, agent workflow patterns, evaluation rubrics, regulation summaries | 1–2 years | Main text, in dated boxes ("as of <month year>") |
| Tool | Product steps, model names, prices, screenshots | 3–6 months | Compass only |

Laws and rules (especially Chapter 18) carry an "as of" date.

## 7. Accessibility (from the first draft, not after)

Target WCAG 2.1 AA (required of public universities under the DOJ ADA Title II rule; compliance dates as revised in 2026 [VERIFY]).

- Meaningful alt text on every image; long descriptions for complex figures
- Heading hierarchy with no skipped levels (H1 → H2 → H3)
- Color never carries meaning alone; text contrast at least 4.5:1
- Tables have a defined header row; no merged cells
- Math as LaTeX/MathML, never as an image
- Captions and transcripts for any video
- Outputs as tagged PDF and EPUB 3, tested automatically (Ace by DAISY, EPUBCheck) and manually before release

## 8. Integrity and disclosure

- Compass (OptiWisdom) is optional, free and ungraded for UTD students; never imply that grades or student data go to Compass.
- Log substantive AI assistance in docs/ai-use-log.md (date, tool, purpose, human change).
- No AI tool is ever listed as an author. The author makes the final voice edit on every chapter.
