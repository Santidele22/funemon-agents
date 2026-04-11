# Skill: tdd

## ¿Qué soy?

Soy el skill de TDD (Test-Driven Development) con DELEGACIÓN OBLIGATORIA a Bruno. EXIJO que NADIE escriba código antesde que YO (Bruno) haya escrito los tests.

## Reglas de Hierro

1. **NADIE IMPLEMENTA sin TESTS de Bruno**
2. **SIEMPRE delegar a Bruno PRIMERO**
3. **SIEMPRE guardar delegación en memoria Funemon**
4. **ESPERAR resultado de Bruno antes de codificar**

## Las 5Fases del Workflow TDD

### Fase 1: DELEGAR(Obligatoria)

**ANTES de escribir CUALQUIER código:**

1. Magnus/Aurora recibe tarea
2. ANTES de implementar:
   - Crear Task para Bruno usando `/templates/task.md`
   - Task DEBE incluir:
     - Descripción del feature
     - Acceptance criteria específicos
     - Edge cases conocidos
     - Archivos/componentes afectados
3. Guardar delegación en memoria:
   ```yaml
   funemon_memory_store(
     type: "plan",
     title: "Delegation: {Magnus|Aurora} → Bruno",
     what: "Write tests for {feature}",
     where_field: "{component/file}",
     why: "TDD mandatory - tests before implementation"
   )
   ```
4. **ESPERAR** resultado de Bruno

### Fase 2: RECIBIR TESTS

Cuando Bruno entrega tests:
- Revisar archivo de tests
- Verificar coverage metrics
- Entender cada test case
- Preguntar si algo no está claro
- Confirmar que tests cubren acceptance criteria

### Fase 3: IMPLEMENTAR

Escribir código para pasar tests:
- Implementar feature mínimamente
- `npm test` o `cargo test` frecuentemente
- Si tests fallan → **CORREGIR CÓDIGO**, no tests
- Si tests pasan → Continuar

### Fase 4: ITERAR (Si Necesario)

Si edge cases faltantes:
- Delegar más tests a Bruno
- Guardar nueva delegación en memoria
- Esperar nuevos tests
- Implementar para pasar

### Fase 5: CONTINUAR

Cuando todos los tests pasan:
- Coverage > 80%
- Todos los edge cases cubiertos
- DELEGAR docs a Almendra (si es necesario)
- DELEGAR security a Gabriela (si es necesario)
- CREAR PR siguiendo skill `git-workflow`

## Template de Delegación

Cuando Magnus/Aurora delega a Bruno, DEBE usar este formato:

```markdown
## Task

**ID:** task-{número}
**From:**{Magnus|Aurora}
**To:** Bruno
**Timestamp:** {ISO timestamp}

### Description

Write tests for {feature description}.

### Context

- Component/File: {path}
- Feature: {feature name}
- Expected input: {input spec}
- Expected output: {output spec}

### Acceptance Criteria

- [ ] Unit tests for {specific logic}
- [ ] Integration tests for {component interaction}
- [ ] Edge case tests: {list edge cases}
- [ ] Coverage target: >80%

### Edge Cases Known

- {Edge case 1}: {expected behavior}
- {Edge case 2}: {expected behavior}
- {Edge case N}: {expected behavior}

### Resources

- Spec: {path to spec if exists}
- Design doc:{path to design doc if exists}
- Related files: {list}

---

**Bruno:** Ejecutar tests y reportar coverage metrics.
```

## Ejemplo Completo de Delegación

```markdown
## Task

**ID:** task-001
**From:** Magnus
**To:** Bruno
**Timestamp:** 2026-04-11T10:00:00Z

### Description

Write tests for user authentication API endpoint.

### Context

- Endpoint: POST /api/auth/login
- File: `/backend/src/routes/auth.ts`
- Expected input: `{email: string, password: string}`
- Expected output: `{token: string, user: {id, email, name}}`

### Acceptance Criteria

- [ ] Unit tests for password validation logic
- [ ] Unit tests for token generation
- [ ] Integration tests for POST /api/auth/login
- [ ] Edge case: invalid email format
- [ ] Edge case: wrong password
- [ ] Edge case: empty fields
- [ ] Edge case: user not found
- [ ] Coverage target: >85%

### Edge Cases Known

- Invalid email format: should return 400
- Wrong password: should return 401
- Empty fields: should return 400 with validation errors
- User not found: should return 401 (security: don't reveal existence)
- Database connection fails: should return 503

### Resources

- Spec: `/docs/api/auth-spec.md`
- Design: `/docs/design/auth-flow.md`

---

**Bruno: Write tests and report coverage.**
```

