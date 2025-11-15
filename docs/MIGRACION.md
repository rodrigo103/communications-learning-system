# 🔄 Migración: Sistema Python → Sistema Claude Code

Este documento explica qué del sistema antiguo (Python CLI) se conserva y qué se reemplaza con el nuevo sistema (Claude Code).

---

## ✅ Lo Que SE CONSERVA (útil)

### 1. Sistema de Estado (`state/`)

**Archivos:**
- `state/learning_state.json` - ✅ **Mantener y usar**
- `state/session_history.jsonl` - ✅ **Mantener y usar**
- `state/current_session.json` - ✅ **Usar** (creado/borrado por sesiones)

**Por qué:** Estructura bien diseñada para trackear progreso, compatible con Git, y los comandos nuevos la usan.

### 2. Tests (`tests/`)

**Archivos:**
- `tests/test_coordinator.py` - ✅ **Mantener**
- `tests/test_derivation_engine.py` - ✅ **Mantener como referencia**
- `tests/test_problem_solver.py` - ✅ **Mantener como referencia**

**Por qué:** Validan la estructura de datos. Los tests del coordinator siguen siendo útiles.

### 3. Documentación (`docs/`)

**Archivos:**
- `docs/programa_materia.md` - ✅ **Mantener y usar**
- `docs/ejercicio_ruido.txt` - ✅ **Mantener y usar**
- `docs/MEJORAS_Y_REVISION.md` - ✅ **Mantener como referencia**
- `docs/MEJORAS_IMPLEMENTADAS.md` - ✅ **Mantener como referencia**

**Por qué:** Contienen información sobre el curso y ejercicios de práctica.

### 4. Esquemas (`learning_state_schema.json`)

**Archivo:**
- `learning_state_schema.json` - ✅ **Mantener**

**Por qué:** Define la estructura de datos esperada.

### 5. Configuración

**Archivos:**
- `requirements.txt` - ⚠️ **Simplificar** (algunas dependencias ya no se usan)
- `.gitignore` - ✅ **Mantener**

---

## ❌ Lo Que SE REEMPLAZA (ya no se usa)

### 1. Código Python de Agentes (`agents/`)

**Archivos:**
- `agents/coordinator.py` - ⚠️ **Reemplazado** por `/start-session` y `/end-session`
- `agents/derivation_engine.py` - ❌ **Reemplazado** por `/derive` (Claude Code genera dinámicamente)
- `agents/problem_solver.py` - ❌ **Reemplazado** por `/solve` (Claude Code genera dinámicamente)

**Por qué:** Las derivaciones hardcodeadas se reemplazan con generación dinámica por Claude Code.

**¿Qué hacer?** Pueden quedar como referencia pero no se ejecutan más.

### 2. CLI Python (`main.py`)

**Archivo:**
- `main.py` - ❌ **Reemplazado** por slash commands de Claude Code

**Por qué:** El CLI de Click se reemplaza con comandos nativos de Claude Code.

**¿Qué hacer?** Puede quedar como referencia de la arquitectura.

### 3. Outputs Antiguos

**Archivos:**
- `outputs/derivations/*.apkg` (Anki packages viejos) - ⚠️ **Opcional eliminar**
- `outputs/derivations/*.json` (derivaciones hardcodeadas) - ⚠️ **Opcional eliminar**

**Por qué:** Los nuevos outputs son archivos Markdown generados dinámicamente.

---

## 🆕 Lo Que SE AGREGA (nuevo sistema)

### 1. Slash Commands (`.claude/commands/`)

**Archivos nuevos:**
```
.claude/commands/
├── start-session.md  ← Iniciar sesión
├── derive.md         ← Derivar fórmulas
├── solve.md          ← Resolver ejercicios
├── progress.md       ← Ver progreso
└── end-session.md    ← Terminar sesión
```

**Función:** Comandos que Claude Code ejecuta para generar contenido dinámico.

### 2. Scripts de Utilidad (`scripts/`)

**Archivos nuevos:**
```
scripts/
├── quick_progress.py   ← Ver progreso rápido
├── check_session.py    ← Verificar sesión activa
└── list_exercises.py   ← Listar ejercicios
```

**Función:** Utilities standalone que no requieren Claude Code.

### 3. Documentación Nueva (`docs/`)

**Archivos nuevos:**
```
docs/
├── SISTEMA_REAL.md      ← Documentación completa del nuevo sistema
├── MIGRACION.md         ← Este archivo
└── HOW_IT_WORKS.md      ← Explicación técnica (del sistema antiguo)
```

### 4. README Actualizado

**Archivo nuevo:**
- `README_NUEVO.md` - Quick start del nuevo sistema

---

## 📊 Comparación de Archivos

| Archivo/Directorio | Sistema Antiguo | Sistema Nuevo | Acción |
|-------------------|-----------------|---------------|---------|
| `state/` | ✅ Usa | ✅ Usa | Mantener |
| `agents/*.py` | ✅ Ejecuta | ❌ No usa | Opcional: mover a `_archive/` |
| `main.py` | ✅ Ejecuta | ❌ No usa | Opcional: mover a `_archive/` |
| `.claude/commands/` | ❌ No existe | ✅ Usa | **Nuevo** |
| `scripts/*.py` | ❌ No existe | ✅ Usa | **Nuevo** |
| `tests/` | ✅ Ejecuta | ⚠️ Referencia | Mantener |
| `docs/ejercicio*.txt` | ✅ Usa | ✅ Usa | Mantener |
| `docs/programa_materia.md` | ✅ Usa | ✅ Usa | Mantener |
| `outputs/derivations/` | ✅ Genera `.apkg`, `.json` | ✅ Genera `.md` | Limpiar antiguos |

