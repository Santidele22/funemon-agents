# Skill: QA - Quality Assurance

## Descripción

Skill para realizar testing exhaustivo y asegurar la calidad del software.

## Triggers

- "qa"
- "quality assurance"
- "testing"
- "verificación"
- "validation"

## Proceso QA

### 1. Revisión de Requisitos
- Entender qué debe hacer el feature
- Identificar criterios de aceptación
- Verificar que son medibles

### 2. Plan de Testing
- Listar casos de prueba
- Priorizar por riesgo
- Asignar recursos

### 3. Ejecución
- Ejecutar casos de prueba
- Registrar resultados
- Documentar desviaciones

### 4. Reporting
- Resumen de testing
- Bugs encontrados
- Recomendaciones

## Tipos de Prueba

### Funcionales
- Positive: Lo que debe funcionar
- Negative: Casos de error
- Boundary: Límites

### No Funcionales
- Performance: Velocidad, carga
- Security: Seguridad
- Usability: Usabilidad
- Compatibility: Compatibilidad

## Casos de Prueba

```markdown
## CP-001: Login con credenciales válidas

**Precondición**: Usuario registrado en el sistema

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Ingresar email válido | Campo acepta email |
| 2 | Ingresar contraseña válida | Campo acepta contraseña |
| 3 | Click en "Ingrrar" | Redirige a dashboard |
| 4 | Verificar nombre de usuario | Muestra nombre正确 |

**Resultado**: ✅ PASS / ❌ FAIL
```

## Matriz de Testing

| Feature | Unit | Integration | E2E | Status |
|---------|------|-------------|-----|--------|
| Login | ✅ | ✅ | ✅ | Pass |
| Register | ✅ | ✅ | ✅ | Pass |
| Logout | ✅ | ❌ | ✅ | Fail |
| Profile | ✅ | ✅ | ❌ | Pending |

## Bug Report

```markdown
## Bug Report #012

**Título**: El login falla con caracteres especiales en contraseña

**Severity**: High
**Priority**: P1
**Environment**: Chrome 122, Windows 11

**Descripción**:
Cuando el usuario ingresa caracteres especiales (ñ, á, ü) en la contraseña, el login falla sin mostrar mensaje de error.

**Steps to Reproduce**:
1. Ir a /login
2. Ingresar "contraseñañ" en campo contraseña
3. Click en "Ingrrar"
4. Verificar resultado

**Expected**: Redirigir a dashboard
**Actual**: Muestra pantalla en blanco

**Attachments**: screenshot.png, video.mp4
```

## Testing Checklist

- [ ] Todos los criterios de aceptación probados
- [ ] Casos de borde probados
- [ ] Datos inválidos probados
- [ ] Performance aceptable
- [ ] Compatible con browsers objetivo
- [ ] Accesible (A11y)
- [ ] Tests automatizados pasando
- [ ] Code review hecho

## Output

- Casos de prueba ejecutados
- Resultados documentados
- Bugs reportados
- Recomendaciones