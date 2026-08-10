# static-site-generator

A small static site generator written in pure Python (no dependencies). It converts a tree of
Markdown files into a static HTML site by rendering each file through an HTML template, and can
optionally build a chronological blog listing page.

## Features

- Recursively converts a directory of Markdown files into HTML pages, mirroring the folder structure
- Custom Markdown-to-HTML parser supporting:
  - Headings, paragraphs, code blocks, blockquotes
  - Ordered and unordered lists
  - Inline **bold**, *italic*, `code`, links, and images
- Copies static assets (CSS, images, etc.) alongside the generated pages, if a `static/` directory exists
- Supports deploying under a subpath (e.g. GitHub Pages project sites) via a configurable base path
- Optional blog listing page: posts are grouped by year (extracted from a `YYYY-MM-DD` date in
  each post) and rendered as a linked, dated list
- No third-party dependencies — just the Python standard library

## Project layout

```
.
├── content/                 # Markdown source files (rendered recursively)
├── static/                  # Static assets copied as-is into the build (CSS, images, ...); optional
├── blog_template.html       # HTML template used to render every page
├── blog_list_template.html  # HTML template for the blog listing page
├── post_component.html      # Per-post row used to build the blog listing
├── year_component.html      # Per-year grouping used to build the blog listing
├── docs/                    # Generated site output (build target)
├── src/                     # Generator source code
├── build.sh                 # Build the site for deployment (e.g. GitHub Pages)
├── main.sh                  # Build the site (with blog listing) and serve it locally
└── test.sh                  # Run the test suite
```

Each Markdown file must start with an `h1` (`# Title`) — it's used as the page's `<title>`. A
`YYYY-MM-DD` date anywhere in the file is optional; if present it's reformatted (e.g. `Jul 31 2026`)
in the rendered output and used to group posts in the blog listing.

## Usage

### Serve locally

```sh
./main.sh
```

This builds the site into `docs/` (including the blog listing page) and serves it at
`http://localhost:8888`.

### Build for deployment

```sh
./build.sh
```

Builds the site with `/static-site-generator/` as the base path, suitable for deploying to a
project's GitHub Pages URL (`https://<user>.github.io/static-site-generator/`). To build with a
different base path, or to control the blog listing, run the generator directly:

```sh
python3 src/main.py [base_path] [--listing]
```

- `base_path` defaults to `/` if omitted.
- Pass `--listing` to also (re)generate `docs/blog/index.html` from every post under
  `content/blog/`, grouped by year.

### Run tests

```sh
./test.sh
```

## How it works

1. `docs/` is cleared and repopulated with a fresh copy of `static/` (if it exists).
2. Every file in `content/` is walked recursively; each `.md` file is converted to HTML and
   written to the corresponding path in `docs/`, with `{{title}}` and `{{content}}` in
   `blog_template.html` filled in.
3. Root-relative `href="/…"` and `src="/…"` attributes are rewritten with the given base path, so
   the site works whether it's served from the domain root or a subpath.
4. If `--listing` is passed, every post under `content/blog/` is scanned for its title and date,
   grouped by year using `year_component.html`, rendered per-post with `post_component.html`, and
   assembled into `docs/blog/index.html` via `blog_list_template.html`.

## Customizing

- Edit `blog_template.html` to change the page layout/styling shell.
- Edit `blog_list_template.html`, `post_component.html`, and `year_component.html` to change how
  the blog listing page looks.
- Add CSS, images, or other assets to `static/` — they're copied into the build untouched.
- Add or edit Markdown files under `content/` to change site content.
