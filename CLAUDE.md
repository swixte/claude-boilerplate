# Project Name

## Project Overview
[INSERT] Brief one-sentence purpose + main value proposition.

### Planning Hierarchy
- **Roadmap** (`/docs/roadmap.md`) – Epics, features, high-level status. Updated as work completes. Should contain a modular view of entire project.
- **Epic Docs** (`/docs/epics/epic-*.md`) – Detailed specs, decisions, implementation phases. One per major initiative, modular no direct overlap 
- **Session Planning** – Use Plan Mode for tactical exploration. Ephemeral, not saved.

### Progress Tracking
- **Progress Log** (`/docs/progress.md`) – Rolling 10-entry log of session progress
- Each entry captures: epic, what was done, decisions made, next steps, blockers
- Updated at end of each working session
- When adding entry 11+, prune the oldest

### Session Flow
1. **Start** – Read progress log, roadmap, and relevant epic doc
2. **Plan** – Use Plan Mode to explore current task
3. **Execute** – Implement
4. **Wrap Up** – Add progress log entry, update epic doc and roadmap as needed

## Client / User Context
You are working with a technical product manager who prefers:
- Concise answers
- Clear reasoning
- Confidence that you understand project context & trade-offs

## Repository Info
- [INSERT] **GitHub**: https://github.com/your-org/your-repo
- [INSERT] **Main Branch**: main
- [INSERT] **Tech Stack**: [List your main technologies]

## Architecture
High-level architecture overview:
- [INSERT] Frontend: [Framework/Library]
- [INSERT] Backend: [Framework/Language]
- [INSERT] Database: [Database type]
- [INSERT] Infrastructure: [Cloud/Hosting]
- ** More details can be updated and viewed in /docs/architecture.md 

## Project Structure
This is a **monorepo** with separate frontend and backend packages:
```
/frontend         - Frontend application
  /src            - React/Vue/etc source code
  /public         - Static assets
  /tests          - Frontend tests
  package.json    - Frontend dependencies

/backend          - Backend API
  /src            - API source code
  /tests          - Backend tests
  package.json    - Backend dependencies

/shared           - Shared code between frontend/backend (types, utils)
/docs             - Documentation
/scripts          - Build and utility scripts
/.claude          - Claude Code configuration
package.json      - Root workspace config (if using npm/yarn workspaces)
```

### Monorepo Conventions
- Each package has its own `package.json` and can be developed/tested independently
- Shared types and utilities go in `/shared`
- Run commands from root or specific package directory as needed

## Develop Worflow 
[INSERT] A high level description of the development workflow the project should follow. 

## Coding Standards
- Follow [ESLint/Prettier/your linter] rules
- Write tests for new features
- Keep functions small and focused
- Use meaningful variable names
- Document complex logic in logical place
- Avoid 


## Git Workflow
- Create feature branches from `main`
- Branch naming: `feature/description` or `fix/description`
- Commit message format: `type: description` (e.g., `feat: add user login`)
- Require PR reviews before merging
- Run tests before pushing

## Testing Guidelines
- Write unit tests for business logic
- Write integration tests for API endpoints
- Aim for [X]% code coverage
- Run tests locally before pushing

## Environment Variables
[INSERT] Required environment variables (see `.env.example`):
- `DATABASE_URL` - Database connection string
- `API_KEY` - External API key
- `NODE_ENV` - Environment (development/production)

## Deployment
- **Staging**: Automatically deploys from `develop` branch
- **Production**: Automatically deploys from `main` branch
- **Manual Deploy**: Run `npm run deploy`

## Project Documentation in /docs
Please review and update this documentation as needed throughout the lifecycle of project development.
- Software Architecture: @docs/architecture.md 
- Changelog: @docs/changelog.md
- API Documentation: @docs/api.md (create when needed)
- Database Schema: @docs/schema.md (create when needed)
- Design System: @docs/design.md (create when needed)

## Notes
[INSERT] Any project-specific context, gotchas, or important information that Claude should know when working on this project.
