---
tags:
  - wiki/planificacion
source_file: ProgramaSistemasDeComunicaciones.md
curso: Sistemas de Comunicaciones
unidad: null
---

# Programa Oficial: Sistemas de Comunicaciones (UTN)

> **Last verified:** 2025-11-16 | **Verified by:** source

## Datos generales

- **Carrera:** Ingeniería Electrónica, UTN
- **Evaluación:** 2 parciales escritos + examen final oral teórico-integrador con resolución de problema
- **Regularidad:** 70% de presentismo
- **Bibliografía obligatoria:** Stremler, Carlson, Tomasi, Haykin, Couch, Schwartz [source — [[../../ProgramaSistemasDeComunicaciones]]]

## Contenidos por unidad

### Unidad 1: Introducción
Conceptos generales de sistemas de comunicación electrónica. Uso racional del espectro electromagnético. Organismos de normalización nacionales e internacionales.
- [[../introduccion/elementos-sistema]]
- [[../introduccion/espectro-electromagnetico]]
- [[../introduccion/organismos-normalizacion]]

### Unidad 2: Análisis de Señales
Serie y transformada de Fourier. Espectros de amplitud y fase. Densidad espectral. [[../herramientas-matematicas/teorema-parseval|Teorema de Parseval]]. Teorema de convolución. Función impulso. Espectros de potencia y correlación. [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]]. Señal analítica. Deducción de BLU.
- [[../herramientas-matematicas/serie-fourier]]
- [[../herramientas-matematicas/transformada-fourier]]
- [[../herramientas-matematicas/densidad-espectral-potencia]]
- [[../herramientas-matematicas/teorema-wiener-khinchin]]
- [[../derivaciones/teorema-parseval]]

### Unidad 3: Modulación Lineal
AM, DBL (DSB), BLU (SSB), Banda Lateral Vestigial (VSB). Moduladores: balanceado, en anillo, por desplazamiento de fase. Formas de onda, espectros, anchos de banda y potencias. Detectores lineales. Detección sincrónica. Receptor superheterodino. Múltiplex en frecuencia (FDM).
- [[../modulacion-analogica/am-vs-dsb-sc]]
- [[../modulacion-analogica/indice-modulacion-am]]
- [[../modulacion-analogica/receptor-superheterodino]]
- [[../derivaciones/modulacion-am]]

### Unidad 4: Modulación Exponencial
FM y PM. Modulación multitono. Espectros de banda ancha y banda angosta. [[../modulacion-analogica/ancho-banda-carson|Regla de Carson]]. Moduladores y detectores. Multiplicadores de frecuencia. FM estéreo.
- [[../modulacion-analogica/fm-vs-pm]]
- [[../modulacion-analogica/fm-banda-angosta]]
- [[../modulacion-analogica/fm-banda-ancha]]
- [[../derivaciones/modulacion-fm-carson]]
- [[../derivaciones/modulacion-fm-banda-angosta]]

### Unidad 5: Modulación de Pulsos
[[../herramientas-matematicas/teorema-muestreo|Teorema de muestreo]]. Muestreo ideal y natural. PAM, PWM, PPM. [[../modulacion-pulsos/pcm|PCM]]: cuantificación, error, companding (Ley A, Ley $\mu$). SQNR $\approx 6n + 1.76$ dB. Modulación Delta y Delta adaptativa. Codificación de línea. TDM en PCM, jerarquías.
- [[../modulacion-pulsos/cuantificacion]]
- [[../modulacion-pulsos/tdm]]
- [[../modulacion-pulsos/companding]]

### Unidad 6: Modulación Digital
[[../modulacion-digital/ask-fsk-psk|ASK, FSK, PSK]] (M-arios) y [[../modulacion-digital/modulacion-qam|QAM]]. [[../modulacion-digital/constelaciones|Constelaciones]]. Espectros, anchos de banda. Velocidad de señalización vs tasa de información. Probabilidad de error y relación S/R. Comparación digital vs analógica.
- [[../modulacion-digital/probabilidad-error]]
- [[../modulacion-digital/comparacion-digital-analogica]]
- [[../derivaciones/modulacion-qam]]
- [[../resumenes/modulacion-digital-unidad6]]

### Unidad 7: Ruido y Radio Interferencias
Fuentes de ruido. Ruido blanco y de banda angosta. Potencia disponible de ruido ($P_n = kTB$). [[../ruido/factor-ruido-temperatura|Temperatura y figura de ruido]]. Relación señal a ruido. [[../ruido/formula-friis|Fórmula de Friis]] para cuadripolos en cascada. Atenuadores.
- [[../ruido/fuentes-ruido]]
- [[../ruido/ruido-termico]]
- [[../derivaciones/ecuacion-friis]]

### Unidad 8: Intercomparación de Sistemas
Ruido de banda angosta: modelo estadístico. SNR para modulación lineal (AM, DSB, SSB). [[../ruido/efecto-umbral-fm|Efecto umbral]]. SNR en PM y FM. Redes de énfasis. SNR en modulación de pulsos analógica. Intercomparación global.
- [[../ruido/intercomparacion-sistemas]]
- [[../ruido/snr-modulacion-lineal]]

### Unidad 9: Teoría de la Información
[[../teoria-informacion/entropia|Entropía]] ($H = -\sum p_i \log_2 p_i$). Información mutua. [[../teoria-informacion/capacidad-canal-shannon|Capacidad de canal]]. [[../teoria-informacion/teorema-shannon-hartley|Teorema de Shannon-Hartley]] ($C = B\log_2(1+SNR)$). Codificación de fuente (Huffman). Codificación de canal (detección/corrección de errores).
- [[../teoria-informacion/codificacion-canal]]
- [[../derivaciones/teorema-shannon-hartley]]

### Unidad 10: Espectro Expandido y OFDM
[[../espectro-expandido/cdma|CDMA]]: secuencia directa (DSSS), salto de frecuencia (FHSS). Correlación. [[../espectro-expandido/ofdm|OFDM]]: principio, FFT/IFFT, prefijo cíclico, ortogonalidad, aplicaciones.
- [[../espectro-expandido/dsss]]
- [[../espectro-expandido/fhss]]

## Referencia bibliográfica

- Ferrel G. Stremler: *Introducción a los Sistemas de Comunicaciones*
- Bruce Carlson: *Sistemas de Comunicación*
- Wayne Tomasi: *Sistemas de Comunicaciones Electrónicas*
- Simon Haykin: *Sistemas de Comunicaciones*
- Leon W. Couch: *Sistemas de Comunicación Digitales y Analógicos*
- Mischa Schwartz: *Transmisión de la Información, Modulación y Ruido*
- Norman Abrahmson: *Teoría de la Información y Codificación*

## Ver también

- [[../planificacion/progreso-actual]]
- [[../planificacion/mazo-anki]]
- [[../resumenes/overview-curso]]
- [[../../outputs/mindmaps/communications_systems_course_overview_20251116|Mapa mental del curso]] — Estructura visual de contenidos
