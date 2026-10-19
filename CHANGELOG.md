# Changelog

All notable changes to BlockForge Studio are documented here.

## [2.0.0] — In development

### Added
- Searchable block palette within the selected category.
- Starter projects: Hello World, Calculator, Number Guessing Game, and Python Game Starter.
- Browser-local autosave and an opt-in prompt to restore the latest draft.
- Version 2 .bforge project exports and import checks for size, format/version, known block types, duplicate IDs, required fields, and excessive nesting.
- Workspace zoom controls and a first-run onboarding guide.
- Added explicit generator cases for type conversions, operators/comparisons, common string methods, dictionaries, text-file read/write, and class definitions.
- Block copy/cut/paste and duplicate keyboard shortcuts.
- Optional standard-library localhost Python runner with source/request/output limits, timeout, temporary working directory, and a visible output panel.
- Beginner quick-start, contribution guidelines, code of conduct, issue reporting guidance, and automated runner tests.
- GitHub Actions checks for inline JavaScript parsing and Python runner tests.

### Changed
- README now explains the optional local runner, security caveats, and V2 feature status.
- Project remains a single-file offline-capable visual editor; the runner is optional and only needed for in-app execution.

### Security and limitations
- The local runner is **not a security sandbox**. Programs run with the current user's permissions and must be trusted.
- Visual block expressions use Python syntax but are not fully parsed or statically type-checked.
- Arbitrary Python source cannot be safely converted back into visual blocks.
- V2 has not yet had exhaustive browser-based interaction testing and is not a stable release.