---

## 🔧 Plan de Migración (Opcional)

Si quieres limpiar el código antiguo:

### Opción 1: Archivar (Recomendado)

```bash
# Crear directorio de archivo
mkdir _archive

# Mover código Python antiguo
mv agents/ _archive/
mv main.py _archive/
mv tests/ _archive/  # O mantener para validar estructura

# Actualizar README
mv README.md _archive/README_antiguo.md
mv README_NUEVO.md README.md
```

### Opción 2: Mantener Todo

Dejar todo como está. El sistema nuevo simplemente no ejecuta los archivos antiguos.

### Opción 3: Eliminar

```bash
# Solo si estás SEGURO de que no los necesitas
rm -rf agents/
rm main.py
rm -rf outputs/derivations/*.apkg
rm -rf outputs/derivations/*.json
```

**⚠️ Recomendación:** Opción 1 (archivar) es más seguro.

---

## 🎯 Estructura Final Recomendada

```
communications-learning-system/
├── .claude/
│   └── commands/              ← NUEVO: Comandos para Claude Code
│
├── state/                     ← CONSERVADO: Estado del sistema
│   ├── learning_state.json
│   ├── current_session.json
│   └── session_history.jsonl
│
├── outputs/
│   ├── derivations/           ← CONSERVADO: Ahora genera .md
│   └── solutions/             ← CONSERVADO: Ahora genera .md
│
├── sessions/                  ← CONSERVADO: Logs de sesiones
│
├── docs/                      ← CONSERVADO + AMPLIADO
│   ├── programa_materia.md
│   ├── ejercicio_ruido.txt
│   ├── SISTEMA_REAL.md        ← NUEVO
│   ├── MIGRACION.md           ← NUEVO (este archivo)
│   └── HOW_IT_WORKS.md
│
├── scripts/                   ← NUEVO: Utilidades
│   ├── quick_progress.py
│   ├── check_session.py
│   └── list_exercises.py
│
├── _archive/                  ← OPCIONAL: Código antiguo
│   ├── agents/
│   ├── main.py
│   └── README_antiguo.md
│
├── learning_state_schema.json ← CONSERVADO
├── requirements.txt           ← SIMPLIFICAR
├── .gitignore                 ← CONSERVADO
└── README.md                  ← ACTUALIZADO
```

---

## 📝 Actualizar `requirements.txt`

### Dependencias Antiguas (no necesarias)

```
# Ya no se usan con Claude Code:
click>=8.1.0         # CLI - reemplazado por slash commands
rich>=13.0.0         # Formatting - no necesario
reportlab>=4.0.0     # PDF - Claude genera markdown
genanki>=0.13.0      # Anki - se puede generar después
matplotlib>=3.7.0    # Plotting - no implementado
seaborn>=0.12.0      # Plotting - no implementado
graphviz>=0.20.0     # Concept mapping - no implementado
networkx>=3.1        # Concept mapping - no implementado
```

### Dependencias Mínimas Necesarias

```txt
# Core (para scripts de utilidad)
python-dateutil>=2.8.0
pyyaml>=6.0  # Si usas YAML

# Testing (opcional - para validar estructura)
pytest>=7.4.0
pytest-cov>=4.1.0
```

**O simplemente:**
```txt
python-dateutil>=2.8.0
pytest>=7.4.0
```

---

## ✅ Checklist de Migración

- [ ] Probar comandos nuevos (`/start-session`, `/derive`, `/solve`)
- [ ] Verificar que `state/learning_state.json` se actualiza correctamente
- [ ] Revisar outputs generados en `outputs/derivations/` y `outputs/solutions/`
- [ ] Decidir qué hacer con código Python antiguo (archivar o eliminar)
- [ ] Actualizar README principal
- [ ] Simplificar `requirements.txt`
- [ ] Commit de cambios a Git
- [ ] (Opcional) Limpiar outputs antiguos (`.apkg`, `.json` hardcodeados)

---

## 🎓 Uso del Sistema Nuevo

```bash
# En Claude Code:
/start-session rodrigo
/derive AM
/solve docs/ejercicio_ruido.txt
/progress
/end-session

# En terminal (utilidades):
python scripts/quick_progress.py
python scripts/check_session.py
```

**Ver:** `README_NUEVO.md` para guía completa.

---

## 🤔 ¿Dudas?

**P: ¿Pierdo mi progreso actual?**
R: No. El archivo `state/learning_state.json` se mantiene intacto.

**P: ¿Puedo volver al sistema antiguo?**
R: Sí, si archivaste los archivos. Pero el nuevo sistema es superior.

**P: ¿Qué pasa con los outputs antiguos?**
R: Los nuevos se generan en Markdown. Los antiguos (`.apkg`, `.json`) pueden eliminarse.

**P: ¿Funciona igual para colaboradores?**
R: Mejor. El sistema de estado es el mismo, pero ahora cada uno usa Claude Code para generar contenido.

---

**Creado:** 2025-11-15
**Sistema Nuevo:** Completamente funcional ✅
