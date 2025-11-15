# 📖 Guía de Uso Práctica - Sistema de Aprendizaje

> **Guía paso a paso para usar el sistema de aprendizaje**
> Fecha de examen configurada: **2025-12-15** (30 días restantes)

---

## 🎯 ¿Qué puede hacer este sistema AHORA?

### ✅ Funcionalidades Implementadas y Testeadas

El sistema tiene **3 agentes principales** completamente funcionales:

1. **📋 Coordinator** - Gestión de sesiones de estudio
2. **🧮 DerivationEngine** - Derivaciones matemáticas paso a paso
3. **📝 ProblemSolver** - Resolución de ejercicios tipo examen

---

## 🚀 Tutorial Paso a Paso

### Paso 1: Iniciar una Sesión de Estudio

Antes de trabajar, **siempre inicia una sesión**:

```bash
python main.py start-session --user rodrigo
```

**Salida esperada:**
```
✓ Session iniciada para: rodrigo
✓ Estado cargado correctamente

📊 Current Progress:
═══════════════════════════════════════
Overall: 0%
Concepts Mastered: 0/87
Problems Solved: 0
Study Hours: 0.0

📚 Current Focus:
Unit 1: Introducción a Sistemas de Comunicaciones (0%)

💡 Recommendations:
→ Start with Unit 1 fundamentals
→ ⚠️ Only 30 days until exam!
→ Begin with AM modulation derivations
```

**¿Qué hace esto?**
- Crea un archivo `state/current_session.json` que guarda tu sesión activa
- Lee el estado de aprendizaje desde `state/learning_state.json`
- Te muestra tu progreso actual y recomendaciones

---

### Paso 2: Derivar una Fórmula

Usa el **DerivationEngine** para obtener derivaciones matemáticas completas:

#### Ejemplo 1: Derivación de AM (Amplitude Modulation)

```bash
python main.py derive AM
```

**¿Qué obtienes?**
- ✅ Derivación paso a paso en la terminal
- ✅ PDF guardado en `outputs/derivations/AM_derivation_YYYYMMDD_HHMMSS.pdf`
- ✅ Tarjetas Anki en `outputs/anki/AM_derivation_YYYYMMDD_HHMMSS.apkg`
- ✅ JSON con toda la derivación en `outputs/derivations/AM_derivation_YYYYMMDD_HHMMSS.json`

**Salida esperada:**
```
═══════════════════════════════════════
Amplitude Modulation (AM) Derivation
Level: complete
═══════════════════════════════════════

Step 1: Definition of Amplitude Modulation
───────────────────────────────────────
Equation:
  s_AM(t) = A_c [1 + m(t)] cos(2πf_c t)

Explanation:
  AM works by varying the amplitude of a high-frequency carrier signal...

Step 2: Expanding the Signal
───────────────────────────────────────
Equation:
  s_AM(t) = A_c cos(2πf_c t) + A_c m(t) cos(2πf_c t)

Explanation:
  The AM signal consists of two components: carrier and modulation product...

[... más pasos ...]

Final Formula:
  s_AM(t) = A_c [1 + k_a m(t)] cos(2πf_c t)

Key Results:
• Bandwidth: BW = 2f_m (twice the message bandwidth)
• Power: P_total = P_c(1 + μ²/2) where μ is modulation index
• Modulation index: μ = k_a A_m, must be ≤ 1 to avoid distortion

✓ Saved to: outputs/derivations/AM_derivation_20251115_143022.pdf
✓ Anki deck: outputs/anki/AM_derivation_20251115_143022.apkg
✓ JSON saved: outputs/derivations/AM_derivation_20251115_143022.json
```

#### Temas Disponibles para Derivar

```bash
# Modulación
python main.py derive AM          # Amplitude Modulation
python main.py derive FM          # Frequency Modulation (Carson's rule)

# Teoría de la Información
python main.py derive Shannon-Hartley  # Channel capacity

# Ruido
python main.py derive Friis       # Cascaded noise figure

# Modulación Digital
python main.py derive QAM         # Quadrature Amplitude Modulation
```

#### Opciones Adicionales

```bash
# Con PDF
python main.py derive AM --pdf

# Con tarjetas Anki
python main.py derive AM --anki

# Ambos
python main.py derive AM --pdf --anki

# Niveles de detalle
python main.py derive AM --level basic     # Derivación simplificada
python main.py derive AM --level complete  # Derivación completa (default)
python main.py derive AM --level expert    # Máximo detalle
```

---

### Paso 3: Resolver un Ejercicio

Usa el **ProblemSolver** para resolver problemas tipo examen:

#### Ejemplo: Resolver Ejercicio de Ruido

