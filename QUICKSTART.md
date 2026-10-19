# Block Forge — Quick Start

## Open the editor

1. Download or clone this repository.
2. Open `blockforge_studio.html` in a modern browser. The visual editor and Python export work offline without a build step.
3. Pick a category, click or drag a block into the workspace, then select it to edit values.
4. Use the **Python Code** tab to inspect generated source.
5. Choose **Export .py** to download a Python file, or **Project** to save an editable `.bforge` project.

## Run generated Python locally (optional)

The HTML file cannot execute Python by itself. To enable the **Run** button:

1. Install Python 3.9 or newer from the official Python distribution.
2. Put `runner.py` and `blockforge_studio.html` in the same folder.
3. Open a terminal in that folder and run `python runner.py`.
4. Open `http://127.0.0.1:8765` in your browser.
5. Build or load a program and click **Run**. Stop the runner with Ctrl+C.

The runner uses only the Python standard library. It enforces request/source/output limits and a five-second execution timeout, and starts each program in a temporary working directory. **These measures are not a security sandbox.** Code runs with your account's permissions and may access your files or network. Only run code you wrote or trust. Do not expose the runner to the internet or change its bind address.

## Known limitations

- Visual blocks cover a useful subset of Python; expressions entered in block fields are Python syntax and are not fully parsed by the editor.
- The Any Python block is a source escape hatch. Arbitrary source cannot be reliably converted back into visual blocks.
- The code preview is generated and read-only; edits should be made through blocks or the Any Python block.
- The runner does not isolate untrusted code at the operating-system level. It is intended for local learning and trusted programs, not hostile code.
- The single-file editor has not been exhaustively tested across all browsers or screen sizes. Report issues with reproduction steps.
