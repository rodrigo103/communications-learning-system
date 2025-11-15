# 🚀 Quick Start Guide para Claude Code

## Para el Usuario Humano

### Paso 1: Setup Inicial (5 minutos)

```bash
# 1. Crear el proyecto
mkdir ~/communications-learning-system
cd ~/communications-learning-system

# 2. Inicializar Git
git init

# 3. Crear estructura de directorios
mkdir -p agents state progress/{units,concepts,problems/{solved,pending}} \
         knowledge/{formulas,derivations} \
         outputs/{anki,derivations,solutions,simulations,reports} \
         sessions docs config tests scripts

# 4. Copiar archivos desde /tmp/
cp /tmp/SYSTEM_ARCHITECTURE.md docs/
cp /tmp/README.md .
cp /tmp/main.py .
cp /tmp/coordinator.py agents/
cp /tmp/learning_state_schema.json state/learning_state.json

# 5. Copiar materiales del curso
cp /mnt/project/Programa_de_la_materia docs/programa_materia.md
cp "/mnt/project/Examen_final__24_04_2025___Ejercicio_3. Ruido [2,5 puntos]" docs/ejercicio_ruido.txt

# 6. Crear requirements.txt
cat > requirements.txt << 'EOF'
# Core
numpy>=1.24.0
scipy>=1.10.0
sympy>=1.12

# CLI
click>=8.1.0
rich>=13.0.0

# Visualización
matplotlib>=3.7.0

# Anki
genanki>=0.13.0
requests>=2.31.0

# Utilidades
pyyaml>=6.0
python-dateutil>=2.8.0
EOF

# 7. Instalar dependencias
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 8. Commit inicial
git add .
git commit -m "Initial commit: System architecture and foundation"

# 9. (Opcional) Subir a GitHub
# git remote add origin https://github.com/tu-usuario/communications-learning.git
# git push -u origin main
```

### Paso 2: Iniciar Claude Code

```bash
# Desde el directorio del proyecto
claude-code
```

---

## Para Claude Code

### Contexto Inmediato

Acabas de ser invocado en un proyecto de sistema de aprendizaje multi-agente para Sistemas de Comunicaciones. Tu trabajo es implementar este sistema.

### Archivos Clave que Debes Leer PRIMERO

1. **`/docs/SYSTEM_ARCHITECTURE.md`** ⭐⭐⭐ LEER PRIMERO
   - Contiene la arquitectura completa del sistema
   - Diseño de 7 agentes especializados
   - Plan de implementación por fases
   - Casos de uso detallados

2. **`/docs/programa_materia.md`**
   - Programa de la asignatura (10 unidades)
   - Contenidos específicos

3. **`/docs/ejercicio_ruido.txt`**
   - Ejercicio ejemplo del examen final
   - Servirá para testear el Problem Solver

### Estado Actual del Proyecto

```
✅ Estructura de directorios creada
✅ Sistema de archivos definido
✅ CLI básico implementado (main.py)
✅ Coordinator esqueleto creado (agents/coordinator.py)
✅ Schema de learning_state.json definido

⏳ TODO: Implementar funcionalidad de los agentes
⏳ TODO: Testing
⏳ TODO: Integración completa
```

### Tu Primera Tarea: Completar Coordinator (Fase 1)

El usuario está en **Fase 1** del plan de implementación. Necesitas:

#### 1. Completar `agents/coordinator.py`

Los métodos que necesitan implementación completa (marcados con `# TODO`):

```python
# En coordinator.py:

def _create_default_learning_state(self):
    """Crear estructura completa basada en programa de la materia"""
    # TODO: Parsear docs/programa_materia.md
    # TODO: Crear estructura de 10 unidades con conceptos
    pass

def build_context_from_files(self, state, user_profile):
    """Reconstruir contexto completo desde archivos"""
    # TODO: Cargar últimas sesiones
    # TODO: Analizar progreso
    # TODO: Generar recomendaciones
    pass

def _generate_recommendations(self, state, user_profile):
    """Generar recomendaciones inteligentes"""
    # TODO: Basado en progreso actual
    # TODO: Basado en fecha de examen
    # TODO: Basado en conceptos débiles
    pass

def _format_* methods():
    """Formatear contenido para session logs en Markdown"""
    # TODO: Implementar formateo de cada sección
    pass
```

#### 2. Hacer que el CLI funcione end-to-end

**Test básico que debe funcionar:**

```bash
# Usuario puede:
$ python main.py start-session --user rodrigo
# ↓ Debe mostrar contexto completo

$ python main.py progress
# ↓ Debe mostrar estado de las 10 unidades

$ python main.py end-session --summary "Test session"
# ↓ Debe generar session log en sessions/
# ↓ Debe actualizar learning_state.json
```

