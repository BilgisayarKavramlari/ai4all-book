# Author voice profile — Şadi Evren Şeker

Status: DRAFT v0.1 (2026-10-17), built with ai4all-author-voice Mode A. Pending the author's answers to the open questions at the end. Not yet approved.

## Basis and limits

| Sample | Year | Language | Words | Register |
|---|---|---|---|---|
| HermAI: Hermenötik Açıklanabilir Yapay Zeka (YBS Ansiklopedi) | 2025 | Turkish | ~4,400 | Research article: philosophy + engineering |
| Kolay.AI: KOBİ'lere Özel Basit Yapay Zeka Çözümü (YBS Ansiklopedi) | 2023 | Turkish (+ English abstract) | ~5,300 | Applied, product and SME oriented |
| Çizge Teorisi (YBS Ansiklopedi) | 2015 | Turkish | ~4,700 | Teaching entry, step by step |
| Bilişim Sistemleri ve Eşitlik Teorisi (YBS Ansiklopedi) | 2014 | Turkish | ~1,300 | Short encyclopedia entry |
| Pareto Prensibi (YBS Ansiklopedi) | 2014 | Turkish | ~480 | Short encyclopedia entry |
| Computerized Argument Delphi Technique (IEEE Access) | 2015 | English | ~7,700 body | Journal article, publisher-copyedited |

Limits: five of six samples are Turkish, and the only English sample is 2015 and copyedited by the journal. The profile is reliable on **structure, teaching moves, examples and stance**, and only provisional on **English sentence-level voice**. Update it when recent, unedited English writing is added. Other inventory: docs/voice/ybs-inventory.md (41 more 2014 entries, all Turkish).

## 1. Sentence length and variation

- Turkish entries: mean about 13–17 words per sentence, median 10–16, longest tenth 25–28 words; 2–3 sentences per paragraph. (Turkish packs more meaning per word; the English equivalent is roughly 18–24 words.)
- English (IEEE): medium to long sentences, often extended with "which", "where" and "while" clauses.
- Variation pattern: a long framing sentence followed by a short restatement ("Yani …", "Basitçe …"). Definitions are short; explanations and literature sentences run long.
- **For the book:** keep the long-then-short rhythm, but bring the average under 20 words (style sheet). Split "which/where" chains into two sentences.

## 2. How paragraphs and pieces open

1. **Breadth first.** Many pieces open by placing the idea across fields: "from sociology to computer science, from business to industrial engineering." This fits a book for every major.
2. **The core claim stated plainly, often as a hypothesis or definition**, then why it matters ("Bu yaklaşım … için kullanışlı bir temel teşkil etmektedir").
3. **Stakes in one concrete constraint.** Kolay.AI opens with a statistic and a small, vivid constraint: a firm with 5–10 employees cannot hire, direct and check an AI specialist.
4. **A roadmap sentence**: "This piece first defines …, then turns to studies and uses in the field."
5. **Question headings**: "Eşitlik Teorisi Nedir?", "Buradaki soru acaba …?" — a question, then the answer.

## 3. Characteristic moves and phrases

| Move | Turkish form in the samples | English equivalent to use |
|---|---|---|
| Example right after a claim | "Örneğin …" (very frequent; usually two or three examples from different sectors) | "For example, …" / "Take a hospital …" |
| Plain restatement | "Yani …", "Basitçe …", "Bunu şöyle yorumlamak da mümkündür." | "In other words, …" / "Put simply, …" / "Here is another way to see it." |
| Widening the concept | "… sadece maaş olarak da düşünmemek gerekir." | "Don't think of this only as …" |
| "The real lesson" | "… esas kazandırdığı, … önemidir." | "What the principle really gives you is …" |
| Walkthrough in first-person plural | "ele alalım", "çizecek olursak" | "Let's take …", "If we draw …" |
| Contrast pivot | "Ancak …", "Buna karşılık …", "Ne var ki …" | "But …", "In contrast, …", "Yet …" |
| Model → solve → apply | "gerçek dünyadan bir problem modellenir, bu model çözülür ve gerçek dünyaya uygulanır" | A recurring three-step frame; maps naturally to the AI Work Loop |
| Bilingual term | "çizge (graph)", "özellik atfı (feature attribution)" | In the book: English term, Turkish only in the glossary |
| Picture before prose | "Genel görüntüsü aşağıdaki şekilde çizilebilir" | Introduce the figure, then explain it |
| Linking own earlier work | Cross-references to his other entries; HermAI cites the Argument Delphi paper | Use sparingly and only where it helps the reader |

English transitions seen in the IEEE paper: "Also," (very frequent, including sentence-initial), "Because of …", "Besides …", "On the other hand", "In addition", "Finally", "For example, consider …".

## 4. "I", "we" and "you"

- Turkish entries are impersonal and passive (academic Turkish norm): "ele alınacaktır", "gösterilecektir", "denilebilir". No "I" and no direct "you".
- Walkthroughs switch to an inclusive "we/let's" ("ele alalım"). The 2025 HermAI article uses "we" for the author's own proposal ("çerçevemiz", "tartışıyoruz").
- The IEEE paper avoids "I" and almost never uses "we".
- **For the book:** the style sheet asks for "you" and first-person asides. This is a deliberate shift from the author's published register; the inclusive "let's" walkthrough is the natural bridge. Author asides in "I" appear only where the author supplies the story.

