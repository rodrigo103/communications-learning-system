---
tags:
  - wiki/teoria-informacion
source_file: explicaciones_anki/unidad_09/carta_48_codigos_detectores_correctores.md
curso: Sistemas de Comunicaciones
unidad: 9
---

# Codigos Detectores y Correctores de Errores

> **Last verified:** 2025-11-16 | **Verified by:** source

## Concepto

Los **codigos de canal** agregan redundancia controlada para detectar o corregir errores introducidos durante la transmision. Son la razon por la cual las comunicaciones digitales modernas funcionan de manera confiable en canales ruidosos. [source — [[../../explicaciones_anki/unidad_09/carta_48_codigos_detectores_correctores]]]

## Clasificacion

### Codigos Detectores
- Detectan la presencia de errores pero no pueden corregirlos
- Requieren retransmision (ARQ — Automatic Repeat reQuest)
- Ejemplo basico: **bit de paridad**

### Codigos Correctores (FEC — Forward Error Correction)
- Detectan **y corrigen** errores sin necesidad de retransmision
- Requieren mayor redundancia que los detectores
- Fundamentales en comunicaciones donde la retransmision es costosa o imposible (satelites, espacio profundo, broadcast) [analysis]

### Por estructura

- **Codigos de bloque**: procesan bloques fijos de $k$ bits de datos $\to$ $n$ bits codificados ($n > k$)
  - Ejemplos: Hamming, Reed-Solomon, BCH, LDPC
- **Codigos convolucionales**: procesan flujo continuo con memoria
  - Decodificacion Viterbi, usados en telefonia movil

## Distancia de Hamming

La **distancia de Hamming** $d_{min}$ entre palabras codigo determina la capacidad del codigo: [source — [[../../explicaciones_anki/unidad_09/carta_48_codigos_detectores_correctores]]]

$$\boxed{e_d = d_{min} - 1}$$

Capacidad de deteccion: hasta $e_d$ errores.

$$\boxed{e_c = \left\lfloor \frac{d_{min} - 1}{2} \right\rfloor}$$

Capacidad de correccion: hasta $e_c$ errores.

### Intuicion

Con $d_{min} = 3$: cualquier error de 1 bit deja la palabra recibida mas cerca de la original que de cualquier otra palabra codigo. Con 2 errores: se puede detectar pero no corregir.

## Codigos Principales

### Codigo de Hamming (7,4)
- 4 bits de datos, 3 bits de paridad
- $d_{min} = 3 \Rightarrow$ corrige 1 error, detecta 2
- La **matriz de paridad** $H$ genera el sindrome $s = H \cdot r^T$
- Si $s = 0$: no hay error. Si $s \neq 0$: el sindrome indica la posicion del error [analysis]

### Reed-Solomon
- Opera sobre simbolos (no bits individuales) en campos finitos (Galois)
- Extremadamente usado: CD, DVD, Blu-ray, codigos QR, comunicaciones espaciales
- Puede corregir rafagas de errores (ej.: rayones en CD)
- RS(255, 223): 223 simbolos de datos, 32 de paridad, corrige hasta 16 simbolos erroneos [source — [[../../explicaciones_anki/unidad_09/carta_48_codigos_detectores_correctores]]]

### Turbo Codes y LDPC
- **Turbo codes** (1993): revolucionarios, se acercan a $\sim 0.5$ dB del limite de Shannon
- **LDPC** (Low-Density Parity Check): adoptados en 5G para eMBB, altamente paralelizables
- **Polar codes**: probadamente optimos, usados en canales de control 5G [source — [[../../explicaciones_anki/unidad_09/carta_48_codigos_detectores_correctores]]]

## Formulas Fundamentales

| Formula | Significado |
|---------|-------------|
| $e_d = d_{min} - 1$ | Maximos errores detectables |
| $e_c = \lfloor(d_{min} - 1)/2\rfloor$ | Maximos errores corregibles |
| $R = k/n$ | Tasa del codigo |
| $d_{min} \leq n - k + 1$ | Limite de Singleton |

## Aplicaciones

| Sistema | Codigo | Funcion |
|---------|--------|---------|
| WiFi 802.11 | Convolucional + LDPC | BER $10^{-5} \to 10^{-10}$ |
| 4G LTE | Turbo codes | Cerca de Shannon |
| DVD/Blu-ray | Reed-Solomon | Correccion de rafagas |
| QR Code | RS + estructura | Recuperacion con hasta 30% de dano |
| 5G NR | LDPC (datos), Polar (control) | Maximo rendimiento |

## Errores Comunes

- Confundir tasa del codigo ($R = k/n$) con eficiencia: un codigo con $R = 0.5$ puede ser eficiente si permite usar modulacion de orden superior
- Pensar que mas redundancia siempre es mejor: existe un optimo segun el canal
- Ignorar latencia: codigos convolucionales con memoria introducen retardo

## Ver tambien

- [[../teoria-informacion/codigo-compacto]]
- [[../teoria-informacion/entropia-fuente]]
- [[../modulacion-digital/probabilidad-error]]
- [[../teoria-informacion/teorema-shannon-hartley]]
- [[../teoria-informacion/capacidad-canal-shannon]]
