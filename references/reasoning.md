# Clinical question decomposition and speaker notes

## From the unit PDF to a model

Extract the case chronology before reading its final diagnosis as an answer. Keep page numbers with each fact. Use these categories: confirmed present; explicitly denied/normal; unreported; working inference; later evidence. Missing family history is not negative family history. The host includes age/sex, disease, anatomy, previous therapy, current drugs, immune state, smoking, occupational/home exposures and relevant family/personal history. Only use factors with a plausible relationship to the specific question. Do not manufacture a demographic risk estimate.

Turn each relevant fact into a causal path:
`host feature → mechanism → candidate cause → expected clinical evidence → discriminating observation/test`.
Rank which causes must be assessed first using likelihood, consequences of missing them and whether treatment conflicts. Do not assign numerical probabilities without data. A host can change: corticosteroid exposure after the initial presentation creates new infection risks. Some diagnoses coexist.

For example, in the source case (an illustration, not a reusable medical answer): recurrent esophageal cancer led to questions about obstruction/tumor and aspiration; nivolumab plus chemotherapy led to drug injury and immune-state questions; remote radiation required timing/field comparison; renovation work required identifying the actual material, not calling every dust exposure HP. The clinical topic and supporting evidence must be re-established for each new unit.

## A paced narrative

The questions below are a planning scaffold for the teaching sequence, not ready-made slide titles. Translate each into a title naming the actual mechanism, finding, test or decision taught on that slide, following presentation.md.

A useful shape, adapted to the question rather than enforced as a fixed slide count:
1. What is the presenting problem at this time point?
2. What do we actually know about this host and timeline?
3. What does the finding mean descriptively?
4. Which initial cause is plausible, and why?
5. What prerequisite mechanism must we understand?
6. Can that mechanism produce the observed finding?
7. What does a published example show, and what does it not prove?
8. What are the limits of that image/pattern?
9. How urgent is the patient's physiology? In a real emergency this is assessed immediately and in parallel, even if explained here in a teaching sequence.
10. What evidence is still missing before diagnosis?
11. Evaluate relevant alternatives in small steps. Split positive and negative test interpretation when educationally useful.
12. Only now show the integrated algorithm.
13. Apply it with known/unknown evidence to the case; state diagnostic confidence.
14. If the unit provides later events, explicitly move the time point and update the model.
15. Answer the assigned question, followed by visible full references.

Keep the deck as a connected explanation of the assigned question rather than a collection of related facts. For each slide, identify what it adds to the previous slide and why the audience needs it before the next. Add a brief causal or question-to-answer bridge where needed; do not force a dramatic story or invent case events. Delete or merge tangents, repeated background, and source summaries whose removal would not change the audience's understanding or the final answer. Choose only the parts of the scaffold above that serve this topic.

One slide should not jump from “drug given” to “immune injury confirmed”. Avoid algorithm-first lectures or exhaustive lists. If a diagram requires several new concepts, crop one intact branch at a time and introduce its terms. Repeat a source image only if it helps revisit the same decision; never as visual filler.

## The test-decision contract

Before recommending any test, fill these fields in the evidence plan; retain the relevant interpretation and decision cues in notes:
- Clinical uncertainty and why this host makes it relevant.
- Test/specimen/timing, including prior treatment that affects yield.
- Predicted finding if the candidate cause is correct.
- Positive: which hypothesis is strengthened, whether contamination/colonization/nonspecific response is possible, what action follows.
- Negative: what was genuinely tested, sampling/sensitivity limits, whether residual concern warrants a different test.
- Safety/feasibility and whether the result would alter management.

Do not turn a negative culture into “no infection”, a compatible CT into proof, a biomarker into a disease-specific test, or steroid response into etiologic confirmation. Do not order the same expansive panel for every host. Distinguish diagnostic confidence, urgency and treatment choice. These are general reasoning cautions, not substitutes for disease-specific guidelines.

## Presenter notes: minimal plain-text cues

Notes are for scanning during a live report, not for reading a textbook or a full script. Use Traditional Chinese with English medical terms. Write short plain-text lines separated by line breaks; no Markdown headings, bold markers, tables, nested lists, or two-part sections. Do not append a detailed reading article. Aim for roughly 3–5 short lines on a typical slide, adjusting only when the actual content requires it; there is no mandatory count or character quota.

Keep the lines in speaking order. Include the slide's main point, the essential “because → therefore” connection, what to point out in the figure or test, and what it means for this case. Include a caveat or next-slide transition only when needed. Use natural short phrases that cue the explanation, not isolated keywords or long sentences to read aloud. Explain an unfamiliar term briefly at first use if it is needed for understanding.

For a test, retain why it is relevant, what a positive or negative result changes, and the key limitation. For a figure, cue the feature to point at and what it supports; preserve any limitation that would otherwise make the claim misleading. Keep bibliographic details in the visible reference section, not in the scanning notes. Research and the evidence plan must still support these cues; brevity does not justify skipping verification or overstating certainty.

Illustrative note style (not a medical claim to reuse without source checking):
陰性培養：這份檢體未培養出病原，不能直接排除感染
先前治療／採樣位置 → 可能降低檢出率
若仍高度懷疑 → 評估更合適的採樣方式
下一頁：哪些證據能區分剩下的原因

Read each note alongside its slide as if presenting: can the speaker find every essential cue with a quick glance, follow the speaking order, and state why the conclusion follows? Shorten repetition and peripheral detail; retain the causal link and any qualification essential to accuracy.

## Content QA

Check that every claim has an appropriate source, uncertainty is retained, and the answer addresses exactly the assigned question. Later results must not leak into initial reasoning. Figure patterns must not become causes; a general-drug algorithm must not silently become a disease-specific diagnostic standard. Check all acronyms in the visual are explained somewhere accessible in the corresponding notes. Ensure each test's negative branch says what remains possible, rather than just “rules out”.
