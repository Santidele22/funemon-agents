# Inter-Agent Communication Protocol

## Overview

Funemon agents communicate via structured messages. This document defines the protocol.

## Communication Flow

```
Orchestrator
    │
    ├──(task)──▶ PM
    │              │
    │◀──(result)──┤
    │
    ├──(task)──▶ Backend
    │              │
    │◀──(result)──┤
    │
    └──(task)──▶ Tester
                   │
                   └─(result)──▶ Orchestrator
```

## Message Types

### 1. TASK
Sent when an agent delegates work to another.

**Structure:**
```json
{
  "type": "task",
  "task_id": "uuid",
  "from": "backend",
  "to": "tester",
  "timestamp": "ISO8601",
  "deadline": "ISO8601",
  "payload": {
    "description": "...",
    "context": {...},
    "success_criteria": [...],
    "resources": {...}
  }
}
```

### 2. RESULT
Sent when an agent completes a task.

**Structure:**
```json
{
  "type": "result",
  "task_id": "uuid",
  "from": "tester",
  "to": "backend",
  "timestamp": "ISO8601",
  "status": "completed | pending_approval | error",
  "payload": {
    "output": {...},
    "logs": [...],
    "next_actions": [...],
    "delegate_to": ["security"]
  }
}
```

### 3. ACK (Acknowledgment)
Sent to confirm receipt of a message.

**Structure:**
```json
{
  "type": "ack",
  "message_id": "uuid",
  "original_task_id": "uuid",
  "status": "received | rejected",
  "reason": "..."
}
```

## Communication Rules

### a) All messages include
- `type`: TASK, RESULT, or ACK
- `from`: Sender agent
- `to`: Receiver agent
- `timestamp`: When sent

### b) TASK must include
- `task_id`: Unique task identifier
- `deadline`: When it must be completed
- `payload.description`: What to do
- `payload.success_criteria`: How to verify

### c) RESULT must include
- `status`: completed, pending_approval, error
- `payload.output`: What was produced
- `payload.logs`: Relevant notes
- `payload.next_actions`: Suggestions

### d) Errors
- If an agent cannot process a TASK, it must return a RESULT with `status: error` and explanation

## Communication Examples

### Step 1: Orchestrator → Backend
```json
{
  "type": "task",
  "task_id": "123e4567-e89b-12d3-a456-426614174000",
  "from": "orchestrator",
  "to": "backend",
  "timestamp": "2026-04-09T10:00:00Z",
  "deadline": "2026-04-09T18:00:00Z",
  "payload": {
    "description": "Implement JWT login endpoint",
    "context": {
      "project": "my-app",
      "user_story": "US-001"
    },
    "success_criteria": [
      "Endpoint /api/auth/login functional",
      "Generates valid JWT",
      "Tests passing"
    ]
  }
}
```

### Step 2: Backend → Tester (delegation)
```json
{
  "type": "task",
  "task_id": "223e4567-e89b-12d3-a456-426614174001",
  "from": "backend",
  "to": "tester",
  "timestamp": "2026-04-09T12:00:00Z",
  "deadline": "2026-04-09T16:00:00Z",
  "payload": {
    "description": "Write tests for login endpoint",
    "context": {
      "endpoint": "/api/auth/login",
      "existing_tests": []
    },
    "success_criteria": [
      "Unit tests for auth",
      "Integration tests",
      "Coverage > 80%"
    ]
  }
}
```

### Step 3: Tester → Backend
```json
{
  "type": "result",
  "task_id": "223e4567-e89b-12d3-a456-426614174001",
  "from": "tester",
  "to": "backend",
  "timestamp": "2026-04-09T15:30:00Z",
  "status": "completed",
  "payload": {
    "output": {
      "tests_created": 12,
      "coverage": "85%",
      "files": ["tests/auth_test.rs"]
    },
    "logs": [
      "JWT mock working",
      "Edge case tests included"
    ],
    "next_actions": [
      "Review tests with code review"
    ],
    "delegate_to": ["security"]
  }
}
```

### Step 4: Backend → Orchestrator
```json
{
  "type": "result",
  "task_id": "123e4567-e89b-12d3-a456-426614174000",
  "from": "backend",
  "to": "orchestrator",
  "timestamp": "2026-04-09T16:00:00Z",
  "status": "completed",
  "payload": {
    "output": {
      "endpoint_created": "/api/auth/login",
      "tests_coverage": "85%",
      "security_review": "pending"
    },
    "logs": [
      "JWT with 24h expiration",
      "Password hashed with bcrypt"
    ],
    "next_actions": [
      "Delegate to security for review"
    ]
  }
}
```

## Timeout and Retry

- **Timeout**: If an agent doesn't respond in 30 min, re-send TASK
- **Max retries**: 3 attempts
- **Fallback**: If all attempts fail, report error to orchestrator

## Logging

All messages must be saved in Funemon for audit:
```python
funemon_memory_store(
    type="observation",
    title=f"Message {type} between {from} and {to}",
    what=f"task_id: {task_id}, status: {status}"
)
```

## Language Rules

**CRITICAL:** All inter-agent communication MUST follow these language rules:

### 1. Agent-to-Agent: ENGLISH

All Task templates must be in English.
All Result templates must be in English.
All communication between Magnus, Bruno, Aurora, Almendra, Gabriela, ATLAS, Tyrion must be in English.

**Example:**
```json
{
  "type": "task",
  "task_id": "task-001",
  "from": "magnus",
  "to": "bruno",
  "payload": {
    "description": "Write unit tests for authentication API",
    "context": {
      "endpoint": "/api/auth/login"
    },
    "success_criteria": [
      "Tests pass",
      "Coverage > 80%"
    ]
  }
}
```

### 2. Agent-to-User (Santi): SPANISH

All explanations to Santi must be in Spanish.
All status reports to Santi must be in Spanish.
All approval requests to Santi must be in Spanish.

**Example:**
```markdown
## Estado de la Tarea

**Status:** Completado

He terminado de implementar el endpoint de autenticación.
¿Necesitas que haga algún cambio antes de crear el PR?
```

### 3. Templates: ENGLISH Only

- `task.md` template: English
- `result.md` template: English
- `delegation-memory.md` template: English

### 4. Memory: Mixed

- Keys: English
- Values: Context-dependent (English for technical, Spanish for user-facing)

```yaml
funemon_memory_store(
  type: "plan",
  title: "Delegation: Magnus → Bruno",  # English
  what: "Write tests for auth API",       # English
  where_field: "src/api/auth.rs",         # English
  learned: "User requested OAuth support" # Can be Spanish for user context
)
```

### Why These Rules?

- **English** standardizes technical communication between agents
- **Spanish** provides natural communication with Santi
- This prevents confusion and ensures consistency across the team

---

## Tools

Agents can use templates in `templates/`:
- `task.md`: To create tasks
- `result.md`: To return results
- `delegation-memory.md`: To track delegations in memory