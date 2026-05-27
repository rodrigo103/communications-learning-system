---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_07/carta_34_temperatura-ruido.md
curso: Sistemas de Comunicaciones
unidad: 7
---

# Temperatura de Ruido

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_07/carta_34_temperatura-ruido]]]

La temperatura de ruido es una forma alternativa de expresar el factor de ruido, muy usada en sistemas de microondas, satelites y radioastronomia. En lugar de manejar factores adimensionales, se trabaja con temperaturas equivalentes en Kelvin.

## Potencia de ruido desde temperatura equivalente

La potencia de ruido generada por un dispositivo a temperatura equivalente $T_e$ es:

$$N = k T_e B$$

donde $k = 1.38 \times 10^{-23} \text{ J/K}$ es la constante de Boltzmann y $B$ el ancho de banda.

## Ruido termico (Johnson-Nyquist)

El ruido termico generado por una resistencia a temperatura $T$ tiene una tension cuadratica media:

$$v_n^2 = 4 k T R B$$

y una potencia de ruido disponible:

$$\boxed{N_{\text{termico}} = k T B}$$

Este es el ruido minimo presente en cualquier sistema a temperatura $T > 0$.

## Conversion entre factor de ruido y temperatura

La relacion fundamental entre temperatura equivalente de ruido y factor de ruido:

$$\boxed{T_e = T_0 (F - 1)}$$

donde $T_0 = 290\text{ K}$ es la temperatura de referencia estandar IEEE. En forma inversa:

$$F = 1 + \frac{T_e}{T_0}$$

[source — [[../../explicaciones_anki/unidad_07/carta_34_temperatura-ruido]]]

## Temperatura del sistema

La temperatura total del sistema suma las contribuciones de antena y receptor:

$$\boxed{T_{sys} = T_{\text{antena}} + T_{\text{receptor}}}$$

La temperatura de antena $T_{\text{antena}}$ depende de hacia donde apunta (cielo frio ~30 K vs tierra ~290 K). La temperatura es aditiva: esto facilita sumar contribuciones de distintas fuentes de ruido.

## Formula de Friis en temperatura

La formula de Friis expresada en temperaturas equivalentes:

$$\boxed{T_{e,\text{total}} = T_{e,1} + \frac{T_{e,2}}{G_1} + \frac{T_{e,3}}{G_1 G_2} + \cdots}$$

Esto muestra explicitamente que el ruido de las etapas posteriores se divide entre las ganancias de las etapas anteriores. [source — [[../../explicaciones_anki/unidad_07/carta_34_temperatura-ruido]]]

## El LNA domina la temperatura del sistema

El amplificador de bajo ruido (LNA) es la primera etapa activa y su ruido **no** es dividido por ninguna ganancia previa. Por eso el ruido del LNA es critico y determina la temperatura total del sistema. [analysis]

## Valores practicos tipicos

| Componente | $T_e$ tipica |
|---|---|
| LNA bueno | 50–100 K |
| LNA promedio | 200–500 K |
| LNA criogenico | ~20 K |
| Antena (apuntando al cielo) | 30–50 K |
| Antena (apuntando al horizonte) | 100–150 K |
| Mezclador | 500–2000 K |

## Ejemplo de calculo

Receptor con:
- LNA: $T_{e,1} = 50\text{ K}$, $G_1 = 20\text{ dB} = 100$
- Mezclador: $T_{e,2} = 500\text{ K}$

$$T_{e,\text{total}} = 50 + \frac{500}{100} = 50 + 5 = 55\text{ K}$$

La contribucion del mezclador es de solo 5 K gracias a la ganancia del LNA. Sin LNA, el mezclador aportaria 500 K. [analysis]

## Aplicaciones

- **Receptores satelitales:** LNA criogenicos ($T_e \sim 20\text{ K}$) para recibir senales debiles
- **Radioastronomia:** se requieren temperaturas de ruido extremadamente bajas
- **Comunicaciones de espacio profundo:** cada fraccion de dB cuenta

## Ver también

- [[../ruido/formula-friis]] — Formula de Friis
- [[../ruido/factor-ruido-temperatura]] — Factor de ruido F y NF
- [[../ruido/fuentes-ruido]] — Fuentes de ruido
- [[../ruido/ruido-termico]] — Ruido termico
- [[../ruido/relacion-snr]] — Relacion Senal a Ruido
- [[../ruido/lna-diseno-receptor]] — Diseno de receptor con LNA
