"""
Session Coordinator - Orquestador principal del sistema

Responsabilidades:
- Gestionar inicio/fin de sesiones
- Mantener estado global del aprendizaje
- Delegar tareas a agentes especializados
- Generar recomendaciones personalizadas
- Trackear progreso por unidad/concepto
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SessionCoordinator:
    """
    Orquestador principal del sistema de aprendizaje.
    
    Gestiona:
    - Estado global (learning_state.json)
    - Historial de sesiones (session_history.jsonl)
    - Perfiles de usuario (user_profiles.json)
    - Contexto actual (current_focus.json)
    """
    
    def __init__(self, base_path: Path = None):
        """
        Inicializar coordinator
        
        Args:
            base_path: Ruta base del proyecto (default: directorio actual)
        """
        self.base_path = base_path or Path.cwd()
        self.state_dir = self.base_path / "state"
        self.progress_dir = self.base_path / "progress"
        self.sessions_dir = self.base_path / "sessions"
        
        # Ensure directories exist
        self.state_dir.mkdir(exist_ok=True)
        self.progress_dir.mkdir(exist_ok=True)
        self.sessions_dir.mkdir(exist_ok=True)
        
        # File paths
        self.learning_state_path = self.state_dir / "learning_state.json"
        self.user_profiles_path = self.state_dir / "user_profiles.json"
        self.session_history_path = self.state_dir / "session_history.jsonl"
        self.current_focus_path = self.state_dir / "current_focus.json"
        self.current_session_path = self.state_dir / "current_session.json"

        # Current session state (will be loaded from file if exists)
        self.current_user = None
        self.session_start_time = None
        self.session_data = {}

        # Try to load active session on init
        self._load_active_session()
    
    # ========================================================================
    # STATE LOADING / SAVING
    # ========================================================================
    
    def load_learning_state(self) -> Dict:
        """
        Cargar estado global del aprendizaje
        
        Returns:
            Dict con el estado completo
        """
        if not self.learning_state_path.exists():
            logger.warning("learning_state.json not found, creating default")
            return self._create_default_learning_state()
        
        try:
            with open(self.learning_state_path, 'r', encoding='utf-8') as f:
                state = json.load(f)
            logger.info("✓ learning_state.json loaded")
            return state
        except Exception as e:
            logger.error(f"Error loading learning_state.json: {e}")
            raise
    
    def save_learning_state(self, state: Dict) -> None:
        """
        Guardar estado global del aprendizaje
        
        Args:
            state: Diccionario con el estado completo
        """
        try:
            # Update metadata
            state['metadata']['last_updated'] = datetime.now().isoformat()
            
            with open(self.learning_state_path, 'w', encoding='utf-8') as f:
                json.dump(state, f, indent=2, ensure_ascii=False)
            
            logger.info("✓ learning_state.json saved")
        except Exception as e:
            logger.error(f"Error saving learning_state.json: {e}")
            raise
    
    def _create_default_learning_state(self) -> Dict:
        """
        Crear estado inicial por defecto

        Returns:
            Dict con estructura inicial
        """
        # Load from schema file
        schema_path = self.base_path / "learning_state_schema.json"

        if schema_path.exists():
            logger.info("Loading default state from schema file")
            with open(schema_path, 'r', encoding='utf-8') as f:
                default_state = json.load(f)

            # Update timestamps and metadata
            default_state['metadata']['created_at'] = datetime.now().isoformat()
            default_state['metadata']['last_updated'] = datetime.now().isoformat()
        else:
            # Fallback: create minimal structure
            logger.warning("Schema file not found, creating minimal structure")
            default_state = {
                "metadata": {
                    "created_at": datetime.now().isoformat(),
                    "last_updated": datetime.now().isoformat(),
                    "primary_user": None,
                    "collaborators": [],
                    "exam_date": "2025-04-24",
                    "system_version": "1.0.0"
                },
                "progress_summary": {
                    "overall_completion": 0.0,
                    "units_completed": [],
                    "units_in_progress": [],
                    "units_pending": list(range(1, 11)),
                    "concepts_mastered": 0,
                    "total_concepts": 87,
                    "problems_solved": 0,
                    "total_problems": 150
                },
                "current_context": {
                    "active_unit": None,
                    "active_topic": None,
                    "last_concept_studied": None,
                    "last_session_date": None,
                    "next_recommended": "Start with Unit 1: Introducción",
                    "open_questions": [],
                    "current_focus_area": None
                },
                "units": {},
                "knowledge_graph": {},
                "learning_velocity": {
                    "last_7_days": {
                        "concepts_learned": 0,
                        "problems_solved": 0,
                        "hours_studied": 0.0,
                        "anki_cards_reviewed": 0,
                        "sessions": 0
                    },
                    "last_30_days": {
                        "concepts_learned": 0,
                        "problems_solved": 0,
                        "hours_studied": 0.0,
                        "anki_cards_reviewed": 0,
                        "sessions": 0
                    },
                    "total": {
                        "concepts_learned": 0,
                        "problems_solved": 0,
                        "hours_studied": 0.0,
                        "anki_cards_reviewed": 0,
                        "sessions": 0
                    }
                },
                "recommendations": {
                    "next_topics": ["Start with Unit 1: Introducción"],
                    "weak_concepts": [],
                    "suggested_review": [],
                    "priority_areas": []
                },
                "milestones": {
                    "completed": [],
                    "upcoming": []
                }
            }

        self.save_learning_state(default_state)
        return default_state
    
    def load_user_profiles(self) -> Dict:
        """Cargar perfiles de usuarios"""
        if not self.user_profiles_path.exists():
            return {}
        
        with open(self.user_profiles_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def save_user_profiles(self, profiles: Dict) -> None:
        """Guardar perfiles de usuarios"""
        with open(self.user_profiles_path, 'w', encoding='utf-8') as f:
            json.dump(profiles, f, indent=2, ensure_ascii=False)

    def _load_active_session(self) -> None:
        """
        Cargar sesión activa si existe

        Esto permite que comandos CLI separados puedan acceder a la misma sesión.
        """
        if not self.current_session_path.exists():
            return

        try:
            with open(self.current_session_path, 'r', encoding='utf-8') as f:
                session = json.load(f)

            self.current_user = session.get('user')
            start_time_str = session.get('start_time')
            if start_time_str:
                self.session_start_time = datetime.fromisoformat(start_time_str)
            self.session_data = session.get('data', {})

            logger.info(f"✓ Active session loaded for user: {self.current_user}")
        except Exception as e:
            logger.warning(f"Could not load active session: {e}")

    def _save_active_session(self) -> None:
        """
        Guardar sesión activa a archivo

        Esto permite que comandos CLI separados puedan continuar la misma sesión.
        """
        if not self.current_user:
            return

        session = {
            'user': self.current_user,
            'start_time': self.session_start_time.isoformat() if self.session_start_time else None,
            'data': self.session_data
        }

        with open(self.current_session_path, 'w', encoding='utf-8') as f:
            json.dump(session, f, indent=2, ensure_ascii=False)

        logger.info("✓ Active session saved")

    def _clear_active_session(self) -> None:
        """
        Limpiar sesión activa del archivo
        """
        if self.current_session_path.exists():
            self.current_session_path.unlink()
            logger.info("✓ Active session cleared")
    
    # ========================================================================
    # SESSION MANAGEMENT
    # ========================================================================
    
    def start_session(self, user: str) -> Dict:
        """
        Iniciar una nueva sesión de estudio
        
        Args:
            user: Nombre del usuario
        
        Returns:
            Dict con contexto de la sesión
        """
        logger.info(f"Starting session for user: {user}")
        
        # Load state
        state = self.load_learning_state()
        profiles = self.load_user_profiles()
        
        # Get or create user profile
        if user not in profiles:
            profiles[user] = self._create_user_profile(user)
            self.save_user_profiles(profiles)
        
        # Store session info
        self.current_user = user
        self.session_start_time = datetime.now()
        self.session_data = {
            'user': user,
            'start_time': self.session_start_time.isoformat(),
            'actions': [],
            'completed_tasks': [],
            'progress_updates': []
        }

        # Save active session to file for CLI persistence
        self._save_active_session()

        # Build context for user
        context = self.build_context_from_files(state, profiles[user])

        # Update current focus
        self._update_current_focus(user, "session_started")

        return context
    
    def end_session(self, summary: str = None) -> Dict:
        """
        Finalizar sesión actual y guardar todo el estado
        
        Args:
            summary: Resumen opcional de la sesión
        
        Returns:
            Dict con reporte de la sesión
        """
        if not self.current_user:
            raise ValueError("No active session to end")
        
        logger.info(f"Ending session for user: {self.current_user}")
        
        # Calculate duration
        duration = datetime.now() - self.session_start_time
        
        # Build session report
        self.session_data['end_time'] = datetime.now().isoformat()
        self.session_data['duration_minutes'] = duration.total_seconds() / 60
        self.session_data['summary'] = summary
        
        # Save session log
        log_path = self._save_session_log()
        
        # Append to session history
        self._append_to_session_history(self.session_data)
        
        # Update learning state with session data
        state = self.load_learning_state()
        state = self._update_state_from_session(state, self.session_data)
        self.save_learning_state(state)
        
        # Build report
        report = {
            'duration': self._format_duration(duration),
            'completed': self.session_data.get('completed_tasks', []) or ['Session completed'],
            'updates': self.session_data.get('progress_updates', []) or ['State updated'],
            'next_focus': self._generate_next_focus(state),
            'log_path': str(log_path)
        }

        # Clear active session file
        self._clear_active_session()

        # Clear current session in memory
        self.current_user = None
        self.session_start_time = None
        self.session_data = {}

        return report
    
    def _save_session_log(self) -> Path:
        """
        Guardar log detallado de la sesión en Markdown
        
        Returns:
            Path al archivo creado
        """
        # Create sessions subdirectory by month
        month_dir = self.sessions_dir / datetime.now().strftime("%Y-%m")
        month_dir.mkdir(exist_ok=True)
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y-%m-%d")
        filename = f"{timestamp}_{self.current_user}_session.md"
        filepath = month_dir / filename
        
        # Generate markdown content
        content = self._generate_session_markdown()
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"✓ Session log saved: {filepath}")
        return filepath
    
    def _generate_session_markdown(self) -> str:
        """
        Generar contenido Markdown para el log de sesión
        
        Returns:
            String con el contenido en Markdown
        """
        duration = datetime.now() - self.session_start_time
        
        md = f"""# Session Log: {self.session_data.get('topic', 'Study Session')}

