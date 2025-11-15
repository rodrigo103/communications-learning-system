# 🤖 Flujo de Trabajo Real con Subagentes

> **Sistema correcto usando Task tool y subagentes especializados**

---

## 🎯 Arquitectura Real

```
Usuario solicita tarea
    ↓
Claude Code (yo, coordinador principal)
    ↓
Analizo qué se necesita
    ↓
Lanzo subagente(s) apropiado(s) con Task tool
    ↓
Subagente(s) ejecutan autónomamente
    ↓
Retornan resultados
    ↓
Yo presento resultados al usuario
```

---

## 🤖 Tipos de Subagentes Disponibles

### 1. `general-purpose`
**Cuándo usar:** Tareas complejas multi-paso que requieren múltiples herramientas

**Tiene acceso a:** TODAS las herramientas (Read, Write, Edit, Bash, Grep, Glob, WebFetch, etc.)

**Ejemplos:**
- Derivar fórmulas completas
- Resolver ejercicios complejos
- Generar reportes detallados
- Investigar y documentar

### 2. `Explore`
**Cuándo usar:** Explorar el codebase, buscar archivos, entender estructura

**Niveles:**
- `quick` - Búsquedas básicas
- `medium` - Exploración moderada
- `very thorough` - Análisis comprehensivo

**Ejemplos:**
- Encontrar todos los ejercicios
- Buscar patrones en derivaciones
- Mapear estructura de archivos

### 3. `Plan`
**Cuándo usar:** Planificar implementación de tareas complejas

**Ejemplos:**
- Crear plan de estudio
- Diseñar estrategia de examen
- Estructurar approach para tema complejo

---

## 📚 Workflows con Subagentes

### Workflow 1: Derivar Fórmula

**Usuario dice:** "Deriva la fórmula de Friis"

**Yo hago:**

```python
# 1. Lanzo subagente general-purpose
Task(
    subagent_type="general-purpose",
    description="Derive Friis cascade noise formula",
    prompt="""
    You are an expert in communications systems.

    Derive the Friis cascade noise figure formula from first principles:
    - Start with SNR definitions
    - Show step-by-step derivation
    - Include at least 6 mathematical steps
    - Explain physical meaning at each step
    - Provide final formula with all variables defined

    Save to: outputs/derivations/Friis_cascade_[DATE].md

    Use LaTeX notation. Be pedagogically clear.

    Return: Summary of derivation and file location
    """
)
```

**Subagente hace:**
1. Crea el archivo markdown
2. Escribe derivación completa con LaTeX
3. Guarda en outputs/derivations/
4. Me devuelve resumen

**Yo presento:**
```
✅ Friis Cascade Formula Derived!

📄 Saved to: outputs/derivations/Friis_cascade_20251115.md

📊 Summary:
- Starting point: SNR_out = SNR_in / F
- 8 derivation steps
- Final formula: F_total = F1 + (F2-1)/G1 + (F3-1)/(G1*G2) + ...
- Key insight: First stage dominates!

Would you like me to:
• Explain any step in more detail?
• Generate practice problems?
• Create Anki flashcards?
```

---

### Workflow 2: Resolver Ejercicio

**Usuario dice:** "Resuelve docs/ejercicio_ruido.txt"

**Yo hago:**

```python
# 1. Leo el ejercicio primero (para darte contexto)
ejercicio = read_file("docs/ejercicio_ruido.txt")

# 2. Muestro qué voy a hacer
print("Analyzing noise problem with 5 parts...")

# 3. Lanzo subagente
Task(
    subagent_type="general-purpose",
    description="Solve noise exercise completely",
    prompt=f"""
    Solve this communications systems problem step-by-step:

    {ejercicio}

    For EACH part:
    1. Identify what's being asked
    2. List relevant formulas
    3. Show calculation steps with units
    4. Provide numerical answer
    5. Validate dimensionally

    Structure:
    - Problem analysis
    - Given data table
    - Solution for each part (a, b, c, d, e)
    - Validation checks
    - Key learnings

    Save to: outputs/solutions/ejercicio_ruido_solution_[DATE].md

    Use LaTeX for equations. Show ALL work.

    Return: Summary with final answers
    """
)
```

