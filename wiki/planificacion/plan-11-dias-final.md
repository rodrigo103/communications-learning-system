---
tags:
  - wiki/planificacion
curso: Sistemas de Comunicaciones
---

# Plan para el Final (30 de julio) — recalculado 26/07 (v4)

> **Last verified:** 2026-07-26 | **Verified by:** analysis + revision cruzada con 42 finales unicos resueltos (2019-2026, ver "Frecuencia de Temas en los Finales") + documento oficial de la catedra (modalidad vigente desde feb. 2022, ult. modificacion 30/07/2025) + recalculo de cronograma tras desvio real de fechas (v4, 26/07)

> ⚠️ **Recalculo de cronograma (26/07, version 4) + cambio de ritmo:** el Dia 2 no llego a cubrir SSB, VSB ni FM (solo AM) — se extiende a hoy 26/07. Como todavia es la madrugada del 26 (0 dias perdidos, el 26 sigue entero por delante), el resto de temas se recorre asi: **26/07** SSB+VSB+FM (y PCM si alcanza); **27/07** PCM (si quedo pendiente) + Modulacion Digital; **28/07** Ruido+BER + Teoria de la Informacion + Espectro Expandido, los tres juntos; **29/07** Repaso + Simulacro (se recupera, ya no hace falta correrlo al 30/07). Ademas, **desde ahora el ritmo cambia**: formula compacta + un ejemplo numerico rapido, sin re-derivar desde cero salvo pedido explicito — la profundidad tipo Dia 1 fue valiosa pero ya no hay tiempo para sostenerla.

> ⚠️ **Recalculo de cronograma (23/07, version 2):** el plan original preveia 1 dia (19 jul) para el Dia 1 (Unidad 2: Shannon, Fourier, Parseval, Hilbert, DEP). En la practica llevo 4 dias de calendario (19, 20, 22 y la madrugada del 23 — el 21 no hubo sesion), sobre todo por la profundidad con la que se exploro la Transformada de Hilbert. Fue tiempo bien invertido en entendimiento, pero el cronograma de 11 dias quedo obsoleto. Quedan **7 dias completos** (23 al 29 de julio — el 23 todavia esta entero por delante, el Dia 1 se termino de madrugada antes del amanecer). Con ese dia extra respecto al primer recalculo, se deshizo la fusion mas forzada (Teoria de la Informacion + Espectro Expandido) y **se reordeno el plan**: AM/FM (entre los temas mas testeados — ver "Frecuencia de Temas en los Finales") se adelanto al primer dia de contenido nuevo en vez de quedar en el medio, como gestion de riesgo por si el cronograma se atrasa de nuevo. Ver "Lo comprimido" para el detalle.

> ⚠️ **Recalculo de cronograma (25/07, version 3):** el Dia 2 (AM/FM), planeado para el 23/07 solo, termino ocupando **tres** dias de calendario (23, 24 y 25 jul — autoevaluacion + ejercicio de practica se terminaron recien hoy). Eso consume exactamente el dia extra que la v2 habia recuperado: quedan **4 dias completos** (26 al 29 de julio) para cubrir PCM, Modulacion Digital, Ruido+BER, Teoria de la Informacion y Espectro Expandido/OFDM — 5 bloques de contenido en 4 dias. Para que cierre, se recomprime asi: **Modulacion Digital se fusiona con Ruido+BER** en un solo dia intenso (justificado porque ya estaban pensados como dias adyacentes que reusan formulas) y **Teoria de la Informacion se re-fusiona con Espectro Expandido/OFDM** (la misma fusion que existia en la v1 del recalculo, antes de recuperar el dia extra que ahora se volvio a perder) — sin sinergia real de contenido entre esos dos, es pura necesidad de cronograma. PCM se mantiene solo (sigue siendo, con evidencia, el tema individual mas testeado — 71,4%). El dia de Repaso+Simulacro (29/07) no se toca. Ver tabla actualizada y "Lo comprimido" para el detalle completo.

