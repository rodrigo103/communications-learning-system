---
tags:
  - wiki/teoria-informacion
source_file: explicaciones_anki/unidad_09/carta_44_entropia-fuente.md
curso: Sistemas de Comunicaciones
unidad: 9
---

# Entropia de una Fuente de Informacion

> **Last verified:** 2025-11-16 | **Verified by:** source

## Definicion

La **entropia** $H(X)$ mide la informacion promedio (incertidumbre) de una fuente discreta, introducida por Claude Shannon en 1948. Constituye el concepto fundamental de la teoria de la informacion y establece limites precisos de compresion y eficiencia de transmision.

$$\boxed{H(X) = -\sum_{i=1}^{n} p_i \log_2(p_i) \quad \text{[bits/simbolo]}}$$

donde $p_i$ es la probabilidad del simbolo $i$. [source]

### Informacion de un evento unico

La informacion contenida en un evento con probabilidad $p$ es:

$$I(p) = \log_2\left(\frac{1}{p}\right) = -\log_2(p) \quad \text{[bits]}$$

Propiedades fundamentales: [analysis]
- Eventos mas improbables contienen mas informacion al ocurrir
- Eventos seguros ($p=1$) no aportan informacion ($I = 0$)
- La informacion es aditiva para eventos independientes

### Axiomas de Shannon

Shannon demostro que una medida $H$ de entropia que satisfaga: [source]
1. Continuidad en las probabilidades
2. Monotonicidad creciente con $n$ para eventos equiprobables
3. Consistencia bajo particionamiento

tiene la forma unica $H = -K \sum p_i \log p_i$. Eligiendo $K = 1/\ln(2)$ se obtienen bits.

## Propiedades

- **Acotacion**: $\boxed{0 \leq H \leq \log_2(n)}$ [source]
- **Entropia maxima**: $H_{max} = \log_2(n)$ cuando todos los simbolos son equiprobables ($p_i = 1/n$)
- **Entropia minima**: $H = 0$ cuando un simbolo tiene $p = 1$
- Para $p_i = 0$, se define $0 \log_2(0) = 0$ (consistente con $\lim_{p \to 0} p \log p = 0$)

### Entropia Binaria

Para fuente binaria con $p(1) = p$, $p(0) = 1-p$:

$$H(p) = -p\log_2(p) - (1-p)\log_2(1-p)$$

- $p = 0.5 \Rightarrow H = 1$ bit (maxima)
- $p = 0.9 \Rightarrow H \approx 0.469$ bits
- $p = 1.0 \Rightarrow H = 0$ (determinista)

## Fuentes con y sin Memoria

**Fuente sin memoria**: $H = -\sum_i p_i \log_2 p_i$ — los simbolos son independientes. [source]

**Fuentes con memoria (Markovianas)**: la probabilidad depende del contexto anterior:

$$H = -\sum_{i,j} p(i)p(j|i) \log_2 p(j|i)$$

Las dependencias reducen la incertidumbre y por tanto la entropia. [analysis]
Ejemplo: en ingles, despues de "Q" casi siempre viene "U", reduciendo $H$ de $\sim 4.7$ a $\sim 3.5$ bits/letra.

## Redundancia

La **redundancia** mide cuanto "sobra" respecto al minimo teorico:

$$\boxed{R = 1 - \frac{H}{H_{max}} = 1 - \frac{H}{\log_2(n)}}$$

- $R = 0$: fuente optima (equiprobable, sin memoria)
- $R > 0$: informacion predecible/repetitiva
- Lenguajes naturales tipicamente tienen $\sim 50\%$ de redundancia [analysis]

La **compresion sin perdida** puede reducir la representacion hasta $H$ bits/simbolo. El limite de compresion es: $L_{min} = H$.

## Aplicaciones y Conexiones

- **Compresion de datos**: ZIP, MP3, H.264 explotan baja entropia [analysis]
- **Comunicaciones digitales**: diseno de codigos fuente eficientes
- **Criptografia**: la entropia mide aleatoriedad y seguridad de claves
- **Machine Learning**: arboles de decision, entropia cruzada como funcion de costo

## Errores Comunes

- Confundir entropia de informacion con entropia termodinamica: conceptos relacionados pero distintos
- Olvidar el signo negativo: los $p_i \log_2(p_i)$ son negativos, pero $H$ es siempre no-negativa
- Usar logaritmo natural en vez de base 2: base 2 $\to$ bits, base $e \to$ nats

## Ver tambien

- [[teoria-informacion/capacidad-canal-shannon]]
- [[teoria-informacion/teorema-shannon-hartley]]
- [[teoria-informacion/codigo-compacto]]
- [[teoria-informacion/codigos-deteccion-error]]
- [[teoria-informacion/sistema-ideal-comunicaciones]]
