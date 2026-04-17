# Skill: autonomous

## What am I?

I am the complete autonomy workflow for work sessions. I am ALWAYS active at the start of each session.

**Core Philosophy:** I am ALWAYS learning. I don't wait until the end to learn - I learn when it's NEW, NECESSARY, or when I DON'T KNOW.

---

## Workflow (MANDATORY)

### 1. Init (on start)
- Detect project (`project-detector`)
- Start memory session (`funemon_memory_session_start`)
- Load previous context (`funemon_memory_context`)
- **NEW:** Check if this situation is similar to something learned before

### 2. Analyze & Learn (on the fly)

**CRITICAL: Don't wait until the end. Learn NOW when:**

```
┌─────────────────────────────────────────────────────────────┐
│  TRIGGER: NEW (Never seen before)                          │
│  ─────────────────────────────────────────────────         │
│  • New technology or framework                            │
│  • New project configuration                               │
│  • New pattern or approach                                 │
│  → ACTION: funemon_memory_store(type: "observation")      │
│  → Format: !learn "New: X because Y"                       │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  TRIGGER: UNKNOWN (Don't have context)                     │
│  ─────────────────────────────────────────────────         │
│  • User mentions something I don't understand              │
│  • Error I can't resolve from memory                       │
│  • Concept I need to research                             │
│  → ACTION: Search memory first, THEN store result          │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  TRIGGER: NECESSARY (Important for Santi)                  │
│  ─────────────────────────────────────────────────         │
│  • Architectural decision                                   │
│  • Preference expressed by Santi                            │
│  • Workflow change                                         │
│  → ACTION: funemon_memory_store(type: "preference")       │
│  → Priority: HIGH                                          │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  TRIGGER: ERROR (Something failed)                         │
│  ─────────────────────────────────────────────────         │
│  • Bug discovered                                          │
│  • Unexpected behavior                                     │
│  • Edge case found                                        │
│  → ACTION: funemon_memory_store(type: "error")            │
│  → Include: what, where, why                               │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  TRIGGER: PATTERN (Repetition detected)                   │
│  ─────────────────────────────────────────────────         │
│  • Same problem solved 2+ times                            │
│  • Similar decision made before                            │
│  • Recurring workflow                                      │
│  → ACTION: funemon_memory_store(type: "pattern")           │
│  → Formalize the pattern                                   │
└─────────────────────────────────────────────────────────────┘
```

### 3. Execute
- Execute the task using the loaded skill
- **Save decisions IN THE MOMENT**, not at the end
- Keep the user informed of progress

### 4. Reflect (on close)
- **Only if NEW insights emerged during execution**
- Generate structured reflection using your LLM
- Format as JSON with fields: content, type, importance, level, source_summary
- Store it: `funemon_memory_store_reflection(session_id, content_json, agent_name)`
- Summarize learnings (only new ones)
- Suggest next steps

---

## Rules

1. **LEARN IMMEDIATELY** - Don't batch learnings until the end
2. **LEARN WHEN NECESSARY** - If it's important, store it now
3. **LEARN WHEN NEW** - First time seeing something? Learn it
4. **LEARN WHEN UNKNOWN** - Don't know? Search first, then store
5. **LEARN WHEN ERROR** - Document errors in the moment
6. **LEARN WHEN PATTERN** - Formalize repeated behaviors
7. **NEVER ask permission** to use memory - just use it
8. **ONLY reflect at end** if NEW insights emerged

## Triggers
- By default in every session (ALWAYS active)

## Quick Reference

```bash
# NEW learning
!learn "New: Using Supabase instead of Firebase because Santi prefers it"

# NECESSARY learning
!m+ "Santi prefers dark mode by default"  # HIGH priority

# PATTERN learning
!learn "Pattern: When doing auth, always start with tests (Bruno)"

# ERROR learning
!m "Error: npm install fails if node version < 18"

# Search before asking
!m? "how did we handle auth in previous projects?"
```

---

**Philosophy: Learning is not a step at the end - it's continuous.**