Estrategia de preparacion para el examen final. Foco en modulaciones digitales, con cobertura reforzada en analogicas tras revisar el patron real de exigencia en finales anteriores.

> ✅ **Modalidad oficial confirmada por la catedra (documento compartido 20/07):**
> - Examen **escrito**, sin instancia oral. Empieza **19:00** en sede a confirmar.
> - **4 problemas**, uno por hoja. Cada 30 min (19:30, 20:00, 20:30, 21:00) hay que entregar un problema resuelto **a eleccion** — el orden lo elige el estudiante, pero el presupuesto total es 2 horas para los 4 (30 min promedio c/u). Se resuelve sobre la misma hoja del enunciado, con hojas adicionales si hace falta.
> - **Material permitido: solo en soporte papel** — libros, presentaciones, tabla de formulas, apuntes propios o de terceros. **No se admite carpeta digital / notebook / tablet.** Esto ya no es una pregunta abierta: el [[../planificacion/formulario-imprimible|Formulario Imprimible]] hay que llevarlo impreso si o si.
> - **Prohibido:** guias de problemas, y resoluciones de otros finales/parciales/recuperatorios. Los 42 finales en `exercises/finales/md/` son **solo para practicar** — no se pueden llevar al examen.
> - Se puede consultar al equipo docente durante el examen (probablemente por eso varios finales traen anexo un grafico de $Q(k)$ — no hace falta memorizar esas tablas).
> - Aprueba con sumatoria $\geq 6/10$ sin redondeo, y minimo 25% desarrollado por problema (un problema en blanco = examen desaprobado, sin importar el resto).

---

## Resumen

- **Fecha examen:** 30 de julio de 2026, 19:00 hs
- **Dias disponibles (real, recalculo v4 del 26/07):** 4 dias completos (26 jul → 29 jul) — sin perder ninguno respecto a la v3, pero recontenidos porque el Dia 2 no llego a SSB/VSB/FM
- **Formato:** escrito, 4 problemas, ~30 min c/u con entrega escalonada, material propio en papel permitido
- **Estrategia:** el cuello de botella real es la *velocidad bajo presion de tiempo fijo* (30 min por problema, no negociable). **Ritmo nuevo desde el 26/07**: formula compacta + ejemplo rapido, casi sin derivacion — la profundidad tipo Dia 1 costo demasiado tiempo para lo que queda. Intercomparacion (U8) recortada casi del todo (ver "Lo comprimido").

### Metodologia de practica cronometrada

Desde ya (26/07) en adelante, cada ejercicio de `exercises/finales/md/` se practica con reloj: **30 minutos, sin mirar la seccion `<details>` de respuesta hasta que se cumpla el tiempo o el ejercicio este terminado.** El objetivo no es solo llegar al resultado correcto, sino llegar en el tiempo real del examen. Si un tema toma sistematicamente mas de 30 min, es señal de que hace falta mas practica ahi, no de que el limite este mal.

---

## Frecuencia de Temas en los Finales (evidencia)

> **Recalculado 24/07** sobre el corpus completo: 48 archivos en `exercises/finales/md/`, de los cuales 6 son duplicados exactos del mismo llamado (enunciado en blanco + su resolucion, o dos resoluciones distintas del mismo examen) → **42 finales unicos** (2019-2026). El analisis original de este plan (77%/54%/69%/62%/31%, citado en varias notas de abajo) se habia hecho sobre los primeros 13 finales convertidos, antes de sumar los 35 restantes — los numeros de esta tabla son los que valen ahora.

