# Claude Code Boilerplate

A complete boilerplate structure for Claude Code projects with session-based workflow, epic planning, and progress tracking.

## Directory Structure

```
.
├── .claude/                      # Claude Code configuration directory
│   ├── settings.json            # Project-level settings (committed)
│   ├── commands/                # Slash commands for common workflows
│   │   ├── init-project.md     # One-time project setup interview
│   │   ├── start.md            # Begin a session
│   │   ├── wrap-up.md          # End a session, update docs
│   │   ├── commit.md           # Commit with smart message
│   │   ├── status.md           # Quick status check
│   │   ├── focus.md            # Focus on specific epic
│   │   ├── plan-epic.md        # Plan a new epic
│   │   ├── resume-planning.md  # Resume interrupted planning
│   │   └── validate-setup.md   # Validate project setup
│   ├── templates/               # Doc templates for initialization
│   │   ├── architecture.md
│   │   ├── changelog.md
│   │   ├── epic.md
│   │   ├── progress.md
│   │   └── roadmap.md
│   ├── rules/                   # Modular instruction files
│   │   ├── code-style.md       # Code style guidelines
│   │   ├── testing.md          # Testing standards
│   │   └── security.md         # Security best practices
│   ├── agents/                  # Custom subagents
│   │   ├── code-reviewer.md    # Reviews code for quality/security
│   │   ├── qa-tester.md        # Runs tests, fixes failures
│   │   ├── pr-preparer.md      # Prepares pull requests
│   │   └── refactor.md         # Refactors code safely
│   └── skills/                  # Custom skills (add your own)
├── docs/                        # Project documentation
│   ├── architecture.md         # System architecture
│   ├── changelog.md            # Version history
│   ├── progress.md             # Rolling session log (10 max)
│   ├── roadmap.md              # Epics and status
│   └── epics/                  # Individual epic docs
├── CLAUDE.md                    # Project context and instructions
├── .gitignore                   # Includes Claude local file exclusions
└── README.md                    # This file
```

## Session Workflow

This boilerplate is designed around a session-based development workflow:

### Starting a Session
```
/start
```
Reads progress log and roadmap, summarizes where you left off, asks what to focus on.

### During Development
```
/focus Auth System
```
Loads the relevant epic doc and context for focused work.

```
/status
```
Quick status check on current progress.

### Committing Work
```
/commit
```
Stages all changes and commits with a conventional commit message.

```
/commit added user preferences feature
```
Pass context to guide the commit message.

### Ending a Session
```
/wrap-up
```
Updates progress log, epic docs, roadmap checkboxes, and changelog.

## Planning Workflow

### Initialize a New Project
```
/init-project
```
Interview-style setup that fills in CLAUDE.md and creates initial docs.

### Plan a New Epic
```
/plan-epic User Notifications
```
Structured planning interview with scope, evaluation criteria, and phased breakdown.

### Validate Setup
```
/validate-setup
```
Checks for missing files, broken links, and placeholder content.

## Documentation System

### Planning Hierarchy
- **Roadmap** (`/docs/roadmap.md`) – Epics, dependencies, high-level status
- **Epic Docs** (`/docs/epics/epic-*.md`) – Detailed specs per initiative
- **Progress Log** (`/docs/progress.md`) – Rolling 10-entry session log
- **Changelog** (`/docs/changelog.md`) – User-facing version history

### Templates
Templates in `.claude/templates/` are copied to `/docs/` during initialization.

## Configuration

### Rules (`.claude/rules/`)

Modular instruction files loaded into every conversation:
- **code-style.md**: Naming conventions, code organization
- **testing.md**: Testing philosophy, coverage goals
- **security.md**: Security principles, common vulnerabilities

### Settings (`.claude/settings.json`)

```json
{
  "permissions": {
    "allow": ["Bash(npm run lint)", "Bash(npm run test)"],
    "deny": ["Read(./.env)", "Write(./.env)"]
  },
  "env": {
    "GITHUB_REPO": "your-org/your-repo"
  }
}
```

### Local Overrides (gitignored)

- `.claude/settings.local.json` – Personal permission overrides
- `.claude/CLAUDE.local.md` – Personal project notes

## Getting Started

### 1. Copy This Boilerplate
```bash
cp -r claude-code-boilerplate your-project
cd your-project
git init
```

### 2. Run Project Initialization
```
/init-project
```
Claude will interview you to fill in project details.

### 3. Start Building
```
/start
```
Begin your first session!

## Built-in Agents

Claude can automatically delegate to these specialized agents:

| Agent | Triggers When | What It Does |
|-------|---------------|--------------|
| `code-reviewer` | Code is written, review requested | Reviews for bugs, security, best practices |
| `qa-tester` | Tests needed, tests failing | Runs tests, diagnoses failures, writes new tests |
| `pr-preparer` | Ready to submit PR | Runs checks, generates PR description, creates PR |
| `refactor` | Code cleanup requested | Improves structure without changing behavior |

### How Agents Work
- Claude decides when to use them based on context
- They run autonomously and return structured results
- You can also explicitly request them: *"Use the code-reviewer agent"*

### Customize Agents
Edit files in `.claude/agents/` to match your project's tech stack and standards.

---

## Adding Custom Components

### Add Rules
```bash
touch .claude/rules/api-design.md
```

### Add Agents
```bash
touch .claude/agents/deployment-manager.md
```

### Add Skills
```bash
mkdir -p .claude/skills/my-skill
touch .claude/skills/my-skill/SKILL.md
```

## Best Practices

1. **Run `/wrap-up` at session end** – Keeps progress log current
2. **Keep epics modular** – One doc per initiative, no overlap
3. **Prune progress log** – Max 10 entries, oldest removed
4. **Update changelog** – For user-facing changes
5. **Run `/validate-setup`** – Periodically check for issues

## Learn More

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Commands Documentation](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- [Settings Reference](https://docs.anthropic.com/en/docs/claude-code/settings)

---

**Ready to start building!** Run `/init-project` to customize for your project.
