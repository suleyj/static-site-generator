# static-site-generator

A small static site generator written in pure Python (no dependencies). It converts a tree of
Markdown files into a static HTML site by rendering each file through an HTML template.

## Features

- Recursively converts a directory of Markdown files into HTML pages, mirroring the folder structure
- Custom Markdown-to-HTML parser supporting:
  - Headings, paragraphs, code blocks, blockquotes
  - Ordered and unordered lists
  - Inline **bold**, *italic*, `code`, links, and images
- Copies static assets (CSS, images, etc.) alongside the generated pages
- Supports deploying under a subpath (e.g. GitHub Pages project sites) via a configurable base path
- No third-party dependencies — just the Python standard library

## Project layout

```
.
├── content/         # Markdown source files (rendered recursively)
├── static/          # Static assets copied as-is into the build (CSS, images, ...)
├── template.html     # HTML template used to render every page
├── docs/            # Generated site output (build target)
├── src/             # Generator source code
├── build.sh         # Build the site for deployment (e.g. GitHub Pages)
├── main.sh          # Build the site and serve it locally
└── test.sh          # Run the test suite
```

Each Markdown file must start with an `h1` (`# Title`) — it's used as the page's `<title>`.

## Usage

### Serve locally

```sh
./main.sh
```

This builds the site into `docs/` and serves it at `http://localhost:8888`.

### Build for deployment

```sh
./build.sh
```

Builds the site with `/static-site-generator/` as the base path, suitable for deploying to a
project's GitHub Pages URL (`https://<user>.github.io/static-site-generator/`). To build with a
different base path, run the generator directly:

```sh
python3 src/main.py [base_path]
```

`base_path` defaults to `/` if omitted.

### Run tests

```sh
./test.sh
```

## How it works

1. `docs/` is cleared and repopulated with a fresh copy of `static/`.
2. Every file in `content/` is walked recursively; each `.md` file is converted to HTML and
   written to the corresponding path in `docs/`, with `{{ Title }}` and `{{ Content }}` in
   `template.html` filled in.
3. Root-relative `href="/…"` and `src="/…"` attributes are rewritten with the given base path, so
   the site works whether it's served from the domain root or a subpath.

## Customizing

- Edit `template.html` to change the page layout/styling shell.
- Add CSS, images, or other assets to `static/` — they're copied into the build untouched.
- Add or edit Markdown files under `content/` to change site content.
