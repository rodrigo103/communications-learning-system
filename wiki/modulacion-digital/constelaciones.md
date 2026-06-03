---
tags:
  - wiki/modulacion-digital
source_file: explicaciones_anki/unidad_06/carta_28_constelacion-modulacion-digital.md
curso: Sistemas de Comunicaciones
unidad: 6
---

# Diagramas de Constelación

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_06/carta_28_constelacion-modulacion-digital]]]

## Definición

Una **constelación** es la representación gráfica de todos los símbolos posibles de una modulación digital en el plano complejo I-Q. Cada punto $(I_k, Q_k)$ corresponde a un símbolo único. [source — [[../../explicaciones_anki/unidad_06/carta_28_constelacion-modulacion-digital]]]

## Representación Matemática

Cualquier señal modulada digitalmente puede expresarse en banda base compleja:

$$\tilde{s}(t) = I(t) + jQ(t) = A(t)e^{j\phi(t)}$$

donde:
- $I(t)$ = componente en fase (In-phase)
- $Q(t)$ = componente en cuadratura (Quadrature)
- $A(t) = \sqrt{I^2 + Q^2}$ = amplitud instantánea
- $\phi(t) = \arctan(Q/I)$ = fase instantánea

## Parámetros Clave

**Distancia euclidiana** entre símbolos $s_i$ y $s_j$:

$$d_{ij} = |s_i - s_j| = \sqrt{(I_i - I_j)^2 + (Q_i - Q_j)^2}$$

**Distancia mínima** de la constelación:

$$\boxed{d_{min} = \min_{i \neq j} d_{ij}}$$

**Energía promedio** por símbolo:

$$\boxed{E_s = \frac{1}{M}\sum_{k=1}^{M} (I_k^2 + Q_k^2)}$$

## Relación con Probabilidad de Error

Para canal AWGN, la probabilidad de error de símbolo se aproxima por:

$$P_e \approx Q\left(\frac{d_{min}}{2\sigma_n}\right)$$

**Principio fundamental:** mayor $d_{min}$ → menor $P_e$. [source — [[../../explicaciones_anki/unidad_06/carta_28_constelacion-modulacion-digital]]]

## Mapeo Gray

El mapeo Gray asigna códigos binarios a símbolos adyacentes difiriendo en solo 1 bit. Esto minimiza el BER porque un error de símbolo (a un vecino) produce solo 1 bit erróneo. [analysis]

## Constelaciones Típicas

| Modulación | $M$ | $d_{min}$ (norm.) | $E_b/N_0$ @ $10^{-6}$ |
|------------|-----|---------------------|------------------------|
| BPSK | 2 | 2 | 10.5 dB |
| QPSK | 4 | $\sqrt{2}$ | 10.5 dB |
| 8-PSK | 8 | 0.765 | 14 dB |
| 16-QAM | 16 | 0.632 | 14.5 dB |
| 64-QAM | 64 | 0.308 | 18.5 dB |

Mayor $M$ → mayor eficiencia espectral pero menor $d_{min}$ → requiere mayor SNR. [analysis]

## Diagnóstico con Constelaciones

- **Puntos nítidos**: buena SNR
- **Nubes difusas**: mucho ruido
- **Puntos desplazados**: error de frecuencia/DC offset
- **Elipses**: desbalance I/Q
- **Compresión externa**: saturación del amplificador

## Ver también

- [[../modulacion-digital/ask-fsk-psk]] — BPSK/QPSK como constelaciones básicas
- [[../modulacion-digital/modulacion-qam]] — Constelaciones rectangulares densas
- [[../modulacion-digital/probabilidad-error]] — Relación $d_{min}$ con BER
- [[../../claude-conversations/2025-11-20_modulaci-n-bpsk-sobre-fm-en-telemetr-a-espacial|Conversación: BPSK sobre FM en telemetría]]
