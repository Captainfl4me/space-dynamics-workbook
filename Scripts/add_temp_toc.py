"""
    Python script to generate the Workbook hand-in 1 PDF
"""
import nbformat as nbf
import sys
from os import path, mkdir


def add_toc_at_top(file_path: str):
    nb: nbf.NotebookNode = nbf.v4.new_notebook()
    with open(file_path, 'r', encoding="UTF-8") as f:
        nb = nbf.read(f, nbf.NO_CONVERT)

    nb.cells.insert(0, nbf.v4.new_markdown_cell("\\tableofcontents"))

    if not path.exists("temp"):
        mkdir("temp")
    with open(f"temp/{file_path}", 'w', encoding="UTF-8") as f:
        nbf.write(nb, f)

    print(f"Add toc at top of {sys.argv[1]} stored at temp/{file_path}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: add_temp_toc.py <file_path>")
        sys.exit(1)
    add_toc_at_top(sys.argv[1])
    sys.exit(0)
