# PubMed selection, institutional access and figure provenance

## Search only after identifying the information gap

Use PubMed to verify article identity and search concept-specific reviews. Also search the wider web by exact title/DOI to locate publisher downloads, repositories and complete article copies; PubMed is the metadata anchor, not the only retrieval route. Example query forms:
`[disease] review diagnosis differential`, `[mechanism] narrative review`, `[specific test] diagnostic accuracy systematic review`, `[disease] clinical practice guideline`.
Start with high-value queries, then search each relevant mechanism, diagnostic distinction and clinical decision. Compare multiple complementary papers and actively look through their figures and captions for clear teaching visuals, rather than stopping at one convenient overview. Keep useful supplementary papers in the local collection even when they do not require an additional slide. Seek complementary reviews covering the disease framework, host risks, treatment decisions and relevant adverse-effect mechanisms rather than repeatedly citing one overview. Stop when the question and important uncertainties are covered; do not pad the collection with irrelevant papers or impose a fixed review count. Review title/abstract for relevance before downloading. Prefer an appropriate guideline for diagnostic standards, a strong review for mechanisms and clinical framing, a diagnostic accuracy synthesis for test limitations, and primary research when the precise claim requires it. Newest is not automatically best; an accessible figure is not evidence quality. Record why each source is selected, population, type, recency and limits. Do not call this process a formal systematic review or a uniquely objective “best paper”.

### Expand the paper and figure search together

Search separately for the topic's mechanisms, pathways, diagnostic/treatment flowcharts, drug effects and relevant clinical evidence. Open complementary papers and inspect their full captions and figures; do not select only papers whose abstracts already support the planned prose. Build a broader useful PDF collection, including supplementary papers with relevant mechanisms or visual explanations, even if only some are ultimately cited. Prefer original mechanism diagrams, process schematics and algorithms when they explain the topic accurately. Record promising figure numbers, panels and their teaching use in the existing evidence plan/source records. A text claim being adequately cited is not by itself a reason to stop the visual search. Stop once the learning questions and useful visual needs are covered; do not use a fixed paper count or irrelevant downloads as a substitute for coverage.

## Trustworthy web articles and educational visuals

Search beyond journal PDFs when a trustworthy web article or resource explains the mechanism or decision more clearly. Suitable candidates include public-health agencies, professional societies, universities, teaching hospitals and reputable clinical educational publishers with identifiable authorship or medical review. These are starting points, not automatic endorsements. Open and read the actual article and caption; search-result snippets and image thumbnails are discovery aids, not sufficient evidence.

Compare relevant candidates for clinical accuracy, evidence traceability, author/reviewer expertise, editorial accountability, currency for the claim, audience suitability, completeness of causal steps and visual clarity. Prefer the source that best explains the specific learning question while retaining evidence quality. Record a brief selection reason rather than claiming an exhaustive or objectively “highest-quality” search. Do not favour a weak source because it has a convenient image, and do not assume the newest or highest-profile journal has the clearest explanation.

For treatment recommendations, numerical risks and disputed claims, verify against an appropriate primary study, guideline or high-quality synthesis. An educational illustration can explain anatomy or mechanism without serving as the sole authority for treatment. If the image is republished from a paper, trace and credit the original where possible and distinguish the host page from the original creator. Avoid unattributed reposts, promotional claims and unsourced social-media graphics as medical evidence. Check applicable reuse terms and preserve required credits.

Record web sources in `papers/sources.json` with `source_type: web_article` or `educational_resource`, author/organisation, title, published/updated date when available, exact article URL, retrieval date, relevant section/caption, visual origin, use and quality rationale. Store permitted local visual assets in `figures/` with provenance. Use an offered PDF when available; a web-only resource does not need a fabricated paper PDF and must not be counted as a downloaded research article. Cite the exact article/resource link or a formal web citation visibly on the slide, with complete bibliographic details in the reference section. Keep the following PDF collection requirement for selected research papers.

### Real equipment, drugs and structures

Also search for authentic images of the specific objects introduced in the slides: medical equipment and interfaces, drug products/packaging or dosage forms, anatomical structures and molecular structures. Suitable sources include official manufacturers, regulatory product labels, hospitals, universities and attributable image collections with appropriate reuse terms. Verify the image actually depicts the named item, model, drug/formulation or structure; open the source page rather than citing an image-search thumbnail. Manufacturer photos can establish product identity and appearance; verify therapeutic recommendations independently with clinical evidence.

These images may provide context and recognition without carrying the slide's central argument. For example, a photo of a nasal cannula can accompany an oxygen-support discussion even when the main point is a treatment decision. The deck should mix useful paper figures with relevant real-world medical visuals rather than restricting every image to a scientific result. Record the creator, exact source URL, depicted item, reuse terms and contextual purpose with the other visual assets. Do not imply that an illustrative device/product was used by the case patient unless the handout establishes that fact. Integrate image credits into the same final reference list as the other sources.

## Required local PDF collection

Create `papers/` under the active task workspace unless the user specifies another location. For each paper selected for slides or relevant supplementary reading, actively attempt PDF retrieval and save each successful complete article there. Reuse verified local PDFs by copying them into the collection without overwriting user files; deduplicate by DOI/version and file hash. Use readable filenames such as `Author_Year_Short_Title.pdf`. Do not download every search result indiscriminately.

Maintain `papers/sources.json` and a concise `papers/README.md` so the user can audit the collection. For each selected paper record:

