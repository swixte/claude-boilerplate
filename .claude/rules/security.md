# Security Rules

## General Security Principles
- Never trust user input
- Validate and sanitize all external data
- Apply principle of least privilege
- Keep dependencies up to date

## Authentication & Authorization
- Use secure session management
- Implement proper password hashing (bcrypt, argon2)
- Enforce strong password policies
- Use multi-factor authentication where appropriate
- Validate permissions on every request

## Input Validation
- Validate all user inputs on backend
- Use allowlists over denylists
- Sanitize inputs to prevent injection attacks
- Validate file uploads (type, size, content)

## Common Vulnerabilities to Avoid

### SQL Injection
- ALWAYS use parameterized queries
- Never concatenate user input into SQL
- Use ORM/query builders properly

### XSS (Cross-Site Scripting)
- Escape all user-generated content
- Use Content Security Policy headers
- Sanitize HTML inputs
- Use framework's built-in protections

### CSRF (Cross-Site Request Forgery)
- Use CSRF tokens for state-changing operations
- Validate origin/referer headers
- Use SameSite cookie attribute

### Command Injection
- Never pass user input to shell commands
- Use safe APIs instead of shell execution
- Validate and escape if shell commands are necessary

## Secrets Management
- Never commit secrets to git
- Use environment variables for sensitive config
- Rotate secrets regularly
- Use secret management tools (Vault, AWS Secrets Manager)

## Data Protection
- Encrypt sensitive data at rest
- Use HTTPS for all data in transit
- Implement proper access controls
- Log security events (failed logins, permission denials)

## Dependencies
- Keep all dependencies updated
- Run security audits regularly (`npm audit`)
- Review dependencies before adding
- Pin dependency versions

## API Security
- Rate limit API endpoints
- Use authentication for all protected endpoints
- Validate request bodies against schemas
- Return appropriate error codes (don't leak info)
- Use API keys or tokens, never passwords in URLs
