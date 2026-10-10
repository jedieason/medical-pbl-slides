# Approved presentation specification

## Source of truth and layout

This is the user's final preference after multiple revisions, calibrated against the final v7 deck. Earlier orange strips, green takeaways, step labels and `Next:` prompts are obsolete. For future edits, inspect the actual latest file and user's reference slide; a lower version filename can have newer user edits. Preserve all user edits, not just the filename with the largest version. Do not overwrite an open source file. For new topics, use these design tokens; do not reuse the old case's medical content.

16:9, white. Reference canvas 1280×720 px / 12192000×6858000 EMU. One pixel = 9525 EMU at this canvas. The reference title box: x64, y48.5, w1152, h88. Arial bold 33 pt (44 px), burgundy #800020. Main body #202124; major labels ~25.5 pt (34 px), ordinary body ~21.75 pt (29 px). Adjust within the reference's visual hierarchy for actual content, preferring less text over smaller type. Select only meaningful words inside a line in #5A8298; do not color an entire paragraph or highlight every noun.

Footer: right aligned, #5F6368, Arial 10.5 pt (14 px), x64, y672, w1152, h30 px. Single line; shorten references rather than shrink type or allow overflow. No DOI/journal/volume/page bibliography on teaching-slide footers. Keep citation wording plain and unlinked; when linking a source, append a short ` | Link` anchor, and underline/link only `Link`. Avoid extra headings, page numbers, next-step text and bottom takeaways. The old #F6AE2D and #CAD5C4 bars are not part of the current style. Original artwork may legitimately contain those colors.

Content region roughly y165–550. A large figure should usually have a small amount of explanatory text that makes its teaching purpose and logic visible. A figure-only slide is appropriate when the figure itself clearly carries that structure. Maintain image aspect ratio and fit. The reference case image was 370×370 px with rounded corners; source scientific tables/plots can retain rectangular boundaries to preserve labels. Do not force rounding if it clips meaningful content. Image plus concise text is appropriate when the text supplies the host link. White space after removal of a takeaway bar need not be filled.

## Content and emphasis

Prefer a cropped original figure over newly transcribed prose when it actually teaches this step. A table is useful only when it makes a comparison/decision apparent: highlight the important row/cell/phrase with a reason, retaining negative-result limits. Do not turn every slide into a table or colored card grid. Use relevant real equipment/drug photos and sourced anatomical or molecular illustrations to make abstract discussion concrete. Avoid unrelated decoration, stock pictures, fabricated AI medical imagery, arbitrary icons or invented patient diagrams.

### Slightly fuller text, with visible reasoning

Increase explanation modestly, not to paragraph-heavy slides. Prefer two or three compact explanatory statements, often one or two lines each, accompanying the main visual. Each should express a relationship or implication, not merely name a topic. For example, replace “Renal function / Drug levels / Toxicity” with “Reduced renal clearance can increase drug exposure” and “Use renal trends and timed levels to guide dose adjustment”. This is a writing example, not a required clinical claim or fixed slide template.

Make the slide’s reasoning readable without opening the notes: what is observed or assumed, why it matters, and what follows. When useful, use brief functional body labels such as “Mechanism”, “Case relevance” or “Clinical implication”, or number genuine sequential steps. Vary this structure to suit the content; do not force every slide into three columns, cards or a repeated framework. The existing ban on decorative kickers/subtitles does not prohibit these meaningful body labels.

Add only the missing connective explanation. Do not duplicate everything already labelled in the image, fill all white space, add an unrelated summary bar or reduce the established font sizes to fit more prose. Put the mechanisms and qualifications essential to understanding the claim on the relevant slides; notes retain only concise speaking cues, not full explanations. At review, check both extremes: isolated words that hide the reasoning, and dense text that competes with the visual.

### Plan and teach through visuals

For each teaching slide choose the representation that makes its reasoning visible: a mechanism diagram from a paper or trustworthy educational resource for pathophysiology, an original diagnostic/treatment algorithm for decisions, a labelled CT/MRI/pathology panel for manifestations, or an original research plot for evidence and uncertainty. Prefer these to transcribing a paper into a new table. Choose the clearest accurate visual from papers or trustworthy web resources; being a paper figure alone does not make it the best teaching choice. When suitable sourced figures are available, they should form the main teaching material across the deck, not a token image on an otherwise text-heavy presentation. There is no mandatory image percentage or single-table quota; retain a table when the comparison itself benefits from one.

Complement scientific figures with actual medical equipment, drug/product photos, and anatomical or molecular structures from trustworthy sources. These can show what an object looks like and make the slide more visual and engaging; they do not need to be the slide's main argument. For example, pair an oxygen-device discussion with a photo of that device, or a drug discussion with verified packaging or its molecular structure. Choose images of the item actually named and cite the source. A relevant contextual photo need not be converted into a data figure or forced into a mechanism explanation. Use a varied mix of paper artwork and real medical objects across the deck, with meaningful image sizes and concise text; avoid long runs of pure-text slides when useful visuals are available.

