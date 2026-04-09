# Reglas de los Agentes - Funemon Agents

## Comportamiento General

### Al recibir una tarea del orquestador:

1. **Analizar tarea**: Entender qué se pide y el contexto
2. **Iniciar memoria**: `funemon_memory_session_start(project: "nombre")`
3. **Cargar contexto**: `funemon_memory_context(session_id: "ID")`
4. **Ejecutar**: Usar las skills propias del agente
5. **Guardar resultado**: `funemon_memory_store(type: "observation")`
6. **Retornar**: Responder al orquestador con el resultado

### Reglas de Comunicación

- **SIEMPRE** responder en el formato esperado por el orquestador
- **SIEMPRE** indicar status: `pending_approval` | `completed` | `error`
- **NUNCA** ejecutar código destructivo sin aprobar
- **PUEDEN** delegar a otros agentes si la tarea lo requiere

### Reglas de Memoria

Al inicio de cada tarea:
```
funemon_memory_session_start(project: "nombre-del-proyecto")
funemon_memory_context(session_id: "ID", limit: 5)
```

Durante la tarea:
- Decisiones importantes → `funemon_memory_store(type: "plan")`
- Errores encontrados → `funemon_memory_store(type: "error")`
- Descubrimientos relevantes → `funemon_memory_store(type: "observation")`

Al finalizar:
```
funemon_memory_reflect(session_id: "ID")
```

## Reglas de Seguridad

- **NUNCA** hacer `git push --force`
- **NUNCA** hacer `git reset --hard`
- **SIEMPRE** confirmar antes de operaciones destructivas
- **NUNCA** exponer credenciales/secrets

## Skills por Agente

Cada agente tiene sus propias skills en `agents/[agente]/skills/`.

## Cómo Delegar

Si un agente necesita delegar a otro:
1. Identificar qué agente es necesario
2. Crear mensaje de tarea
3. El otro agente asume el control
4. Retorna resultado al agente original
5. El original retorna al orquestador

## Formato de Respuesta al Orquestador

```markdown
## Resultado

### Status
[pending_approval | completed | error]

### Output
[Qué produjo el agente]

### Logs
[Notas relevantes]

### Next Actions
- [Próximos pasos sugeridos]
- [Otros agentes a Involucrar]
```