## Respuesta de Bruno(Ejemplo)

```markdown
## Result

**Task ID:** task-001
**From:** Bruno
**To:** Magnus
**Timestamp:** 2026-04-11T11:30:00Z

### Tests Created

- `/backend/tests/unit/auth/validation.test.ts`
  - Password validation tests: 8 tests
  - Email format validation tests: 5 tests
  
- `/backend/tests/unit/auth/token.test.ts`
  - Token generation tests: 6 tests
  - Token verification tests: 4 tests

- `/backend/tests/integration/auth/login.test.ts`
  - Happy path: 1 test
  - Invalid email: 3 tests
  - Wrong password: 2 tests
  - Empty fields: 4 tests
  - User not found: 2 tests
  - Database failures: 3 tests

### Coverage Metrics

- Lines: 87%
- Functions: 92%
- Branches: 81%
- Statements: 88%

### Notes

- All edge cases from spec covered
- Added 2 additional edge cases for concurrent logins
- Tests are deterministic (no flaky tests)
- Average test execution time: 2.3s

---

**Magnus:** Implement to pass these tests.
```

## Integración con OtherSkills

| Skill| Cuándo se usa | Relación con TDD |
|------|---------------|------------------|
| **autonomous** | Siempre activo | Carga tdd automáticamente |
| **sdd** | Spec-Driven | TDD se ejecuta en fase IMPLEMENT |
| **git-workflow** | Después de tests passing | Se ejecuta DESPUÉS de TDD |
| **security** | Si aplica | Bruno puede delegar security tests a Gabriela |
| **docs-auto-update** | Si aplica | Bruno puede delegar docs a Almendra |

## Flujo Visual

```
┌─────────────────────────────────────────────────────────────┐
│                     TDD WITH DELEGATION                     │
└─────────────────────────────────────────────────────────────┘

    Magnus/Aurora recibe task
                │
                ▼
    ┌───────────────────────────────────┐
    │  FASE 1: DELEGAR                   │
    │  - Crear Task para Bruno           │
    │  - Guardar en Funemon memory       │
    │  - ESPERAR resultado               │
    └───────────┬───────────────────────┘
                │
   (Bruno escribe tests)
                │
                ▼
    ┌───────────────────────────────────┐
    │  FASE 2: RECIBIR TESTS             │
    │  - Revisar archivos de test        │
    │  - Verificar coverage              │
    │  - Entender test cases             │
    └───────────┬───────────────────────┘
                │
                ▼
    ┌───────────────────────────────────┐
    │  FASE 3: IMPLEMENTAR               │
    │  - Escribir código mínimo          │
    │  - npm test / cargo test           │
    │  - Si fallan: fix código           │
    │  - Si pasan: continuar             │
    └───────────┬───────────────────────┘
                │
                ▼
    ┌───────────────────────────────────┐
    │  FASE 4: ITERAR(si necesario)      │
    │  - Edge cases faltantes?           │
    │  - Delegar más tests a Bruno       │
    │  - Guardar en memoria              │
    │  - ESPERAR nuevos tests            │
    └───────────┬───────────────────────┘
                │
                ▼
    ┌───────────────────────────────────┐
    │  FASE 5: CONTINUAR                 │
    │  - Todos tests passing             │
    │  - Coverage > 80%                  │
    │  - Delegar docs (Almendra)         │
    │  - Delegar security (Gabriela)     │
    │  - Crear PR (git-workflow)         │
    └───────────────────────────────────┘
```

## Anti-Patrones que EVITAR

### ❌ Implementar sin delegar

