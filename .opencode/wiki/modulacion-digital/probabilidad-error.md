---
tags:
  - wiki/modulacion-digital
source_file: explicaciones_anki/unidad_06/carta_31_ber_probabilidad_error.md
curso: Sistemas de Comunicaciones
unidad: 6
---

# Probabilidad de Error de Bit (BER)

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Definición

El **Bit Error Rate (BER)** es la probabilidad de que un bit transmitido se reciba erróneamente:

$$\boxed{BER = \frac{\text{bits erróneos}}{\text{total de bits transmitidos}}}$$

Es la métrica fundamental de calidad en sistemas de comunicación digital. [source]

## Factores que Afectan el BER

1. **$E_b/N_0$** (energía por bit / densidad de ruido): el factor dominante
2. **Tipo de modulación**: [[modulacion-digital/ask-fsk-psk|BPSK, FSK, QPSK]], [[modulacion-digital/modulacion-qam|QAM]]
3. **Tipo de detección**: coherente vs. no coherente
4. **Características del canal**: desvanecimiento, interferencia, ISI
5. **Codificación de canal**: códigos correctores reducen el BER efectivo

## Fórmulas para Canal AWGN

**BPSK / QPSK (coherente):**

$$\boxed{BER_{BPSK} = Q\left(\sqrt{\frac{2E_b}{N_0}}\right) = \frac{1}{2}\text{erfc}\left(\sqrt{\frac{E_b}{N_0}}\right)}$$

**FSK ortogonal (coherente):**

$$BER_{FSK} = Q\left(\sqrt{\frac{E_b}{N_0}}\right)$$

**M-QAM rectangular (aproximación):**

$$BER_{M\text{-}QAM} \approx \frac{2(\sqrt{M}-1)}{\sqrt{M}\log_2(M)} Q\left(\sqrt{\frac{3\log_2(M)E_b}{(M-1)N_0}}\right)$$

## Relación $E_b/N_0$ con SNR

$$\frac{E_b}{N_0} = SNR \cdot \frac{B}{R_b}$$

## Valores de Referencia

| Aplicación | BER objetivo | $E_b/N_0$ típico (QPSK) |
|------------|-------------|--------------------------|
| Voz digital | $10^{-3}$ – $10^{-4}$ | 4-6 dB |
| Video streaming | $10^{-6}$ | 10.5 dB |
| Datos críticos | $10^{-9}$ – $10^{-12}$ | 13-15 dB |
| Fibra óptica | $< 10^{-15}$ | > 15 dB + FEC |

## BER vs SER

Con mapeo Gray: $BER \approx SER / \log_2(M)$. Un error de símbolo típicamente afecta solo 1 bit. [analysis]

## Efecto de la Codificación

La codificación de canal ([[teoria-informacion/codigos-detectores-correctores|códigos correctores]]) puede mejorar el BER en órdenes de magnitud a costa de reducir la tasa efectiva. Ejemplo: código Hamming (7,4) reduce BER de $10^{-3}$ a $~2 \times 10^{-5}$.

## Trade-off Fundamental

Mayor eficiencia espectral requiere mayor $E_b/N_0$ para el mismo BER. Cada duplicación de bits/símbolo cuesta ~6 dB adicionales. [analysis]

## Ver también

- [[modulacion-digital/ask-fsk-psk]] — Curvas BER para modulaciones básicas
- [[modulacion-digital/constelaciones]] — Distancia mínima como determinante del BER
- [[ruido/relacion-snr]] — Relación SNR y su vínculo con $E_b/N_0$
- [[ruido/intercomparacion-sistemas]] — Comparación de sistemas vía BER
