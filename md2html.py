import sys
import os
import argparse
import markdown


def md_to_html(md_path, css_path=None):
    with open(md_path, encoding="utf-8") as f:
        md_text = f.read()
    html = markdown.markdown(
        md_text, extensions=["extra", "codehilite", "toc"], output_format="html5"
    )
    html_doc = f"""
    <html>
    <head>
        <meta charset='utf-8'>
        {f'<link rel=\"stylesheet\" href=\"{css_path}\">' if css_path else ''}
    </head>
    <body>
        {html}
    </body>
    </html>
    """
    return html_doc


def main():
    parser = argparse.ArgumentParser(
        description="Markdown to HTML converter with CSS support."
    )
    parser.add_argument(
        "input", help="Path to markdown file (with or without .md extension)"
    )
    parser.add_argument(
        "--css", help="Path to custom CSS file (overrides default)", default=None
    )
    args = parser.parse_args()

    input_path = args.input
    if not input_path.lower().endswith(".md"):
        if os.path.exists(input_path + ".md"):
            input_path = input_path + ".md"
    if not os.path.exists(input_path):
        print(f"Input file '{input_path}' not found.")
        sys.exit(1)

    base, _ = os.path.splitext(input_path)
    output = base + ".html"
    css_path = (
        args.css
        if args.css
        else (
            base + ".css"
            if os.path.exists(base + ".css")
            else ("custom.css" if os.path.exists("custom.css") else None)
        )
    )

    html = md_to_html(input_path, css_path)
    with open(output, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML saved as {output}")


if __name__ == "__main__":
    main()
