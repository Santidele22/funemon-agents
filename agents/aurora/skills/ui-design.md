# Skill: UI Design

## Descripción

Skill para diseñar interfaces de usuario siguiendo principios de UX y diseño visual.

## Triggers

- "ui design"
- "diseño ui"
- "interfaz"
- "diseño visual"
- "layout"
- "componente"

## Principios de Diseño

### UX Fundamentals
- **Jerarquía visual**: Lo importante debe destacar
- **Consistencia**: Mismos patrones en toda la app
- **Feedback**: El usuario sabe qué pasó
- **Accesibilidad**: Todos pueden usar la app
- **Simplicidad**: Menos es más

### Diseño Visual
- **Espaciado**: Margins, padding consistentes
- **Tipografía**: Escala de tamaños clara
- **Color**: Paleta limitada, contraste adecuado
- **Sombras**: Profundidad y jerarquía

## Sistema de Diseño

### Tokens
```css
:root {
  /* Colores */
  --color-primary: #3B82F6;
  --color-secondary: #64748B;
  --color-success: #22C55E;
  --color-error: #EF4444;
  
  /* Espaciado */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  
  /* Tipografía */
  --font-xs: 12px;
  --font-sm: 14px;
  --font-md: 16px;
  --font-lg: 20px;
  --font-xl: 24px;
  
  /* Border radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
}
```

### Componentes Base
- Button
- Input
- Card
- Modal
- Dropdown
- Toast
- Table
- Navigation

## Layouts

### Grid
```
.container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
}
```

### Flexbox
```
.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.flex-between {
  display: flex;
  justify-content: space-between;
}
```

### Responsive
```css
/* Mobile first */
.card {
  padding: 16px;
}

@media (min-width: 768px) {
  .card {
    padding: 24px;
  }
}

@media (min-width: 1024px) {
  .card {
    padding: 32px;
  }
}
```

## Componentes

### Button
```
Primary: background azul, texto blanco
Secondary: background transparente, border
Danger: background rojo
Disabled: opacity 0.5, cursor not-allowed
```

### Input
```
States: default, focus, error, disabled
Incluir: label, placeholder, helper text, error message
```

### Card
```
Estructura: header, body, footer
Sombras:轻微 en desktop, none en mobile
Border radius: 8-12px
```

## Accesibilidad (A11y)

- **ARIA labels** donde corresponda
- **Focus visible**: siempre visible
- **Contrast ratio**: mínimo 4.5:1
- **Keyboard navigation**: todo navegable
- **Screen reader**: etiquetas correctas

## Output

- Wireframes o mockups
- Sistema de diseño
- Componentes definidos
- Guía de estilos