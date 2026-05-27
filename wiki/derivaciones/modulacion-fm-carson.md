---
tags:
  - wiki/derivaciones
  - wiki/modulacion-analogica
source_file: outputs/derivations/FM_Carson_parallel_20251115.md
curso: Sistemas de Comunicaciones
unidad: 4
---

# Derivación de FM y Regla de Carson

> **Last verified:** 2025-11-15 | **Verified by:** source

## Fundamento: modulación angular

Una señal modulada en ángulo tiene la forma general:

$$s(t) = A_c \cos[2\pi f_c t + \phi(t)]$$

donde $\phi(t)$ es la desviación de fase variable en el tiempo.

### Frecuencia instantánea

La frecuencia instantánea se define como la derivada de la fase instantánea:

$$f_i(t) = f_c + \frac{1}{2\pi}\frac{d\phi(t)}{dt}$$

## FM: definición fundamental

En **Frequency Modulation (FM)**, la desviación de frecuencia instantánea es proporcional al mensaje:

$$f_i(t) = f_c + k_f m(t)$$

donde $k_f$ es la sensibilidad de frecuencia [Hz/V] [source — [[../../outputs/derivations/FM_Carson_parallel_20251115]]].

Integrando para obtener la fase:

$$\phi(t) = 2\pi k_f \int_{-\infty}^{t} m(\tau) d\tau$$

La señal FM completa es:

$$\boxed{s_{FM}(t) = A_c \cos\left[2\pi f_c t + 2\pi k_f \int_{-\infty}^{t} m(\tau) d\tau\right]}$$

## Modulación con tono único

Para $m(t) = A_m \cos(2\pi f_m t)$:

### Desviación de frecuencia

$$\boxed{\Delta f = k_f A_m}$$

Es la máxima excursión de frecuencia respecto a $f_c$.

### Índice de modulación

$$\boxed{\beta = \frac{\Delta f}{f_m}}$$

$\beta$ determina el ancho de banda y si la FM es de banda angosta o ancha [analysis].

### Señal FM con tono único

Sustituyendo:

$$\boxed{s_{FM}(t) = A_c \cos[2\pi f_c t + \beta \sin(2\pi f_m t)]}$$

## Espectro FM: funciones de Bessel

Usando la identidad de Jacobi-Anger:

$$s_{FM}(t) = A_c \sum_{n=-\infty}^{\infty} J_n(\beta) \cos[2\pi(f_c + n f_m)t]$$

donde $J_n(\beta)$ son las funciones de Bessel de primera especie [source — [[../../outputs/derivations/FM_Carson_parallel_20251115]]].

El espectro FM contiene **infinitas bandas laterales** (a diferencia de AM que tiene solo 2), pero las amplitudes $J_n(\beta)$ decaen con $n$.

### Propiedades de Bessel relevantes

- $J_0(0) = 1$, $J_n(0) = 0$ para $n \neq 0$
- $\sum_{n=-\infty}^{\infty} J_n^2(\beta) = 1$ (conservación de potencia)
- Para $\beta \ll 1$: $J_0(\beta) \approx 1$, $J_1(\beta) \approx \beta/2$, $J_n(\beta) \approx 0$ para $n > 1$
- Bandas significativas: aproximadamente $\beta + 1$ pares con $|J_n(\beta)| > 0.01$

## Regla de Carson

La regla de Carson estima el ancho de banda que contiene ~98% de la potencia:

$$\boxed{BW_{Carson} = 2(\Delta f + f_m) = 2f_m(\beta + 1)}$$

Para una señal general con ancho de banda $B$:

$$\boxed{BW_{Carson} = 2(\Delta f + B)}$$

### Precisión

Comparada con el ancho de banda exacto (corte al 1% por Bessel), Carson tiene un error de aproximadamente $\pm 10\%$ para valores prácticos de $\beta$ [analysis].

## Clasificación: NBFM vs WBFM

| Tipo | Condición | Ancho de banda |
|------|-----------|----------------|
| **NBFM** | $\beta < 0.3$ | $BW \approx 2f_m$ |
| **WBFM** | $\beta > 1$ | $BW \approx 2\Delta f$ |

## Ejemplo: FM broadcast

- $\Delta f = 75$ kHz, $f_m = 15$ kHz, $\beta = 5$
- $BW = 2(75 + 15) = 180$ kHz
- Asignación práctica: 200 kHz (con bandas de guarda)

## Ganancia SNR en FM

Para WBFM, la mejora de SNR respecto a AM es:

$$\frac{SNR_{FM}}{SNR_{AM}} \approx \frac{3\beta^3}{2}$$

FM intercambia ancho de banda por SNR: $SNR_{FM} \propto \beta^2 \propto BW^2$ [analysis].

## Ver también

- [[../modulacion-analogica/ancho-banda-carson]]
- [[../modulacion-analogica/fm-vs-pm]]
- [[../derivaciones/modulacion-fm-banda-angosta]]
- [[../modulacion-analogica/funciones-bessel]]
- [[../ruido/efecto-umbral-fm]]
