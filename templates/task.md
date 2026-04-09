# Template: Tarea

Plantilla para enviar una tarea de un agente a otro.

---

## Tarea

**ID**: `[task_id]`
**De**: `[agente_origen]`
**Para**: `[agente_destino]`
**Fecha**: `[timestamp]`
**Deadline**: `[fecha_límite]`

---

### Descripción

```
[Descripción clara de qué necesita hacer el agente receptor]
```

---

### Contexto

```markdown
## Background
[Información relevante sobre el proyecto, decisiones previas, etc.]

## Requisitos
- [Requisito 1]
- [Requisito 2]

## Restricciones
- [Restricción 1]
- [Restricción 2]
```

---

### Criterios de Éxito

- [ ] [Criterio medible 1]
- [ ] [Criterio medible 2]
- [ ] [Criterio medible 3]

---

### Recursos

- **Código**: `[link a archivos]`
- **Docs**: `[link a documentación]`
- **Specs**: `[link a specifications]`

---

### Notas Adicionales

```
[Cualquier nota extra para el agente]
```

---

## Respuesta Esperada

El agente debe retornar:
1. **Status**: `pending_approval` | `completed` | `error`
2. **Output**: Qué produjo
3. **Logs**: Notas relevantes
4. **Next Actions**: Próximos pasos sugeridos