---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_07/carta_38_ruido-receptor-am.md
curso: Sistemas de Comunicaciones
unidad: 7
---

# Relación Señal-Ruido (SNR)

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Definición

La relación señal-ruido (SNR) es la métrica fundamental de calidad en comunicaciones:

$$\boxed{SNR = \frac{P_{se\tilde{n}al}}{P_{ruido}}}$$

En dB: $SNR_{dB} = 10\log_{10}(SNR)$. [source]

## Potencia de Ruido Disponible

La potencia de ruido térmico en un ancho de banda $B$:

$$\boxed{N = kTB}$$

A temperatura de referencia $T_0 = 290$ K: $N = -174 + 10\log_{10}(B)$ dBm. [source]

## SNR de Entrada vs. SNR de Salida

La [[ruido/factor-ruido-temperatura|figura de ruido]] relaciona ambas:

$$SNR_{out} = \frac{SNR_{in}}{F}$$

Cada dispositivo en la cadena degrada la SNR. La [[ruido/formula-friis|fórmula de Friis]] permite calcular la degradación total.

## Relación con $E_b/N_0$

Para sistemas digitales, se prefiere la métrica normalizada:

$$\boxed{\frac{E_b}{N_0} = SNR \cdot \frac{B}{R_b}}$$

donde $E_b$ es la energía por bit y $R_b$ la tasa de bits. Esta métrica permite comparar sistemas con diferentes anchos de banda y tasas. [source]

## SNR en Receptores AM

Para AM con detección de envolvente, la señal recibida con ruido es:

$$r(t) = [A_c(1 + m(t)) + x(t)]\cos(2\pi f_c t) - y(t)\sin(2\pi f_c t)$$

**Alto SNR** (señal $\gg$ ruido): la salida del detector es aproximadamente $A_c m(t) + x(t)$. Solo la componente en fase del ruido afecta.

$$\boxed{SNR_{out}^{AM} = \frac{m^2}{2 + m^2} \cdot SNR_{in}}$$

**Bajo SNR**: ocurre el [[ruido/efecto-umbral|efecto umbral]], la señal es suprimida por el ruido.

## SNR en FM

Sobre el umbral, FM ofrece ganancia de SNR:

$$\boxed{SNR_{out}^{FM} = 3\beta^2(\beta + 1) \cdot SNR_{in}}$$

donde $\beta$ es el índice de modulación. Ver [[ruido/snr-modulacion-exponencial]]. [source]

## Ver también

- [[ruido/factor-ruido-temperatura]] — Caracterización del ruido en dispositivos
- [[ruido/formula-friis]] — SNR en sistemas en cascada
- [[ruido/intercomparacion-sistemas]] — Comparación de SNR entre sistemas
