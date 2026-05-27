---
name: check-commit
description: "Run python tests + lint, then commit with a structured message. Trigger when the user asks to commit, comitear, or hacer commit."
allowed-tools: Bash, Read, Glob, Write, Edit
---

# Check Commit

Gatekeeper antes de commitear: corre tests, revisa wiki, y si todo pasa genera el commit.

## Procedure

### Step 1 — Mostrar resumen de cambios

```bash
git diff --stat
git status --short
```

### Step 2 — Correr tests (si existen)

```bash
python -m pytest tests/ -v
```

- Si **falla** → mostrar los tests fallidos, preguntar si quiere arreglarlos o forzar el commit (`--no-verify`).
- Si pasa → continuar.

### Step 3 — Revisar wiki

Analizar `git diff --stat` con este criterio:

- Si se tocaron archivos mencionados en páginas del wiki `.opencode/wiki/` (ver `source_file:` en frontmatter), mostrar qué páginas podrían estar desactualizadas.
- Señales de que la wiki necesita update:
  - Archivos originales eliminados/renombrados que son `source_file` de páginas wiki
  - Nuevas derivaciones, soluciones o explicaciones no reflejadas en la wiki
  - Cambios en el programa oficial (ProgramaSistemasDeComunicaciones.md)
- Preguntar: _"Do these changes affect any wiki pages? Should we update `.opencode/wiki/`?"_
- Si el usuario dice sí, actualizar las páginas correspondientes y agregar entrada en `log.md`.

### Step 4 — Generar el commit

Analizar los cambios con `git diff` y preguntar:

1. **Tipo**: feat / fix / refactor / chore / docs / test
2. **Descripción corta** (imperativo, < 72 chars)
3. **Cuerpo opcional** (bullet points de cambios)

### Step 5 — Ejecutar

```bash
git add <files>
git commit -m "<type>: <description>"
```

Si hay cuerpo:
```bash
git commit -m "<type>: <description>" -m "<body>"
```

Mostrar resultado del commit al final.
