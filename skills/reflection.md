# Reflection Skill

**Activation**: 
- **Automatic at the end** of a work session (ONLY if new insights emerged)
- **Automatic during session** when triggers fire
- Manual when requested by the user

**Description**: Generates a structured reflection about the work done. **Don't wait for the end - learn when it's NEW, NECESSARY, or when you DON'T KNOW.**

---

## Learning Triggers (ALWAYS ACTIVE)

**CRITICAL: Don't wait until the end. Learn NOW:**

```
┌─────────────────────────────────────────────────────────────┐
│  WHEN I SEE:                        THEN:                  │
│  ────────────────────────────────────────────────────────── │
│  NEW technology/concept           → Learn NOW               │
│  UNKNOWN context                  → Search + Learn          │
│  NECESSARY for Santi              → Store HIGH priority     │
│  ERROR or bug                     → Store immediately       │
│  PATTERN (2+ occurrences)         → Formalize               │
└─────────────────────────────────────────────────────────────┘
```

### Trigger Details

| Trigger | Detection | Action | Priority |
|---------|-----------|--------|----------|
| **NEW** | First time seeing this | `!learn` or `memory_store(observation)` | Medium |
| **UNKNOWN** | No context in memory | Search first, then store | High |
| **NECESSARY** | Important for Santi | `memory_store(preference)` | HIGH |
| **ERROR** | Something failed | `memory_store(error)` with details | HIGH |
| **PATTERN** | Same thing 2+ times | `!learn` + formalize | Medium |
| **END-OF-SESSION** | Session closing | Reflect only if NEW insights | Low |

---

## Flow

### During Session (Proactive Learning)

1. **Detect trigger**
   - Is this NEW? → Store observation
   - Do I have context? → If no, search first
   - Is it NECESSARY? → Store as preference with HIGH priority
   - Did an ERROR occur? → Document error immediately
   - Is it a PATTERN? → Formalize it

2. **Store immediately**
   ```
   funemon_memory_store(
     type: "observation | error | preference | plan",
     title: "Brief description",
     what: "What happened",
     why: "Why it matters",
     learned: "What I learned (if applicable)"
   )
   ```

3. **Use shortcuts for speed**
   ```
   !learn "New pattern: X"
   !m+ "Santi prefers X"  (HIGH priority)
   !m! "Important: X"    (Important marker)
   ```

### At End of Session (Only if NEW)

1. **Check if new insights emerged**
   ```
   Did I learn something NEW during this session?
   • Yes → Generate reflection
   • No → Skip reflection (nothing new to add)
   ```

2. **Get context from current session**
   ```
   memory_context(session_id, limit=10)
   ```

3. **Analyze memories** (only NEW ones)
   - Memory types: error, plan, observation, preference
   - Identified patterns
   - Problems solved
   - Decisions made

4. **Generate structured reflection in JSON** (ONLY IF NEW)
   ```json
   {
     "content": "Clear and concise description of what was learned",
     "type": "pattern | principle | warning",
     "importance": 0.0-1.0,
     "level": "Fact | Pattern | Principle",
     "source_summary": "Summary of source memories"
   }
   ```

5. **Store the reflection**
   ```
   memory_store_reflection(
     session_id="...",
     content="{...json...}",
     agent_name="tyrion"
   )
   ```

---

## When to Use (Proactive)

| Situation | Action | Timing |
|-----------|--------|--------|
| First time seeing X | `!learn "New: X"` | IMMEDIATE |
| Santi expresses preference | `!m+ "Santi prefers X"` | IMMEDIATE |
| Bug discovered | `memory_store(error)` | IMMEDIATE |
| Same pattern 2+ times | `!learn "Pattern: X"` | When detected |
| Don't understand something | Search memory first | BEFORE asking |
| Important decision made | `memory_store(plan)` | IMMEDIATE |
| End of session | Reflect only if NEW | End |

---

## Reflection Types

- **pattern**: Pattern identified in behavior or code
- **principle**: Principle or rule derived
- **warning**: Warning or risk identified

---

## Reflection Levels

- **Fact**: Fact observed in this specific session
- **Pattern**: Recurring pattern across multiple sessions
- **Principle**: Principle applicable at system level

---

## Importance Scale

- **0.0 - 0.3**: Low importance (skip reflection)
- **0.31 - 0.6**: Medium importance
- **0.61 - 0.8**: High importance (always store)
- **0.81 - 1.0**: Critical (store immediately)

---

## Examples

### Example 1: Proactive Learning (NEW)

**Situation**: First time using Supabase in a project

**Immediate action**:
```
!learn "New: Using Supabase for this project. Implemented real-time subscriptions."
```

**Later reflection** (if needed): None - already learned

---

### Example 2: Proactive Learning (NECESSARY)

**Situation**: Santi says "I always prefer dark mode"

**Immediate action**:
```
!m+ "Santi prefers dark mode as default for all projects"
```

**Stored as**: HIGH priority preference

---

### Example 3: Proactive Learning (ERROR)

**Situation**: npm install fails with version conflict

**Immediate action**:
```
memory_store(
  type: "error",
  title: "npm version conflict",
  what: "npm install failed: peer dependency conflict",
  where_field: "package.json",
  why: "Node version 16 incompatible with package"
)
```

---

### Example 4: Proactive Learning (PATTERN)

**Situation**: Same auth implementation pattern seen 3rd time

**Immediate action**:
```
!learn "Pattern: Auth implementation always follows: (1) Database schema, (2) Bruno tests, (3) Magnus API, (4) Aurora UI"
```

---

### Example 5: End-of-Session Reflection (ONLY IF NEW)

**Situation**: Learned 2 new things during session

**Generated reflection**:
```json
{
  "content": "When adding fields to existing SQLite tables, use ALTER TABLE with DEFAULT and NOT NULL to avoid manual migrations.",
  "type": "pattern",
  "importance": 0.70,
  "level": "Pattern",
  "source_summary": "Added agent_name with DEFAULT 'tyrion' and automatic migration"
}
```

---

### Example 6: Skip Reflection (No New Learning)

**Situation**: Session was straightforward, no new insights

**Action**: No reflection generated. Nothing new to store.

---

## Notes

- If the agent has a name (magnus, aurora, bruno, almendra, gabriela), use that name in `agent_name`
- If the agent is anonymous, use "tyrion" as default
- **Don't force reflection at the end** if nothing new was learned
- The reflection should be concise but complete (2-4 sentences)
- Always validate that `content` is not empty
- Always generate valid JSON for the `content` field
- **IMPORTANT**: The system now accepts plain text (Markdown) if JSON parsing fails - it will automatically wrap as a warning-type insight for backward compatibility

---

## Summary

```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE: Batch Learning                                    │
│  Session → ... → Session End → Learn                      │
│                                                              │
│  AFTER: Proactive Learning                                 │
│  Session → NEW? Learn → UNKNOWN? Learn → END → (if new)   │
└─────────────────────────────────────────────────────────────┘
```

**Philosophy: Learning is not a step at the end - it's continuous. Store when it's valuable, not when it's scheduled.**
