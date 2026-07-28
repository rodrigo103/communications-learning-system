---
tags:
  - wiki/conceptos-integradores
curso: Sistemas de Comunicaciones
unidad: 5-6
---

# PCM vs Modulacion Digital — como se conectan y en que se diferencian

> **Last verified:** 2026-07-28 | **Verified by:** [analysis]

PCM y Modulacion Digital son **etapas consecutivas** en un sistema de comunicaciones completo. No compiten: se complementan. PCM digitaliza la fuente; la modulacion digital transmite el resultado.

## Que hace cada una

### PCM (Unidad 5) — Digitalizar la fuente

Convierte una señal **analogica** en un tren de **bits** [analysis]:

| Etapa | Que hace | Resultado |
|-------|----------|-----------|
| Muestreo | Discretiza en tiempo ($f_s \geq 2B$) | $x(nT_s)$ |
| Cuantificacion | Discretiza en amplitud ($M=2^n$ niveles) | Error maximo $q/2$ |
| Codificacion | Asigna $n$ bits a cada nivel | $R_b = n \cdot f_s$ bps |

**No hay portadora.** Es procesamiento de fuente. Metrica clave: $SNR_Q$ (6 dB/bit).

### Modulacion Digital (Unidad 6) — Transmitir los bits

Toma un tren de **bits** y los convierte en una **forma de onda pasabanda** [analysis]:

| Etapa | Que hace | Resultado |
|-------|----------|-----------|
| Agrupar bits | $\ell = \log_2 M_{mod}$ bits → 1 simbolo | $D = R_b / \ell$ baudios |
| Mapear a constelacion | Simbolo → punto $(I_k, Q_k)$ | $s(t) = I\cos - Q\sin$ |
| Modular | Subir a $f_c$ | Señal pasabanda |
| Recibir con ruido | $Y = HX + N$ | BER segun $E_b/N_0$ |

**Si hay portadora.** Es transmision. Metrica clave: $BER$ vs $E_b/N_0$.

## La cadena completa (donde se tocan)

$$\boxed{f_s\ [\text{muestras/s}] \xrightarrow{\times n} R_b\ [\text{bps}] \xrightarrow{\div\ell} D\ [\text{baudios}] \xrightarrow{\text{Nyquist}} B\ [\text{Hz}]}$$

```
PCM produce los bits  ──>  Digital los transmite
```

El **punto de union es $R_b$**: PCM entrega bits por segundo; la modulacion digital agarra esos bits y los empaqueta en simbolos para el canal [analysis].

## $n$ y $\ell$ son independientes

Misma formula ($\log_2$ de un conteo), conceptos **distintos** [analysis]:

