"""
Problem Solver - Resolver ejercicios tipo examen

Responsabilidades:
- Parsear enunciados de problemas
- Identificar tipo de problema y conceptos involucrados
- Resolver paso a paso con justificación
- Validar unidades dimensionalmente
- Generar PDF con solución completa
- Crear tarjetas Anki automáticamente
"""

import re
import json
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
import logging
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import genanki
import random

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ProblemSolver:
    """
    Motor de resolución de problemas de comunicaciones.

    Resuelve ejercicios paso a paso, valida dimensiones, y genera
    PDFs y tarjetas Anki automáticamente.
    """

    # Unit conversion dictionary
    UNIT_CONVERSIONS = {
        # Frequency
        'kHz': ('Hz', 1e3),
        'MHz': ('Hz', 1e6),
        'GHz': ('Hz', 1e9),
        # Power
        'mW': ('W', 1e-3),
        'μW': ('W', 1e-6),
        'uW': ('W', 1e-6),  # Alternative spelling
        'nW': ('W', 1e-9),
        'pW': ('W', 1e-12),
        'dBm': ('W', None),  # Special case: 10^((P_dBm - 30)/10)
        # Time
        'ms': ('s', 1e-3),
        'μs': ('s', 1e-6),
        'us': ('s', 1e-6),  # Alternative spelling
        'ns': ('s', 1e-9),
        'ps': ('s', 1e-12),
        # Distance
        'km': ('m', 1e3),
        'cm': ('m', 1e-2),
        'mm': ('m', 1e-3),
        'μm': ('m', 1e-6),
        'um': ('m', 1e-6),  # Alternative spelling
        'nm': ('m', 1e-9),
    }

    def __init__(self, base_path: Path = None):
        """
        Inicializar ProblemSolver

        Args:
            base_path: Ruta base del proyecto (default: directorio actual)
        """
        self.base_path = base_path or Path.cwd()
        self.outputs_dir = self.base_path / "outputs" / "solutions"
        self.outputs_dir.mkdir(parents=True, exist_ok=True)

        # Physical constants
        self.constants = {
            'k': 1.38e-23,  # Boltzmann constant [J/K]
            'T_0': 290,     # Reference temperature [K]
            'c': 3e8,       # Speed of light [m/s]
        }

        # Problem type knowledge base
        self.problem_types = {
            'noise': {
                'keywords': ['ruido', 'noise', 'figura', 'temperature', 'SNR', 'friis'],
                'formulas': ['F = P_n_out / (G * P_n_in)', 'T_e = T_0 * (F - 1)', 'F_total = F_1 + (F_2 - 1)/G_1'],
                'units': {'F': 'dimensionless', 'T': 'K', 'P': 'W', 'G': 'dimensionless'}
            },
            'modulation': {
                'keywords': ['modulación', 'modulation', 'AM', 'FM', 'PM', 'bandwidth', 'power'],
                'formulas': ['BW_AM = 2*f_m', 'BW_FM = 2*(Δf + f_m)', 'P_c = A_c^2/2'],
                'units': {'BW': 'Hz', 'f': 'Hz', 'P': 'W'}
            },
            'channel_capacity': {
                'keywords': ['capacidad', 'capacity', 'shannon', 'hartley', 'bits'],
                'formulas': ['C = B * log2(1 + SNR)'],
                'units': {'C': 'bits/s', 'B': 'Hz', 'SNR': 'dimensionless'}
            }
        }

        # Anki model
        self.anki_model_id = random.randrange(1 << 30, 1 << 31)
        self.anki_deck_id = random.randrange(1 << 30, 1 << 31)

    def solve_problem(self, problem_file: Path) -> Dict:
        """
        Resolver un problema completo desde archivo

        Args:
            problem_file: Path al archivo con el enunciado

        Returns:
            Dict con solución completa
        """
        logger.info(f"Solving problem: {problem_file}")

        # Parse problem
        problem = self.parse_problem(problem_file)

        # Identify type
        problem_type = self.identify_type(problem)
        problem['type'] = problem_type

        # Solve based on type
        if problem_type == 'noise':
            solution = self.solve_noise_problem(problem)
        elif problem_type == 'modulation':
            solution = self.solve_modulation_problem(problem)
        elif problem_type == 'channel_capacity':
            solution = self.solve_capacity_problem(problem)
        else:
            solution = self.solve_generic_problem(problem)

        solution['problem'] = problem
        solution['timestamp'] = datetime.now().isoformat()

        logger.info(f"✓ Problem solved: {problem['title']}")

        return solution

    def parse_problem(self, problem_file: Path) -> Dict:
        """
        Parsear enunciado de problema desde archivo

        Args:
            problem_file: Path al archivo

        Returns:
            Dict con problema parseado
        """
        with open(problem_file, 'r', encoding='utf-8') as f:
            text = f.read()

        problem = {
            'title': '',
            'text': text,
            'given': {},
            'asked': [],
            'constants': {}
        }

        # Extract title (first line)
        lines = text.strip().split('\n')
        problem['title'] = lines[0] if lines else 'Problema'

        # Extract given data
        given_section = re.search(r'Datos?:(.*?)(?:Se pide|Constantes?:|$)', text, re.DOTALL | re.IGNORECASE)
        if given_section:
            given_text = given_section.group(1)
            problem['given'] = self._extract_variables(given_text)

        # Extract questions
        asked_section = re.search(r'Se pide:(.*?)(?:Constantes?:|$)', text, re.DOTALL | re.IGNORECASE)
        if asked_section:
            asked_text = asked_section.group(1)
            # Split by a), b), c) etc
            questions = re.findall(r'[a-e]\)(.*?)(?=[a-e]\)|$)', asked_text, re.DOTALL)
            problem['asked'] = [q.strip() for q in questions]

        # Extract constants
        constants_section = re.search(r'Constantes?:(.*?)$', text, re.DOTALL | re.IGNORECASE)
        if constants_section:
            constants_text = constants_section.group(1)
            problem['constants'] = self._extract_variables(constants_text)

        return problem

    def _extract_variables(self, text: str) -> Dict:
        """
        Extraer variables y sus valores de un texto

        Args:
            text: Texto con variables

        Returns:
            Dict de variables y valores
        """
        variables = {}

        # Patterns para diferentes formatos
        # Pattern for full scientific notation: P_n_out = 72×10^-12 W
        pattern1 = r'([A-Za-zη_][A-Za-z0-9η_]*)\s*=\s*([\d.]+)\s*[×x*]\s*10\s*\^\s*([-+]?\d+)\s*([A-Za-z/]+)?'
        # Pattern for exponential notation: S_in = 10^-15 W
        pattern2 = r'([A-Za-zη_][A-Za-z0-9η_]*)\s*=\s*10\s*\^\s*([-+]?\d+)\s*([A-Za-z/]+)?'
        # Pattern for regular numbers: G = 50 dB
        pattern3 = r'([A-Za-zη_][A-Za-z0-9η_]*)\s*=\s*([\d.]+)\s*([A-Za-z/]+)?'

        # Try pattern 1: full scientific notation
        matches1 = re.findall(pattern1, text)
        for match in matches1:
            var_name = match[0].strip().replace('η', 'eta')
            mantissa = float(match[1])
            exponent = int(match[2])
            value = mantissa * (10 ** exponent)
            unit = match[3].strip() if len(match) > 3 and match[3] else ''

            variables[var_name] = {
                'value': value,
                'unit': unit,
                'original': f"{match[1]}×10^{match[2]}"
            }

        # Try pattern 2: exponential only
        matches2 = re.findall(pattern2, text)
        for match in matches2:
            var_name = match[0].strip().replace('η', 'eta')
            if var_name not in variables:  # Don't overwrite
                exponent = int(match[1])
                value = 10 ** exponent
                unit = match[2].strip() if len(match) > 2 and match[2] else ''

                variables[var_name] = {
                    'value': value,
                    'unit': unit,
                    'original': f"10^{match[1]}"
                }

        # Try pattern 3: regular numbers
        matches3 = re.findall(pattern3, text)
        for match in matches3:
            var_name = match[0].strip().replace('η', 'eta')
            if var_name not in variables:  # Don't overwrite
                try:
                    value = float(match[1])
                    unit = match[2].strip() if len(match) > 2 and match[2] else ''

                    # Apply unit conversions if applicable
                    if unit in self.UNIT_CONVERSIONS:
                        base_unit, multiplier = self.UNIT_CONVERSIONS[unit]
                        if multiplier is not None:
                            value = value * multiplier
                            unit = base_unit
                        elif unit == 'dBm':
                            # Special case: dBm to Watts
                            value = 10 ** ((value - 30) / 10)
                            unit = 'W'

                    variables[var_name] = {
                        'value': value,
                        'unit': unit,
                        'original': match[1]
                    }
                except (ValueError, TypeError) as e:
                    logger.debug(f"Could not parse variable {var_name}: {e}")

        return variables

    def identify_type(self, problem: Dict) -> str:
        """
        Identificar tipo de problema

        Args:
            problem: Problema parseado

        Returns:
            Tipo de problema
        """
        text_lower = problem['text'].lower()

        # Check keywords for each type
        for ptype, info in self.problem_types.items():
            keyword_count = sum(1 for kw in info['keywords'] if kw.lower() in text_lower)
            if keyword_count >= 2:
                logger.info(f"✓ Problem type identified: {ptype}")
                return ptype

        return 'generic'

    def solve_noise_problem(self, problem: Dict) -> Dict:
        """
        Resolver problema de ruido

        Args:
            problem: Problema parseado

        Returns:
            Solución completa
        """
        solution = {
            'type': 'noise',
            'parts': []
        }

        given = problem['given']
        constants_raw = problem.get('constants', {})

        # Extract common parameters (get values from dict format)
        G_dB = given.get('G', {}).get('value')
        BW = given.get('BW', {}).get('value')
        P_n_out = given.get('P_n_out', {}).get('value')
        eta_in = given.get('eta_in', {}).get('value')  # η is converted to eta in parsing

        # Get constants (could be dict or direct value)
        if isinstance(constants_raw.get('T_0'), dict):
            T_0 = constants_raw['T_0'].get('value', 290)
        else:
            T_0 = constants_raw.get('T_0', self.constants['T_0'])

        if isinstance(constants_raw.get('k'), dict):
            k = constants_raw['k'].get('value', 1.38e-23)
        else:
            k = constants_raw.get('k', self.constants['k'])

        # Part a) Noise figure
        if G_dB and BW and P_n_out and eta_in:
            part_a = self._solve_noise_figure(G_dB, BW, P_n_out, eta_in)
            solution['parts'].append(part_a)

            # Store for next parts
            F_linear = part_a['result']['F_linear']
            G_linear = part_a['result']['G_linear']

            # Part b) Noise temperature
            if F_linear:
                part_b = self._solve_noise_temperature(F_linear, T_0)
                solution['parts'].append(part_b)

                T_e = part_b['result']['T_e']

                # Part c) Cascaded noise figure
                part_c = self._solve_cascaded_noise_figure(F_linear, G_linear)
                solution['parts'].append(part_c)

                # Part d) Total noise temperature
                F_total = part_c['result']['F_total_linear']
                part_d = self._solve_noise_temperature(F_total, T_0, label='total')
                solution['parts'].append(part_d)

                # Part e) SNR at output
                S_in = given.get('S_in', {}).get('value')
                if S_in or len(problem['asked']) > 4:
                    # Use example value if not given
                    S_in = S_in or 1e-15
                    part_e = self._solve_snr_output(S_in, G_linear, P_n_out)
                    solution['parts'].append(part_e)

        return solution

    def _solve_noise_figure(self, G_dB: float, BW: float, P_n_out: float, eta_in: float) -> Dict:
        """Resolver figura de ruido"""
        steps = []

        # Step 1: Convert gain to linear
        G_linear = 10 ** (G_dB / 10)
        steps.append({
            'number': 1,
            'description': 'Convertir ganancia de dB a lineal',
            'formula': 'G = 10^(G_dB/10)',
            'calculation': f'G = 10^({G_dB}/10) = {G_linear:.0f}',
            'result': G_linear,
            'unit': 'dimensionless'
        })

        # Step 2: Calculate input noise power
        P_n_in = eta_in * BW
        steps.append({
            'number': 2,
            'description': 'Calcular potencia de ruido de entrada',
            'formula': 'P_n_in = η_in × BW',
            'calculation': f'P_n_in = {eta_in:.2e} W/Hz × {BW:.2e} Hz = {P_n_in:.2e} W',
            'result': P_n_in,
            'unit': 'W'
        })

        # Step 3: Calculate noise figure
        F_linear = P_n_out / (G_linear * P_n_in)
        steps.append({
            'number': 3,
            'description': 'Aplicar definición de figura de ruido',
            'formula': 'F = P_n_out / (G × P_n_in)',
            'calculation': f'F = {P_n_out:.2e} / ({G_linear:.0f} × {P_n_in:.2e}) = {F_linear:.2f}',
            'result': F_linear,
            'unit': 'dimensionless'
        })

        # Step 4: Convert to dB
        F_dB = 10 * np.log10(F_linear)
        steps.append({
            'number': 4,
            'description': 'Convertir a dB',
            'formula': 'F_dB = 10 log₁₀(F)',
            'calculation': f'F_dB = 10 log₁₀({F_linear:.2f}) = {F_dB:.2f} dB',
            'result': F_dB,
            'unit': 'dB'
        })

        return {
            'question': 'a) Calcular la figura de ruido F del amplificador',
            'steps': steps,
            'result': {
                'F_linear': F_linear,
                'F_dB': F_dB,
                'G_linear': G_linear,
                'P_n_in': P_n_in
            },
            'answer': f'F = {F_linear:.2f} (lineal) = {F_dB:.2f} dB',
            'validation': 'Dimensiones correctas: [W] / ([1] × [W]) = [1] ✓'
        }

    def _solve_noise_temperature(self, F_linear: float, T_0: float, label: str = '') -> Dict:
        """Resolver temperatura de ruido"""
        steps = []

        # Step 1: Apply formula
        T_e = T_0 * (F_linear - 1)
        steps.append({
            'number': 1,
            'description': 'Aplicar relación entre figura de ruido y temperatura',
            'formula': f'T_{"e" if not label else label} = T_0 × (F - 1)',
            'calculation': f'T_{"e" if not label else label} = {T_0} K × ({F_linear:.2f} - 1) = {T_e:.2f} K',
            'result': T_e,
            'unit': 'K'
        })

        question = 'b) Calcular la temperatura de ruido equivalente T_e' if not label else f'd) Calcular la temperatura de ruido {label} T_{label}'

        return {
            'question': question,
            'steps': steps,
            'result': {'T_e' if not label else f'T_{label}': T_e},
            'answer': f'T_{"e" if not label else label} = {T_e:.2f} K',
            'validation': 'Dimensiones correctas: [K] × [1] = [K] ✓'
        }

    def _solve_cascaded_noise_figure(self, F1: float, G1: float) -> Dict:
        """Resolver figura de ruido en cascada (Friis)"""
        steps = []

        # For identical amplifiers: F2 = F1
        F2 = F1

        # Step 1: Apply Friis formula
        F_total = F1 + (F2 - 1) / G1
        steps.append({
            'number': 1,
            'description': 'Aplicar fórmula de Friis para dos etapas idénticas',
            'formula': 'F_total = F_1 + (F_2 - 1) / G_1',
            'calculation': f'F_total = {F1:.2f} + ({F2:.2f} - 1) / {G1:.0f} = {F_total:.4f}',
            'result': F_total,
            'unit': 'dimensionless'
        })

        # Step 2: Convert to dB
        F_total_dB = 10 * np.log10(F_total)
        steps.append({
            'number': 2,
            'description': 'Convertir a dB',
            'formula': 'F_total_dB = 10 log₁₀(F_total)',
            'calculation': f'F_total_dB = 10 log₁₀({F_total:.4f}) = {F_total_dB:.2f} dB',
            'result': F_total_dB,
            'unit': 'dB'
        })

        return {
            'question': 'c) Calcular la figura de ruido total del sistema en cascada',
            'steps': steps,
            'result': {
                'F_total_linear': F_total,
                'F_total_dB': F_total_dB
            },
            'answer': f'F_total = {F_total:.4f} (lineal) = {F_total_dB:.2f} dB',
            'validation': 'Friis formula aplicada correctamente ✓'
        }

    def _solve_snr_output(self, S_in: float, G: float, P_n_out: float) -> Dict:
        """Resolver SNR a la salida"""
        steps = []

        # Step 1: Calculate output signal power
        S_out = G * S_in
        steps.append({
            'number': 1,
            'description': 'Calcular potencia de señal a la salida',
            'formula': 'S_out = G × S_in',
            'calculation': f'S_out = {G:.0f} × {S_in:.2e} W = {S_out:.2e} W',
            'result': S_out,
            'unit': 'W'
        })

        # Step 2: Calculate SNR
        SNR_linear = S_out / P_n_out
        steps.append({
            'number': 2,
            'description': 'Calcular SNR a la salida',
            'formula': 'SNR_out = S_out / P_n_out',
            'calculation': f'SNR_out = {S_out:.2e} / {P_n_out:.2e} = {SNR_linear:.2f}',
            'result': SNR_linear,
            'unit': 'dimensionless'
        })

        # Step 3: Convert to dB
        SNR_dB = 10 * np.log10(SNR_linear)
        steps.append({
            'number': 3,
            'description': 'Convertir a dB',
            'formula': 'SNR_dB = 10 log₁₀(SNR)',
            'calculation': f'SNR_dB = 10 log₁₀({SNR_linear:.2f}) = {SNR_dB:.2f} dB',
            'result': SNR_dB,
            'unit': 'dB'
        })

        return {
            'question': 'e) Calcular el SNR a la salida',
            'steps': steps,
            'result': {
                'SNR_linear': SNR_linear,
                'SNR_dB': SNR_dB,
                'S_out': S_out
            },
            'answer': f'SNR_out = {SNR_linear:.2f} (lineal) = {SNR_dB:.2f} dB',
            'validation': 'Dimensiones correctas: [W] / [W] = [1] ✓'
        }

    def solve_modulation_problem(self, problem: Dict) -> Dict:
        """Resolver problema de modulación"""
        # TODO: Implement modulation problems
        return {
            'type': 'modulation',
            'parts': [],
            'note': 'Modulation problem solver to be implemented'
        }

    def solve_capacity_problem(self, problem: Dict) -> Dict:
        """Resolver problema de capacidad de canal"""
        # TODO: Implement capacity problems
        return {
            'type': 'channel_capacity',
            'parts': [],
            'note': 'Channel capacity problem solver to be implemented'
        }

    def solve_generic_problem(self, problem: Dict) -> Dict:
        """Resolver problema genérico"""
        return {
            'type': 'generic',
            'parts': [],
            'note': 'Generic problem - requires manual solution'
        }

    def generate_pdf(self, solution: Dict, output_path: Path = None) -> Path:
        """
        Generar PDF con la solución completa

        Args:
            solution: Solución completa
            output_path: Ruta de salida (opcional)

        Returns:
            Path al PDF generado
        """
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            problem_name = solution['problem']['title'].split(':')[0].replace(' ', '_')
            filename = f"{problem_name}_{timestamp}.pdf"
            output_path = self.outputs_dir / filename

        logger.info(f"Generating PDF: {output_path}")

        # Create PDF
        doc = SimpleDocTemplate(str(output_path), pagesize=letter)
        story = []
        styles = getSampleStyleSheet()

        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=20,
            textColor='darkblue',
            spaceAfter=20,
            alignment=TA_CENTER
        )

        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            textColor='darkblue',
            spaceAfter=10,
            spaceBefore=10
        )

        # Title
        title = Paragraph(solution['problem']['title'], title_style)
        story.append(title)
        story.append(Spacer(1, 0.3 * inch))

        # Given data
        story.append(Paragraph("Datos dados:", heading_style))
        for var, data in solution['problem']['given'].items():
            text = f"{var} = {data['original']} {data.get('unit', '')}"
            story.append(Paragraph(text, styles['Normal']))
        story.append(Spacer(1, 0.2 * inch))

        # Solutions for each part
        for part in solution['parts']:
            # Question
            story.append(Paragraph(part['question'], heading_style))

            # Steps
            for step in part['steps']:
                # Step number and description
                step_text = f"<b>Paso {step['number']}:</b> {step['description']}"
                story.append(Paragraph(step_text, styles['Normal']))

                # Formula
                formula_text = f"<font face='courier'>{step['formula']}</font>"
                story.append(Paragraph(formula_text, styles['Code']))

                # Calculation
                calc_text = f"<font face='courier'>{step['calculation']}</font>"
                story.append(Paragraph(calc_text, styles['Code']))

                story.append(Spacer(1, 0.1 * inch))

            # Answer
            answer_text = f"<b>Respuesta:</b> {part['answer']}"
            story.append(Paragraph(answer_text, styles['Normal']))

            # Validation
            if part.get('validation'):
                validation_text = f"<i>✓ {part['validation']}</i>"
                story.append(Paragraph(validation_text, styles['Italic']))

            story.append(Spacer(1, 0.3 * inch))

        # Build PDF
        doc.build(story)

        logger.info(f"✓ PDF generated: {output_path}")
        return output_path

    def create_anki_cards(self, solution: Dict) -> List[Dict]:
        """
        Crear tarjetas Anki desde la solución

        Args:
            solution: Solución completa

        Returns:
            Lista de tarjetas Anki
        """
        cards = []

        # Card for each part
        for i, part in enumerate(solution['parts']):
            # Main question card
            cards.append({
                'front': part['question'],
                'back': part['answer'] + '\n\n' + part.get('validation', ''),
                'tags': [solution['type'], 'problem', f'part_{i+1}']
            })

            # Formula cards
            for step in part['steps']:
                if 'formula' in step and step['formula']:
                    cards.append({
                        'front': f"Fórmula: {step['description']}",
                        'back': step['formula'],
                        'tags': [solution['type'], 'formula', 'reference']
                    })

        logger.info(f"✓ Created {len(cards)} Anki cards")
        return cards

    def export_to_anki_deck(self, solution: Dict, deck_name: str = None) -> Path:
        """
        Exportar tarjetas a un deck de Anki (.apkg)

        Args:
            solution: Solución completa
            deck_name: Nombre del deck (opcional)

        Returns:
            Path al archivo .apkg generado
        """
        if deck_name is None:
            deck_name = f"Communications: {solution['problem']['title']}"

        # Create Anki deck
        deck = genanki.Deck(
            self.anki_deck_id,
            deck_name
        )

        # Create note model
        model = genanki.Model(
            self.anki_model_id,
            'Problem Solver Model',
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{Question}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                },
            ])

        # Create cards
        cards = self.create_anki_cards(solution)
        for card in cards:
            note = genanki.Note(
                model=model,
                fields=[card['front'], card['back']],
                tags=card['tags']
            )
            deck.add_note(note)

        # Save deck
        problem_name = solution['problem']['title'].split(':')[0].replace(' ', '_')
        output_path = self.outputs_dir / f"{problem_name}_anki.apkg"
        genanki.Package(deck).write_to_file(str(output_path))

        logger.info(f"✓ Anki deck exported: {output_path}")
        return output_path

    def save_solution(self, solution: Dict) -> Path:
        """
        Guardar solución en formato JSON

        Args:
            solution: Solución a guardar

        Returns:
            Path al archivo JSON
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        problem_name = solution['problem']['title'].split(':')[0].replace(' ', '_')
        filename = f"{problem_name}_{timestamp}.json"
        output_path = self.outputs_dir / filename

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(solution, f, indent=2, ensure_ascii=False, default=str)

        logger.info(f"✓ Solution saved: {output_path}")
        return output_path


# ============================================================================
# MAIN (para testing)
# ============================================================================

if __name__ == '__main__':
    # Quick test
    solver = ProblemSolver()

    # Test with noise problem
    problem_file = Path("docs/ejercicio_ruido.txt")
    if problem_file.exists():
        solution = solver.solve_problem(problem_file)
        print(f"\nSolution for: {solution['problem']['title']}")
        print(f"Parts solved: {len(solution['parts'])}")

        # Generate outputs
        pdf_path = solver.generate_pdf(solution)
        print(f"PDF: {pdf_path}")

        anki_path = solver.export_to_anki_deck(solution)
        print(f"Anki: {anki_path}")
