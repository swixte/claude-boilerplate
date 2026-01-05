# Roadmap

## Epics

| # | Epic | Why | Status | Depends On | Doc |
|---|------|-----|--------|------------|-----|
| 1 | Project Setup | Foundation for everything | ✅ Done | — | [→ epic-setup.md](/docs/plans/epic-setup.md) |
| 2 | Auth System | Users need to log in | 🟡 Active | 1 | [→ epic-auth.md](/docs/plans/epic-auth.md) |
| 3 | Core API | Main functionality | ⚪ Blocked | 2 | [→ epic-api.md](/docs/plans/epic-api.md) |
| 4 | Dashboard | User-facing UI | ⚪ Blocked | 2, 3 | — |
| 5 | Polish & Launch | Production ready | ⚪ Blocked | 1-4 | — |

**Status Key:** ✅ Done | 🟡 Active | ⚪ Blocked | 🔴 Problem

## Dependency Graph
```
1. Setup
   └── 2. Auth
       ├── 3. API
       │   └── 4. Dashboard
       └── 4. Dashboard
           └── 5. Launch
```

## Active Epic
**Current Focus:** Epic 2 - Auth System
**Next Up:** Epic 3 - Core API (unblocked when Auth complete)

## Blocked / Risks
- Epic 3 waiting on Auth
- TBD: Third-party API key needed for Epic 4

## Completed
| Epic | Outcome |
|------|---------|
| 1. Project Setup | Repo, CI/CD, base config |