| Tema | Aparece en | Frecuencia |
|---|---|---|
| Modulacion por Codificacion de Pulsos (PCM/Muestreo, U2/U5) | 30/42 | **71,4%** |
| Modulacion Lineal (AM/DSB/SSB, U3) | 26/42 | 61,9% |
| Modulacion Exponencial (FM/PM, U4) | 26/42 | 61,9% |
| Espectro Expandido / OFDM (U10) | 24/42 | 57,1% |
| Ruido (U7) | 22/42 | 52,4% |
| Teoria de la Informacion (U9) | 22/42 | 52,4% |
| Modulacion Digital (ASK/FSK/PSK/QAM, U6) | 17/42 | 40,5% |
| Analisis de Señales, como ejercicio propio (U2) | 1/42 | 2,4% |
| Intercomparacion de Sistemas (U8) | 0/42 | 0% |

**Que cambia respecto al plan original:** PCM pasa a ser, individualmente, el tema mas testeado — por encima de AM. AM y FM quedan practicamente empatados (61,9% cada uno, ya no 77%/54%). Teoria de la Informacion baja de 69% a 52,4% al sumar los finales nuevos, queda empatada con Ruido y **por debajo** de Espectro Expandido — el orden actual (Dia 6 = Teoria de la Informacion, Dia 7 = Espectro Expandido) ya no refleja la frecuencia real; se mantiene por ahora porque no cambia la urgencia practica (los dos temas siguen cubiertos, en algun orden, antes del simulacro), pero si se prioriza estrictamente por frecuencia convendria invertirlos. Intercomparacion sigue en 0% — el unico recorte de este plan con evidencia de "cero apariciones", no solo "poca frecuencia", se mantiene sin cambios.

---

## Plan Diario

### Completado

| Dia | Fecha(s) reales | Foco | Contenido clave |
|-----|-------|------|-----------------|
| **1** | 19, 20, 22, 23 jul (4 dias, no 1) | U1+U2 — Fundamentos | Modelo de Shannon, espectro EM, Fourier, Parseval (con Fubini), Hilbert (transformada, señal analitica, envolvente compleja, teorema pasabanda), DEP. Cobertura muy profunda — mas de lo que pedia el plan original, de ahi el desvio de cronograma. |

#### Lecturas — Dia 1 (fundamentos, ya completado)

- [[../introduccion/modelo-shannon|Modelo de Shannon]] — esquema fuente-transmisor-canal-receptor-destino, el marco que se repite para cada modulacion
- [[../introduccion/espectro-electromagnetico|Espectro Electromagnetico]] — bandas de frecuencia, para ubicar donde vive cada modulacion
- [[../conceptos-integradores/aportes-fourier|Aportes de Fourier]] — Transformada y Serie de Fourier, tabla de propiedades (usar esta, no `herramientas-matematicas/serie-fourier` ni `transformada-fourier`, que son paginas stub sin contenido real)
- [[../herramientas-matematicas/teorema-parseval|Teorema de Parseval]] — conservacion de energia tiempo-frecuencia, con la derivacion completa via Fubini
- [[../herramientas-matematicas/senales-energia-potencia|Señales de Energia vs Potencia]] — de donde sale $E=\int|x(t)|^2dt$, y la clasificacion energia/potencia
- [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]] — la nota mas trabajada de todas: transformada, señal analitica, envolvente compleja, teorema pasabanda, constelaciones y OFDM
- [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert|Carta 8: Transformada de Hilbert y Señales Analíticas]] — la fuente original en formato Anki, con los 3 ejemplos numericos (SSB, envolvente AM, frecuencia instantanea FM) que dieron pie a varias de las preguntas de hoy. Opcional si ya leiste la nota de arriba, que absorbio y corrigio su contenido
- [[../herramientas-matematicas/densidad-espectral-potencia|Densidad Espectral de Potencia]] — DEP y Wiener-Khinchin (prioridad baja, no se testea como categoria propia en los finales)
- [[../herramientas-matematicas/ancho-de-banda|Ancho de Banda]] — los 5 tipos de ancho de banda, tema del Dia 1 que faltaba y se agrego despues

### Recalculado v4 — 4 dias reales, ritmo rapido (26 al 29 de julio)

