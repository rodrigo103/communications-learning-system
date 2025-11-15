# 🎓 Sistema de Aprendizaje Multi-Agente - Sistemas de Comunicaciones

> **Sistema inteligente para preparación del examen final de Sistemas de Comunicaciones (UTN)**

## 🚀 Quick Start

```bash
# 1. Clonar/crear el repositorio
git clone [tu-repo] communications-learning-system
cd communications-learning-system

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Iniciar sesión de estudio
python main.py start-session --user rodrigo

# 4. Trabajar con los agentes
python main.py derive "Shannon-Hartley equation"
python main.py solve ejercicio.txt
python main.py sim qam --M 16

# 5. Finalizar y guardar
python main.py end-session
git add . && git commit -m "Session: ..." && git push
```

## 📚 ¿Qué es esto?

Un sistema de aprendizaje impulsado por IA con **7 agentes especializados** que te ayudan a:

- 🧮 **Derivar fórmulas** desde primeros principios
- 📝 **Resolver ejercicios** tipo examen con soluciones paso a paso
- 🗺️ **Mapear conceptos** y sus interdependencias
- 🎴 **Generar flashcards** automáticamente para Anki
- 📊 **Simular señales** y visualizar espectros
- 🎯 **Prepararte para exámenes** con mocks y análisis

## 🤖 Los Agentes

| Agente | Función | Comando |
|--------|---------|---------|
| **Coordinator** | Orquesta todo el sistema | `start-session`, `end-session` |
| **Derivation Engine** | Derivaciones matemáticas rigurosas | `derive "formula"` |
| **Problem Solver** | Resuelve ejercicios tipo examen | `solve ejercicio.txt` |
| **Concept Mapper** | Mapea relaciones conceptuales | `concept "OFDM"` |
| **Anki Factory** | Genera y gestiona flashcards | `anki generate`, `anki sync` |
| **Signal Simulator** | Simula y visualiza señales | `sim qam --M 16` |
| **Exam Coach** | Preparación para exámenes | `exam --mock` |

## 🗂️ Estructura del Proyecto

```
communications-learning-system/
├── agents/              # Código de los agentes
├── state/              # Estado compartido (Git) ⭐
│   ├── learning_state.json
│   └── session_history.jsonl
├── progress/           # Tracking por unidad/concepto
├── knowledge/          # Base de conocimiento
├── outputs/            # Artefactos generados
│   ├── anki/          # Flashcards
│   ├── derivations/   # PDFs con derivaciones
│   └── simulations/   # Gráficos y notebooks
├── sessions/          # Logs de sesiones ⭐
├── docs/              # Documentación
│   └── SYSTEM_ARCHITECTURE.md  # ⭐ Lee esto primero
└── main.py            # CLI principal
```

## 💡 Características Clave

### ✅ Colaboración Multi-Usuario
- Estado vive en Git, no en conversaciones
- Múltiples usuarios pueden continuar sesiones
- Session logs detallados

### ✅ Integración con Anki
- Generación automática de flashcards
- Sync bidireccional con AnkiConnect
- Tracking de progreso de revisión

### ✅ Comprensión Profunda
- Derivaciones matemáticas desde primeros principios
- Validación con SymPy
- Explicaciones paso a paso

### ✅ Preparación Completa
- Mock exams
- Simulación oral
- Análisis de puntos débiles

## 📖 Documentación

- **[SYSTEM_ARCHITECTURE.md](docs/SYSTEM_ARCHITECTURE.md)** - Arquitectura completa del sistema
- **[programa_materia.md](docs/programa_materia.md)** - Programa de la asignatura (10 unidades)

## 🎯 Casos de Uso

### Resolver un ejercicio del examen
```bash
$ python main.py solve /docs/ejercicio_ruido.txt

✓ Problema analizado: Noise figure y temperatura
✓ Solución paso a paso generada
✓ 8 tarjetas Anki creadas
✓ PDF guardado en: outputs/solutions/
```

