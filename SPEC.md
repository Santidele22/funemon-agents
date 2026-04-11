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