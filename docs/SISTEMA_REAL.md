# 🎓 Sistema Real de Aprendizaje con Claude Code

> **Sistema correcto que SÍ usa Claude Code dinámicamente**

## 🎯 Lo Que Realmente Tienes Ahora

Este es el sistema **correcto** que pediste originalmente: un flujo de trabajo que **usa Claude Code (yo) activamente** con subagentes para ayudarte a estudiar Sistemas de Comunicaciones.

---

## ✅ Arquitectura Real

```
Usuario ejecuta comando en Claude Code
    ↓
Slash command (.claude/commands/)
    ↓
Claude Code (yo) procesa dinámicamente
    ↓
Uso Task tool con subagentes si es necesario
    ↓
Genero contenido personalizado EN ESE MOMENTO
    ↓
Guardo en archivos (state/, outputs/, sessions/)
    ↓
Usuario puede continuar después
```

---

## 🚀 Cómo Funciona

### 1️⃣ Iniciar Sesión de Estudio

En Claude Code, escribes:

```
/start-session rodrigo
```

**¿Qué pasa?**
- Yo (Claude Code) ejecuto el comando
- Leo tu estado de `state/learning_state.json`
- Analizo tu progreso
- Creo `state/current_session.json`
- Te muestro recomendaciones personalizadas basadas en tu situación

**Output que recibes:**
```
✓ Session started for: rodrigo
⏰ Started at: 14:30
📅 Exam in: 29 days

📊 Current Status:
• Overall progress: 8%
• Active unit: Unit 7 - Ruido
• Concepts mastered: 5/87
• Problems solved: 2

💡 Recommendations:
1. Focus on noise figure derivations
2. Practice more Friis cascade problems
3. ⚠️ Only 29 days until exam!

✨ Ready! Use these commands:
• /derive [formula] - Get step-by-step derivation
• /solve [file] - Solve an exercise
• /progress - Check your progress
• /end-session - Finish and save
```

---

### 2️⃣ Derivar una Fórmula

```
/derive AM
```

o más específico:

```
/derive Friis cascade noise figure with detailed mathematical steps
```

**¿Qué pasa?**
- Yo (Claude Code) leo el comando
- Genero una derivación **desde cero** en ese momento
- No es texto hardcodeado - es generado dinámicamente
- Adapto el nivel de detalle a lo que necesitas
- Guardo en `outputs/derivations/[TOPIC]_[DATE].md`
- Actualizo tu sesión en `state/current_session.json`

**Output que recibes:**

Una derivación completa con:
- Definiciones y punto de partida
- Pasos matemáticos justificados
- Interpretación física
- Validación dimensional
- Casos especiales y límites
- Conexiones con otros conceptos

**Archivo guardado:**
```markdown
# Amplitude Modulation (AM) - Complete Derivation

## Starting Point

We want to derive the time-domain expression for an AM signal...

## Step 1: Definition of Amplitude Modulation

**Equation:**
$$s_{AM}(t) = A_c [1 + m(t)] \cos(2\pi f_c t)$$

**Explanation:**
The AM signal is created by varying the amplitude of a high-frequency carrier...

[... derivación completa ...]

## Final Result

$$s_{AM}(t) = A_c [1 + k_a m(t)] \cos(2\pi f_c t)$$

Where:
- $A_c$ = Carrier amplitude [V]
- $k_a$ = Amplitude sensitivity [V⁻¹]
- $m(t)$ = Message signal (normalized)
- $f_c$ = Carrier frequency [Hz]

## Key Insights

• Bandwidth: BW = 2f_m (twice the message bandwidth)
• Power efficiency: Maximum 33.3% when μ = 1
• Trade-off: Simplicity vs. power efficiency

[... más detalles ...]
```

---

### 3️⃣ Resolver un Ejercicio

```
/solve docs/ejercicio_ruido.txt
```

**¿Qué pasa?**
- Yo leo el archivo del ejercicio
- Analizo qué tipo de problema es
- Identifico las variables y datos
- Genero una solución paso a paso **en ese momento**
- Valido dimensionalmente
- Explico cada paso con justificación
- Guardo en `outputs/solutions/`
- Actualizo tu progreso

