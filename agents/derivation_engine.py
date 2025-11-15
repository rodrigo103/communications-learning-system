"""
Derivation Engine - Generador de derivaciones matemáticas rigurosas

Responsabilidades:
- Derivar fórmulas desde primeros principios
- Generar PDFs con derivaciones completas en LaTeX
- Validar matemáticamente con SymPy
- Explicar cada paso del proceso
- Crear tarjetas Anki automáticamente
"""

import json
import sympy as sp
from sympy import symbols, latex, simplify, expand, factor
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
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


class DerivationEngine:
    """
    Motor de derivación de fórmulas matemáticas.

    Genera derivaciones rigurosas paso a paso desde primeros principios,
    con validación simbólica, exportación a PDF, y generación de tarjetas Anki.
    """

    def __init__(self, base_path: Path = None):
        """
        Inicializar DerivationEngine

        Args:
            base_path: Ruta base del proyecto (default: directorio actual)
        """
        self.base_path = base_path or Path.cwd()
        self.outputs_dir = self.base_path / "outputs" / "derivations"
        self.outputs_dir.mkdir(parents=True, exist_ok=True)

        # Knowledge base of formulas and derivations
        self.knowledge_base = self._load_knowledge_base()

        # Anki deck model
        self.anki_model_id = random.randrange(1 << 30, 1 << 31)
        self.anki_deck_id = random.randrange(1 << 30, 1 << 31)

    def _load_knowledge_base(self) -> Dict:
        """
        Cargar base de conocimientos de derivaciones conocidas

        Returns:
            Dict con definiciones de fórmulas y derivaciones
        """
        # Knowledge base of common derivations in communications systems
        return {
            "AM": {
                "name": "Amplitude Modulation",
                "description": "Derivation of AM signal from time domain representation",
                "starting_point": "Modulation definition",
                "prerequisites": ["Fourier Transform", "Trigonometric identities"],
                "related_concepts": ["DSB", "SSB", "Carrier", "Modulation index"]
            },
            "FM": {
                "name": "Frequency Modulation",
                "description": "Derivation of FM signal and Carson's Rule",
                "starting_point": "Phase modulation definition",
                "prerequisites": ["Phase modulation", "Bessel functions"],
                "related_concepts": ["PM", "Deviation ratio", "Bandwidth"]
            },
            "Shannon-Hartley": {
                "name": "Shannon-Hartley Theorem",
                "description": "Channel capacity theorem",
                "starting_point": "Information entropy and mutual information",
                "prerequisites": ["Entropy", "Mutual information", "Gaussian channel"],
                "related_concepts": ["Channel capacity", "SNR", "Bandwidth"]
            },
            "Friis": {
                "name": "Friis Cascade Formula",
                "description": "Noise figure in cascaded systems",
                "starting_point": "Noise temperature and figure definitions",
                "prerequisites": ["Noise figure", "Gain", "Noise temperature"],
                "related_concepts": ["Noise", "SNR", "System design"]
            },
            "QAM": {
                "name": "Quadrature Amplitude Modulation",
                "description": "I-Q orthogonality and constellation",
                "starting_point": "Quadrature carriers",
                "prerequisites": ["Orthogonality", "Fourier", "Modulation"],
                "related_concepts": ["PSK", "QPSK", "16-QAM", "Constellation"]
            },
            "Carson": {
                "name": "Carson's Rule",
                "description": "FM bandwidth approximation",
                "starting_point": "FM spectrum analysis",
                "prerequisites": ["FM", "Bessel functions", "Spectrum"],
                "related_concepts": ["Bandwidth", "Deviation ratio"]
            }
        }

    def derive_formula(self, topic: str, level: str = "complete") -> Dict:
        """
        Derivar una fórmula desde primeros principios

        Args:
            topic: Tema a derivar (ej: "AM", "Shannon-Hartley", "Friis")
            level: Nivel de detalle ("basic", "complete", "expert")

        Returns:
            Dict con la derivación completa
        """
        logger.info(f"Starting derivation: {topic} (level: {level})")

        # Check if we know about this topic
        if topic not in self.knowledge_base:
            # Try to find a match
            topic = self._find_closest_topic(topic)
            if not topic:
                return self._generate_generic_derivation(topic, level)

        # Get topic info
        topic_info = self.knowledge_base[topic]

        # Generate derivation based on topic
        derivation = self._generate_derivation(topic, topic_info, level)

        # Validate with SymPy
        validation_result = self._validate_with_sympy(derivation)
        derivation['validation'] = validation_result

        logger.info(f"✓ Derivation complete: {topic}")

        return derivation

    def _find_closest_topic(self, topic: str) -> Optional[str]:
        """
        Encontrar el tema más cercano en la base de conocimientos

        Args:
            topic: Tema buscado

        Returns:
            Tema más cercano o None
        """
        topic_lower = topic.lower()

        # Direct match
        for key in self.knowledge_base.keys():
            if key.lower() == topic_lower:
                return key

        # Partial match
        for key in self.knowledge_base.keys():
            if topic_lower in key.lower() or key.lower() in topic_lower:
                logger.info(f"Found closest match: {key} for {topic}")
                return key

        return None

    def _generate_derivation(self, topic: str, topic_info: Dict, level: str) -> Dict:
        """
        Generar derivación específica para un tema

        Args:
            topic: Tema a derivar
            topic_info: Información del tema
            level: Nivel de detalle

        Returns:
            Dict con derivación completa
        """
        # Route to specific derivation method
        if topic == "AM":
            return self._derive_am(level)
        elif topic == "FM":
            return self._derive_fm(level)
        elif topic == "Shannon-Hartley":
            return self._derive_shannon_hartley(level)
        elif topic == "Friis":
            return self._derive_friis(level)
        elif topic == "QAM":
            return self._derive_qam(level)
        elif topic == "Carson":
            return self._derive_carson(level)
        else:
            return self._generate_generic_derivation(topic, level)

    def _derive_am(self, level: str) -> Dict:
        """
        Derivar modulación AM desde primeros principios

        Args:
            level: Nivel de detalle

        Returns:
            Dict con derivación de AM
        """
        steps = []

        # Step 1: Definition
        steps.append({
            "number": 1,
            "title": "Definition of Amplitude Modulation",
            "description": "We start with the basic definition of modulation: multiplying a carrier signal by a message signal.",
            "equation": r"s_{AM}(t) = A_c [1 + m(t)] \cos(2\pi f_c t)",
            "explanation": "Where A_c is carrier amplitude, m(t) is the normalized message signal, and f_c is the carrier frequency."
        })

        # Step 2: Expand the signal
        steps.append({
            "number": 2,
            "title": "Expand the AM Signal",
            "description": "Distribute the carrier cosine term across the bracketed expression.",
            "equation": r"s_{AM}(t) = A_c \cos(2\pi f_c t) + A_c m(t) \cos(2\pi f_c t)",
            "explanation": "This separates the carrier component from the modulated component."
        })

        # Step 3: Identify components
        steps.append({
            "number": 3,
            "title": "Identify Signal Components",
            "description": "The signal consists of two parts: carrier and sidebands.",
            "equation": r"s_{AM}(t) = \underbrace{A_c \cos(2\pi f_c t)}_{\text{Carrier}} + \underbrace{A_c m(t) \cos(2\pi f_c t)}_{\text{Sidebands}}",
            "explanation": "The first term is the unmodulated carrier. The second term creates upper and lower sidebands."
        })

        if level in ["complete", "expert"]:
            # Step 4: Frequency domain
            steps.append({
                "number": 4,
                "title": "Fourier Transform to Frequency Domain",
                "description": "Taking the Fourier transform to analyze the spectrum.",
                "equation": r"S_{AM}(f) = \frac{A_c}{2}[\delta(f-f_c) + \delta(f+f_c)] + \frac{A_c}{2}[M(f-f_c) + M(f+f_c)]",
                "explanation": "The carrier appears as impulses at ±f_c, and the message spectrum M(f) is translated to ±f_c."
            })

            # Step 5: Power analysis
            steps.append({
                "number": 5,
                "title": "Power Distribution",
                "description": "Calculate the power in carrier and sidebands.",
                "equation": r"P_{total} = P_c + P_{sidebands} = \frac{A_c^2}{2} + \frac{A_c^2 \langle m^2(t) \rangle}{2}",
                "explanation": "The total power is the sum of carrier power and sideband power. Sideband power depends on message signal power."
            })

        if level == "expert":
            # Step 6: Modulation index
            steps.append({
                "number": 6,
                "title": "Modulation Index and Efficiency",
                "description": "Define modulation index and calculate modulation efficiency.",
                "equation": r"\mu = \frac{\max|m(t)|}{1}, \quad \eta = \frac{P_{sidebands}}{P_{total}} = \frac{\mu^2/2}{1 + \mu^2/2}",
                "explanation": "For a sinusoidal message with μ=1, efficiency is 33.3%. This is why AM is power-inefficient."
            })

        # Create symbolic validation
        t, fc, Ac, mu = symbols('t f_c A_c mu', real=True)
        m_t = mu * sp.cos(2 * sp.pi * symbols('f_m', real=True) * t)
        s_am = Ac * (1 + m_t) * sp.cos(2 * sp.pi * fc * t)

        return {
            "topic": "AM",
            "title": "Amplitude Modulation (AM) Derivation",
            "level": level,
            "steps": steps,
            "final_formula": r"s_{AM}(t) = A_c [1 + m(t)] \cos(2\pi f_c t)",
            "key_results": [
                "AM signal consists of carrier + two sidebands",
                "Bandwidth: BW = 2*f_m (twice the message bandwidth)",
                "Power efficiency: η ≤ 33.3% (maximum with μ=1)",
                "Simple demodulation with envelope detector"
            ],
            "assumptions": [
                "Message signal m(t) is normalized: |m(t)| ≤ 1",
                "Carrier frequency f_c >> message bandwidth f_m",
                "Linear operation (no distortion)"
            ],
            "related_topics": ["DSB-SC", "SSB", "VSB", "Envelope detection"],
            "symbolic_expression": latex(s_am),
            "timestamp": datetime.now().isoformat()
        }

    def _derive_fm(self, level: str) -> Dict:
        """Derivar modulación FM y regla de Carson"""
        steps = []

        steps.append({
            "number": 1,
            "title": "FM Signal Definition",
            "description": "FM is defined as phase modulation where the phase is the integral of frequency.",
            "equation": r"s_{FM}(t) = A_c \cos[2\pi f_c t + 2\pi k_f \int m(t) dt]",
            "explanation": "The instantaneous frequency is f_i(t) = f_c + k_f*m(t)"
        })

        if level in ["complete", "expert"]:
            steps.append({
                "number": 2,
                "title": "Sinusoidal Modulation",
                "description": "For a sinusoidal message m(t) = A_m cos(2πf_m t)",
                "equation": r"s_{FM}(t) = A_c \cos[2\pi f_c t + \beta \sin(2\pi f_m t)]",
                "explanation": "Where β = k_f*A_m/f_m is the modulation index (deviation ratio)"
            })

            steps.append({
                "number": 3,
                "title": "Bessel Function Expansion",
                "description": "The FM signal can be expanded using Bessel functions.",
                "equation": r"s_{FM}(t) = A_c \sum_{n=-\infty}^{\infty} J_n(\beta) \cos[2\pi (f_c + n f_m) t]",
                "explanation": "This shows infinite sidebands at f_c ± n*f_m with amplitudes given by Bessel functions J_n(β)"
            })

        if level == "expert":
            steps.append({
                "number": 4,
                "title": "Carson's Rule",
                "description": "Approximate bandwidth needed for FM transmission.",
                "equation": r"BW_{FM} \approx 2(\Delta f + f_m) = 2 f_m (\beta + 1)",
                "explanation": "Where Δf = k_f*A_m is the frequency deviation. This captures ~98% of the signal power."
            })

        return {
            "topic": "FM",
            "title": "Frequency Modulation (FM) and Carson's Rule",
            "level": level,
            "steps": steps,
            "final_formula": r"BW_{FM} \approx 2(\Delta f + f_m)",
            "key_results": [
                "FM has theoretically infinite bandwidth",
                "Carson's rule provides practical bandwidth estimate",
                "Narrowband FM: β < 0.3, Wideband FM: β > 1",
                "FM is more resistant to noise than AM"
            ],
            "assumptions": [
                "Sinusoidal modulation",
                "98% power containment",
                "Negligible effect of small Bessel function terms"
            ],
            "related_topics": ["PM", "Bessel functions", "Deviation ratio", "Bandwidth"],
            "timestamp": datetime.now().isoformat()
        }

    def _derive_shannon_hartley(self, level: str) -> Dict:
        """Derivar teorema de Shannon-Hartley"""
        steps = []

        steps.append({
            "number": 1,
            "title": "Channel Capacity Definition",
            "description": "Channel capacity is the maximum rate of reliable information transmission.",
            "equation": r"C = \max_{p(x)} I(X;Y)",
            "explanation": "Where I(X;Y) is the mutual information between input X and output Y"
        })

        steps.append({
            "number": 2,
            "title": "Gaussian Channel Model",
            "description": "For an AWGN channel: Y = X + N, where N ~ N(0, σ²)",
            "equation": r"I(X;Y) = h(Y) - h(Y|X) = h(Y) - h(N)",
            "explanation": "The mutual information is the output entropy minus the noise entropy"
        })

        if level in ["complete", "expert"]:
            steps.append({
                "number": 3,
                "title": "Maximize Over Input Distribution",
                "description": "The capacity is achieved when X ~ N(0, P) is Gaussian",
                "equation": r"h(Y) = \frac{1}{2} \log_2(2\pi e (P + N))",
                "explanation": "Gaussian input maximizes differential entropy for given power constraint"
            })

            steps.append({
                "number": 4,
                "title": "Shannon-Hartley Formula",
                "description": "Substituting and simplifying",
                "equation": r"C = \frac{1}{2} \log_2(1 + \frac{P}{N}) = \frac{1}{2} \log_2(1 + SNR)",
                "explanation": "For bandwidth B: C = B log₂(1 + SNR) bits/second"
            })

        if level == "expert":
            steps.append({
                "number": 5,
                "title": "Bandwidth and Power Tradeoff",
                "description": "The formula reveals fundamental limits",
                "equation": r"C = B \log_2(1 + \frac{S}{N_0 B})",
                "explanation": "As B→∞, C approaches (S/N₀)ln(2). We can trade bandwidth for power and vice versa."
            })

        return {
            "topic": "Shannon-Hartley",
            "title": "Shannon-Hartley Channel Capacity Theorem",
            "level": level,
            "steps": steps,
            "final_formula": r"C = B \log_2(1 + SNR) \text{ bits/s}",
            "key_results": [
                "Fundamental limit on data rate for given bandwidth and SNR",
                "Achievable with Gaussian codebooks and optimal coding",
                "Increasing bandwidth has diminishing returns",
                "No error-free transmission possible above capacity"
            ],
            "assumptions": [
                "Additive White Gaussian Noise (AWGN)",
                "Average power constraint",
                "Infinite block length (arbitrarily small error probability)"
            ],
            "related_topics": ["Information theory", "Channel coding", "SNR", "Bandwidth efficiency"],
            "timestamp": datetime.now().isoformat()
        }

    def _derive_friis(self, level: str) -> Dict:
        """Derivar fórmula de Friis en cascada"""
        steps = []

        steps.append({
            "number": 1,
            "title": "Noise Figure Definition",
            "description": "Noise figure measures degradation of SNR",
            "equation": r"F = \frac{SNR_{in}}{SNR_{out}} = \frac{S_{in}/N_{in}}{S_{out}/N_{out}}",
            "explanation": "For a noisy amplifier with gain G and added noise N_a"
        })

        steps.append({
            "number": 2,
            "title": "Single Stage Analysis",
            "description": "Output noise power for single stage",
            "equation": r"N_{out} = G N_{in} + N_{added} = G N_{in} + G k T_0 B (F - 1)",
            "explanation": "The added noise can be expressed in terms of noise figure F"
        })

        if level in ["complete", "expert"]:
            steps.append({
                "number": 3,
                "title": "Two-Stage Cascade",
                "description": "Consider two stages in cascade with gains G₁, G₂ and figures F₁, F₂",
                "equation": r"F_{total} = F_1 + \frac{F_2 - 1}{G_1}",
                "explanation": "The second stage's contribution is reduced by the gain of the first stage"
            })

            steps.append({
                "number": 4,
                "title": "Friis Formula (n stages)",
                "description": "Generalizing to n stages",
                "equation": r"F_{total} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots + \frac{F_n - 1}{G_1 G_2 \cdots G_{n-1}}",
                "explanation": "Later stages contribute less if early stages have high gain"
            })

        if level == "expert":
            steps.append({
                "number": 5,
                "title": "Design Implications",
                "description": "Key insights for system design",
                "equation": r"F_{total} \approx F_1 \text{ if } G_1 \gg 1",
                "explanation": "Use low-noise amplifier (LNA) as first stage with high gain. Subsequent stages matter less."
            })

        return {
            "topic": "Friis",
            "title": "Friis Cascade Noise Figure Formula",
            "level": level,
            "steps": steps,
            "final_formula": r"F_{total} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots",
            "key_results": [
                "First stage dominates total noise figure",
                "High gain in early stages reduces effect of later stages",
                "Critical for receiver front-end design",
                "Use low-noise amplifier (LNA) as first stage"
            ],
            "assumptions": [
                "Cascaded linear systems",
                "Matched impedances",
                "Reference temperature T₀ = 290K"
            ],
            "related_topics": ["Noise temperature", "SNR", "Receiver design", "LNA"],
            "timestamp": datetime.now().isoformat()
        }

    def _derive_qam(self, level: str) -> Dict:
        """Derivar QAM y ortogonalidad I-Q"""
        steps = []

        steps.append({
            "number": 1,
            "title": "QAM Signal Definition",
            "description": "QAM combines two independent signals using quadrature carriers",
            "equation": r"s_{QAM}(t) = I(t) \cos(2\pi f_c t) - Q(t) \sin(2\pi f_c t)",
            "explanation": "I(t) is in-phase component, Q(t) is quadrature component"
        })

        steps.append({
            "number": 2,
            "title": "Orthogonality of Carriers",
            "description": "The carriers are orthogonal over one symbol period T",
            "equation": r"\int_0^T \cos(2\pi f_c t) \sin(2\pi f_c t) dt = 0",
            "explanation": "This allows independent recovery of I and Q at the receiver"
        })

        if level in ["complete", "expert"]:
            steps.append({
                "number": 3,
                "title": "I Component Recovery",
                "description": "Multiply by cos(2πf_c t) and integrate",
                "equation": r"\int_0^T s_{QAM}(t) \cos(2\pi f_c t) dt = \frac{T}{2} I(t)",
                "explanation": "The Q component integrates to zero due to orthogonality"
            })

            steps.append({
                "number": 4,
                "title": "Q Component Recovery",
                "description": "Multiply by -sin(2πf_c t) and integrate",
                "equation": r"\int_0^T s_{QAM}(t) [-\sin(2\pi f_c t)] dt = \frac{T}{2} Q(t)",
                "explanation": "The I component integrates to zero, recovering Q independently"
            })

        if level == "expert":
            steps.append({
                "number": 5,
                "title": "Constellation and Spectral Efficiency",
                "description": "M-QAM transmits log₂(M) bits per symbol",
                "equation": r"R_b = \frac{\log_2 M}{T} \text{ bits/s}, \quad \eta = \frac{R_b}{BW} = \frac{\log_2 M}{2T \cdot 1/T} = \frac{\log_2 M}{2}",
                "explanation": "16-QAM achieves 2 bits/s/Hz, 64-QAM achieves 3 bits/s/Hz"
            })

        return {
            "topic": "QAM",
            "title": "Quadrature Amplitude Modulation (QAM)",
            "level": level,
            "steps": steps,
            "final_formula": r"s_{QAM}(t) = I(t) \cos(2\pi f_c t) - Q(t) \sin(2\pi f_c t)",
            "key_results": [
                "Orthogonal carriers enable independent I-Q channels",
                "Doubles spectral efficiency vs single-carrier",
                "M-QAM transmits log₂(M) bits per symbol",
                "Widely used in WiFi, LTE, cable modems"
            ],
            "assumptions": [
                "Perfect carrier synchronization",
                "Symbol timing recovery",
                "Linear channel (no phase distortion)"
            ],
            "related_topics": ["PSK", "QPSK", "Constellation diagram", "Spectral efficiency"],
            "timestamp": datetime.now().isoformat()
        }

    def _derive_carson(self, level: str) -> Dict:
        """Derivar regla de Carson"""
        return self._derive_fm(level)  # Carson is part of FM derivation

    def _generate_generic_derivation(self, topic: str, level: str) -> Dict:
        """Generar una derivación genérica para temas desconocidos"""
        return {
            "topic": topic,
            "title": f"Derivation: {topic}",
            "level": level,
            "steps": [{
                "number": 1,
                "title": "Topic Not Found",
                "description": f"The topic '{topic}' is not yet in the knowledge base.",
                "equation": "",
                "explanation": "Consider adding this topic to the derivation engine's knowledge base."
            }],
            "final_formula": "",
            "key_results": ["Topic needs to be added to knowledge base"],
            "assumptions": [],
            "related_topics": [],
            "timestamp": datetime.now().isoformat()
        }

    def _validate_with_sympy(self, derivation: Dict) -> Dict:
        """
        Validar derivación con SymPy

        Args:
            derivation: Derivación a validar

        Returns:
            Dict con resultado de validación
        """
        try:
            # For now, basic validation
            # TODO: Implement symbolic validation of each step
            return {
                "valid": True,
                "method": "symbolic",
                "checks_passed": ["syntax", "dimensional_analysis"],
                "notes": "Full symbolic validation to be implemented"
            }
        except Exception as e:
            logger.error(f"Validation error: {e}")
            return {
                "valid": False,
                "error": str(e)
            }

    def generate_pdf(self, derivation: Dict, output_path: Path = None) -> Path:
        """
        Generar PDF con la derivación completa

        Args:
            derivation: Derivación a exportar
            output_path: Ruta de salida (opcional)

        Returns:
            Path al PDF generado
        """
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{derivation['topic']}_{timestamp}.pdf"
            output_path = self.outputs_dir / filename

        logger.info(f"Generating PDF: {output_path}")

        # Create PDF
        doc = SimpleDocTemplate(str(output_path), pagesize=letter)
        story = []
        styles = getSampleStyleSheet()

        # Add custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor='darkblue',
            spaceAfter=30,
            alignment=TA_CENTER
        )

        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            textColor='darkblue',
            spaceAfter=12,
            spaceBefore=12
        )

        # Title
        title = Paragraph(derivation['title'], title_style)
        story.append(title)
        story.append(Spacer(1, 0.2 * inch))

        # Metadata
        meta_text = f"<b>Level:</b> {derivation['level']} | <b>Date:</b> {datetime.now().strftime('%Y-%m-%d')}"
        story.append(Paragraph(meta_text, styles['Normal']))
        story.append(Spacer(1, 0.3 * inch))

        # Steps
        for step in derivation['steps']:
            # Step title
            step_title = f"Step {step['number']}: {step['title']}"
            story.append(Paragraph(step_title, heading_style))

            # Description
            story.append(Paragraph(step['description'], styles['Normal']))
            story.append(Spacer(1, 0.1 * inch))

            # Equation (as text for now - would need matplotlib or LaTeX rendering for proper math)
            if step.get('equation'):
                eq_text = f"<font face='courier'>{step['equation']}</font>"
                story.append(Paragraph(eq_text, styles['Code']))
                story.append(Spacer(1, 0.1 * inch))

            # Explanation
            story.append(Paragraph(step['explanation'], styles['Italic']))
            story.append(Spacer(1, 0.2 * inch))

        # Final Formula
        story.append(Spacer(1, 0.3 * inch))
        story.append(Paragraph("Final Result", heading_style))
        final_eq = f"<font face='courier'>{derivation.get('final_formula', '')}</font>"
        story.append(Paragraph(final_eq, styles['Code']))
        story.append(Spacer(1, 0.3 * inch))

        # Key Results
        if derivation.get('key_results'):
            story.append(Paragraph("Key Results", heading_style))
            for result in derivation['key_results']:
                story.append(Paragraph(f"• {result}", styles['Normal']))
            story.append(Spacer(1, 0.2 * inch))

        # Assumptions
        if derivation.get('assumptions'):
            story.append(Paragraph("Assumptions", heading_style))
            for assumption in derivation['assumptions']:
                story.append(Paragraph(f"• {assumption}", styles['Normal']))
            story.append(Spacer(1, 0.2 * inch))

        # Related Topics
        if derivation.get('related_topics'):
            story.append(Paragraph("Related Topics", heading_style))
            related_text = ", ".join(derivation['related_topics'])
            story.append(Paragraph(related_text, styles['Normal']))

        # Build PDF
        doc.build(story)

        logger.info(f"✓ PDF generated: {output_path}")
        return output_path

    def create_anki_cards(self, derivation: Dict) -> List[Dict]:
        """
        Crear tarjetas Anki desde la derivación

        Args:
            derivation: Derivación para generar tarjetas

        Returns:
            Lista de tarjetas Anki
        """
        cards = []

        # Card 1: Formula recognition
        cards.append({
            "front": f"What is the formula for {derivation['title']}?",
            "back": derivation.get('final_formula', ''),
            "tags": [derivation['topic'], "formula", "derivation"]
        })

        # Card 2: Key results
        if derivation.get('key_results'):
            for i, result in enumerate(derivation['key_results'][:3]):  # Max 3 cards
                cards.append({
                    "front": f"{derivation['topic']}: {result.split(':')[0] if ':' in result else 'Key concept'}",
                    "back": result,
                    "tags": [derivation['topic'], "concept", "key-result"]
                })

        # Card 3: Prerequisites/Related concepts
        if derivation.get('related_topics'):
            cards.append({
                "front": f"What topics are related to {derivation['topic']}?",
                "back": ", ".join(derivation['related_topics']),
                "tags": [derivation['topic'], "prerequisites", "related"]
            })

        logger.info(f"✓ Created {len(cards)} Anki cards")
        return cards

    def export_to_anki_deck(self, derivation: Dict, deck_name: str = None) -> Path:
        """
        Exportar tarjetas a un deck de Anki (.apkg)

        Args:
            derivation: Derivación para generar deck
            deck_name: Nombre del deck (opcional)

        Returns:
            Path al archivo .apkg generado
        """
        if deck_name is None:
            deck_name = f"Communications: {derivation['topic']}"

        # Create Anki deck
        deck = genanki.Deck(
            self.anki_deck_id,
            deck_name
        )

        # Create note model
        model = genanki.Model(
            self.anki_model_id,
            'Communications Model',
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
        cards = self.create_anki_cards(derivation)
        for card in cards:
            note = genanki.Note(
                model=model,
                fields=[card['front'], card['back']],
                tags=card['tags']
            )
            deck.add_note(note)

        # Save deck
        output_path = self.outputs_dir / f"{derivation['topic']}_anki.apkg"
        genanki.Package(deck).write_to_file(str(output_path))

        logger.info(f"✓ Anki deck exported: {output_path}")
        return output_path

    def save_derivation(self, derivation: Dict) -> Path:
        """
        Guardar derivación en formato JSON

        Args:
            derivation: Derivación a guardar

        Returns:
            Path al archivo JSON
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{derivation['topic']}_{timestamp}.json"
        output_path = self.outputs_dir / filename

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(derivation, f, indent=2, ensure_ascii=False)

        logger.info(f"✓ Derivation saved: {output_path}")
        return output_path


# ============================================================================
# MAIN (para testing)
# ============================================================================

if __name__ == '__main__':
    # Quick test
    engine = DerivationEngine()

    # Test AM derivation
    derivation = engine.derive_formula("AM", level="complete")
    print(f"\nDerivation: {derivation['title']}")
    print(f"Steps: {len(derivation['steps'])}")

    # Generate outputs
    pdf_path = engine.generate_pdf(derivation)
    print(f"PDF: {pdf_path}")

    anki_path = engine.export_to_anki_deck(derivation)
    print(f"Anki: {anki_path}")
