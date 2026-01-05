# Claude Code Boilerplate

This is a complete boilerplate structure for Claude Code projects. Use this as a template for setting up new projects with Claude Code configuration.

## Directory Structure

```
.
├── .claude/                      # Claude Code configuration directory
│   ├── settings.json            # Project-level settings (committed)
│   ├── rules/                   # Modular instruction files
│   │   ├── code-style.md       # Code style guidelines
│   │   ├── testing.md          # Testing standards
│   │   └── security.md         # Security best practices
│   ├── agents/                  # Custom subagents
│   │   ├── qa-improver.md      # QA recursive improvement agent
│   │   └── code-reviewer.md    # Code review agent
│   └── skills/                  # Custom skills
│       └── data-analyzer/       # Example data analysis skill
│           ├── SKILL.md
│           └── scripts/
│               ├── analyze_csv.py
│               └── generate_report.py
├── CLAUDE.md                    # Project context and instructions
├── .gitignore                   # Includes Claude local file exclusions
└── README.md                    # This file
```

## What's Included

### Configuration Files

- **`.claude/settings.json`**: Project permissions, environment variables, hooks, and model settings
- **`CLAUDE.md`**: Main project context that Claude reads in every conversation
- **`.gitignore`**: Configured to exclude local Claude settings (`.local` files)

### Rules (`.claude/rules/`)

Modular instruction files for different aspects of development:
- **code-style.md**: Naming conventions, code organization, commenting guidelines
- **testing.md**: Testing philosophy, coverage goals, best practices
- **security.md**: Security principles, common vulnerabilities to avoid

### Subagents (`.claude/agents/`)

Pre-configured specialized agents:
- **qa-improver**: Recursively tests and improves code quality
- **code-reviewer**: Reviews code changes and PRs with detailed feedback

### Skills (`.claude/skills/`)

Example skill for data analysis:
- **data-analyzer**: Analyzes CSV/JSON files with Python scripts

## Getting Started

### 1. Customize for Your Project

Edit these files to match your project:

**`CLAUDE.md`**:
- Update project name and overview
- Set correct repository URL
- Define your tech stack
- List common commands
- Document architecture

**`.claude/settings.json`**:
- Update `GITHUB_REPO` environment variable
- Adjust allowed/denied Bash commands
- Configure hooks as needed

### 2. Add Your Own Rules

Create additional rule files in `.claude/rules/`:
```bash
touch .claude/rules/api-design.md
touch .claude/rules/database.md
```

### 3. Create Custom Agents

Add specialized agents for your workflow:
```bash
touch .claude/agents/deployment-manager.md
touch .claude/agents/documentation-writer.md
```

### 4. Add Skills

Create skills for repetitive tasks or specialized knowledge:
```bash
mkdir -p .claude/skills/my-skill
touch .claude/skills/my-skill/SKILL.md
```

## Configuration Scopes

Claude Code uses a hierarchy of configuration scopes:

| Scope | Location | Committed | Purpose |
|-------|----------|-----------|---------|
| **Local** | `.claude/*.local.*` | No (gitignored) | Personal project settings |
| **Project** | `.claude/` | Yes | Shared team configuration |
| **User** | `~/.claude/` | No | Your global settings |
| **Enterprise** | Managed by IT | - | Organization-wide settings |

## Local Overrides

Create these files for personal project customization (automatically gitignored):

- `.claude/settings.local.json` - Personal permission overrides
- `.claude/CLAUDE.local.md` - Personal project notes

## Using the Subagents

### QA Improver
```
Use the qa-improver agent to test and improve the checkout feature
```

Claude will delegate to the QA agent which will:
1. Run tests
2. Identify issues
3. Fix problems
4. Re-test
5. Repeat until quality standards are met

### Code Reviewer
```
Use the code-reviewer agent to review my recent changes
```

The reviewer will analyze your code against project standards and provide detailed feedback.

## Using the Data Analyzer Skill

Claude will automatically use this skill when you work with data:

```
Analyze the sales_data.csv file and create a summary report
```

## Environment Variables

The boilerplate includes these environment variables in `settings.json`:

- `GITHUB_REPO`: Your repository (update this!)
- `MAIN_BRANCH`: Your main branch name
- `NODE_ENV`: Development environment

Add more as needed for your project.

## Security

The `.gitignore` is configured to prevent committing:
- `.env` files
- Local Claude settings
- Secrets directory
- API keys and credentials

**Always review files before committing to ensure no secrets are included.**

## Best Practices

1. **Keep CLAUDE.md updated**: As your project evolves, update the context
2. **Use modular rules**: Split large instruction sets into topic-specific files
3. **Document environment setup**: Include all required env vars in CLAUDE.md
4. **Share with team**: Commit `.claude/` directory to share configuration
5. **Test agents**: Verify custom agents work as expected
6. **Review permissions**: Regularly audit allowed/denied commands

## Next Steps

1. Initialize git repository: `git init`
2. Customize `CLAUDE.md` with your project details
3. Update environment variables in `settings.json`
4. Add project-specific rules, agents, and skills
5. Start using Claude Code: `claude-code`

## Learn More

- [Claude Code Documentation](https://code.claude.com/docs)
- [Skills Documentation](https://code.claude.com/docs/en/skills.md)
- [Subagents Documentation](https://code.claude.com/docs/en/sub-agents.md)
- [Settings Reference](https://code.claude.com/docs/en/settings.md)

---

**Ready to start building!** This boilerplate gives you a solid foundation for working with Claude Code on any project.
