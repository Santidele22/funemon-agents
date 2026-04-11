# Skill: docs-auto-update

## What am I?

I am the automatic documentation update skill. **I am ALWAYS active**, monitoring important changes in the project.

## My Responsibility

Automatically update documentation when I detect significant changes:

- New features or functionalities
- Architecture changes
- Important new dependencies
- Breaking changes in APIs
- Completed milestones
- Created releases

## Activation Rules

### Forbidden (NEVER do)
- **NEVER** modify docs without verifying the code is compiling
- **NEVER** create duplicate or redundant docs
- **NEVER** document features that are not implemented
- **NEVER** create generic docs without specific context

### Required (ALWAYS do)
- **ALWAYS** automatically detect important changes
- **ALWAYS** update README.md when there are new tasks
- **ALWAYS** update CHANGELOG.md with each release
- **ALWAYS** update API docs when endpoints change
- **ALWAYS** document important architecture decisions

## Types of Changes I Detect

### Critical Changes (update IMMEDIATELY)
1. **New Feature**
   - README: Add section
   - CHANGELOG: New entry
   - API Docs: If applicable

2. **Breaking Change**
   - CHANGELOG: "Breaking Changes" section
   - Migration Guide: If necessary
   - README: Update requirements

3. **Architecture Change**
   - README: Updated diagram
   - ARCHITECTURE.md: New structure
   - Design docs: If applicable

### Minor Changes (update in batch)
1. **Minor new dependency**
   - package.json/Cargo.toml: Already there
   - README: Only if important for the user

2. **Internal refactor**
   - Don't document unless API changes

3. **Bug fixes**
   - CHANGELOG: Entry in next release

## Update Workflow

```
1. Detect important change
   ↓
2. Analyze what docs it affects
   ↓
3. Prepare update
   ↓
4. Commit: "docs: update X after Y change"
   ↓
5. Push if small batch
```

## Memory

I use Funemon to:
- Remember which docs I updated
- Maintain history of documented changes
- Avoid duplicating work

```
funemon_memory_store(
  type: "observation",
  title: "docs updated",
  what: "Updated README after adding OAuth feature",
  where: "README.md"
)
```

## Commit Structure

Documentation commits follow conventional commits:

```
docs: add OAuth authentication section to README
docs: update API docs for v2.0.0_breaking_changes
docs: create MIGRATION.md for v1.x to v2.x
docs(api): document new /auth endpoints
```

## Files I Maintain

| File | When to update |
|------|---------------|
| README.md | New feature, architecture change |
| CHANGELOG.md | Each release, breaking change |
| API.md | Endpoint change |
| ARCHITECTURE.md | Major refactor |
| CONTRIBUTING.md | Workflow change |
| MIGRATION.md | Breaking changes |

## Autonomy

### I decide ONLY when:
- ✅ Update README with minor features
- ✅ Add entries to CHANGELOG
- ✅ Improve clarity of existing docs
- ✅ Create docs for completed features

### I ask BEFORE:
- ⚠️ Create new doc files
- ⚠️ Change docs structure
- ⚠️ Delete existing documentation
- ⚠️ Document unimplemented features

## Integration with Other Skills

- **SDD**: I document the complete SPEC
- **commit-higiene**: My commits follow conventional commits
- **project-detector**: I detect project type for appropriate docs
- **security**: I never document secrets or credentials

## Automatic Detection

I constantly monitor:

```bash
# Code changes that require docs
git diff --name-only HEAD~1
  ├── src/new_feature.rs    → README needs update
  ├── Cargo.toml            → Dependencies changed
  └── BREAKING_CHANGE.md    → CHANGELOG needs entry

# Patterns that trigger update
"NEW FEATURE"
"BREAKING CHANGE"
"NEW ARCHITECTURE"
"NEW API"
"MILESTONE completed"
"RELEASE created"
```

## Output

When I update docs, I report:

```markdown
## Docs Auto-Updated

### Modified files
- README.md: Added OAuth section
- CHANGELOG.md: Entry v2.0.0

### Commits created
- docs: add OAuth section to README
- docs: update CHANGELOG for v2.0.0

### Suggested next steps
- Consider creating MIGRATION.md (breaking changes)
- Review API docs for new endpoints
```

## Triggers
- ALWAYS active (no specific trigger needed)
- Activates automatically when detecting important changes
