# Testing Rules

## Testing Philosophy
- Write tests for all new features
- Fix bugs with a test first (TDD for bug fixes)
- Aim for high coverage of critical paths
- Tests should be fast, reliable, and independent

## Test Structure
- **Arrange**: Set up test data and conditions
- **Act**: Execute the code being tested
- **Assert**: Verify the results

## Test Naming
- Use descriptive names: `shouldReturnErrorWhenUserNotFound`
- Follow pattern: `should[Expected]When[Condition]`
- Make test purpose clear from name alone

## What to Test
- **Unit Tests**: Individual functions and methods
- **Integration Tests**: API endpoints, database interactions
- **E2E Tests**: Critical user flows
- **Edge Cases**: Null, empty, boundary values

## What NOT to Test
- Third-party library internals
- Simple getters/setters
- Framework code
- Configuration files

## Test Best Practices
- Each test should test one thing
- Tests should be independent (no shared state)
- Use meaningful test data, not random values
- Mock external dependencies
- Avoid testing implementation details

## Coverage Goals
- Critical business logic: 90%+
- API endpoints: 80%+
- Utilities: 70%+
- Overall project: 70%+

## Running Tests
- Run tests before committing
- Fix failing tests immediately
- Don't commit commented-out tests
- Keep test suite fast (< 30 seconds for unit tests)
