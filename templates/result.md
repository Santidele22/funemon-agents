# Template: Resultado

Plantilla para que un agente retorne el resultado de una tarea.

---

## Resultado de Tarea

**ID**: `[task_id]`
**De**: `[agente_origen]`
**Para**: `[agente_destino]`
**Fecha**: `[timestamp]`

---

## Status

```
[pending_approval | completed | error]
```

---

## Output

```markdown
## Qué se produjo

[Descripción del output producido por el agente]

## Archivos Creados/Modificados

- `src/file1.rs` - [descripción]
- `src/file2.ts` - [descripción]

## Tests

- ✅ Test 1: passing
- ✅ Test 2: passing

## Coverage

[Porcentaje de coverage si aplica]
```

---

## Logs

```markdown
## Notas del agente

[Notas relevantes durante la ejecución]

## Decisiones Tomadas

- [Decisión 1]: [rationale]
- [Decisión 2]: [rationale]

## Problemas Encontrados

- [Problema 1]: [descripción]
- [Problema 2]: [descripción]
```

---

## Next Actions

```markdown
## Sugerencias

- [ ] [Próximo paso 1]
- [ ] [Próximo paso 2]

## Otros Agentes a Involucrar

- **Agente X**: [Por qué debería participar]
- **Agente Y**: [Por qué debería participar]

## Dependencies

- [Dependencia 1] debe completarse primero
- [Dependencia 2] puede ejecutarse en paralelo
```

---

## Approval Request

```
[Si status es "pending_approval"]

Se requiere aprobación para:
- [ ] Ejecutar código en [entorno]
- [ ] Aplicar cambios en [sistema]
- [ ] [Otra acción que requiere aprobación]
```

---

## Error Info (si aplica)

```markdown
## Error

**Tipo**: [tipo de error]
**Mensaje**: [mensaje de error]

## Stack Trace

```
[stack trace si aplica]
```

## Posibles Causas

- [Causa 1]
- [Causa 2]

## Sugerencias de Fix

[Cómo resolver el error]
```