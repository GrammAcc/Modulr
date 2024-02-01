if __name__ != "__main__":
    raise ImportError("This is a standalone script and should not be imported.")

from pathlib import Path


def getindent(line: str) -> str:
    """Return the indentation of `line` as a string of whitespace."""

    return line.split("<")[0]


components_dir = Path("src/components")


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


for root, dirs, files in Path("src").walk(on_error=print):
    if "components" in dirs:
        dirs.remove("components")
    filepaths = [root / file for file in files if file.endswith(".html")]
    for fp in filepaths:
        str_dirpath = str(root)
        str_filepath = str(fp)
        output_dir = Path("site") / str_dirpath.removeprefix("src").removeprefix("/")
        output_path = output_dir / fp.name
        output_lines: list[str] = []
        with fp.open("r") as html_file:
            print(f"Parsing {str_filepath}...")
            for line in html_file.readlines():
                if line.lstrip().startswith("<!-- static-component"):
                    output_lines.append(parse_component_identifier(line))
                else:
                    output_lines.append(line)
        output_html = "".join(output_lines)
        if not output_dir.exists():
            output_dir.mkdir()
        print(f"Writing parsed {str_filepath} to {output_path}...")
        output_path.write_text(output_html)