**1. Crea un archivo con el ejercicio** (o usa el existente):

```bash
cat docs/ejercicio_ruido.txt
```

Contenido:
```
Ejercicio 3: Ruido [2.5 puntos]

Datos:
- Ganancia: G = 50 dB
- Ancho de banda: BW = 20 kHz
- Potencia de ruido a la salida: P_n_out = 72×10^-12 W
- Densidad espectral de potencia de ruido a la entrada: η_in = 12×10^-21 W/Hz

Se pide:
a) Calcular la figura de ruido F del amplificador (en dB y lineal).
b) Calcular la temperatura de ruido equivalente T_e del amplificador.
c) Si este amplificador se conecta en cascada con un segundo amplificador idéntico, calcular la figura de ruido total F_total del sistema en cascada.
d) Calcular la temperatura de ruido total del sistema en cascada T_total.
e) Si la señal de entrada tiene una potencia S_in = 1×10^-15 W, ¿cuál sería el SNR a la salida del sistema en cascada?

Constantes:
- T_0 = 290 K
- k = 1.38×10^-23 J/K
```

**2. Resuelve el ejercicio:**

```bash
python main.py solve docs/ejercicio_ruido.txt
```

**Salida esperada:**
```
═══════════════════════════════════════
Problem Analysis
═══════════════════════════════════════

Title: Ejercicio 3: Ruido [2.5 puntos]
Type: noise
Status: ✓ Solved

Given Data:
• G = 50 dB
• BW = 20000 Hz  (converted from 20 kHz)
• P_n_out = 7.2e-11 W  (converted from 72×10^-12)
• eta_in = 1.2e-20 W/Hz  (converted from 12×10^-21)

Constants:
• T_0 = 290 K
• k = 1.38e-23 J/K

═══════════════════════════════════════
Solution Part (a): Noise Figure
═══════════════════════════════════════

Step 1: Convert gain from dB to linear
  G_linear = 10^(G_dB/10) = 10^(50/10) = 100000

Step 2: Calculate input noise power
  P_n_in = η_in × BW = 1.2×10^-20 × 20000 = 2.4×10^-16 W

Step 3: Calculate noise figure
  F = P_n_out / (G × P_n_in)
  F = 7.2×10^-11 / (100000 × 2.4×10^-16)
  F = 3.0

Step 4: Convert to dB
  F_dB = 10 log₁₀(F) = 10 log₁₀(3.0) = 4.77 dB

Result:
  F_linear = 3.0
  F_dB = 4.77 dB

Validation: ✓ Dimensiones correctas

[... continúa con partes b), c), d), e) ...]

═══════════════════════════════════════
Final Answers
═══════════════════════════════════════

a) F = 3.0 (4.77 dB)
b) T_e = 580 K
c) F_total = 3.00002
d) T_total = 580.01 K
e) SNR_out = 1.39 (1.42 dB)

✓ PDF saved: outputs/solutions/ejercicio_ruido_20251115_143500.pdf
✓ Anki deck: outputs/anki/ejercicio_ruido_20251115_143500.apkg
✓ JSON saved: outputs/solutions/ejercicio_ruido_20251115_143500.json
```

#### ¿Qué hace el ProblemSolver?

1. **Parsea el enunciado** - Extrae variables, valores, unidades
2. **Convierte unidades automáticamente** - kHz→Hz, mW→W, μs→s, etc. (20 unidades soportadas)
3. **Identifica el tipo de problema** - noise, modulation, channel_capacity
4. **Resuelve paso a paso** - Con justificación matemática
5. **Valida dimensiones** - Verifica que las unidades sean correctas
6. **Genera outputs**:
   - PDF con solución completa
   - Tarjetas Anki con conceptos clave
   - JSON con todos los datos

#### Unidades Soportadas

El sistema convierte automáticamente:

**Frecuencia:** kHz, MHz, GHz → Hz
**Potencia:** mW, μW, nW, pW, dBm → W
**Tiempo:** ms, μs, ns, ps → s
**Distancia:** km, cm, mm, μm, nm → m

---

### Paso 4: Ver tu Progreso

En cualquier momento puedes ver tu progreso:

```bash
python main.py progress
```

**Salida:**
```
📊 Overall Progress: 0%
═══════════════════════════════════════

Units:
⏳ Unit 1: Introducción (0%)
⏳ Unit 2: Análisis de Señales (0%)
⏳ Unit 3: Modulación Lineal (0%)
⏳ Unit 4: Modulación Exponencial (0%)
⏳ Unit 5: Modulación de Pulsos (0%)
⏳ Unit 6: Modulación Digital (0%)
⏳ Unit 7: Ruido (0%)
⏳ Unit 8: Intercomparación (0%)
⏳ Unit 9: Teoría de la Información (0%)
⏳ Unit 10: Temas Avanzados (0%)

📈 Learning Velocity:
Sessions: 1
Study time: 0.0 hours
Concepts mastered: 0
Problems solved: 0

Next Recommended:
→ Start with Unit 1 fundamentals
→ ⚠️ Only 30 days until exam!
```

