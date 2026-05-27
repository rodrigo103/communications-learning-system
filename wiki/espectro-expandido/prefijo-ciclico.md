---
tags:
  - wiki/espectro-expandido
source_file: explicaciones_anki/unidad_10/carta_55_prefijo-ciclico.md
curso: Sistemas de Comunicaciones
unidad: 10
---

# Prefijo Ciclico (Cyclic Prefix)

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_10/carta_55_prefijo-ciclico]]]

El prefijo ciclico (CP) es la tecnica clave que permite a OFDM operar en canales con dispersion multitrayecto usando receptores simples. Sin CP, OFDM sufriria interferencia entre simbolos (ISI) e interferencia entre portadoras (ICI).

## Que es el prefijo ciclico

El CP consiste en copiar las **ultimas muestras** del simbolo OFDM y agregarlas al **inicio** del mismo simbolo:

```
|<-------- Simbolo OFDM util --------->|
                            |<-- CP -->|
|<-- CP -->|<-------- Simbolo OFDM --------->|
           |<------ Simbolo extendido ------>|
```

[source — [[../../explicaciones_anki/unidad_10/carta_55_prefijo-ciclico]]]

## Condicion de diseno

Para eliminar completamente la ISI, la duracion del CP debe exceder el maximo retardo del canal:

$$\boxed{T_{CP} > \tau_{\max}}$$

donde $\tau_{\max}$ es el maximo delay spread del canal multitrayecto.

## Eficiencia espectral del CP

El CP representa un overhead: tiempo que no transporta datos nuevos.

$$\boxed{\eta = \frac{T_s}{T_s + T_{CP}}}$$

donde $T_s$ es la duracion del simbolo OFDM util (sin CP).

## Overhead tipico

| Sistema | $T_{CP}$ | $T_s$ | Overhead |
|---|---|---|---|
| LTE (CP normal) | 4.7 $\mu$s | 66.7 $\mu$s | ~7% |
| LTE (CP extendido) | 16.7 $\mu$s | 66.7 $\mu$s | ~25% |
| 5G NR | Variable | Variable | 7-10% tipico |

## Como el CP elimina ISI e ICI

Con CP, la senal recibida en cada subportadora es:

$$\boxed{Y_{n,k} = H_k X_{n,k} + N_k}$$

Donde:
- $Y_{n,k}$: simbolo recibido en subportadora $k$, simbolo OFDM $n$
- $H_k$: respuesta del canal en la subportadora $k$ (un solo numero complejo)
- $X_{n,k}$: simbolo transmitido
- $N_k$: ruido

### Sin ISI

El CP absorbe los ecos del simbolo anterior. Como $T_{CP} > \tau_{\max}$, cuando comienza la parte util del simbolo, todos los ecos del simbolo previo ya terminaron.

### Sin ICI

El CP convierte la convolucion lineal del canal en **convolucion circular**. Esto preserva la ortogonalidad entre subportadoras. [analysis]

## Ecualizacion simplificada

Gracias al CP, cada subportadora experimenta **desvanecimiento plano** (flat fading). La ecualizacion se reduce a una division por escalar:

$$\hat{X}_{n,k} = \frac{Y_{n,k}}{H_k}$$

Esto contrasta fuertemente con sistemas sin CP, donde se necesitarian ecualizadores complejos (con muchos taps) para combatir la ISI. [analysis]

## Compromiso de diseno

| CP largo | CP corto |
|---|---|
| Mejor contra multitrayecto (mas delay spread) | Menor overhead → mas throughput |
| Menor eficiencia espectral | Mas vulnerable a ISI |
| Necesario en celdas grandes / entornos montanosos | Suficiente en celdas pequenas / interiores |

## Sin CP: que falla

Sin prefijo ciclico:
- Las copias retrasadas del simbolo $n$ se solapan con el simbolo $n+1$ → **ISI**
- La convolucion lineal del canal rompe la ortogonalidad entre subportadoras → **ICI**
- Se necesitarian ecualizadores complejos (con muchos coeficientes) o tecnicas de cancelacion de interferencia

[analysis]

## Ver también

- [[../espectro-expandido/ofdm]] — OFDM
- [[../espectro-expandido/dsss]] — DSSS (alternativa a OFDM)
- [[../herramientas-matematicas/teorema-convolucion]] — Teorema de convolucion
- [[../espectro-expandido/aplicaciones-spread-spectrum]] — Aplicaciones