**Output que recibes:**

```markdown
# Ejercicio 3: Ruido - Solution

## Problem Analysis

**Type:** Noise figure and cascaded systems
**Given:**
- G = 50 dB
- BW = 20 kHz
- P_n_out = 72×10⁻¹² W
- η_in = 12×10⁻²¹ W/Hz

**Asked:**
a) Noise figure F (linear and dB)
b) Noise temperature T_e
c) Cascaded noise figure F_total
d) Total cascade temperature T_total
e) Output SNR

## Solution

### Part (a): Noise Figure

**Step 1: Convert gain from dB to linear**

Formula:
$$G_{linear} = 10^{G_{dB}/10}$$

Calculation:
$$G_{linear} = 10^{50/10} = 10^5 = 100000$$

**Step 2: Calculate input noise power**

Formula:
$$P_{n,in} = \eta_{in} \times BW$$

Calculation:
$$P_{n,in} = 12 \times 10^{-21} \times 20 \times 10^3$$
$$P_{n,in} = 2.4 \times 10^{-16} \text{ W}$$

**Step 3: Apply noise figure definition**

Formula:
$$F = \frac{P_{n,out}}{G \times P_{n,in}}$$

Calculation:
$$F = \frac{72 \times 10^{-12}}{100000 \times 2.4 \times 10^{-16}}$$
$$F = \frac{72 \times 10^{-12}}{2.4 \times 10^{-11}} = 3.0$$

**Step 4: Convert to dB**

Formula:
$$F_{dB} = 10 \log_{10}(F)$$

Calculation:
$$F_{dB} = 10 \log_{10}(3.0) = 4.77 \text{ dB}$$

✅ **Answer (a):** F = 3.0 (linear) = 4.77 dB

**Validation:**
- Dimensions: [P]/([dimensionless]×[P]) = [dimensionless] ✓
- Sanity: F > 1 (amplifier adds noise) ✓
- Typical: F = 3 is reasonable for RF amplifier ✓

[... continúa con partes b), c), d), e) ...]
```

---

### 4️⃣ Ver Progreso

```
/progress
```

**¿Qué pasa?**
- Leo tu `state/learning_state.json`
- Analizo tu historial de sesiones
- Calculo métricas de velocidad de aprendizaje
- Identifico áreas débiles
- Genero recomendaciones personalizadas

**Output:** Reporte completo como se muestra en el comando

---

### 5️⃣ Terminar Sesión

```
/end-session
```

**¿Qué pasa?**
- Leo tu sesión de `state/current_session.json`
- Calculo duración y trabajo completado
- Actualizo `state/learning_state.json` con nuevo progreso
- Creo un log detallado en `sessions/YYYY-MM/`
- Agrego entrada al historial
- Borro la sesión activa
- Te muestro resumen y próximos pasos

---

## 🛠️ Herramientas Adicionales

### Scripts de Utilidad (standalone)

Para checks rápidos sin entrar a Claude Code:

```bash
# Ver progreso rápido
python scripts/quick_progress.py

# Verificar si hay sesión activa
python scripts/check_session.py

# Listar ejercicios disponibles
python scripts/list_exercises.py
```

Estos scripts son simples y **no requieren** Claude Code, solo leen los archivos de estado.

---

## 📂 Estructura de Archivos

```
communications-learning-system/
├── .claude/
│   └── commands/              # ← Slash commands para Claude Code
│       ├── start-session.md
│       ├── derive.md
│       ├── solve.md
│       ├── progress.md
│       └── end-session.md
│
├── state/                     # ← Estado del sistema (Git)
│   ├── learning_state.json    # Tu progreso general
│   ├── current_session.json   # Sesión activa (temporal)
│   └── session_history.jsonl  # Historial completo
│
├── outputs/                   # ← Contenido generado por Claude Code
│   ├── derivations/           # Derivaciones en Markdown
│   ├── solutions/             # Soluciones de ejercicios
│   └── anki/                  # (futuro) Tarjetas Anki
│
├── sessions/                  # ← Logs de sesiones
│   └── YYYY-MM/
│       └── YYYY-MM-DD_user_session.md
│
├── docs/                      # ← Documentación y ejercicios
│   ├── programa_materia.md
│   ├── ejercicio_ruido.txt
│   └── [tus ejercicios].txt
│
├── scripts/                   # ← Utilidades standalone
│   ├── quick_progress.py
│   ├── check_session.py
│   └── list_exercises.py
│
└── agents/                    # ← Sistema antiguo (puede ignorarse)
    └── [código Python hardcodeado - ya no se usa]
```