| Dia | Fecha | Foco | Horas | Contenido clave |
|-----|-------|------|-------|-----------------|
| **2** | 23-26 jul (en curso) | U3+U4 — Analogicas: AM listo, falta SSB+VSB+FM | ~15-16h + hoy | AM completo (potencia, PEP, envolvente, multitono, DSB-SC) ya cubierto. **Hoy 26/07, rapido**: SSB (conecta con Hilbert del Dia 1), VSB (breve), y FM completo (Carson $BW\approx2(\Delta f+f_m)$, indice $\beta$, NBFM/WBFM, moduladores indirectos) — formula y ejemplo, sin re-derivar. |
| **3** | 26-27 jul | U2+U5 — Muestreo + PCM | 5-6h | Nyquist ($f_s\geq2B$), cuantificacion, PCM, companding, SQNR$\approx6n+1{,}76$dB. **71,4% de frecuencia, el tema individual mas testeado** — arranca hoy si alcanza, si no pasa al 27. |
| **4** | 27 jul | U6 — Modulacion Digital | 5-6h | BW, constelaciones, $R_b=R_s\log_2M$, pares BER ($P_e^{BPSK}=Q(\sqrt{2E_b/N_0})$). Comparte dia con el resto de PCM si hizo falta correrlo. |
| **5+6+7** | 28 jul | U7+U9+U10 — Ruido+BER, Teoria de la Informacion y Espectro Expandido, los tres juntos | 9-10h | **Dia mas cargado del plan** — sin sinergia fuerte entre los tres, es necesidad de cronograma pura. Ruido: $N=kTB$, Friis, SNR. TI (52,4%): Entropia, Shannon-Hartley, limite -1.59dB. Espectro (57,1%): DSSS/FHSS/CDMA/OFDM, $G_p=R_c/R_b$, $N=2^L-1$ — el que mas formulas de sustitucion directa tiene, el mas facil de ir rapido. |
| **8** | 29 jul | Repaso general + Intercomparacion (breve) + **simulacro cronometrado real** | 6-7h | Repaso de formulas y del arbol de modulaciones (Intercomparacion, repaso rapido — ver "Lo comprimido"). **Simulacro en formato real**: final no visto antes (ej. `exercises/finales/md/F_Comu_2026-02-26_res.md`), reloj en 19:00, un problema cada 30 min hasta las 21:00, solo formulario impreso. |
| **30 jul** | — | **EXAMEN — 19:00hs** | — | — |

> Si el 27 o el 28 jul se atrasan, el primer candidato a recortar es Espectro Expandido dentro del dia 5+6+7 (57,1% de frecuencia, pero el que menos derivacion propia tiene — formulas directas de sustitucion), pasandolo a repaso el dia 29 en vez de bloque propio.

### Lecturas — Dia 2 (23-26 jul, AM/FM — AM listo, hoy SSB+VSB+FM)

**AM / Modulacion Lineal:**
- [[../derivaciones/modulacion-am|Derivacion Completa de AM]] — potencia, envolvente, indice de modulacion; es la base, empezar por aca
- [[../modulacion-analogica/indice-modulacion-am|Indice de Modulacion en AM]]
- [[../modulacion-analogica/am-vs-dsb-sc|AM-DSB-FC vs DSB-SC]] — comparacion explicita, aparece en el enunciado del dia
- [[../modulacion-analogica/modulacion-ssb|Modulacion SSB]] — conecta directo con la Transformada de Hilbert del Dia 1
- [[../modulacion-analogica/modulacion-vsb|Modulacion VSB]] — breve, menor peso pero parte de la misma familia

**FM / Modulacion Exponencial:**
- [[../derivaciones/modulacion-fm-carson|Derivacion de FM y Regla de Carson]] — la formula clave, $BW\approx2(\Delta f+f_m)$
- [[../modulacion-analogica/fm-banda-angosta|FM Banda Angosta (NBFM) vs Banda Ancha (WBFM)]]
- [[../modulacion-analogica/fm-vs-pm|FM vs PM]]
- [[../modulacion-analogica/modulador-armstrong|Modulador Armstrong]] y [[../modulacion-analogica/modulador-fm|Moduladores y Demoduladores FM]] — moduladores indirectos con multiplicadores de frecuencia, el patron que se repite en los finales (ej. `F_Comu_2024-02-22_res.md` y `F_Comu_2025-04-24_res.md`)

