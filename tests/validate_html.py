"""Lightweight, dependency-free checks for the portfolio page."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
HTML_FILE = ROOT / "index.html"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.elements: set[str] = set()
        self.ids: set[str] = set()
        self.local_references: list[str] = []
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        self.elements.add(tag)
        if element_id := attributes.get("id"):
            self.ids.add(element_id)
        if tag == "img" and not attributes.get("alt"):
            self.errors.append("Every image must have useful alternative text.")
        for name in ("href", "src"):
            if reference := attributes.get(name):
                parsed = urlparse(reference)
                if not parsed.scheme and not reference.startswith("//"):
                    self.local_references.append(reference)


def main() -> None:
    parser = PageParser()
    parser.feed(HTML_FILE.read_text(encoding="utf-8"))

    required = {"header", "nav", "main", "section", "footer", "h1", "h2"}
    missing = sorted(required - parser.elements)
    if missing:
        parser.errors.append(f"Missing semantic elements: {', '.join(missing)}")

    for reference in parser.local_references:
        path, _, fragment = reference.partition("#")
        if path and not (ROOT / path).is_file():
            parser.errors.append(f"Missing local file: {path}")
        if fragment and not path and fragment not in parser.ids:
            parser.errors.append(f"Missing fragment target: #{fragment}")

    if parser.errors:
        raise SystemExit("\n".join(parser.errors))
    print("HTML structure and local references are valid.")


if __name__ == "__main__":
    main()
