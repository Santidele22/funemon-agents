# Reflection Skill

**Activation**: Automatic at the end of a work session, or manual when requested by the user.

**Description**: Generates a structured reflection about the work done in the session and stores it in memory.

## When to Use

- At the end of a work session (automatic)
- When the user requests a session summary
- After completing a complex task
- When there's an important error to document

## Flow

1. **Get context from current session**
   ```
   memory_context(session_id, limit=10)
   ```

2. **Analyze memories**
   - Memory types: error, plan, observation, preference
   - Identified patterns
   - Problems solved
   - Decisions made

3. **Generate structured reflection in JSON**
   ```json
   {
     "content": "Clear and concise description of what was learned",
     "type": "pattern | principle | warning",
     "importance": 0.0-1.0,
     "level": "Fact | Pattern | Principle",
     "source_summary": "Summary of source memories"
   }
   ```

4. **Store the reflection**
   ```
   memory_store_reflection(
     session_id="...",
     content="{...json...}",
     agent_name="tyrion"
   )
   ```

## Reflection Types

- **pattern**: Pattern identified in behavior or code
- **principle**: Principle or rule derived
- **warning**: Warning or risk identified

## Reflection Levels

- **Fact**: Fact observed in this specific session
- **Pattern**: Recurring pattern across multiple sessions
- **Principle**: Principle applicable at system level

## Importance

- **0.0 - 0.3**: Low importance
- **0.31 - 0.6**: Medium importance
- **0.61 - 0.8**: High importance
- **0.81 - 1.0**: Critical

## Examples

### Example 1: Principle about architecture

**Context**: Discovered that funemon was hardcoded to Ollama.

**Generated reflection**:
```json
{
  "content": "Reflections should be handled as external skills, not as LLM calls from funemon. Agents use opencode-go's LLM and only store results in funemon.",
  "type": "principle",
  "importance": 0.85,
  "level": "Principle",
  "source_summary": "Removed llm_client.rs and reimplemented store_reflection()"
}
```

### Example 2: Pattern about implementation

**Context**: Implemented agent_name system.

**Generated reflection**:
```json
{
  "content": "When adding fields to existing SQLite tables, use ALTER TABLE with DEFAULT and NOT NULL to avoid manual migrations. Automatic migration allows backward compatibility.",
  "type": "pattern",
  "importance": 0.70,
  "level": "Pattern",
  "source_summary": "Added agent_name with DEFAULT 'tyrion' and automatic migration"
}
```

### Example 3: Warning about limits

**Context**: glm-5:cloud had weekly usage limit.

**Generated reflection**:
```json
{
  "content": "Ollama cloud models have weekly limits. Verify availability before using in production.",
  "type": "warning",
  "importance": 0.75,
  "level": "Pattern",
  "source_summary": "glm-5:cloud and deepseek-v3.2:cloud reached weekly usage limits"
}
```

## Notes

- If the agent has a name (magnus, aurora, bruno, almendra, gabriela), use that name in `agent_name`
- If the agent is anonymous, use "tyrion" as default
- The reflection should be concise but complete (2-4 sentences)
- Always validate that `content` is not empty
- Always generate valid JSON for the `content` field
- **IMPORTANT**: The system now accepts plain text (Markdown) if JSON parsing fails - it will automatically wrap as a warning-type insight for backward compatibility