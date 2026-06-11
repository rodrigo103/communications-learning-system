---
tags:
  - wiki/conceptos-integradores
curso: Sistemas de Comunicaciones
unidad: 1-9
---

# Claude Shannon y sus Aportes a los Sistemas de Comunicaciones

> **Last verified:** 2026-06-10 | **Verified by:** analysis

## Biografia Breve

Claude Elwood Shannon (1916–2001) fue un matematico e ingeniero estadounidense que trabajo en los Laboratorios Bell. En 1948 publico "**A Mathematical Theory of Communication**", el trabajo que fundo la teoria de la informacion y revoluciono las telecomunicaciones. Antes de Shannon, las comunicaciones eran un arte empirico; despues de Shannon, se convirtieron en una ingenieria con fundamentos matematicos rigurosos.

> *"The fundamental problem of communication is that of reproducing at one point either exactly or approximately a message selected at another point."*
> — Claude Shannon, 1948

## Mapa de Aportes por Unidad del Curso

Cada uno de los aportes de Shannon que se estudian en esta materia esta vinculado a su pagina wiki correspondiente.

### Unidad 1 — Modelo del Sistema de Comunicaciones

Shannon formalizo el diagrama de bloques universal de todo sistema de comunicacion:

```
[Fuente] → [Transmisor] → [Canal] → [Receptor] → [Destino]
                              ↑
                           [Ruido]
```

La inclusion del **ruido** como componente inherente al modelo fue una de sus ideas mas revolucionarias: el ruido no es un accidente, es parte del sistema.

→ [[../introduccion/modelo-shannon|Modelo de Shannon: Componentes del Sistema]]

### Unidad 2 — Herramientas Matematicas: Teorema de Muestreo

El **Teorema de Nyquist-Shannon** establece que una señal limitada en banda $B$ puede reconstruirse perfectamente a partir de sus muestras si la frecuencia de muestreo cumple:

$$\boxed{f_s \geq 2B}$$

Este teorema es la base del procesamiento digital de señales, conversores ADC/DAC y sistemas PCM.

→ [[../herramientas-matematicas/teorema-muestreo|Teorema del Muestreo de Nyquist-Shannon]]

### Unidad 7 — Ruido: Modelo AWGN

Shannon adopto el **ruido blanco gaussiano aditivo (AWGN)** como modelo matematico del ruido en su teoria de 1948. Esta abstraccion —aunque simplificada— permitio derivar resultados exactos sobre limites de capacidad que siguen siendo validos para canales reales. [analysis]

→ [[../ruido/fuentes-ruido|Fuentes de Ruido]]

### Unidad 9 — Teoria de la Informacion

Es la unidad donde convergen la mayoria de los aportes de Shannon:

#### Entropia

Shannon definio la **entropia** $H$ como medida de la informacion promedio de una fuente:

$$\boxed{H(X) = -\sum_i p(x_i) \log_2 p(x_i)}$$

Esta formula separa el contenido informativo del significado semantico, y establece el limite de compresion sin perdida: no se puede comprimir por debajo de $H$ bits/simbolo.

→ [[../teoria-informacion/entropia|Entropia de Fuente]]

#### Capacidad del Canal y Teorema de Shannon-Hartley

El resultado mas celebre de Shannon: la maxima tasa de transmision libre de errores en un canal AWGN es:

$$\boxed{C = B \log_2\left(1 + \frac{S}{N}\right)}$$

→ [[../teoria-informacion/teorema-shannon-hartley|Teorema de Shannon-Hartley]]
→ [[../teoria-informacion/capacidad-canal-shannon|Capacidad del Canal de Shannon]]

#### Teorema de Codificacion de Fuente

Shannon demostro que existe un codigo sin perdida con longitud promedio $\bar{L}$ tal que:

$$\boxed{H \leq \bar{L} < H + 1}$$

Este limite es la base de todos los algoritmos de compresion modernos. [analysis]

→ [[../teoria-informacion/redundancia-compresion|Redundancia y Compresion]]
→ [[../teoria-informacion/codigo-compacto|Codigos Compactos (Shannon-Fano, Huffman)]]

