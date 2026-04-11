# Template: Task

Template for sending a task from one agent to another.

---

## Task

**ID**: `[task_id]`
**From**: `[source_agent]`
**To**: `[target_agent]`
**Date**: `[timestamp]`
**Deadline**: `[deadline]`

---

## Description

```
[Clear description of what the receiving agent needs to do]
```

---

## Context

```markdown
## Background
[Relevant information about the project, prior decisions, etc.]

## Requirements
- [Requirement 1]
- [Requirement 2]

## Constraints
- [Constraint 1]
- [Constraint 2]
```

---

## Success Criteria

- [ ] [Measurable criterion 1]
- [ ] [Measurable criterion 2]
- [ ] [Measurable criterion 3]

---

## Resources

- **Code**: `[link to files]`
- **Docs**: `[link to documentation]`
- **Specs**: `[link to specifications]`

---

## Additional Notes

```
[Any extra notes for the agent]
```

---

## Expected Response

The agent must return:
1. **Status**: `pending_approval` | `completed` | `error`
2. **Output**: What was produced
3. **Logs**: Relevant notes
4. **Next Actions**: Suggested next steps

---

## Example Usage

```markdown
## Task

**ID**: `task-001-auth-tests`
**From**: `Magnus`
**To**: `Bruno`
**Date**: `2026-04-11T10:00:00Z`
**Deadline**: `2026-04-11T16:00:00Z`

## Description

Write unit tests and integration tests for the authentication API endpoint.

## Context

## Background
We are implementing a JWT-based authentication system. The login endpoint `/api/auth/login` is being built.

## Requirements
- Tests must cover happy path and error cases
- Mock the JWT token generation
- Tests should be independent and runnable in any order

## Constraints
- Use existing test framework
- No external API calls in tests

## Success Criteria

- [ ] 80%+ code coverage for auth module
- [ ] All edge cases tested (null input, expired tokens, invalid credentials)
- [ ] Integration tests for full login flow
- [ ] Tests pass with `cargo test`

## Resources

- **Code**: `src/api/auth.rs`
- **Docs**: `docs/api/auth.md`
- **Specs**: `specs/auth-spec.md`

## Additional Notes

The password hashing uses bcrypt. Mock this in tests.
```

---

**Note:** This template must be used in ENGLISH for all inter-agent communication.