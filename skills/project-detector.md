# Skill: project-detector

## What am I?

I am the skill that automatically detects the current project. I activate at the start of each session.

## Project Detection

### 1. Detect project type
Search in order:
- `package.json` → Node/npm project
- `Cargo.toml` → Rust project
- `pyproject.toml` → Python project
- `go.mod` → Go project
- `pom.xml` → Java/Maven project
- `*.csproj` → C#/.NET project
- `composer.json` → PHP project

### 2. Extract project name
- package.json → name
- Cargo.toml → package.name
- pyproject.toml → project.name
- go.mod → current directory

### 3. Detect framework/stack
- Node: next/, react/, vue/, angular/
- Rust: src/, tests/
- Python: src/, tests/, pyproject.toml with tool.setuptools
- Go: cmd/, internal/, pkg/

### 4. Detect testing tools
- Node: vitest, jest, mocha, playwright
- Rust: cargo test, cargo bench
- Python: pytest, unittest

## Output
Returns a JSON with:
```json
{
  "name": "project-name",
  "type": "rust|node|python|go|java|csharp",
  "framework": "detected-framework",
  "testing": ["test-tool-1", "test-tool-2"]
}
```

## Triggers
- At the start of each session
- When the user asks about the project
