# Mrugsen Gopnarayan — personal website

This repository contains the source for [mrugseniisc.github.io](https://mrugseniisc.github.io). The site uses plain HTML, shared CSS, and a small contact-reveal script; there is no build step or package installation for preview or deployment.

## Preview locally

From the repository root, run:

```bash
python3 -m http.server 8000 --directory site
```

Then open <http://localhost:8000>. Stop the server with `Ctrl+C`.

## Update the site

- Edit the HTML pages and shared layout styles in `site/`.
- Keep page navigation consistent across `index.html`, `research.html`, `publications.html`, `experience.html`, and `cv.html`.
- `cv.html` displays both rendered public CV pages from `site/assets/cv/` and provides the searchable PDF in `site/assets/Mrugsen_Gopnarayan_CV.pdf` for opening and download. Prepare a public copy with email text and links removed, then refresh its page previews; see the command below.
- The seven generated paper illustrations are in `site/assets/papers/`. Keep each image paired with its paper and useful alt text. Display the complete composition without cropping, and keep the link to the full image. Scientific briefs and generation prompts are recorded in [the scientific illustration report](reports/scientific_illustrations/README.md).
- The visual palette is defined by CSS variables at the top of `site/styles.css`; update the `theme-color` metadata along with it if the main background changes.
- Check publication titles, author order, dates, status, and links against their official records before changing them.
- Keep descriptions grounded in the current CV and research materials. Label future interests as interests, and do not add talks until a dated, reliable source is available.
- Keep portrait images in `site/assets/`; `profile.jpg` is the portrait shown on the website and used in social previews. `portrait-preview.jpeg` is retained as an existing personal photo.

## Contact and public CV

All contact links lead to `contact.html`. `contact.js` assembles the address only after a visitor activates the reveal button; no literal address or email link is present in the initial page. This reduces routine harvesting, but client-side obfuscation is not access control. Capable bots can decode it, and old Git history or external papers may still contain previously published addresses.

To update the public CV, keep the original PDF separate and run the helper below. PyMuPDF and Pillow are needed only for this maintenance operation, not for running the website:

```bash
python3 -m pip install pymupdf Pillow
python3 scripts/prepare_public_cv.py /path/to/private/CV.pdf site/assets/Mrugsen_Gopnarayan_CV.pdf --preview-dir site/assets/cv
```

The helper removes email text and all `mailto:` annotations, replaces the main contact line with a link to the contact page, withholds reference email addresses, and renders both pages for display on mobile and desktop. Review both pages after each update and check the PDF download and page previews.

## Publish

The GitHub Actions workflow in `.github/workflows/pages.yml` deploys `site/` to GitHub Pages on pushes to `main`. In repository settings, set **Pages → Build and deployment → Source** to **GitHub Actions**.