**Opcional / menor prioridad** (no aparecieron como ejercicio en ninguno de los 42 finales unicos — leer solo si sobra tiempo):
- [[../modulacion-analogica/deteccion-coherente|Deteccion Coherente]]
- [[../modulacion-analogica/preenfasis-deenfasis|Preenfasis/Deenfasis]]
- [[../modulacion-analogica/fm-estereo|FM Estereo]]
- [[../modulacion-analogica/funciones-bessel|Funciones de Bessel]]

### Lecturas — Dia 3 (26-27 jul, PCM/Muestreo)

**Nucleo:**
- [[../herramientas-matematicas/teorema-muestreo|Teorema de Muestreo]] — condicion de Nyquist $f_s\geq2B$, empezar por aca
- [[../modulacion-pulsos/muestreo-ideal-natural|Muestreo Ideal y Natural]]
- [[../modulacion-pulsos/pcm-cuantificacion|PCM: Muestreo, Cuantificacion y Codificacion]] — la nota real (usar esta, no `pcm.md` ni `cuantificacion.md`, que son paginas stub de redireccion)
- [[../modulacion-pulsos/companding|Companding]] — Ley A / Ley $\mu$, para el calculo de SQNR con compansion
- [[../conceptos-integradores/aportes-nyquist|Aportes de Nyquist]]

**Opcional / menor prioridad:**
- [[../modulacion-pulsos/multiplex-tdm|Multiplexacion TDM]] — aparece combinado con PAM en un par de finales (ej. `F_Comu_2022-02-24_X_res.md`), prioridad media-baja (usar esta nota, no `tdm.md`, que es stub)
- [[../modulacion-pulsos/modulacion-delta|Modulacion Delta]] — no aparecio como ejercicio en ninguno de los 42 finales

### Lecturas — Dia 4 (27 jul, Modulacion Digital)

**Modulacion Digital:**
- [[../modulacion-digital/ask-fsk-psk|ASK, FSK, PSK]] — formulas de BW y constelaciones basicas, empezar por aca
- [[../modulacion-digital/modulacion-qam|Modulacion QAM]]
- [[../modulacion-digital/constelaciones|Constelaciones]] — diagramas I/Q, aparece en varios finales
- [[../modulacion-digital/probabilidad-error|Probabilidad de Error (BER)]] — pares $Q(\cdot)$ por tipo de modulacion
- [[../modulacion-digital/codificacion-linea|Codificacion de Linea]] — NRZ/Manchester, aparece con frecuencia notable en los finales
- [[../modulacion-digital/eficiencia-espectral|Eficiencia Espectral]]

**Opcional / menor prioridad:**
- [[../modulacion-digital/comparacion-digital-analogica|Comparacion Digital vs Analogica]]

### Lecturas — Dia 5+6+7 (28 jul, Ruido+BER + Teoria de la Informacion + Espectro Expandido, los tres juntos)

**Ruido:**
- [[../ruido/fuentes-ruido|Fuentes de Ruido]]
- [[../ruido/ruido-termico|Ruido Termico]] — $N=kTB$
- [[../ruido/temperatura-ruido|Temperatura de Ruido]]
- [[../ruido/factor-ruido-temperatura|Factor de Ruido y Temperatura Equivalente]]
- [[../ruido/formula-friis|Formula de Friis para Sistemas en Cascada]] — la version corta, para fluidez de formula; si hace falta la derivacion completa ver [[../derivaciones/ecuacion-friis|Derivacion de Friis]] (opcional, mas largo)
- [[../ruido/relacion-snr|Relacion Señal-Ruido (SNR)]]
- [[../ruido/aclaracion-densidad-espectral-ruido|Aclaracion sobre Densidad Espectral de Ruido]]