#### 3. Crear tests básicos

En `tests/test_coordinator.py`:

```python
def test_start_session():
    """Test que se puede iniciar sesión"""
    pass

def test_end_session():
    """Test que se guarda session log"""
    pass

def test_state_persistence():
    """Test que el estado persiste correctamente"""
    pass
```

### Enfoque de Implementación

1. **Lee la arquitectura completa** en `docs/SYSTEM_ARCHITECTURE.md`
2. **Completa el Coordinator** para que sea funcional
3. **Haz que el CLI funcione** con comandos básicos
4. **Testea** que el ciclo start-session → end-session funciona
5. **Documenta** cualquier decisión de diseño

### Criterio de Éxito para Fase 1

```bash
# Este workflow completo debe funcionar:

$ python main.py start-session --user rodrigo
✓ Session started
✓ Estado cargado desde learning_state.json
✓ Contexto mostrado (10 unidades, progreso 0%)

$ python main.py progress
✓ Muestra todas las unidades
✓ Progreso general: 0%

$ python main.py end-session --summary "Initial test"
✓ Session log guardado en sessions/2025-11/
✓ learning_state.json actualizado
✓ session_history.jsonl actualizado

$ git status
✓ Archivos modificados: learning_state.json, session_history.jsonl
✓ Nuevo archivo: sessions/2025-11/2025-11-15_rodrigo_session.md
```

### Después de Fase 1

Una vez que el Coordinator funcione, preguntarás al usuario qué implementar a continuación:
- **Fase 2a**: Problem Solver (para resolver ejercicio de ruido)
- **Fase 2b**: Derivation Engine (para derivar fórmulas)
- **Fase 3**: Anki Integration

### Notas Importantes

⚠️ **NO uses memoria de conversaciones anteriores** - Todo el contexto debe venir de archivos en el repo.

⚠️ **Mantén la compatibilidad con Git** - Cualquier usuario debe poder hacer `git pull` y continuar el trabajo.

⚠️ **Escribe código limpio y documentado** - Otros desarrolladores (y el usuario) leerán tu código.

⚠️ **Implementa incrementalmente** - No intentes hacer todo de una vez. Haz que cada pieza funcione antes de continuar.

### Recursos

- Arquitectura completa: `docs/SYSTEM_ARCHITECTURE.md`
- Programa del curso: `docs/programa_materia.md`
- Ejercicio ejemplo: `docs/ejercicio_ruido.txt`
- Schema del estado: `state/learning_state.json`

### Comando para Verificar tu Trabajo

```bash
# Antes de considerar Fase 1 completa, ejecuta:
python -m pytest tests/test_coordinator.py -v
python main.py start-session --user test_user
python main.py progress
python main.py end-session
```

---

## Prompt Sugerido para Iniciar

Cuando el usuario inicie Claude Code, puede decir:

```
Hi! I need you to implement Phase 1 of the communications learning system.

Please:
1. Read /docs/SYSTEM_ARCHITECTURE.md (complete architecture)
2. Read /docs/programa_materia.md (course curriculum)
3. Complete the implementation of agents/coordinator.py
4. Make the CLI in main.py fully functional for basic session management
5. Create basic tests in tests/test_coordinator.py

The goal is to have a working session management system where I can:
- Start/end sessions
- Track progress across 10 course units
- Persist state to Git for multi-user collaboration

Let's start by confirming you've read and understood the architecture.
```

---

## Checklist de Implementación

### Fase 1: Fundación
- [ ] Coordinator: `_create_default_learning_state()` implementado
- [ ] Coordinator: `build_context_from_files()` implementado
- [ ] Coordinator: `_generate_recommendations()` implementado
- [ ] Coordinator: Session log formatting implementado
- [ ] CLI: `start-session` funcional
- [ ] CLI: `end-session` funcional
- [ ] CLI: `progress` funcional
- [ ] Tests: test_coordinator.py con 3+ tests
- [ ] Documentación: README actualizado si es necesario

### Fase 2a: Problem Solver (próximo)
- [ ] `agents/problem_solver.py` creado
- [ ] Resolver ejercicio de ruido completamente
- [ ] Integración con CLI
- [ ] Tests

### Fase 2b: Derivation Engine (próximo)
- [ ] `agents/derivation_engine.py` creado
- [ ] Derivar Friis formula como prueba
- [ ] Integración con CLI
- [ ] Tests

---

¡Listo para comenzar la implementación! 🚀
