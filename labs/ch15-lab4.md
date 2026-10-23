# Lab 15.4 — Same Frames, New Tool

| Field | Value |
|---|---|
| Type | Check It (optional; at home or in class) |
| Objectives | O1, O3, O5 (LO5); transfers Chapter 12's data gate and fit matrix (O4, O6; LO2) and section 15.7's threat-model vocabulary · tags 4D:DIL, 4D:DISC, 4D:DEL |
| Time | About 35 minutes (30 on the five steps, 5 on the debrief); the clock assumes a short look at each provider page and two test inputs |
| Materials | One AI tool of a kind you have not used in this book's labs, that you can already reach (built into an app you already have, provided or approved by your institution, or usable without signing in); one real, low-stakes task of your own with no personal or confidential data; the section 12.5 table; the evaluation sheet below (one page, also in the companion files). **No new account, install or device needed:** the dated sample pack in the companion files (or, if your course provides it, your instructor's): one tool kind, a dated terms extract, three provided inputs and three numbered, dated outputs from a real run, which replace every live step |

## Safety and privacy (read before you start)
- Do not create an account, start a free trial, install software or add a browser extension for this lab. If trying the tool would need any of these, use the pages-only route or the sample pack (see Alternative routes).
- Use only public information or your own non-sensitive work. No personal data about other people, internal or confidential information, or restricted or legally protected information, in any tool (the section 12.5 table). Use placeholders when the part does not need real names.
- Never record, photograph or upload anyone else (voices, faces, messages, documents) to test a tool. For a tool that works on recordings or images, use your own voice or work, or the sample pack.
- Use the tool only as its provider intends. Do not try to get around its safety rules, limits or paywall, or reveal its hidden instructions; none of that is part of this lab.
- On the sheet, name the tool by its kind (for example, "a note app's AI summary feature"), not by brand. Keep the product name and version in your own notes if you want to re-test it later.

