---
tags:
  - wiki/planificacion
curso: Sistemas de Comunicaciones
---

# Plan para el Final (30 de julio) — recalculado 23/07

> **Last verified:** 2026-07-23 | **Verified by:** analysis + revision cruzada con 13 finales resueltos (2022-2026) + documento oficial de la catedra (modalidad vigente desde feb. 2022, ult. modificacion 30/07/2025) + recalculo de cronograma tras desvio real de fechas

> ⚠️ **Recalculo de cronograma (23/07):** el plan original preveia 1 dia (19 jul) para el Dia 1 (Unidad 2: Shannon, Fourier, Parseval, Hilbert, DEP). En la practica llevo 4 dias de calendario (19, 20, 22 y 23 jul — el 21 no hubo sesion), sobre todo por la profundidad con la que se exploro la Transformada de Hilbert. Fue tiempo bien invertido en entendimiento, pero el cronograma de 11 dias quedo obsoleto: quedan **6 dias de calendario** (24 al 29 de julio), no 10. El plan diario de abajo esta recalculado sobre esa base real, no sobre el original. Ver "Lo comprimido" para el detalle de que se fusiono y por que.

Estrategia de preparacion para el examen final. Foco en modulaciones digitales, con cobertura reforzada en analogicas tras revisar el patron real de exigencia en finales anteriores.

> ✅ **Modalidad oficial confirmada por la catedra (documento compartido 20/07):**
> - Examen **escrito**, sin instancia oral. Empieza **19:00** en sede a confirmar.
> - **4 problemas**, uno por hoja. Cada 30 min (19:30, 20:00, 20:30, 21:00) hay que entregar un problema resuelto **a eleccion** — el orden lo elige el estudiante, pero el presupuesto total es 2 horas para los 4 (30 min promedio c/u). Se resuelve sobre la misma hoja del enunciado, con hojas adicionales si hace falta.
> - **Material permitido: solo en soporte papel** — libros, presentaciones, tabla de formulas, apuntes propios o de terceros. **No se admite carpeta digital / notebook / tablet.** Esto ya no es una pregunta abierta: el [[../planificacion/formulario-imprimible|Formulario Imprimible]] hay que llevarlo impreso si o si.
> - **Prohibido:** guias de problemas, y resoluciones de otros finales/parciales/recuperatorios. Los 13 finales en `exercises/finales/md/` son **solo para practicar** — no se pueden llevar al examen.
> - Se puede consultar al equipo docente durante el examen (probablemente por eso varios finales traen anexo un grafico de $Q(k)$ — no hace falta memorizar esas tablas).
> - Aprueba con sumatoria $\geq 6/10$ sin redondeo, y minimo 25% desarrollado por problema (un problema en blanco = examen desaprobado, sin importar el resto).

---

## Resumen

- **Fecha examen:** 30 de julio de 2026, 19:00 hs
- **Dias disponibles (real, desde el recalculo del 23/07):** 6 (24 jul → 29 jul) — el Dia 1 (19-23 jul) ya esta completo
- **Formato:** escrito, 4 problemas, ~30 min c/u con entrega escalonada, material propio en papel permitido
- **Estrategia:** el cuello de botella real es la *velocidad bajo presion de tiempo fijo* (30 min por problema, no negociable), no la memorizacion pura ni la busqueda de datos — el formulario impreso resuelve la busqueda, pero no resuelve la velocidad. Con solo 6 dias reales, las sesiones tienen que ser mas rapidas y orientadas a formula+practica — menos derivacion profunda tipo Hilbert (valiosa pero cara en tiempo), mas resolucion cronometrada. Profundidad en digitales, cobertura reforzada en analogicas (AM/FM) segun el patron real de los finales, Intercomparacion (U8) recortada casi del todo (ver "Lo comprimido").

### Metodologia de practica cronometrada

Desde el dia 25/07 (Modulacion Digital) en adelante, cada ejercicio de `exercises/finales/md/` se practica con reloj: **30 minutos, sin mirar la seccion `<details>` de respuesta hasta que se cumpla el tiempo o el ejercicio este terminado.** El objetivo no es solo llegar al resultado correcto, sino llegar en el tiempo real del examen. Si un tema toma sistematicamente mas de 30 min, es señal de que hace falta mas practica ahi, no de que el limite este mal.

---

## Plan Diario

### Completado

| Dia | Fecha(s) reales | Foco | Contenido clave |
|-----|-------|------|-----------------|
| **1** | 19, 20, 22, 23 jul (4 dias, no 1) | U1+U2 — Fundamentos | Modelo de Shannon, espectro EM, Fourier, Parseval (con Fubini), Hilbert (transformada, señal analitica, envolvente compleja, teorema pasabanda), DEP. Cobertura muy profunda — mas de lo que pedia el plan original, de ahi el desvio de cronograma. |

### Recalculado — 6 dias reales restantes (24 al 29 de julio)

