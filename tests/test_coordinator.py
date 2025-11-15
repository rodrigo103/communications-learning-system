"""
Tests for SessionCoordinator

Tests básicos para verificar que el Coordinator funciona correctamente.
"""

import pytest
import json
import tempfile
import shutil
from pathlib import Path
from datetime import datetime

# Add parent directory to path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.coordinator import SessionCoordinator


@pytest.fixture
def temp_dir():
    """Create temporary directory for tests"""
    temp = tempfile.mkdtemp()
    yield Path(temp)
    shutil.rmtree(temp)


@pytest.fixture
def coordinator(temp_dir):
    """Create coordinator instance with temp directory"""
    # Copy schema file to temp directory
    schema_src = Path(__file__).parent.parent / "learning_state_schema.json"
    if schema_src.exists():
        schema_dst = temp_dir / "learning_state_schema.json"
        shutil.copy(schema_src, schema_dst)

    return SessionCoordinator(base_path=temp_dir)


def test_coordinator_initialization(coordinator, temp_dir):
    """Test que el coordinator se inicializa correctamente"""
    assert coordinator.base_path == temp_dir
    assert coordinator.state_dir.exists()
    assert coordinator.progress_dir.exists()
    assert coordinator.sessions_dir.exists()


def test_create_default_learning_state(coordinator):
    """Test que se crea el estado inicial por defecto"""
    state = coordinator._create_default_learning_state()

    # Check structure
    assert 'metadata' in state
    assert 'progress_summary' in state
    assert 'current_context' in state
    assert 'units' in state
    assert 'learning_velocity' in state

    # Check metadata
    assert state['metadata']['exam_date'] == "2025-12-15"
    assert state['metadata']['system_version'] == "1.0.0"

    # Check units (should have 10 units)
    assert len(state['units']) == 10
    for i in range(1, 11):
        assert str(i) in state['units']
        unit = state['units'][str(i)]
        assert 'name' in unit
        assert 'status' in unit
        assert 'progress' in unit


def test_start_session(coordinator):
    """Test que se puede iniciar sesión"""
    context = coordinator.start_session("test_user")

    # Check context structure
    assert 'user' in context
    assert 'progress' in context
    assert 'recommendations' in context

    # Check session is active
    assert coordinator.current_user == "test_user"
    assert coordinator.session_start_time is not None

    # Check session file was created
    assert coordinator.current_session_path.exists()


def test_end_session(coordinator):
    """Test que se guarda session log"""
    # Start session first
    coordinator.start_session("test_user")

    # End session
    report = coordinator.end_session("Test session summary")

    # Check report structure
    assert 'duration' in report
    assert 'completed' in report
    assert 'updates' in report
    assert 'next_focus' in report
    assert 'log_path' in report

    # Check session was cleared
    assert coordinator.current_user is None
    assert coordinator.session_start_time is None
    assert not coordinator.current_session_path.exists()

    # Check session log was created
    log_path = Path(report['log_path'])
    assert log_path.exists()
    assert log_path.suffix == '.md'


def test_session_persistence(coordinator):
    """Test que el estado persiste correctamente entre instancias"""
    # Start session
    coordinator.start_session("test_user")

    # Create new coordinator instance (simulates new CLI command)
    new_coordinator = SessionCoordinator(base_path=coordinator.base_path)

    # Check that session was loaded
    assert new_coordinator.current_user == "test_user"
    assert new_coordinator.session_start_time is not None

    # End session with new instance
    report = new_coordinator.end_session("Test persistence")
    assert 'duration' in report


def test_state_persistence(coordinator):
    """Test que learning_state persiste correctamente"""
    # Load initial state
    state1 = coordinator.load_learning_state()

    # Modify and save
    state1['progress_summary']['concepts_mastered'] = 5
    coordinator.save_learning_state(state1)

    # Create new coordinator and load
    new_coordinator = SessionCoordinator(base_path=coordinator.base_path)
    state2 = new_coordinator.load_learning_state()

    # Check that changes persisted
    assert state2['progress_summary']['concepts_mastered'] == 5


def test_progress_tracking(coordinator):
    """Test que se puede obtener progreso"""
    progress = coordinator.get_progress()

    # Check structure
    assert 'overall' in progress
    assert 'concepts_mastered' in progress
    assert 'total_concepts' in progress
    assert 'problems_solved' in progress
    assert 'study_hours' in progress
    assert 'units' in progress

    # Check that we have 10 units
    assert len(progress['units']) >= 10


def test_user_profile_creation(coordinator):
    """Test que se crean perfiles de usuario"""
    profile = coordinator._create_user_profile("test_user")

    assert profile['username'] == "test_user"
    assert 'created_at' in profile
    assert 'role' in profile
    assert 'stats' in profile


def test_recommendations_generation(coordinator):
    """Test que se generan recomendaciones"""
    state = coordinator.load_learning_state()
    user_profile = coordinator._create_user_profile("test_user")

    recommendations = coordinator._generate_recommendations(state, user_profile)

    # Should have at least one recommendation
    assert len(recommendations) > 0
    assert isinstance(recommendations[0], str)


def test_session_history_append(coordinator):
    """Test que se añade correctamente al historial"""
    # Start and end a session
    coordinator.start_session("test_user")
    coordinator.end_session("Test history")

    # Check that history file was created and has content
    assert coordinator.session_history_path.exists()

    with open(coordinator.session_history_path, 'r') as f:
        lines = f.readlines()
        assert len(lines) > 0

        # Parse last line as JSON
        last_session = json.loads(lines[-1])
        assert last_session['user'] == "test_user"


def test_format_methods(coordinator):
    """Test que los métodos de formato funcionan"""
    # Setup session data
    coordinator.session_data = {
        'completed_tasks': ['Task 1', 'Task 2'],
        'insights': ['Insight 1'],
        'artifacts': [{'type': 'PDF', 'path': '/tmp/test.pdf'}],
        'open_questions': ['Question 1'],
        'handoff_notes': 'Notes for next session'
    }

    # Test each format method
    completed = coordinator._format_completed_work()
    assert 'Task 1' in completed

    insights = coordinator._format_insights()
    assert 'Insight 1' in insights

    artifacts = coordinator._format_artifacts()
    assert 'PDF' in artifacts

    questions = coordinator._format_open_questions()
    assert 'Question 1' in questions

    handoff = coordinator._format_handoff_notes()
    assert 'Notes for next session' in handoff


def test_update_state_from_session(coordinator):
    """Test que el estado se actualiza desde la sesión"""
    state = coordinator.load_learning_state()

    # Create session data
    session_data = {
        'completed_tasks': ['Test task completed']
    }

    # Update state
    updated_state = coordinator._update_state_from_session(state, session_data)

    # Check that session count increased
    assert updated_state['learning_velocity']['total']['sessions'] > 0
    assert 'last_session_date' in updated_state['current_context']


if __name__ == '__main__':
    # Run tests with pytest
    pytest.main([__file__, '-v'])
