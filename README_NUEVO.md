# 🎓 Sistema de Aprendizaje con Claude Code

> **Sistema real que usa Claude Code activamente para estudiar Sistemas de Comunicaciones**

**Examen:** 2025-12-15 | **Estado:** ✅ Completamente funcional

---

## 🚀 Quick Start

```bash
# En Claude Code (este chat):

# 1. Iniciar sesión
/start-session rodrigo

# 2. Derivar fórmulas
/derive AM
/derive Friis cascade noise figure

# 3. Resolver ejercicios
/solve docs/ejercicio_ruido.txt

# 4. Ver progreso
/progress

# 5. Terminar
/end-session
```

---

## ✨ ¿Qué Hace Este Sistema?

**Usa Claude Code (yo) dinámicamente** para:

- 🧮 **Derivar fórmulas** desde primeros principios (generadas en tiempo real)
- 📝 **Resolver ejercicios** paso a paso con explicaciones
- 📊 **Trackear progreso** en archivos Git
- 🎯 **Recomendaciones** personalizadas basadas en tu avance
- 💾 **Persistencia** completa - continúa después de cerrar

---

## 🎯 Comandos Principales

| Comando | Qué Hace |
|---------|----------|
| `/start-session [nombre]` | Inicia sesión de estudio |
| `/derive [fórmula]` | Genera derivación matemática |
| `/solve [archivo]` | Resuelve ejercicio paso a paso |
| `/progress` | Muestra progreso detallado |
| `/end-session` | Termina y guarda sesión |

---

## 📖 Ejemplo Real

### Sesión de Estudio

```
Tú: /start-session rodrigo

Claude Code:
✓ Session started for: rodrigo
📅 Exam in: 29 days
📊 Overall progress: 8%
💡 Recommendations:
  1. Focus on noise figure derivations
  2. Practice Friis cascade problems
  3. Start Unit 8 soon

---

Tú: /derive AM with detailed mathematical steps

Claude Code:
[Genera derivación completa de AM desde cero]
# Amplitude Modulation - Complete Derivation

## Starting Point
We want to derive the time-domain expression...

[... derivación paso a paso ...]

✓ Saved to: outputs/derivations/AM_20251115.md

---

Tú: /solve docs/ejercicio_ruido.txt

Claude Code:
[Lee el ejercicio, lo analiza, y genera solución]

# Ejercicio 3: Ruido - Solution

## Part (a): Noise Figure

Step 1: Convert gain to linear
G_linear = 10^(50/10) = 100000

Step 2: Calculate input noise
P_n_in = η_in × BW = 2.4×10⁻¹⁶ W

[... solución completa ...]

✓ Saved to: outputs/solutions/ejercicio_ruido_20251115.md

---

Tú: /end-session

Claude Code:
📊 Session Summary
⏱️  Duration: 1h 23m
✅ Completed:
  • Derived: AM
  • Solved: ejercicio_ruido.txt
📈 Progress: 8% → 12% (+4%)
💡 Next: Continue with FM derivation

✓ Session log: sessions/2025-11/2025-11-15_rodrigo.md
```

---

## 🗂️ Estructura de Archivos

```
communications-learning-system/
├── .claude/commands/          # ← Slash commands
│   ├── start-session.md
│   ├── derive.md
│   ├── solve.md
│   ├── progress.md
│   └── end-session.md
│
├── state/                     # ← Tu progreso (Git)
│   ├── learning_state.json    # Estado general
│   ├── current_session.json   # Sesión activa
│   └── session_history.jsonl  # Historial
│
├── outputs/                   # ← Contenido generado
│   ├── derivations/           # Derivaciones
│   └── solutions/             # Soluciones
│
├── sessions/                  # ← Logs de sesiones
│   └── 2025-11/
│
├── docs/                      # ← Ejercicios y docs
│   ├── ejercicio_ruido.txt
│   └── programa_materia.md
│
└── scripts/                   # ← Utilidades
    ├── quick_progress.py
    ├── check_session.py
    └── list_exercises.py
```

