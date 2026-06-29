---
tags:
  - wiki/planificacion
curso: Sistemas de Comunicaciones
---

# Plan de Estudio: Enfoque por Modulaciones

> **Last verified:** 2026-06-10 | **Verified by:** analysis

Estrategia de estudio que reorganiza las 10 unidades oficiales alrededor de cada familia de modulacion, aplicando 4 capas progresivas de profundidad.

---

## Las 4 Capas

Para cada modulacion o familia, se estudia en este orden:

1. **Capa conceptual** — Que hace esta modulacion, para que sirve, como se clasifica (analogica vs digital, banda base vs paso-banda), como se relaciona con otras (AM→ASK, FM→FSK, PM→PSK).

2. **Capa matematica** — Formulas: expresion temporal $s(t)$, ancho de banda $BW$, espectro $S(f)$, eficiencia espectral $\eta_B$, diagramas de constelacion. Teoremas fundamentales que la sustentan (Nyquist, Shannon-Hartley, Carson).

3. **Capa de desempeño** — Comportamiento frente al ruido: SNR, BER, $E_b/N_0$, probabilidad de error. Eficiencia espectral vs energetica. Compromisos de diseño (BW vs potencia vs complejidad).

4. **Capa de implementacion y combinacion** — Como se construye el sistema (modulador, demodulador, receptor). Como se combina con multiplexacion (FDM/TDM/OFDM/CDMA). Ejemplos reales.

---

## Mapa Semanal por Modulacion

| Semana | Foco | Unidades oficiales | Contenido |
|--------|------|-------------------|-----------|
| **1** | Fundamentos + clasificacion | U1 | Modelo de Shannon, espectro EM, necesidad de modulacion, arbol taxonomico |
| **2** | Herramientas matematicas | U2 | Fourier, Parseval, Hilbert, convolucion, DEP, teorema de muestreo (Nyquist) |
| **3** | AM y familia | U3 (AM) | AM-DSB, DSB-SC, SSB, VSB. Capas 1→2→3→4 para cada variante. Receptor superheterodino. |
| **4** | FM / PM | U4 (FM/PM) | FM, PM, NBFM, WBFM, regla de Carson, pre/defnfasis. Capas 1→2→3→4. |
| **5** | Pulsos analogicos + PCM | U5 (pulsos) | PAM, PWM, PPM. Muestreo, cuantificacion, PCM, Delta, DPCM, ADPCM. Companding. TDM, T1/E1. |
| **6** | ASK / FSK / PSK | U6 (basico) | ASK, FSK, BPSK, QPSK. Constelaciones, BER, $E_b/N_0$. Deteccion coherente vs no coherente. |
| **7** | QAM + ruido analogico | U6 (QAM) + U7 (ruido AM/FM) | 16/64/256-QAM. SNR en AM, DSB, SSB. SNR en FM. Efecto umbral. |
| **8** | Ruido digital + Friis | U7 (ruido digital) | BER vs $E_b/N_0$, ruido termico, temperatura de ruido, factor de ruido, formula de Friis. |
| **9** | Intercomparacion | U8 | Eficiencia espectral vs energetica, tabla comparativa global, ganancia de procesamiento. |
| **10** | Teoria de la informacion | U9 | Entropia, Shannon-Hartley, codigos de fuente (Huffman), codigos de canal (Hamming, LDPC). |
| **11** | OFDM + espectro expandido | U10 | DSSS, FHSS, CDMA, OFDM, prefijo ciclico, aplicaciones (WiFi, 5G, GPS). |

---

## Ejemplo: Semana 3 — AM (Capas aplicadas)

### Capa 1 — Conceptual
- AM modula la amplitud de una portadora senoidal con $m(t)$
- Variantes: DSB-FC (convencional), DSB-SC (portadora suprimida), SSB (banda lateral unica), VSB (vestigial)
- Relacion con ASK: mismo concepto pero con valores discretos
- → [[../introduccion/modelo-shannon|Modelo de Shannon]]
- → [[../introduccion/necesidad-modulacion|Necesidad de Modulacion]]

### Capa 2 — Matematica
- $s_{AM}(t) = [A_c + m(t)]\cos(2\pi f_c t)$
- $s_{DSB-SC}(t) = m(t)\cos(2\pi f_c t)$
- Indice de modulacion: $\mu = |\min m(t)|/A_c$
- Ancho de banda: $BW = 2f_m$
- Eficiencia: $\eta = \mu^2/(2 + \mu^2)$
- → [[../modulacion-analogica/am-vs-dsb-sc|AM vs DSB-SC]]
- → [[../modulacion-analogica/modulacion-ssb|Modulacion SSB]]
- → [[../modulacion-analogica/indice-modulacion-am|Indice de Modulacion AM]]

### Capa 3 — Desempeño
- SNR en AM con deteccion coherente: $SNR_{out} = \frac{P_m}{N_0 B}$
- SNR en AM con deteccion de envolvente: degradacion por umbral
- Comparacion: DSB-SC duplica la eficiencia de AM, SSB cuadriplica
- → [[../ruido/snr-modulacion-lineal|SNR en Modulacion Lineal]]
- → [[../ruido/efecto-umbral|Efecto Umbral]]

### Capa 4 — Implementacion
- Modulador balanceado (DSB-SC): dos ramas en contrafase cancelan la portadora
- Receptor superheterodino: RF → IF → demodulacion
- AM comercial: 530-1700 kHz, $\mu \leq 1$, potencia hasta 50 kW
- → [[../modulacion-analogica/receptor-superheterodino|Receptor Superheterodino]]
- → [[../modulacion-analogica/modulador-fm|Moduladores y Detectores]] (incluye balanceado)

---

## Ver Tambien

- [[../conceptos-integradores/clasificacion-modulaciones|Clasificacion de Modulaciones]]
- [[../conceptos-integradores/aportes-shannon|Aportes de Shannon]]
- [[../conceptos-integradores/compromisos-diseno|Compromisos de Diseno]]
- [[../resumenes/overview-curso|Resumen General del Curso]]
- [[../planificacion/programa-oficial|Programa Oficial]]
- [[../planificacion/mazo-anki|Mazo Anki Completo]]
- [[../planificacion/progreso-actual|Progreso Actual]]
