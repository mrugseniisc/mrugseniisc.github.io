"""Make a public CV copy without harvestable email text or email links.

Requires PyMuPDF; page previews also require Pillow. The original PDF is never changed.
"""

import argparse
import re
from pathlib import Path

import fitz


EMAIL = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
CONTACT = "https://mrugseniisc.github.io/contact.html"


def prepare(source, destination, preview_directory=None):
    if source.resolve() == destination.resolve():
        raise ValueError("Choose a destination separate from the original PDF")
    with fitz.open(source) as document:
        for page in document:
            replacements = []
            for address in set(EMAIL.findall(page.get_text())):
                for rectangle in page.search_for(address):
                    label = "Contact via website" if page.number == 0 and rectangle.y0 < 120 else "Available on request"
                    page.add_redact_annot(rectangle, fill=(1, 1, 1))
                    replacements.append((rectangle, label))
            for link in page.get_links():
                if link.get("uri", "").lower().startswith("mailto:"):
                    page.delete_link(link)
            page.apply_redactions()
            for rectangle, label in replacements:
                size = min(9, rectangle.width / fitz.get_text_length(label, fontsize=1))
                page.insert_text((rectangle.x0, rectangle.y1 - 2), label, fontsize=size,
                                 fontname="helv", color=(.12, .22, .36))
                if label == "Contact via website":
                    page.insert_link({"kind": fitz.LINK_URI, "from": rectangle, "uri": CONTACT})
        document.save(destination, garbage=4, deflate=True)
    with fitz.open(destination) as document:
        if any(EMAIL.search(page.get_text()) for page in document):
            raise ValueError("An email address remains in the public PDF")
        if any(link.get("uri", "").lower().startswith("mailto:")
               for page in document for link in page.get_links()):
            raise ValueError("An email link remains in the public PDF")
        if preview_directory is not None:
            from PIL import Image
            preview_directory.mkdir(parents=True, exist_ok=True)
            for page in document:
                pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
                image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
                image.save(preview_directory / f"page-{page.number + 1}.webp",
                           "WEBP", quality=93, method=6)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--preview-dir", type=Path)
    args = parser.parse_args()
    prepare(args.source, args.destination, args.preview_dir)