Use a full-width figure or a large figure with two or three brief interpretative statements. If a dense figure cannot be read at presentation size, split it into meaningful panels or decision branches across slides; preserve each branch’s context, arrows, axes, legends and denominators. Explain which portion is shown. Do not reuse the same crop merely to increase image coverage. When no suitable original exists, a simple editable causal or decision diagram may synthesise cited evidence; label it as a clinical synthesis, not a published figure or patient finding.

For explanatory/evidence visuals, notes should briefly cue where to point, the key observation, its interpretation and case relevance, and any limitation essential to avoid a misleading claim. For contextual equipment/drug/structure images, a brief identification or useful recognition cue is sufficient; do not invent an evidence interpretation or patient-specific use. Distinguish a published illustrative patient from the actual case. Explain observational study selection and uncertainty alongside plots rather than implying causation or equivalence from their appearance.

Render and inspect every slide at full presentation size. Check especially for cut-off labels, fragments from adjacent panels, missing legends, tiny algorithm text and graphs separated from their numbers-at-risk table. Adjust the crop or layout rather than shrinking everything to fit. Preserve original scientific artwork and lettering, including its original spelling; newly authored prose and notes follow the user’s requested language and English variant.

### Specific slide titles

Write one concise English title that lets a medical student identify the slide’s actual subject and teaching purpose before reading the body. Name the relevant mechanism, imaging finding, test, exposure or clinical decision, and make its relationship or interpretive focus clear. A title should distinguish this slide from neighbouring slides; if it fits several unrelated slides unchanged, make it more specific.

Choose the form that suits the content: a specific topic phrase for an overview, a relationship statement for a supported mechanism or conclusion, or a concrete question when the slide answers that question. Questions are optional. Avoid generic prompts such as “What does this mean?”, “What mechanism must we understand?” or “What evidence is still missing?” without naming the actual subject. Do not copy abstract planning questions from reasoning.md into slide titles.

Illustrative rewrites, not fixed titles or medical claims to reuse:
- “What mechanism must we understand?” → “How PD-1 blockade affects immune tolerance”
- “What does this pattern mean?” → “Ground-glass opacity: possible causes”
- “What evidence is still missing?” → “Evidence needed before diagnosing drug-induced pneumonitis”

Keep wording natural and readily understandable to a preclinical student. Prefer familiar medical terms and explain essential unfamiliar terms in the slide or notes. Include the case connection when it clarifies this particular slide; do not repeat the patient or diagnosis in every title. Prefer a single line when practical, but do not force a word count or remove essential qualifications to fit.

Match the title’s certainty to the visible evidence and the current case time point. A compatible pattern or suspected cause must not become a confirmed diagnosis in the title, and later case results must not leak into earlier titles. Avoid packing several reasoning steps into one title; split the slide when those steps require separate teaching.

One main title only; body questions are acceptable when they are the actual reasoning being taught, not a repeated navigation subtitle. Use concise notes to cue the explanation; do not add an on-slide summary strip. During review, check that every title names the specific subject, matches what the slide actually teaches, and remains supported by its evidence.

## Citations and notes

- Original paper figure: `Li et al. (2025), Figure 4E`.
- Web article/resource: `Organisation or Author (year), Short article title | Link`, with only `Link` underlined and linked to the exact article. Use `n.d.` if undated. Include the full web citation and URL in the visible reference section; credit an independently named figure creator when applicable.
- Several panels: `Raghu et al. (2020), Figure 1A–C`.
- Handout: `Huang et al. (2025), Unit 1 handout, p. 1` (only if these authors are actually in the current handout).
- Other supporting source on the same line: `Li et al. (2025), Figure 3; Conte et al. (2022)`.
- A synthesized text-only slide: author/year list; “Synthesized from” is optional and accurate for the synthesis.
- Do not label a direct screenshot “Modified from” merely because it was cropped. An actual scientific adaptation/redraw requires disclosure of what changed and its source.

For a web source, use the verifiable author/organisation, published or updated date, article title, website name (omit if identical to the author) and direct URL. Add a retrieval date for undated or changing resources where appropriate; never invent a DOI, author, date or figure number. A short `Link` anchor keeps the footer readable while leaving the author, date and article title plain.

### Continuous References layout

Put full APA references visibly at the end in one continuous list. Include all cited papers, guidelines, web resources, teaching handouts, exam sources and required image credits in this same list; do not divide it into topics, source types or separate image-credit sections. Use a consistent order across pages, normally APA author/year order, with the title `References` on each page and no category headings.

Use exactly one bibliography body text box per reference slide, with each citation as a separate paragraph inside that box. The slide title remains a separate title box. Do not create a separate text block, card or column for each citation or source group. Split each citation into plain bibliographic runs and separate URL/DOI runs inside the shared body box. Only the displayed URL/DOI is underlined and clickable; link it to that exact URL/DOI. Author/year, article title, journal, volume/pages and source labels must have no hyperlink and no underline. Never apply a hyperlink to a whole entry, paragraph, footer or text box, and do not inherit hyperlinks/underline from paragraph defaults. Verify both rendered appearance and the exported run/relationship targets; a clickable URL alone does not prove surrounding prose is unlinked.

