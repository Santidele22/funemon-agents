# Skill: Rust Development

## Descripción

Skill para desarrollar aplicaciones en Rust siguiendo las mejores prácticas del ecosistema.

## Triggers

- "rust"
- "desarrollo rust"
- "cargo"
- "rustlang"
- "wasm"

## Configuración del Entorno

```toml
# Cargo.toml
[package]
name = "my-app"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
axum = "0.7"

[dev-dependencies]
tokio-test = "0.4"
```

## Estructura de Proyecto

```
src/
├── main.rs           # Entry point
├── lib.rs            # Library root
├── config.rs         # Configuración
├── models/           # Modelos de datos
├── handlers/         # Handlers de HTTP
├── services/         # Lógica de negocio
├── repository/       # Acceso a datos
└── errors.rs         # Definición de errores
```

## Patrones Comunes

### Error Handling
```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("Database error: {0}")]
    Database(#[from] sqlx::Error),
    
    #[error("Not found: {0}")]
    NotFound(String),
    
    #[error("Unauthorized")]
    Unauthorized,
}

impl IntoResponse for AppError {
    fn into_response(self) -> Response {
        match self {
            AppError::NotFound(msg) => (StatusCode::NOT_FOUND, msg).into_response(),
            AppError::Unauthorized => (StatusCode::UNAUTHORIZED, "Unauthorized").into_response(),
            _ => (StatusCode::INTERNAL_SERVER_ERROR, "Internal error").into_response(),
        }
    }
}
```

### State Management
```rust
pub struct AppState {
    pub db: SqlitePool,
    pub config: Config,
}

impl Clone for AppState {
    fn clone(&self) -> Self {
        Self {
            db: self.db.clone(),
            config: self.config.clone(),
        }
    }
}
```

### Async Handlers
```rust
async fn get_user(
    State(state): State<AppState>,
    Path(user_id): Path<i64>,
) -> Result<Json<User>, AppError> {
    let user = state.repository.get_user(user_id).await?
        .ok_or(AppError::NotFound(format!("User {} not found", user_id)))?;
    Ok(Json(user))
}
```

## Testing

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[tokio::test]
    async fn test_something() {
        // Arrange
        let input = 42;
        
        // Act
        let result = do_something(input).await;
        
        // Assert
        assert_eq!(result, expected);
    }
}
```

## Crates Recomendados

| Crate | Uso |
|-------|-----|
| **axum** | Web framework |
| **tokio** | Async runtime |
| **serde** | Serialización |
| **thiserror** | Error handling |
| **sqlx** | Database |
| **tracing** | Logging |
| **tower** | Middleware |

## Seguridad

- **NUNCA** usar `unsafe` sin justificación
- **SIEMPRE** validar input
- **USAR** tipos de Ownership
- **EVITAR** `unwrap()` en producción

## Output

- Código en Rust
- Tests unitarios
- Configuración de Cargo
- Documentación de API