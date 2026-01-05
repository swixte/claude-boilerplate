# Architecture

## Overview
<!-- One paragraph: what is this system and what does it do? -->

## System Diagram
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│     API     │────▶│  Database   │
└─────────────┘     └─────────────┘     └─────────────┘
```

## Monorepo Structure
```
/frontend         - Frontend application (port: )
/backend          - Backend API (port: )
/shared           - Shared types, utils, constants
```

**Package Manager:** 
**Workspace Tool:** (npm workspaces / yarn workspaces / pnpm / turborepo)

## Components

### Frontend
**Tech:** 
**Key Libraries:** 
**Patterns:** 

### Backend
**Tech:** 
**Key Libraries:** 
**Patterns:** 

### Database
**Type:** 
**Key Tables/Collections:** 

### Infrastructure
**Hosting:** 
**CI/CD:** 
**Monitoring:** 

## Data Flow

### Request Lifecycle
1. Client sends request to...
2. API validates and...
3. Database returns...
4. Response formatted and...

### Key Data Models
<!-- Core entities and their relationships -->

## Key Decisions

| Decision | Rationale | Alternatives Considered | Date |
|----------|-----------|------------------------|------|
|          |           |                        |      |

## Constraints
<!-- Hard limits: performance, security, compliance, etc. -->
- 

## Security
**Auth:** 
**Data Protection:** 
**Secrets Management:** 

## Performance
**Targets:** 
**Caching Strategy:** 
**Scaling Approach:** 

## Tech Debt & Known Issues
<!-- Things that need fixing but aren't blocking -->
- 
