# Project Name

## Overview
Brief description of what this project does and its main purpose.

## Repository Info
- **GitHub**: https://github.com/your-org/your-repo
- **Main Branch**: main
- **Tech Stack**: [List your main technologies]

## Architecture
High-level architecture overview:
- Frontend: [Framework/Library]
- Backend: [Framework/Language]
- Database: [Database type]
- Infrastructure: [Cloud/Hosting]

## Project Structure
```
/src          - Source code
/tests        - Test files
/docs         - Documentation
/scripts      - Build and utility scripts
/.claude      - Claude Code configuration
```

## Common Commands
- **Install dependencies**: `npm install` (or your package manager)
- **Development server**: `npm run dev`
- **Run tests**: `npm run test`
- **Build**: `npm run build`
- **Lint**: `npm run lint`

## Coding Standards
- Follow [ESLint/Prettier/your linter] rules
- Write tests for new features
- Keep functions small and focused
- Use meaningful variable names
- Document complex logic

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
Required environment variables (see `.env.example`):
- `DATABASE_URL` - Database connection string
- `API_KEY` - External API key
- `NODE_ENV` - Environment (development/production)

## Deployment
- **Staging**: Automatically deploys from `develop` branch
- **Production**: Automatically deploys from `main` branch
- **Manual Deploy**: Run `npm run deploy`

## Additional Resources
- API Documentation: @docs/api.md
- Database Schema: @docs/schema.md
- Design System: @docs/design.md

## Notes
Any project-specific context, gotchas, or important information that Claude should know when working on this project.