#### Teorema de Codificacion de Canal

Antes de Shannon, se creia que la unica forma de reducir errores era aumentar la potencia o bajar la velocidad. Shannon demostro que:

- Si $R < C$: existe un codigo que transmite con probabilidad de error **arbitrariamente pequena**.
- Si $R > C$: la comunicacion confiable es **imposible**.

Este resultado guio decadas de investigacion en codigos correctores de errores (Hamming, convolucionales, Turbo, LDPC, Polar). [analysis]

→ [[../teoria-informacion/codigos-deteccion-error|Codigos Detectores y Correctores de Errores]]
→ [[../teoria-informacion/sistema-ideal-comunicaciones|Sistema Ideal de Comunicaciones]]

### Conceptos Integradores

#### Trade-off Ancho de Banda vs Potencia

Del teorema de Shannon-Hartley se deriva que $B$ y $S/N$ son **intercambiables**, pero con rendimientos diferentes segun el regimen de operacion. [analysis]

→ [[../conceptos-integradores/compromisos-diseno|Compromisos Fundamentales de Diseno]]

#### Limite Absoluto en $E_b/N_0$

Haciendo $B \to \infty$ en la formula de capacidad se obtiene el limite fundamental:

$$\boxed{\frac{E_b}{N_0} > \ln 2 \approx -1.59 \text{ dB}}$$

Ningun sistema de comunicacion puede operar por debajo de este valor. [analysis]

→ [[../conceptos-integradores/eb-n0-vs-snr|$E_b/N_0$ vs SNR y Limite de Shannon]]

#### Acercamiento al Limite en Sistemas Reales

Los sistemas practicos modernos (Turbo codes, LDPC) operan a tan solo 1–3 dB del limite de Shannon. [analysis]

→ [[../conceptos-integradores/evolucion-sistemas|Evolucion de los Sistemas de Comunicaciones]]

## Derivacion Matematica Completa

La derivacion paso a paso del teorema de Shannon-Hartley desde primeros principios:

→ [[../derivaciones/teorema-shannon-hartley|Derivacion del Teorema de Shannon-Hartley]]

## El Legado de Shannon

Los aportes de Shannon no solo dieron fundamento matematico a las comunicaciones, sino que **predijeron la transicion inevitable de analogico a digital**. Su trabajo de 1948 establecio que:

1. La informacion se puede **medir** (entropia).
2. Existen **limites fundamentales** que ninguna tecnologia puede superar.
3. La comunicacion **libre de errores** es posible por debajo de la capacidad del canal.

Hoy, cada sistema de comunicacion —desde 5G hasta WiFi 7, desde fibra optica hasta comunicaciones satelitales— se disena teniendo como referencia los limites establecidos por Shannon en 1948. [analysis]

## Ver Tambien

- [[../introduccion/modelo-shannon|Modelo de Shannon]]
- [[../herramientas-matematicas/teorema-muestreo|Teorema de Muestreo Nyquist-Shannon]]
- [[../teoria-informacion/entropia|Entropia de Fuente]]
- [[../teoria-informacion/teorema-shannon-hartley|Teorema de Shannon-Hartley]]
- [[../teoria-informacion/capacidad-canal-shannon|Capacidad del Canal de Shannon]]
- [[../teoria-informacion/redundancia-compresion|Redundancia y Compresion]]
- [[../teoria-informacion/codigo-compacto|Codigos Compactos]]
- [[../teoria-informacion/codigos-deteccion-error|Codigos Detectores/Correctores]]
- [[../teoria-informacion/sistema-ideal-comunicaciones|Sistema Ideal de Comunicaciones]]
- [[../conceptos-integradores/compromisos-diseno|Compromisos de Diseno]]
- [[../conceptos-integradores/eb-n0-vs-snr|$E_b/N_0$ vs SNR]]
- [[../conceptos-integradores/evolucion-sistemas|Evolucion de Sistemas]]
- [[../derivaciones/teorema-shannon-hartley|Derivacion Shannon-Hartley]]
- [[../resumenes/overview-curso|Resumen General del Curso]]