---

## 🎯 Flujo de Trabajo Típico

### Sesión de Estudio Completa

**En Claude Code:**

```
# 1. Iniciar
/start-session rodrigo

# 2. Estudiar teoría
/derive AM
/derive Friis cascade formula

# 3. Practicar
/solve docs/ejercicio_ruido.txt
/solve docs/ejercicio_AM.txt

# 4. Revisar progreso
/progress

# 5. Terminar
/end-session
```

**En terminal (opcional):**

```bash
# Check rápido antes de empezar
python scripts/check_session.py

# Ver qué ejercicios hay disponibles
python scripts/list_exercises.py

# Después de terminar, commit
git add .
git commit -m "Session: Studied AM and noise, solved 2 exercises"
git push
```

---

## 🧠 Ventajas del Sistema Real

### ✅ Usa Claude Code Activamente

- Cada derivación es **generada dinámicamente**
- Puedo adaptarme a tu nivel y necesidades
- Respuestas personalizadas, no plantillas
- Uso subagentes cuando es necesario

### ✅ Contenido de Alta Calidad

- Derivaciones rigurosas desde primeros principios
- Explicaciones pedagógicas, no solo matemáticas
- Validación dimensional y física
- Conexiones entre conceptos

### ✅ Tracking Inteligente

- Estado persistente en Git
- Progreso medible y cuantificable
- Recomendaciones basadas en datos
- Historial completo de sesiones

### ✅ Colaboración Posible

```bash
# Persona A
/start-session alice
/derive Shannon-Hartley
/end-session
git commit && git push

# Persona B
git pull  # Recibe el trabajo de A
/start-session bob
# Ve el progreso de Alice
/solve problema_capacidad.txt
/end-session
git commit && git push
```

### ✅ Offline-Friendly con Git

- Todo el estado en archivos
- No depende de memoria de conversación
- Puedes volver después de semanas
- Backup automático con Git

---

## 💡 Casos de Uso Reales

### 1. Entender una Fórmula

**Problema:** "No entiendo de dónde sale la fórmula de Friis"

**Solución:**
```
/derive Friis cascade noise figure from first principles, include physical interpretation
```

Recibes derivación completa desde SNR_in/SNR_out hasta la fórmula final.

---

### 2. Prepararse para Examen

**Problema:** "Examen en 4 semanas, qué estudiar?"

**Solución:**
```
/progress
```

Recibes análisis de qué unidades dominas, qué te falta, cuántas horas necesitas.

---

### 3. Resolver Ejercicio de Práctica

**Problema:** "Tengo este ejercicio del libro"

**Solución:**
1. Copia el enunciado a `docs/mi_ejercicio.txt`
2. En Claude Code:
```
/solve docs/mi_ejercicio.txt
```

Recibes solución paso a paso con explicaciones.

---

### 4. Repaso Antes del Oral

**Problema:** "Tengo oral mañana, repaso?"

**Solución:**
```
/derive AM level:expert
/derive FM level:expert
/derive Shannon-Hartley level:expert
```

Cada uno con máximo nivel de detalle para explicar al profesor.

---

## 🆚 Comparación: Sistema Antiguo vs Nuevo

| Aspecto | Sistema Antiguo (Python CLI) | Sistema Nuevo (Claude Code) |
|---------|------------------------------|------------------------------|
| **Contenido** | Hardcodeado en strings | Generado dinámicamente por mí |
| **Flexibilidad** | Fijo, no se adapta | Me adapto a tus necesidades |
| **Calidad** | Limitado a lo que escribí | Sin límites, siempre actualizado |
| **Mantenimiento** | Hay que editar código Python | Yo mejoro con cada versión |
| **Costo** | Gratis (offline) | Gratis (incluido en Claude Code) |
| **Uso de IA** | ❌ No usa IA | ✅ Usa Claude activamente |
| **Personalización** | ❌ No personaliza | ✅ Personalizado para ti |
| **Progreso** | ✅ Sí (aprovechado) | ✅ Sí (mejorado) |

