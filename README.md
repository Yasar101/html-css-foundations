# HTML & CSS Foundations

**Portfolio level:** 01 — Beginner

A small static website documenting the start of a web-development learning journey. It intentionally uses only HTML and CSS so the core building blocks remain easy to inspect.

## Purpose

This project turns an originally empty first repository into a complete, modest webpage while preserving its place as the first step in the portfolio.

## What I learned

- How semantic elements give a page meaningful structure
- How headings, links, lists, and images work together
- How CSS controls spacing, colour, and typography
- How a small media query improves a layout on narrow screens
- Why alternative text, visible focus styles, and descriptive links matter

## Features

- Semantic header, navigation, main sections, and footer
- Locally stored original SVG illustration (no external asset dependency)
- Responsive two-column introduction that becomes one column on mobile
- Keyboard-visible navigation and a skip link

## Technologies

- HTML5
- CSS3

## Project structure

```text
.
├── assets/
│   └── learning-journey.svg
├── index.html
├── styles.css
├── tests/
│   └── validate_html.py
├── LICENSE
└── README.md
```

## How to run

Open `index.html` in a browser, or serve the directory locally:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Validation and testing

Run the dependency-free structural checks with:

```bash
python3 tests/validate_html.py
```

The check parses the page and verifies its landmarks, image alternatives, local files, and fragment links. Browser checks at desktop and mobile widths are still recommended.

## Limitations

- The site is a single page.
- It has no JavaScript or server-side behaviour.
- The contact link is deliberately a link to the page section, not a working form.

## Future improvements

- Add a second page and shared navigation.
- Explore CSS custom properties and reusable components.
- Add automated HTML validation in continuous integration.

## Portfolio progression

Next: **02 — Responsive Web Foundations** (prepared locally from `my-first-website1`).

## Licence

MIT — see [LICENSE](LICENSE).
