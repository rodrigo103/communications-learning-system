---
tags:
  - wiki/meta
---

# Wiki - Sistemas de Comunicaciones (UTN)

> **Last verified:** 2025-11-16 | **Verified by:** [source]

Base de conocimiento interconectada para el curso de Sistemas de Comunicaciones. Cada pagina linkea a sus conceptos relacionados, derivaciones matematicas y problemas de aplicacion.

---

## Introduccion y Fundamentos

- [[introduccion/modelo-shannon]] — Modelo de Shannon, componentes de un sistema de comunicaciones
- [[introduccion/necesidad-modulacion]] — Por que es necesaria la modulacion
- [[introduccion/espectro-electromagnetico]] — Espectro EM y uso racional

## Herramientas Matematicas

- [[herramientas-matematicas/teorema-parseval]] — Teorema de Parseval, conservacion de energia
- [[herramientas-matematicas/teorema-muestreo]] — Nyquist-Shannon, aliasing
- [[herramientas-matematicas/densidad-espectral-potencia]] — DEP, Wiener-Khinchin, autocorrelacion
- [[herramientas-matematicas/teorema-convolucion]] — Convolucion tiempo-frecuencia
- [[herramientas-matematicas/transformada-hilbert]] — Hilbert, senal analitica, BLU
- [[herramientas-matematicas/senales-energia-potencia]] — Senales de energia vs potencia

## Modulacion Analogica

### Modulacion Lineal (AM)

- [[modulacion-analogica/am-vs-dsb-sc]] — AM convencional vs Doble Banda Suprimida
- [[modulacion-analogica/modulacion-ssb]] — Banda Lateral Unica (BLU)
- [[modulacion-analogica/receptor-superheterodino]] — Receptor superheterodino
- [[modulacion-analogica/indice-modulacion-am]] — Indice de modulacion en AM
- [[modulacion-analogica/modulacion-vsb]] — Banda Lateral Vestigial (TV)
- [[modulacion-analogica/multiplex-fdm]] — Multiplex por Division de Frecuencia

### Modulacion Exponencial (FM/PM)

- [[modulacion-analogica/fm-vs-pm]] — FM vs PM, diferencias fundamentales
- [[modulacion-analogica/ancho-banda-carson]] — Regla de Carson para FM
- [[modulacion-analogica/fm-banda-angosta]] — FM de banda angosta (NBFM)
- [[modulacion-analogica/preenfasis-deenfasis]] — Pre-enfasis y de-enfasis
- [[modulacion-analogica/fm-estereo]] — Transmision y recepcion FM estereo
- [[modulacion-analogica/modulador-fm]] — Tipos de moduladores y detectores FM

## Modulacion de Pulsos

- [[modulacion-pulsos/muestreo-ideal-natural]] — Muestreo ideal vs natural
- [[modulacion-pulsos/pcm-cuantificacion]] — PCM, cuantificacion, error
- [[modulacion-pulsos/companding]] — Companding, ley A y ley mu
- [[modulacion-pulsos/modulacion-delta]] — Modulacion Delta y Delta adaptativa
- [[modulacion-pulsos/multiplex-tdm]] — Multiplex por Division de Tiempo

## Modulacion Digital

- [[modulacion-digital/ask-fsk-psk]] — ASK, FSK, PSK (binario y M-ario)
- [[modulacion-digital/modulacion-qam]] — QAM y constelaciones
- [[modulacion-digital/constelaciones]] — Diagramas de constelacion
- [[modulacion-digital/probabilidad-error]] — Probabilidad de error, S/R en digital
- [[modulacion-digital/comparacion-digital-analogica]] — Digital vs analogica: ventajas
- [[modulacion-digital/codificacion-linea]] — Codificacion de linea (NRZ, RZ, Manchester)

## Ruido e Intercomparacion

- [[ruido/fuentes-ruido]] — Fuentes de ruido y radiointerferencias
- [[ruido/fuentes-ruido]] — Fuentes de ruido y radiointerferencias
- [[ruido/ruido-blanco-banda-angosta]] — Ruido blanco: caracteristicas
- [[ruido/ruido-banda-angosta]] — Ruido de banda angosta: I-Q, Rayleigh
- [[ruido/aclaracion-densidad-espectral-ruido]] — Densidad espectral: $N_0 = kT$ vs $4kT$
- [[ruido/temperatura-ruido]] — Temperatura equivalente de ruido Te
- [[ruido/factor-ruido-temperatura]] — Factor de ruido F, NF, conversion
- [[ruido/formula-friis]] — Formula de Friis para cuadripolos en cascada
- [[ruido/relacion-snr]] — Relacion Senal a Ruido (SNR)
- [[ruido/snr-modulacion-lineal]] — S/R en modulacion lineal, efecto umbral
- [[ruido/snr-modulacion-exponencial]] — S/R en FM/PM, red de enfasis
- [[ruido/efecto-umbral]] — Efecto umbral en FM y AM
- [[ruido/efecto-enfasis-fm-am]] — Enfasis en FM/AM, mejora 10-13 dB
- [[ruido/eficiencia-espectral-comparada]] — Eficiencia espectral por sistema
- [[ruido/ganancia-procesamiento-pulsos]] — Ganancia de procesamiento PCM
- [[ruido/intercomparacion-sistemas]] — Intercomparacion global de sistemas