---

### Paso 5: Finalizar la Sesión

**Siempre termina tu sesión** cuando termines de estudiar:

```bash
python main.py end-session
```

**Salida:**
```
═══════════════════════════════════════
Session Report
═══════════════════════════════════════

User: rodrigo
Duration: 1.2 hours

Completed Work:
• Derived AM formula
• Solved noise exercise

Insights & Key Learnings:
• AM bandwidth is twice the message frequency
• Friis formula shows first stage dominates cascade noise

Artifacts Generated:
• PDF: outputs/derivations/AM_derivation_20251115_143022.pdf
• PDF: outputs/solutions/ejercicio_ruido_20251115_143500.pdf
• Anki: 2 decks created (15 cards total)

Next Focus:
→ Continue with FM derivation
→ Practice more noise problems

✓ Session log saved: sessions/20251115_143000_rodrigo.md
✓ Learning state updated
```

**¿Qué pasa al terminar?**
- Se guarda un log detallado en `sessions/YYYYMMDD_HHMMSS_usuario.md`
- Se actualiza `state/learning_state.json` con tu progreso
- Se añade entrada al historial en `state/session_history.jsonl`
- Se borra `state/current_session.json`

---

## 📁 Estructura de Archivos Generados

Después de usar el sistema, tendrás:

```
communications-learning-system/
├── state/
│   ├── learning_state.json      # Tu progreso general
│   ├── session_history.jsonl    # Historial de todas las sesiones
│   └── current_session.json     # Sesión activa (temporal)
│
├── sessions/
│   ├── 20251115_143000_rodrigo.md
│   └── 20251115_150000_rodrigo.md
│
├── outputs/
│   ├── derivations/
│   │   ├── AM_derivation_20251115_143022.pdf
│   │   ├── AM_derivation_20251115_143022.json
│   │   └── Shannon_Hartley_derivation_20251115_144000.pdf
│   │
│   ├── solutions/
│   │   ├── ejercicio_ruido_20251115_143500.pdf
│   │   ├── ejercicio_ruido_20251115_143500.json
│   │   └── ejercicio_AM_20251115_145000.pdf
│   │
│   └── anki/
│       ├── AM_derivation_20251115_143022.apkg
│       └── ejercicio_ruido_20251115_143500.apkg
```

---

## 🔄 Flujo de Trabajo Típico

### Sesión de Estudio Completa

```bash
# 1. Iniciar sesión
python main.py start-session --user rodrigo

# 2. Estudiar teoría - Derivar fórmulas
python main.py derive AM --pdf --anki
python main.py derive FM --pdf --anki
python main.py derive Shannon-Hartley --pdf

# 3. Practicar - Resolver ejercicios
python main.py solve docs/ejercicio_ruido.txt
python main.py solve docs/ejercicio_modulacion.txt

# 4. Revisar progreso
python main.py progress

# 5. Finalizar y guardar
python main.py end-session

# 6. Commitear a Git (opcional pero recomendado)
git add .
git commit -m "Session: Studied AM, FM, solved 2 noise problems"
git push
```

### Preparación para Examen

```bash
# Día 1-5: Teoría (Derivaciones)
python main.py start-session --user rodrigo
python main.py derive AM --pdf --anki
python main.py derive FM --pdf --anki
python main.py derive Friis --pdf --anki
python main.py derive Shannon-Hartley --pdf --anki
python main.py end-session

# Día 6-10: Práctica (Ejercicios)
python main.py start-session --user rodrigo
python main.py solve docs/ejercicio1.txt
python main.py solve docs/ejercicio2.txt
python main.py solve docs/ejercicio3.txt
python main.py end-session

# Día 11-15: Repaso con Anki
# Importa los archivos .apkg en Anki y estudia las flashcards
```

---

## 💡 Tips y Trucos

### Tip 1: Usa Git para Backup

```bash
# Después de cada sesión
git add state/ sessions/ outputs/
git commit -m "Session $(date): Studied [temas]"
git push
```

### Tip 2: Organiza tus Ejercicios

Crea una carpeta para tus ejercicios:

```bash
mkdir -p docs/ejercicios
# Crea archivos de texto con enunciados
nano docs/ejercicios/ruido_1.txt
nano docs/ejercicios/ruido_2.txt
nano docs/ejercicios/modulacion_1.txt
```

