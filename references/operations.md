# Production operations and failure recovery

## Persist just enough context

Use a task-local structure:
`papers/` verified PDFs + `sources.json` + user-facing `README.md`; `figures/` crops + provenance; `.build/plan.json` + render/QA intermediates; `output/` versioned final PPTX.
Do not put private case PDFs, downloaded literature or this project's clinical deck inside the installed skill. The reusable skill contains methods and design tokens, not a hidden case database. Keep the last completed step, source status and pending decisions in the plan when work spans turns.

Use the available workspace-dependencies resolver to discover Node/Python/libraries. Resolve current presentation/PDF skill paths from the available catalog, and if stale search the installed cache for the current skill. In the originating session the presentation package changed from 26.905 to 26.909; hard-coded finalizer imports then failed. Fix the path, do not unnecessarily rebuild the entire deck or claim export succeeded.

## Build or edit

Use the presentation runtime supported in the current environment. The originating workflow used `@oai/artifact-tool` to import/render PPTX and validate/export, with Python zipfile/lxml for surgical OOXML edits. If available, follow its current skill implementation/finalization instructions; do not rely on a stale copy of a library API. Standard artifact-tool rendering in that environment:
```js
const p = await PresentationFile.importPptx(await FileBlob.load(inputPath));
const png = await p.export({slide: p.slides.items[index], format: 'png', scale: 1});
```
Inspect the available API before using it in a new runtime.

For OOXML editing, start with a copy, preserve untouched ZIP members, use actual relationships to map slides/notes/media, and never infer that notesSlideN corresponds to visual slide N in every deck. Keep namespaces and schema child order. In particular, appending a:solidFill after font elements inside a:rPr broke package validation; preserve/insert fills before font elements. Do not wipe full text-body formatting to change one phrase. `deck_notes.py` provides a scoped replacement for existing notes bodies, preserving all slide parts and media.

Do not append hidden full bibliography text to notes when the user wants visible references. Do not mistake notes-page print overflow for text loss in Presenter View, but ensure the full note text is actually present and mapped correctly. A separate notes document is optional only when requested.

## Validation gates

1. Clinical: question answered, evidence supports claim, host assumptions explicit, each meaningful test has result branches, cited population/algorithm not misrepresented.
2. Source: every selected paper has a verified local PDF in `papers/` or an explicit unavailable status and attempted routes. Downloaded PDFs match their identity, version and recorded source URL; download and reading statuses are distinct. Check exact figure/panel/page mapping, complete visible references, and no altered scientific information or mislabeled case images. Do not infer institutional/VPN access from download success.
3. Visual: render all slides; inspect a montage for overall flow and every slide at full size. No clipping, tiny paper text, extra subheading, footer wrapping, old green bar or irrelevant highlighting. Reuse exact scientific colors.
4. Package: run available integrity/layout/import checks. `audit_deck.py` is an additional narrow content check, not a replacement. Unsupported mandatory validator options should be resolved through current runtime docs.
5. Notes: match by slide relationship/title, compare complete saved notes against authored text. Check background explanations and transitions, not only length.
6. Preserve user data: verify unchanged artwork/media for a notes-only operation. Deliver to a new versioned filename; finalizers may refuse overwriting existing files, which is expected.

## Fast iteration

Fix the actual finding and rerun affected checks. Examples from this project: footer text clipped at slide bottom → shorten to author/year and a single line; colored bars unwanted → remove only the known shape, not all green pixels in scientific images; newest user style exists in v3 while generated v5 exists → inspect the real current source and preserve latest intentional edits.

Avoid repeated all-source browsing for formatting tasks, blanket re-rendering between tiny dependent text changes, inventing new diagrams when the paper figure is sufficient, and reconstructing an already verified paper manifest. User permission is not required simply to perform authorized reversible drafting/edits. Browser login, missing indispensable data or external purchase are different constraints; explain only actual blockers.
