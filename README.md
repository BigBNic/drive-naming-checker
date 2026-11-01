# Drive Naming Checker

Real-time filename gate for Nicholas Bryan's AI workflow.

## What it does

- **Phase 1 (live):** Validates any filename against `YYYY-MM-DD_project-slug_plain-title.ext` before a bot is allowed to save. Bad name = no save, one-line blocker report. Zero tolerance on ID strings in filenames.
- **Phase 2 (in progress):** Scores bot prompts and outputs against the hard-rules set and flags violations before they reach Nicholas.

## Run tests

```bash
python test_checker.py
```

## Nicholas's rules (from hard-rules v1.3.0)

- Every file: `YYYY-MM-DD_project-slug_plain-title.ext`
- No bare `t01.png`, no `untitled` dumps
- No ID strings spoken aloud or shown to Nicholas
- Real-time check on creation, not a sweep cadence
- If a bot cannot produce a clean name, it does not save and reports the blocker

## Status

- [x] Core validator + tests
- [x] Pushed to GitHub
- [ ] Drive API watch trigger (needs service account + folder watch)
- [ ] Bot-side pre-save hook
- [ ] Prompt-rule scorer wired to hard-rules v1.3.0
- [ ] Hosted always-on instance
