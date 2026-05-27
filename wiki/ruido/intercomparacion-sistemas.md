---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_08/carta_40_parametros-comparacion-sistemas.md
curso: Sistemas de Comunicaciones
unidad: 8
---

# Intercomparación de Sistemas de Modulación

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Parámetros de Comparación

No existe una modulación universalmente óptima. Cada sistema representa compromisos entre múltiples parámetros: [analysis]

1. **Eficiencia espectral** $\eta = R_b/B$ [bits/s/Hz]
2. **Eficiencia de potencia**: $E_b/N_0$ requerido para un BER objetivo
3. **SNR de salida** vs. SNR de entrada (ganancia de procesamiento)
4. **Complejidad** de implementación
5. **Robustez** ante ruido, interferencia y desvanecimiento
6. **Requisitos de sincronización**

## Figura de Mérito $\gamma$

Para comparar sistemas con diferentes anchos de banda, se define:

$$\boxed{\gamma = \frac{SNR_{out}}{SNR_{in}} \cdot \frac{B_{ref}}{B_{sistema}}}$$

Un $\gamma > 1$ indica que el sistema ofrece mejor SNR por unidad de ancho de banda que la transmisión en banda base. [analysis]

## Trade-off Fundamental (Shannon)

El [[teoria-informacion/teorema-shannon-hartley|teorema de Shannon-Hartley]] establece el límite:

$$C = B \log_2(1 + SNR)$$

Esto implica que **ancho de banda y potencia son intercambiables**: se puede reducir la potencia requerida aumentando el ancho de banda, y viceversa. [source]

## Comparación Global

### Modulaciones Analógicas

| Sistema | $SNR_{out}$ (relativo) | BW | Ventaja clave |
|---------|------------------------|-----|---------------|
| AM (envolvente) | $\frac{m^2}{2+m^2} SNR_{in}$ | $2f_m$ | Simplicidad |
| DSB-SC (síncrono) | $SNR_{in}$ | $2f_m$ | Sin umbral |
| SSB (síncrono) | $SNR_{in}$ | $f_m$ | Máxima eficiencia BW |
| FM ($\beta = 5$) | $3\beta^2 \cdot SNR_{in}$ | $2(\Delta f + f_m)$ | Mejor SNR (sobre umbral) |
| FM con énfasis | $3\beta^2 \cdot SNR_{in} + 12$ dB | Igual | Máxima calidad analógica |

### Modulaciones Digitales

| Sistema | $\eta$ [bits/s/Hz] | $E_b/N_0$ @ $10^{-6}$ |
|---------|-------------------|------------------------|
| BPSK | 1 | 10.5 dB |
| QPSK | 2 | 10.5 dB |
| 16-QAM | 4 | 14.5 dB |
| 64-QAM | 6 | 18.8 dB |
| 256-QAM | 8 | 24.4 dB |

## SNR vs. Ancho de Banda: Trade-off

**FM** es el ejemplo clásico: sacrifica ancho de banda (180 kHz vs. 10-30 kHz para AM) a cambio de SNR superior (~26 dB de ganancia para $\beta = 5$ más ~12 dB por énfasis).

**PCM** sigue el mismo principio: expande el ancho de banda ($n$ veces) a cambio de inmunidad al ruido por regeneración.

## Elección según Aplicación

| Aplicación | Prioridad | Mejor opción |
|------------|-----------|-------------|
| Radio AM broadcast | Cobertura, simplicidad | AM |
| Radio FM broadcast | Calidad de audio | FM con énfasis |
| Satélite (potencia limitada) | Eficiencia de potencia | QPSK, BPSK |
| Fibra óptica (BW abundante) | Eficiencia espectral | 64-QAM, 256-QAM |
| Telefonía móvil (adaptativo) | Balance dinámico | QPSK a 256-QAM |

## Ver también

- [[ruido/relacion-snr]] — Métrica fundamental de comparación
- [[ruido/snr-modulacion-lineal]] — Desempeño de AM, DSB-SC, SSB
- [[ruido/snr-modulacion-exponencial]] — Desempeño de FM y PM
- [[ruido/efecto-umbral]] — Limitación crítica de FM
- [[conceptos-integradores/comparacion-global-modulaciones]] — Visión integradora de todas las modulaciones
- [[teoria-informacion/teorema-shannon-hartley]] — Límite teórico fundamental
