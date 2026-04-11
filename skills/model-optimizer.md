# Skill: model-optimizer

## What am I?

I am the LLM cost optimization skill. **I am ALWAYS active**, monitoring model usage and automatically switching to minimize costs.

## My Responsibility

Intelligently manage language model usage:

- **Prioritize FREE models by default**
- **Switch to paid models** only when absolutely necessary
- **Monitor costs** per agent and session
- **Switch automatically** if there is excessive spending

## Model Hierarchy

### Level 1: FREE (USE BY DEFAULT)
```yaml
free:
  - bigpickle             # Fast, available via opencode-go
  - ollama/codellama      # Specialized in code
  - ollama/mistral        # Good speed/quality balance
```

**When to use them:**
- ✅ General conversation
- ✅ File reading
- ✅ Simple analysis
- ✅ Basic documentation
- ✅ Routine tasks
- ✅ Commits and git operations

### Level 2: ECONOMICAL (USE WITH MODERATION)
```yaml
economical:
  - openai/gpt-3.5-turbo  # $0.0015/1K tokens
  - anthropic/claude-haiku # Fast and cheap
```

**When to use them:**
- ✅ Complex code analysis
- ✅ Moderate refactoring
- ✅ Simple debugging
- ✅ Testing assistance

**Rule:** Use for a maximum of **5 minutes** continuously, then switch back to free.

### Level 3: PREMIUM (USE ONLY IF CRITICAL)
```yaml
premium:
  - glm-5                  # High performance, moderate cost
  - openai/gpt-4           # Maximum quality, high cost
  - anthropic/claude-sonnet # Cost/quality balance
```

**When to use them:**
- ⚠️ Complex architecture from scratch
- ⚠️ Massive refactoring (>500 lines)
- ⚠️ Critical security review
- ⚠️ Complete system design
- ⚠️ Complex bug in production

**Rule:** Use for a maximum of **10 minutes**, then switch back to economical or free.

### Level 4: ULTRA-PREMIUM (EMERGENCIES ONLY)
```yaml
ultra-premium:
  - openai/gpt-4-turbo     # Maximum capacity, high cost
  - anthropic/claude-opus  # Top tier, very expensive
```

**When to use them:**
- 🚨 ONLY with EXPLICIT user approval
- 🚨 Critical production situation
- 🚨 Legacy architecture migration

**Rule:** Maximum **5 minutes** and only with prior confirmation.

## Detecting When to Switch

### Signals to LEVEL UP

**Free → Economical:**
```python
if any([
    "no entiendo" in response,
    "contexto muy largo" in response,
    "código muy complejo" in task,
    tokens_used > 4000,
    retry_count > 2
]):
    switch_to_economical()
```

**Economical → Premium:**
```python
if any([
    "arquitectura desde cero" in task,
    "refactoring masivo" in task,
    "security critical" in task,
    "bug en producción" in task,
    complexity_score > 8/10
]):
    switch_to_premium()
```

**Premium → Ultra-Premium:**
```python
if any([
    "emergencia crítica" in task,
    "sistema caído" in task,
    user_confirmed == True,
    priority == "critical"
]):
    ask_user_permission()  # NEVER automatic
```

### Signals to LEVEL DOWN

**Premium → Economical:**
```python
if any([
    time_on_premium > 10_minutes,
    task_completed == True,
    "cambiar a modelo gratis" in memory,
    cost_accumulated > threshold
]):
    switch_to_economical()
```

**Economical → Free:**
```python
if any([
    time_on_economical > 5_minutes,
    task_completed == True,
    "solo lectura" in current_task,
    "análisis simple" in current_task
]):
    switch_to_free()
```

## Per-Agent Cost Monitoring

Each agent has a **budget proportional to their task**:

