---
tags:
  - wiki/conceptos-integradores
source_file: explicaciones_anki/conceptos_integradores/carta_60_evolucion_historica_sistemas_modulacion.md
curso: Sistemas de Comunicaciones
unidad: 1-10
---

# Evolucion Historica de Sistemas de Modulacion

> **Last verified:** 2025-11-16 | **Verified by:** source

## Tendencias Fundamentales

La historia de las telecomunicaciones es la historia de **como hemos aprendido a usar el espectro electromagnetico de manera cada vez mas eficiente**. Tres fuerzas motrices guian esta evolucion: [analysis]

1. **Limites fundamentales** (Shannon, 1948): cada generacion busca acercarse a $C = B\log_2(1 + S/N)$
2. **Demandas de la aplicacion**: de broadcasting de voz a realidad virtual en tiempo real
3. **Avances tecnologicos**: del transistor al DSP, FPGAs, y procesamiento con IA

---

## Cronologia por Eras

### Era 1: Analogica (1920s – 1980s)

**AM (1920s)**:
- Primera modulacion practica: deteccion de envolvente simple
- Propagacion ionosferica favorable (onda media), alcance de cientos de km
- Deficiencia: solo 33% de eficiencia maxima de potencia, susceptible al ruido

**FM (1930s – presente)**:
- Edwin Armstrong (1933): amplitud constante $\to$ inmunidad al ruido
- Regla de Carson: $BW_{FM} \approx 2(\Delta f + f_m)$
- Mejora de SNR proporcional a $\beta^2$: $\frac{SNR_{out}}{SNR_{in}} \approx 3\beta^2$
- Pre-enfasis/de-enfasis: mejora adicional de 10-13 dB
- Trade-off: calidad hi-fi a costa de 20x mas espectro que AM

**SSB y VSB**:
- SSB: eficiencia 100%, usado en HF militar
- VSB: compromiso AM-SSB, base de TV analogica (NTSC, PAL)

### Era 2: Transicion Digital (1980s – 2000)

**PCM (1960s – presente)**:
- Digitalizacion: muestreo (Nyquist) + cuantificacion + codificacion
- $SNR_q \approx 6n + 1.76$ dB para $n$ bits/muestra
- Ventaja clave: regeneracion digital sin perdida

**GSM — 2G TDMA (1991)**:
- GMSK: envolvente constante, eficiente para baterias moviles
- 8 usuarios por portadora de 200 kHz (TDMA + FDMA)
- $\eta \approx 1.35$ bits/s/Hz — modesta pero robusta

**IS-95 — 2G CDMA (1993)**:
- Cambio de paradigma: todos comparten frecuencia, separados por codigos
- Soft capacity: mas usuarios = degradacion gradual, no limite duro
- Control de potencia a 800 Hz para mitigar near-far

### Era 3: Internet Movil (2000 – 2010)

**3G — WCDMA / CDMA2000**:
- CDMA de banda ancha (5 MHz), chip rate 3.84 Mcps
- Turbo codes: revolucionarios, a 0.5 dB de Shannon
- Modulacion adaptativa: QPSK a 16-QAM segun condiciones

**Limitaciones que motivaron 4G**: [analysis]
- CDMA no escala bien a tasas muy altas (MAI crece con capacidad)
- Control de potencia intratable con muchos usuarios
- Ecualizacion compleja en canales selectivos en frecuencia

### Era 4: OFDM y MIMO (2010 – 2020)

**4G LTE (2009)**:
- Cambio radical: CDMA $\to$ OFDMA
- Subportadoras ortogonales: $\Delta f = 15$ kHz
- Modulacion por subportadora: QPSK a 256-QAM
- MIMO: multiplica capacidad sin mas espectro ni potencia
- Eficiencia espectral: 3-5x mejor que 3G

**Por que OFDM reemplazo CDMA**:
- Multitrayecto: enemigo en CDMA, aliado en OFDM
- Escalabilidad flexible: 1.4 a 20 MHz
- Ecualizacion trivial: $Y_k = H_k X_k + N_k \Rightarrow \hat{X}_k = Y_k / H_k$

### Era 5: Diversidad de Servicios (2020+)

**5G NR**:
- Numerologia flexible: $\Delta f = 15$ a 240 kHz
- Bandas mmWave (24-52 GHz): espectro abundante, canales de 100+ MHz
- Massive MIMO: 64-256 antenas, pencil beams
- LDPC + Polar codes: reemplazan Turbo codes
- Network slicing: una red fisica $\to$ multiples redes logicas

Casos de uso: **eMBB** (banda ancha), **URLLC** (ultra-confiable, baja latencia), **mMTC** (IoT masivo).

---

## Acercamiento al Limite de Shannon

| Generacion | $\eta$ tipica | % del limite de Shannon | Tecnologia clave |
|-----------|---------------|------------------------|------------------|
| FM analogico | (equiv.) 0.1 | $\sim 5\%$ | Discriminador |
| 2G GSM | 1.35 | $\sim 8\%$ | GMSK |
| 3G WCDMA | 0.5-2 | $\sim 18\%$ | CDMA + Turbo |
| 4G LTE | 1.5-5 | $\sim 54\%$ | OFDM + MIMO |
| 5G NR | 2-8+ | $\sim 75\%$ | Flex + mmWave |

En 100 anos hemos pasado de $\sim 5\%$ a $\sim 75\%$ del limite teorico. Los ultimos dB son los mas dificiles (y costosos). [analysis]

---

## Lecciones Historicas

- La complejidad es funcion de la tecnologia disponible: OFDM se propuso en los 1960s pero solo fue practico cuando las FFTs se pudieron implementar en tiempo real (2000s).
- No siempre gana el mejor desempeno tecnico: GSM (mas simple) domino sobre CDMA (mas capacidad) por costo, ecosistema y simplicidad.
- Cada generacion no reemplaza sino que **complementa**: 2G/3G/4G/5G coexisten como capas de cobertura y capacidad.

## Ver tambien

- [[introduccion/necesidad-modulacion]]
- [[modulacion-digital/comparacion-digital-analogica]]
- [[espectro-expandido/aplicaciones-spread-spectrum]]
- [[conceptos-integradores/comparacion-global-modulaciones]]
- [[teoria-informacion/teorema-shannon-hartley]]
- [[conceptos-integradores/seleccion-modulacion]]
