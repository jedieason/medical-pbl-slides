---
name: medical-pbl-slides
description: Build or revise a medical student small-group/PBL PowerPoint from a question and a case/unit PDF, with PubMed-verified web research, a local papers/ PDF collection, paper figures, trustworthy web visuals and clear explanatory structure, stepwise host-based clinical reasoning, detailed bilingual speaker notes, and the user's minimal white slide style. Use for medical PBL or 小組討論簡報 requests, not generic presentations or standalone literature summaries.
---

# Medical PBL slides

Produce the finished editable PPTX, not merely a research brief. Input is normally a topic/question plus a teaching-unit PDF. Communicate in Traditional Chinese; slides are English; notes use Traditional Chinese with English medical terms. The audience is preclinical medical students with no clinical-rotation experience. Teach all prerequisites and intermediate causal links in detailed reading articles in speaker notes.

Use this user's latest explicit instructions over these defaults. Do not invent case facts or hard-code the example patient's disease into a new task. Do not impose 10 questions, 28 slides, a mandatory cover, or an approval/upload checkpoint. A connected university VPN is a possible access route, not proof of full-text access.

## Route by task

- **New topic + unit PDF:** read [reasoning.md](references/reasoning.md), then [literature-access.md](references/literature-access.md). Build the evidence/slide plan before authoring. Read [presentation.md](references/presentation.md) at production time.
- **Content/notes revision:** inspect the latest actual deck and its notes, then read the relevant sections of reasoning and presentation. Search only for newly needed medical evidence.
- **Style/citation-only revision:** inspect the user's edited reference slide and latest files; read presentation only. Do not restart literature research or rewrite clinical content.
- **Implementation and recovery:** [operations.md](references/operations.md) contains tested package-editing rules, validation, scripts and bounded access retries.

Use the available presentation/PDF capability for actual rendering and export. Resolve its installed paths and runtime dynamically; do not assume a cached version number. No skill-specific external connector is required. Do not load unrelated PBL pipelines with conflicting styles merely because their names match.

## Essential workflow

1. Inspect available files and the provided PDF. Establish the question's scope and **time point**. Separate known, absent, unreported, inferred and later-revealed findings, with PDF page pointers. Do not use the unit's eventual answer as evidence available at initial presentation.
2. Build a host model and a sequence of small clinical questions. For each proposed test record: why this host needs it, expected finding, what a positive means, what a negative means, limitations, and next decision. Distinguish compatibility from confirmation and coexistence from mutually exclusive diagnoses.
3. Actively search PubMed and the wider web by these questions. Seek complementary, relevant reviews for the clinical framework and mechanisms, plus guidelines and primary studies for specific claims. Also consider trustworthy web articles and educational resources for clearer visual explanations; compare evidence quality, explanatory logic and relevance rather than selecting by prestige, recency or attractive artwork alone. Download every selected paper whose PDF is accessible into the task workspace’s `papers/` folder, including supplementary reading; do not stop at links, abstracts or a request for uploads when retrieval is possible. Follow [literature-access.md](references/literature-access.md) for retrieval, failed-access reporting and source records. Read the full texts and captions used in the deck. Never claim a formal systematic review without its methodology.
4. Save a compact evidence/slide plan using [plan.schema.json](assets/plan.schema.json). Track decisions once rather than repeatedly rediscovering them. Use a source ID across the plan, papers, figures and citations.
5. Draft one reasoning move per slide, planning the visual before the prose. Make paper figures, trustworthy web-resource illustrations, imaging, meaningful crops, plots and decision diagrams the main teaching mode wherever suitable evidence exists. Add a modest amount of explanatory text so the audience can see the premise, causal link and implication on the slide itself, rather than isolated keywords; keep full detail in notes. Use a cited editable explanatory diagram when the literature has no suitable original figure; never invent clinical data. Avoid a deck dominated by tables, repeated text columns or bullet summaries. Teach prerequisites before algorithms and put detailed interpretation in notes. Follow the visual selection and crop checks in [presentation.md](references/presentation.md).
6. Author in the style below. Write substantive notes that let a speaker prepare without reopening the whole research process. Keep full bibliographic entries visible in the final reference section.
7. Render, inspect, repair, verify note-to-slide correspondence and source mapping, then deliver a versioned PPTX. Preserve the user's edited source. Deliver links to both the versioned PPTX and `papers/`, with a brief, accurate count and any material access gaps; do not claim every sought paper was downloaded if some failed.

## Non-negotiable defaults from the approved final deck

- White background. Burgundy title `#800020`; body `#202124`; **selected inline keywords** `#5A8298`; citations `#5F6368`.
- No subtitle/step kicker, no `Next:` subquestion, no page numbers, **no bottom green takeaway bar**. Do not resurrect earlier orange/sage designs. Original paper artwork keeps its own colors.
- One main title plus an evidence-based visual and concise explanatory statements, or interpreted text/table. Functional body labels may reveal the reasoning structure; they are not decorative subtitles. No decorative stock pictures, AI medical images or filler icons.
- Figure citations: `Li et al. (2025), Figure 4E`. A crop is still cited by the original figure/panel; do not automatically prepend “Modified from” or “Reproduced from”. Use an adaptation disclosure only for substantive redrawing/recombination/changed scientific content. Teaching handout: author/year, handout name, page.
- Web visuals cite the specific article/resource with an author or organisation, date when available, and a clickable article link or formal web citation; do not cite an image-search results page. Short citations fit on **one visible footer line**. Complete APA entries belong on the final reference slide(s), not only in notes. Text synthesis may say “Synthesized from” when useful; it is not a claim of generated artwork.
- Notes are substantial, connected teaching articles for a preclinical student: normal foundations, mechanisms, figure/test interpretation, host-specific reasoning, competing explanations, result branches and next decisions. Each note has two ordered parts: a brief presentation cheat sheet first, then the complete detailed reading article. The cheat sheet never replaces or shortens the article. Persuade by explaining why conclusions follow, not by asking the student to memorize them. Do not treat the earlier v7 note length/depth as sufficient; this requirement supersedes it.

## Helpers

Run scripts with the resolved Python environment; each has `--help`.
- `scripts/fetch_pdf.py`: bounded download to a new local file, PDF signature/parser validation and provenance JSON. For public or institution-IP-authorized URLs; browser-authenticated downloads use the browser instead.
- `scripts/crop_figure.py`: render/crop a PDF region at adequate resolution and record exact source/page/bounds. No invented or AI-redrawn medical images.
- `scripts/deck_notes.py`: extract or replace notes using actual slide relationships; preserves slide artwork. Replacement requires a complete, matching slide list.
- `scripts/audit_deck.py`: detect missing notes, old template artifacts and citation formatting. A structural check, not medical or visual QA.

These tools reduce repetitive work. They do not replace source reading, clinical judgment, checking captions, or inspecting the rendered deck.
