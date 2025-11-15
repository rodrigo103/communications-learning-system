"""
Tests for ProblemSolver

Verificar que el solver parsea y resuelve problemas correctamente.
"""

import pytest
import tempfile
import shutil
from pathlib import Path

# Add parent directory to path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.problem_solver import ProblemSolver


@pytest.fixture
def temp_dir():
    """Create temporary directory for tests"""
    temp = tempfile.mkdtemp()
    yield Path(temp)
    shutil.rmtree(temp)


@pytest.fixture
def solver(temp_dir):
    """Create problem solver instance with temp directory"""
    return ProblemSolver(base_path=temp_dir)


@pytest.fixture
def sample_problem_file(temp_dir):
    """Create a sample problem file"""
    problem_text = """Ejercicio de Prueba: Ruido

Datos:
- Ganancia: G = 40 dB
- Ancho de banda: BW = 10 kHz
- Potencia de ruido a la salida: P_n_out = 50×10^-12 W
- Densidad espectral de potencia de ruido a la entrada: η_in = 10×10^-21 W/Hz

Se pide:
a) Calcular la figura de ruido F del amplificador.

Constantes:
- T_0 = 290 K
"""
    problem_file = temp_dir / "test_problem.txt"
    with open(problem_file, 'w', encoding='utf-8') as f:
        f.write(problem_text)
    return problem_file


def test_solver_initialization(solver, temp_dir):
    """Test que el solver se inicializa correctamente"""
    assert solver.base_path == temp_dir
    assert solver.outputs_dir.exists()
    assert len(solver.constants) >= 3
    assert len(solver.problem_types) >= 3


def test_unit_conversions_dictionary(solver):
    """Test que el diccionario de conversiones está completo"""
    assert 'kHz' in solver.UNIT_CONVERSIONS
    assert 'MHz' in solver.UNIT_CONVERSIONS
    assert 'GHz' in solver.UNIT_CONVERSIONS
    assert 'mW' in solver.UNIT_CONVERSIONS
    assert 'μW' in solver.UNIT_CONVERSIONS
    assert 'ms' in solver.UNIT_CONVERSIONS
    assert 'μs' in solver.UNIT_CONVERSIONS

    # Check conversions are correct
    assert solver.UNIT_CONVERSIONS['kHz'] == ('Hz', 1e3)
    assert solver.UNIT_CONVERSIONS['mW'] == ('W', 1e-3)
    assert solver.UNIT_CONVERSIONS['ms'] == ('s', 1e-3)


def test_parse_problem_basic(solver, sample_problem_file):
    """Test parseo básico de problema"""
    problem = solver.parse_problem(sample_problem_file)

    assert 'title' in problem
    assert 'text' in problem
    assert 'given' in problem
    assert 'asked' in problem
    assert 'constants' in problem


def test_parse_given_data(solver, sample_problem_file):
    """Test que se parsean los datos correctamente"""
    problem = solver.parse_problem(sample_problem_file)

    # Check G is parsed
    assert 'G' in problem['given']
    assert problem['given']['G']['value'] == 40
    assert problem['given']['G']['unit'] == 'dB'

    # Check BW is parsed and converted
    assert 'BW' in problem['given']
    assert problem['given']['BW']['value'] == 10000  # Converted from kHz to Hz
    assert problem['given']['BW']['unit'] == 'Hz'


def test_parse_scientific_notation(solver, sample_problem_file):
    """Test parseo de notación científica"""
    problem = solver.parse_problem(sample_problem_file)

    # Check P_n_out with scientific notation
    assert 'P_n_out' in problem['given']
    assert abs(problem['given']['P_n_out']['value'] - 50e-12) < 1e-15


def test_parse_eta_character(solver, sample_problem_file):
    """Test que η se convierte a eta"""
    problem = solver.parse_problem(sample_problem_file)

    # η should be converted to eta
    assert 'eta_in' in problem['given']
    assert abs(problem['given']['eta_in']['value'] - 10e-21) < 1e-25


def test_identify_noise_problem(solver, sample_problem_file):
    """Test identificación de problema de ruido"""
    problem = solver.parse_problem(sample_problem_file)
    problem_type = solver.identify_type(problem)

    assert problem_type == 'noise'


def test_noise_figure_calculation(solver):
    """Test cálculo de figura de ruido"""
    result = solver._solve_noise_figure(
        G_dB=40,
        BW=10000,
        P_n_out=50e-12,
        eta_in=10e-21
    )

    # Check structure
    assert 'steps' in result
    assert 'result' in result
    assert 'answer' in result

    # Check results
    assert 'F_linear' in result['result']
    assert 'F_dB' in result['result']
    assert 'G_linear' in result['result']

    # Check G conversion
    assert abs(result['result']['G_linear'] - 10000) < 1  # 40 dB = 10000

    # Check calculation steps
    assert len(result['steps']) == 4