**Opcional / menor prioridad (Ruido):**
- [[../ruido/ruido-banda-angosta|Ruido de Banda Angosta]] y [[../ruido/ruido-blanco-banda-angosta|Ruido Blanco de Banda Angosta]] — prioridad media, no critico
- [[../ruido/efecto-umbral|Efecto Umbral]] — no aparecio como ejercicio en ninguno de los 42 finales (relevante sobre todo para FM, ya cubierto en Dia 2)

**Teoria de la Informacion:**
- [[../teoria-informacion/entropia-fuente|Entropia de Fuente]] — $H=-\sum p_i\log_2p_i$, empezar por aca (usar esta, no `entropia.md`, que es stub)
- [[../teoria-informacion/capacidad-canal-shannon|Capacidad de Canal y Teorema de Shannon-Hartley]]
- [[../teoria-informacion/teorema-shannon-hartley|Teorema de Shannon-Hartley]] — nota conceptual corta, para fluidez de formula; si hace falta la derivacion completa ver [[../derivaciones/teorema-shannon-hartley|Derivacion de Shannon-Hartley]] (opcional, mas largo)
- [[../conceptos-integradores/aportes-shannon|Aportes de Shannon]]

**Opcional / menor prioridad (Huffman/Hamming no aparecieron como ejercicio en ninguno de los 42 finales):**
- [[../teoria-informacion/codigo-compacto|Codigo Compacto (Huffman)]]
- [[../teoria-informacion/codigos-deteccion-error|Codigos de Deteccion y Correccion de Errores (Hamming)]]
- [[../teoria-informacion/redundancia-compresion|Redundancia y Compresion]]
- [[../teoria-informacion/sistema-ideal-comunicaciones|Sistema Ideal de Comunicaciones]]

**Espectro Expandido / OFDM:**
- [[../espectro-expandido/dsss|DSSS]]
- [[../espectro-expandido/fhss|FHSS]]
- [[../espectro-expandido/cdma|CDMA]]
- [[../espectro-expandido/ofdm|OFDM]]

**Opcional / menor prioridad:**
- [[../espectro-expandido/prefijo-ciclico|Prefijo Ciclico]] — aparece en un solo final
- [[../espectro-expandido/correlacion-senales|Correlacion de Señales]] — no aparecio como ejercicio propio
- [[../espectro-expandido/aplicaciones-spread-spectrum|Aplicaciones de Spread Spectrum]] — contexto, no formulas

### Lecturas — Dia 8 (29 jul, Repaso + Intercomparacion + Simulacro)

- [[../ruido/intercomparacion-sistemas|Intercomparacion de Sistemas]] — repaso conceptual rapido (20-30 min), no bloque dedicado (ver "Lo comprimido")
- [[../conceptos-integradores/comparacion-global-modulaciones|Comparacion Global de Modulaciones]]
- [[../conceptos-integradores/clasificacion-modulaciones|Clasificacion de Modulaciones]] — mapa central para repasar el arbol completo
- [[../conceptos-integradores/compromisos-diseno|Compromisos de Diseno]] y [[../conceptos-integradores/trade-off-bw-potencia|Trade-off BW vs Potencia]]
- [[../conceptos-integradores/eb-n0-vs-snr|$E_b/N_0$ vs SNR]] — conexion entre las metricas de Digital y de Ruido, util para el repaso integrador
- [[../conceptos-integradores/seleccion-modulacion|Seleccion de Modulacion]]
- [[../planificacion/formulario-imprimible|Formulario Imprimible]] — repaso final antes del simulacro; confirmar que ya esta impreso

---

## Lo comprimido (y por que no es grave)

