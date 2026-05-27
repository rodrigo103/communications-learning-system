---
tags:
  - wiki/herramientas-matematicas
source_file: explicaciones_anki/unidad_02/carta_05_teorema-muestreo.md
curso: Sistemas de Comunicaciones
unidad: 2
---

# Teorema del Muestreo de Nyquist-Shannon

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_02/carta_05_teorema-muestreo]]]

## Enunciado

Una señal de banda limitada con frecuencia maxima $f_m$ puede ser **completamente reconstruida** a partir de sus muestras si la frecuencia de muestreo cumple [source — [[../../explicaciones_anki/unidad_02/carta_05_teorema-muestreo]]]:

$$\boxed{f_s \geq 2f_m}$$

La frecuencia minima $f_s = 2f_m$ se conoce como **frecuencia de Nyquist**.

## Importancia Practica

- Fundamento de la conversion analogico-digital (ADC) [source — [[../../explicaciones_anki/unidad_02/carta_05_teorema-muestreo]]]
- Define la minima tasa de muestreo necesaria para no perder informacion
- Si $f_s < 2f_m$ ocurre **aliasing** (solapamiento espectral) y perdida irreversible de informacion
- Base de sistemas PCM, audio digital, video digital

## Desarrollo Matematico

### Señal de Banda Limitada

$x(t)$ es de banda limitada si $X(f) = 0$ para $|f| > f_m$.

### Proceso de Muestreo Ideal

El muestreo se modela como multiplicacion por un tren de impulsos [source — [[../../explicaciones_anki/unidad_02/carta_05_teorema-muestreo]]]:

$$x_s(t) = x(t) \cdot \sum_{n=-\infty}^{\infty} \delta(t - nT_s)$$

donde $T_s = 1/f_s$ es el periodo de muestreo.

### Efecto en Frecuencia

En el dominio frecuencial, el muestreo crea **replicas del espectro** [source — [[../../explicaciones_anki/unidad_02/carta_05_teorema-muestreo]]]:

$$\boxed{X_s(f) = \frac{1}{T_s} \sum_{k=-\infty}^{\infty} X(f - kf_s)}$$

### Condicion de No Solapamiento

Para que las replicas no se solapen entre si:

$$f_s - f_m > f_m \quad \Rightarrow \quad f_s \geq 2f_m$$

## Aliasing

Cuando $f_s < 2f_m$, las replicas espectrales se solapan y las frecuencias altas aparecen como frecuencias bajas [source — [[../../explicaciones_anki/unidad_02/carta_05_teorema-muestreo]]]. El aliasing es **irreversible**: una vez que ocurre, la informacion se pierde para siempre.

**Ejemplo**: señal de 10 kHz muestreada a $f_s = 15$ kHz:
- Nyquist requiere $f_s \geq 20$ kHz
- La componente de 10 kHz aparece tambien en $|10 - 15| = 5$ kHz
- La señal de 10 kHz se percibe incorrectamente como 5 kHz

## Valores Tipicos

| Aplicacion | $f_m$ | $f_s$ estandar | Justificacion |
|------------|-------|----------------|---------------|
| Telefonia | 3.4 kHz | 8 kHz | Voz inteligible |
| CD Audio | 20 kHz | 44.1 kHz | Espectro audible completo |
| Audio Pro | 20 kHz | 48/96/192 kHz | Post-procesamiento |
| Video | 4.2 MHz | 13.5 MHz | ITU-R 601 |

## Analogia

El muestreo es como tomar fotografias de una rueda girando. Si tomas suficientes fotos por segundo (al menos 2 por ciclo), puedes reconstruir perfectamente el movimiento. Con menos fotos, la rueda puede parecer girar hacia atras (efecto estroboscopico = aliasing) [analysis].

## Puntos Clave

- ✓ $f_s \geq 2f_m$ es un limite fundamental, no arbitrario [source — [[../../explicaciones_anki/unidad_02/carta_05_teorema-muestreo]]]
- ✓ El aliasing es irreversible [source — [[../../explicaciones_anki/unidad_02/carta_05_teorema-muestreo]]]
- ✓ La eleccion practica de $f_s$ incluye margenes para filtros reales
- ✓ Tasa de bits: $R = f_s \times \text{bits/muestra}$

## Ver tambien

- [[../herramientas-matematicas/teorema-parseval]]
- [[../herramientas-matematicas/densidad-espectral-potencia]]
- [[../modulacion-pulsos/pcm-cuantificacion]]
- [[../modulacion-pulsos/muestreo-ideal-natural]]
