# Skill: Framework Development

## Descripción

Skill para desarrollar aplicaciones usando frameworks frontend modernos (React, Vue, Svelte).

## Triggers

- "react"
- "vue"
- "svelte"
- "nextjs"
- "nuxt"
- "framework"
- "componente"

## React / Next.js

### Estructura
```
src/
├── app/                 # Next.js App Router
│   ├── page.tsx
│   ├── layout.tsx
│   └── api/
├── components/         # Componentes reutilizables
│   ├── Button/
│   │   ├── Button.tsx
│   │   └── Button.test.tsx
│   └── ...
├── hooks/              # Custom hooks
├── lib/                # Utilidades
├── styles/             # Estilos
└── types/              # TypeScript types
```

### Componente Ejemplo
```tsx
import { useState } from 'react';

interface ButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary';
  onClick?: () => void;
  disabled?: boolean;
}

export function Button({ 
  children, 
  variant = 'primary',
  onClick,
  disabled = false 
}: ButtonProps) {
  const [loading, setLoading] = useState(false);
  
  const handleClick = async () => {
    if (onClick) {
      setLoading(true);
      await onClick();
      setLoading(false);
    }
  };
  
  return (
    <button 
      className={`btn btn-${variant}`}
      onClick={handleClick}
      disabled={disabled || loading}
    >
      {loading ? <Spinner /> : children}
    </button>
  );
}
```

### Hooks Personalizados
```tsx
export function useLocalStorage<T>(key: string, initialValue: T) {
  const [value, setValue] = useState<T>(() => {
    if (typeof window === 'undefined') return initialValue;
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : initialValue;
  });
  
  const setStoredValue = (value: T | ((val: T) => T)) => {
    const valueToStore = value instanceof Function 
      ? value(value) 
      : value;
    setValue(valueToStore);
    localStorage.setItem(key, JSON.stringify(valueToStore));
  };
  
  return [value, setStoredValue] as const;
}
```

## Vue / Nuxt

### Componente
```vue
<script setup lang="ts">
interface Props {
  title: string;
  count?: number;
}

const props = withDefaults(defineProps<Props>(), {
  count: 0
});

const emit = defineEmits<{
  (e: 'update', value: number): void;
}>();
</script>

<template>
  <div class="card">
    <h2>{{ title }}</h2>
    <p>Count: {{ count }}</p>
    <button @click="emit('update', count + 1)">
      Increment
    </button>
  </div>
</template>

<style scoped>
.card {
  padding: 1rem;
  border-radius: 8px;
}
</style>
```

## Svelte

### Componente
```svelte
<script lang="ts">
  export let name: string;
  let count = 0;
  
  function increment() {
    count += 1;
  }
</script>

<div class="greeting">
  <h1>Hello {name}!</h1>
  <button on:click={increment}>
    Clicked {count} times
  </button>
</div>

<style>
  h1 {
    color: blue;
  }
</style>
```

## State Management

### Zustand (React)
```ts
import { create } from 'zustand';

interface CounterStore {
  count: number;
  increment: () => void;
  decrement: () => void;
}

export const useCounterStore = create<CounterStore>((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
}));
```

### Pinia (Vue)
```ts
import { defineStore } from 'pinia';

export const useCounterStore = defineStore('counter', {
  state: () => ({ count: 0 }),
  actions: {
    increment() {
      this.count++;
    },
  },
});
```

## Testing

```tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

test('renders button and handles click', () => {
  const handleClick = vi.fn();
  render(<Button onClick={handleClick}>Click me</Button>);
  
  fireEvent.click(screen.getByText('Click me'));
  expect(handleClick).toHaveBeenCalled();
});
```

## Output

- Código de componentes
- Tests de componentes
- Hooks personalizados
- Configuración de proyecto