> ⚠️ **Recalculado 23/07 (v2):** con el dia extra recuperado (7 dias reales en vez de 6), se deshizo la fusion mas forzada (Teoria de la Informacion + Espectro Expandido, que no tenian sinergia real entre si). Queda un solo tema combinado — Ruido + BER — que ademas tiene justificacion propia (ver tabla). AM/FM se mantiene sin comprimir y encima se adelanto en el orden (entre los mas evaluados — ver "Frecuencia de Temas en los Finales"), porque la mayoria de los finales incluyen la regla "un punto sin desarrollo alguno implica que el examen esta desaprobado" — no se puede dejar un item en blanco.
>
> ⚠️ **Recalculado 25/07 (v3):** el dia extra que la v2 habia recuperado se volvio a perder (AM/FM se extendio 23-25/07 en vez de terminar el 23/07). Se vuelve a comprimir: **Teoria de la Informacion se re-fusiona con Espectro Expandido/OFDM** y **Modulacion Digital se fusiona con Ruido + BER**. PCM y AM/FM no se tocan.
>
> ⚠️ **Recalculado 26/07 (v4) + cambio de ritmo:** el Dia 2 tampoco llego a SSB/VSB/FM (solo AM). Se reagrupa una vez mas: **Ruido+BER, Teoria de la Informacion y Espectro Expandido quedan los tres juntos** en un solo dia (28/07), y **Modulacion Digital pasa a compartir dia con el resto de PCM** en vez de con Ruido/BER. Ademas, de aca en mas el estudio va a ritmo rapido — formula y ejemplo, sin re-derivar — para no repetir el atraso.

| Tema | Que se hizo | Justificacion |
|------|---------------|---------------|
| **Intercomparacion (U8)** | Recortada casi del todo — pasa a ser repaso conceptual de 20-30 min el ultimo dia, no un bloque dedicado | Revisando los titulos de ejercicio de los 42 finales unicos, "Intercomparacion" **nunca aparece como categoria propia** (0/42, ver "Frecuencia de Temas en los Finales"). Es el unico recorte de este plan con evidencia de "cero apariciones", no solo "poca frecuencia". |
| **Ruido+BER + Teoria de la Informacion + Espectro Expandido** | Los tres juntos en un solo dia (28/07, 9-10h) — *(v4, 26/07)* | Sin sinergia fuerte entre los tres — necesidad de cronograma, no de contenido. Es el nivel de compresion mas alto del plan hasta ahora, consecuencia de que el Dia 2 volvio a atrasarse. |
| **Modulacion Digital + resto de PCM** | Comparten dia (27/07) si PCM no cerro el 26/07 | Digital y PCM tienen orden logico real (PCM digitaliza, Digital transmite esos bits) — mejor pareja que forzar a Digital con Ruido/BER un dia mas cargado. Digital aparece como ejercicio dedicado en 40,5% de los finales. |
| SNR en analogicas | Casi nada | Lo preguntan, pero es derivable de las mismas formulas de ruido. |
| Preenfasis, FM estereo | Nada explicito | Temas de menor peso. Preenfasis/deenfasis no aparece como ejercicio en ninguno de los 42 finales; "estereo" aparece solo como dato incidental de contexto en 2 ejercicios de FM (no como categoria propia). |

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
- → `exercises/finales/md/` — 48 archivos (42 finales unicos, 2019-2026) convertidos a Markdown, enunciado + resolucion colapsable. Base empirica de este plan revisado — ver "Frecuencia de Temas en los Finales" para el desglose completo.
- → [[../herramientas-matematicas/ancho-de-banda|Ancho de Banda]] — los 5 tipos de ancho de banda (absoluto, -3dB, nulo a nulo, fraccional, equivalente de ruido) en un solo lugar

---

## Ver Tambien

- [[../planificacion/programa-oficial|Programa Oficial]]
- [[../planificacion/progreso-actual|Progreso Actual]]
- [[../planificacion/mazo-anki|Mazo Anki Completo]]
- [[../resumenes/overview-curso|Resumen General del Curso]]
