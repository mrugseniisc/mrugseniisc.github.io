# Scientific paper illustrations — 6 October 2026

Replaced all seven cinematic paper images with original scientific schematics generated using the built-in image generation tool. Read the task, methods and results in the papers and inspected the reference figures before generation. Images use aligned panels, explicit task variables and model connections, with navy, periwinkle and copper on a light background. They explain scientific structure; they are not reproduced empirical figures.

| Image | Source figures and scientific constraints |
| --- | --- |
| `preference-inference.webp` | [Human bargaining](https://www.biorxiv.org/content/10.64898/2026.07.09.737460v1), Figure 1, PDF page 3. Hidden buyer preferences versus visible item scores; up to four offers among twelve alternatives; optional gaze and Bayesian preference updating. No claim that gaze improves overall earnings. |
| `llm-cues.webp` | [LLM preference inference](https://osf.io/preprints/psyarxiv/bw5kq_v1), Figure 1, PDF page 4. Interaction history encoded as text, four cue conditions, distinct utility and preference-recovery outcomes. Gaze is the first-fixated attribute, not raw coordinates. RT adaptation differs across models. |
| `value-evidence.webp` | [Affective symptoms and choice](https://www.biorxiv.org/content/10.64898/2026.06.09.731091v1), Figure 2, PDF page 6. Equal-probability mixed gamble, accept/reject, value-weighted drift, matched decision boundaries. Trajectories are schematic and scalp activity is not a measured map. |
| `social-prediction.webp` | [Predicted decisions for others](https://osf.io/preprints/psyarxiv/5ukqr_v1), Figures 1 and 4, PDF pages 6 and 19. Self choices, agent learning and prediction; similar/dissimilar preferences. Risk curves show one example participant. Earlier reliable self/similar contrast does not imply a reliable self/dissimilar contrast; later difficulty effects are shared. Scalp icons do not imply source localization. |
| `process-models.webp` | [From DDMs to DNNs](https://doi.org/10.1037/dec0000239), Figure 2, PDF page 12. Same final choice can reflect different processes. Proposed training uses prior observed stimulus, gaze, pupil, EEG/fMRI and choice. Predictions and observations enter comparison; error feeds the network; observations feed the next step. This is a proposal, not a validated training experiment. |
| `visual-stream.webp` | [Natural and manmade images](https://www.biorxiv.org/content/10.1101/2022.09.22.509086v1), Figures 2–3, PDF page 4. Human fMRI V1/V2/V4/LatOcc versus CORnet-S V1/V2/V4/IT. Overlapping qualitative distributions illustrate more pronounced late category differences without fabricating values. |
| `protein-structures.webp` | [Side-chain dispersion](https://journals.iucr.org/m/issues/2022/01/00/fq5017/), Figure 1, PDF page 3. Comparable resolutions, looser cryo-EM side-chain packing and overlapping distributions. Generic molecular neighborhoods avoid invented chemical identities or altered bond geometry; interface geometry is conceptual. |

## Generation and display

See [image-prompts.md](image-prompts.md) for scientific briefs, generation prompts and targeted corrections. Final raster outputs were encoded as lossless WebP without visual alteration. [assets.json](assets.json) records dimensions, file sizes and SHA-256 hashes. Source PDF renders were used as references, not added to the public site.

Publication illustrations now occupy the full article width and follow the citation and author line. Research captions and publication entries offer full-size links. Alt text describes each schematic. Every image displays its full composition without cropping. Curves and results-style drawings are explicitly schematic, not numerical evidence.

## Validation

Preview command: `python3 -m http.server 8000 --directory site`.

The affected home, research and publication pages were checked in Chromium at 320, 390 and 1440 CSS pixels. Checks cover horizontal overflow, image loading and dimensions, local links and anchors, full-size image links, and metadata. See [validation.json](validation.json). `git diff --check` passes. Source figures were reviewed again for cue definitions, cortical region names, proposal status, gamble probabilities and model-arrow direction.
