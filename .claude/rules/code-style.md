# Code Style Rules

## General Principles
- Write clean, readable, and maintainable code
- Prefer clarity over cleverness
- Keep functions small and focused (max 50 lines)
- Use meaningful names that describe intent

## Naming Conventions
- **Variables**: camelCase (`userName`, `totalCount`)
- **Constants**: UPPER_SNAKE_CASE (`MAX_RETRIES`, `API_URL`)
- **Functions**: camelCase, verb-based (`getUserData`, `calculateTotal`)
- **Classes**: PascalCase (`UserService`, `PaymentProcessor`)
- **Files**: kebab-case (`user-service.ts`, `payment-utils.ts`)

## Code Organization
- Group related functionality together
- Keep related files in the same directory
- Separate concerns (business logic, data access, presentation)
- Avoid deep nesting (max 3 levels)

## Comments
- Write self-documenting code first
- Add comments only when "why" isn't obvious from code
- Keep comments up to date with code changes
- Document complex algorithms or business logic

## Error Handling
- Handle errors explicitly, don't ignore them
- Use meaningful error messages
- Log errors with appropriate context
- Validate inputs at system boundaries

## Performance
- Don't optimize prematurely
- Profile before optimizing
- Consider time and space complexity for critical paths
- Cache expensive operations when appropriate