| | PCM | Digital |
|---|---|---|
| Simbolo | $n$ | $\ell$ |
| Que cuenta $M$ | **Niveles del ADC** | **Puntos de la constelacion** |
| Unidad | bits/**muestra** | bits/**simbolo** |
| Etapa | Digitalizacion (fuente) | Transmision (canal) |

$n$ y $\ell$ **no tienen por que coincidir**. Son numeros independientes. Un ADC de 8 bits puede alimentar un modulador QPSK ($\ell=2$) o uno 64-QAM ($\ell=6$). En la cadena, $n$ **multiplica** al entrar y $\ell$ **divide** al salir — actuan en etapas distintas y en direcciones opuestas [analysis]:

$$f_s \xrightarrow{\times n} R_b \xrightarrow{\div \ell} D$$

## Ejemplo base — cuando coinciden (casualidad comoda)

Señal de voz $B = 4$ kHz, $n = 3$ bits/muestra, $M = 8$ niveles, $f_s = 8$ kHz, $R_b = 24$ kbps [analysis].

| Codigo | Nivel | Fase 8-PSK |
|--------|-------|------------|
| `000` | $-4q$ | 0° |
| `001` | $-3q$ | 45° |
| `010` | $-2q$ | 90° |
| `011` | $-q$ | 135° |
| `100` | 0 | 180° |
| `101` | $+q$ | 225° |
| `110` | $+2q$ | 270° |
| `111` | $+3q$ | 315° |

Como $n = \ell = 3$, cada muestra PCM de 3 bits = exactamente un simbolo 8-PSK. El mapeo es 1:1. $D = 24\text{k} / 3 = 8$ kbaud, $B = D = 8$ kHz [analysis].

## Mismo PCM, distinta modulacion — el verdadero desacople

Mismo $n = 3$, $R_b = 24$ kbps. Cambiamos $\ell$ [analysis].

### $\ell = 2$ (QPSK)

Cada simbolo QPSK lleva 2 bits. Los bits fluyen como un rio: el modulador no sabe donde terminan las muestras PCM, solo corta en bloques de 2:

```
Muestra 1    Muestra 2    Muestra 3    Muestra 4
[1 0 1]      [0 1 1]      [0 0 1]      [1 1 0]
   │ │            │ │           │ │           │ │
   ▼ ▼            ▼ ▼           ▼ ▼           ▼ ▼
[1 0] [1 0] [1 1] [0 0] [1 1] [1 0] ...

Simbolo  Simbolo  Simbolo  Simbolo  Simbolo  Simbolo
```

- $D = 24\text{k} / 2 =$ **12 kbaud**
- Cada 2 muestras PCM producen 3 simbolos QPSK
- $B = 12$ kHz — **mas ancho de banda** que con 8-PSK, pero con mejor BER (QPSK vs 8-PSK)

### $\ell = 4$ (16-QAM)

Cada simbolo 16-QAM lleva 4 bits:

```
Muestra 1    Muestra 2    Muestra 3    Muestra 4
[1 0 1]      [0 1 1]      [0 0 1]      [1 1 0]
   │ │            │ │           │ │           │ │
   ▼ ▼            ▼ ▼           ▼ ▼           ▼ ▼
[1 0 1 0]    [1 1 0 0]    [1 1 1 0]    ...

 1 simbolo    1 simbolo    1 simbolo
  16-QAM       16-QAM       16-QAM
```

- $D = 24\text{k} / 4 =$ **6 kbaud**
- Cada 4 muestras PCM producen 3 simbolos 16-QAM
- $B = 6$ kHz — **menos ancho de banda** que con 8-PSK, pero peor BER (16-QAM vs 8-PSK)

### El patron

| $\ell$ | $D$ | $B$ | BER |
|--------|-----|-----|-----|
| 2 (QPSK) | 12 kbaud | 12 kHz | Mejor |
| 3 (8-PSK) | 8 kbaud | 8 kHz | Medio |
| 4 (16-QAM) | 6 kbaud | 6 kHz | Peor |

A mayor $\ell$, mas bits por simbolo → menos baudios → menor ancho de banda → pero los puntos de la constelacion quedan mas juntos y la BER empeora. Es el **trade-off ancho de banda vs robustez al ruido** [analysis].

## Comparacion resumen

| | PCM | Modulacion Digital |
|---|---|---|
| **Dominio** | Fuente (digitalizacion) | Canal (transmision) |
| **Entrada** | Señal analogica | Bits |
| **Salida** | Bits ($R_b$) | Señal pasabanda |
| **¿Portadora?** | No | Si ($f_c$) |
| **Operacion clave** | $\log_2 M$ → $n$ (niveles→bits) | $\log_2 M_{mod}$ → $\ell$ (bits→simbolo) |
| **Metrica de calidad** | $SNR_Q$ | BER / $E_b/N_0$ |
| **Ruido que enfrenta** | Cuantificacion ($q^2/12$) | Termico del canal ($N_0$) |
| **Factor de conversion** | $n$ bits/muestra | $\ell$ bits/simbolo |

## Intuicion clave

Los bits fluyen como un rio: PCM los vierte, la modulacion los toma en grupos de $\ell$. Si los grupos no calzan justo con las fronteras de las muestras PCM, no pasa nada — el modulador es ciego a eso. PCM te dice *cuantos bits* representa cada muestra; la modulacion digital te dice *como empaquetas* esos bits en formas de onda. Son dos "embalajes" superpuestos conectados por $R_b$ [analysis].

## Ver tambien

- [[../modulacion-pulsos/pcm-cuantificacion|PCM: Muestreo, Cuantificacion y Codificacion]]
- [[../modulacion-pulsos/pcm-formulario-examen|PCM — Formulario de examen]]
- [[../modulacion-digital/digital-formulario-examen|Modulacion Digital — Formulario de examen]]
- [[../modulacion-digital/constelaciones|Constelaciones]]
- [[../conceptos-integradores/eb-n0-vs-snr|$E_b/N_0$ vs SNR]]
