# Skill: Security Review

## Descripción

Skill para realizar revisiones de seguridad de código y encontrar vulnerabilidades.

## Triggers

- "security review"
- "revisión seguridad"
- "vulnerability"
- "vulnerabilidad"
- "owasp"
- "audit"

## Checklist de Seguridad

### Autenticación
- [ ] Contraseñas hasheadas (bcrypt, argon2)
- [ ] No almacenar passwords en plaintext
- [ ] Tokens con expiration
- [ ] Rate limiting en login
- [ ] 2FA disponible

### Autorización
- [ ] RBAC implementado
- [ ] Verificar permisos en cada request
- [ ] No confiar en cliente para permisos
- [ ] Principio de mínimo privilegio

### Input Validation
- [ ] Sanitizar todo input
- [ ] Validar tipos y rangos
- [ ] Usar prepared statements (SQL)
- [ ] Output encoding

### Datos Sensibles
- [ ] No exponer secrets en logs
- [ ] HTTPS everywhere
- [ ] Headers de seguridad
- [ ] Cookies HttpOnly, Secure
- [ ] No exponer IDs internos

## Vulnerabilidades Comunes

### SQL Injection
```rust
// ❌ Peligroso
let query = format!("SELECT * FROM users WHERE id = {}", user_id);

// ✅ Seguro
let query = "SELECT * FROM users WHERE id = $1";
sqlx::query(&query).bind(user_id).fetch_all(&pool).await?;
```

### XSS
```typescript
// ❌ Peligroso
<div>{userInput}</div>

// ✅ Seguro
<div>{sanitize(userInput)}</div>
```

### CSRF
```rust
// ✅ Verificar CSRF token
if !csrf_token.validate(&request) {
    return Err(Error::Unauthorized);
}
```

### Command Injection
```rust
// ❌ Peligroso
std::process::Command::new("sh").arg("-c").arg(user_input);

// ✅ Permitir solo valores específicos
match user_input.as_str() {
    "status" => run_status(),
    "logs" => run_logs(),
    _ => return Err(Error::InvalidCommand),
}
```

## Tipos de Revisión

### Static Analysis
- Revisar código sin ejecutar
- Buscar patterns conocidos
- Tools: clippy, semgrep, bandita

### Dynamic Analysis
- Testing en runtime
- Fuzz testing
- Pen testing manual

### Dependency Check
- Verificar vulnerabilidades en dependencias
- tools: npm audit, cargo audit, snyk

## Reporte de Seguridad

```markdown
## Security Report #012

**Proyecto**: auth-service
**Fecha**: 2026-04-09
**Auditor**: Security Agent
**Severity**: High

### Finding 1: SQL Injection en /users/:id

**Descripción**:
El endpoint usa string interpolation para construir queries SQL.

**Código vulnerable**:
```rust
let query = format!("SELECT * FROM users WHERE id = {}", id);
```

**Impacto**:
Un atacante puede ejecutar SQL arbitrario.

**Recomendación**:
Usar parameterized queries:

**Fix aplicado**:
```rust
let query = "SELECT * FROM users WHERE id = $1";
sqlx::query(&query).bind(&id).fetch_one(&pool).await?;
```

**Severity**: Critical (CVSS 9.8)
**Status**: Fixed
```

## Output

- Reporte de hallazgos
- CVSS score por vulnerabilidad
- Recomendaciones de fix
- Estado de remediación