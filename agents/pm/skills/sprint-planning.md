# Skill: Sprint Planning

## Descripción

Skill para planificar sprints efectivos y gestionar la capacidad del equipo.

## Triggers

- "sprint planning"
- "planificar sprint"
- "estimación"
- "capacity planning"
- "sprint goal"

## Proceso de Sprint Planning

### 1. Revisión del Backlog
- Ordenar historias por prioridad
- Identificar dependencias
- Seleccionar historias candidates

### 2. Commitment
- Definir sprint goal
- Seleccionar historias que caben en el sprint
- Commitment del equipo

### 3. Desglose de Tareas
- Dividir historias en tareas técnicas
- Asignar a miembros del equipo
- Estimar horas/tareas

### 4. Definition of Done
- Código mergueado
- Tests pasando
- Code review aprobado
- Dokumentación actualizada

## Estimación

### Fibonacci
- 1: Muy simple
- 2: Simple
- 3: Normal
- 5: Complejo
- 8: Muy complejo
- 13: 超复杂 (necesita más investigación)

### Capacity Planning
- Días hábiles del sprint
- Días de vacaciones/reuniones
- = Días disponibles por miembro
- × Miembros del equipo
- = Capacity total

## Sprint Goal

El sprint goal debe ser:
- **Claro**: Entendible por todos
- **Medible**: Se puede verificar
- **Alcanzable**: Realista
- **Valioso**: Aporta al producto

## Ejemplo de Sprint

```
Sprint 23: Autenticación

Sprint Goal: Implementar login con OAuth para que usuarios puedan autenticarse con Google

Commitment:
- Historia #42: OAuth con Google (8 pts)
- Historia #43: Pantalla de login (3 pts)
- Historia #44: Logout (2 pts)
- Historia #45: Sesión persistente (5 pts)

Total: 18 puntos
Velocidad anterior: 20 puntos
Status: Aceptable

Definition of Done:
- [ ] Tests unitarios > 80%
- [ ] Code review por 2 personas
- [ ]部署 a staging
- [ ] Documentación actualizada
```

## Output

- Sprint goal definido
- Historias comprometidas
- Tareas asignadas
- Definition of Done
- Capacity utilizada