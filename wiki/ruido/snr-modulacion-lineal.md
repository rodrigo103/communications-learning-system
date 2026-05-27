---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_07/carta_38_ruido-receptor-am.md
curso: Sistemas de Comunicaciones
unidad: 8
---

# SNR en Modulaciones Lineales

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_07/carta_38_ruido-receptor-am]]]

## AM con Portadora (DSB-FC)

La señal recibida con ruido de banda angosta:

$$r(t) = [A_c(1 + m(t)) + x(t)]\cos(2\pi f_c t) - y(t)\sin(2\pi f_c t)$$

### Detección de Envolvente

**SNR alta** ($A_c \gg \sigma_n$): la envolvente es aproximadamente:

$$E(t) \approx A_c + A_c m(t) + x(t)$$

Salida del detector (quitando DC): $y_D(t) = A_c m(t) + x(t)$.

$$\boxed{SNR_{out}^{AM} = \frac{m^2}{2 + m^2} \cdot SNR_{in}}$$

Para $m = 1$ (100% modulación): $SNR_{out} = SNR_{in}/3$ (pérdida de ~4.8 dB). [source — [[../../explicaciones_anki/unidad_07/carta_38_ruido-receptor-am]]]

### Efecto Umbral

Por debajo de $SNR_{in} \approx 10$ dB, la envolvente sigue al ruido y no a la señal — **supresión de la modulación**. La señal se pierde completamente. [source — [[../../explicaciones_anki/unidad_07/carta_38_ruido-receptor-am]]]

## DSB-SC (Detección Síncrona)

Con detección coherente (sin umbral):

$$SNR_{out}^{DSB\text{-}SC} = SNR_{in}$$

La detección síncrona no tiene efecto umbral, pero requiere recuperación de portadora. [analysis]

## SSB (Detección Síncrona)

$$\boxed{SNR_{out}^{SSB} = SNR_{in}}$$

Misma SNR que DSB-SC, pero usando la mitad del ancho de banda. SSB es la modulación lineal más eficiente espectralmente. [source — [[../../explicaciones_anki/unidad_07/carta_38_ruido-receptor-am]]]

## Comparación de Modulaciones Lineales

| Modulación | $SNR_{out}$ relativo | BW | Umbral |
|-----------|----------------------|-----|--------|
| AM (envolvente) | $\frac{m^2}{2+m^2} SNR_{in}$ | $2f_m$ | ~10 dB |
| DSB-SC (síncrono) | $SNR_{in}$ | $2f_m$ | No tiene |
| SSB (síncrono) | $SNR_{in}$ | $f_m$ | No tiene |

**Conclusión:** SSB ofrece la misma SNR de salida que DSB-SC con la mitad del ancho de banda, siendo la modulación lineal óptima en el trade-off BW-SNR. [analysis]

## Ver también

- [[../ruido/relacion-snr]] — Definiciones y métricas de SNR
- [[../modulacion-analogica/am-vs-dsb-sc]] — Comparación detallada de variantes AM
- [[../modulacion-analogica/modulacion-ssb]] — Modulación de banda lateral única
- [[../ruido/efecto-umbral]] — Fenómeno del umbral en detalle
- [[../ruido/intercomparacion-sistemas]] — Comparación global con modulaciones exponenciales
