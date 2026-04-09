# Funemon Agents

> Sub-agentes especializados para desarrollo estructurado con SDD.

## ¿Qué es?

Repositorio de **sub-agentes especializados** que el orquestador delega para ejecutar tareas específicas. Cada agente tiene sus propias skills, contexto y comportamiento definido.

## Estructura

```
funemon-agents/
├── orchestator/        # Configuración del orquestador
├── agents/             # Sub-agentes especializados
│   ├── pm/            # Product Manager / Scrum
│   ├── backend/       # Desarrollo backend
│   ├── frontend/      # Desarrollo frontend
│   ├── tester/        # Testing / QA
│   ├── documentador/  # Documentación
│   └── seguridad/     # Security review
├── templates/          # Templates de comunicación
└── communication/     # Protocolo entre agentes
```

## Agentes Disponibles

| Agente | Rol | Triggers |
|--------|-----|----------|
| **PM** | Historias de usuario, sprints, priorización | "pm", "sprint", "historia", "backlog" |
| **Backend** | Lógica de servidor, APIs, DB | "backend", "api", "server", "database" |
| **Frontend** | UI/UX, interfaces | "frontend", "ui", "interface", "web" |
| **Tester** | Tests, QA, coverage | "test", "qa", "coverage", "testing" |
| **Documentador** | Docs, README, API specs | "docs", "documentación", "readme" |
| **Seguridad** | Reviews, auditorías | "security", "seguridad", "audit" |

## Uso

El **orquestador** carga el config del sub-agente según la tarea y le delega. El sub-agente:
1. Inicia sesión en Funemon (`funemon_memory_session_start`)
2. Carga sus skills específicas
3. Ejecuta la tarea
4. Retorna resultado al orquestador
5. Puede delegar a otros agentes si es necesario

## Comunicación

Los agentes se comunican mediante mensajes estructurados:
- **Tarea**: `templates/task.md`
- **Resultado**: `templates/result.md`

## Requisitos

- Funemon instalado y funcionando
- Ollama con modelo disponible (ej: llama3.2)

## Licencia

MIT