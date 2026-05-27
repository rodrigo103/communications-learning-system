---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_08/carta_41_eficiencia-espectral-comparada.md
curso: Sistemas de Comunicaciones
unidad: 8
---

# Eficiencia Espectral Comparada

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_08/carta_41_eficiencia-espectral-comparada]]]

La eficiencia espectral es la metrica fundamental para comparar que tan bien aprovechan el ancho de banda los distintos sistemas de modulacion.

## Definicion

$$\boxed{\eta = \frac{R_b}{B} \;\; [\text{bits/s/Hz}]}$$

Es la cantidad de bits por segundo que se transmiten por cada Hz de ancho de banda. [source — [[../../explicaciones_anki/unidad_08/carta_41_eficiencia-espectral-comparada]]]

## Eficiencia de M-QAM

Para modulacion M-QAM con filtro de raiz de coseno realzado y factor de roll-off $\alpha$:

$$\boxed{\eta_{\text{M-QAM}} = \frac{2\log_2(M)}{1 + \alpha}}$$

Ejemplos:
- 4-QAM (QPSK), $\alpha = 0.25$: $\eta = 1.6$ bits/s/Hz
- 16-QAM, $\alpha = 0.25$: $\eta = 3.2$ bits/s/Hz
- 64-QAM, $\alpha = 0.25$: $\eta = 4.8$ bits/s/Hz
- 256-QAM, $\alpha = 0$: $\eta = 8$ bits/s/Hz

## Limite de Shannon

El maximo teorico de eficiencia espectral esta dado por el teorema de Shannon-Hartley:

$$\boxed{\eta_{\text{max}} = \log_2(1 + \text{SNR})}$$

Ningun sistema real puede superar este limite. Los sistemas digitales modernos se acercan mucho mas que los analogicos. [source — [[../../explicaciones_anki/unidad_08/carta_41_eficiencia-espectral-comparada]]]

## Jerarquia de eficiencia espectral

$$\text{QAM} > \text{PSK} > \text{FSK}$$

- **QAM:** maxima eficiencia, usa amplitud y fase simultaneamente
- **PSK:** eficiencia intermedia, solo modula fase
- **FSK:** baja eficiencia, $\eta$ disminuye al aumentar $M$

[analysis]

## Compromiso eficiencia vs SNR

Duplicar la eficiencia espectral cuesta aproximadamente **6 dB** de SNR adicional. Este trade-off es fundamental en el diseno de sistemas: mas bits/Hz requieren mayor potencia o menor ruido. [analysis]

## Evolucion historica (2G → 5G)

| Generacion | Tecnologia | $\eta$ [bits/s/Hz] |
|---|---|---|
| 2G | GSM | 0.33 |
| 3G | WCDMA | ~3 |
| 4G | LTE | 15 |
| 5G | NR | 30 |

## Eficiencia en modulaciones analogicas

| Modulacion | $\eta$ aproximada |
|---|---|
| AM | ~1 |
| FM banda ancha | ~0.1 |

FM intercambia ancho de banda por SNR (aumenta el indice de modulacion $\beta$), lo que explica su baja eficiencia espectral pero alta calidad de audio. [analysis]

## Overhead de protocolo

La eficiencia practica es menor que la teorica debido a:
- Headers y preambulos
- Bandas de guarda
- Pilotos y senales de referencia
- Codigos de correccion de errores (agregan redundancia)

Estos overheads pueden reducir la eficiencia neta en 20-40%.

## Ver también

- [[../ruido/intercomparacion-sistemas]] — Intercomparacion de sistemas
- [[../modulacion-digital/modulacion-qam]] — Modulacion QAM
- [[../modulacion-digital/eficiencia-espectral]] — Eficiencia espectral
- [[../teoria-informacion/teorema-shannon-hartley]] — Teorema de Shannon-Hartley
- [[../modulacion-digital/comparacion-digital-analogica]] — Digital vs analogica
- [[../conceptos-integradores/comparacion-global-modulaciones]] — Comparacion global
