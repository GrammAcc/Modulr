# Modulr
A simple Python script for modular Frontend web development without the
runtime cost of Native Web Components or the bloat of large Frontend frameworks.

## Motivation

Modern Frontend JS frameworks are impressive tools that allow us to build very
complex and interactive web applications, but they come at a cost of increased
complexity, and most of their functionality is not necessary for the majority
of websites on the internet today.

There have been a lot of improvements to the ECMAscript standards since React
was first released in 2013, and direct DOM updates are not the performance
bottleneck that they used to be. For these reasons, it would be great if there
was a productive workflow for developing Frontend applications without any
large framework, only using the features of the language, but there aren't a
lot of options right now.

Native Web Components are great, but they have a runtime cost that results
in content reflow unless template tags are used in the HTML page that the component
is loaded into. This is because the component has to parse and render the HTML
it owns at runtime unless the template is included in the consuming page, which defeats
the purpose of the modular components.

I'm sure there's a way to make a performant web app with some shadow dom trickery, but
this again adds a lot of complexity for the sole benefit of allowing reusable chunks of
code and HTML.

From a software development perspective, we really only need a couple of things to be
really productive:

1. Some way to reuse modular pieces of the application.
2. Good tooling for automated testing, code quality, etc...

Number 2 is already solved by the current JS/TS tooling. If we use Node, then we
have access to a number of different testing frameworks, Typescript, and various linters
and autoformatting workflows.

Additionally, even without a build step, JSDoc can provide in-editor type checking
via the Typescript LSP as long as the editor has a ts client.

Since the capabilities of pure JS have advanced to the point where we can build
complex interactive applications without a large framework, and we have all of the
tooling we need to be effective, we just need a way to modularize our code.

Modulr solves this problem by parsing source HTML files and looking for structured
comments, which it then replaces with the contents of the component HTML file named
in the comment.

This is a very simple but effective way to develop modular components without a large
runtime cost.

## Installation

Currently, this script is not available on PyPi or as a standalone application.

To install, simply download the modulr.py script into your project's root directory.

Run the script with Python: `python modulr.py`.

Modulr requires Python >= 3.12 because of the use of `Path.walk`. I plan to eventually
package Modulr as a standalone commandline app, but for now, you will need Python 3.12
installed in order to run the script.

If your system doesn't come with 3.12, the easiest way to get a different version
installed is with either
[Hatch](https://hatch.pypa.io/latest/install/) or
[Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation).

## Roadmap

- [x] Add automatic JS/TS and CSS component script detection so we no longer have to manually include component script sources in the source HTML file.
- [ ] Add arguments for source, output, and component dirs to make the project structure configurable.
- [ ] Package the script as a standalone commandline application.
  - This requires making the script path-independent so that it operates on the CWD regarless of where the executable is located.
