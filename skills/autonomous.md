# Skill: autonomous

## What am I?

I am the complete autonomy workflow for work sessions. I am ALWAYS active at the start of each session.

## Workflow (MANDATORY)

### 1. Init (on start)
- Detect project (`project-detector`)
- Start memory session (`funemon_memory_session_start`)
- Load previous context (`funemon_memory_context`)

### 2. Analyze
- Understand the user's task
- Identify the required workflow (SDD, TDD, etc.)
- Load the appropriate skill

### 3. Execute
- Execute the task using the loaded skill
- Save important decisions (`funemon_memory_store`)
- Keep the user informed of progress

### 4. Reflect (on close)
- Generate structured reflection using your LLM
- Format as JSON with fields: content, type, importance, level, source_summary
- Store it: `funemon_memory_store_reflection(session_id, content_json, agent_name)`
- Summarize learnings
- Suggest next steps

## Rules

1. **NEVER ask permission** to use memory - just use it
2. **ALWAYS save** important decisions
3. **ALWAYS reflect** on close
4. **Maintain context** between sessions

## Triggers
- By default in every session (ALWAYS active)
