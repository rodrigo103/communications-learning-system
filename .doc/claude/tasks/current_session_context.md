# Current Session Context

## Session Goal
Fix Mermaid parsing error in the communications systems course mind map - equations are not rendering correctly.

## Source Materials
- **ProgramaSistemasDeComunicaciones.md**: Official course syllabus with 10 units
- **Mazo_Anki_Sistemas_Comunicaciones.md**: 60 flashcards covering key concepts from all units

## Course Structure Overview

### 10 Main Units:
1. **Introducción** - Communication systems basics, spectrum management
2. **Análisis de Señales** - Fourier, Parseval, sampling, Hilbert transform
3. **Modulación Lineal** - AM, DSB, SSB, VSB, superheterodyne receivers
4. **Modulación Exponencial** - FM, PM, Carson's rule, pre-emphasis
5. **Modulación de Pulsos** - PAM, PWM, PPM, PCM, companding, TDM
6. **Modulación Digital** - ASK, FSK, PSK, QAM, constellations, BER
7. **Ruido** - White noise, noise figure, Friis formula, SNR analysis
8. **Intercomparación de Sistemas** - Comparison metrics, efficiency trade-offs
9. **Teoría de la Información** - Entropy, Shannon-Hartley, channel capacity, coding
10. **Spread Spectrum y OFDM** - DSSS, FHSS, CDMA, OFDM principles

## Key Themes to Visualize
- Hierarchy of units and subtopics
- Relationships between modulation techniques
- Trade-offs (bandwidth vs power, spectral vs power efficiency)
- Evolution from analog to digital
- Theoretical foundations (Fourier, Shannon) connecting multiple units

## Current Issue
Mind map was created but has Mermaid parsing error:
```
MermaidDetailedError: Parse error on line 35:
...    `$E = \int |s(t)|^2 dt = \int |S(f)|
-----------------------^
Expecting 'SPACELINE', 'NL', 'EOF', got 'NODE_ID'
```

**Problem**: Mathematical formulas with backticks and LaTeX notation are causing parsing errors in Mermaid mindmap syntax.

**File location**: outputs/mindmaps/communications_systems_course_overview_20251116.md

**Lines with equations** (from grep search):
- Line 83: Parseval theorem equation
- Line 95: AM signal equation
- Line 100, 112: Bandwidth formulas
- Line 126-139: FM/PM equations
- Line 153-176: Sampling and PCM equations
- Line 185-187: Digital modulation formulas
- Line 223-239: Noise formulas

## Task
Fix the Mermaid mindmap so equations render correctly. Research proper Mermaid syntax for including mathematical formulas in mindmap nodes. All ~20 equations need to be fixed while preserving their mathematical meaning.

## Requirements
- Equations must display correctly in Mermaid
- Preserve mathematical accuracy
- Test that the fixed version parses without errors
- Keep all other content unchanged
