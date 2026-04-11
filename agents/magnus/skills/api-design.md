# Skill: API Design

## Descripción

Skill para diseñar APIs RESTful o GraphQL efectivas y bien estructuradas.

## Triggers

- "diseñar api"
- "api design"
- "rest"
- "graphql"
- "endpoint"
- "endpoint"

## Principios de Diseño

### RESTful
- **Recursos**: URLs representan recursos (sustantivos)
- **Verbos HTTP**: GET, POST, PUT, PATCH, DELETE
- **Códigos de estado**: 200, 201, 400, 404, 500
- **Stateless**: Cada request es independiente

### Naming
- Plural para colecciones: `/users`, `/products`
- Singular para recurso específico: `/users/123`
- Anidación para relaciones: `/users/123/orders`
- Verbos para acciones: `/users/123/activate`

### Versioning
- En URL: `/api/v1/users`
- En header: `Accept: application/vnd.api+json;version=1`

## Formato de Endpoint

```
GET    /resources          - Listar recursos
GET    /resources/:id      - Obtener recurso específico
POST   /resources          - Crear recurso
PUT    /resources/:id      - Actualizar recurso completo
PATCH  /resources/:id      - Actualizar recurso parcial
DELETE /resources/:id      - Eliminar recurso
```

## Request/Response

### Request
```json
{
  "method": "POST",
  "url": "/api/v1/users",
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer ..."
  },
  "body": {
    "name": "Juan",
    "email": "juan@example.com"
  }
}
```

### Response
```json
{
  "status": 201,
  "body": {
    "id": "123",
    "name": "Juan",
    "email": "juan@example.com",
    "createdAt": "2026-04-09T12:00:00Z"
  }
}
```

## Códigos de Estado

| Código | Significado |
|--------|-------------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 422 | Unprocessable Entity |
| 500 | Internal Server Error |

## Errores

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email inválido",
    "details": [
      {
        "field": "email",
        "message": "Debe ser un email válido"
      }
    ]
  }
}
```

## Pagination

```json
GET /users?page=2&limit=20

{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 100,
    "pages": 5
  }
}
```

## Filtering & Sorting

```
GET /users?status=active&sort=name,-createdAt
GET /products?price_min=10&price_max=100
```

## Output

- Documentación de endpoints
- Contratos de request/response
- Códigos de error
- Ejemplos de uso