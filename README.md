# BlockForge Studio

**Build Python programs visually with drag-and-drop blocks. Export real Python files.**

BlockForge Studio is a browser-based visual programming editor inspired by block-based coding tools such as Scratch. Instead of writing every line by hand, you assemble blocks, edit their values, and see the Python source generated from your script.

> **Status:** Early project / work in progress. Feedback, bug reports, and feature ideas are welcome.

## 🚧 Block Forge V2 development

The `v2-development` branch adds a focused set of improvements while keeping the app as a single, offline-friendly HTML file:

- **Searchable block palette** — filter blocks in the selected category by name, description, or type.
- **Starter examples** — load Hello World, Calculator, Number Guessing Game, or a Python game starter.
- **Local draft autosave** — the editor can recover the last draft from this browser using local storage. Drafts stay in this browser and are not uploaded.
- **Safer project import** — validates the project format/version, rejects duplicate block IDs, fills missing fields from block defaults, and limits imports to 5 MB and 100 nested levels.
- **Versioned project format** — new exports use format version 2 while version 1 projects remain importable.

V2 is still under development. These changes are being prepared on a separate branch; review the branch and test the workflows before treating it as a stable release. The editor generates Python source and exports it; the optional local runner executes it in a separate Python process on your computer, not inside the browser.

## ✨ Features

- **Visual block workspace** — drag blocks from the palette, reorder them, and nest them inside control-flow blocks.
- **Python code preview** — inspect the generated source as you build.
- **Export Python** — download your program as a .py file.
- **Save and reopen projects** — export an editable .bforge project and open it again later.
- **Python block categories** — Events, Input/Output, Variables, Control, Exceptions, Math, Lists, Data types, Operators, Strings, Dictionaries, Files, Classes, Functions, and Any Python.
- **Workspace controls** — zoom in/out/reset, plus native scrolling for workspace navigation.
- **Block shortcuts** — undo/redo, copy/cut/paste, duplicate, delete, save, and export.
- **Beginner onboarding** — a first-run guide with an option to load a Hello World example.
- **Optional local execution** — run generated code using the standard-library runner on localhost; execution is not sandboxed.
- **Edit block values** — select a block to configure its inputs in the Inspector.
- **Undo and redo** — recover from recent editing mistakes.
- **Keyboard shortcuts** — use familiar shortcuts for common actions.
- **Single-file app** — the editor is provided as one HTML file and is designed to work locally in a modern browser without a build step.

## 🚀 Get started

### Option 1: Use the editor

1. Open [blockforge_studio.html](./blockforge_studio.html) from this repository.
2. Download the file using GitHub's **Download raw file** option, or click **Code → Download ZIP** to download the repository.
3. Open blockforge_studio.html in a modern browser such as Brave, Chrome, Edge, or Firefox.
4. Start building! No Node.js project setup or compilation is required to open the HTML editor.

### Option 2: Run a local copy

1. Download or clone this repository.
2. Open blockforge_studio.html in your browser.
3. Keep the downloaded file somewhere convenient; your project files can be saved separately from the editor.

## 🧩 How to use BlockForge

### 1. Add blocks

Choose a category on the left. Click a block to add it to the workspace, or drag it into place. A simple first script can use **When program starts** followed by **Print**.

### 2. Arrange and nest blocks

Drag blocks to reorder them. Drop a block into the body area of a supported block—such as **If**, **Repeat**, **While**, **For range**, **For each item**, **Function**, or **Try / Except**—to make it part of that block.

### 3. Configure a block

Select a block and edit its settings in the **Inspector** panel. Fields marked as Python expressions expect valid Python syntax. For example:

- Text value: "Hello, world!"
- Number: 42
- Comparison: score > 10
- List: [1, 2, 3]
- Function arguments: "Ada", 3

Use the **Any Python** category when you need a raw Python code block or a feature that is not represented by a dedicated block.

### 4. Preview the generated code

