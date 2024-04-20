# Modulr

A simple Python script for modular front-end web development without the
runtime cost of Native Web Components or the bloat of large front-end frameworks.

## Motivation

Modern front-end JS frameworks are impressive tools that allow us to build very
complex and interactive web applications, but they come at a cost of increased
complexity and most of their functionality is not necessary for the majority
of websites on the internet today.

There have been a lot of improvements to the ECMAScript standards since React
was first released in 2013, and direct DOM updates are not the performance
bottleneck that they used to be. For these reasons, it would be great if there
were a productive workflow for developing front-end applications without needing to
utilize any large framework - only using the features of the language - but there aren't
a lot of options right now.

Native Web Components are great, but they have a runtime cost that results
in content reflow unless template tags are used within the HTML page that the component
is loaded into. This is because the component has to parse and render the HTML
it owns at runtime unless the template is included in the consuming page, which defeats
any performance gains of the modular components.

There is likely a way to make a performant web app with some shadow DOM trickery, but
this again adds a lot of complexity for the sole benefit of allowing reusable chunks of
code and HTML.

From a software development perspective, there are really only a couple of things required
to be productive:

1. Some way to reuse modular pieces of the application.
2. Good tooling for automated testing, code quality, etc.

Number 2 is already solved by the current JS/TS tooling. With Node, you get access to a
number of different testing frameworks, TypeScript, and various linters and autoformatting
workflows.

Additionally, even without a build step, JSDoc can provide in-editor type checking
via the TypeScript LSP as long as the editor has a TS client.

Since the capabilities of pure JS have advanced to the point where we can build
complex interactive applications without a large framework, and we have all of the
tooling we need to be effective, we just need a way to modularize our code.

Modulr solves this problem by parsing source HTML files and looking for structured
comments. It then replaces those with the contents of the component HTML file named
in the comment.

This is a very simple but effective way to develop modular components without a large
runtime cost.

## Installation

Currently, this script is not available on PyPi or as a standalone application.

To install, simply download the modulr.py script into your project's root directory.

Run the script with Python: `python modulr.py`.

Modulr requires Python >= 3.12 because of the use of `Path.walk`. I plan to eventually
package Modulr as a standalone commandline app; but for now, you will need Python 3.12
installed in order to run the script.

If your system doesn't come with 3.12, the easiest way to get a different version
installed is with either
[Hatch](https://hatch.pypa.io/latest/install/) or
[Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation).

## Project Scope & Limitations

After careful consideration, there are some features that this project does not intend to
support. Justification for each is included beneath.

1. Including a component multiple times within the same page.

Modulr endeavors to improve maintainability by allowing you to develop common page
components once and copy-paste them to your desired pages before release. Many of these
components will likely involve some level of DOM manipulation, so including these multiple
times on the same page will inevitably lead to selection collisions. Any suitable solution
to this challenge will result in a leaky abstraction, which runs counter to Modulr's goal
of improving maintainability, so this project is built with the philosophy that Modulr
components are single-use within a page.

Examples of components that may make for good Modulr components include navigation bars,
page headers, and site footers.

2. Nesting Modulr components within each other.

Rather than the SPA and Native Web Component interpretation of what a "component" is,
Modulr components are intended to be factored-out, shared sections of web pages. Aside from
this being out-of-scope for this project, Modulr aims to help you reduce boilerplate. Nested
components add more overhead to your code, and while how/when to break up components is (to
some extent) a stylistic choice within some front-end technologies, this process easily devolves
into code that is difficult to compose and reason about. Not supporting this feature should help
encourage components that are easier to maintain.

3. Passing properties (AKA "props") to components.

This runs very closely with scope item number two. Due to many of the same reasons why
nesting components adds complexity to projects, passing properties to components is another
major source of complexity in your code that this project avoids.

## Roadmap

- [ ] Add automatic JS/TS and CSS component script detection so we no longer have to manually include component script sources in the source HTML file.
- [ ] Add arguments for source, output, and component dirs to make the project structure configurable.
- [ ] Package the script as a standalone commandline application.
  - This requires making the script path-independent so that it operates on the CWD regarless of where the executable is located.
