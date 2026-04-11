---
name: red-green-refactor
description: The TDD cycle explained
---

# Red-Green-Refactor - The TDD Cycle

> *"The rhythm of TDD: Red-Green-Refactor, repeat."*

## The Three Phases

### 🔴RED Phase

**Goal:** Write a failing test that defines expected behavior

```typescript
// What does RED mean?
// - Test FAILS
// - Code doesn't exist yet
// - Defines WHAT we want

describe('UserRepository', () => {
  it('should find user by id', () => {
    const repo = new UserRepository();
    const user = repo.findById('user-123');
    
    expect(user).toBeDefined();
    expect(user.id).toBe('user-123');
  });
});

// Run test → RED (fails)
// Why RED?
// - UserRepository doesn't exist
// - findById doesn't exist
// - This is EXPECTED and GOOD
```

**Key Points:**

```yaml
RED Phase:
  - Test defines behavior
  - Test expresses intent
  - Test FAILS (expected)
  - Don't write code yet
  - Focus on WHAT, not HOW
```

### 🟢 GREEN Phase

**Goal:** Write minimum code to make test pass

```typescript
// What does GREEN mean?
// - Test PASSES
// - Code exists and works
// - Code is MINIMAL (not perfect)

class UserRepository {
  private users: Map<string, User> = new Map();
  
  findById(id: string): User | undefined {
    return this.users.get(id);
  }
}

// Run test → GREEN (passes)
// Why GREEN?
// - findById exists
// - Returns correct result
// - Code is MINIMAL
```

**Key Points:**

```yaml
GREEN Phase:
  - Write MINIMUM code to pass
  - Don't optimize yet
  - Don't over-engineer
  - Hard-coded values OK
  - Ugly code OK
  - Tests PASS
```

### ♻️ REFACTOR Phase

**Goal:** Improve code design while keeping tests green

```typescript
// What does REFACTOR mean?
// - Improve design
// - Remove duplication
// - Better naming
// - Tests stay GREEN

class UserRepository {
  private database: Database;
  private cache: Cache;
  
  constructor(database: Database, cache: Cache) {
    this.database = database;
    this.cache = cache;
  }
  
  async findById(id: string): Promise<User | undefined> {
    // Check cache first
    const cached = this.cache.get(id);
    if (cached) {
      return cached;
    }
    
    // Query database
    const user = await this.database.query(
      'SELECT * FROM users WHERE id = ?',
      [id]
    );
    
    // Cache result
    if (user) {
      this.cache.set(id, user);
    }
    
    return user;
  }
}

// Run test → Still GREEN
// Why refactor?
// - Better design
// - Performance improved
// - Tests still pass
```

**Key Points:**

```yaml
REFACTOR Phase:
  - Improve code quality
  - Extract methods
  - Reduce duplication
  - Better naming
  - Add abstractions
  - Tests stay GREEN
  - Small steps
  - Run tests frequently
```

## The Cycle

```
    ┌──────────────────────┐
    │                      │
    │   🔴 RED             │
    │   Write Failing Test │
    │                      │
    └──────────┬───────────┘
               │
               │ npm test
               │ (fails)
               │
    ┌──────────▼───────────┐
    │                      │
    │   🟢 GREEN           │
    │   Write Minimal Code │
    │                      │
    └──────────┬───────────┘
               │
               │ npm test
               │ (passes)
               │
    ┌──────────▼───────────┐
    │                      │
    │   ♻️ REFACTOR        │
    │   Improve Design     │
    │                      │
    └──────────┬───────────┘
               │
               │ npm test
               │ (still passes)
               │
               └─────► Repeat
```

## Example: Complete TDD Cycle

### Iteration 1

```typescript
// 🔴 RED
it('should add two numbers', () => {
  const calc = new Calculator();
  expect(calc.add(2, 3)).toBe(5);
});

// Run test → RED (Calculator doesn't exist)

// 🟢 GREEN
class Calculator {
  add(a: number, b: number): number {
    return 5; // Hard-coded! But test passes
  }
}

// Run test → GREEN

// ♻️ REFACTOR
class Calculator {
  add(a: number, b: number): number {
    return a + b; // Actually correct
  }
}

// Run test → Still GREEN
```

### Iteration 2

```typescript
// 🔴 RED
it('should subtract two numbers', () => {
  const calc = new Calculator();
  expect(calc.subtract(5, 3)).toBe(2);
});

// Run test → RED (subtract doesn't exist)

// 🟢 GREEN
class Calculator {
  add(a: number, b: number): number {
    return a + b;
  }
  
  subtract(a: number, b: number): number {
    return 2; // Hard-coded! But test passes
  }
}

// Run test → GREEN

// ♻️ REFACTOR
class Calculator {
  add(a: number, b: number): number {
    return a + b;
  }
  
  subtract(a: number, b: number): number {
    return a - b; // Actually correct
  }
}

// Run test → Still GREEN
```

## Tips

### RED Phase Tips

```markdown
1. Test name describes behavior
   ✓ it('should create user with valid email')
   ✗ it('works')

2. One concept per test
   ✓ it('should validate email format')
   ✗ it('should validate email and create user')

3. Test what matters
   ✓ Test behavior, not implementation

4. Edge cases are important
   ✓ Test happy path AND error cases
```

### GREEN Phase Tips

```markdown
1. Write minimum code
   ✓ return 5 (if test expects 5)
   ✗ Write complex algorithm (not needed yet)

2. Hard-coded is OK
   ✓ return "john" (if test expects "john")
   ✗ Implement full logic

3. Tests must pass
   ✓ All tests green
   ✗ Skip failing tests

4. Don't optimize
   ✓ Simple implementation
   ✗ Premature optimization
```

### REFACTOR Phase Tips

```markdown
1. Small steps
   ✓ Extract one method
   ✗ Rewrite everything

2. Run tests frequently
   ✓ Every small change
   ✗ Big changes at once

3. Keep tests green
   ✓ Tests always pass
   ✗ Break tests

4. No behavior changes
   ✓ Improve design
   ✗ Change what code does
```

---

**Remember: Red (failing test) → Green (minimal code) → Refactor (better design) → Repeat**