Select **Python Code** on the right to review the Python source produced from your blocks. If a field contains invalid Python syntax, correct it in the Inspector before using the exported script.

### 5. Export your program

Click **Export .py** to download the generated Python file. To run it, install Python from [python.org](https://www.python.org/downloads/) if it is not already installed, then open a terminal in the download folder and run:

~~~bash
python your_program.py
~~~

On some Windows installations, use **py your_program.py** instead.

**Important:** BlockForge generates Python source; it does not execute that source inside the HTML editor. Your exported script may need Python packages or other setup depending on the code you create.

### 6. Save your editable project

Click **Project** to download a .bforge file. Later, use **Open** to load that file and continue editing. Exporting a .py file saves the generated program, not the editable block layout.

## ⌨️ Keyboard shortcuts

| Shortcut | Action |
| --- | --- |
| Ctrl + Z | Undo |
| Ctrl + Y or Ctrl + Shift + Z | Redo |
| Ctrl + E | Export Python |
| Ctrl + S | Save editable project |
| Delete | Delete the selected block |

## 🛠️ Current limitations

BlockForge Studio is an early-stage project, so please treat it as a work in progress.

- It generates Python code; it is not a full Python runtime or debugger.
- Python expressions and raw code must be valid Python. The editor cannot guarantee that every program is syntactically or logically correct.
- Programs that use third-party packages require those packages to be installed in the Python environment where the exported file runs.
- The editor is primarily designed for a desktop-sized screen; a narrow window may make some panels unavailable.

## 💬 Help improve BlockForge

I'd love feedback from people learning Python, teachers, and developers. **You don't need to be an expert to help.** Tell me what confused you, what worked well, or what you wish the editor could do.

- **Report a bug:** [Open an issue](https://github.com/siddop422/BlockForge-Studio/issues/new) or use the **Issues** tab.
- **Suggest a feature:** [Open a feature request](https://github.com/siddop422/BlockForge-Studio/issues/new) and explain the problem the feature would solve.
- **Share your experience:** Tell me what you tried, what you expected, and what happened instead.
- **Contribute code or documentation:** Fork the repository, make your changes, and open a pull request.

When reporting a bug, please include:
1. What you were trying to do.
2. The steps to reproduce it.
3. What you expected to happen and what actually happened.
4. Your browser and operating system.
5. If possible, a small example project or the generated Python code (remove any personal information first).

### Feature request template

- **What problem are you trying to solve?**
- **What would you like BlockForge to do?**
- **How would this help learners or developers?**
- **Is there an example of how it could work?**

Thoughtful feedback helps prioritize improvements. If you try BlockForge, please leave an issue with your first impressions—even a short review is useful!

## 📄 License

BlockForge Studio is distributed under the [Apache License 2.0](./LICENSE). See the license file for details.

---

**Made for learning, experimenting, and making Python more visual.**

## Optional local Python runner

The visual editor and Python export work offline in a browser without a build step. To run generated programs from the editor, use the optional local runner:

1. Install Python 3.9 or newer.
2. Keep runner.py in the same folder as blockforge_studio.html.
3. Run python runner.py in a terminal.
4. Open http://127.0.0.1:8765 in your browser and use the **Run** button.

The runner uses Python's standard library only. It limits request/source/output sizes, runs with a timeout, and uses a temporary working directory. **It is not a security sandbox:** executed programs run with your user permissions and may access your files or network. Only run code you trust, and do not expose the runner to the internet. The editor remains usable by opening the HTML file directly if you do not need execution.

## V2 feature status

Implemented in the development branch: searchable block palette, starter examples, local draft recovery, versioned project files with import checks, generated Python preview/export, undo/redo, block nesting/reordering, workspace zoom, and optional localhost execution. This is still a development build, not a stable release. Multi-project management, full bidirectional Python-to-block conversion, exhaustive cross-browser QA, and operating-system-level sandboxing are not implemented.

See [Quick Start](./QUICKSTART.md), [Contributing](./CONTRIBUTING.md), and [Changelog](./CHANGELOG.md).
