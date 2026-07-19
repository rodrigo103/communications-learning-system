---
tags:
  - wiki/planificacion
curso: Sistemas de Comunicaciones
---

# Plan Intensivo: 11 Dias para el Final (30 de julio)

> **Last verified:** 2026-07-19 | **Verified by:** analysis

Estrategia de preparacion para el examen final oral teorico-integrador con resolucion de problema. Foco en modulaciones digitales, minimo viable en analogicas.

---

## Resumen

- **Fecha examen:** 30 de julio de 2026
- **Dias disponibles:** 11 (19 jul → 29 jul)
- **Formato:** oral teorico-integrador + resolucion de problema
- **Estrategia:** profundidad en digitales, superficial en analogicas (AM/FM), nada omitido

---

## Plan Diario

| Dia | Fecha | Foco | Horas | Contenido clave |
|-----|-------|------|-------|-----------------|
| **1** | 19 jul | U1+U2 — Fundamentos | 5-6h | Modelo de Shannon, espectro EM, Fourier, Parseval, Hilbert, DEP, ancho de banda |
| **2** | 20 jul | U2+U5 — Muestreo + PCM | 5-6h | Teorema de Nyquist ($f_s \geq 2B$), muestreo, cuantificacion, PCM, companding, SQNR = $6n + 1.76$ dB |
| **3** | 21 jul | U6 — ASK, FSK, BPSK, QPSK | 5-6h | Formulas, constelaciones, ancho de banda, BER, $E_b/N_0$, Q(x) |
| **4** | 22 jul | U6 — QAM + M-PSK | 4-5h | 16/64/256-QAM, constelaciones, bits/simbolo, $R_b = R_s \log_2 M$ |
| **5** | 23 jul | U7 — Ruido digital | 5-6h | $N = kTB$, $N_0$, temperatura de ruido, factor de ruido, Friis cascada |
| **6** | 24 jul | U7 — BER practica | 4-5h | BER vs $E_b/N_0$ para cada modulacion, curvas, resolucion de problemas |
| **7** | 25 jul | U3+U4 — Analogicas (minimo) | 3-4h | Solo definiciones y formulas clave: AM ($s(t)$, $\mu$, BW), FM (Carson: $2(\Delta f+f_m)$), SSB/VSB conceptual |
| **8** | 26 jul | U9 — Teoria de la Informacion | 5-6h | Entropia $H = -\sum p_i \log_2 p_i$, Shannon-Hartley $C = B\log_2(1+SNR)$, limite -1.59 dB, Huffman, Hamming |
| **9** | 27 jul | U10 — OFDM + Spread Spectrum | 4-5h | DSSS, FHSS, CDMA conceptual, OFDM + prefijo ciclico, IFFT/FFT, aplicaciones (WiFi, 5G, GPS) |
| **10** | 28 jul | U8 — Intercomparacion + problemas | 5-6h | Eficiencia espectral vs energetica, tabla comparativa, ejercicios integradores (SNR, Friis, BER, capacidad) |
| **11** | 29 jul | Repaso + simulacion oral | 4-5h | Repaso de todas las formulas, practica de explicacion oral, repaso del arbol de modulaciones |

---

## Lo comprimido (y por que no es grave)

| Tema | Dias dedicados | Justificacion |
|------|---------------|---------------|
| AM/DSB/SSB/VSB | Medio dia (dia 7) | AM→ASK ya lo entendiste. Lo demas son variantes de eficiencia. |
| FM/PM analogicas | Medio dia (dia 7) | Regla de Carson y el concepto de $\beta$ es lo que mas preguntan. |
| SNR en analogicas | Casi nada | Lo preguntan, pero es derivable de las mismas formulas de ruido. |
| Preenfasis, FM estereo | Nada explicito | Temas de menor peso. Los lees el dia 11 si sobra tiempo. |

---

## Formulas que hay que escribir de memoria

| Formula | Que es | Unidad |
|---------|--------|--------|
| $C = B\log_2(1 + S/N)$ | Capacidad de Shannon | U9 |
| $H = -\sum p_i \log_2 p_i$ | Entropia | U9 |
| $f_s \geq 2B$ | Nyquist | U2/U5 |
| $SQNR \approx 6n + 1.76$ dB | Calidad PCM | U5 |
| $F_{total} = F_1 + \frac{F_2-1}{G_1} + \cdots$ | Friis cascada | U7 |
| $N = kTB$ | Ruido termico | U7 |
| $R_b = R_s \cdot \log_2 M$ | Bits vs simbolos | U6 |
| $BW_{FM} \approx 2(\Delta f + f_m)$ | Carson | U4 |
| $P_e^{BPSK} = Q(\sqrt{2E_b/N_0})$ | BER BPSK | U6 |
| $\frac{E_b}{N_0} > \ln 2 = -1.59$ dB | Limite absoluto | U9 |

---

## Recursos clave

- → [[../conceptos-integradores/clasificacion-modulaciones|Clasificacion de Modulaciones]] — mapa central de todas las modulaciones
- → [[../conceptos-integradores/compromisos-diseno|Compromisos de Diseno]] — BW vs potencia vs complejidad
- → [[../conceptos-integradores/aportes-shannon|Aportes de Shannon]] — todo U9 resumido
- → [[../conceptos-integradores/aportes-nyquist|Aportes de Nyquist]] — muestreo, ISI, ruido termico
- → [[../modulacion-digital/constelaciones|Constelaciones]] — diagramas I/Q de todas las modulaciones
- → [[../modulacion-digital/probabilidad-error|Probabilidad de Error (BER)]] — curvas BER vs Eb/N0
- → [[../ruido/formula-friis|Formula de Friis]] — cascada de ruido
- → [[../teoria-informacion/teorema-shannon-hartley|Teorema de Shannon-Hartley]] — capacidad de canal
- → [[../espectro-expandido/ofdm|OFDM]] y [[../espectro-expandido/cdma|CDMA]]
- → [[../planificacion/plan-estudio-por-modulaciones|Plan por Modulaciones]] — la ruta acelerada original
- → [[../glosario|Glosario]] — siglas y notacion rapida
- → [[../../Mazo_Anki_Sistemas_Comunicaciones|Mazo Anki]] — 60 cartas para repasar en huecos

---

## Ver Tambien

- [[../planificacion/programa-oficial|Programa Oficial]]
- [[../planificacion/progreso-actual|Progreso Actual]]
- [[../planificacion/mazo-anki|Mazo Anki Completo]]
- [[../resumenes/overview-curso|Resumen General del Curso]]
