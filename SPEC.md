# SPEC: Integrar model-optimizer skill en funemon-agents

## Problem Statement

Los agentes de funemon-agents tienen configurado un sistema de budgets en sus archivos config.md, pero **no están usando la skill `model-optimizer`** que ya existe en `~/.config/opencode/skills/`. Esto ha caused que en el pasado no implementen correctamente el control de gastos.

## User Stories

**Como** agente (Magnus, Aurora, Bruno, Almendra, Gabriela),
**Quiero** tener la skill model-optimizer como referencia obligatoria en mi configuración,
**Para** que se apliquen automáticamente las reglas de optimización de costos durante mi trabajo.

## Acceptance Criteria

1. ✅ Cada agente tiene referencia a la skill `model-optimizer` en su config.md
2. ✅ La skill se marca como **ALWAYS ACTIVE** (siempre activa)
3. ✅ Los agentes entienden que deben seguir las reglas de la skill
4. ✅ Se aplicarán las reglas de Level Up/Down automáticamente

## Edge Cases

- Si un agente ya está usando un modelo de nivel superior, la skill manejará el downgrade automático
- Si el presupuesto se agota, la skill cambiara automáticamente a free

## Constraints

- NO modificar la skill global en ~/.config/opencode/skills/model-optimizer.md
- Solo agregar referencias en los configs de los agentes

## Implementation Plan

1. Actualizar agents/magnus/config.md - agregar referencia a model-optimizer
2. Actualizar agents/aurora/config.md - agregar referencia a model-optimizer
3. Actualizar agents/bruno/config.md - agregar referencia a model-optimizer
4. Actualizar agents/almendra/config.md - agregar referencia a model-optimizer
5. Actualizar agents/gabriela/config.md - agregar referencia a model-optimizer

## Success Criteria

- Todos los agentes referencian model-optimizer como skill obligatoria
- La documentación de cada agente menciona la skill

---

# SPEC: Documentación Automática

## Problem Statement

La documentación de funemon-agents está desactualizada y no se mantiene automáticamente cuando se agregan nuevos agentes o cambian las configuraciones.

## Solution

La skill `docs-auto-update` está configurada para detectar cambios importantes y actualizar la documentación automáticamente. Sin embargo, necesita que los agentes la usen activamente.

## Activación de Actualización Automática

La skill `docs-auto-update` se activa cuando:

1. **Nueva Feature**: Se detecta un nuevo archivo en `agents/*/`
2. **Breaking Change**: Se modifica el workflow de agentes
3. **Nueva Arquitectura**: Se agrega un nuevo agente
4. **Nuevo API**: Se crean nuevos templates o protocolos
5. **Milestone Completado**: Se hace merge de cambios significativos

## Archivos que se Actualizan Automáticamente

| Archivo | Cuándo Actualizar |
|---------|-------------------|
| README.md | Nuevos agentes, cambios en estructura |
| AGENTS.md | Nuevos triggers, cambios en skills |
| agents/*/config.md | Solo cuando el agente lo modifica |

## Para Activar la Actualización

Los agentes deben seguir el workflow:

1. Detectan un cambio importante
2. Usan la skill `docs-auto-update` 
3. La skill actualiza los archivos relevantes automáticamente
4. Se commitea con conventional commits

## Limitaciones Actuales

- La skill requiere que los agentes la invoquen explícitamente
- No hay CI/CD que la active automáticamente
- Los cambios manuales deben hacerse siguiendo git workflow