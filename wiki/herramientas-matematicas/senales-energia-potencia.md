---
tags:
  - wiki/herramientas-matematicas
source_file: explicaciones_anki/unidad_02/carta_09_energia_vs_potencia.md
curso: Sistemas de Comunicaciones
unidad: 2
---

# Señales de Energia vs Señales de Potencia

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_02/carta_09_energia_vs_potencia]]]

## Origen fisico de $E=\int|x(t)|^2dt$: ¿definicion o se puede deducir?

Dentro de la teoria de señales, $E\triangleq\int|x(t)|^2dt$ **es la definicion** (norma al cuadrado en $L^2$) — no hay algo mas primitivo del cual deducirla dentro de ese marco. Pero la forma especifica de la formula no es arbitraria: se puede **derivar/motivar** partiendo de electricidad basica (Ohm + Joule) mas una convencion de normalizacion. [analysis]

1. *Ley de Ohm*: para $v(t)$ sobre una resistencia $R$, $i(t)=v(t)/R$.
2. *Potencia instantanea disipada (Joule)*: $p(t)=v(t)i(t)=v^2(t)/R$ [W].
3. *Energia = integral de potencia en el tiempo* (definicion fisica basica, $P=dE/dt \Rightarrow E=\int P\,dt$): $E=\int_{-\infty}^{\infty} v^2(t)/R\,dt$.
4. *Normalizacion $R=1\Omega$*: para que la "energia de la señal" no dependa de una resistencia externa arbitraria (la misma convencion de "$Z=1\Omega$ si no dan dato" que aparece en los ejercicios de potencia de AM), se toma $R=1$: $E=\int v^2(t)\,dt \to E=\int x^2(t)\,dt$.
5. *Generalizacion a señales complejas*: se reemplaza $x^2(t)$ por $x(t)x^*(t)=|x(t)|^2$ (coincide con $x^2(t)$ si $x(t)$ es real, y garantiza un resultado real y no-negativo si $x(t)$ es complejo, ej. representacion analitica via Hilbert): $E=\int_{-\infty}^{\infty}|x(t)|^2\,dt$.

Esta es la expresion que usa el Teorema de Parseval como punto de partida — ver [[../herramientas-matematicas/teorema-parseval]].

## Clasificacion Fundamental

Toda señal se clasifica en una de dos categorias mutuamente excluyentes [source — [[../../explicaciones_anki/unidad_02/carta_09_energia_vs_potencia]]]:

### Señales de Energia

- Duracion finita o decaimiento asintotico
- **Energia finita**: $E = \int_{-\infty}^{\infty} |x(t)|^2 dt < \infty$
- **Potencia promedio**: $P = 0$

**Ejemplos**: pulsos unicos, rafagas, transitorios, bits en comunicacion digital.

### Señales de Potencia

- Duracion infinita o periodicas
- **Potencia promedio finita**: $P = \lim_{T\to\infty} \frac{1}{T}\int_{-T/2}^{T/2} |x(t)|^2 dt < \infty$
- **Energia infinita**

**Ejemplos**: sinusoides, portadoras RF, señales aleatorias estacionarias, ruido.

## Expresiones Matematicas

Para una señal $x(t)$ [source — [[../../explicaciones_anki/unidad_02/carta_09_energia_vs_potencia]]]:

$$\boxed{E_x = \int_{-\infty}^{\infty} |x(t)|^2 dt}$$

$$\boxed{P_x = \lim_{T \to \infty} \frac{1}{T} \int_{-T/2}^{T/2} |x(t)|^2 dt}$$

Para señales **periodicas** de periodo $T_0$:

$$P_x = \frac{1}{T_0} \int_{0}^{T_0} |x(t)|^2 dt$$

## Ejemplo: Pulso vs Sinusoide

**Pulso rectangular** de amplitud $A$ y duracion $T$:

$$E_x = A^2 T < \infty \quad \Rightarrow \quad \text{Señal de energia}$$

**Sinusoide** $x(t) = A\cos(2\pi f_0 t)$:

$$E_x = \infty, \quad P_x = \frac{A^2}{2} < \infty \quad \Rightarrow \quad \text{Señal de potencia}$$

## Ejemplo: Ruido Termico

El ruido termico es siempre una **señal de potencia** [source — [[../../explicaciones_anki/unidad_02/carta_09_energia_vs_potencia]]]:

- DEP: $N_0 = kT$ [W/Hz]
- Potencia en banda $B$: $P_n = N_0 B = kTB$ (finita)
- Energia en tiempo $T$: $E_n = kTB \cdot T \to \infty$ cuando $T \to \infty$

## Analogia

Una linterna con flash (señal de energia) libera energia finita en tiempo corto: potencia instantanea alta, pero potencia promedio $\approx 0$. Una lampara encendida permanentemente (señal de potencia) consume potencia constante; la energia crece sin limite [analysis].

## Implicaciones en Comunicaciones

| Tipo | Usa | Herramienta |
|------|-----|-------------|
| Energia | $X(f)$ (TF) | Teorema de Parseval |
| Potencia | $S_x(f)$ (DEP) | Wiener-Khinchin |

- Las señales de potencia **no tienen transformada de Fourier tradicional**
- Para ellas se usa la [[../herramientas-matematicas/densidad-espectral-potencia]]
- El ruido es siempre señal de potencia → se analiza con DEP

## Puntos Clave

- ✓ Clasificacion **mutuamente excluyente**: una señal es de energia O de potencia [source — [[../../explicaciones_anki/unidad_02/carta_09_energia_vs_potencia]]]
- ✓ Señales periodicas (no nulas) son siempre de potencia [source — [[../../explicaciones_anki/unidad_02/carta_09_energia_vs_potencia]]]
- ✓ Señales de duracion finita son siempre de energia [source — [[../../explicaciones_anki/unidad_02/carta_09_energia_vs_potencia]]]
- ✓ El ruido siempre es señal de potencia [source — [[../../explicaciones_anki/unidad_02/carta_09_energia_vs_potencia]]]

## Ver tambien

- [[../herramientas-matematicas/densidad-espectral-potencia]]
- [[../herramientas-matematicas/teorema-parseval]]
- [[../ruido/ruido-blanco-banda-angosta]]
- [[../../claude-conversations/2025-11-04_signal-power-calculations-and-mean-value-expressions|Conversación: potencia de señal y Parseval]]
