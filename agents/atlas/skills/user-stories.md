# Skill: User Stories

## Descripción

Skill para escribir historias de usuario efectivas con criterios de aceptación claros.

## Triggers

- "historia de usuario"
- "user story"
- "criterios de aceptación"
- "acceptance criteria"
- "como usuario"

## Formato de Historia de Usuario

```
Título: [Nombre breve]

Como [rol],
Quiero [funcionalidad],
Para [beneficio].

Criterios de aceptación:
- [ ] [Criterio 1]
- [ ] [Criterio 2]
- [ ] [Criterio 3]

Estimación: [1-13 puntos]
Prioridad: [Must/Should/Could/Won't]
```

## Reglas

### INVEST
- **I**ndependent: Independiente de otras historias
- **N**egotiable: Negociable, no contrato rígido
- **V**aluable: Aporta valor al usuario
- **E**stimable: Estimable por el equipo
- **S**mall: Pequeña, cabe en un sprint
- **T**estable: Testeable

### Criterios de Aceptación
- Usar formato Gherkin: Given/When/Then
- Ser verificables
- Cubrir happy path y edge cases

## Ejemplo

```
Historia: Login con Google

Como usuario registrado,
Quiero iniciar sesión con mi cuenta de Google,
Para no tener que recordar otra contraseña.

Criterios de aceptación:
- [ ] Botón "Login with Google" visible en página de login
- [ ] Redirect a OAuth de Google
- [ ] Después de login, redirigir a página principal
- [ ] Mostrar nombre del usuario logueado

Estimación: 5 puntos
Prioridad: Must
```

## Output

Historia de usuario completa con:
- Título descriptivo
- Descripción (Como/Quiero/Para)
- Criterios de aceptación (Gherkin)
- Estimación
- Prioridad