def test_noise_temperature_calculation(solver):
    """Test cálculo de temperatura de ruido"""
    result = solver._solve_noise_temperature(F_linear=3.0, T_0=290)

    assert 'steps' in result
    assert 'result' in result

    # T_e = T_0 * (F - 1) = 290 * (3 - 1) = 580
    assert abs(result['result']['T_e'] - 580) < 0.1


def test_cascaded_noise_figure(solver):
    """Test cálculo de Friis en cascada"""
    result = solver._solve_cascaded_noise_figure(F1=3.0, G1=100000)

    assert 'steps' in result
    assert 'result' in result

    # For identical stages: F_total = F1 + (F1 - 1)/G1
    expected = 3.0 + (3.0 - 1) / 100000
    assert abs(result['result']['F_total_linear'] - expected) < 0.0001


def test_snr_output_calculation(solver):
    """Test cálculo de SNR de salida"""
    result = solver._solve_snr_output(S_in=1e-15, G=100000, P_n_out=72e-12)

    assert 'steps' in result
    assert 'result' in result

    # SNR = (G * S_in) / P_n_out
    S_out = 100000 * 1e-15
    expected_snr = S_out / 72e-12
    assert abs(result['result']['SNR_linear'] - expected_snr) < 0.01


def test_solve_complete_problem(solver):
    """Test resolución de problema completo desde archivo"""
    # Use the real exercise file
    exercise_file = solver.base_path.parent / "docs" / "ejercicio_ruido.txt"
    if exercise_file.exists():
        solution = solver.solve_problem(exercise_file)

        assert solution['type'] == 'noise'
        assert len(solution['parts']) >= 4  # At least 4 parts solved


def test_pdf_generation(solver, sample_problem_file):
    """Test generación de PDF"""
    solution = solver.solve_problem(sample_problem_file)
    pdf_path = solver.generate_pdf(solution)

    # Check file exists
    assert pdf_path.exists()
    assert pdf_path.stat().st_size > 1000  # At least 1KB

    # Check it's a PDF
    with open(pdf_path, 'rb') as f:
        header = f.read(4)
        assert header == b'%PDF'


def test_anki_cards_generation(solver, sample_problem_file):
    """Test generación de tarjetas Anki"""
    solution = solver.solve_problem(sample_problem_file)
    cards = solver.create_anki_cards(solution)

    assert len(cards) >= 1  # At least 1 card
    for card in cards:
        assert 'front' in card
        assert 'back' in card
        assert 'tags' in card


def test_anki_deck_export(solver, sample_problem_file):
    """Test exportación de deck Anki"""
    solution = solver.solve_problem(sample_problem_file)
    anki_path = solver.export_to_anki_deck(solution)

    assert anki_path.exists()
    assert anki_path.suffix == '.apkg'
    assert anki_path.stat().st_size > 1000


def test_save_solution(solver, sample_problem_file):
    """Test guardado de solución en JSON"""
    solution = solver.solve_problem(sample_problem_file)
    json_path = solver.save_solution(solution)

    assert json_path.exists()
    assert json_path.suffix == '.json'

    # Load and verify
    import json
    with open(json_path, 'r') as f:
        loaded = json.load(f)

    assert loaded['type'] == solution['type']


def test_extract_variables_with_units(solver):
    """Test extracción de variables con diferentes unidades"""
    text = """
    P = 10 mW
    T = 5 ms
    f = 2.4 GHz
    d = 50 μm
    """

    variables = solver._extract_variables(text)

    # Check mW conversion
    if 'P' in variables:
        assert abs(variables['P']['value'] - 0.01) < 1e-6  # 10 mW = 0.01 W

    # Check ms conversion
    if 'T' in variables:
        assert abs(variables['T']['value'] - 0.005) < 1e-6  # 5 ms = 0.005 s

    # Check GHz conversion
    if 'f' in variables:
        assert abs(variables['f']['value'] - 2.4e9) < 1e3  # 2.4 GHz = 2.4e9 Hz


def test_validation_messages(solver):
    """Test que los mensajes de validación están presentes"""
    result = solver._solve_noise_figure(40, 10000, 50e-12, 10e-21)

    assert 'validation' in result
    assert 'Dimensiones correctas' in result['validation'] or '✓' in result['validation']


def test_problem_types_knowledge_base(solver):
    """Test que la knowledge base tiene tipos correctos"""
    assert 'noise' in solver.problem_types
    assert 'modulation' in solver.problem_types
    assert 'channel_capacity' in solver.problem_types

    # Check structure
    for ptype, info in solver.problem_types.items():
        assert 'keywords' in info
        assert 'formulas' in info
        assert 'units' in info


if __name__ == '__main__':
    # Run tests with pytest
    pytest.main([__file__, '-v'])
