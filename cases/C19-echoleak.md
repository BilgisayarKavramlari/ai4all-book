# Case: EchoLeak, a Zero-Click Prompt Injection in Microsoft 365 Copilot (2025)

Chapter: 15 (short case 1; Case Study only) · Field: enterprise software / security · Failure label: tree **security vulnerability**, leaf **indirect prompt injection**, **documented** (CVE-2025-32711) · data-flow map: attacker's email in the input box, an outbound link or image address in the output box · Outcome: mixed (critical flaw fixed by the vendor before public disclosure; no known exploitation)

## Context
Microsoft 365 Copilot is an AI assistant built into email and documents that retrieves a user's mail and files to answer questions (an assistant with retrieval, not an agent in Chapter 14's sense).

## Timeline
- Early 2025: researchers at Aim Labs (Aim Security) report the flaw to Microsoft's Security Response Center (reported).
- June 11, 2025: public disclosure; Microsoft lists CVE-2025-32711, "M365 Copilot information disclosure vulnerability", described as AI command injection (CWE-74), critical, CVSS 9.3; fixed on Microsoft's servers, no customer action needed; no known exploitation (Microsoft, 2025; The Hacker News, 2025, Jun 12). The finders class it as indirect prompt injection ("LLM scope violation") (Aim Labs Team, 2025).

## What the AI did
When a user asked an ordinary question, the assistant retrieved an attacker's email together with the user's own data; hidden instructions in the email could lead the response to include internal data in a link or image address that would send it out (summary level only; no bypass techniques described in the book).

## What humans did
Nothing was required of the victim (zero-click). The researchers disclosed responsibly; the vendor fixed the flaw server-side.

## Labels
Tree: **security vulnerability** (indirect prompt injection), **documented** by the vulnerability record and the finders' write-up (the EchoLeak tree figure in the Case Study). Map: input (outside email), connectors (the user's mail and files), output (outbound link) (the EchoLeak data-flow map in the Case Study). Chain: no loss known.

## Consequences (documented only)
A vendor fix; no known exploitation.

## A better workflow
Remove a leg of the risky combination where possible (no outbound links from responses that draw on private data), layer defenses, and treat retrieved outside content as untrusted.

## Questions
See Case Study Question 5.

## Sources (accessed 2026-10-18)
1. Microsoft. (2025, June 11). *M365 Copilot information disclosure vulnerability* (CVE-2025-32711) [Security update guide entry]. https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711 (read via the MSRC API by the fact-checker)
2. Aim Labs Team. (2025, June 11). *Breaking down "EchoLeak," the first zero-click AI vulnerability enabling data exfiltration from Microsoft 365 Copilot* [Blog post]. Aim Security. https://www.aim.security/post/echoleak-blogpost (title as published; the book does not repeat the "first" claim)
3. Secondary: The Hacker News (2025, June 12), https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html; AI Incident Database report 5307.
