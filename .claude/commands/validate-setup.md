Validate the project setup for consistency and completeness.

## Check Required Files Exist
Verify these files are present:
- [ ] CLAUDE.md
- [ ] /docs/roadmap.md
- [ ] /docs/progress.md
- [ ] /docs/architecture.md
- [ ] /docs/changelog.md
- [ ] .gitignore

## Check for Placeholder Content
Scan CLAUDE.md for any remaining `[INSERT]` placeholders that need to be filled in.

## Validate Path References
Check that all path references are consistent:
- Epic docs should reference `/docs/epics/`
- Roadmap links should point to `/docs/epics/epic-*.md`
- Commands should reference `/docs/epics/` not `/docs/plans/`

## Check Epic Consistency
For each epic listed in /docs/roadmap.md:
- Verify the linked epic doc exists in /docs/epics/
- Flag any broken links

## Check Progress Log
- Verify /docs/progress.md exists and has correct format
- Warn if more than 10 entries (should be pruned)

## Report
Provide a summary:
- ✅ Items that passed validation
- ⚠️ Warnings (non-blocking issues)
- ❌ Errors (must fix)

Suggest fixes for any issues found.