**Subagente hace:**
1. Parsea el problema
2. Resuelve cada parte paso a paso
3. Valida dimensionalmente
4. Guarda solución completa
5. Me devuelve resumen con respuestas

**Yo presento:**
```
✅ Exercise Solved!

📄 Solution: outputs/solutions/ejercicio_ruido_solution_20251115.md

📊 Final Answers:
a) F = 3.0 (4.77 dB)
b) Te = 580 K
c) F_total = 3.00002
d) T_total = 580.01 K
e) SNR_out = 1.39 (1.42 dB)

✅ All dimensional checks passed
📝 5 key concepts identified

Want to:
• Review any step?
• Try a similar problem?
• Create flashcards from this?
```

---

### Workflow 3: Progreso (sin subagente necesario)

**Usuario dice:** "/progress"

**Yo hago:**

```python
# Leo directamente (tarea simple, no necesita subagente)
state = read_json("state/learning_state.json")
history = read_jsonl("state/session_history.jsonl")

# Analizo y presento
analyze_and_present_progress(state, history)
```

**No lanzo subagente porque:**
- Tarea simple
- Solo lectura y análisis
- No requiere herramientas complejas
- Más rápido hacerlo yo directamente

---

### Workflow 4: Múltiples Derivaciones en Paralelo

**Usuario dice:** "Deriva AM, FM y Shannon-Hartley"

**Yo hago:**

```python
# Lanzo 3 subagentes EN PARALELO
tasks = [
    Task(subagent_type="general-purpose",
         description="Derive AM",
         prompt="Derive AM formula..."),

    Task(subagent_type="general-purpose",
         description="Derive FM",
         prompt="Derive FM and Carson's rule..."),

    Task(subagent_type="general-purpose",
         description="Derive Shannon-Hartley",
         prompt="Derive channel capacity theorem...")
]

# Los 3 corren simultáneamente
# Más rápido que secuencial
```

**Resultado:**
```
✅ 3 Derivations Complete!

📄 Files created:
1. outputs/derivations/AM_20251115.md
2. outputs/derivations/FM_Carson_20251115.md
3. outputs/derivations/Shannon_Hartley_20251115.md

⏱️ Completed in parallel (faster!)

📚 Ready to study. Open any file to review.
```

---

### Workflow 5: Explorar Ejercicios Disponibles

**Usuario dice:** "¿Qué ejercicios tengo?"

**Yo hago:**

```python
Task(
    subagent_type="Explore",
    description="Find all exercises",
    prompt="""
    Find all exercise files in the docs/ directory.

    Look for:
    - Files with 'ejercicio' or 'exercise' in name
    - .txt files with problem statements
    - Any PDF with exercises

    For each file found:
    - Read first few lines to get title
    - Identify problem type (noise, modulation, etc.)
    - Note difficulty if evident

    Return: Organized list by topic
    """
)
```

**Subagente explora y retorna:**
```
📝 Exercises Found:

**Noise Problems:**
1. docs/ejercicio_ruido.txt - Noise figure and cascade (Medium)
2. docs/noise_temperature_problem.txt - Temperature calculations (Easy)

**Modulation:**
3. docs/ejercicio_AM.txt - AM bandwidth and power (Easy)
4. docs/fm_carson_problem.txt - FM spectrum (Medium)

**Information Theory:**
5. docs/shannon_capacity.txt - Channel capacity (Hard)

**Mixed:**
6. docs/exam_2024_partial.txt - Exam with 4 problems (Hard)
```

---

## 🎯 Cuándo Usar Subagentes vs Hacerlo Yo

### ✅ USA SUBAGENTE (Task tool) cuando:

- [ ] Tarea requiere múltiples pasos complejos
- [ ] Necesita acceso a herramientas (Write, Bash, etc.)
- [ ] Generación de contenido extenso (derivaciones, soluciones)
- [ ] Exploración de archivos/codebase
- [ ] Tareas que pueden correr en paralelo
- [ ] Análisis que requiere lectura de múltiples archivos

### ❌ NO uses subagente (hazlo directamente) cuando:

