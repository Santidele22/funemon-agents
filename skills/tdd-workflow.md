---
name: tdd-workflow
description: Test-Driven Development workflow obligatorio
---

# TDD Workflow - Test-Driven Development

> *"Red-Green-Refactor. Every feature starts with a test."*

## ¿Por qué TDD?

TDD garantiza que:
- El código hace lo que se espera
- Los tests documentan el comportamiento
- Refactoring es seguro
- Cobertura es alta (>80%)

## The TDD Cycle

### Phase 1: RED

```typescript
// ❌ FAILING TEST - Define expected behavior
describe('UserService', () => {
  it('should create user with valid email', () => {
    const service = new UserService();
    const user = service.createUser('john@example.com');
    
    expect(user).toBeDefined();
    expect(user.email).toBe('john@example.com');
    expect(user.id).toBeDefined();
  });
});

// This test FAILS because createUser doesn't exist yet
// Run: npm test → RED (test fails)
```

### Phase 2: GREEN

```typescript
// ✅ MINIMAL CODE - Just enough to pass
class UserService {
  createUser(email: string): User {
    return {
      id: generateId(),
      email: email
    };
  }
}

// Run: npm test → GREEN (test passes)
// Don't optimize yet!
```

### Phase 3: REFACTOR

```typescript
// ♻️ REFACTOR - Improve design while keeping tests green
class UserService {
  private users: Map<string, User> = new Map();
  
  createUser(email: string): User {
    this.validateEmail(email);
    const user = {
      id: generateId(),
      email: email,
      createdAt: new Date()
    };
    this.users.set(user.id, user);
    return user;
  }
  
  private validateEmail(email: string): void {
    if (!email.includes('@')) {
      throw new Error('Invalid email');
    }
  }
}

// Run: npm test → Still GREEN
// Refactoring is safe because tests catch regressions
```

## TDD Workflow per Agent

### For Magnus (Backend)

```yaml
Before writing code:
  1. Write integration test first
  2. Write unit tests for components
  3. Run tests: Should see RED
  
During implementation:
  1. Write MINIMAL code to pass
  2. Don't optimize or over-engineer
  3. Run tests: Should see GREEN
  
After implementation:
  1. Refactor for better design
  2. Extract methods, reduce duplication
  3. Run tests: Should stay GREEN
```

### For Aurora (Frontend)

```yaml
Before writing code:
  1. Write component test first
  2. Define user interactions
  3. Run tests: Should see RED
  
During implementation:
  1. Write component with MINIMAL logic
  2. Don't add features not needed by tests
  3. Run tests: Should see GREEN
  
After implementation:
  1. Refactor CSS, extract components
  2. Improve accessibility
  3. Run tests: Should stay GREEN
```

### For Bruno (QA)

```yaml
TDD for QA:
  1. Review test coverage
  2. Suggest edge cases to test
  3. Write E2E tests for critical flows
  4. Verify tests are deterministic
```

## Commands

```bash
# Run tests
npm test

# Run tests in watch mode (TDD)
npm test -- --watch

# Run specific test
npm test -- UserService.test

# Check coverage
npm test -- --coverage
```

## Anti-Patterns

### ❌ Don't:

```typescript
// Don't write test after code
class UserService { ... }
// ❌ Now writing test (TOO LATE)

// Don't skip RED phase
it('should work', () => {
  // ❌ This test passes because code already exists
});

// Don't write big tests
it('should do everything', () => {
  // ❌ Test is too large
  // Hard to debug when it fails
});
```

### ✅ Do:

```typescript
// Write test first
it('should create user', () => {
  // ✅ Test defines behavior
  // Run test → RED
});

// Then write code
class UserService { ... }
// ✅ Run test → GREEN

// Then refactor
class UserService {
  // ✅ Improved design
  // Run test → Still GREEN
});
```

## Acceptance Criteria

For every PR:

- [ ] Tests written BEFORE code
- [ ] All tests pass
- [ ] Coverage > 80%
- [ ] No commented-out tests
- [ ] Tests are readable
- [ ] Tests are fast (< 5s)

## Examples by Language

### Rust

```rust
// Phase 1: RED
#[cfg(test)]
mod tests {
  use super::*;
  
  #[test]
  fn it_creates_user_with_email() {
    let service = UserService::new();
    let user = service.create_user("john@example.com");
    
    assert!(user.is_ok());
    assert_eq!(user.unwrap().email, "john@example.com");
  }
}

// cargo test → RED

// Phase 2: GREEN
pub struct UserService {
  users: Vec<User>,
}

impl UserService {
  pub fn new() -> Self {
    Self { users: Vec::new() }
  }
  
  pub fn create_user(&self, email: &str) -> Result<User, Error> {
    Ok(User {
      id: generate_id(),
      email: email.to_string(),
    })
  }
}

// cargo test → GREEN

// Phase 3: REFACTOR
// (Improve implementation while keeping tests green)
```

### Python

```python
# Phase 1: RED
def test_create_user():
    service = UserService()
    user = service.create_user("john@example.com")
    
    assert user is not None
    assert user.email == "john@example.com"
    assert user.id is not None

# pytest → RED

# Phase 2: GREEN
class UserService:
    def create_user(self, email):
        return User(
            id=generate_id(),
            email=email
        )

# pytest → GREEN

# Phase 3: REFACTOR
# (Improve implementation)
```

---

**Remember: Red-Green-Refactor. Every feature starts with a failing test.**