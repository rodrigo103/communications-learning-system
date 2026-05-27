---
tags:
  - wiki/conceptos-integradores
source_file: explicaciones_anki/conceptos_integradores/carta_57_eb_n0_vs_snr.md
curso: Sistemas de Comunicaciones
unidad: [7, 8, 9]
---

# Eb/N0 vs SNR

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/conceptos_integradores/carta_57_eb_n0_vs_snr]]]

$E_b/N_0$ (energia por bit sobre densidad espectral de ruido) y SNR (relacion senal a ruido) son dos metricas fundamentales para evaluar el desempeno de sistemas de comunicacion. Aunque relacionadas, sirven para propositos distintos.

## Definiciones

- **$E_b$:** Energia por bit [Joules]
- **$N_0$:** Densidad espectral de potencia de ruido [W/Hz]
- **$S$ (o $P_r$):** Potencia de senal recibida [W]
- **$N$:** Potencia de ruido total $N = N_0 B$ [W]
- **SNR:** $S/N$, adimensional

## Relacion fundamental

$$\boxed{\frac{E_b}{N_0} = \frac{S}{N} \cdot \frac{B}{R_b}}$$

donde $B$ es el ancho de banda y $R_b$ la tasa de bits. Esta ecuacion es el **puente** entre ambas metricas. [source — [[../../explicaciones_anki/conceptos_integradores/carta_57_eb_n0_vs_snr]]]

## Relacion con energia de simbolo

Para modulacion M-aria:

$$\boxed{\frac{E_s}{N_0} = \frac{E_b}{N_0} \cdot \log_2(M)}$$

donde $E_s$ es la energia por simbolo. Cada simbolo transporta $\log_2(M)$ bits.

## Conversion SNR a dB

$$\boxed{\text{SNR}_{\text{dB}} = \left(\frac{E_b}{N_0}\right)_{\text{dB}} + 10\log_{10}(\log_2 M) - 10\log_{10}\left(\frac{B}{R_s}\right)}$$

## Por que usar Eb/N0 en lugar de SNR

| Metrica | Depende de | Mejor para |
|---|---|---|
| SNR | Ancho de banda, tasa de datos | Analisis de un sistema especifico |
| Eb/N0 | Solo de la modulacion y BER deseada | **Comparar sistemas distintos** |

$E_b/N_0$ es **independiente del ancho de banda**, lo que permite comparar de forma justa sistemas con diferentes $B$ y $R_b$. [analysis]

## Limite de Shannon en Eb/N0

El limite fundamental de Shannon expresado en $E_b/N_0$:

$$\boxed{\frac{E_b}{N_0} \geq \ln(2) \approx -1.59 \text{ dB}}$$

Este es el **minimo absoluto** de $E_b/N_0$ requerido para comunicacion confiable (con $B \to \infty$). Ningun sistema real puede operar por debajo de este valor. [source — [[../../explicaciones_anki/conceptos_integradores/carta_57_eb_n0_vs_snr]]]

## Ejemplo comparativo: BPSK vs QPSK

| Modulacion | $E_b/N_0$ para BER = $10^{-5}$ | Tasa de bits | Ancho de banda |
|---|---|---|---|
| BPSK | ~9.6 dB | $R_b$ | $2R_b$ |
| QPSK | ~9.6 dB | $2R_b$ | $R_b$ |

Ambas requieren el mismo $E_b/N_0$ para la misma BER, pero QPSK duplica la tasa de bits en el mismo ancho de banda. El $E_b/N_0$ identico refleja que ambas tienen la misma eficiencia energetica por bit. [analysis]

## Espectro expandido y el factor B/Rb

En DSSS (Direct Sequence Spread Spectrum), el factor de expansion $B/R_b$ (ganancia de procesamiento) permite:

$$\frac{S}{N} = \frac{E_b}{N_0} \cdot \frac{R_b}{B}$$

Con $B \gg R_b$, se puede tener SNR de recepcion **negativa** (senal bajo el ruido) y aun asi $E_b/N_0$ suficiente para demodular. Esto es la base de CDMA y GPS. [analysis]

## Ver también

- [[../ruido/relacion-snr]] — Relacion Senal a Ruido
- [[../teoria-informacion/teorema-shannon-hartley]] — Teorema Shannon-Hartley
- [[../conceptos-integradores/comparacion-global-modulaciones]] — Comparacion global
- [[../modulacion-digital/probabilidad-error]] — Probabilidad de error
- [[../conceptos-integradores/compromisos-diseno]] — Compromisos de diseno
