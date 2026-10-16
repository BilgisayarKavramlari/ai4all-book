---
name: ai4all-author-voice
description: Builds a voice profile from the author's own writing samples and edits AI for All drafts toward that voice without changing facts, structure or citations.
---

# AI for All — author voice

## Mode A: build or update the profile
1. Read every sample in docs/voice/samples/ (the author's own English writing: articles, blog posts, lecture notes, emails). Ignore anything not written by the author.
2. Write docs/voice/voice-profile.md with: typical sentence length and variation; how paragraphs open; favorite transitions and phrases; use of "I" and "you"; humor level; how the author handles examples from industry and teaching; words and constructions the author never uses; 5 short representative excerpts (under 40 words each).
3. Note constructions that read as Turkish-influenced in English and mark each as "keep (part of the voice)" or "smooth (likely to confuse readers)". Ask the author to confirm these.

## Mode B: voice pass on a draft
1. Read docs/voice/voice-profile.md. If it is missing, run Mode A first.
2. Edit for voice only: rhythm, word choice, transitions, openings, personal register.
3. Do NOT change facts, numbers, citations, objectives, headings, figure references, or the meaning of any sentence.
4. Do NOT invent anecdotes or opinions for the author. Leave `[AUTHOR ANECDOTE NEEDED]` markers in place.
5. Output the revised text plus a short list of the kinds of changes made, so the author can accept or reject them.

The author always makes the final voice edit. This skill prepares the draft for it.
