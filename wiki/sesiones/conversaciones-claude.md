---
tags:
  - wiki/sesiones
source_file: claude-conversations/
---

# Conversaciones Claude

> **Last verified:** 2026-06-02 | **Verified by:** [source]

Índice de conversaciones históricas con Claude que contienen discusiones y soluciones sobre conceptos del curso. Cada entrada linkea a la conversación original y a las páginas del wiki relacionadas.

---

## Herramientas Matemáticas

### Potencia de señal, Parseval y Fourier
- [[claude-conversations/2025-11-04_signal-power-calculations-and-mean-value-expressions|Potencia de señal y expresiones de valor medio]]
  - Cálculo de potencia RMS, varianza, teorema de Parseval, análisis de Fourier.
  - Wiki: [[herramientas-matematicas/teorema-parseval]], [[herramientas-matematicas/senales-energia-potencia]], [[herramientas-matematicas/transformada-fourier]]

---

## Modulación Analógica

### Separación de canales FM y ancho de banda real
- [[claude-conversations/2025-11-19_separaci-n-de-canales-fm-y-ancho-de-banda-real|Separación de canales FM y ancho de banda real]]
  - Espaciado de 200 kHz en FM broadcast, regla de Carson ($BW = 2(\Delta f + f_m)$), bandas de guarda, diseño real de FM.
  - Wiki: [[modulacion-analogica/ancho-banda-carson]], [[modulacion-analogica/fm-estereo]], [[modulacion-analogica/fm-vs-pm]]

### BPSK sobre FM en telemetría espacial
- [[claude-conversations/2025-11-20_modulaci-n-bpsk-sobre-fm-en-telemetr-a-espacial|BPSK sobre FM en telemetría espacial]]
  - Modulación en cascada BPSK→FM, envolvente constante, efecto de captura, aplicaciones espaciales.
  - Wiki: [[modulacion-digital/ask-fsk-psk]], [[modulacion-analogica/fm-vs-pm]], [[modulacion-digital/constelaciones]]

---

## Modulación de Pulsos

### Muestreo, Nyquist y reconstrucción
- [[claude-conversations/2025-11-05_understanding-an-explanation|Entendiendo muestreo y Nyquist]]
  - Muestreo ideal vs real, teorema de Nyquist, tren de pulsos, reconstrucción de señal.
  - Wiki: [[modulacion-pulsos/muestreo-ideal-natural]], [[herramientas-matematicas/teorema-muestreo]]

---

## Modulación Digital

### Historia de la modulación digital y conceptos de bandpass
- [[claude-conversations/2025-11-16_digital-modulation-history-and-bandpass-concepts|Historia de la modulación digital y conceptos bandpass]]
  - Evolución histórica (modems 1960s), bandpass vs baseband, necesidad de desplazar el espectro.
  - Wiki: [[modulacion-digital/comparacion-digital-analogica]], [[modulacion-digital/ask-fsk-psk]], [[conceptos-integradores/evolucion-sistemas]]

### BPSK sobre FM en telemetría espacial
- Véase también en [[#bpsk-sobre-fm-en-telemetria-espacial|Modulación Analógica]].

---

## Ruido

### Ejercicio de ruido de examen final
- [[claude-conversations/2025-11-05_final-exam-noise-exercise-solution|Ejercicio de ruido - solución de examen final]]
  - Factor de ruido ($F$), temperatura equivalente ($T_{eq}$), SNR, ruido en amplificadores, fórmula de Friis (Unidad 7).
  - Wiki: [[ruido/formula-friis]], [[ruido/factor-ruido-temperatura]], [[ruido/temperatura-ruido]], [[problemas/ejercicio-ruido]]

### Subíndices de SNR en cadena receptora RF
- [[claude-conversations/2025-12-07_sub-ndices-de-snr-en-cadena-receptora-rf|Subíndices de SNR en cadena receptora RF]]
  - $\text{SNR}_s$, $\text{SNR}_{IF}$, $\text{SNR}_R$, $\text{SNR}_b$ en cadena superheterodina, Friis para ruido en cascada, degradación entre etapas.
  - Wiki: [[ruido/formula-friis]], [[ruido/relacion-snr]], [[ruido/lna-diseno-receptor]], [[ruido/intercomparacion-sistemas]]

---

## Teoría de la Información

### Capacidad de Shannon y relación señal a ruido
- [[claude-conversations/2025-11-05_shannon-capacity-and-signal-to-noise-ratio|Capacidad de Shannon y SNR]]
  - Teorema de Shannon-Hartley ($C = B \cdot \log_2(1 + S/N)$), trade-off ancho de banda vs SNR (Unidad 9).
  - Wiki: [[teoria-informacion/teorema-shannon-hartley]], [[teoria-informacion/capacidad-canal-shannon]], [[teoria-informacion/sistema-ideal-comunicaciones]]

---

## Planificación

### Mazo Anki de fundamentos del curso
- [[claude-conversations/2025-11-07_anki-flashcard-deck-for-subject-fundamentals|Mazo Anki - 60 cartas, 10 unidades]]
  - Generación de 60 flashcards cubriendo todas las unidades del programa, estrategia de diseño.
  - Wiki: [[planificacion/mazo-anki]], [[planificacion/programa-oficial]]

### Conversión de tarjetas a formato Anki
- [[claude-conversations/2025-11-12_converting-cards-to-anki-flashcard-format|Conversión de tarjetas markdown a .apkg]]
  - Conversión técnica de formato markdown a archivo importable de Anki.
  - Wiki: [[planificacion/mazo-anki]]

### Sistema multi-agente de aprendizaje
- [[claude-conversations/2025-11-15_multi-agent-learning-system-for-communications|Sistema multi-agente para comunicaciones]]
  - Diseño de arquitectura multi-agente Claude Code: agentes de derivación, resolución de ejercicios, análisis de progreso.
  - Wiki: [[planificacion/progreso-actual]], [[sesiones/2025-11-15-sesion]]

---

## Notas

- Las conversaciones `format-text-as-markdown` y `notion-not-recognizing-markdown` son de tooling/formateo y no contienen contenido del curso.
- Todas las fechas corresponden a noviembre-diciembre 2025.
