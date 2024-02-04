#!/bin/python

"""Stitch together modular HTML files.

Currently, this script takes a single positional argument, which is
used as the project root directory.

Once implemented, it will take arguments for the following:
    - Project Root Directory (string/path)
    - HTML Source Directory (string/path)
    - Components Directory (string/path)
    - Output/Site Directory (string/path)
    - Flat/Nested Components Directory (bool/flag)
    - Automatically Include JS/CSS Files (bool/flag)

These arguments will be validated and documented by argparse, but for
now, they are not implemented yet.
"""

if __name__ != "__main__":
    raise ImportError("This is a standalone script and should not be imported.")

from pathlib import Path

# TODO: Replace this with argparse
import sys
project_root = Path(".")

try:
    project_root = Path(sys.argv[1])
except IndexError:
    pass


def getindent(line: str) -> str:
    """Return the indentation of `line` as a string of whitespace."""

    return line.split("<")[0]


components_dir = project_root / "src/components"


def parse_component_identifier(line: str) -> str:
    """Return the html of the web component that placeholder identifier
    `line` specifies with the same indentation level as the placeholder."""

    indentation = getindent(line)
    component_filepath = (components_dir / line.split(":")[1]).with_suffix(".html")
    output_html: list[str] = []
    with open(component_filepath, "r") as html_file:
        for i in html_file.readlines():
            output_html.append("".join([indentation, i]))
    return "".join(output_html)


for root, dirs, files in (project_root / "src").walk(on_error=print):
    if "components" in dirs:
        dirs.remove("components")
    filepaths = [root / file for file in files if file.endswith(".html")]
    for fp in filepaths:
        str_dirpath = str(root).removeprefix(str(project_root)).removeprefix("/")
        print(str_dirpath)
        str_filepath = str(fp)
        output_dir = project_root / "site" / str_dirpath.removeprefix("src").removeprefix("/")
        output_path = output_dir / fp.name
        output_lines: list[str] = []
        with fp.open("r") as html_file:
            print(f"Parsing {str_filepath}...")
            for line in html_file.readlines():
                if line.lstrip().startswith("<!-- modulr-component"):
                    output_lines.append(parse_component_identifier(line))
                else:
                    output_lines.append(line)
        output_html = "".join(output_lines)
        if not output_dir.exists():
            output_dir.mkdir()
        print(f"Writing parsed {str_filepath} to {output_path}...")
        output_path.write_text(output_html)

