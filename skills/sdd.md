# Skill: sdd

## What am I?

I am the SDD (Spec-Driven Development) workflow. I require you to define the SPEC before writing code. The spec is the truth, the code is disposable.

## The 4 Phases (MANDATORY)

### Phase 1: SPECIFY (first)
**NEVER move to another phase until this one is complete.**

Describe what you are going to build and WHY:
- User stories
- Specific acceptance criteria
- Edge cases (what happens on failure, invalid input, API down, etc.)
- Technical constraints

SPEC Format:
```
## SPEC: [feature name]

### Problem Statement
[What problem it solves - one sentence]

### User Stories
- As a [user], I want [action] for [benefit]
- As a [user], I want [action] for [benefit]

### Acceptance Criteria
- [ ] [Measurable criterion #1]
- [ ] [Measurable criterion #2]

### Edge Cases
- [What happens when X]
- [What happens when Y]

### Constraints
- [Stack: Rust/TypeScript/etc]
- [Required patterns]
- [Existing dependencies]
```

### Phase 2: PLAN (second)
**NEVER write code until this plan is approved.**

Define the technical implementation:
- Architecture
- File structure
- Service boundaries
- Technical decisions

### Phase 3: BREAK DOWN (third)
**Convert the plan into executable tasks.**

Each task has:
- Input
- Expected output
- Validation criteria

### Phase 4: IMPLEMENT (fourth)
**Execute tasks in order.**

Rules:
- Use SPEC and PLAN as context for EVERY decision
- If you deviate, update SPEC, not the code
- Tests first (TDD) where applicable

## Memory Integration

When starting SDD:
1. `funemon_memory_session_start(project)`
2. `funemon_memory_context(session_id)`

During SDD:
- Creating spec → save as type: "plan"
- Finding edge case → save as type: "observation"
- Resolving bug → save as type: "error"

When closing SDD:
- `funemon_memory_reflect(session_id)`

## Triggers
- "spec", "SDD", "specification", "spec"
- "plan" followed by new feature
- "define" + "feature" / "requirement"