**User:** {self.current_user}  
**Date:** {self.session_start_time.strftime('%Y-%m-%d')}  
**Duration:** {self._format_duration(duration)}  
**Unit:** {self.session_data.get('unit', 'N/A')}

## Objective

{self.session_data.get('objective', 'General study session')}

## Work Completed

{self._format_completed_work()}

## Insights Gained

{self._format_insights()}

## Generated Artifacts

{self._format_artifacts()}

## Questions for Next Session

{self._format_open_questions()}

## Handoff Notes for Collaborators

{self._format_handoff_notes()}

## State Updates

```json
{json.dumps(self.session_data.get('state_updates', {}), indent=2)}
```
"""
        return md
    
    def _append_to_session_history(self, session_data: Dict) -> None:
        """
        Añadir sesión al historial (formato JSONL)
        
        Args:
            session_data: Datos de la sesión
        """
        with open(self.session_history_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(session_data, ensure_ascii=False) + '\n')
    
    # ========================================================================
    # CONTEXT BUILDING
    # ========================================================================
    
    def build_context_from_files(self, state: Dict, user_profile: Dict) -> Dict:
        """
        Construir contexto completo desde archivos (NO desde conversaciones)
        
        Esta es la clave de la colaboración multi-usuario:
        TODO el contexto viene de archivos en el repo, no de memory de Claude.
        
        Args:
            state: Estado global del aprendizaje
            user_profile: Perfil del usuario
        
        Returns:
            Dict con contexto completo para la sesión
        """
        context = {
            'user': user_profile,
            'progress': state['progress_summary']['overall_completion'],
            'active_unit': state['current_context']['active_unit'],
            'last_topic': state['current_context']['last_concept_studied'],
            'recommendations': self._generate_recommendations(state, user_profile),
            'recent_activity': self._load_recent_sessions(n=3),
            'weak_concepts': self._identify_weak_concepts(state),
            'anki_status': self._get_anki_summary(),
        }
        
        return context
    
    def _load_recent_sessions(self, n: int = 3) -> List[Dict]:
        """
        Cargar las últimas N sesiones (de cualquier usuario)
        
        Args:
            n: Número de sesiones a cargar
        
        Returns:
            Lista de sesiones recientes
        """
        if not self.session_history_path.exists():
            return []
        
        sessions = []
        with open(self.session_history_path, 'r', encoding='utf-8') as f:
            for line in f:
                sessions.append(json.loads(line))
        
        # Return last n sessions
        return sessions[-n:] if len(sessions) > n else sessions
    
    def _generate_recommendations(self, state: Dict, user_profile: Dict) -> List[str]:
        """
        Generar recomendaciones personalizadas

        Args:
            state: Estado global
            user_profile: Perfil del usuario

        Returns:
            Lista de recomendaciones
        """
        recommendations = []

        # Get current context
        current = state.get('current_context', {})
        progress = state.get('progress_summary', {})
        units = state.get('units', {})

        # Recommendation 1: Next unit or continue current
        active_unit = current.get('active_unit')
        if active_unit and str(active_unit) in units:
            unit_data = units[str(active_unit)]
            if unit_data['progress'] < 100:
                recommendations.append(f"Continue with Unit {active_unit}: {unit_data['name']}")
            else:
                # Move to next unit
                next_unit = active_unit + 1
                if str(next_unit) in units:
                    recommendations.append(f"Start Unit {next_unit}: {units[str(next_unit)]['name']}")
        else:
            # No active unit, suggest Unit 1
            if '1' in units:
                recommendations.append(f"Start with Unit 1: {units['1']['name']}")

        # Recommendation 2: Based on exam date
        exam_date_str = state['metadata'].get('exam_date')
        if exam_date_str:
            try:
                exam_date = datetime.fromisoformat(exam_date_str)
                days_until_exam = (exam_date - datetime.now()).days

                if days_until_exam < 0:
                    recommendations.append("⚠️ Exam date has passed - update in settings")
                elif days_until_exam < 30:
                    recommendations.append(f"⚠️ Only {days_until_exam} days until exam! Focus on weak concepts")
                elif days_until_exam < 60:
                    recommendations.append("Start reviewing previous units for exam prep")
            except (ValueError, TypeError) as e:
                logger.warning(f"Could not parse exam date '{exam_date_str}': {e}")

        # Recommendation 3: Anki review
        anki_status = self._get_anki_summary()
        if anki_status.get('new', 0) > 0 or anki_status.get('learning', 0) > 0:
            recommendations.append("Review Anki cards (pending reviews)")

        # Recommendation 4: Weak concepts
        weak_concepts = state.get('recommendations', {}).get('weak_concepts', [])
        if weak_concepts:
            recommendations.append(f"Review weak concepts: {', '.join(weak_concepts[:3])}")

        # Recommendation 5: Study velocity
        velocity = state.get('learning_velocity', {}).get('last_7_days', {})
        if velocity.get('sessions', 0) == 0:
            recommendations.append("No recent study sessions - aim for consistent daily practice")

        return recommendations[:5]  # Max 5 recommendations
    
    # ========================================================================
    # PROGRESS TRACKING
    # ========================================================================
    
    def get_progress(self, detailed: bool = False, unit: int = None) -> Dict:
        """
        Obtener progreso actual
        
        Args:
            detailed: Si incluir información detallada
            unit: Si especificado, solo mostrar ese unit
        
        Returns:
            Dict con información de progreso
        """
        state = self.load_learning_state()
        
        progress_data = {
            'overall': state['progress_summary']['overall_completion'],
            'concepts_mastered': state['progress_summary']['concepts_mastered'],
            'total_concepts': state['progress_summary']['total_concepts'],
            'problems_solved': state['progress_summary']['problems_solved'],
            'study_hours': state['learning_velocity']['last_7_days']['hours_studied'],
            'units': []
        }
        
        # Add unit information
        for unit_num, unit_data in state['units'].items():
            if unit and int(unit_num) != unit:
                continue
            
            progress_data['units'].append({
                'number': int(unit_num),
                'name': unit_data['name'],
                'status': unit_data['status'],
                'progress': unit_data['progress'],
                'complete': unit_data['status'] == 'completed',
                'in_progress': unit_data['status'] == 'in_progress'
            })
        
        if detailed:
            # Add Anki stats
            progress_data['anki'] = self._get_anki_summary()
        
        return progress_data
    
    def _get_anki_summary(self) -> Dict:
        """
        Obtener resumen de stats de Anki
        
        Returns:
            Dict con stats de Anki
        """
        # TODO: Integrate with AnkiFactory
        return {
            'total': 0,
            'new': 0,
            'learning': 0,
            'young': 0,
            'mature': 0
        }
    
    def _identify_weak_concepts(self, state: Dict) -> List[str]:
        """
        Identificar conceptos débiles
        
        Args:
            state: Estado global
        
        Returns:
            Lista de conceptos débiles
        """
        # TODO: Implement based on:
        # - Anki success rate
        # - Problem solving success
        # - Review frequency
        return []
    
    # ========================================================================
    # UTILITIES
    # ========================================================================
    
    def _create_user_profile(self, username: str) -> Dict:
        """
        Crear perfil inicial para nuevo usuario
        
        Args:
            username: Nombre del usuario
        
        Returns:
            Dict con perfil inicial
        """
        return {
            'username': username,
            'created_at': datetime.now().isoformat(),
            'role': 'primary' if not self.load_user_profiles() else 'collaborator',
            'learning_style': 'balanced',
            'stats': {
                'total_sessions': 0,
                'total_hours': 0.0,
                'concepts_mastered': 0
            }
        }
    
    def _format_duration(self, duration: timedelta) -> str:
        """Format duration as human-readable string"""
        hours = int(duration.total_seconds() // 3600)
        minutes = int((duration.total_seconds() % 3600) // 60)
        return f"{hours}h {minutes}m"
    
    def _format_completed_work(self) -> str:
        """Format completed work for session log"""
        completed = self.session_data.get('completed_tasks', [])
        if not completed:
            return "- No specific tasks completed this session\n"

        result = []
        for task in completed:
            result.append(f"- {task}")
        return "\n".join(result) + "\n"

    def _format_insights(self) -> str:
        """Format insights for session log"""
        insights = self.session_data.get('insights', [])
        if not insights:
            return "- No key insights recorded\n"

        result = []
        for insight in insights:
            result.append(f"- {insight}")
        return "\n".join(result) + "\n"

    def _format_artifacts(self) -> str:
        """Format generated artifacts for session log"""
        artifacts = self.session_data.get('artifacts', [])
        if not artifacts:
            return "- No artifacts generated\n"

        result = []
        for artifact in artifacts:
            if isinstance(artifact, dict):
                result.append(f"- [{artifact.get('type', 'Unknown')}] {artifact.get('path', '')}")
            else:
                result.append(f"- {artifact}")
        return "\n".join(result) + "\n"

    def _format_open_questions(self) -> str:
        """Format open questions for session log"""
        questions = self.session_data.get('open_questions', [])
        if not questions:
            return "- No open questions\n"

        result = []
        for q in questions:
            result.append(f"- {q}")
        return "\n".join(result) + "\n"

    def _format_handoff_notes(self) -> str:
        """Format handoff notes for collaborators"""
        notes = self.session_data.get('handoff_notes', '')
        if not notes:
            return "- Ready for next collaborator to continue\n"

        return notes + "\n"
    
    def _update_state_from_session(self, state: Dict, session_data: Dict) -> Dict:
        """Update learning state based on session data"""
        # Update session count
        velocity = state.get('learning_velocity', {})
        velocity['last_7_days']['sessions'] = velocity.get('last_7_days', {}).get('sessions', 0) + 1
        velocity['last_30_days']['sessions'] = velocity.get('last_30_days', {}).get('sessions', 0) + 1
        velocity['total']['sessions'] = velocity.get('total', {}).get('sessions', 0) + 1

        # Update last session date
        state['current_context']['last_session_date'] = datetime.now().isoformat()

        # Update progress if tasks were completed
        completed = session_data.get('completed_tasks', [])
        if completed:
            state['current_context']['last_activity'] = completed[-1]

        return state

    def _generate_next_focus(self, state: Dict) -> str:
        """Generate next recommended focus"""
        recommendations = state.get('recommendations', {}).get('next_topics', [])
        if recommendations:
            return recommendations[0]

        # Fallback
        active_unit = state.get('current_context', {}).get('active_unit')
        if active_unit:
            return f"Continue with Unit {active_unit}"

        return "Start with Unit 1: Introducción"
    
    def _update_current_focus(self, user: str, status: str) -> None:
        """Update current focus file"""
        focus = {
            'user': user,
            'status': status,
            'timestamp': datetime.now().isoformat()
        }
        
        with open(self.current_focus_path, 'w', encoding='utf-8') as f:
            json.dump(focus, f, indent=2)
    
    # ========================================================================
    # SYNC & COLLABORATION
    # ========================================================================
    
    def sync_state(self) -> Dict:
        """
        Sincronizar estado con repositorio
        
        Returns:
            Dict con resultado de sincronización
        """
        # TODO: Implement
        # - Check for conflicts
        # - Merge changes
        # - Report updates from collaborators
        
        return {
            'conflicts': [],
            'updates': []
        }


# ============================================================================
# MAIN (para testing)
# ============================================================================

if __name__ == '__main__':
    # Quick test
    coordinator = SessionCoordinator()
    
    # Test start session
    context = coordinator.start_session("rodrigo")
    print("Session started:", context)
    
    # Test end session
    report = coordinator.end_session("Initial test session")
    print("Session ended:", report)