| Agent | Base Budget | Premium Limit | Justification |
|-------|-------------|---------------|---------------|
| Magnus (Backend) | $0.10/session | $0.50 | Critical code, may need premium |
| Aurora (Frontend) | $0.05/session | $0.30 | Less critical UI, economical sufficient |
| Bruno (Tester) | $0.03/session | $0.20 | Testing with free is usually enough |
| Almendra (Docs) | $0.02/session | $0.10 | Simple documentation, use free |
| Gabriela (Security) | $0.15/session | $0.80 | Critical security review |
| Tyrion (PM) | $0.02/session | $0.15 | Coordination, free sufficient |

### Overspending Detection Algorithm

```python
def check_agent_overspending(agent, current_cost):
    limit = budget_limits[agent]
    
    if current_cost > limit["premium"]:
        print(f"⚠️ {agent} is spending ${current_cost}")
        print(f"   Budget: ${limit['base']}")
        print(f"   Premium limit: ${limit['premium']}")
        
        # AUTOMATICALLY SWITCH TO FREE
        switch_agent_to_free(agent)
        
        # Save to memory
        funemon_memory_store(
            type="error",
            title="Agent overspending detected",
            what=f"{agent} exceeded budget: ${current_cost}",
            learned=f"Automatically switched to free model"
        )
        
        # Notify user
        notify_user(
            f"⚠️ Switched {agent} to free model due to excessive spending (${current_cost})"
        )
```

## Automatic Switching Rules

### Forbidden (NEVER do without permission)
- **NEVER** switch to ultra-premium without user confirmation
- **NEVER** stay on premium > 10 minutes without review
- **NEVER** ignore overspending signals
- **NEVER** use premium for simple tasks

### Required (ALWAYS do)
- **ALWAYS** start with free model
- **ALWAYS** monitor time at each level
- **ALWAYS** level down when task simplifies
- **ALWAYS** save model changes to memory
- **ALWAYS** notify user of level changes > economical

## Decision Workflow

```
New task
    ↓
Evaluate complexity (1-10)
    ↓
Complexity < 4?
    ├─ YES → Use FREE
    └─ NO → Complexity < 7?
        ├─ YES → Use ECONOMICAL
        └─ NO → Complexity >= 7?
            ├─ YES → Is it critical?
            │   ├─ YES → Ask permission for PREMIUM
            │   └─ NO → Use ECONOMICAL with monitoring
            └─ ERROR → Re-evaluate
```

## Memory Integration

Each model change is saved to funemon:

```yaml
funemon_memory_store(
  type: "plan",
  title: "Model switch",
  what: "Switched from bigpickle to glm-5",
  why: "Complex architecture requires more capacity",
  where: "agent/magnus"
)
```

## Success Metrics

The skill is successful when:
- ✅ > 80% of time on free models
- ✅ < 5% of time on ultra-premium
- ✅ Total cost < $1/project/day
- ✅ Zero overspend without detection
- ✅ Automatic switches working

## Triggers
- ALWAYS active (no specific trigger needed)
- Activates at start of each session
- Re-evaluated on each important task
- Continuously monitors during session

## User Output

When switching models, I report:

```markdown
## Optimized Model

### Change detected
- Previous model: bigpickle
- New model: glm-5
- Reason: Complex architecture (complexity: 8/10)

### Estimated cost
- Estimated time: 8 minutes
- Estimated cost: $0.15
- Remaining budget: $0.85

### Actions taken
- ✅ Automatically switched for this task
- ✅ Monitoring usage
- ⏱️ Will return to free in 8 minutes or when complete
```

## Usage Examples

### Example 1: Complex Backend
```
Task: "Refactor auth system"
Complexity: 7/10
Decision: Use glm-5 for 10 minutes
Result: ✅ Task completed, $0.12 spent
Switch: → bigpickle (free)
```

### Example 2: Simple Docs
```
Task: "Update README"
Complexity: 2/10
Decision: Use bigpickle (free)
Result: ✅ Task completed, $0.00 spent
Model: No changes
```

### Example 3: Limit Exceeded
```
Agent: Magnus
Budget: $0.10
Spent: $0.18
Action: ⚠️ OVERSPEND DETECTED
Switch: Automatic to bigpickle
Notification: User informed
Memory: Saved as error
```
