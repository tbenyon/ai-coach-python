#!/usr/bin/env python3
"""
Generate PDF versions of all instruction markdown files in the repository.
Recursively searches for files starting with 'instruction' and ending with '.md'

Requirements: pip3 install markdown weasyprint
"""

import os
from pathlib import Path

try:
    import markdown
    from weasyprint import HTML
except ImportError:
    print("✗ Error: Required packages not found. Please install:")
    print("  pip3 install markdown weasyprint")
    exit(1)

def find_instruction_files(root_dir):
    """
    Recursively find all instruction markdown files

    Args:
        root_dir: Root directory to start search from

    Returns:
        List of Path objects for matching files
    """
    instruction_files = []

    for path in Path(root_dir).rglob('instruction*.md'):
        instruction_files.append(path)

    return instruction_files

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
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])

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
                h1, h2, h3 {{
                    color: #333;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 10px;
                    border-radius: 5px;
                    overflow-x: auto;
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

        print(f"✓ Generated: {pdf_file}")
        return pdf_file

    except Exception as e:
        print(f"✗ Failed to convert {md_file}: {str(e)}")
        return None

def main():
    """Main function to find and convert all instruction files"""
    # Get the repository root (parent of internal_tools)
    repo_root = Path(__file__).parent.parent

    print(f"Searching for instruction files in: {repo_root}")
    print("="*50)

    # Find all instruction markdown files
    instruction_files = find_instruction_files(repo_root)

    if not instruction_files:
        print("No instruction markdown files found!")
        return

    print(f"\nFound {len(instruction_files)} instruction file(s):")
    for file in instruction_files:
        print(f"  - {file.relative_to(repo_root)}")

    print("\n" + "="*50)
    print("Converting to PDF...\n")

    # Convert each file to PDF
    success_count = 0
    for md_file in instruction_files:
        if convert_md_to_pdf(md_file):
            success_count += 1

    print("\n" + "="*50)
    print(f"Conversion complete: {success_count}/{len(instruction_files)} successful")

if __name__ == "__main__":
    main()