---

## 🔮 Capacidades Avanzadas

### Uso de Subagentes

Cuando una tarea es compleja, yo puedo usar el **Task tool** internamente:

```
/derive Shannon-Hartley with proof of channel coding theorem
```

Internamente, yo podría:
1. Lanzar subagente "Explore" para buscar información sobre el teorema
2. Lanzar subagente especializado para la derivación matemática
3. Combinar resultados y presentarte la derivación completa

**Tú no ves esto** - yo lo manejo automáticamente según la complejidad.

---

### Preguntas Durante Derivación

Mientras derivo, puedes interrumpir:

```
Usuario: /derive AM

[Yo empiezo a derivar...]

Usuario: "Wait, why does the modulation index have to be ≤ 1?"

[Yo explico en detalle]

Usuario: "Ok, continue"

[Continúo la derivación]
```

---

### Generación de Material Adicional

Después de una derivación:

```
Usuario: "Can you create Anki flashcards from this AM derivation?"

Yo: [Genero tarjetas conceptuales]
- Front: "What is the bandwidth of an AM signal?"
- Back: "BW = 2f_m (twice the message signal bandwidth)"

[Guardo en formato importable a Anki]
```

---

## 📋 Comandos Disponibles

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `/start-session [user]` | Iniciar sesión de estudio | `/start-session rodrigo` |
| `/derive [formula]` | Derivar fórmula dinámicamente | `/derive Friis cascade` |
| `/solve [file]` | Resolver ejercicio | `/solve docs/ejercicio.txt` |
| `/progress` | Ver progreso detallado | `/progress` |
| `/end-session` | Terminar y guardar sesión | `/end-session` |

---

## 🎓 Primeros Pasos

1. **Asegúrate de estar en el directorio del proyecto**
   ```bash
   cd communications-learning-system
   ```

2. **Abre Claude Code en este directorio**
   (Ya estás aquí!)

3. **Inicia tu primera sesión:**
   ```
   /start-session rodrigo
   ```

4. **Prueba derivar algo:**
   ```
   /derive AM with detailed steps
   ```

5. **Resuelve un ejercicio:**
   ```
   /solve docs/ejercicio_ruido.txt
   ```

6. **Termina la sesión:**
   ```
   /end-session
   ```

---

## ❓ Preguntas Frecuentes

**P: ¿Tengo que usar los slash commands?**
R: No, puedes pedirme directamente "derive AM" o "solve this exercise", pero los slash commands son más convenientes.

**P: ¿Qué pasa con el código Python que ya existe?**
R: Queda como referencia. El sistema de estado (`learning_state.json`) es útil y lo aprovechamos. El código de derivaciones hardcodeadas puede ignorarse.

**P: ¿Funciona offline?**
R: No, requiero conexión porque YO (Claude Code) genero el contenido. Pero los scripts de utilidad (`quick_progress.py`, etc.) sí funcionan offline.

**P: ¿Costo?**
R: Incluido en Claude Code, sin costo adicional de API.

**P: ¿Puedo modificar los comandos?**
R: Sí! Edita los archivos en `.claude/commands/` para personalizarlos.

---

## 🎯 Próximos Pasos

Ahora que entiendes el sistema real:

1. **Pruébalo:** Ejecuta `/start-session [tu nombre]`
2. **Experimenta:** Pide derivaciones y resuelve ejercicios
3. **Personaliza:** Edita los comandos según tus necesidades
4. **Estudia:** Usa el sistema para preparar tu examen del 2025-12-15

---

## 💬 Soporte

Si algo no funciona o necesitas ajustes:
- Pídeme ayuda directamente en Claude Code
- Reviso los logs de sesiones para ver qué mejorar
- Puedo adaptar los comandos a tu estilo de aprendizaje

**¡Este es el sistema que querías! 🎓✨**

Sistema que **me usa activamente** para ayudarte a dominar Sistemas de Comunicaciones.