```typescript
// ❌ MAL: Magnus escribe código directamente
class UserService {createUser() { ... } }

// ❌ DESPUÉS trata de delegar tests
// Esto NO es TDD
```

### ✅ Delegar PRIMERO

```typescript
// ✅ BIEN: Magnus delega tests PRIMERO
// Magnus: "Bruno, necesito tests para UserService.createUser"

// Bruno escribe tests
describe('UserService.createUser', () => {
  it('should create user with valid email', () => {
    // Test definition
  });
});

// Magnus: Recibe tests
// Magnus: Implementa para pasar tests
class UserService {
  createUser() {
    // Implementation
  }
}
```

### ❌ Guardar delegación sin memoria

```yaml
# ❌ MAL: Delegar sin guardar en Funemon memory
# Magnus: "Bruno, tests for login feature"
# (No lo guardó, se pierde el contexto)
```

### ✅ Guardar SIEMPRE

```yaml
# ✅ BIEN: Delegar y guardar
funemon_memory_store(
  type: "plan",
  title: "Delegation: Magnus → Bruno",
  what: "Write tests for UserService.createUser",
  where_field: "/backend/src/services/UserService.ts",
  why: "TDD mandatory - tests before implementation"
)
```

## Comandos de Testing

### TypeScript/JavaScript

```bash
# Ejecutar tests
npm test

# Tests en modo watch (TDD)
npm test -- --watch

# Tests específicos
npm test -- UserService.test

# Coverage
npm test -- --coverage

# Verificar coverage > 80%
npm test -- --coverage --coverageThreshold='{"global":{"lines":80}}'
```

### Rust

```bash
# Ejecutar tests
cargo test

# Tests específicos
cargo test --test user_service

# Coverage con tarpaulin
cargo tarpaulin --out Html

# Verificar coverage
# Abrir tarpaulin-report.html
```

### Python

```bash
# Ejecutar tests
pytest

# Tests específicos
pytest tests/test_user_service.py

# Coverage
pytest --cov=src --cov-report=html

# Verificar coverage > 80%
pytest --cov=src --cov-fail-under=80
```

## Triggers

Este skill se activa cuando:

- "test", "TDD", "testing", "tests"
- "implement", "build", "create", "develop" (requiere TDD primero)
- "feature", "endpoint", "component", "service"
- "unit test", "integration test", "e2e test"
- Usuario pide implementar algo nuevo

## Responsabilidades por Agente

| Agente | Rol en TDD |
|--------|-----------|
| **Magnus** | Delega tests a Bruno, implementa después |
| **Aurora** | Delega tests a Bruno, implementa después |
| **Bruno** | RECIBE delegación, escribe tests, retorna coverage |
| **Almendra** | Delega después de tests passing (docs) |
| **Gabriela** | Delega después de tests passing (security) |
| **Tyrion** | Orquesta, no implementa, delega a especialistas |

## Memoria y Tracking

### Cuando Magnus/Aurora delega:

```yaml
funemon_memory_store(
  type: "plan",
  title: "Delegation: {agent} → Bruno",
  what: "Write tests for {feature}",
  where_field: "{component}",
  why: "TDD mandatory"
)
```

### Cuando Bruno completa tests:

```yaml
funemon_memory_store(
  type: "observation",
  title: "Tests completed for {feature}",
  what: "Created {X} tests with {Y}% coverage",
  where_field: "{test files}",
  learned: "Edge cases covered: {list}"
)
```

### Cuando tests fallan y se arreglan:

```yaml
funemon_memory_store(
  type: "error",
  title: "Test failure in {feature}",
  what: "Tests failed, required fix",
  where_field: "{component}",
  why: "Implementation didn't match test expectations",
  learned: "Fixed by {solution}"
)
```

## Checklist Final

Antes de pasar a la siguiente fase:

- [ ] Tests creados por Bruno
- [ ] Coverage report generado
- [ ] Coverage > 80%
- [ ] Todos los edge cases cubiertos
- [ ] Tests determinísticos (no flaky)
- [ ] Delegación guardada en memoria
- [ ] Resultado de Bruno recibido y revisado

---

**Recuerda: SIN TESTS DE BRUNO, NO HAY CÓDIGO. Esta es la regla.**