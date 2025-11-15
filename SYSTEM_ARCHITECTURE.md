# Sistema de Aprendizaje Multi-Agente para Sistemas de Comunicaciones

> **Autor:** Rodrigo  
> **Institución:** UTN - Universidad Tecnológica Nacional  
> **Asignatura:** Sistemas de Comunicaciones  
> **Examen Final:** 24 de Abril, 2025  
> **Fecha de Diseño:** 15 de Noviembre, 2025  
> **Conversación Original:** Claude.ai Project - Sistemas de Comunicaciones  

---

## 📖 Tabla de Contenidos

1. [Contexto y Motivación](#1-contexto-y-motivación)
2. [Arquitectura del Sistema](#2-arquitectura-del-sistema)
3. [Agentes Especializados](#3-agentes-especializados)
4. [Estructura de Archivos](#4-estructura-de-archivos)
5. [Gestión de Estado y Colaboración](#5-gestión-de-estado-y-colaboración)
6. [Integración con Anki](#6-integración-con-anki)
7. [Flujo de Trabajo](#7-flujo-de-trabajo)
8. [Comandos CLI](#8-comandos-cli)
9. [Plan de Implementación](#9-plan-de-implementación)
10. [Casos de Uso](#10-casos-de-uso)
11. [Consideraciones Técnicas](#11-consideraciones-técnicas)

---

## 1. Contexto y Motivación

### 1.1 Perfil del Usuario

**Rodrigo** es estudiante de Ingeniería en Comunicaciones en la UTN, preparándose para su examen final de Sistemas de Comunicaciones. Su enfoque de aprendizaje se caracteriza por:

- **Comprensión profunda sobre memorización**: Busca derivaciones matemáticas desde primeros principios
- **Cuestionamiento activo**: Identifica contradicciones aparentes y busca resolverlas matemáticamente
- **Integración conceptual**: Conecta conceptos entre unidades (ej: ortogonalidad temporal en QAM vs frecuencial en OFDM)
- **Uso de Anki**: Actualmente maneja un deck de 60+ tarjetas con spaced repetition
- **Análisis riguroso**: Valora tanto la elegancia matemática como las aplicaciones prácticas

### 1.2 Programa de la Asignatura

El curso abarca **10 unidades**:

1. **Introducción** - Conceptos básicos de comunicaciones
2. **Análisis de Señales** - Fourier, espectros, transformada de Hilbert
3. **Modulación Lineal** - AM, DBL, BLU, VSB
4. **Modulación Exponencial** - FM, PM, banda ancha/angosta
5. **Modulación de Pulsos** - PAM, PWM, PPM, PCM, Delta
6. **Modulación Digital** - ASK, FSK, PSK, QAM, constelaciones
7. **Ruido** - Figura de ruido, temperatura, Friis, SNR
8. **Intercomparación** - Análisis de S/N en diferentes sistemas
9. **Teoría de la Información** - Entropía, capacidad de canal, Shannon-Hartley
10. **Temas Avanzados** - Spread Spectrum, OFDM

**Referencias:**
- Programa completo: `/docs/programa_materia.md`
- Ejercicio ejemplo: `/docs/ejercicio_ruido.txt`

### 1.3 Objetivos del Sistema

Crear un entorno de aprendizaje que:

1. **Automatice tareas repetitivas**: Generación de flashcards, organización de material
2. **Facilite comprensión profunda**: Derivaciones matemáticas detalladas, simulaciones
3. **Permita colaboración**: Múltiples usuarios pueden continuar sesiones vía Git
4. **Integre con herramientas existentes**: Anki, Git, notebooks
5. **Optimice el tiempo de estudio**: Identificación de gaps, recomendaciones personalizadas

---

## 2. Arquitectura del Sistema

### 2.1 Principios de Diseño

**Principio Fundamental:**
> **El repositorio ES la fuente de verdad, NO las conversaciones de Claude**

Implicaciones:
- Todo el estado se persiste en archivos (JSON, Markdown, PDFs)
- Conversaciones de Claude Code NO se comparten entre usuarios
- El contexto se reconstruye leyendo archivos del repositorio
- Git gestiona la colaboración y el versionado

### 2.2 Componentes Principales

```
┌─────────────────────────────────────────────────────────────────┐
│                     SISTEMA DE APRENDIZAJE                      │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              COORDINATOR (Orquestador)                    │  │
│  │  - Session management                                     │  │
│  │  - Progress tracking                                      │  │
│  │  - Agent delegation                                       │  │
│  └──────────────────────────────────────────────────────────┘  │
│                             │                                   │
│        ┌────────────────────┼────────────────────┐             │
│        │                    │                    │             │
│  ┌─────▼──────┐      ┌─────▼──────┐      ┌─────▼──────┐      │
│  │ Derivation │      │  Problem   │      │  Concept   │      │
│  │   Engine   │      │   Solver   │      │   Mapper   │      │
│  └────────────┘      └────────────┘      └────────────┘      │
│        │                    │                    │             │
│  ┌─────▼──────┐      ┌─────▼──────┐      ┌─────▼──────┐      │
│  │   Anki     │      │   Signal   │      │    Exam    │      │
│  │  Factory   │      │ Simulator  │      │   Coach    │      │
│  └────────────┘      └────────────┘      └────────────┘      │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │           PERSISTENT STATE (Git Repository)              │  │
│  │  - learning_state.json                                   │  │
│  │  - session_history.jsonl                                 │  │
│  │  - user_profiles.json                                    │  │
│  │  - cards_database.json                                   │  │
│  │  - progress/ (units, concepts, problems)                 │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Agentes Especializados

### 3.1 Coordinator (`coordinator.py`)

**Rol:** Orquestador principal del sistema

**Responsabilidades:**
- Gestionar sesiones de estudio (inicio/fin)
- Mantener el estado global del aprendizaje
- Delegar tareas a agentes especializados
- Generar recomendaciones personalizadas
- Trackear progreso por unidad/concepto

**Estado que maneja:**
- `state/learning_state.json` - Estado global
- `state/session_history.jsonl` - Log de todas las sesiones
- `state/user_profiles.json` - Perfiles de usuarios
- `state/current_focus.json` - Trabajo actual

**Métodos clave:**
```python
class SessionCoordinator:
    def start_session(user: str) -> SessionContext
    def end_session(summary: str) -> SessionReport
    def build_context_from_files() -> str
    def delegate_to_agent(agent: str, task: dict) -> Result
    def update_learning_state(updates: dict) -> None
    def generate_recommendations() -> List[str]
```

**Ejemplo de uso:**
```bash
$ python main.py start-session --user rodrigo
Loading state...
✓ Last session: 2 hours ago (Unit 7 - Noise)
✓ Unit 7 progress: 85%
✓ Recommended: Continue with Friis cascade formula
✓ 12 Anki cards ready for review

Session started. What would you like to work on?
```

---

### 3.2 Derivation Engine (`derivation_engine.py`)

**Rol:** Generador de derivaciones matemáticas rigurosas

**Responsabilidades:**
- Derivar fórmulas desde primeros principios
- Generar PDFs con derivaciones completas en LaTeX
- Validar matemáticamente con SymPy
- Explicar cada paso del proceso
- Conectar derivaciones con conceptos relacionados

**Capacidades:**
- Derivaciones paso a paso con justificación de cada transición
- Identificación de asunciones implícitas
- Generación de ejemplos numéricos
- Creación automática de tarjetas Anki de la fórmula derivada

**Ejemplos de derivaciones:**
- Shannon-Hartley desde capacidad de canal
- Figura de ruido en cascada (Friis)
- Ancho de banda de FM (regla de Carson)
- Espectro de AM/FM/PM
- Probabilidad de error en QAM
- Ortogonalidad I-Q en QAM

**Métodos clave:**
```python
class DerivationEngine:
    def derive_formula(topic: str, level: str = "complete") -> Derivation
    def validate_with_sympy(steps: List[str]) -> bool
    def generate_pdf(derivation: Derivation) -> Path
    def create_anki_cards(derivation: Derivation) -> List[Card]
    def connect_to_concepts(formula: str) -> List[str]
```

**Ejemplo de uso:**
```bash
$ python main.py derive "Friis cascade noise figure"

Deriving: Friis formula for cascaded noise figure
═══════════════════════════════════════════════════

Starting from definition of noise figure:
F = (SNR_in) / (SNR_out)

Step 1: For a single amplifier...
[Derivación completa paso a paso]

✓ Derivation complete
✓ Validated with SymPy
✓ PDF generated: outputs/derivations/friis_formula_2025-11-15.pdf
✓ 3 Anki cards created

Would you like to:
1. See a numerical example
2. Derive special cases (lossy components)
3. Continue to next concept
```

---

### 3.3 Problem Solver (`problem_solver.py`)

**Rol:** Resolver ejercicios tipo examen

**Responsabilidades:**
- Parsear enunciados de problemas
- Identificar tipo de problema y conceptos involucrados
- Resolver paso a paso con justificación
- Validar unidades dimensionalmente
- Generar variaciones del problema
- Crear tarjetas Anki automáticamente

**Tipos de problemas soportados:**
- Cálculos de ruido (figura, temperatura, SNR)
- Análisis de modulaciones (potencia, BW, espectro)
- Sistemas digitales (BER, probabilidad de error)
- Capacidad de canal y teoría de información
- Múltiplex (FDM, TDM, CDMA)

**Workflow:**
1. Parse del enunciado (extracción de datos)
2. Identificación de fórmulas aplicables
3. Solución paso a paso
4. Validación dimensional
5. Interpretación de resultados
6. Generación de variaciones
7. Creación de flashcards

**Métodos clave:**
```python
class ProblemSolver:
    def parse_problem(text: str) -> Problem
    def identify_type(problem: Problem) -> ProblemType
    def solve_step_by_step(problem: Problem) -> Solution
    def validate_dimensions(solution: Solution) -> bool
    def generate_variations(problem: Problem, n: int) -> List[Problem]
    def create_anki_from_problem(solution: Solution) -> List[Card]
```

**Ejemplo de uso (ejercicio real del examen):**
```bash
$ python main.py solve /docs/ejercicio_ruido.txt

Analyzing problem...
✓ Type: Noise figure and temperature calculation
✓ Concepts: noise_figure, noise_temperature, snr, cascaded_systems
✓ Given data extracted:
  - G = 50 dB = 100,000 (linear)
  - BW = 20 kHz
  - P_n_out = 72×10^-12 W
  - η_in = 12×10^-21 W/Hz

Solving part (a): Noise figure
════════════════════════════════

Step 1: Calculate input noise power
P_n_in = η_in × BW
P_n_in = (12×10^-21 W/Hz) × (20×10^3 Hz)
P_n_in = 2.4×10^-16 W

Step 2: Apply noise figure definition
F = P_n_out / (G × P_n_in)
F = 72×10^-12 / (100,000 × 2.4×10^-16)
F = 72×10^-12 / 2.4×10^-11
F = 3 (linear) = 4.77 dB

✓ Dimensional check: [W] / ([1] × [W]) = [1] ✓

[... continúa con partes b, c, d, e ...]

Solution complete!
✓ All dimensional checks passed
✓ 8 Anki cards generated
✓ Solution PDF: outputs/solutions/ejercicio3_2025-11-15.pdf

Insights:
- F remains constant (= 3) regardless of η_in when it's thermal
- This is because F is an intrinsic amplifier property
- Watch for this trap in exam questions!
```

---

### 3.4 Concept Mapper (`concept_mapper.py`)

**Rol:** Mapear relaciones conceptuales

**Responsabilidades:**
- Crear grafos de dependencias entre conceptos
- Visualizar con mermaid o graphviz
- Identificar prerrequisitos
- Mostrar aplicaciones prácticas
- Conectar conceptos entre unidades

**Capacidades:**
- Knowledge graph de todo el programa
- Visualización interactiva
- Path finding: ¿qué necesito saber para entender X?
- Identificación de conceptos "puente"

**Métodos clave:**
```python
class ConceptMapper:
    def build_knowledge_graph() -> Graph
    def visualize_concept(concept_id: str) -> Image
    def find_prerequisites(concept_id: str) -> List[str]
    def find_applications(concept_id: str) -> List[str]
    def find_path(from_concept: str, to_concept: str) -> List[str]
    def identify_gaps(mastered: List[str]) -> List[str]
```

**Ejemplo de uso:**
```bash
$ python main.py concept "OFDM"

Analyzing concept: OFDM
════════════════════════

Prerequisites:
✓ fourier_transform (mastered)
✓ orthogonality (mastered)
✗ fft_ifft (learning)
✗ qam_modulation (weak)

Concept map:
┌─────────────────────────────────────────┐
│              OFDM                       │
│  (Orthogonal Frequency Division Mux)   │
└─────────────────────────────────────────┘
         │
         ├──► Orthogonality (frequency domain)
         │    └──► Related: QAM orthogonality (time domain)
         │
         ├──► FFT/IFFT (implementation)
         │    └──► Prerequisite: Discrete Fourier Transform
         │
         ├──► Subcarriers (QAM modulated)
         │    └──► Prerequisite: QAM constellation
         │
         └──► Cyclic Prefix
              └──► Purpose: ISI mitigation

Applications:
- WiFi (802.11a/g/n/ac)
- LTE / 5G
- DVB-T (Digital TV)
- ADSL

Related topics:
- Spread Spectrum (Unit 10)
- Channel capacity (Unit 9)
- Digital modulation (Unit 6)

Recommendation: Strengthen QAM understanding before deep-diving into OFDM
```

---

### 3.5 Anki Factory (`anki_factory.py`)

**Rol:** Gestión completa de flashcards

**Responsabilidades:**
- Generar tarjetas automáticamente desde derivaciones/problemas
- Integración con AnkiConnect API
- Parser de archivos .apkg como fallback
- Tracking de stats de revisión
- Sincronización bidireccional

**Tipos de tarjetas generadas:**
- **Definiciones**: Conceptos fundamentales
- **Fórmulas**: Con contexto de aplicación
- **Comparaciones**: AM vs FM, ASK vs FSK, etc.
- **Problemas**: Variaciones numéricas
- **Aplicaciones**: Casos reales

**Pipeline de generación:**
```
Concepto/Problema → Extracción → Template → Tarjeta Anki
                                      ↓
                              Tagging automático
                              (unit, difficulty, type)
```

**Métodos clave:**
```python
class AnkiFactory:
    def generate_from_derivation(derivation: Derivation) -> List[Card]
    def generate_from_problem(solution: Solution) -> List[Card]
    def generate_from_concept(concept: Concept) -> List[Card]
    def export_deck(cards: List[Card]) -> Path  # .apkg file
    def push_to_anki(cards: List[Card]) -> List[int]  # via AnkiConnect
```

**Ejemplo de uso:**
```bash
$ python main.py anki generate --from-problem ejercicio3.txt

Generating Anki cards...
═══════════════════════════

From problem solution:
✓ Card 1: Noise figure definition
✓ Card 2: Noise figure formula (with units)
✓ Card 3: Noise temperature conversion
✓ Card 4: SNR calculation with amplifier gain
✓ Card 5: Effect of changing input noise density
✓ Card 6: Cloze: F = P_n_out / ({{c1::G}} × P_n_in)
✓ Card 7: Problem variation (different BW)
✓ Card 8: Conceptual: Why F is independent of η_in

8 cards generated and saved to: outputs/anki/pending_import/

Push to Anki now? (requires Anki running with AnkiConnect) [y/N]: y

Connecting to Anki...
✓ AnkiConnect available
✓ 8 cards pushed to deck "Sistemas de Comunicaciones"
✓ cards_database.json updated with Anki IDs
```

---

### 3.6 Signal Simulator (`signal_simulator.py`)

**Rol:** Visualización y simulación de señales

**Responsabilidades:**
- Generar simulaciones de modulaciones
- Visualizar espectros y formas de onda
- Simulaciones Monte Carlo (BER vs SNR)
- Constelaciones digitales
- Notebooks interactivos

**Simulaciones disponibles:**
- **Modulaciones analógicas**: AM, FM, PM (espectros, formas de onda)
- **Modulaciones digitales**: ASK, FSK, PSK, QAM (constelaciones, diagramas de ojo)
- **Muestreo**: Teorema de Nyquist, aliasing
- **Ruido**: Efecto en diferentes SNR
- **Filtros**: Respuesta en frecuencia, convolución

**Métodos clave:**
```python
class SignalSimulator:
    def simulate_modulation(type: str, params: dict) -> Simulation
    def plot_spectrum(signal: Signal) -> Figure
    def plot_constellation(modulation: str, M: int, snr_db: float) -> Figure
    def monte_carlo_ber(modulation: str, snr_range: List[float]) -> Figure
    def interactive_demo(topic: str) -> NotebookPath
```

**Ejemplo de uso:**
```bash
$ python main.py sim qam --M 16 --snr 20

Simulating 16-QAM with SNR = 20 dB...
════════════════════════════════════════

✓ Constellation plot: outputs/simulations/qam16_constellation.png
✓ Eye diagram: outputs/simulations/qam16_eye.png
✓ Spectrum: outputs/simulations/qam16_spectrum.png
✓ BER vs SNR: outputs/simulations/qam16_ber_curve.png

Interactive notebook: outputs/simulations/qam16_interactive.ipynb

Key observations:
- Symbol error rate at 20 dB: 3.2×10^-4
- Bandwidth efficiency: 4 bits/symbol
- Euclidean distance between symbols: 0.632
```

---

### 3.7 Exam Coach (`exam_coach.py`)

**Rol:** Preparación para exámenes

**Responsabilidades:**
- Generar mock exams
- Simulación de examen oral
- Análisis de puntos débiles
- Sugerencias de estudio
- Tracking de preparación

**Modos de operación:**

**1. Mock Exam Generator**
```bash
$ python main.py exam --mock --units 1,2,3,7,9 --duration 120

Generating mock exam...
═══════════════════════

Duration: 120 minutes
Coverage: Units 1, 2, 3, 7, 9

PROBLEMS (70 points):
1. [25 pts] Noise analysis in 3-stage amplifier cascade
2. [25 pts] AM modulation with 80% modulation index
3. [20 pts] Channel capacity calculation

THEORY (30 points):
4. [15 pts] Explain Friis formula derivation
5. [15 pts] Compare FM vs PM advantages/disadvantages

Timer started. Good luck!
```

**2. Oral Exam Simulator**
```bash
$ python main.py exam --oral --unit 7

Oral Exam Simulation - Unit 7: Noise
══════════════════════════════════════

Question 1: What is noise figure and how is it defined?

[You respond...]

Evaluation:
✓ Correct definition of F = SNR_in / SNR_out
✓ Mentioned it's a measure of SNR degradation
✗ Didn't explain why F ≥ 1 always
⚠ Could improve: Relate to practical amplifier design

Follow-up: Why is the noise figure of the first stage most important
in a cascade?

[...]
```

**3. Weak Points Analyzer**
```bash
$ python main.py exam --analyze-weak-points

Analyzing your learning progress...
════════════════════════════════════

Weak areas identified:
🔴 OFDM orthogonality (Unit 10)
   - Only 2/8 related problems solved correctly
   - Anki cards: 40% success rate
   - Recommendation: Review FFT fundamentals first

🟡 Spread Spectrum (Unit 10)
   - Limited exposure (only 1 session)
   - Missing key concepts: PN sequences, processing gain

🟢 Noise Figure (Unit 7) - STRONG
   - 95% problem success rate
   - All Anki cards mature

Recommended study plan:
1. Strengthen FFT/DFT understanding (2-3 hours)
2. Deep-dive OFDM with simulations (4-5 hours)
3. Spread spectrum fundamentals (3-4 hours)
```

---

## 4. Estructura de Archivos

```
communications-learning-system/
│
├── agents/                           # Código de los agentes
│   ├── __init__.py
│   ├── coordinator.py                # Orquestador principal
│   ├── derivation_engine.py
│   ├── problem_solver.py
│   ├── concept_mapper.py
│   ├── anki_factory.py
│   ├── signal_simulator.py
│   └── exam_coach.py
│
├── state/                            # ⭐ ESTADO COMPARTIDO (Git)
│   ├── learning_state.json          # Estado global del aprendizaje
│   ├── session_history.jsonl        # Log de todas las sesiones
│   ├── user_profiles.json           # Perfiles de usuarios
│   └── current_focus.json           # Trabajo actual en curso
│
├── progress/                         # Tracking granular
│   ├── units/
│   │   ├── unit_01_intro.json
│   │   ├── unit_02_fourier.json
│   │   ├── unit_07_noise.json
│   │   └── ...
│   ├── concepts/
│   │   ├── noise_figure.json
│   │   ├── qam_modulation.json
│   │   ├── shannon_capacity.json
│   │   └── ...
│   └── problems/
│       ├── solved/
│       │   ├── ejercicio_ruido_001.json
│       │   └── ...
│       └── pending/
│           └── ...
│
├── knowledge/                        # Base de conocimiento
│   ├── programa_materia.json        # Programa parseado
│   ├── formulas/
│   │   ├── modulation.json
│   │   ├── noise.json
│   │   ├── information_theory.json
│   │   └── ...
│   └── derivations/
│       ├── shannon_hartley.md
│       ├── friis_formula.md
│       ├── fm_bandwidth_carson.md
│       └── ...
│
├── outputs/                          # Artefactos generados
│   ├── anki/
│   │   ├── deck_master.apkg         # Deck Anki principal
│   │   ├── cards_database.json      # Metadata de tarjetas
│   │   ├── deck_snapshot.json       # Último snapshot del .apkg
│   │   └── pending_import/          # Tarjetas para importar
│   ├── derivations/
│   │   ├── friis_formula_2025-11-15.pdf
│   │   └── ...
│   ├── solutions/
│   │   ├── ejercicio3_2025-11-15.pdf
│   │   └── ...
│   ├── simulations/
│   │   ├── qam16_constellation.png
│   │   ├── qam16_interactive.ipynb
│   │   └── ...
│   └── reports/
│       ├── weekly_progress_week8.md
│       └── ...
│
├── sessions/                         # ⭐ LOGS DE SESIONES
│   └── 2025-11/
│       ├── 2025-11-15_rodrigo_noise_analysis.md
│       ├── 2025-11-16_rodrigo_friis_derivation.md
│       ├── 2025-11-16_amigo1_unit8_review.md
│       └── ...
│
├── docs/                             # Documentación
│   ├── README.md
│   ├── SYSTEM_ARCHITECTURE.md       # Este documento
│   ├── COLLABORATION_GUIDE.md
│   ├── programa_materia.md          # Programa de la materia
│   └── ejercicio_ruido.txt          # Ejercicio ejemplo
│
├── config/
│   ├── learning_plan.yaml           # Plan de 10 semanas
│   └── agent_config.yaml            # Configuración de agentes
│
├── tests/                            # Tests unitarios
│   ├── test_coordinator.py
│   ├── test_problem_solver.py
│   └── ...
│
├── scripts/                          # Utilidades
│   ├── validate_state.py
│   ├── generate_dashboard.py
│   └── sync_anki.py
│
├── .gitignore
├── requirements.txt
├── main.py                           # CLI principal
└── README.md
```

### 4.1 Archivos Clave de Estado

#### `state/learning_state.json`

```json
{
  "metadata": {
    "last_updated": "2025-11-15T18:30:00Z",
    "primary_user": "rodrigo",
    "collaborators": ["amigo1"],
    "exam_date": "2025-04-24",
    "days_remaining": 160
  },
  
  "progress_summary": {
    "overall_completion": 0.72,
    "units_completed": [1, 2, 3, 4, 5, 6],
    "units_in_progress": [7],
    "units_pending": [8, 9, 10]
  },
  
  "current_context": {
    "active_unit": 7,
    "active_topic": "Noise in receivers",
    "last_concept_studied": "Noise temperature and figure",
    "next_recommended": "Friis formula for cascaded systems",
    "open_questions": [
      "How does Friis formula change with lossy components?",
      "Relationship between Te and F for cascades"
    ]
  },
  
  "knowledge_graph": {
    "noise_figure": {
      "status": "mastered",
      "confidence": 0.92,
      "last_reviewed": "2025-11-15",
      "dependencies_met": true,
      "related_concepts": ["noise_temperature", "snr", "friis_formula"]
    },
    "friis_formula": {
      "status": "learning",
      "confidence": 0.45,
      "next_review": "2025-11-16",
      "dependencies_met": true,
      "blockers": []
    }
  },
  
  "learning_velocity": {
    "last_7_days": {
      "concepts_learned": 12,
      "problems_solved": 8,
      "hours_studied": 18.5,
      "anki_cards_reviewed": 145
    }
  }
}
```

#### `state/user_profiles.json`

```json
{
  "rodrigo": {
    "role": "primary",
    "timezone": "America/Argentina/Buenos_Aires",
    "study_schedule": {
      "monday": ["19:00-22:00"],
      "wednesday": ["19:00-22:00"],
      "friday": ["14:00-18:00"]
    },
    "learning_style": "deep_derivations_first",
    "preferences": {
      "language": "es",
      "math_notation": "latex",
      "explanation_depth": "comprehensive"
    },
    "stats": {
      "total_sessions": 45,
      "total_hours": 87.5,
      "concepts_mastered": 58
    }
  },
  
  "amigo1": {
    "role": "collaborator",
    "learning_style": "problem_solving_focus",
    "focus_areas": ["unit_8", "unit_9"]
  }
}
```

#### `outputs/anki/cards_database.json`

```json
{
  "metadata": {
    "deck_name": "Sistemas de Comunicaciones - UTN",
    "total_cards": 87,
    "last_updated": "2025-11-15T21:30:00Z",
    "anki_deck_id": "1699234567890"
  },
  
  "cards": [
    {
      "card_id": "comm_noise_fig_001",
      "created_at": "2025-11-10T14:20:00Z",
      "created_by": "rodrigo",
      "session": "2025-11-10_rodrigo_noise",
      
      "content": {
        "front": "¿Qué es la cifra de ruido (F) de un amplificador?",
        "back": "Es la relación entre SNR a la entrada y SNR a la salida:\n\nF = (SNR_in) / (SNR_out)\n\nMide cuánto degrada el amplificador la relación señal/ruido. Siempre F ≥ 1.",
        "type": "basic",
        "tags": ["unit_7", "noise", "definition", "fundamental"]
      },
      
      "concept_mapping": {
        "unit": 7,
        "concept_id": "noise_figure",
        "difficulty": "medium",
        "prerequisites": ["snr", "amplifier_basics"],
        "relates_to": ["noise_temperature", "friis_formula"]
      },
      
      "anki_metadata": {
        "note_id": 1573456789012,
        "card_id": 1573456789013,
        "deck_id": "1699234567890",
        "model": "Basic"
      },
      
      "learning_stats": {
        "times_reviewed": 8,
        "last_reviewed": "2025-11-14T20:15:00Z",
        "ease_factor": 2.6,
        "interval_days": 25,
        "status": "mature"
      },
      
      "generation_context": {
        "source": "problem_solver",
        "trigger": "exam_exercise_3",
        "auto_generated": true,
        "reviewed_by_human": true
      }
    }
  ]
}
```

---

## 5. Gestión de Estado y Colaboración

### 5.1 Principio Fundamental

**Las conversaciones de Claude Code NO se comparten entre usuarios**, pero el **estado del aprendizaje SÍ** mediante Git.

### 5.2 Flujo de Colaboración

```
Usuario A (Rodrigo)
│
├─ git pull                    # Sincronizar
├─ start-session              # Cargar estado desde archivos
├─ [Trabajar 2 horas]
├─ end-session                # Guardar estado en archivos
├─ git commit + push          # Compartir cambios
│
└─► Usuario B (Amigo)
    │
    ├─ git pull               # Recibir cambios de A
    ├─ start-session          # Cargar estado actualizado
    ├─ [Continuar desde donde quedó A]
    └─ ...
```

### 5.3 Sesión de Usuario A (Ejemplo)

```bash
$ cd communications-learning-system
$ git pull origin main

Already up to date.

$ python main.py start-session --user rodrigo

🎯 Starting session for rodrigo...

Loading state from repository...
✓ learning_state.json loaded
✓ Session history loaded (45 previous sessions)
✓ User profile loaded

📊 Current Status:
- Overall progress: 72%
- Active unit: Unit 7 (Noise)
- Last studied: Noise figure and temperature
- Next recommended: Friis cascade formula

📚 Anki Status:
- Total cards: 87
- Due for review: 12
- New cards: 3

💡 Recommendations:
1. Continue with Friis formula derivation (high priority)
2. Review weak concept: OFDM orthogonality
3. Generate more cards for Unit 9 (Information Theory)

What would you like to work on?
> derive Friis formula

Starting Derivation Engine...
[... derivación completa ...]

✓ Derivation complete
✓ 3 Anki cards generated
✓ Session log updated

Continue working? [Y/n]: n

$ python main.py end-session

📊 Session Summary:
═══════════════════════════════════════════
Duration: 2h 15m
Completed:
- Friis formula derivation
- 3 Anki cards generated
- Unit 7 progress: 85% → 92%

Next recommended focus:
- Practice cascaded noise problems
- Review Unit 8 (System comparisons)

Session log saved to:
sessions/2025-11-15_rodrigo_friis_derivation.md

State updated in:
- learning_state.json
- progress/units/unit_07_noise.json
- progress/concepts/friis_formula.json

$ git add .
$ git commit -m "Session: Friis formula derived + Unit 7 at 92%"
$ git push origin main
```

### 5.4 Usuario B Continúa

```bash
$ git pull origin main

remote: Counting objects: 15, done.
New updates from rodrigo:
✓ Friis formula derivation complete
✓ Unit 7 progress: 92%
✓ 3 new Anki cards

$ python main.py start-session --user amigo1

🎯 Starting session for amigo1...

📰 Recent Activity:
- rodrigo completed Friis derivation 2 hours ago
- See: sessions/2025-11-15_rodrigo_friis_derivation.md

Recommendations:
1. Review rodrigo's Friis derivation
2. Solve practice problems on cascaded systems
3. Start Unit 8 (System Comparisons)

What would you like to work on?
> review last session

Opening rodrigo's session notes...
[Muestra el contenido del session log]

Would you like to:
1. Practice cascaded noise problems
2. Continue to Unit 8
3. Work on something else

> 1

Starting Problem Solver...
Generating 5 practice problems on cascaded systems...
[...]
```

### 5.5 Evitar Conflictos

**Protocolo:**
1. Siempre `git pull` antes de empezar
2. Si hay conflictos en `learning_state.json`:
   ```bash
   $ python main.py resolve-conflicts
   
   Detected conflict in learning_state.json
   
   Version A (rodrigo, 2 hours ago):
   - Unit 7 progress: 92%
   
   Version B (amigo1, 1 hour ago):
   - Unit 8 progress: 15%
   
   Auto-merging...
   ✓ Merged: Both progresses preserved
   ```

---

## 6. Integración con Anki

### 6.1 Tres Niveles de Integración

```
Nivel 1: AnkiConnect API (Ideal)
└─► Sync en vivo cuando Anki está corriendo
    - Push tarjetas nuevas automáticamente
    - Leer stats en tiempo real
    - Identificar conceptos débiles

Nivel 2: Parser .apkg (Fallback)
└─► Leer SQLite sin necesidad de Anki
    - Extraer stats del deck
    - Export a JSON

Nivel 3: Metadata JSON (Mínimo)
└─► Tracking manual
    - Usuario actualiza stats periódicamente
```

### 6.2 Clase de Integración

```python
class AnkiIntegration:
    def __init__(self, deck_path: str, db_path: str):
        self.deck_path = deck_path
        self.db_path = db_path
        self.connector = AnkiConnector()
        self.has_live = self._check_anki_running()
    
    def sync_stats(self) -> Dict:
        """Sincroniza stats usando mejor método disponible"""
        if self.has_live:
            return self.connector.sync_card_stats(self.db_path)
        elif Path(self.deck_path).exists():
            return self._parse_apkg()
        else:
            return {"status": "no_sync"}
    
    def get_learning_status(self) -> Dict:
        """Retorna status consolidado por concepto"""
        # Agrupa tarjetas por concepto
        # Determina: mastered, learning, weak
        pass
```

### 6.3 Flujo de Trabajo con Anki

```bash
# Al inicio de sesión
$ python main.py start-session --user rodrigo

📡 Syncing with Anki...
✓ AnkiConnect available
✓ 87 cards synchronized
✓ Status updated:
  - 12 cards now mature
  - 3 concepts marked as "mastered"
  - Weak concept identified: OFDM (success rate: 62%)

# Durante la sesión, generar tarjetas
$ python main.py solve ejercicio.txt

[... solución ...]

✓ 8 Anki cards generated

Push to Anki now? [Y/n]: y

✓ Connecting to AnkiConnect...
✓ 8 cards added to deck "Sistemas de Comunicaciones"
✓ cards_database.json updated

# Al final
$ python main.py anki export

Exporting deck...
✓ deck_master.apkg updated
✓ Commit changes to Git
```

---

## 7. Flujo de Trabajo

### 7.1 Sesión Típica de Estudio (3 horas)

```
┌─────────────────────────────────────────────────────────────┐
│ INICIO (10 min)                                             │
├─────────────────────────────────────────────────────────────┤
│ 1. git pull                                                 │
│ 2. python main.py start-session --user rodrigo             │
│ 3. Revisar recomendaciones                                 │
│ 4. Sincronizar Anki stats                                  │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ FASE 1: Teoría (60 min)                                     │
├─────────────────────────────────────────────────────────────┤
│ - Derivation Engine: Nueva fórmula (30 min)                │
│   → Derivación completa                                     │
│   → Validación con SymPy                                    │
│   → PDF generado                                            │
│                                                             │
│ - Concept Mapper: Conexiones (15 min)                      │
│   → Visualizar relaciones                                   │
│   → Identificar prerrequisitos                              │
│                                                             │
│ - Signal Simulator: Simulación (15 min)                    │
│   → Visualizar concepto                                     │
│   → Notebook interactivo                                    │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ FASE 2: Práctica (90 min)                                   │
├─────────────────────────────────────────────────────────────┤
│ - Problem Solver: 3-4 ejercicios                           │
│   → Solución paso a paso                                    │
│   → Validación dimensional                                  │
│   → Tarjetas Anki generadas                                 │
│                                                             │
│ - Anki Review: Tarjetas pendientes (20 min)                │
│   → Revisión en la app                                      │
│   → Stats se sincronizarán al final                         │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ FASE 3: Consolidación (40 min)                             │
├─────────────────────────────────────────────────────────────┤
│ - Revisar session log                                       │
│ - Generar tarjetas adicionales si es necesario              │
│ - Actualizar knowledge graph                                │
│ - Identificar próximos pasos                                │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ CIERRE (10 min)                                             │
├─────────────────────────────────────────────────────────────┤
│ 1. python main.py end-session                               │
│ 2. Revisar resumen                                          │
│ 3. git add . && git commit -m "..."                         │
│ 4. git push origin main                                     │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Plan de Estudio Semanal

```
SEMANA 8 (Ejemplo - 3 meses antes del examen)
═══════════════════════════════════════════════

Lunes (3h):
- Unidad 7: Completar ruido en cascadas (Friis)
- 10 problemas de práctica
- Generar 15 tarjetas Anki

Miércoles (3h):
- Unidad 8: Iniciar inter-comparación de sistemas
- Derivar S/N para modulación lineal
- Simulación: Comparar AM vs FM en ruido

Viernes (4h):
- Unidad 8: Continuar
- Mock exam: Unidades 1-7
- Analizar errores

Sábado (2h):
- Review Anki de la semana
- Weak concepts del mock exam
- Preparar siguiente semana

Total: 12 horas
```

---

## 8. Comandos CLI

### 8.1 Gestión de Sesiones

```bash
# Iniciar sesión
$ python main.py start-session --user rodrigo

# Finalizar sesión
$ python main.py end-session [--summary "texto"]

# Sincronizar estado
$ python main.py sync

# Ver progreso
$ python main.py progress [--detailed] [--unit N]

# Resolver conflictos
$ python main.py resolve-conflicts
```

### 8.2 Agentes Específicos

```bash
# Derivation Engine
$ python main.py derive "Shannon-Hartley equation"
$ python main.py derive "FM bandwidth Carson" --level detailed

# Problem Solver
$ python main.py solve ejercicio.txt
$ python main.py solve --type noise --generate 5  # Generar 5 problemas

# Concept Mapper
$ python main.py concept "OFDM"
$ python main.py concept --map-all  # Grafo completo
$ python main.py concept --path-from "fourier" --to "ofdm"

# Signal Simulator
$ python main.py sim qam --M 16 --snr 20
$ python main.py sim am --modulation-index 0.8
$ python main.py sim --interactive  # Notebook

# Exam Coach
$ python main.py exam --mock --units 1,2,7
$ python main.py exam --oral --unit 7
$ python main.py exam --analyze-weak-points
```

### 8.3 Integración con Anki

```bash
# Sincronizar stats
$ python main.py anki sync

# Generar tarjetas
$ python main.py anki generate --from-problem ejercicio.txt
$ python main.py anki generate --from-derivation friis
$ python main.py anki generate --from-unit 7 --count 20

# Push a Anki (requiere AnkiConnect)
$ python main.py anki push

# Exportar deck
$ python main.py anki export [--output deck.apkg]

# Analizar weak concepts
$ python main.py anki analyze
```

### 8.4 Utilidades

```bash
# Dashboard HTML
$ python main.py dashboard [--port 8000]

# Generar reporte
$ python main.py report --weekly
$ python main.py report --unit 7

# Backup
$ python main.py backup [--destination path]

# Limpiar outputs antiguos
$ python main.py clean --older-than 30d
```

---

## 9. Plan de Implementación

### 9.1 Fase 1: Fundación (Semana 1) ⭐ CRÍTICO

**Objetivos:**
- Estructura de directorios funcional
- Estado persistente básico
- Coordinator operativo
- CLI funcional

**Tareas:**
```bash
# Día 1-2: Setup
[ ] Crear estructura de directorios
[ ] Implementar learning_state.json schema
[ ] Implementar user_profiles.json schema
[ ] Git repo inicializado

# Día 3-4: Coordinator
[ ] coordinator.py básico
    [ ] start_session()
    [ ] end_session()
    [ ] build_context_from_files()
    [ ] update_learning_state()

# Día 5-7: CLI
[ ] main.py con argparse
    [ ] Comandos básicos: start-session, end-session
    [ ] Comando: progress
    [ ] Comando: sync
[ ] Tests básicos
[ ] Documentación README
```

**Criterio de éxito:**
```bash
$ python main.py start-session --user rodrigo
✓ Session started successfully

$ python main.py progress
✓ Shows current progress

$ python main.py end-session
✓ Session saved to sessions/
✓ learning_state.json updated
```

---

### 9.2 Fase 2: Agentes Core (Semana 2-3)

**Prioridad A: Problem Solver**

```bash
# Día 8-10: Problem Solver básico
[ ] problem_solver.py
    [ ] parse_problem() - Extracción de datos
    [ ] identify_type() - Tipo de problema
    [ ] solve_step_by_step() - Solución
    [ ] validate_dimensions() - Validación

[ ] Resolver ejercicio de ruido del examen
    [ ] Parsing completo
    [ ] Solución de las 5 partes
    [ ] PDF con solución
    [ ] Validación dimensional

[ ] CLI integration
    [ ] python main.py solve ejercicio.txt
```

**Prioridad B: Derivation Engine**

```bash
# Día 11-14: Derivation Engine
[ ] derivation_engine.py
    [ ] derive_formula() - Core
    [ ] validate_with_sympy() - Validación
    [ ] generate_latex() - Formato
    [ ] generate_pdf() - Output

[ ] Implementar 3 derivaciones clave:
    [ ] Friis formula
    [ ] Shannon-Hartley
    [ ] FM bandwidth (Carson)

[ ] CLI integration
    [ ] python main.py derive "formula"
```

---

### 9.3 Fase 3: Anki Integration (Semana 4)

```bash
# Día 15-17: Anki Factory
[ ] anki_factory.py
    [ ] generate_from_problem()
    [ ] generate_from_derivation()
    [ ] export_deck() - Genera .apkg

[ ] AnkiConnect integration
    [ ] anki_connector.py
    [ ] _invoke() - API calls
    [ ] sync_card_stats()
    [ ] push_to_anki()

# Día 18-21: Anki Parser (fallback)
[ ] anki_parser.py
    [ ] Parse .apkg → SQLite
    [ ] Extract card stats
    [ ] Export to JSON

[ ] Integración con Coordinator
    [ ] Sync al inicio de sesión
    [ ] Update cards_database.json
    [ ] Identify weak concepts
```

---

### 9.4 Fase 4: Agentes Avanzados (Semana 5-7)

**Concept Mapper:**
```bash
[ ] concept_mapper.py
    [ ] build_knowledge_graph()
    [ ] visualize_with_mermaid()
    [ ] find_prerequisites()
    [ ] identify_gaps()
```

**Signal Simulator:**
```bash
[ ] signal_simulator.py
    [ ] simulate_modulation()
    [ ] plot_spectrum()
    [ ] plot_constellation()
    [ ] generate_notebook()
```

**Exam Coach:**
```bash
[ ] exam_coach.py
    [ ] generate_mock_exam()
    [ ] simulate_oral_exam()
    [ ] analyze_weak_points()
```

---

### 9.5 Fase 5: Refinamiento (Semana 8+)

```bash
[ ] Dashboard web
[ ] Tests comprehensivos
[ ] Documentación completa
[ ] Optimizaciones de performance
[ ] Integración CI/CD
[ ] Deployment guide
```

---

## 10. Casos de Uso

### 10.1 Caso 1: Resolver Ejercicio del Examen

**Input:**
```bash
$ python main.py solve /docs/ejercicio_ruido.txt
```

**Proceso:**
1. Problem Solver parsea el enunciado
2. Identifica: problema de ruido (figura, temperatura, SNR)
3. Extrae datos: G=50dB, BW=20kHz, etc.
4. Resuelve las 5 partes paso a paso
5. Valida dimensionalmente cada resultado
6. Genera PDF con solución completa
7. Crea 8 tarjetas Anki automáticamente

**Output:**
- `outputs/solutions/ejercicio_ruido_2025-11-15.pdf`
- `outputs/anki/pending_import/noise_exercise_cards.apkg`
- Session log actualizado
- Progress tracking actualizado

---

### 10.2 Caso 2: Derivar Fórmula Desde Cero

**Input:**
```bash
$ python main.py derive "Friis cascade noise figure"
```

**Proceso:**
1. Derivation Engine identifica conceptos involucrados
2. Comienza desde F = SNR_in / SNR_out
3. Expande para un amplificador
4. Generaliza para N amplificadores en cascada
5. Simplifica y obtiene expresión final
6. Valida con SymPy
7. Genera PDF con LaTeX
8. Crea tarjetas Anki de la fórmula

**Output:**
- `outputs/derivations/friis_formula_2025-11-15.pdf`
- 3 tarjetas Anki (definición, fórmula, aplicación)
- Knowledge graph actualizado

---

### 10.3 Caso 3: Sesión Colaborativa

**Rodrigo (Día 1):**
```bash
$ git pull
$ python main.py start-session --user rodrigo
$ python main.py derive "Shannon-Hartley"
$ python main.py end-session
$ git commit -m "Derived Shannon-Hartley" && git push
```

**Amigo (Día 1, 3 horas después):**
```bash
$ git pull  # Recibe derivación de Rodrigo
$ python main.py start-session --user amigo1

New updates:
✓ rodrigo completed Shannon-Hartley derivation

$ python main.py solve --type information_theory --generate 5
# Resuelve 5 problemas usando la derivación
$ git commit -m "Practice problems on channel capacity" && git push
```

**Rodrigo (Día 2):**
```bash
$ git pull  # Recibe práctica de amigo
$ python main.py start-session --user rodrigo

New updates:
✓ amigo1 solved 5 channel capacity problems

$ python main.py review-session 2025-11-15_amigo1
# Revisa el trabajo del amigo
# Continúa desde ahí
```

---

### 10.4 Caso 4: Preparación Intensiva Pre-Examen

**2 semanas antes del examen:**

```bash
# Día 1: Identificar gaps
$ python main.py exam --analyze-weak-points

Weak areas:
🔴 OFDM orthogonality
🟡 Spread Spectrum

# Día 2-5: Reforzar OFDM
$ python main.py concept "OFDM" --deep-dive
$ python main.py derive "OFDM subcarrier orthogonality"
$ python main.py sim ofdm --subcarriers 64
$ python main.py solve --type ofdm --generate 10

# Día 6: Mock exam 1
$ python main.py exam --mock --all-units --duration 180
[Resultados: 75/100]

# Día 7-9: Reforzar errores del mock
[Análisis de errores → estudio dirigido]

# Día 10: Mock exam 2
$ python main.py exam --mock --all-units
[Resultados: 88/100]

# Día 11-13: Simulación oral
$ python main.py exam --oral [todas las unidades]

# Día 14: Review final
$ python main.py anki sync
$ python main.py progress --detailed
# Repaso de tarjetas críticas
```

---

## 11. Consideraciones Técnicas

### 11.1 Dependencias

**requirements.txt:**
```txt
# Core
numpy>=1.24.0
scipy>=1.10.0
sympy>=1.12

# Visualización
matplotlib>=3.7.0
seaborn>=0.12.0

# Anki
genanki>=0.13.0  # Generar .apkg
requests>=2.31.0  # AnkiConnect

# Concept mapping
graphviz>=0.20.0
networkx>=3.1

# Notebooks
jupyter>=1.0.0
ipywidgets>=8.0.0

# Utilidades
pyyaml>=6.0
python-dateutil>=2.8.0
click>=8.1.0  # CLI framework
rich>=13.0.0  # Terminal formatting

# PDF generation
reportlab>=4.0.0
pypdf>=3.0.0

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0
```

### 11.2 Validación Matemática

**SymPy para derivaciones:**
```python
from sympy import symbols, simplify, expand, latex

def validate_derivation(start, steps, end):
    """Valida que una derivación sea correcta"""
    expr = start
    for step in steps:
        expr = step(expr)
        if not simplify(expr - end) == 0:
            return False, f"Error at step {steps.index(step)}"
    return True, "Valid"
```

### 11.3 Testing

**Estructura de tests:**
```python
tests/
├── test_coordinator.py
│   └── test_session_management()
│   └── test_state_persistence()
│
├── test_problem_solver.py
│   └── test_noise_problem()
│   └── test_dimensional_validation()
│
├── test_derivation_engine.py
│   └── test_friis_derivation()
│   └── test_sympy_validation()
│
└── test_anki_integration.py
    └── test_ankiconnect()
    └── test_apkg_parser()
```

### 11.4 Performance

**Optimizaciones:**
- Cache de derivaciones comunes
- Lazy loading de knowledge graph
- Incremental updates en JSON files
- Batch operations para Anki

### 11.5 Seguridad

**Consideraciones:**
- NO guardar API keys en Git
- `.gitignore` para datos sensibles
- Validación de inputs en todos los agentes
- Sanitización de LaTeX injection

---

## 12. Próximos Pasos Inmediatos

### Para Comenzar la Implementación:

**1. Setup Inicial (5 minutos):**
```bash
mkdir ~/communications-learning-system
cd ~/communications-learning-system
git init
mkdir -p {agents,state,progress,knowledge,outputs,sessions,docs,config,tests,scripts}
```

**2. Copiar este documento:**
```bash
# Guardar este archivo como:
docs/SYSTEM_ARCHITECTURE.md
```

**3. Copiar materiales del curso:**
```bash
cp /mnt/project/Programa_de_la_materia docs/programa_materia.md
cp /mnt/project/Examen_final__24_04_2025___Ejercicio_3 docs/ejercicio_ruido.txt
```

**4. Crear requirements.txt** (ver sección 11.1)

**5. Iniciar con Claude Code:**
```bash
claude-code
```

**Prompt inicial para Claude Code:**
```
I need to implement the multi-agent learning system documented in:
/docs/SYSTEM_ARCHITECTURE.md

Please read that file first to understand the complete architecture.

Then, let's start with Phase 1 implementation:
1. Create learning_state.json schema
2. Implement basic coordinator.py
3. Build CLI in main.py

The goal is to have a working session management system where I can:
- Start/end sessions
- Track progress
- Persist state to Git

Let's begin!
```

---

## 13. Referencias

### Documentos Clave:
- Programa de la materia: `/docs/programa_materia.md`
- Ejercicio ejemplo: `/docs/ejercicio_ruido.txt`
- Conversación original: Claude.ai Project (2025-11-15)

### Libros del Curso:
- Stremler: Introducción a los sistemas de comunicaciones
- Carlson: Sistemas de Comunicación
- Tomasi: Sistemas de Comunicaciones Electrónicas
- Haykin: Sistemas de Comunicaciones

### Recursos Externos:
- AnkiConnect API: https://foosoft.net/projects/anki-connect/
- SymPy Documentation: https://docs.sympy.org/
- Matplotlib Gallery: https://matplotlib.org/stable/gallery/

---

**Fin del documento de arquitectura**

Este documento debe servir como referencia completa para la implementación del sistema. Cualquier usuario de Claude Code puede leer este archivo y comenzar a trabajar inmediatamente en el proyecto.

**Última actualización:** 2025-11-15  
**Versión:** 1.0  
**Autor:** Rodrigo (con asistencia de Claude Sonnet 4.5)
