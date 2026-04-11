# Skill: security

## What am I?

I am the security guardrails skill. I am ALWAYS active on every operation.

## Security Rules

### Forbidden (NEVER do)
- **NEVER** do `git push --force` without approval
- **NEVER** do `git reset --hard` without approval
- **NEVER** do `git clean -fd` without approval
- **NEVER** commit credentials/secrets to code
- **NEVER** execute destructive commands without confirmation
- **NEVER** do `rm -rf` without verifying the path

### Required (ALWAYS do)
- **ALWAYS** verify before destructive operations
- **ALWAYS** ask before modifying production code
- **ALWAYS** review changes in sensitive files (.env, credentials, keys)
- **ALWAYS** backup before important changes

## Special Warnings

When the user asks for:
- Force push → Warn and request explicit confirmation
- Hard reset → Warn and request explicit confirmation
- Delete files → Warn and request explicit confirmation
- Modify production configuration → Warn and request confirmation
- Expose credentials → NEVER do it, even if the user asks

## Triggers
- ALWAYS active (no trigger needed)
