# Skill: TDD - Test Driven Development

## Descripción

Skill para implementar software usando TDD: RED → GREEN → REFACTOR.

## Triggers

- "tdd"
- "test driven"
- "tests primero"
- "red green refactor"

## Ciclo TDD

### 1. RED - Escribir test que falla
```rust
#[test]
fn test_add_numbers() {
    let calculator = Calculator::new();
    assert_eq!(calculator.add(2, 3), 5); // Fallará porque add no existe
}
```

### 2. GREEN - Implementar lo mínimo para pasar
```rust
impl Calculator {
    pub fn add(&self, a: i32, b: i32) -> i32 {
        a + b // Implementación mínima
    }
}
```

### 3. REFACTOR - Mejorar sin cambiar comportamiento
```rust
impl Calculator {
    /// Suma dos números
    /// 
    /// # Arguments
    /// * `a` - Primer número
    /// * `b` - Segundo número
    /// 
    /// # Returns
    /// La suma de a + b
    pub fn add(&self, a: i32, b: i32) -> i32 {
        // Mejorar código manteniendo funcionalidad
        a + b
    }
}
```

## Estructura de Tests

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    // Setup común
    fn setup() -> TestContext {
        // inicializar lo necesario
    }
    
    #[test]
    fn test_description() {
        // Arrange
        let ctx = setup();
        
        // Act
        let result = ctx.sut.method();
        
        // Assert
        assert_eq!(result, expected);
    }
    
    #[test]
    #[should_panic(expected = "description")]
    fn test_should_panic() {
        // Test que debe panicar
    }
    
    #[test]
    fn test_async() {
        tokio::runtime_test(async {
            // Test async
        })
    }
}
```

## Naming de Tests

```
test_[method]_[expected_behavior]
test_should_[behavior]_when_[condition]
test_[component]_[behavior]
```

## Principios

1. **Test primero**: Escribir test antes del código
2. **Pequeños pasos**: Implementar lo mínimo
3. **Names descriptivos**: El test documenta el comportamiento
4. **AAA**: Arrange, Act, Assert
5. **No logique en tests**: Solo asserts simples
6. **Un assertion por test**: Más claro qué falla

## Coverage

- **Unit tests**: Mínimo 80%
- **Funcional**: 100% de features cubiertos
- **Edge cases**: Todos los casos extremos

## Output

- Tests que pasan
- Coverage >= 80%
- Código testeable