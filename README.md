# Funemon Agents

> Sub-agentes especializados para desarrollo estructurado con SDD.

## ¿Qué es?

Repositorio de **sub-agentes especializados** que el orquestador delega para ejecutar tareas específicas. Cada agente tiene sus propias skills, contexto y comportamiento definido.

## Integración con funemon-ecosystem

```
funemon-ecosystem (CLI) → ~/.config/opencode/ (global) → proyecto local
                                                        ↓
                                              AGENTS.md + project-skills/
                                                        ↓
                                              OpenCode carga orquestador de funemon-agents
                                                        ↓
                                              Orquestador delega a sub-agentes
```

## Estructura

```
funemon-agents/
├── orchestator/        # Configuración del orquestador
│   └── config.md       # SDD Orchestrator completo
├── agents/             # Sub-agentes especializados
│   ├── atlas/         # Product Manager / Scrum
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
| **ATLAS** | Historias de usuario, sprints, priorización | "atlas", "sprint", "historia", "backlog", "prioridad", "velocity" |
| **Backend** | Lógica de servidor, APIs, DB, Rust, Node | "backend", "api", "server", "database", "rust", "node", "python" |
| **Frontend** | UI/UX, interfaces, React, Vue | "frontend", "ui", "interface", "web", "react", "vue", "svelte", "css", "html" |
| **Tester** | Tests, QA, coverage | "test", "qa", "coverage", "testing", "calidad" |
| **Documentador** | Docs, README, API specs | "docs", "documentación", "readme", "documentar", "api docs", "guía", "manual" |
| **Seguridad** | Reviews, auditorías | "security", "seguridad", "vulnerabilidad", "audit", "secure" |

## Uso

El orquestador se instala automáticamente con `funemon-ecosystem install-global`. Cuando OpenCode inicia una sesión:

1. Carga el **orquestador SDD** de `~/.config/opencode/system-prompt/`
2. Carga las **skills** de `~/.config/opencode/skills/`
3. Puede usar **skills locales** de `project-skills/`
4. Delega a **sub-agentes** según el contexto

## Comunicación

Los agentes se comunican mediante mensajes estructurados:
- **Tarea**: `templates/task.md`
- **Resultado**: `templates/result.md`

## Requisitos

- funemon-ecosystem instalado (`install-global`)
- OpenCode instalado
- (Opcional) Funemon para memoria persistente
- (Opcional) Ollama con modelo disponible (ej: llama3.2)

## Ver también

- [funemon-ecosystem](../funemon-ecosystem/) - CLI del ecosistema
- [funemon](../funemon/) - Sistema de memoria persistente

## Licencia

MIT