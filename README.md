# Markdown to HTML Converter

A simple Python tool to convert Markdown files to HTML, with support for custom CSS.

## Features
- Convert Markdown to HTML
- Use your own CSS for styling (auto-detected or via `--css`)
- All code and output messages are in English

## Requirements
- Python 3.7+
- See `requirements.txt` for dependencies

## Installation
Install dependencies with pip:

```bash
pip install -r requirements.txt
```

## Usage

Convert a Markdown file to HTML (CSS auto-detected or specify with `--css`):

```bash
python md2html.py example.md
```

Or with a specific CSS file:

```bash
python md2html.py example.md --css custom.css
```

The script will generate `example.html`.

## Example
See `example.md` for a sample Markdown file.

## License
MIT
