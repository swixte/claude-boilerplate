Help me initialize this project. This is a one-time setup conversation.

First, read CLAUDE.md and identify all [INSERT] placeholders that need to be filled in.

## Phase 1: Project Overview
Ask me (one at a time, wait for answers):
- What is this project? One sentence: what it does and why it matters.
- Who is it for?

## Phase 2: Repository & Tech Stack
Ask me (one at a time):
- GitHub repo URL?
- Main branch name? (usually `main`)
- Tech stack:
  - Frontend framework/library?
  - Backend language/framework?
  - Database?
  - Infrastructure/hosting?
- Key external integrations or dependencies?

## Phase 3: Project Structure
Ask me:
- Is this a monorepo with separate frontend/backend folders? (default: yes)
- If monorepo: What workspace tool? (npm workspaces, yarn workspaces, pnpm, turborepo)
- Any shared code between frontend/backend? (types, utils, constants)
- Walk me through your folder structure, or should I scan the repo and propose one?

## Phase 4: Development Workflow
Ask me:
- Common commands (dev server, test, build, lint, deploy)?
- Linter/formatter setup (ESLint, Prettier, etc.)?
- Test framework and coverage target?
- Any workflow specifics I should know?

## Phase 5: Environment & Deployment
Ask me:
- Required environment variables?
- Deployment setup (staging/prod branches, manual deploy command)?

## Phase 6: Notes & Gotchas
Ask me:
- Anything else Claude should know? Quirks, constraints, legacy baggage?

## Phase 7: Generate Artifacts
Once aligned, update:

1. **CLAUDE.md** – Replace all [INSERT] placeholders with our answers

2. **/docs/roadmap.md** – Create with:
   - Initial epics (ask me what the first 3-5 major chunks of work are)
   - Sequencing notes

3. **/docs/progress.md** – Create empty template

4. **/docs/architecture.md** – High-level architecture based on tech decisions

5. **/docs/changelog.md** – Initialize with project start entry

## Rules
- One question at a time. Wait for my answer.
- Be persistent – if I'm vague, push for specifics.
- Summarize after each phase before moving on.
- Don't update any files until I confirm we're aligned.
- This may span multiple sessions – that's fine.