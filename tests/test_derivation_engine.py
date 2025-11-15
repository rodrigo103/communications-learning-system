"""
Tests for DerivationEngine

Verificar que las derivaciones son correctas y completas.
"""

import pytest
import tempfile
import shutil
from pathlib import Path

# Add parent directory to path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.derivation_engine import DerivationEngine


@pytest.fixture
def temp_dir():
    """Create temporary directory for tests"""
    temp = tempfile.mkdtemp()
    yield Path(temp)
    shutil.rmtree(temp)


@pytest.fixture
def engine(temp_dir):
    """Create derivation engine instance with temp directory"""
    return DerivationEngine(base_path=temp_dir)


def test_engine_initialization(engine, temp_dir):
    """Test que el engine se inicializa correctamente"""
    assert engine.base_path == temp_dir
    assert engine.outputs_dir.exists()
    assert len(engine.knowledge_base) >= 6  # At least 6 topics


def test_knowledge_base_structure(engine):
    """Test que la knowledge base tiene la estructura correcta"""
    for topic, info in engine.knowledge_base.items():
        assert 'name' in info
        assert 'description' in info
        assert 'starting_point' in info
        assert 'prerequisites' in info
        assert 'related_concepts' in info


def test_am_derivation(engine):
    """Test que la derivación de AM produce resultado correcto"""
    result = engine.derive_formula('AM', level='complete')

    # Check basic structure
    assert result['topic'] == 'AM'
    assert result['title'] == 'Amplitude Modulation (AM) Derivation'
    assert result['level'] == 'complete'

    # Check steps
    assert len(result['steps']) >= 5
    assert 'final_formula' in result
    assert 'A_c [1 + m(t)]' in result['final_formula']

    # Check key results
    assert len(result['key_results']) >= 3
    assert any('bandwidth' in r.lower() for r in result['key_results'])


def test_am_derivation_basic_level(engine):
    """Test derivación AM nivel básico tiene menos pasos"""
    result_basic = engine.derive_formula('AM', level='basic')
    result_complete = engine.derive_formula('AM', level='complete')

    # Basic should have fewer steps than complete
    assert len(result_basic['steps']) < len(result_complete['steps'])


def test_fm_derivation(engine):
    """Test que la derivación de FM funciona"""
    result = engine.derive_formula('FM', level='complete')

    assert result['topic'] == 'FM'
    assert 'Carson' in result['title'] or 'Frequency Modulation' in result['title']
    assert len(result['steps']) >= 3
    assert result['final_formula']


def test_shannon_hartley_derivation(engine):
    """Test derivación de Shannon-Hartley"""
    result = engine.derive_formula('Shannon-Hartley', level='complete')

    assert result['topic'] == 'Shannon-Hartley'
    assert 'Channel Capacity' in result['title']
    assert len(result['steps']) >= 4
    assert 'log' in result['final_formula'].lower()


def test_friis_derivation(engine):
    """Test derivación de Friis"""
    result = engine.derive_formula('Friis', level='complete')

    assert result['topic'] == 'Friis'
    assert 'Cascade' in result['title'] or 'Noise' in result['title']
    assert len(result['steps']) >= 3


def test_qam_derivation(engine):
    """Test derivación de QAM"""
    result = engine.derive_formula('QAM', level='complete')

    assert result['topic'] == 'QAM'
    assert 'Quadrature' in result['title']
    assert len(result['steps']) >= 2
    assert 'orthogonal' in result['title'].lower() or any(
        'orthogon' in r.lower() for r in result['key_results']
    )


def test_unknown_topic(engine):
    """Test que temas desconocidos se manejan correctamente"""
    result = engine.derive_formula('UnknownTopic', level='complete')

    # Unknown topics return generic derivation
    assert result is not None
    assert len(result['steps']) >= 1
    # Generic derivation should indicate topic not found
    if result.get('topic'):
        assert result['topic'] in ['UnknownTopic', 'generic']


def test_validation_structure(engine):
    """Test que la validación tiene estructura correcta"""
    result = engine.derive_formula('AM', level='complete')

    assert 'validation' in result
    validation = result['validation']
    assert 'valid' in validation
    assert isinstance(validation['valid'], bool)


def test_anki_cards_generation(engine):
    """Test que se generan tarjetas Anki"""
    result = engine.derive_formula('AM', level='complete')
    cards = engine.create_anki_cards(result)

    assert len(cards) >= 3  # At least 3 cards
    for card in cards:
        assert 'front' in card
        assert 'back' in card
        assert 'tags' in card
        assert len(card['front']) > 0
        assert len(card['back']) > 0


def test_pdf_generation(engine):
    """Test que se genera PDF correctamente"""
    result = engine.derive_formula('AM', level='complete')
    pdf_path = engine.generate_pdf(result)

    # Check file exists and is not empty
    assert pdf_path.exists()
    assert pdf_path.stat().st_size > 1000  # At least 1KB

    # Check it's a PDF file
    with open(pdf_path, 'rb') as f:
        header = f.read(4)
        assert header == b'%PDF'


def test_anki_deck_export(engine):
    """Test que se exporta deck de Anki"""
    result = engine.derive_formula('AM', level='complete')
    anki_path = engine.export_to_anki_deck(result)

    # Check file exists
    assert anki_path.exists()
    assert anki_path.suffix == '.apkg'
    assert anki_path.stat().st_size > 1000  # At least 1KB


def test_save_derivation(engine):
    """Test que se guarda derivación en JSON"""
    result = engine.derive_formula('AM', level='complete')
    json_path = engine.save_derivation(result)

    # Check file exists
    assert json_path.exists()
    assert json_path.suffix == '.json'

    # Load and verify structure
    import json
    with open(json_path, 'r') as f:
        loaded = json.load(f)

    assert loaded['topic'] == 'AM'
    assert loaded['title'] == result['title']


def test_multiple_derivations_same_topic(engine):
    """Test que múltiples derivaciones del mismo tema son consistentes"""
    result1 = engine.derive_formula('AM', level='complete')
    result2 = engine.derive_formula('AM', level='complete')

    # Should produce same results
    assert result1['topic'] == result2['topic']
    assert result1['final_formula'] == result2['final_formula']
    assert len(result1['steps']) == len(result2['steps'])


def test_expert_level_has_more_content(engine):
    """Test que nivel expert tiene más contenido que complete"""
    result_complete = engine.derive_formula('Shannon-Hartley', level='complete')
    result_expert = engine.derive_formula('Shannon-Hartley', level='expert')

    # Expert should have more or equal steps
    assert len(result_expert['steps']) >= len(result_complete['steps'])


def test_all_topics_derive_successfully(engine):
    """Test que todos los temas conocidos derivan sin errores"""
    for topic in engine.knowledge_base.keys():
        result = engine.derive_formula(topic, level='complete')
        # Carson redirects to FM, so allow that
        if topic == 'Carson':
            assert result['topic'] in ['Carson', 'FM']
        else:
            assert result['topic'] == topic
        assert len(result['steps']) > 0
        assert 'final_formula' in result


if __name__ == '__main__':
    # Run tests with pytest
    pytest.main([__file__, '-v'])
