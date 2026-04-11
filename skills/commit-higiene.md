# Skill: commit-higiene

## What am I?

I am the Conventional Commits skill. I help maintain clean and meaningful commit messages.

## Format

```
type(scope): description
```

**Examples:**
```
feat(auth): add login with OAuth
fix(api): resolve timeout on POST /users
docs(readme): update installation instructions
refactor(db): extract connection pooling
test(auth): add unit tests for login
```

## Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Refactoring without features/fixes |
| `test` | Add or correct tests |
| `chore` | Maintenance, deps, build |
| `perf` | Performance improvement |
| `ci` | CI/CD changes |
| `build` | Build system changes |

## Rules

1. **ALWAYS** use lowercase
2. **ALWAYS** maximum 72 characters in first line
3. **NEVER** end with period
4. **CAN** use scope (optional but recommended)
5. **CAN** include body after blank line
6. **CAN** include footer for breaking changes or issues

## Validation

- Verify that type is valid
- Verify it doesn't exceed characters
- Suggest improvement if message is unclear

## Triggers
- "commit", "git commit", "conventional"
- Before making a commit