Paginate by actual rendered text height at a readable font size and ordinary paragraph spacing: put as many complete entries as fit on the first page, then continue the remaining entries on the second, and repeat as needed. Do not preallocate a page count, limit each page to a fixed number of sources, or begin a new page because a topic/source category changes. Use the available reference-page body area rather than leaving room for a teaching-slide footer. Wrap long entries normally; keep a whole citation on one page whenever possible. Start the next page only when the next complete entry will not fit. Do not shrink the text excessively or squeeze spacing to force everything onto one slide; the last page may naturally be less full.

Render and inspect every reference page for overflow, tiny text and avoidable unused space before a continuation page. Include every cited source and no uncited padding. Notes remain minimal plain-text cues according to reasoning.md; do not duplicate the bibliography in notes.

## Highly relevant Taiwan physician licensing past-exam slides

During new-deck research or a requested content expansion, search 醫師國考考古題 using the specific concepts, mechanisms or decisions covered in the deck. Search both stages as relevant to the topic; the audience's preclinical level alone does not exclude a directly relevant second-stage question. Prefer 考選部 original papers and official answer keys. A searchable question bank may help discovery, but verify wording, options, year, sitting, stage/subject, question number and answer against the official source when available. Check revised keys, cancelled questions and multiple accepted answers. Do not label an unverified or self-written question as a past exam. Record the question source URL and answer-key URL in the evidence plan/source record.

Include a question only if answering it directly uses the specific concept or reasoning taught on the immediately preceding slide(s). Sharing a disease name, drug name or specialty is insufficient. Record a short overlap rationale in the plan. Prefer the best match rather than inserting several repetitive questions; there is no exam-question quota. If no verified high-overlap question is found after a focused search, omit the exam slide and briefly report this in delivery. Do not broaden the teaching scope just to make an exam question fit.

Place the question immediately after teaching the corresponding concept, before advancing to the next concept. Inspect [the user's exam-slide layout reference](../assets/exam-slide-reference.png) when authoring these slides. Match the white slide area of the example, excluding the surrounding dark screenshot frame: white background, large black serif text, original question number and stem near the upper-middle left, A–D (or the original option labels) on separate left-aligned lines below, generous white space, and a black source label near the lower right. Use only the verified year–sitting–subject label, such as `107-2-醫學（二）` or `115-1-醫學（一）`, at the lower right. Do not append `／第一階段`, stage descriptions, question numbers or other metadata to this on-slide source label; keep detailed provenance in the plan and final references. The original question number is part of the stem, not a slide page number. Use editable text and a suitable Traditional Chinese serif font with an English serif companion. Preserve the exam's original Chinese/English wording, symbols and options: these slides are an exception to the usual English-slide, burgundy-title and one-main-title defaults. Do not add a decorative header, image, takeaway bar or answer highlight to the question slide.

### Exam text wrapping checks

Keep the question number and every option label beside the first line of its text, never stranded on a line above it. Use separate label/body text boxes with a consistent hanging indent, or reliable paragraph tabs/indents; do not rely on automatic list formatting or a mixed-font string that may separate `8.`, `A.`–`D.` from the content. Give English runs a suitable English serif font (for example Times New Roman) and Chinese runs a Traditional Chinese serif font (for example Songti TC), explicitly configuring the script fonts. If the renderer ignores East Asian font attributes, split Chinese and English into explicit font runs and check the result again.

Choose line breaks by the rendered line width. Preserve the original wording while avoiding closing punctuation stranded at the start of a line, isolated final characters, split English words and broken medical names such as `Treponema pallidum`. Add intentional breaks at a meaningful phrase boundary and enough height/spacing for the complete stem and each option. Keep continuation lines aligned with the body, not the option label. Do not reduce type excessively to force long text onto one line.

Render every exam slide at full size after exporting/re-importing the PPTX. Inspect the complete question number, first line, every option label and continuation, English names, punctuation, source label and bottom boundary. Compare the normalized wording against the official question separately from the visual check. Fix actual wrap/spacing problems and render again; source extraction or an overlap validator alone cannot establish correct line breaks.

Put the verified answer and one short explanation connecting it to the preceding concept in the minimal plain-text presenter notes; add a brief misconception cue only when useful. Keep the answer off the question slide unless the user requests a reveal. Include the exam-paper and answer-key links in the visible final references, without crowding the sample layout. The attached Paxlovid question illustrates layout only; do not assume its metadata or answer is verified and do not reuse its content in unrelated decks.

## Revision discipline

For style-only edits, preserve original media and notes. For note-only edits, preserve slide artwork. For citations, change only relevant text and the notes' attribution explanations. Do not casually rebuild a user's current deck from an older generation script: that restored obsolete bars and citations during earlier iterations.

Inspect rendered slides, especially the longest title, longest footer, smallest scientific figure and final references. Check note mapping and complete text independently of the visual render; slides looking good does not prove notes were saved.
