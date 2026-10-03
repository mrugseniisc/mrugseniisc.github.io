# Mrugsen Gopnarayan — personal website

This repository contains the source for [mrugseniisc.github.io](https://mrugseniisc.github.io). The site is plain HTML and CSS; there is no build step or package installation.

## Preview locally

From the repository root, run:

```bash
python3 -m http.server 8000 --directory site
```

Then open <http://localhost:8000>. Stop the server with `Ctrl+C`.

## Update the site

- Edit the HTML pages and shared layout styles in `site/`.
- Keep page navigation consistent across `index.html`, `research.html`, `publications.html`, and `experience.html`.
- Check publication titles, author order, dates, status, and links against their official records before changing them.
- Keep descriptions grounded in the current CV and research materials. Label future interests as interests, and do not add talks until a dated, reliable source is available.
- Keep portrait images in `site/assets/`; `profile.jpg` is the portrait shown on the website and used in social previews. `portrait-preview.jpeg` is retained as an existing personal photo.

## Publish

The GitHub Actions workflow in `.github/workflows/pages.yml` deploys `site/` to GitHub Pages on pushes to `main`. In repository settings, set **Pages → Build and deployment → Source** to **GitHub Actions**.
