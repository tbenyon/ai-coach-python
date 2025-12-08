#!/usr/bin/env python3
"""
Generate PDF versions of all markdown files in students_resources.

Requirements: pip3 install markdown weasyprint
"""

import os
from pathlib import Path

try:
    import markdown
    from weasyprint import HTML
except ImportError:
    print("Error: Required packages not found. Please install:")
    print("  pip3 install markdown weasyprint")
    exit(1)

def find_markdown_files(root_dir):
    """
    Recursively find all markdown files in students_resources

    Args:
        root_dir: Root directory to start search from

    Returns:
        List of Path objects for matching files
    """
    students_resources = root_dir / 'students_resources'

    if not students_resources.exists():
        print(f"Error: students_resources directory not found at {students_resources}")
        return []

    markdown_files = []
    for path in students_resources.rglob('*.md'):
        markdown_files.append(path)

    return markdown_files

def convert_md_to_pdf(md_file):
    """
    Convert a markdown file to PDF using markdown and weasyprint

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
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'fenced_code'])

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
                    overflow-x: auto;
                    border: 1px solid #ddd;
                }}
                pre code {{
                    background-color: transparent;
                    padding: 0;
                }}
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
    """Main function to find and convert all markdown files"""
    # Get the repository root (parent of internal_tools)
    repo_root = Path(__file__).parent.parent

    print("PDF Generator for Student Resources")
    print("=" * 50)
    print(f"Searching in: {repo_root / 'students_resources'}")
    print()

    # Find all markdown files
    markdown_files = find_markdown_files(repo_root)

    if not markdown_files:
        print("No markdown files found!")
        return

    print(f"Found {len(markdown_files)} markdown file(s):")
    for file in sorted(markdown_files):
        print(f"  - {file.relative_to(repo_root)}")

    print()
    print("=" * 50)
    print("Converting to PDF...")
    print()

    # Convert each file to PDF
    success_count = 0
    for md_file in sorted(markdown_files):
        if convert_md_to_pdf(md_file):
            success_count += 1

    print()
    print("=" * 50)
    print(f"Complete: {success_count}/{len(markdown_files)} files converted successfully")

if __name__ == "__main__":
    main()
