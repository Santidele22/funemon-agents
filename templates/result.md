# Template: Result

Template for an agent to return the result of a task.

---

## Task Result

**ID**: `[task_id]`
**From**: `[agent_name]`
**To**: `[requesting_agent]`
**Date**: `[timestamp]`

---

## Status

```
[pending_approval | completed | error]
```

---

## Output

```markdown
## What was produced

[Description of the output produced by the agent]

## Files Created/Modified

- `src/file1.rs` - [description]
- `src/file2.ts` - [description]

## Tests

- ✅ Test 1: passing
- ✅ Test 2: passing

## Coverage

[Coverage percentage if applicable]
```

---

## Logs

```markdown
## Agent Notes

[Relevant notes during execution]

## Decisions Made

- [Decision 1]: [rationale]
- [Decision 2]: [rationale]

## Issues Encountered

- [Issue 1]: [description]
- [Issue 2]: [description]
```

---

## Next Actions

```markdown
## Suggestions

- [ ] [Next step 1]
- [ ] [Next step 2]

## Other Agents to Involve

- **Agent X**: [Why they should participate]
- **Agent Y**: [Why they should participate]

## Dependencies

- [Dependency 1] must complete first
- [Dependency 2] can run in parallel
```

---

## Approval Request

```
[If status is "pending_approval"]

Approval required for:
- [ ] Execute code in [environment]
- [ ] Apply changes to [system]
- [ ] [Other action requiring approval]
```

---

## Error Info (if applicable)

```markdown
## Error

**Type**: [error type]
**Message**: [error message]

## Stack Trace

```
[stack trace if applicable]
```

## Possible Causes

- [Cause 1]
- [Cause 2]

## Fix Suggestions

[How to resolve the error]
```

---

## Example Usage

```markdown
## Task Result

**ID**: `task-001-auth-tests`
**From**: `Bruno`
**To**: `Magnus`
**Date**: `2026-04-11T15:30:00Z`

## Status

```
completed
```

## Output

## What was produced

Created unit tests and integration tests for authentication API.

## Files Created/Modified

- `tests/api/auth_test.rs` - Unit tests for auth module
- `tests/integration/auth_integration_test.rs` - Integration tests

## Tests

- ✅ test_login_success: passing
- ✅ test_login_invalid_credentials: passing
- ✅ test_login_null_input: passing
- ✅ test_login_expired_token: passing

## Coverage

85% coverage for auth module

## Logs

## Agent Notes

- Mocked the JWT token generation
- Covered edge cases for invalid inputs
- Integration tests verify full login flow

## Decisions Made

- Used bcrypt mock for password hashing: Speeds up tests
- Separated unit and integration tests: Better organization

## Issues Encountered

None

## Next Actions

## Suggestions

- [ ] Run tests with `cargo test`
- [ ] Verify coverage report

## Other Agents to Involve

None required for this task

## Dependencies

- Magnus can now proceed with implementation
- Consider Gabriela for security review after implementation
```

---

**Note:** This template must be used in ENGLISH for all inter-agent communication.