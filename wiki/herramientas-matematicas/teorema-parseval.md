---
tags:
  - wiki/herramientas-matematicas
source_file: explicaciones_anki/unidad_02/carta_04_teorema-parseval.md
curso: Sistemas de Comunicaciones
unidad: 2
---

# Teorema de Parseval

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_02/carta_04_teorema-parseval]]]

## Enunciado

El Teorema de Parseval establece la conservacion de energia entre los dominios del tiempo y la frecuencia [source — [[../../explicaciones_anki/unidad_02/carta_04_teorema-parseval]]]:

$$\boxed{\int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df}$$

## Interpretacion Fisica

La energia total de una señal en el dominio del tiempo es **exactamente igual** a la energia total en el dominio de la frecuencia [source — [[../../explicaciones_anki/unidad_02/carta_04_teorema-parseval]]]. Esto demuestra que la Transformada de Fourier conserva la energia y permite calcular la energia integrando la densidad espectral de energia $|X(f)|^2$.

## Significado de los Terminos

- $|x(t)|^2$: potencia instantanea en el instante $t$ [W]
- $|X(f)|^2$: densidad espectral de energia en la frecuencia $f$ [J/Hz]
- Las integrales suman estas densidades para obtener la energia total

## Derivacion

Partiendo de la energia en tiempo:

$$E = \int_{-\infty}^{\infty} x(t) \cdot x^*(t) dt$$

Usando la transformada inversa y el teorema de Fubini para intercambiar integracion:

$$E = \int_{-\infty}^{\infty} X^*(f) \cdot X(f) df = \int_{-\infty}^{\infty} |X(f)|^2 df$$

## Analogia

Imagina el teorema como un **principio de conservacion financiera**: si tienes $1000 en billetes, no importa si los cuentas como billetes individuales (dominio temporal) o agrupados por denominacion (dominio frecuencial) — el total es el mismo [analysis].

La transformada de Fourier actua como un **prisma optico** que descompone luz blanca en sus colores. El teorema asegura que la energia total de la luz es igual a la suma de energias de todos los colores [analysis].

## Ejemplo: Pulso Rectangular

Para un pulso de amplitud $A=5$V y duracion $T=2$ms:

**En tiempo:**
$$E_{tiempo} = \int_{-T/2}^{T/2} A^2 dt = A^2 T = 25 \cdot 0.002 = 0.05 \text{ J}$$

**En frecuencia:** $X(f) = AT \cdot \text{sinc}(fT)$

$$E_{frecuencia} = \int_{-\infty}^{\infty} |AT \cdot \text{sinc}(fT)|^2 df = A^2T = 0.05 \text{ J}$$

Ambos calculos coinciden exactamente, confirmando el teorema.

## Aplicaciones en Comunicaciones

- **Diseño de filtros**: calcular energia perdida/transmitida en una banda
- **Analisis de modulacion**: distribucion de energia en bandas laterales
- **Compresion de señales**: concentrar energia en pocas frecuencias

## Puntos Clave

- ✓ La energia es invariante bajo la Transformada de Fourier [source — [[../../explicaciones_anki/unidad_02/carta_04_teorema-parseval]]]
- ✓ Se puede calcular energia en el dominio mas conveniente [analysis]
- ✓ $|X(f)|^2$ tiene significado fisico real como densidad espectral de energia
- ✓ Para señales periodicas: $\frac{1}{T}\int |x(t)|^2 dt = \sum |X_n|^2$

## Ver tambien

- [[../herramientas-matematicas/densidad-espectral-potencia]]
- [[../herramientas-matematicas/teorema-convolucion]]
- [[../herramientas-matematicas/senales-energia-potencia]]
- [[../derivaciones/teorema-parseval]]
- [[../../claude-conversations/2025-11-04_signal-power-calculations-and-mean-value-expressions|Conversación: potencia de señal y Parseval]]
