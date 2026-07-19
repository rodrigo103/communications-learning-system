---
tags:
  - wiki/planificacion
curso: Sistemas de Comunicaciones
---

# Plan Intensivo: 11 Dias para el Final (30 de julio)

> **Last verified:** 2026-07-19 | **Verified by:** analysis + revision cruzada con 13 finales resueltos (2022-2026)

Estrategia de preparacion para el examen final. Foco en modulaciones digitales, con cobertura reforzada en analogicas tras revisar el patron real de exigencia en finales anteriores.

> ✅ **Confirmado (19/07):** el examen es **escrito y con carpeta abierta** (se puede consultar material durante el examen), consistente con los 13 finales revisados en `exercises/finales/md/` (examenes escritos, cronometrados, con hoja de calificacion por item).
>
> ⚠️ **Accion pendiente — material impreso:** la carpeta de apuntes de Rodrigo es digital (este repo). Con carpeta abierta, la restriccion tipica no es "saber de memoria" sino "poder llegar al dato rapido durante el examen". Dos frentes:
> 1. Preguntar a la catedra si se puede usar/imprimir la carpeta digital (notebook, tablet, o impresion completa) el dia del examen.
> 2. Como respaldo (o si la respuesta es que solo se admite papel impreso), llevar un **formulario impreso de 1-2 paginas** con las formulas clave — ver [[../planificacion/formulario-imprimible|Formulario Imprimible]].

---

## Resumen

- **Fecha examen:** 30 de julio de 2026
- **Dias disponibles:** 11 (19 jul → 29 jul)
- **Formato:** escrito, con carpeta abierta (consulta de material permitida)
- **Estrategia:** con carpeta abierta el cuello de botella es la *velocidad para resolver*, no la memorizacion pura — igual conviene tener las formulas mas usadas de memoria para no perder tiempo buscando. Profundidad en digitales, cobertura reforzada en analogicas (AM/FM) segun el patron real de los finales, nada omitido. Preparar un formulario impreso compacto como respaldo por si la carpeta digital no se puede usar en el examen.

---

## Plan Diario

| Dia | Fecha | Foco | Horas | Contenido clave |
|-----|-------|------|-------|-----------------|
| **1** | 19 jul | U1+U2 — Fundamentos | 5-6h | Modelo de Shannon, espectro EM, Fourier, Parseval, Hilbert, DEP, ancho de banda |
| **2** | 20 jul | U2+U5 — Muestreo + PCM | 5-6h | Teorema de Nyquist ($f_s \geq 2B$), muestreo, cuantificacion, PCM, companding, SQNR = $6n + 1.76$ dB |
| **3** | 21 jul | U6 — ASK, FSK, BPSK, QPSK | 5-6h | Formulas, constelaciones, ancho de banda, BER, $E_b/N_0$, Q(x) |
| **4** | 22 jul | U6 — QAM + M-PSK (repaso) | 2-3h | 16/64/256-QAM, constelaciones, bits/simbolo, $R_b = R_s \log_2 M$. Repaso rapido: se reusa integramente en los dias 5-6 (Ruido/BER), no hace falta profundizar mas aca. |
| **5** | 23 jul | U7 — Ruido digital | 5-6h | $N = kTB$, $N_0$, temperatura de ruido, factor de ruido, Friis cascada |
| **6** | 24 jul | U7 — BER practica | 4-5h | BER vs $E_b/N_0$ para cada modulacion, curvas, resolucion de problemas |
| **7** | 25 jul | U3+U4 — Analogicas (AM/FM), en profundidad | 5-6h | **Revision de finales:** AM/DSB aparece en 10/13 finales historicos (77%) y FM/PM en 7/13 (54%) — es el tema mas consistentemente evaluado, mas que PCM o Ruido. Practicar los patrones que se repiten: potencia normalizada en dBW, PEP, dibujo de envolvente a escala temporal, AM multitono ($P = P_c + \sum P_{SSB,i}$), DSB-SC vs AM convencional, regla de Carson y moduladores indirectos con multiplicadores/mezcladores de frecuencia. Ver ejercicios "Modulacion lineal" y "Modulacion exponencial" en `exercises/finales/md/`. |
| **8** | 26 jul | U9 — Teoria de la Informacion | 5-6h | Entropia $H = -\sum p_i \log_2 p_i$, Shannon-Hartley $C = B\log_2(1+SNR)$, limite -1.59 dB, Huffman, Hamming |
| **9** | 27 jul | U10 — OFDM + Spread Spectrum | 4-5h | DSSS, FHSS, CDMA conceptual, OFDM + prefijo ciclico, IFFT/FFT, aplicaciones (WiFi, 5G, GPS). Drillear ganancia de procesamiento $G_p = R_c/R_b$ y longitud de LFSR ($N = 2^L - 1$) — patron que se repite en 5/13 finales (ejercicios "Espectro expandido"). |
| **10** | 28 jul | U8 — Intercomparacion + problemas | 5-6h | Eficiencia espectral vs energetica, tabla comparativa, ejercicios integradores (SNR, Friis, BER, capacidad) |
| **11** | 29 jul | Repaso + simulacro cronometrado | 4-5h | Repaso de todas las formulas, repaso del arbol de modulaciones, y **simulacro escrito cronometrado** con un final real completo (recomendado: `exercises/finales/md/F_Comu_2026-02-26_res.md`, el mas reciente) respetando la regla de "minimo 25% desarrollado por item". Si se confirma que la instancia es oral, sumar practica de explicacion oral sobre ese mismo simulacro. |

