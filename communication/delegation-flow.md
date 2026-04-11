# Delegation Flow Protocol

## Overview

This document defines the MANDATORY delegation protocol for all Funemon agents. Following this protocol ensures proper task distribution, quality assurance, and traceability.

## CRITICAL: Delegation Triggers

### MANDATORY Delegation Points

| Trigger | Delegate To | When | Priority |
|---------|-------------|------|----------|
| **Tests needed** | Bruno | BEFORE implementing | HIGHEST |
| **Documentation needed** | Almendra | After implementation | HIGH |
| **Security review needed** | Gabriela | After implementation | HIGH |
| **API design** | Magnus | During planning | MEDIUM |
| **UI/UX** | Aurora | During design | MEDIUM |

### The TDD Flow (Test-Driven Development)

**IMPORTANT:** Tests MUST be delegated FIRST, before any implementation.

```
1. Receive feature request
2. DELEGATE tests to Bruno (Create Task template)
3. WAIT for Bruno's test results
4. IMPLEMENT based on tests
5. VERIFY tests pass
6. DELEGATE docs to Almendra (if needed)
7. DELEGATE security review to Gabriela (if needed)
8. CREATE PR only when ALL complete
```

## Delegation Workflow

### Complete Flow Example

```yaml
Magnus receives task "build API"
  │
  ├─ PHASE 1: Test Planning
  │    │
  │    └─ Magnus: "I need tests FIRST" → DELEGATE to Bruno
  │         - Create Task using templates/task.md
  │         - Save to memory: type: "plan", title: "Delegation: Magnus → Bruno"
  │         - WAIT for Result from Bruno
  │
  ├─ PHASE 2: Test Results
  │    │
  │    └─ Bruno: Writes tests → RETURN Result to Magnus
  │         - Test files created
  │         - Coverage metrics
  │         - Status: "completed"
  │
  ├─ PHASE 3: Implementation
  │    │
  │    └─ Magnus: Implements API passing tests
  │         - Code written to satisfy tests
  │         - All tests passing
  │
  ├─ PHASE 4: Documentation
  │    │
  │    └─ Magnus: "I need docs" → DELEGATE to Almendra
  │         - Create Task for documentation
  │         - WAIT for Result from Almendra
  │         - Almendra: Documents API → RETURN Result
  │
  ├─ PHASE 5: Security Review (if applicable)
  │    │
  │    └─ Magnus: "I need security review" → DELEGATE to Gabriela
  │         - Create Task for security review
  │         - WAIT for Result from Gabriela
  │         - Gabriela: Security review → RETURN Result
  │
  └─ PHASE 6: Finalize
       │
       └─ Magnus: "All complete" → CREATE PR
            - git checkout -b feat/api-endpoint
            - Small commits per logical change
            - git push -u origin feat/api-endpoint
            - gh pr create
            - RETURN: "PR created, waiting Santi approval"
```

## Inter-Agent Communication Protocol

### Task Template (Sender)

When delegating, use the Task template from `templates/task.md`:

```markdown
## Task

**ID**: `[task_id]`**De**: `[from_agent]`
**Para**: `[to_agent]`
**Fecha**: `[timestamp]`
**Deadline**: `[deadline]`

## Description
[Clear description of what needs to be done]

## Context
[Background information, existing decisions, constraints]

## Success Criteria
- [ ] [Measurable criterion 1]
- [ ] [Measurable criterion 2]

## Resources
- Code: [links]
- Docs: [links]## Expected Response
Status: completed | pending_approval | error
```

### Result Template (Receiver)

When returning results, use the Result template from `templates/result.md`:

```markdown
## Result

**ID**: `[task_id]`
**De**: `[agent_name]`
**Para**: `[requesting_agent]`
**Fecha**: `[timestamp]`

## Status
[completed | pending_approval | error]

## Output
[What was produced]
- Files Created/Modified
- Tests passing
- Coverage metrics

## Logs
[Relevant notes during execution]

## Next Actions
[Suggestions for next steps]
```

## Memory Tracking Requirement

Every delegation MUST be tracked in Funemon Memory:

### Before Delegating

```yaml
funemon_memory_store(
  type: "plan",
  title: "Delegation: {from_agent} → {to_agent}",
  what: "Delegating {task_description}",
  where_field: "{component_or_file}",
  why: "{reason_for_delegation}",
  learned: "{expected_outcome}"
)
```

### After Receiving Result

```yaml
funemon_memory_store(
  type: "observation",
  title: "Result received from {to_agent}",
  what: "{task_description} completed",
  where_field: "{component_or_file}",
  why: "{delegation_result}",
  learned: "{key_learnings}"
)
```

## Delegation Decision Tree

```
START: Receive task
  │
  ├─ Does task require tests?
  │    │
  │    └─ YES → Delegate to Bruno FIRST
  │              Wait for test results
  │              Implement based on tests
  │
  ├─ Does task create/modify code?
  │    │
  │    └─ YES → After implementation:
  │              - Delegate docs to Almendra (if user-facing)
  │              - Delegate security to Gabriela (if security-sensitive)
  │
  ├─ Does task need UI/UX input?
  │    │
  │    └─ YES → Delegate to Aurora for design review
  │
  └─ All complete?
       │
       └─ YES → Create PR
                Wait for Santi approval
```

## Agent Responsibilities

### Magnus (Backend Developer)
- Receives backend tasks from Orchestrator
- MUST delegate tests to Bruno before implementing
- MUST delegate docs to Almendra for user-facing features
- MUST delegate security review to Gabriela for auth/data features- Creates PR only when all dependencies complete

### Bruno (QA Engineer)
- Writes tests based on specifications
- Returns test files and coverage metrics
- Provides feedback on testability of requirements

### Aurora (Frontend Developer)
- Designs UI components
- Delegates tests to Bruno for frontend code
- Coordinates with Magnus for API integration

### Almendra (Technical Writer)
- Creates documentation based on code/features
- Updates README, API docs, CHANGELOG
- Returns documentation files

### Gabriela (Security Engineer)
- Reviews code for security vulnerabilities
- Provides security recommendations
- Signs off on sensitive features

## Error Handling

### If Delegation Fails

```yaml
funemon_memory_store(
  type: "error",
  title: "Delegation failed: {from_agent} → {to_agent}",
  what: "{task_description}",
  where_field: "{component}",
  why: "{error_reason}",
  learned: "{what_was_tried}"
)
```

### Escalation Path

1. First failure → Retry delegation with additional context
2. Second failure → Escalate to Orchestrator (Tyrion)
3. Critical block → Report to Santi for intervention

## Summary Checklist

Before marking a task as complete, verify:

- [ ] Tests delegated to Bruno (if applicable)
- [ ] Tests received and passing
- [ ] Implementation complete
- [ ] Documentation delegated to Almendra (if applicable)
- [ ] Security review delegated to Gabriela (if applicable)
- [ ] All delegations tracked in Memory
- [ ] PR created
- [ ] Waiting for Santi approval

---

**Remember:** Delegation is not optional. Proper delegation ensures quality, maintainability, and knowledge sharing across the team.