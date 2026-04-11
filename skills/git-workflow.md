---
name: git-workflow
description: Enforces correct Git practices - branches, small commits, PRs, and waiting for approval
---

# Git Workflow - Branch, Commit, PR, Wait

> *"Never push to main. Always create a branch. Small commits. Wait for approval."*

## What Am I?

I am the Git Workflow skill. I enforce CORRECT Git practices: branches, small commits, PRs, and waiting for approval.

## Iron Rules

1. **NEVER push to main directly**
2. **ALWAYS create a branch FIRST**
3. **ONE commit = ONE logical change**
4. **ALWAYS create PR after push**
5. **ONLY Santi (user) merges**

## Git Workflow

### Step 1: Create Branch

```bash
# Choose branch type
feat/     -> New feature
fix/      -> Bug fix
docs/     -> Documentation
refactor/ -> Code refactoring
test/     -> Tests only

# Create branch
git checkout -b <type>/<short-description>

# Examples
git checkout -b feat/user-authentication
git checkout -b fix/login-crash
git checkout -b docs/api-reference
git checkout -b refactor/auth-module
git checkout -b test/auth-tests
```

| Branch Type | Prefix | Example |
|-------------|--------|---------|
| Feature | feat/ | feat/user-auth |
| Fix | fix/ | fix/login-bug |
| Docs | docs/ | docs/api-reference |
| Refactor | refactor/ | refactor/auth-module |
| Test | test/ | test/auth-tests |

Save to memory:
```yaml
funemon_memory_store(
  type: "observation",
  title: "Git: Branch created",
  what: "Created branch {branch_name}",
  why: "Following git-workflow skill"
)
```

### Step 2: Work and Commit

```bash
# Work on your changes...

# Add ONE logical change
git add <file>

# Commit with descriptive message
git commit -m "<type>: <description>"

# Conventional commits format:
# feat: new feature
# fix: bug fix
# docs: documentation
# refactor: code refactoring
# test: adding tests

# Examples
git add src/auth/login.rs
git commit -m "feat: add JWT token generation"

git add src/auth/middleware.rs
git commit -m "feat: add authentication middleware"
```

## Small Commits Rule

```yaml
One Logical Change = One Commit

Examples:
  ✅ GOOD:
    git add src/auth/login.rs
    git commit -m "feat: add JWT validation"
    git add src/auth/middleware.rs
    git commit -m "feat: add auth middleware"
  
  ❌ BAD:
    git add .
    git commit -m "feat: add auth and fix bugs and update docs"
```

### Step 3: Push Branch

```bash
# Push to remote
git push -u origin <type>/<description>

# Example
git push -u origin feat/user-authentication
```

### Step 4: Create Pull Request

```bash
# Create PR with description
gh pr create --title "<type>: <description>" --body "$(cat <<'EOF'
## Summary

<List of changes>

## Changes

- <Change 1>
- <Change 2>

## Testing

- <How to test>

## Checklist

- [ ] Tests pass
- [ ] Documentation updated
- [ ] Ready for review
EOF
)"

# Example
gh pr create --title "feat: user authentication" --body "$(cat <<'EOF'
## Summary

Implements JWT-based user authentication.

## Changes

- Add JWT token generation
- Add authentication middleware
- Add login endpoint

## Testing

- Run: cargo test auth
- Test login endpoint: POST /api/auth/login

## Checklist

- [x] Tests pass
- [x] Documentation updated
- [x] Ready for review
EOF
)"
```

Save to memory:
```yaml
funemon_memory_store(
  type: "observation",
  title: "Git: PR created",
  what: "PR #{number} created",
  why: "Waiting Santi approval"
)
```

### Step 5: Wait for Approval

```yaml
CRITICAL:
  - ONLY Santi (user) can merge
  - NEVER merge your own PR
  - Wait for Santi's approval
  - PR URL: https://github.com/{repo}/pull/{number}
```

### Step 6: After Approval

```bash
# Santi merges the PR
# Your work is done!

# Start fresh for next task
git checkout main
git pull
git checkout -b <new-branch>
```

## What I Deliver

- Branch created: `git checkout -b <type>/<description>`
- Small commits: One commit per logical change
- PR created: `gh pr create`
- Memory saved: Branch and PR tracked

## Integration with Other Skills

- **tdd-workflow**: After tests pass, run git-workflow
- **sdd**: In IMPLEMENT phase, use git-workflow
- **autonomous**: Loads git-workflow automatically

## Triggers

- After completing any work
- "git", "branch", "commit", "push", "PR", "pull request"
- "merge" (trigger warning: only Santi merges)

## Anti-Patterns

```bash
# ❌ NEVER do this
git push origin main

# ❌ NEVER do this
git commit -m "fix stuff"

# ❌ NEVER do this
git push --force

# ❌ NEVER do this
git reset --hard

# ❌ NEVER do this (merge your own PR)
gh pr merge
```

## Memory Tracking

```yaml
# When creating branch
funemon_memory_store(
  type: "observation",
  title: "Git: Branch created",
  what: "Created branch {branch_name} for {feature}",
  why: "Following git-workflow skill"
)

# When creating PR
funemon_memory_store(
  type: "observation",
  title: "Git: PR created",
  what: "PR #{number} created for {feature}",
  why: "Waiting Santi approval"
)
```

## Acceptance Criteria

For every task:

- [ ] Branch created from main
- [ ] Small commits (one per logical change)
- [ ] Conventional commit format used
- [ ] PR created with description
- [ ] Waiting for user approval
- [ ] Memory updated with branch and PR info

---

**Remember: Never push to main. Always branch first. Small commits. Create PR. Wait for approval.**