---

## 💡 Características Clave

### ✅ Generación Dinámica

- **No es contenido hardcodeado**
- Claude Code genera todo en tiempo real
- Adaptado a tu nivel y necesidades
- Respuestas personalizadas

### ✅ Tracking Inteligente

- Progreso guardado en JSON
- Historial completo de sesiones
- Métricas de velocidad de aprendizaje
- Recomendaciones basadas en datos

### ✅ Persistencia con Git

- Todo el estado en archivos
- No depende de memoria de conversación
- Backup automático con Git
- Colaboración posible

### ✅ Offline-Friendly

Scripts de utilidad funcionan sin Claude:
```bash
python scripts/quick_progress.py    # Ver progreso
python scripts/check_session.py     # Ver sesión activa
python scripts/list_exercises.py    # Listar ejercicios
```

---

## 🎯 Casos de Uso

### 📚 Estudiar Teoría

```
/derive Shannon-Hartley theorem with proof
/derive Friis cascade formula from SNR definitions
/derive Carson's rule for FM bandwidth
```

### 📝 Practicar Ejercicios

```
/solve docs/ejercicio_ruido.txt
/solve docs/ejercicio_modulacion.txt
/solve docs/ejercicio_capacidad.txt
```

### 📊 Monitorear Progreso

```
/progress                    # Detallado en Claude Code
python scripts/quick_progress.py  # Rápido en terminal
```

### 🔄 Continuar Después

```bash
# Día 1
/start-session rodrigo
/derive AM
/end-session
git commit && git push

# Semana después
git pull
/start-session rodrigo
# Claude Code carga tu progreso anterior
/derive FM
```

---

## 🆚 Diferencia con Sistema Anterior

| Sistema Python (antiguo) | Claude Code (nuevo) |
|--------------------------|---------------------|
| Contenido hardcodeado | ✨ Generado dinámicamente |
| Derivaciones fijas | 🎯 Adaptadas a ti |
| No usa IA en runtime | ✅ Usa Claude activamente |
| Limitado | 🚀 Sin límites |

**Lo que aprovechamos del antiguo:**
- ✅ Estructura de estado (`learning_state.json`)
- ✅ Sistema de tracking de progreso
- ✅ Tests para validar estructura
- ✅ Ejercicios de ejemplo

---

## 📚 Documentación Completa

- **[SISTEMA_REAL.md](docs/SISTEMA_REAL.md)** - Documentación completa del sistema
- **[HOW_IT_WORKS.md](docs/HOW_IT_WORKS.md)** - Cómo funciona técnicamente
- **[programa_materia.md](docs/programa_materia.md)** - Programa del curso

---

## 🎓 Empezar Ahora

```
/start-session [tu_nombre]
```

¡Listo! Claude Code te guiará desde ahí.

---

## ❓ FAQ

**P: ¿Requiere internet?**
R: Sí, Claude Code genera contenido dinámicamente. Scripts de progreso funcionan offline.

**P: ¿Costo?**
R: Incluido en Claude Code, sin costo adicional.

**P: ¿Qué pasó con el código Python?**
R: Queda de referencia. El sistema nuevo usa Claude Code directamente.

**P: ¿Puedo personalizar?**
R: Sí! Edita archivos en `.claude/commands/`

**P: ¿Funciona para otros cursos?**
R: Puedes adaptarlo editando `programa_materia.md` y los comandos.

---

## 💬 Soporte

Cualquier duda, pregúntame directamente en Claude Code. Estoy aquí para ayudarte a dominar Sistemas de Comunicaciones.

**¡Éxito en tu examen del 2025-12-15! 🎓✨**

---

**Creado por:** Claude Code
**Fecha:** 2025-11-15
**Versión:** 2.0 (Sistema Real con Claude Code)