- [ ] Tarea es trivial (leer 1 archivo)
- [ ] Solo presentar datos existentes
- [ ] Conversación/explicación simple
- [ ] Responder pregunta rápida
- [ ] Clarificación o aclaración

---

## 💡 Ejemplos de Comandos del Usuario

### Derivaciones

```
"Deriva AM desde primeros principios"
"Derive Friis cascade formula with detailed steps"
"Quiero entender Shannon-Hartley, derivalo completo"
"Derive FM bandwidth using Carson's rule"
```

→ Lanzo `general-purpose` subagent para derivar

---

### Ejercicios

```
"Resuelve docs/ejercicio_ruido.txt"
"Solve the AM problem step by step"
"Help me with this exercise: [pasted text]"
```

→ Lanzo `general-purpose` subagent para resolver

---

### Exploración

```
"¿Qué ejercicios tengo disponibles?"
"Find all noise-related problems"
"Show me derivations I've already done"
```

→ Lanzo `Explore` subagent con thoroughness según complejidad

---

### Planificación

```
"Create a 30-day study plan for the exam"
"How should I structure my review of Unit 7?"
"Design a practice schedule for this week"
```

→ Lanzo `Plan` subagent

---

### Progreso/Estado (directo, sin subagente)

```
"/progress"
"How am I doing?"
"Show my stats"
```

→ Leo archivos directamente y analizo

---

## 🔄 Flujo Completo de Sesión de Estudio

```
Usuario: "Start study session"
Yo: [Leo state, creo current_session.json, muestro contexto]

Usuario: "Deriva AM y FM"
Yo: [Lanzo 2 subagentes en paralelo]
Subagentes: [Generan derivaciones, guardan archivos]
Yo: [Presento resúmenes, actualizo sesión]

Usuario: "Resuelve ejercicio_ruido.txt"
Yo: [Lanzo subagente para resolver]
Subagente: [Resuelve paso a paso, guarda solución]
Yo: [Muestro respuestas, actualizo progreso]

Usuario: "¿Cómo voy?"
Yo: [Leo state directamente, analizo, presento reporte]

Usuario: "End session"
Yo: [Calculo métricas, actualizo state, guardo log]
```

---

## 🚀 Ventajas de Subagentes

### 1. Paralelización
```python
# Secuencial (lento): 3 × 2min = 6min
derive_AM()  # 2 min
derive_FM()  # 2 min
derive_Shannon()  # 2 min

# Paralelo (rápido): max(2min, 2min, 2min) = 2min
Task(derive_AM) | Task(derive_FM) | Task(derive_Shannon)
```

### 2. Contexto Fresco
Cada subagente tiene su propio contexto, no contamina mi memoria

### 3. Especialización
Puedo elegir el tipo de subagente óptimo para cada tarea

### 4. Herramientas Completas
Subagentes tienen acceso a todas las herramientas necesarias

### 5. Autonomía
Una vez lanzado, el subagente trabaja solo hasta completar

---

## 📋 Actualización del Sistema

### Lo que YA funcionaba (slash commands):
- Buenos como interfaz rápida
- Útiles para tareas simples
- Pero limitados en poder

### Lo que AHORA tenemos (subagentes):
- **Derivaciones:** Task tool con general-purpose
- **Ejercicios:** Task tool con general-purpose
- **Exploración:** Task tool con Explore
- **Planificación:** Task tool con Plan
- **Progreso:** Directo (no requiere subagente)

### Híbrido (mejor approach):
```
Usuario escribe: /derive AM
    ↓
Yo interpreto y lanzo subagente apropiado
    ↓
Mantengo la simplicidad de la interfaz
    ↓
Pero con el poder de los subagentes
```

---

## 🎓 Conclusión

**Sistema Original (Python CLI):** ❌ Hardcoded, sin IA

**Sistema con Slash Commands:** ⚠️ Usa Claude, pero no subagentes

**Sistema con Subagentes:** ✅ **CORRECTO** - Usa Task tool con agentes especializados

**Este es el sistema que querías desde el inicio.** 🎯

---

**Próximo paso:** ¿Quieres que derive algo con subagentes ahora mismo para ver el poder completo?
