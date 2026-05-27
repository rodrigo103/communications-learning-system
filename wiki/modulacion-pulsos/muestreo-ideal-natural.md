---
tags:
  - wiki/modulacion-pulsos
source_file: explicaciones_anki/unidad_05/carta_22_modulacion-analogica-pulsos.md
curso: Sistemas de Comunicaciones
unidad: 5
---

# Muestreo Ideal, Natural y Modulación PAM

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_05/carta_22_modulacion-analogica-pulsos]]]

## Muestreo Ideal vs. Natural

El muestreo es la primera etapa en la digitalización de señales. Partiendo de una señal continua $m(t)$, el muestreo convierte el tiempo continuo en discreto mediante un tren de pulsos periódicos de período $T_s = 1/f_s$, con $f_s \geq 2f_m$ según [[../herramientas-matematicas/teorema-muestreo]].

### Muestreo Ideal (Impulsos)

El muestreo ideal utiliza un tren de deltas de Dirac:

$$x_s(t) = m(t) \cdot \sum_{n=-\infty}^{\infty} \delta(t - nT_s) = \sum_{n=-\infty}^{\infty} m(nT_s) \, \delta(t - nT_s)$$

En el dominio frecuencial, el espectro se replica cada $f_s$:

$$X_s(f) = f_s \sum_{k=-\infty}^{\infty} X(f - kf_s)$$

Si $f_s < 2f_{max}$ las réplicas se solapan, produciendo **aliasing**. [source — [[../../explicaciones_anki/unidad_05/carta_22_modulacion-analogica-pulsos]]]

### Muestreo Natural (PAM Natural)

En el muestreo natural, la señal $m(t)$ se multiplica por un tren de pulsos rectangulares de ancho $\tau$:

$$s_{PAM\text{-}natural}(t) = m(t) \cdot \sum_{n=-\infty}^{\infty} \Pi\left(\frac{t - nT_s}{\tau}\right)$$

La forma de $m(t)$ se preserva dentro de cada pulso, generando un espectro:

$$S_{PAM}(f) = \frac{\tau}{T_s} M(f) \cdot \text{sinc}(\pi f \tau) + \text{réplicas en } kf_s$$

### Sample-and-Hold (PAM Flat-Top)

La versión práctica más común mantiene la amplitud constante durante el pulso:

$$s_{PAM\text{-}flat}(t) = \sum_{n=-\infty}^{\infty} m(nT_s) \cdot \Pi\left(\frac{t - nT_s}{\tau}\right)$$

Esta variante introduce **distorsión de apertura** que requiere ecualización en el receptor. [analysis]

## PAM, PWM y PPM

La **Pulse Amplitude Modulation (PAM)** varía la amplitud de los pulsos proporcionalmente a $m(t)$. Es la base de [[../modulacion-pulsos/pcm-cuantificacion]].

- **PWM** (Pulse Width Modulation): varía el ancho del pulso, $\tau(t) = \tau_0[1 + k_{PWM} \cdot m(t)]$
- **PPM** (Pulse Position Modulation): varía la posición temporal, $\Delta t(n) = k_{PPM} \cdot m(nT_s)$

Orden de robustez al ruido: PAM < PWM < PPM (la información temporal es más robusta que la de amplitud). [analysis]

## Ancho de Banda

El ancho de banda requerido se relaciona con el ancho del pulso:

$$\boxed{BW_{min} = \frac{1}{\tau}}$$

Para telefonía con $f_s = 8$ kHz y ciclo de trabajo del $10\%$: $\tau = 12.5$ μs, $BW_{min} = 80$ kHz. [source — [[../../explicaciones_anki/unidad_05/carta_22_modulacion-analogica-pulsos]]]

## Ver también

- [[../herramientas-matematicas/teorema-muestreo]] — Fundamento de la frecuencia de muestreo
- [[../modulacion-pulsos/pcm-cuantificacion]] — PAM como primera etapa del PCM
- [[../modulacion-pulsos/multiplex-tdm]] — Multiplexación temporal de canales PAM