### Derivar una fórmula
```bash
$ python main.py derive "Friis cascade noise figure"

✓ Derivación completa desde F = SNR_in/SNR_out
✓ Validado con SymPy
✓ PDF con LaTeX: outputs/derivations/friis_formula.pdf
✓ 3 tarjetas Anki generadas
```

### Simular una modulación
```bash
$ python main.py sim qam --M 16 --snr 20

✓ Constelación 16-QAM generada
✓ Diagrama de ojo: outputs/simulations/qam16_eye.png
✓ Curva BER vs SNR calculada
✓ Notebook interactivo creado
```

### Mock exam
```bash
$ python main.py exam --mock --units 1,2,7 --duration 120

✓ Examen generado (120 minutos)
✓ 3 problemas numéricos + 2 teóricos
✓ Cronómetro iniciado
```

## 🤝 Colaboración

Dos o más personas pueden trabajar en el mismo material:

**Usuario A:**
```bash
git pull
python main.py start-session --user rodrigo
python main.py derive "Shannon-Hartley"
python main.py end-session
git commit && git push
```

**Usuario B (continúa donde quedó A):**
```bash
git pull  # Recibe trabajo de A
python main.py start-session --user amigo1
# Ve: "rodrigo completó Shannon-Hartley hace 2 horas"
python main.py solve --type information_theory
# Continúa...
```

## 🛠️ Instalación

### Requisitos
- Python 3.9+
- Git
- (Opcional) Anki + AnkiConnect plugin

### Setup
```bash
# Clonar
git clone [tu-repo] communications-learning-system
cd communications-learning-system

# Crear virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# (Opcional) Instalar AnkiConnect
# En Anki: Tools → Add-ons → Get Add-ons → Code: 2055492159
```

## 📊 Progreso

Visualiza tu progreso en cualquier momento:

```bash
$ python main.py progress

📊 Overall Progress: 72%
═══════════════════════════════════════

Units:
✅ Unit 1: Introducción (100%)
✅ Unit 2: Análisis de Señales (100%)
✅ Unit 3: Modulación Lineal (100%)
✅ Unit 4: Modulación Exponencial (100%)
✅ Unit 5: Modulación de Pulsos (100%)
✅ Unit 6: Modulación Digital (100%)
📚 Unit 7: Ruido (92%) ← Current
⏳ Unit 8: Intercomparación (0%)
⏳ Unit 9: Teoría de la Información (0%)
⏳ Unit 10: Temas Avanzados (0%)

Concepts Mastered: 58/87
Anki Cards: 87 (23 mature, 34 young, 18 learning, 12 new)
Study Time (last 7 days): 18.5 hours

Next Recommended:
→ Practice cascaded noise problems
→ Start Unit 8: System comparisons
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_problem_solver.py

# With coverage
pytest --cov=agents tests/
```

## 🤖 Comandos Principales

```bash
# Sesiones
python main.py start-session --user <nombre>
python main.py end-session
python main.py progress

# Agentes
python main.py derive "<formula>"
python main.py solve <archivo>
python main.py concept "<concepto>"
python main.py sim <tipo> [opciones]
python main.py exam [--mock|--oral|--analyze]

# Anki
python main.py anki sync
python main.py anki generate [opciones]
python main.py anki push
python main.py anki export
```

## 📅 Plan de Estudio

Ver [docs/learning_plan.md](docs/learning_plan.md) para un plan detallado de 10 semanas.

## 🐛 Troubleshooting

### "AnkiConnect no disponible"
- Asegúrate de que Anki esté corriendo
- Verifica que AnkiConnect esté instalado
- El sistema funcionará con modo fallback (parser .apkg)

### "Conflictos en learning_state.json"
```bash
python main.py resolve-conflicts
```

### "Error al generar PDF"
```bash
pip install reportlab pypdf
```

## 📝 Licencia

MIT License - Úsalo libremente para tu estudio.

## 🙏 Créditos

Diseñado para estudiantes de Ingeniería en Comunicaciones de la UTN que valoran la comprensión profunda sobre la memorización mecánica.

---

**¿Listo para comenzar?**

```bash
python main.py start-session --user tu_nombre
```

¡Buena suerte en tu examen! 🎓✨
