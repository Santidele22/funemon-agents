# Troubleshooting - Funemon Agents

Este documento contiene soluciones a problemas comunes durante la instalación y uso de Funemon Agents.

## Rust Compatibility Issues

### Error: "feature `edition2024` is required"

**Síntoma:**
```
error: failed to parse manifest at `.../clap_lex-1.1.0/Cargo.toml`
Caused by: feature `edition2024` is required
The package requires the Cargo feature called `edition2024`, but that feature is not stabilized in this version of Cargo (1.75.0).
```

**Causa:**
Algunas dependencias como `clap_lex v1.1.0` y `anstyle-query v1.1.5` requieren `edition2024` que solo está disponible en Rust 1.85+. Si tienes Rust 1.75 o anterior, la compilación fallará.

**Solución:**

#### Opción 1: Actualizar Rust (Recomendado)

```bash
# Actualizar Rust a la última versión estable
rustup update stable

# Verificar la versión
rustc --version
# Debería mostrar 1.85.0 o superior
```

#### Opción 2: El fix ya está en main

Si ya están aplicados los fixes en el repositorio, las dependencias problemáticas han sido ajustadas:

- `clap_lex = "0.6"` (en lugar de versiones más nuevas que requieren edition2024)
- `anstyle-query` downgradeado a v1.0.0

**Si todavía tienes problemas después de actualizar:**

1. Limpia el caché de Cargo:
   ```bash
   cargo clean
   rm -rf Cargo.lock
   ```

2. Reconstruye:
   ```bash
   cargo build --release
   ```

## Problemas de Instalación

### El orquestador no se carga

**Síntoma:** OpenCode no reconoce el orquestador SDD.

**Solución:**
1. Verifica que `install-global` se ejecutó correctamente:
   ```bash
   funemon-ecosystem status
   ```

2. Verifica que el archivo existe:
   ```bash
   ls -la ~/.config/opencode/system-prompt/sdd-orchestrator.md
   ```

3. Si no existe, reinstala:
   ```bash
   funemon-ecosystem install-global --force
   ```

### Skills no se cargan

**Síntoma:** Las skills globales no están disponibles.

**Solución:**
1. Verifica el directorio de skills:
   ```bash
   ls -la ~/.config/opencode/skills/
   ```

2. Verifica `opencode.json`:
   ```bash
   cat ~/.config/opencode/opencode.json
   ```

3. Si `mcpServers.funemon` no está configurado, agrégalo manualmente.

## Problemas de Memoria

### Funemon no guarda memorias

**Síntoma:** Las memorias no persisten entre sesiones.

**Solución:**
1. Verifica que Funemon esté corriendo:
   ```bash
   pgrep -f funemon
   ```

2. Verifica la base de datos:
   ```bash
   ls -la ~/.local/share/funemon/funemon.db
   ```

3. Inicializa si no existe:
   ```bash
   funemon init
   ```

### Error de conexión MCP

**Síntoma:** `connection refused` o `timeout` al conectar con Funemon.

**Solución:**
1. Verifica el puerto de Funemon (por defecto: configurable en opencode.json)
2. Reinicia el servidor Funemon:
   ```bash
   pkill -f funemon
   funemon mcp &
   ```

## Problemas de Agentes

### Los agentes no se delegan correctamente

**Síntoma:** Tyrion no delega a sub-agentes.

**Diagnóstico:**
1. Verifica que los archivos de config existen:
   ```bash
   ls -la ~/.config/opencode/agents/
   ```

2. Verifica el formato del AGENTS.md:
   ```bash
   cat ~/.config/opencode/AGENTS.md
   ```

**Solución:**
- Asegúrate de que las reglas de delegación están correctamente configuradas.
- Verifica que los triggers de cada agente coinciden con las palabras clave.

### Bruno no genera tests

**Síntoma:** Bruno delega pero no genera tests.

**Solución:**
1. Verifica que Bruno está configurado para TDD:
   ```bash
   cat ~/.config/opencode/agents/bruno/config.md
   ```

2. Verifica que la skill `tdd-workflow.md` existe en skills globales.

## Logs y Debug

### Habilitar logs detallados

```bash
# Para Funemon
export FUNEMON_LOG=debug
funemon mcp

# Para OpenCode con Funemon
export OPENCODE_LOG=debug
```

### Verificar salud del sistema

```bash
# Estado de Funemon
funemon stats

# Estado del ecosistema
funemon-ecosystem status

# Verificar configuración
funemon-ecosystem config
```

## Contacto y Soporte

Si encuentras un problema no documentado:

1. Busca en [Issues de GitHub](https://github.com/Santidele22/funemon-agents/issues)
2. Crea un nuevo issue con:
   - Versión de Rust (`rustc --version`)
   - Sistema operativo
   - Mensaje de error completo
   - Pasos para reproducir