## Teoria de la Informacion

- [[teoria-informacion/entropia-fuente]] — Entropia, fuente con y sin memoria
- [[teoria-informacion/capacidad-canal-shannon]] — Capacidad de canal, redundancia
- [[teoria-informacion/teorema-shannon-hartley]] — Teorema de Shannon-Hartley
- [[teoria-informacion/codigos-deteccion-error]] — Codigos de deteccion de error
- [[teoria-informacion/codigo-compacto]] — Codigo compacto, longitud media
- [[teoria-informacion/redundancia-compresion]] — Redundancia y compresion
- [[teoria-informacion/sistema-ideal-comunicaciones]] — Sistema ideal de comunicaciones

## Espectro Expandido

- [[espectro-expandido/cdma]] — CDMA: Acceso Multiple por Division de Codigo
- [[espectro-expandido/dsss]] — Secuencia Directa (DSSS)
- [[espectro-expandido/fhss]] — Salto de Frecuencia (FHSS)
- [[espectro-expandido/ofdm]] — OFDM: fundamentos y aplicaciones
- [[espectro-expandido/correlacion-senales]] — Correlacion de senales en CDMA
- [[espectro-expandido/prefijo-ciclico]] — Prefijo ciclico en OFDM
- [[espectro-expandido/aplicaciones-spread-spectrum]] — Aplicaciones practicas

## Conceptos Integradores

- [[conceptos-integradores/comparacion-global-modulaciones]] — Tabla comparativa de modulaciones
- [[conceptos-integradores/evolucion-sistemas]] — Evolucion historica de los sistemas
- [[conceptos-integradores/seleccion-modulacion]] — Criterios de seleccion de modulacion
- [[conceptos-integradores/compromisos-diseno]] — Compromisos de diseno fundamentales
- [[conceptos-integradores/aplicaciones-reales]] — Mapeo de modulaciones a aplicaciones
- [[conceptos-integradores/eb-n0-vs-snr]] — Eb/N0 vs SNR: comparacion justa
- [[conceptos-integradores/aportes-shannon]] — Claude Shannon: biografia y aportes al curso
- [[conceptos-integradores/aportes-nyquist]] — Harry Nyquist: muestreo, ISI, ruido termico
- [[conceptos-integradores/aportes-armstrong]] — Edwin Armstrong: superheterodino, FM
- [[conceptos-integradores/aportes-fourier]] — Joseph Fourier: base matematica del curso
- [[conceptos-integradores/aportes-carson]] — John Carson: regla de Carson, modulador balanceado
- [[conceptos-integradores/aportes-parseval]] — Parseval: conservacion de energia tiempo-frecuencia
- [[conceptos-integradores/aportes-hilbert]] — David Hilbert: transformada de Hilbert, señal analitica, SSB
- [[conceptos-integradores/pioneros-comunicaciones]] — Galeria completa de pioneros (Maxwell, Hertz, Marconi, Bell, Friis, Huffman, Hamming, Viterbi, etc.)

## Derivaciones Matematicas

- [[derivaciones/modulacion-am]] — Derivacion completa de AM
- [[derivaciones/modulacion-fm-carson]] — Regla de Carson: derivacion
- [[derivaciones/modulacion-fm-banda-angosta]] — FM banda angosta: derivacion
- [[derivaciones/modulacion-qam]] — QAM: derivacion completa
- [[derivaciones/teorema-parseval]] — Teorema de Parseval: derivacion
- [[derivaciones/teorema-shannon-hartley]] — Shannon-Hartley: derivacion
- [[derivaciones/ecuacion-friis]] — Formula de Friis: derivacion
- [[derivaciones/ecuacion-friis-extendida]] — Friis: derivacion extendida
- [[derivaciones/modulacion-am-extendida]] — AM: derivacion extendida
- [[derivaciones/modulacion-am-alternativa]] — AM: derivacion alternativa

## Resumenes y Mindmaps

- [[resumenes/overview-curso]] — Mapa mental del curso completo
- [[resumenes/modulacion-digital-unidad6]] — Unidad 6: mindmap detallado
- [[resumenes/resumen-modulacion-digital]] — Unidad 6: resumen completo (772 lineas)

## Problemas Resueltos

- [[problemas/ejercicio-ruido]] — Ejercicio de ruido (completo)
- [[problemas/tp5-ejercicio-3]] — TP5 Ejercicio 3: solucion

## Planificacion

- [[planificacion/programa-oficial]] — Programa oficial de la materia
- [[planificacion/progreso-actual]] — Estado actual de aprendizaje
- [[planificacion/mazo-anki]] — Mazo Anki completo (10 unidades, 60 cartas)

## Sesiones

- [[sesiones/2025-11-15-sesion]] — Sesion del 15/11/2025
- [[sesiones/conversaciones-claude]] — Indice de conversaciones Claude con conceptos del curso

---

*Wiki generada: 2025-11-16 | Mantenida con `/wiki ingest`, `/wiki lint`, `/wiki status`*