| Dia | Fecha | Foco | Horas | Contenido clave |
|-----|-------|------|-------|-----------------|
| **2** | 24 jul | U2+U5 — Muestreo + PCM | 5-6h | Teorema de Nyquist ($f_s \geq 2B$), muestreo, cuantificacion, PCM, companding, SQNR = $6n + 1.76$ dB. Sin cambios respecto al plan original — 69% de frecuencia en los finales, prioridad alta. |
| **3** | 25 jul | U6 — Modulacion Digital esencial (ASK/FSK/PSK/QAM) | 5-6h | Comprime lo que eran 1,5 dias en 1: formulas de BW, constelaciones, $R_b = R_s \log_2 M$, pares BER ($P_e^{BPSK}=Q(\sqrt{2E_b/N_0})$, etc.). Foco en fluidez de formula, no en derivacion — es la base directa del dia siguiente. **Arranca la practica cronometrada de 30 min por ejercicio.** |
| **4** | 26 jul | U7 — Ruido + BER integrado | 6-7h | ⚠️ Fusiona 2 dias del plan original en 1 (el mas apretado). $N=kTB$, $N_0$, temperatura de ruido, Friis cascada, y BER vs $E_b/N_0$ practicado junto, aprovechando que Digital quedo fresco del dia anterior. |
| **5** | 27 jul | U3+U4 — Analogicas (AM/FM), en profundidad | 5-6h | **Sin cambios — la mas testeada, no se toca.** AM/DSB en 10/13 finales (77%), FM/PM en 7/13 (54%). Potencia normalizada en dBW, PEP, envolvente a escala temporal, AM multitono ($P = P_c + \sum P_{SSB,i}$), DSB-SC vs AM convencional, Carson y moduladores indirectos. Ver ejercicios "Modulacion lineal" y "Modulacion exponencial" en `exercises/finales/md/`. |
| **6** | 28 jul | U9 — Teoria de la Informacion + U10 — Espectro Expandido/OFDM | 6-7h | ⚠️ Fusiona 2 dias del plan original en 1 — el otro punto apretado, ninguno de los dos temas se puede recortar (69% y 62% de frecuencia respectivamente). TI: entropia $H=-\sum p_i\log_2p_i$, Shannon-Hartley $C=B\log_2(1+SNR)$, limite -1.59dB. Espectro Expandido/OFDM: $G_p=R_c/R_b$, $N=2^L-1$, IFFT/FFT, prefijo ciclico. |
| **7** | 29 jul | Repaso general + Intercomparacion (breve) + **simulacro cronometrado real** | 6-7h | Repaso de todas las formulas y del arbol de modulaciones (Intercomparacion entra aca como repaso conceptual rapido, no como bloque dedicado — ver "Lo comprimido"). Cierra con **simulacro en el formato exacto del examen**: final completo no visto antes (ej. `exercises/finales/md/F_Comu_2026-02-26_res.md`), reloj en 19:00, entregar un problema cada 30 min hasta las 21:00, orden a eleccion, solo formulario impreso como material. |
| **30 jul** | — | **EXAMEN — 19:00hs** | — | — |

---

## Lo comprimido (y por que no es grave)

> ⚠️ **Recalculado 23/07:** con el desvio de cronograma (6 dias reales en vez de 10), hubo que comprimir mas de lo que preveia la version anterior de este plan. AM/FM se mantiene sin tocar (77%/54% de frecuencia, la mas evaluada) porque 12/13 finales incluyen la regla "un punto sin desarrollo alguno implica que el examen esta desaprobado" — no se puede dejar un item en blanco. Los recortes nuevos son otros, y estan basados en evidencia de los 13 finales, no en intuicion.

| Tema | Que se hizo | Justificacion |
|------|---------------|---------------|
| **Intercomparacion (U8)** | Recortada casi del todo — pasa a ser repaso conceptual de 20-30 min el ultimo dia, no un bloque dedicado | Revisando los titulos de ejercicio de los 13 finales, "Intercomparacion" **nunca aparece como categoria propia** — las que rotan son PCM (8), Ruido (5), Modulacion digital (4), Espectro Expandido/OFDM (6). Es el unico recorte de este plan con evidencia de "cero apariciones", no solo "poca frecuencia". |
| Modulacion Digital (ASK/FSK/PSK/QAM) | 1,5 dias → 1 dia | Aparece como ejercicio dedicado en solo 31% de los finales, y sus formulas se vuelven a usar el dia de Ruido/BER inmediatamente despues — no se pierde por no tener un dia extra de repaso separado. |
| Ruido + BER | 2 dias → 1 dia (6-7h) | ⚠️ Compresion real, no eliminacion — ambos temas se mantienen completos, solo con menos tiempo de practica adicional. Es el punto mas fragil del plan nuevo. |
| Teoria de la Informacion + Espectro Expandido/OFDM | 2 dias → 1 dia (6-7h) | ⚠️ Igual que el anterior — ambos temas son de alta frecuencia (69%/62%) y no se pueden recortar en contenido, solo en tiempo de practica. El otro punto fragil del plan. |
| SNR en analogicas | Casi nada | Lo preguntan, pero es derivable de las mismas formulas de ruido. |
| Preenfasis, FM estereo | Nada explicito | Temas de menor peso. No aparecieron como ejercicio en ninguno de los 13 finales revisados. |

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
