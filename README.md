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
│   ├── iris/           # Design Lead (diseño visual, marca, colores)
│   ├── atlas/          # Product Manager (scrum, historias, backlog)
│   ├── magnus/         # Backend Developer
│   ├── aurora/         # Frontend Developer
│   ├── bruno/          # QA Engineer
│   ├── almendra/       # Technical Writer
│   └── gabriela/       # Security Engineer
├── templates/          # Templates de comunicación
├── skills/             # Skills globales del ecosistema
└── communication/     # Protocolo entre agentes
```

## Agentes Disponibles

| Agente | Rol | Triggers |
|--------|-----|----------|
| **Iris** | Diseño visual, marca, paleta de colores, tipografía, design systems | "design", "branding", "colors", "palette", "typography", "logo", "visual", "brand", "style guide" |
| **ATLAS** | Historias de usuario, sprints, backlog, priorización MoSCoW | "pm", "sprint", "historia", "backlog", "task", "planning", "prioridad" |
| **Magnus** | APIs, lógica de servidor, bases de datos, Rust, Go, Node | "backend", "api", "server", "database", "rust", "node", "python" |
| **Aurora** | Interfaces UI/UX, React, Vue, Svelte, responsive, accessible | "frontend", "ui", "interface", "web", "react", "vue", "svelte", "css", "html" |
| **Bruno** | Tests, QA, coverage, unit, integration, E2E | "test", "qa", "coverage", "testing", "quality" |
| **Almendra** | Docs, README, API specs, guías técnicas | "docs", "documentation", "readme", "document", "api docs", "guide" |
| **Gabriela** | Reviews, auditorías, vulnerabilidades, OWASP | "security", "audit", "vulnerability", "vuln", "seguridad" |

## Flujo de Trabajo

```
Usuario → Tyrion (orquestador)
           ↓
       ATLAS (organiza tareas)
           ↓
       Tyrion (delega)
           ↓
    ┌─────┴─────┐
    ↓           ↓
  Iris    Magnus/Aurora/Bruno/Gabriela
(diseño)    (implementación)
    ↓
  Aurora
(frontend)
```

**Regla crítica:** Iris SIEMPRE se consulta antes de Aurora para tareas de frontend.

## Uso

El orquestador se instala automáticamente con `funemon-ecosystem install-global`. Cuando OpenCode inicia una sesión:

1. Carga el **orquestador SDD** de `~/.config/opencode/system-prompt/`
2. Carga las **skills** de `~/.config/opencode/skills/`
3. Puede usar **skills locales** de `project-skills/`
4. Delega a **sub-agentes** según el contexto

## 🧪 TDD - Test-Driven Development

All agents follow TDD as a mandatory practice:

- **Red**: Write failing test first
- **Green**: Write minimal code to pass
- **Refactor**: Improve design keeping tests green

See [TDD Workflow](../funemon-ecosystem/templates/global/skills/tdd-workflow.md) for details.

## Comunicación

Los agentes se comunican mediante mensajes estructurados:
- **Tarea**: `templates/task.md`
- **Resultado**: `templates/result.md`

## Actualización Automática de Documentación

La documentación se mantiene actualizada automáticamente mediante la skill `docs-auto-update`. Esta skill:

- Detecta cambios importantes (nuevas features, breaking changes, arquitectura)
- Actualiza automáticamente README.md y CHANGELOG.md
- Se activa cuando se detectan commits con convencionales commits

Ver [docs-auto-update skill](skills/docs-auto-update.md) para más detalles.

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