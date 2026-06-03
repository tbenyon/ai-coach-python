#!/usr/bin/env python3
"""
Generate resources for student materials:
- Convert mermaid diagrams (.mmd) to PNG images
- Convert markdown files (.md) to PDFs

Requirements:
- Python packages: pip install markdown weasyprint pygments
- Node.js package: npm install -g @mermaid-js/mermaid-cli
"""

import os
import re
import subprocess
from pathlib import Path

# Check for PDF dependencies
try:
    import markdown
    from weasyprint import HTML
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Check for mermaid CLI
def check_mmdc_available():
    """Check if mermaid-cli (mmdc) is installed."""
    try:
        result = subprocess.run(['mmdc', '--version'], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

MERMAID_AVAILABLE = check_mmdc_available()


def find_files(root_dir, extension):
    """
    Recursively find all files with given extension in students_resources.

    Args:
        root_dir: Root directory of the repo
        extension: File extension to search for (e.g., '.md', '.mmd')

    Returns:
        List of Path objects for matching files
    """
    students_resources = root_dir / 'students_resources'

    if not students_resources.exists():
        print(f"Error: students_resources directory not found at {students_resources}")
        return []

    return list(students_resources.rglob(f'*{extension}'))


def convert_mermaid_to_png(mmd_file):
    """
    Convert a mermaid file to PNG using mmdc.

    Args:
        mmd_file: Path to the mermaid file

    Returns:
        Path to the generated PNG file or None if conversion failed
    """
    png_file = mmd_file.with_suffix('.png')

    try:
        result = subprocess.run(
            ['mmdc', '-i', str(mmd_file), '-o', str(png_file), '-b', 'white'],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"  Generated: {png_file.name}")
            return png_file
        else:
            print(f"  Failed: {mmd_file.name} - {result.stderr}")
            return None

    except Exception as e:
        print(f"  Failed: {mmd_file.name} - {str(e)}")
        return None


_CODEHILITE_BLOCK_RE = re.compile(
    r'<div class="codehilite">\s*<table class="codehilitetable">.*?</table>\s*</div>',
    re.DOTALL,
)
_INNER_CODE_RE = re.compile(r'<code[^>]*>(.*?)</code>', re.DOTALL)


def reformat_codehilite_blocks(html):
    # codehilite renders line numbers in a separate <td>, so when the code
    # column wraps the two columns desync. Flatten the table into one row
    # per source line so each line number stays glued to its line.
    def replace(match):
        block = match.group(0)
        code_match = _INNER_CODE_RE.search(block)
        if not code_match:
            return block
        code_html = code_match.group(1).rstrip('\n')
        lines = code_html.split('\n')
        rows = []
        for i, line in enumerate(lines, start=1):
            line_content = line if line.strip() else '&nbsp;'
            rows.append(
                f'<div class="codeline">'
                f'<span class="ln">{i}</span>'
                f'<span class="cl">{line_content}</span>'
                f'</div>'
            )
        return '<div class="codeblock">' + ''.join(rows) + '</div>'
    return _CODEHILITE_BLOCK_RE.sub(replace, html)


def convert_md_to_pdf(md_file):
    """
    Convert a markdown file to PDF using markdown and weasyprint.

    Args:
        md_file: Path to the markdown file

    Returns:
        Path to the generated PDF file or None if conversion failed
    """
    pdf_file = md_file.with_suffix('.pdf')

    try:
        # Read markdown file
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Convert markdown to HTML
        html_content = markdown.markdown(
            md_content,
            extensions=['extra', 'codehilite', 'fenced_code', 'tables'],
            extension_configs={
                'codehilite': {'linenums': True, 'guess_lang': False},
            },
        )
        html_content = reformat_codehilite_blocks(html_content)

        # Add basic CSS styling
        styled_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    max-width: 800px;
                    margin: 40px auto;
                    padding: 20px;
                }}
                h1 {{
                    color: #333;
                    border-bottom: 2px solid #333;
                    padding-bottom: 10px;
                }}
                h2 {{
                    color: #444;
                    margin-top: 30px;
                }}
                h3 {{
                    color: #555;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 15px;
                    border-radius: 5px;
                    border: 1px solid #ddd;
                    white-space: pre-wrap;
                    word-break: break-word;
                    overflow-wrap: anywhere;
                }}
                pre code {{
                    background-color: transparent;
                    padding: 0;
                    white-space: pre-wrap;
                    word-break: break-word;
                    overflow-wrap: anywhere;
                }}
                /* flex-per-line code blocks (post-processed from codehilite) */
                .codeblock {{
                    background-color: #f4f4f4;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    padding: 12px 0;
                    margin: 12px 0;
                    font-family: 'Courier New', monospace;
                    font-size: 0.9em;
                    line-height: 1.5;
                }}
                .codeline {{
                    display: flex;
                    align-items: flex-start;
                    padding: 0 12px;
                }}
                .codeline .ln {{
                    flex: 0 0 2em;
                    text-align: right;
                    color: #999;
                    padding-right: 12px;
                    margin-right: 12px;
                    border-right: 1px solid #ddd;
                }}
                .codeline .cl {{
                    flex: 1 1 auto;
                    min-width: 0;
                    white-space: pre-wrap;
                    word-break: break-word;
                    overflow-wrap: anywhere;
                }}
                /* minimal Pygments token colors */
                .codeblock .k, .codeblock .kn, .codeblock .kd {{ color: #0066cc; font-weight: bold; }}
                .codeblock .s, .codeblock .s1, .codeblock .s2 {{ color: #008000; }}
                .codeblock .c, .codeblock .c1, .codeblock .cm {{ color: #888; font-style: italic; }}
                .codeblock .nb {{ color: #0066cc; }}
                .codeblock .mi, .codeblock .mf {{ color: #aa5500; }}
                hr {{
                    border: none;
                    border-top: 1px solid #ddd;
                    margin: 30px 0;
                }}
                ol, ul {{
                    padding-left: 25px;
                }}
                li {{
                    margin-bottom: 8px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px 12px;
                    text-align: left;
                }}
                th {{
                    background-color: #f4f4f4;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """

        # Convert HTML to PDF
        HTML(string=styled_html).write_pdf(pdf_file)

        print(f"  Generated: {pdf_file.name}")
        return pdf_file

    except Exception as e:
        print(f"  Failed: {md_file.name} - {str(e)}")
        return None


def main():
    """Main function to find and convert all resource files."""
    # Get the repository root (parent of internal_tools)
    repo_root = Path(__file__).parent.parent

    print("Resource Generator for Student Materials")
    print("=" * 50)
    print()

    # Check dependencies
    if not MERMAID_AVAILABLE:
        print("Warning: mermaid-cli (mmdc) not found")
        print("  Install with: npm install -g @mermaid-js/mermaid-cli")
        print()

    if not PDF_AVAILABLE:
        print("Warning: PDF dependencies not found")
        print("  Install with: pip install markdown weasyprint")
        print()

    if not MERMAID_AVAILABLE and not PDF_AVAILABLE:
        print("Warning: No conversion tools available - will only list files")
        print()

    # Find all files (always find, even if we can't convert)
    mmd_files = find_files(repo_root, '.mmd')
    md_files = find_files(repo_root, '.md')

    # Summary
    print(f"Found {len(mmd_files)} mermaid diagram(s)")
    print(f"Found {len(md_files)} markdown file(s)")
    print()

    # Convert mermaid diagrams
    if mmd_files:
        print("=" * 50)
        if MERMAID_AVAILABLE:
            print("Converting Mermaid diagrams to PNG...")
            print()

            mmd_success = 0
            for mmd_file in sorted(mmd_files):
                if convert_mermaid_to_png(mmd_file):
                    mmd_success += 1

            print()
            print(f"Diagrams: {mmd_success}/{len(mmd_files)} converted")
        else:
            print("Skipping Mermaid conversion (mmdc not installed)")
        print()

    # Convert markdown to PDF
    if md_files:
        print("=" * 50)
        if PDF_AVAILABLE:
            print("Converting Markdown to PDF...")
            print()

            md_success = 0
            for md_file in sorted(md_files):
                if convert_md_to_pdf(md_file):
                    md_success += 1

            print()
            print(f"PDFs: {md_success}/{len(md_files)} converted")
        else:
            print("Skipping PDF conversion (markdown/weasyprint not installed)")
        print()

    print("=" * 50)
    print("Done!")


if __name__ == "__main__":
    main()