---

## Lo comprimido (y por que no es grave)

> ⚠️ **Revisado:** la version original de este plan comprimia AM/FM a medio dia. Al cruzar el plan contra 13 finales resueltos, se vio que AM/DSB aparece en 10/13 examenes (77%) y FM/PM en 7/13 (54%) — el tema individual mas evaluado, y presente en el 100% de los finales revisados (siempre aparece al menos uno de los dos). Ademas, 12/13 finales incluyen la regla "un punto sin desarrollo alguno implica que el examen esta desaprobado", por lo que no se puede dejar un item en blanco. Por eso AM/FM ya **no** esta en la lista de comprimidos (ver dia 7) y en cambio se recorto QAM/M-PSK (dia 4), que aparece como ejercicio propio en solo 4/13 finales (31%) y cuyo contenido se reusa en los dias de Ruido/BER.

| Tema | Dias dedicados | Justificacion |
|------|---------------|---------------|
| QAM/M-PSK como ejercicio propio | Medio dia (dia 4) | Aparece como ejercicio dedicado en solo 31% de los finales historicos, y sus formulas se repasan de nuevo en los dias 5-6 (Ruido/BER), que sí son casi siempre parte del examen. |
| SNR en analogicas | Casi nada | Lo preguntan, pero es derivable de las mismas formulas de ruido. |
| Preenfasis, FM estereo | Nada explicito | Temas de menor peso. No aparecieron como ejercicio en ninguno de los 13 finales revisados. Los lees el dia 11 si sobra tiempo. |

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
| $P_{AM} = \frac{A_c^2}{2Z} + \frac{m^2 A_c^2}{4Z}$ (y su forma multitono $P = P_c + \sum P_{SSB,i}$) | Potencia normalizada AM | U3 |
| $G_p = R_c / R_b$ | Ganancia de procesamiento (spread spectrum) | U10 |
| $N = 2^L - 1$ | Longitud de secuencia de un LFSR de $L$ etapas | U10 |

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
- → `exercises/finales/md/` — 13 finales resueltos (2022-2026) convertidos a Markdown, enunciado + resolucion colapsable. Base empirica de este plan revisado.

---

## Ver Tambien

- [[../planificacion/programa-oficial|Programa Oficial]]
- [[../planificacion/progreso-actual|Progreso Actual]]
- [[../planificacion/mazo-anki|Mazo Anki Completo]]
- [[../resumenes/overview-curso|Resumen General del Curso]]
