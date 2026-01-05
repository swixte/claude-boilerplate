Review what we accomplished this session:

1. Add an entry to /docs/progress.md with:
   - Date
   - Epic name
   - What was done
   - Key decisions made
   - Next steps
   - Blockers (if any)
   Remove the oldest entry if there are more than 10.

2. Update the relevant epic doc in /docs/plans/ if decisions or scope changed

3. Update checkbox status in /docs/roadmap.md if features/tasks completed

Summarize what changed.
```

## How to Use It

In Claude Code, just type:
```
/wrap-up
```

Claude will execute that prompt.

## Other Useful Commands You Might Add
```
.claude/
  commands/
    wrap-up.md        # End of session
    start.md          # "Read progress.md, roadmap.md, and ask what I'm working on today"
    plan-epic.md      # "Help me break down a new epic: $ARGUMENTS"
```

The `$ARGUMENTS` variable lets you pass parameters:
```
/plan-epic User Notifications System