## Steps (tool-neutral)
1. **Choose and describe (0–3 min).** Pick the tool by kind, using the section 12.2 table: for example, an AI feature inside a note-taking, photo, map, language-learning or slide app; a transcription or captioning feature; AI search; a domain tool for your field. It must be a kind you have not used in this book's labs. Answer section 12.2's four questions in one line each: what it receives, what it can do, where it runs, whose terms cover it. Then pick **one part** of a real task of yours that this kind of tool claims to help with, and name the tool you have used most in this book (your familiar tool).
2. **Data gate first (3–11 min).** Before any run, answer the three gate questions from the provider's own pages (training, retention and access, whose contract), recording each page's title and the date you read it. Give each question about 2 minutes; if the answer is not there, write "not found": that is an answer, and a reason for caution. Name your input's data class (its row in the section 12.5 table). Note what the tool can reach beyond what you give it (a whole document, folder, mailbox, photo library, microphone or location): each of these is part of its attack surface (section 15.7). Decide: **pass**, **pass after changing the input**, or **blocked**. If the gate blocks the tool, do not run it: skip step 3, mark the new tool's fit cell "do not use" in step 4, and rate the risks in step 5 from the pages.
3. **A short test (11–19 min).** Write one or two success criteria for the part. Run the part on two small inputs, each in a fresh session with memory and standing instructions off where the tool allows: a **typical** input, and an **edge** input, one that is unusual but possible and most likely to break the tool (Chapter 5). Record the tool kind, the model or version if shown, and the date. For each output, score correctness per criterion with an independent check (the source or your own recalculation), rate its **polish**, how finished it looks and reads, from 1 (rough) to 5 (ready to send) (section 12.6), and note the time, including checking. A third, **different** input is optional.
4. **Decide: one fit-matrix row and a short card (19–25 min; section 12.7).** One row for your part, with three cells: the new tool, your familiar tool, no AI. Each cell holds a decision (use; use with a named check; use only as a lead; do not use), its **rung** (the step of Chapter 12's Delegation Ladder: no AI, automation, augmentation or agency) and a one-line reason. Copy the familiar tool's cell from your A10 if it covered this part; otherwise write your best judgment and mark it "predicted". Mark the new tool's cell "tested once". Under the row, write four lines, *not for* first:
   - **Not for:** uses you have no evidence for, or that the gate blocks.
   - **For:** the part and the user you tested.
   - **Tested on:** the inputs you ran, the tool kind, the model or version if shown, and the date.
   - **Where it fails:** what went wrong on which input, what you did not test, and one re-test trigger.

   Chapter 19's workflow card (section 19.7) extends these four lines into five fields; this short card is its first draft.
5. **Two risks on the heat map (25–30 min; sections 15.5 and 15.7).** Rate two risks of this tool for this task, as it runs today, by the likelihood and impact anchors, each with **D** (your own run, the provider's written terms, a recorded case) or **I** (your reasoning), as hollow markers. For each risk, name the attack family from section 15.7's table (or "not an attack" for a risk such as the provider keeping your input) and the property at stake: confidentiality, integrity or availability. At least one risk should come from something this kind of tool receives, reaches or may do that your familiar tool does not (sections 14.6 and 15.7). Your own runs can document a risk here, because the tool and the kind of task are your own; one run shows that something can happen, not how often. A risk in the high-impact band gets a mitigation (avoid, reduce, detect, accept; section 15.6) or a named owner.

In Compass (optional): ch15-lab4, with the evaluation sheet and notes on where current tools show their data terms and version; also in the companion files.

## Expected observations
The frames apply without change; what changes is what they find. The gate is often where a new tool differs most: a feature built into an app may receive more than the part needs (a whole file, a library, a recording), and its data terms may sit on a different page from the app's, or be "not stated". Polish usually scores high while correctness varies on the edge input, as in Lab 12.1. In this book's reading, risks from what a tool reaches (a whole mailbox, a microphone) are mostly confidentiality risks, and risks from what it reads (a shared document, a web page) are mostly integrity risks through prompt injection. The familiar tool's fit cell rarely carries over, because a fit decision belongs to a task and a tool together. "Blocked at the gate", "pages only, not tested" and "no AI is faster" are complete, valid results.

## Debrief
Answer questions 1 and 4 in the 5 minutes (one line each, or a pair discussion); questions 2 and 3 are optional.

1. Which frame (gate, fit row, heat map, card) caught something you would have missed by judging the new tool's first output? Name the frame and the finding. (analyze)
2. Compare the new tool's fit cell with your familiar tool's cell for the same part: what changed, and was the cause the tool's kind, its terms or its outputs? (analyze)
3. Which of your risks would not appear on your familiar tool's heat map? Name its attack family and property (section 15.7), and the section 12.2 question that explains the difference. (evaluate)
4. Decide: would you add this tool to your workflow for this part? Justify the decision with one cell, one risk and one card line. (evaluate)

## Deliverable and rubric
The one-page evaluation sheet: tool description, gate, fit row with short card, and heat map. Ungraded unless your instructor uses it; it can support a new row in A12 or a tool column in a revised A10.

- **Exceeds:** every cell and risk has a stated reason and evidence mark, every risk names its family (or "not an attack") and property, and the debrief names a finding only one frame caught.
- **Meets:** all five parts complete, with the gate before the test, and D or I, a family and a property on every risk.
- **Approaching:** a part missing, or risks without evidence marks, family or property.
- **Not yet:** the tool was run before the gate, or the sheet contains personal or confidential data.

## Alternative routes
- **Pages-only route (no run):** if trying the tool would need a new account, an install or a trial, or the gate blocks it, complete steps 1, 2 and 5 from the provider's own pages; in step 4, mark the fit cell "predicted" and the card's *tested on* line "not tested". This is a full result.
- **No-account, no-device route:** use the dated sample pack in the companion files (or, if your course provides it, your instructor's): an AI notes feature that turns a recorded talk into a summary and action list, with a dated extract of the provider's data-terms page, three provided inputs (typical, different, edge) with their transcripts, and three numbered, dated outputs from a real run (tool kind, model or version, date). Do every step on paper; your familiar-tool column is "predicted".

## Accessibility and alternatives
The evaluation sheet is an accessible table, in print and screen-reader-friendly versions. The sample pack's audio inputs come with full transcripts, so every step can be done from text. If the tool you chose does not work with your screen reader, keyboard or other assistive technology, record that on the sheet: it is a fit reason, not a failure of yours. A phone is enough for a live run; without a phone or laptop, use the sample pack on paper. Inputs in any language are fine, with an English gloss of each criterion.

## Instructor notes
Setup: check that the dated sample pack in the companion files is available and current; if it is not, prepare your own from a real, dated run (terms extract, three inputs with transcripts, three numbered, dated outputs), never from constructed outputs. Prepare accessible versions of the sheet. Common problems: students choose a tool they have already used (ask for a different kind, not a different brand); students run the tool before the gate (step 2 comes first on the sheet); students want to test on a recording of a classmate or a meeting (offer the sample pack). Accept "blocked" and "pages only" as full results. Timing: the 30 minutes on the steps hold only with the 2-minute page rule in step 2 and two test inputs in step 3; a student who reads the provider's pages in full, or runs a third input, can need 45 to 60 minutes. It fits at home or as the second half of a lab session; the debrief can be a 5-minute pair discussion. Students who have not done A10 mark the familiar tool's cell "predicted"; that is not a penalty.
