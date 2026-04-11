# Skill: Database Design

## Descripción

Skill para diseñar esquemas de bases de datos eficientes y escalables.

## Triggers

- "database design"
- "diseñar base de datos"
- "schema"
- "tabla"
- "migración"
- "sql"

## Tipos de Base de Datos

### Relacionales (SQL)
- PostgreSQL, MySQL, SQLite
- UAtomic transactions, ACID
- Relaciones estrictas

### NoSQL
- MongoDB, Cassandra, DynamoDB
- Escalabilidad horizontal
- Flexibilidad de esquema

## Diseño de Schema

### Entidades y Relaciones

```
Usuario (1) ─────< Pedido (M) ─────> Producto (M)
   |                    |
   +──< Favorito >─────┘
```

### Normalización

**1NF**: Valores atómicos, sin repetidos
**2NF**: No hay dependencias parciales de clave
**3NF**: No hay dependencias transitivas

### Desnormalización
- Cuando leer > escribir
- Para caché
- Para reporting

## Tipos de Datos

| Tipo | Uso |
|------|-----|
| UUID | IDs únicos |
| VARCHAR | Strings cortos |
| TEXT | Strings largos |
| INTEGER | Números enteros |
| DECIMAL | Números con decimales precisos |
| BOOLEAN | true/false |
| TIMESTAMP | Fechas y horas |
| JSONB | Datos estructurados |

## Índices

- **B-tree**: Queries de igualdad y rango
- **Hash**: Queries de igualdad exacta
- **GIN**: Full-text search, JSON
- **BRIN**: Series temporales grandes

## Migraciones

```sql
-- Crear tabla
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Agregar índice
CREATE INDEX idx_users_email ON users(email);

-- Agregar columna
ALTER TABLE users ADD COLUMN avatar_url VARCHAR(500);
```

## Foreign Keys

```sql
ALTER TABLE orders 
ADD CONSTRAINT fk_orders_user 
FOREIGN KEY (user_id) REFERENCES users(id) 
ON DELETE CASCADE;
```

## Queries Comunes

### JOIN
```sql
SELECT o.id, u.name, p.title
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN products p ON o.product_id = p.id;
```

### Aggregations
```sql
SELECT user_id, COUNT(*) as total_orders
FROM orders
GROUP BY user_id
HAVING COUNT(*) > 5;
```

## Output

- Diagrama de schema
- Definición de tablas
- Índices recomendados
- Scripts de migración
- Queries de ejemplo