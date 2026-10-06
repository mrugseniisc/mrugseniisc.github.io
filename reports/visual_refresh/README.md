# Paper artwork and contact refresh — 6 October 2026

Replaced the green palette with midnight blue, warm ivory, copper, and periwinkle. The former seven SVG diagrams are superseded by generated WebP illustrations in `site/assets/papers/`. The artwork is presented as conceptual explanation, with complete compositions and links to full-size views.

Read the linked primary papers (including their abstract, task, results, and discussion sections) before preparing the artwork briefs. The built-in imagegen tool produced each image separately. See [the complete prompt set](image-prompts.md).

| Asset | Scientific message and primary source |
| --- | --- |
| `preference-inference.webp` | [Human bargaining](https://www.biorxiv.org/content/10.64898/2026.07.09.737460v1): choices, response times, and gaze inform Bayesian preference learning in 75 dyads; gaze access changes cue use without improving overall performance. The final illustration uses four offers, matching the task limit. |
| `llm-cues.webp` | [LLM preference inference](https://osf.io/preprints/psyarxiv/bw5kq_v1): gaze helps; response times are used less effectively than by humans. Strong offer utility can coexist with imperfect preference recovery. |
| `value-evidence.webp` | [Affective symptoms and choice](https://www.biorxiv.org/content/10.64898/2026.06.09.731091v1): weaker value sensitivity during accumulation with decision caution largely intact; the two schematic accumulators retain the same boundary separation. |
| `social-prediction.webp` | [Predicted decisions for others](https://osf.io/preprints/psyarxiv/5ukqr_v1): earlier similar/self distinction precedes shared difficulty-related activity. Corrected the utility curves to increase with reward and replaced anatomical source hotspots with qualitative scalp motifs. |
| `process-models.webp` | [From DDMs to DNNs](https://doi.org/10.1037/dec0000239): a perspective proposing decision-process data and models for AI. The artwork depicts proposed applications, not a completed application experiment. |
| `visual-stream.webp` | [Natural and manmade images](https://www.biorxiv.org/content/10.1101/2022.09.22.509086v1): stronger categorical differences later in cortical and CORnet-S hierarchies. Human fMRI regions are V1/V2 and V4/LatOcc; IT appears in the model row. Mosaics are conceptual, not reproduced empirical matrices. |
| `protein-structures.webp` | [Side-chain dispersion](https://journals.iucr.org/m/issues/2022/01/00/fq5017/): cryo-EM structures show looser local side-chain packing than X-ray structures at comparable resolutions, including interfaces. The matched molecular cutaways are conceptual and do not identify a specific protein. |

Publication metadata was also aligned with the source records: the visual-stream title uses “manmade” and the author name Hilliard; the IUCrJ entry identifies the 2022 journal issue and December 2021 online publication.

## Contact handling

- Replaced public HTML email links with a contact page that reveals an encoded address after user activation. This deters ordinary scrapers and does not prevent determined bots from decoding client-side code.
- Prepared the public CV from the unchanged private two-page source. Removed email text and `mailto:` annotations, including reference addresses; the main contact line now points to the contact page. Historical Git commits and external publication files remain outside this protection.
- Added `scripts/prepare_public_cv.py` so future public CV copies can follow the same workflow.

## Validation

- Served with `python3 -m http.server 8000 --directory site`. Inspected all seven HTML pages at 320, 390, and 1440 CSS pixels in Chromium: no horizontal overflow; all artwork and CV previews loaded. Contact reveal was checked with a trusted mouse click, including keyboard focus on the revealed link.
- Fixed the missing 404 favicon and replaced an unreliable embedded PDF viewer with two rendered page previews. Rechecked the CV and 404 pages at all three widths with no failed network requests.
- Checked 110 internal references and anchors; none are missing. Public HTML/CSS/JS/SVG text contains no email addresses or inherited author names.
- Verified the public PDF has two pages, no extracted email addresses, and no mailto annotations. The original CV SHA-256 remains `7fe0c3ca2d82a80a6bcf947c492e319ff03eafcca0fb31c92769f90da04b432f`.
- `node --check site/contact.js` and `git diff --check` pass. Binary attributes prevent PDF cross-reference whitespace from being treated as source-code whitespace.
- Browser measurements and final CV/404 checks are recorded in [validation.json](validation.json); external HTTP checks are recorded separately. Some publishers block automated requests; source metadata and paper contents were checked through their official APIs or full-text PDFs.

GitHub Pages run `37464176985` successfully deployed implementation commit `20f9d2f`. All 23 published site files returned HTTP 200 and matched local bytes; see [deployment.json](deployment.json).
