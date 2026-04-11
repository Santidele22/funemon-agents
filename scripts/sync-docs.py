#!/usr/bin/env python3

"""
Script de sincronización automática de documentación para funemon-agents.

Sincroniza los configs de agents/ con README.md y otros archivos.

Uso: python3 scripts/sync-docs.py

Este script es idempotente: puede ejecutarse múltiples veces sin causar problemas.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List

# Directorio raíz del proyecto
PROJECT_ROOT = Path(__file__).parent.parent

# Archivos y directorios
README_FILE = PROJECT_ROOT / "README.md"
AGENTS_DIR = PROJECT_ROOT / "agents"
ORCHESTRATOR_FILE = PROJECT_ROOT / "orchestator" / "config.md"

# Mapeo de nombres de personajes a roles para el README
NAME_TO_ROLE_MAP = {
    'atlas': 'PM',
    'magnus': 'Backend',
    'aurora': 'Frontend',
    'bruno': 'Tester',
    'almendra': 'Documentador',
    'gabriela': 'Seguridad'
}

# Orden de agentes en la tabla del README
AGENT_ORDER = ['atlas', 'magnus', 'aurora', 'bruno', 'almendra', 'gabriela']

# Descripciones cortas para el README (más legibles que el role completo)
ROLE_SHORT_DESCRIPTIONS = {
    'PM': 'Historias de usuario, sprints, backlog, priorización MoSCoW',
    'Backend': 'APIs, lógica de servidor, bases de datos, Rust, Go, Node',
    'Frontend': 'Interfaces UI/UX, React, Vue, Svelte, responsive, accessible',
    'Tester': 'Tests, QA, coverage, unit, integration, E2E',
    'Documentador': 'Docs, README, API specs, guías técnicas',
    'Seguridad': 'Reviews, auditorías, vulnerabilidades, OWASP'
}


def log(message: str) -> None:
    """Imprime mensaje de log."""
    print(f"[SYNC] {message}")


def error(message: str) -> None:
    """Imprime mensaje de error y termina."""
    print(f"[ERROR] {message}", file=sys.stderr)
    sys.exit(1)


def extract_yaml_frontmatter(content: str) -> Dict[str, any]:
    """
    Extrae el frontmatter YAML de un archivo Markdown.
    
    Retorna un diccionario con los campos del frontmatter.
    """
    # Buscar frontmatter entre --- y ---
    match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    
    frontmatter_text = match.group(1)
    metadata = {}
    
    # Parsear YAML simple
    current_key = None
    for line in frontmatter_text.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        if line.startswith('- '):
            # Es un item de lista
            if current_key and current_key in metadata:
                value = line[2:].strip().strip('"').strip("'")
                if isinstance(metadata[current_key], list):
                    metadata[current_key].append(value)
                else:
                    metadata[current_key] = [metadata[current_key], value]
        elif ':' in line:
            # Es un key-value
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            # Si el valor está vacío, es una lista vacía (para arrays YAML)
            metadata[key] = [] if not value else value
            current_key = key
    
    return metadata


def get_agents_list() -> List[Dict[str, str]]:
    """
    Obtiene la lista de agentes desde los configs.
    
    Retorna una lista de diccionarios con: name, role, description, triggers
    Ordenados según AGENT_ORDER.
    """
    agents_dict = {}
    
    # Leer todos los configs de agentes
    if AGENTS_DIR.exists():
        for agent_dir in AGENTS_DIR.iterdir():
            if agent_dir.is_dir():
                config_file = agent_dir / "config.md"
                if config_file.exists():
                    try:
                        content = config_file.read_text()
                        metadata = extract_yaml_frontmatter(content)
                        
                        if metadata:
                            name = metadata.get('name', '')
                            role = metadata.get('role', '')
                            description = metadata.get('description', '')
                            triggers = metadata.get('triggers', [])
                            
                            # Obtener el nombre del rol para el README
                            role_display = NAME_TO_ROLE_MAP.get(name, name.capitalize())
                            
                            agents_dict[name] = {
                                'name': name,
                                'name_cap': name[0].upper() + name[1:] if name else '',
                                'role': role,
                                'role_display': role_display,
                                'description': description,
                                'triggers': triggers if isinstance(triggers, list) else [triggers]
                            }
                    except Exception as e:
                        log(f"Error procesando {config_file.name}: {e}")
    
    # Ordenar según AGENT_ORDER
    agents = []
    for agent_name in AGENT_ORDER:
        if agent_name in agents_dict:
            agents.append(agents_dict[agent_name])
    
    return agents


def generate_readme_table(agents: List[Dict[str, str]]) -> str:
    """Genera la tabla de agentes para README.md."""
    lines = [
        "| Agente | Rol | Triggers |",
        "|--------|-----|----------|"
    ]
    
    for agent in agents:
        triggers_str = ', '.join(f'"{t}"' for t in agent['triggers'])
        # Usar descripción corta si está disponible, sino usar el rol completo
        role_desc = ROLE_SHORT_DESCRIPTIONS.get(
            agent['role_display'],
            agent['role']
        )
        lines.append(
            f"| **{agent['role_display']}** | {role_desc} | {triggers_str} |"
        )
    
    return '\n'.join(lines)


def get_orchestrator_metadata() -> Dict[str, str]:
    """Obtiene metadata del orquestador."""
    if ORCHESTRATOR_FILE.exists():
        try:
            content = ORCHESTRATOR_FILE.read_text()
            return extract_yaml_frontmatter(content)
        except Exception:
            pass
    return {}


def update_readme(agents: List[Dict[str, str]]) -> bool:
    """
    Actualiza la tabla de agentes en README.md.
    
    Retorna True si hubo cambios, False si no.
    """
    log("Actualizando README.md...")
    
    try:
        content = README_FILE.read_text()
        original_content = content
        
        # Buscar la sección de agentes (líneas 40-47 según el formato actual)
        # Patrón: desde | Agente | hasta el final de la tabla
        pattern = r'(\| Agente \| Rol \| Triggers \|\n\|--------\|-----\|----------\|\n(?:\|.*\|\n)*)'
        
        new_table = generate_readme_table(agents)
        
        # Reemplazar la tabla
        content = re.sub(pattern, new_table + '\n', content)
        
        # Escribir solo si hubo cambios
        if content != original_content:
            README_FILE.write_text(content)
            log("README.md actualizado")
            return True
        else:
            log("README.md ya está sincronizado")
            return False
            
    except Exception as e:
        log(f"Error actualizando README.md: {e}")
        return False


def check_inconsistencies(agents: List[Dict[str, str]]) -> List[str]:
    """
    Verifica inconsistencias entre configs y README.
    
    Retorna lista de inconsistencias encontradas.
    """
    inconsistencies = []
    
    # Leer README actual
    try:
        content = README_FILE.read_text()
        
        # Buscar la tabla actual
        table_match = re.search(
            r'\| Agente \| Rol \| Triggers \|.*?(?=\n\n|\n##|\Z)',
            content,
            re.DOTALL
        )
        
        if table_match:
            table_content = table_match.group(0)
            
            # Verificar cada agente
            for agent in agents:
                role_display = agent['role_display']
                # Buscar si el agente está en la tabla
                if f"**{role_display}**" not in table_content:
                    inconsistencies.append(
                        f"Agente '{agent['name']}' ({role_display}) no encontrado en README.md"
                    )
                
                # Verificar triggers
                for trigger in agent['triggers']:
                    if f'"{trigger}"' not in table_content and f"'{trigger}'" not in table_content:
                        # Solo reportar si faltan triggers principales
                        pass
        
    except Exception as e:
        inconsistencies.append(f"Error verificando README: {e}")
    
    return inconsistencies


def main():
    """Función principal."""
    log("=== Sincronización de Documentación ===")
    log(f"Proyecto: {PROJECT_ROOT}")
    
    # Verificar que los archivos existen
    if not AGENTS_DIR.exists():
        error(f"Directorio de agentes no encontrado: {AGENTS_DIR}")
    
    if not README_FILE.exists():
        error(f"README.md no encontrado: {README_FILE}")
    
    # Obtener lista de agentes
    log("Extrayendo metadata de agentes...")
    agents = get_agents_list()
    log(f"Encontrados {len(agents)} agentes")
    
    for agent in agents:
        log(f"  - {agent['role_display']}: {agent['name']} ({', '.join(agent['triggers'][:3])}...)")
    
    # Verificar inconsistencias
    inconsistencies = check_inconsistencies(agents)
    if inconsistencies:
        log("Inconsistencias encontradas:")
        for inc in inconsistencies:
            log(f"  ⚠️  {inc}")
    else:
        log("No se encontraron inconsistencias")
    
    # Actualizar archivos
    updated = update_readme(agents)
    
    if updated:
        # Agregar al commit
        log("=== Cambios realizados ===")
        log("README.md sincronizado con configs de agentes")
        log("")
        log("Para revisar cambios: git diff README.md")
        log("Para hacer commit: git add README.md && git commit -m 'docs: sync agents table'")
    else:
        log("=== Sincronización completada sin cambios ===")


if __name__ == "__main__":
    main()