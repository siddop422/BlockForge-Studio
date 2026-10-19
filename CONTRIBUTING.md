# Contributing to Block Forge

Thanks for helping improve Block Forge Studio!

## Before starting
- Search existing issues and pull requests to avoid duplicate work.
- For larger changes, open an issue to discuss the design first.
- Preserve the single-file, offline-first editor unless a change has a clear benefit.
- Never claim a block is supported unless its generated Python is meaningful.

## Development and checks
- The browser editor is `blockforge_studio.html`.
- The optional localhost Python runner is `runner.py` (Python 3.9+, standard library only).
- Run the checks with `node scripts/check-html.mjs` and `python -m unittest discover -s tests -v`.
- Test the editor in a browser when changing interactions; static checks are not a substitute for manual testing.

## Pull requests
- Describe the user-visible change and why it is needed.
- Include steps to reproduce and verify bug fixes.
- Add or update tests where practical.
- Update README/CHANGELOG and document known limitations.
- Do not include credentials, personal data, generated caches, or unrelated formatting changes.
