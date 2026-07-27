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

## Multiplicadores y mezcladores de frecuencia (el patrón más testeado)

Aparece constantemente en los finales ("se la pasa por un cuadruplicador", "por tres duplicadores en serie"). La regla operativa es: un multiplicador $\times n$ **multiplica la fase entera**, con lo cual $f_c\to nf_c$, $\Delta f\to n\Delta f$, $\beta\to n\beta$ — pero **$f_m$ no cambia**. Justificación: [analysis]

### Por qué el multiplicador multiplica la fase

Un multiplicador de frecuencia es un **dispositivo no lineal seguido de un filtro pasabanda**. El caso más simple, elevar al cuadrado, ya lo muestra todo. Con $s(t)=A\cos\phi(t)$:

$$s^2(t) = A^2\cos^2\phi(t) = \frac{A^2}{2}\big[1+\cos(2\phi(t))\big]$$

El filtro pasabanda centrado en $2f_c$ elimina el término de continua y deja $\propto\cos(2\phi(t))$: **la fase se duplicó**, $\phi\to2\phi$. Para $\times n$ se usa una no linealidad de orden superior (o duplicadores en cascada) y se filtra el armónico $n$-ésimo, dando $\phi\to n\phi$.

### Por qué eso escala $f_c$ y $\Delta f$ pero no $f_m$

Sustituyendo la fase de FM con tono único, $\phi(t)=2\pi f_ct+\beta\sin(2\pi f_mt)$:

$$n\phi(t) = 2\pi (nf_c)\,t + n\beta\sin(2\pi f_mt)$$

Leyendo término a término está todo:

- $2\pi f_ct \to 2\pi(nf_c)t$ → **portadora $\times n$**
- $\beta \to n\beta$ → **índice $\times n$**, porque $\beta$ es un **coeficiente afuera** del seno
- $\sin(2\pi f_mt)$ → **intacto**, porque $f_m$ vive **adentro del argumento** del seno, y multiplicar la fase por $n$ no toca argumentos internos

Y de $\Delta f=\beta f_m$: como $\beta$ se multiplica por $n$ y $f_m$ queda igual, $\Delta f\to n\Delta f$. **Ese es el punto entero**: $\beta$ está afuera (escala), $f_m$ está adentro (no escala).

**Vía frecuencia instantánea (más directo aún)**: si $\phi\to n\phi$, entonces $f_i=\frac{1}{2\pi}\frac{d\phi}{dt}\to n\,f_i$, o sea la función completa se multiplica por $n$:

$$f_i(t) = f_c+\Delta f\cos(2\pi f_mt) \quad\longrightarrow\quad n f_i(t) = nf_c + n\Delta f\cos(2\pi f_mt)$$

El centro y la excursión se escalan por $n$, pero **la velocidad a la que oscila** (que es $f_m$) no cambia — solo se agrandó el vaivén, no se aceleró.

### La amplitud

En el $s^2(t)$ de arriba la amplitud sí cambia ($A\to A^2/2$). En la práctica el multiplicador va seguido de un **limitador/amplificador** que normaliza la amplitud, y por eso los enunciados aclaran "la amplitud de la señal permanece sin cambio". Como en FM la potencia es $P=A_c^2/2R$ independiente de la modulación, si la amplitud no cambia **la potencia tampoco** — pase lo que pase con $\beta$.

### No confundir con un mezclador (mixer)

Distinción que los finales testean, y es la razón de ser del [[../modulacion-analogica/modulador-armstrong|modulador Armstrong]]:

| Bloque | $f_c$ | $\Delta f$ | $\beta$ | $f_m$ |
|---|---|---|---|---|
| **Multiplicador $\times n$** | $nf_c$ | $n\Delta f$ | $n\beta$ | igual |
| **Mezclador con OL $f_{OL}$** | $f_c\pm f_{OL}$ | **igual** | **igual** | igual |

El mezclador multiplica por $\cos(2\pi f_{OL}t)$ y filtra una banda:

$$A\cos\phi(t)\cdot\cos(2\pi f_{OL}t) \to \tfrac{A}{2}\cos\big(2\pi(f_c\pm f_{OL})t+\beta\sin(2\pi f_mt)\big)$$

El término de modulación $\beta\sin(2\pi f_mt)$ **queda idéntico** — el mezclador *traslada* la portadora sin tocar la desviación. Por eso Armstrong usa **multiplicadores para subir $\beta$** (de NBFM a WBFM) y **mezcladores para ubicar la portadora final** en la frecuencia deseada sin arruinar el $\beta$ ya conseguido.

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
