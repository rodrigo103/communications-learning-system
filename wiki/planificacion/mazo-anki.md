---
tags:
  - wiki/planificacion
source_file: Mazo_Anki_Sistemas_Comunicaciones.md
curso: Sistemas de Comunicaciones
unidad: null
---

# Mazo Anki: Sistemas de Comunicaciones

> **Last verified:** 2025-11-16 | **Verified by:** source

## Visión general

El mazo Anki contiene **60 cartas fundamentales** que cubren las 10 unidades del curso más 5 cartas de conceptos integradores. Las cartas siguen el formato pregunta-respuesta con ecuaciones en LaTeX (compatible con MathJax en Anki).

## Distribución por unidad

| Unidad | Cartas | Temas cubiertos |
|--------|--------|-----------------|
| 1 | 3 | Elementos del sistema, necesidad de modulación, espectro EM |
| 2 | 6 | Parseval, Nyquist, densidad espectral, convolución, Hilbert, señales de energía/potencia |
| 3 | 6 | AM vs DSB-SC, SSB, superheterodino, índice de modulación, modulador balanceado, VSB |
| 4 | 6 | FM vs PM, $\beta$ y NBFM/WBFM, Carson, discriminador, pre/éénfasis, comparación FM-PM |
| 5 | 5 | PAM/PWM/PPM, PCM, companding, Delta/ADM, TDM |
| 6 | 6 | ASK/FSK/PSK comparación, constelaciones, QAM, baud rate vs bit rate, BER, detección coherente |
| 7 | 7 | Ruido blanco, temperatura de ruido, figura de ruido F/NF, Friis, ruido banda angosta, AM con ruido, efecto umbral FM |
| 8 | 4 | Parámetros de comparación, eficiencia espectral, ganancia de procesamiento, pre/éénfasis en comparación |
| 9 | 6 | Entropía, Shannon-Hartley, redundancia, códigos óptimos, detección/corrección, analógico vs digital |
| 10 | 6 | Spread Spectrum, DSSS vs FHSS, CDMA, OFDM, aplicaciones OFDM, prefijo cíclico |
| Integradores | 5 | Trade-off BW-potencia, $E_b/N_0$ vs SNR, eficiencia espectral vs potencia, regeneración digital, evolución histórica |

## Cómo usar el mazo

### Importación a Anki
1. Las cartas están en formato pregunta-respuesta en markdown
2. Recomendado: crear mazos separados por unidad como sub-decks
3. Usar tags para clasificar por tema y dificultad
4. Las ecuaciones usan LaTeX `$$...$$` — Anki lo renderiza con MathJax

### Estrategia de estudio
1. **Orden:** Estudiar en orden numérico (respeta dependencias conceptuales)
2. **No memorizar mecánicamente:** Entender las derivaciones subyacentes
3. **Complementar:** Usar junto con los problemas resueltos y derivaciones
4. **Relacionar:** Identificar conexiones entre unidades (ej: Fourier → modulación, Friis → diseño de receptores)

## Cobertura por categoría del wiki

Las cartas están alineadas con estas áreas del wiki:

- **Introducción (U1):** [[../introduccion/elementos-sistema]], [[../introduccion/espectro-electromagnetico]]
- **Herramientas matemáticas (U2):** [[../herramientas-matematicas/teorema-parseval]], [[../herramientas-matematicas/transformada-fourier]], [[../herramientas-matematicas/transformada-hilbert]]
- **Modulación analógica (U3-U4):** [[../modulacion-analogica/am-vs-dsb-sc]], [[../modulacion-analogica/ancho-banda-carson]], [[../modulacion-analogica/fm-vs-pm]]
- **Modulación de pulsos (U5):** [[../modulacion-pulsos/pcm]], [[../herramientas-matematicas/teorema-muestreo]]
- **Modulación digital (U6):** [[../modulacion-digital/ask-fsk-psk]], [[../modulacion-digital/constelaciones]], [[../modulacion-digital/probabilidad-error]]
- **Ruido (U7):** [[../ruido/factor-ruido-temperatura]], [[../ruido/formula-friis]], [[../ruido/ruido-termico]]
- **Intercomparación (U8):** [[../ruido/intercomparacion-sistemas]], [[../ruido/efecto-umbral-fm]]
- **Teoría de la información (U9):** [[../teoria-informacion/entropia]], [[../teoria-informacion/teorema-shannon-hartley]]
- **Temas avanzados (U10):** [[../espectro-expandido/cdma]], [[../espectro-expandido/dsss]], [[../espectro-expandido/ofdm]]
- **Integradores:** [[../conceptos-integradores/trade-off-bw-potencia]], [[../conceptos-integradores/evolucion-sistemas]]

## Fórmulas clave incluidas

| Carta | Fórmula |
|-------|---------|
| Parseval | $\int \|x(t)\|^2 dt = \int \|X(f)\|^2 df$ |
| Nyquist | $f_s \geq 2f_{max}$ |
| Carson | $BW \approx 2(\Delta f + f_m)$ |
| PCM SQNR | $SNR_q \approx 6n + 1.76$ dB |
| Shannon | $C = B\log_2(1 + SNR)$ |
| Friis | $F_{total} = F_1 + \frac{F_2-1}{G_1} + \cdots$ |
| $E_b/N_0$ | $E_b/N_0 = (S/N) \cdot (B/R_b)$ |

## Ver también

- [[../planificacion/programa-oficial]]
- [[../planificacion/progreso-actual]]
- [[../resumenes/overview-curso]]
- [[../../claude-conversations/2025-11-07_anki-flashcard-deck-for-subject-fundamentals|Conversación: mazo Anki de fundamentos]]
- [[../../claude-conversations/2025-11-12_converting-cards-to-anki-flashcard-format|Conversación: conversión de tarjetas a .apkg]]
