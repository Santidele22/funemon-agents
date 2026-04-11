# Template: Delegation Memory

Template for tracking delegation events in Funemon Memory system.

---

## Purpose

Every delegation between agents MUST be tracked in Funemon Memory for:
- Audit trail
- Knowledge sharing
- Debdugging delegation chains
- Performance metrics

---

## Template Structure

### When Initiating Delegation

```yaml
funemon_memory_store(
  type: "plan",
  title: "Delegation: {from_agent} → {to_agent}",
  what: "Delegating: {task_description}",
  where_field: "{component_or_file}",
  why: "Reason: {reason_for_delegation}",
  learned: "Expected: {expected_outcome}"
)
```

### When Delegation Completes Successfully

```yaml
funemon_memory_store(
  type: "observation",
  title: "Delegation Complete: {from_agent} ← {to_agent}",
  what: "Completed: {task_description}",
  where_field: "{component_or_file}",
  why: "Result: {result_summary}",
  learned: "{key_learnings_from_delegation}"
)
```

### When Delegation Fails

```yaml
funemon_memory_store(
  type: "error",
  title: "Delegation Failed: {from_agent} → {to_agent}",
  what: "Failed: {task_description}",
  where_field: "{component_or_file}",
  why: "Error: {error_reason}",
  learned: "What was tried: {troubleshooting_notes}"
)
```

---

## Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `from_agent` | string | Agent initiating delegation | "Magnus" |
| `to_agent` | string | Agent receiving delegation | "Bruno" |
| `task_id` | string | Unique task identifier | "task-001-api-tests" |
| `timestamp` | ISO8601 | When delegation was initiated | "2026-04-11T10:30:00Z" |
| `status` | enum | Current status | pending / in_progress / completed / error |
| `task_description` | string | What needs to be done | "Write unit tests for login API" |
| `success_criteria` | array | How to verify completion | ["Tests pass", "Coverage > 80%"] |
| `context` | object | Additional context | {"endpoint": "/api/auth/login"} |
| `result` | enum | Final result | completed / pending / error |

---

## Example Usage

### Example 1: Magnus delegates toBruno

**Step 1: Magnus initiates delegation**

```yaml
funemon_memory_store(
  type: "plan",
  title: "Delegation: Magnus → Bruno",
  what: "Delegating: Write tests for authentication API",
  where_field: "src/api/auth.rs",
  why: "TDD requires tests before implementation",
  learned: "Expected: Test files with >80% coverage"
)
```

**Step 2: Bruno receives task**

Bruno checks memory for context:
```yaml
funemon_memory_context(session_id: "bruno-session") 
# Returns: Magnus's delegation plan
```

**Step 3: Bruno completes task**

Bruno stores result:
```yaml
funemon_memory_store(
  type: "observation",
  title: "Delegation Complete: Magnus ← Bruno",
  what: "Completed: Auth API tests created",
  where_field: "tests/api/auth_test.rs",
  why: "Result: 12 tests created, 85% coverage",
  learned: "Edge cases covered: null input, expired tokens"
)
```

**Step 4: Magnus receives result**

Magnus checks memory for Bruno's result.

---

### Example 2: Aurora delegates to Almendra

```yaml
funemon_memory_store(
  type: "plan",
  title: "Delegation: Aurora → Almendra",
  what: "Delegating: Document new UI component library",
  where_field: "src/ui/components/",
  why: "User-facing components need documentation",
  learned: "Expected: README with usage examples"
)
```

---

### Example 3: Delegation with error

```yaml
funemon_memory_store(
  type: "error",
  title: "Delegation Failed: Magnus → Bruno",
  what: "Failed: Write tests for payment module",
  where_field: "src/api/payment.rs",
  why: "Error: Insufficient context provided",
  learned: "Payment provider API spec needed before tests"
)
```

---

## Status Flow

```
┌─────────┐     ┌──────────────┐     ┌───────────┐
│ pending │────▶│ in_progress  │────▶│ completed │
└─────────┘     └──────────────┘     └───────────┘
                      │
                      │ error
                      ▼
                ┌─────────┐
                │  error  │
                └─────────┘
```

---

## Best Practices

1. **Always set a title** in format: "Delegation: {from} → {to}"
2. **Use consistent naming** for agents: Magnus, Bruno, Aurora, Almendra, Gabriela, Tyrion, ATLAS
3. **Include component name** in where_field for easy searching
4. **Store both initiation and completion** for full audit trail
5. **Include success criteria** in learned field when initiating

---

## Integration with Task/Result Templates

The delegation memory template works in conjunction with:

- `templates/task.md` - Structured task delegation message
- `templates/result.md` - Structured result return message

**Flow:**
1. Create Task from template
2. Store delegation in Memory (this template)
3. Wait for Result
4. Store result observation in Memory
5. Continue with next step

---

## Querying Delegation History

To search for past delegations:

```yaml
funemon_memory_search(
  query: "Delegation:Magnus",
  limit: 10
)
```

To search for specific component:

```yaml
funemon_memory_search(
  query: "auth.rs",
  limit: 5
)
```

---

**Remember:** Every delegation creates knowledge. Track it properly.