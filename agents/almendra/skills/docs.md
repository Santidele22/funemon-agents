# Skill: Documentation

## Descripción

Skill para crear documentación técnica clara y mantenible.

## Triggers

- "documentación"
- "docs"
- "readme"
- "documentar"
- "api documentation"

## README Template

```markdown
# Nombre del Proyecto

> Descripción corta (una línea)

## 🚀 Quick Start

```bash
npm install mi-proyecto
```

## 📖 Documentación

- [Getting Started](./docs/getting-started.md)
- [API Reference](./docs/api.md)
- [Contributing](./CONTRIBUTING.md)

## Features

- ✅ Feature 1
- ✅ Feature 2
- ✅ Feature 3

## Requisitos

- Node.js 18+
- npm 9+

## Instalación

```bash
git clone https://github.com/user/project.git
cd project
npm install
```

## Uso

```typescript
import { function } from 'mi-proyecto';

const result = function('input');
console.log(result);
```

## Configuración

| Variable | Descripción | Default |
|----------|-------------|---------|
| `API_URL` | URL de la API | `http://localhost:3000` |
| `DEBUG` | Modo debug | `false` |

## Contribuir

Ver [CONTRIBUTING.md](./CONTRIBUTING.md)

## Licencia

MIT
```

## API Documentation

```markdown
# API Reference

## Authentication

### POST /api/auth/login

**Request:**
```json
{
  "email": "user@example.com",
  "password": "secret"
}
```

**Response (200):**
```json
{
  "token": "jwt-token",
  "expiresIn": 3600
}
```

**Errors:**
- 400: Invalid credentials
- 429: Too many attempts

## Users

### GET /api/users

**Response (200):**
```json
{
  "data": [
    {
      "id": "123",
      "name": "Juan",
      "email": "juan@example.com"
    }
  ],
  "pagination": {
    "page": 1,
    "total": 100
  }
}
```
```

## Changelog

```markdown
# Changelog

## [1.0.0] - 2026-04-09

### Added
- Feature de autenticación
- Primer release público

### Changed
- Mejoras en performance

### Fixed
- Bug en login con caracteres especiales

## [0.1.0] - 2026-03-01

### Added
- Alpha release
```

## Contributing Guide

```markdown
# Contributing

## Setup

1. Fork el repo
2. Clone tu fork
3. Instalar dependencias: `npm install`

## Workflow

1. Crear branch: `git checkout -b feature/mi-feature`
2. Hacer cambios
3. Tests: `npm test`
4. Commit: usar conventional commits
5. Push: `git push origin feature/mi-feature`
6. PR: crear pull request

## Código Style

- Usar ESLint
- Prettier para formateo
- TypeScript strict

## Commits

Usar [Conventional Commits](https://conventionalcommits.org):
- `feat: add new feature`
- `fix: resolve bug`
- `docs: update docs`
```

## Reglas de Documentación

1. **Mantener actualizado**: Docs == Código
2. **Ser conciso**: Sin info redundante
3. **Ejemplos**: Siempre con ejemplos
4. **Code first**: Documentar mientras se codifica
5. **Versionar**: Changelog actualizado

## Output

- README.md
- API docs
- Contributing guide
- Changelog