### Tip 3: Niveles de Derivación

```bash
# Primero overview rápido
python main.py derive AM --level basic

# Luego detalle completo
python main.py derive AM --level complete

# Para examen oral, máximo detalle
python main.py derive AM --level expert
```

### Tip 4: PDFs vs Anki

```bash
# Solo PDF (para imprimir y estudiar)
python main.py derive Shannon-Hartley --pdf

# Solo Anki (para repaso rápido)
python main.py derive Friis --anki

# Ambos (recomendado)
python main.py derive AM --pdf --anki
```

---

## 🎯 Qué NO está implementado (todavía)

Estos comandos aparecen en el `--help` pero **no funcionan aún**:

- ❌ `python main.py concept "OFDM"` - Mapas conceptuales
- ❌ `python main.py sim qam --M 16` - Simulaciones
- ❌ `python main.py exam --mock` - Exámenes de práctica
- ❌ `python main.py dashboard` - Dashboard web
- ❌ `python main.py anki sync` - Sync con AnkiConnect (los .apkg funcionan)

**Lo que SÍ funciona al 100%:**
- ✅ `start-session`, `end-session`
- ✅ `progress`
- ✅ `derive` (6 temas: AM, FM, Shannon-Hartley, Friis, QAM, Carson)
- ✅ `solve` (problemas de ruido completamente)

---

## ❓ Preguntas Frecuentes

### ¿Tengo que usar Anki?

No, es opcional. Si usas `--anki`, se genera un archivo `.apkg` que puedes importar en Anki. Si no lo usas, solo se generan PDFs.

### ¿Puedo resolver cualquier tipo de problema?

Actualmente, el ProblemSolver está optimizado para **problemas de ruido** (noise figure, temperatura, Friis cascade, SNR). Otros tipos de problemas (modulación, capacidad) están en desarrollo.

### ¿Qué hago con los archivos .apkg?

1. Abre Anki
2. File → Import
3. Selecciona el archivo `.apkg`
4. Las tarjetas se importarán en un nuevo deck

### ¿Puedo colaborar con alguien?

Sí, usando Git:

```bash
# Persona A
python main.py start-session --user alice
python main.py derive AM
python main.py end-session
git commit && git push

# Persona B
git pull  # Recibe trabajo de Alice
python main.py start-session --user bob
python main.py solve ejercicio_AM.txt  # Continúa con ejercicios
python main.py end-session
git commit && git push
```

### ¿Cómo cambio la fecha de examen?

Edita `learning_state_schema.json` y `state/learning_state.json`:

```json
"metadata": {
    "exam_date": "2025-12-31",  // Tu nueva fecha
    ...
}
```

---

## 🎓 Ejemplo de Sesión Real

```bash
$ python main.py start-session --user rodrigo
✓ Session iniciada para: rodrigo
💡 Recommendations:
→ ⚠️ Only 30 days until exam!

$ python main.py derive AM --pdf --anki
═══════════════════════════════════════
Amplitude Modulation (AM) Derivation
[... derivación completa ...]
✓ PDF saved: outputs/derivations/AM_derivation_20251115_143022.pdf
✓ Anki deck: outputs/anki/AM_derivation_20251115_143022.apkg

$ python main.py solve docs/ejercicio_ruido.txt
═══════════════════════════════════════
Problem Analysis
[... solución paso a paso ...]
✓ PDF saved: outputs/solutions/ejercicio_ruido_20251115_143500.pdf

$ python main.py progress
📊 Overall Progress: 8%
Concepts Mastered: 3/87
Problems Solved: 1

$ python main.py end-session
═══════════════════════════════════════
Session Report
Duration: 1.2 hours
Completed Work:
• Derived AM formula
• Solved noise exercise
✓ Session log saved

$ git add . && git commit -m "Session: AM derivation + noise exercise"
$ git push
```

---

## 📚 Próximos Pasos

1. **Empieza con derivaciones básicas**
   ```bash
   python main.py derive AM --level basic
   python main.py derive FM --level basic
   ```

2. **Practica con el ejercicio de ejemplo**
   ```bash
   python main.py solve docs/ejercicio_ruido.txt
   ```

3. **Crea tus propios ejercicios** en archivos de texto y resuélvelos

4. **Usa Anki** para repaso espaciado de conceptos

5. **Commitea a Git** regularmente para no perder tu progreso

---

**¿Listo para empezar?**

```bash
python main.py start-session --user tu_nombre
python main.py derive AM --pdf --anki
```

¡Éxito en tu examen del 2025-12-15! 🎓✨
