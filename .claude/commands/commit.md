Commit current work with a well-formatted commit message.

## Step 1: Review Changes
Run `git status` and `git diff --stat` to see what's being committed.

Summarize:
- Files modified
- Files added
- Files deleted

If there are no changes, say so and stop.

## Step 2: Analyze Changes
Read the changed files to understand what was done:
- What feature/fix/refactor was implemented?
- What's the scope of changes?

## Step 3: Generate Commit Message
Create a conventional commit message:

**Format:** `type(scope): description`

**Types:**
- `feat` - new feature
- `fix` - bug fix
- `refactor` - code refactoring
- `docs` - documentation changes
- `test` - test additions/changes
- `chore` - maintenance, deps, config
- `style` - formatting, no code change

**Scope:** (optional) area of codebase - e.g., `auth`, `api`, `ui`

**Rules:**
- Lowercase, no period at end
- Imperative mood ("add" not "added")
- Under 72 characters
- Be specific but concise

**Examples:**
- `feat(auth): add Google OAuth login`
- `fix(api): handle null response from payment service`
- `refactor: extract validation logic to shared utils`
- `docs: update API endpoint documentation`

## Step 4: Stage and Commit
```bash
git add -A
git commit -m "generated message"
```

## Step 5: Confirm
Show the commit hash and message:
```bash
git log -1 --oneline
```

## Optional: With Description
If changes are complex, use multi-line commit:
```bash
git commit -m "type(scope): summary" -m "Longer description of what and why"
```

## Arguments
If the user provides `$ARGUMENTS`, use that as context for the commit message.
Example: `/commit added user preferences` → incorporate that into the message.