- Source ID, title, authors, year, journal, DOI and PMID/PMCID when available.
- Selection rationale and role: cited in slides or supplementary reading; evidence type, population and limitations.
- Requested download URL, final resolved URL, hosting site, access route (publisher, repository, public copy or institutional browser), tool/method, retrieval time and local filename.
- PDF version (published article or accepted manuscript), page count and SHA-256; reading status separately from download status.
- Full-text/abstract-only/unavailable status, attempted routes and their actual results, and precise claim/figure/page locators for material used.
- Institutional-access evidence, if any. A reported VPN connection, a verified network route and publisher-recognised institutional entitlement are distinct facts; use `unverified` when appropriate.

Record the final URL at download time; an article DOI or landing page alone is not a download provenance record. If reusing an older PDF without its original URL, state that the historical download route is unknown rather than reconstructing it as fact. Keep failed HTML/challenge responses outside the deliverable `papers/` collection. Distinguish research articles from the case handout and product information. The README should list included papers, supplementary papers and unresolved access gaps, without claiming that publicly reachable hosting proves permission or institutional authentication.

## Retrieval ladder

1. Reuse a verified existing local PDF matching title/DOI; do not download duplicates.
2. Follow PubMed's publisher and PMC links. Prefer publisher original PDF or PMC/author-deposited full text.
3. Try the publisher DOI page and its actual PDF link. If a paper is available only in a complete journal issue, download the issue, verify title and printed pages, extract the exact article pages with a PDF library, and record both issue and article pagination. This route worked for Li et al. (2025): WestJEM issue → printed pp. 210–218 → 9-page local article. It did **not** prove VPN authentication.
4. For subscribed content, use the user's already connected university network/VPN and existing browser session. Native-machine network access may have the institutional route; a cloud tool/server may not. VPN does not transfer browser cookies to shell requests and does not bypass login challenges. Confirm that actual full text opens.
5. Search the exact title/DOI for an author or institutional repository, accepted manuscript, or a lawfully accessible complete copy hosted elsewhere. Verify article identity and version; clearly identify third-party hosting rather than calling it a publisher download. Check reuse terms for figures. If the PDF remains unavailable, record that gap and use another well-matched accessible source. If the exact paper is indispensable, request only the missing access action while continuing independent work. Never silently omit the failure or substitute an abstract/HTML printout and label it the original paper PDF.

## NTU VPN: do not pretend a universal recipe was proven

When the user reports an active NTU VPN, attempt available native-machine publisher requests or the authorised browser session rather than assuming a remote search tool shares that route. If claiming VPN use, verify and record relevant native routing or egress evidence when available; a current check does not prove the route of an earlier download. Separately record publisher-recognised institutional access if actually observed. Without those checks, say “download attempted while the user reported VPN connected; routing/entitlement unverified”. A 403 response may be an access or automation restriction and does not establish a missing subscription. A successful public PDF download does not establish a subscription benefit.

Do not invent an NTU proxy prefix or library entitlement. If a specific library route is needed, consult current official NTU library instructions. Never disconnect/reconfigure the user’s network as a routine download step.

Use available browser automation when the user's session is needed. Inspect page state, follow the actual full-text/download link and save into `papers/`. If CUA is available, initialize via its documented entry point and use only exposed browser APIs. Do not scrape cookies, reuse credentials outside the browser, or extract VPN secrets. A normal publication PDF download is within the research request; logins/2FA or new paid purchases require the relevant user action. Do not bypass a paywall or defeat access controls.

## Bounded retries and verification

Per paper, try a small number of distinct routes (e.g. publisher, PMC/repository, institution browser). A 403/challenge response calls for a different route, not dozens of identical retries. Use timeouts; parallelize independent public metadata reads where supported, not interactive login/download sequences.

Do not trust `.pdf` extension or HTTP 200: check `%PDF-`, parse page count and text, confirm title/DOI and page continuity. A login HTML document renamed PDF is a failed download. `scripts/fetch_pdf.py` implements a bounded unauthenticated/IP-authorized download; it cannot access a browser-authenticated session. For URLs from a trusted observed source, pass the URL as a structured argument, never interpolate unescaped shell strings.

Read actual full text and captions before detailed claims or figure use. With abstract-only sources, limit claims to the abstract and mark the access status. Do not invent figures, methods, thresholds, or full-text reading. If only HTML full text is available, record it as HTML full text and the PDF as unavailable; do not claim the article is abstract-only when its full text was read. An explicitly requested print-to-PDF version must be labelled as such, not as a publisher PDF.

## Figures

Record article ID, original Figure/Table number, panel, PDF page index, printed page, crop bounds, caption and permission/license information when available. Extract embedded raster images where they preserve the complete intended figure; otherwise render the relevant PDF page at high resolution and crop. Use `scripts/crop_figure.py` for deterministic rendering plus provenance. Aim for at least the final displayed pixel dimensions, often 2×. Inspect the result at presentation size.

A crop must not remove essential axes, legends, comparison arms or caveats. Preserve original annotations and colors; do not recolor medical evidence to match the theme. Distinguish a patient image from a published illustrative case. Avoid fabricated AI CT/pathology and unrelated decorative medical pictures. Relevant real equipment/drug photos and sourced anatomical or molecular illustrations are valid contextual visuals; distinguish them from clinical evidence.

Visible attribution for a direct figure/crop is `Author et al. (year), Figure 3A`. For a teaching handout with no verified original mapping, cite the handout and page; do not invent an original paper. An actual redrawn/adapted diagram needs an accurate adaptation disclosure, but a simple crop does not automatically get “Modified from” in this user's style. Preserve any mandatory license notices without crowding the slide; allocate a visible reference/credits entry if necessary.
