# Scripts de Sincronización

Este directorio contiene scripts utilitarios para mantener la documentación sincronizada.

## sync-docs.py

Script de sincronización automática de documentación.

### Qué hace

1. **Lee configs de agentes** (`agents/*/config.md`)
   - Extrae metadata YAML: `name`, `role`, `description`, `triggers`

2. **Mapea nombres a roles**
   - `pm` → PM
   - `magnus` → Backend
   - `aurora` → Frontend
   - `bruno` → Tester
   - `almendra` → Documentador
   - `gabriela` → Seguridad

3. **Genera tabla actualizada** para README.md
   - Formato consistente con el estilo del proyecto

4. **Verifica inconsistencias** entre configs y documentación

### Uso manual

```bash
python3 scripts/sync-docs.py
```

### Automatización

El script se ejecuta automáticamente via GitHub Actions cuando cambian los configs.

## Estructura esperada

```
funemon-agents/
├── agents/
│   ├── pm/config.md
│   ├── backend/config.md
│   ├── frontend/config.md
│   ├── tester/config.md
│   ├── documentador/config.md
│   └── seguridad/config.md
├── orchestator/
│   └── config.md
└── README.md
```

## Formato de config.md

Cada config debe tener frontmatter YAML:

```yaml
---
name: magnus
role: Backend Developer - The Eternal Architect
description: Los sistemas que construyo perduran milenios...
triggers:
  - "backend"
  - "api"
  - "server"
  - "database"
scope: Desarrollo de lógica de servidor
can_delegate:
  - bruno
  - almendra
  - gabriela
---
```

## Idempotencia

El script es idempotente: puede ejecutarse múltiples veces sin causar problemas. Si no hay cambios, no modifica archivos.