## 5. Humor and emotional register

No humor, irony or exclamation marks in any sample. The tone is calm, explanatory and confident, with occasional evaluative phrases ("The beauty of the Delphi method …", "bir lüksten zorunluluğa"). Strong claims are softened with "denilebilir / mümkündür" (one could say / it is possible to).

## 6. Examples from industry and teaching

- **Everyday, cross-sector examples:** hospital admissions, election vote shares, media ratings, Microsoft bug reports, employees' sense of fairness, SME invoice data.
- **Worked numeric example:** the Pareto entry lists the share of eleven diseases, draws a histogram, then a cumulative curve, then reads the "elbow".
- **Data spelled out field by field:** Kolay.AI lists each invoice column (BELGE_NO, TARIH, …) with "required / optional".
- **Teaching sequence:** definition → formal notation (G = (V, E)) → small example → properties → "where it is used".
- **Industry stance:** pragmatic and pro-access ("the democratization of AI"); ready-made tools before custom projects for small firms.
- **Philosophy as a lens on technology:** HermAI traces explanation from Schleiermacher and Dilthey (erklären vs. verstehen) to LIME and SHAP. This fits Chapters 17 and 23.

## 7. Not observed in the samples (avoid unless the author wants them)

Hype vocabulary ("revolutionary", "game-changing") in the author's own claims; exclamation marks; slang; jokes; second-person commands; long direct quotations; emotional appeals; rhetorical questions without an answer.

Note: the Kolay.AI literature review uses "devrim niteliğinde" (revolutionary) and repeats "Çalışma … buldu" mechanically; see open question 1.

## 8. Five representative excerpts (under 40 words each)

1. "Yani çizge teorisinin işe yaraması için öncelikle gerçek dünyadan bir problem çizge olarak modellenir, bu model çözülür ve daha sonra gerçek dünyaya uygulanır." — Çizge Teorisi, 2015 (the model → solve → apply frame)
2. "Ayrıca eşitlik teorisini sadece maaş veya ödemeler olarak da düşünmemek gerekir." — Eşitlik Teorisi, 2014 (widening the concept)
3. "Örneğin 5-10 çalışanı olan bir KOBİ'nin yapay zeka konusunda uzman istihdam etmesi ve doğru işleri ataması veya atanan işlerin doğru yapılıp yapılmadığını kontrol etmesi çoğu zaman mümkün değildir." — Kolay.AI, 2023 (stakes through one concrete constraint)
4. "Bu kara kutu sorunu, yalnızca akademik bir merak konusu değil, aynı zamanda etik, yasal ve pratik sonuçları olan temel bir güvensizlik kaynağıdır." — HermAI, 2025 (raising the stakes)
5. "The beauty of the Delphi method can also be connected to its Hegelian nature." — IEEE Access, 2015 (English, evaluative bridge to philosophy)

## 9. Turkish-influenced constructions in English (from the IEEE sample) — to confirm

| Construction (as in the sample) | Likely origin | Proposal |
|---|---|---|
| Sentence-initial "Also, …" used very often | "Ayrıca, …" | **Keep** occasionally (part of the voice); vary with "In addition" / "Beyond that" |
| Missing article: "the increasing impact of technique" | Turkish has no articles | **Smooth** |
| "Different than the consensus of traditional Delphi, …" | "… -den farklı olarak" | **Smooth** → "Unlike …" |
| "In one of these researches" | "araştırmalardan birinde" | **Smooth** → "In one of these studies" |
| "According to its continuous behavior, …" | "… davranışına göre" | **Smooth** → "Because it runs continuously, …" |
| "a qualitative prediction of forecasting method" | Stacked noun phrase | **Smooth** |
| "… is proposed which is also suitable for …" (passive + trailing relative clause) | Turkish academic passive | **Smooth** into active voice for the book |
| "and so on", "all around the world" | Common in his English | **Keep** sparingly; friendly and plain |
| "For example, consider the … scenario." | Teaching habit | **Keep** — strong for a textbook |

## 10. Rules for Mode B (voice pass on drafts)

1. Open sections with breadth or a concrete constraint, then the plain claim.
2. Follow every abstract claim with "For example" within two sentences, drawn from at least two different fields.
3. After a dense paragraph, add one short plain restatement ("In other words, …").
4. Use the model → solve → apply frame and the inclusive "Let's take …" walkthrough for worked examples.
5. Keep the calm, non-hype register; replace "one could say" hedges with a sourced, direct statement.
6. Never add humor, anecdotes or opinions the author has not supplied.

## Open questions for the author

1. Were Kolay.AI (2023) or HermAI (2025) drafted with AI assistance? If so, they should count less for sentence-level voice.
2. The book uses "you" and first-person asides, unlike your published register. Are you comfortable with personal "I" stories (supplied by you), or do you prefer mostly the inclusive "we/let's"?
3. A little light humor, or none at all as in the samples?
4. Do you confirm the keep/smooth choices in section 9?
5. How often may the book refer to your own work (HermAI, Argument Delphi, Kolay.AI)? Proposal: only where it is the best example, always with a citation and a disclosure.
