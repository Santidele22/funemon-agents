# Protocolo de Comunicación entre Agentes

## Visión General

Los agentes de Funemon se comunican mediante mensajes estructurados. Este documento define el protocolo.

## Flujo de Comunicación

```
Orquestador
    │
    ├──(tarea)──▶ PM
    │              │
    │◀──(resultado)┤
    │
    ├──(tarea)──▶ Backend
    │              │
    │◀──(resultado)┤
    │
    └──(tarea)──▶ Tester
                   │
                   └─(resultado)──▶ Orquestador
```

## Tipos de Mensaje

### 1. TASK (Tarea)
Enviado cuando un agente delega trabajo a otro.

**Estructura:**
```json
{
  "type": "task",
  "task_id": "uuid",
  "from": "backend",
  "to": "tester",
  "timestamp": "ISO8601",
  "deadline": "ISO8601",
  "payload": {
    "description": "...",
    "context": {...},
    "success_criteria": [...],
    "resources": {...}
  }
}
```

### 2. RESULT (Resultado)
Enviado cuando un agente completa una tarea.

**Estructura:**
```json
{
  "type": "result",
  "task_id": "uuid",
  "from": "tester",
  "to": "backend",
  "timestamp": "ISO8601",
  "status": "completed | pending_approval | error",
  "payload": {
    "output": {...},
    "logs": [...],
    "next_actions": [...],
    "delegate_to": ["seguridad"]
  }
}
```

### 3. ACK (Acknowledgment)
Enviado para confirmar recepción de un mensaje.

**Estructura:**
```json
{
  "type": "ack",
  "message_id": "uuid",
  "original_task_id": "uuid",
  "status": "received | rejected",
  "reason": "..."
}
```

## Reglas de Comunicación

### a) Todos los mensajes incluyen
- `type`: TASK, RESULT, o ACK
- `from`: Agente emisor
- `to`: Agente receptor
- `timestamp`: Cuándo se envió

### b) TASK debe incluir
- `task_id`: ID único de la tarea
- `deadline`: Cuándo debe completarse
- `payload.description`: Qué hacer
- `payload.success_criteria`: Cómo verificar

### c) RESULT debe incluir
- `status`: completed, pending_approval, error
- `payload.output`: Qué se produjo
- `payload.logs`: Notas relevantes
- `payload.next_actions`: Sugerencias

### d) Errores
- Si un agente no puede procesar un TASK, debe retornar un RESULT con `status: error` y explicación

## Ejemplo de Comunicación

### Paso 1: Orquestador → Backend
```json
{
  "type": "task",
  "task_id": "123e4567-e89b-12d3-a456-426614174000",
  "from": "orchestrator",
  "to": "backend",
  "timestamp": "2026-04-09T10:00:00Z",
  "deadline": "2026-04-09T18:00:00Z",
  "payload": {
    "description": "Implementar endpoint de login con JWT",
    "context": {
      "project": "mi-app",
      "historia_usuario": "HU-001"
    },
    "success_criteria": [
      "Endpoint /api/auth/login funcional",
      "Genera JWT válido",
      "Tests pasando"
    ]
  }
}
```

### Paso 2: Backend → Tester (delegación)
```json
{
  "type": "task",
  "task_id": "223e4567-e89b-12d3-a456-426614174001",
  "from": "backend",
  "to": "tester",
  "timestamp": "2026-04-09T12:00:00Z",
  "deadline": "2026-04-09T16:00:00Z",
  "payload": {
    "description": "Escribir tests para endpoint de login",
    "context": {
      "endpoint": "/api/auth/login",
      "tests_existentes": []
    },
    "success_criteria": [
      "Tests unitarios para auth",
      "Tests de integración",
      "Coverage > 80%"
    ]
  }
}
```

### Paso 3: Tester → Backend
```json
{
  "type": "result",
  "task_id": "223e4567-e89b-12d3-a456-426614174001",
  "from": "tester",
  "to": "backend",
  "timestamp": "2026-04-09T15:30:00Z",
  "status": "completed",
  "payload": {
    "output": {
      "tests_created": 12,
      "coverage": "85%",
      "files": ["tests/auth_test.rs"]
    },
    "logs": [
      "Mock de JWT funcionando",
      "Tests de edge cases incluidos"
    ],
    "next_actions": [
      "Revisar tests con code review"
    ],
    "delegate_to": ["seguridad"]
  }
}
```

### Paso 4: Backend → Orquestador
```json
{
  "type": "result",
  "task_id": "123e4567-e89b-12d3-a456-426614174000",
  "from": "backend",
  "to": "orchestrator",
  "timestamp": "2026-04-09T16:00:00Z",
  "status": "completed",
  "payload": {
    "output": {
      "endpoint_created": "/api/auth/login",
      "tests_coverage": "85%",
      "security_review": "pending"
    },
    "logs": [
      "JWT con expiration de 24h",
      "Password hasheada con bcrypt"
    ],
    "next_actions": [
      "Delegar a seguridad para review"
    ]
  }
}
```

## Timeout y Retry

- **Timeout**: Si un agente no responde en 30 min, re-enviar TASK
- **Max retries**: 3 intentos
- **Fallback**: Si todos los intentos fallan, reportar error al orquestador

## Logging

Todos los mensajes deben ser guardados en Funemon para auditoría:
```python
funemon_memory_store(
    type="observation",
    title=f"Message {type} between {from} and {to}",
    what=f"task_id: {task_id}, status: {status}"
)
```

## Herramientas

Los agentes pueden usar las templates en `templates/`:
- `task.md`: Para crear tareas
- `result.md`: Para retornar resultados