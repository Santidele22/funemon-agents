---
name: test-first
description: How to write tests before implementation
---

# Test First - Writing Tests Before Code

## Why Test First?

```yaml
Benefits:
  - Defines expected behavior
  - Documents intent
  - Catches edge cases early
  - Prevents over-engineering
  - Guarantees coverage
```

## Test-First Process

### Step 1: Understand Requirements

```markdown
❓ What should this code do?

Examples:
  - Create user with email
  - Validate email format
  - Store user in database
  - Return user ID
```

### Step 2: Write Test First

```typescript
// Focus on WHAT, not HOW
describe('UserService.createUser', () => {
  it('should create user with valid email', () => {
    const service = new UserService();
    const user = service.createUser('john@example.com');
    
    expect(user.email).toBe('john@example.com');
    expect(user.id).toBeDefined();
  });
  
  it('should throw error for invalid email', () => {
    const service = new UserService();
    
    expect(() => service.createUser('invalid'))
      .toThrow('Invalid email');
  });
});

// This test FAILS because UserService doesn't exist yet
```

### Step 3: Run Test (RED)

```bash
npm test

# Output:
# FAIL UserService.test.ts
# ✗ UserService is not defined
# 
# RED ✗ (Expected behavior)
```

### Step 4: Implement Minimum Code

```typescript
// Write JUST ENOUGH to pass
class UserService {
  createUser(email: string): User {
    if (!email.includes('@')) {
      throw new Error('Invalid email');
    }
    
    return {
      id: generateId(),
      email: email
    };
  }
}
```

### Step 5: Run Test (GREEN)

```bash
npm test

# Output:
# PASS UserService.test.ts
# ✓ should create user with valid email
# ✓ should throw error for invalid email
#
# GREEN ✓ (All tests pass)
```

## Test Quality Checklist

```markdown
For each test:
  [ ] Descriptive name (it should...)
  [ ] One assertion per test (or related group)
  [ ] Arrange-Act-Assert pattern
  [ ] Independent (no shared state)
  [ ] Deterministic (same result every time)
  [ ] Fast (< 1 second)
  [ ] Clear intent
```

## Common Mistakes

### ❌ Test After Code

```typescript
// ❌ WRONG: Write code first
class UserService { ... }

// ❌ Now try to write test
it('should work', () => {
  // Hard to know what to test
  // Tests what exists, not what's needed
});
```

### ✅ Test Before Code

```typescript
// ✅ RIGHT: Write test first
it('should create user', () => {
  // Defines WHAT is needed
  // Documents intent
});

// ✅ Then write code
class UserService { ... }
```

---

**Always write tests first. Define behavior before implementation.**