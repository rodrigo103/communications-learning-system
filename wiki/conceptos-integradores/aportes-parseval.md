---
tags:
  - wiki/conceptos-integradores
curso: Sistemas de Comunicaciones
unidad: 2
---

# Marc-Antoine Parseval y sus Aportes a los Sistemas de Comunicaciones

> **Last verified:** 2026-06-10 | **Verified by:** analysis

Marc-Antoine Parseval des Chenes (1755–1836) fue un matematico frances cuyo teorema de conservacion de energia entre el dominio del tiempo y de la frecuencia es una de las herramientas fundamentales del analisis de señales en comunicaciones.

## Teorema de Parseval

El teorema establece que la energia total de una señal se conserva al pasar del dominio del tiempo al dominio de la frecuencia:

$$\boxed{\int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df}$$

### ¿Por que es fundamental en comunicaciones?

Parseval permite: [analysis]

1. **Calcular potencia sin integrar en el tiempo**: si se conoce el espectro $X(f)$, la energia/potencia se obtiene directamente del area bajo $|X(f)|^2$.

2. **Relacionar SNR con espectro**: 
   $$\text{SNR} = \frac{\int_B S_x(f) df}{\int_B S_n(f) df}$$
   En lugar de integrar señales en el tiempo, se integran densidades espectrales en frecuencia. [analysis]

3. **Demostrar la eficiencia de modulaciones**: Parseval permite comparar cuanta potencia se gasta en la portadora vs en las bandas laterales. Por ejemplo, en AM convencional, solo el 33% de la potencia maxima esta en las bandas laterales (el resto en la portadora). [analysis]

4. **Fundamento de Wiener-Khinchin**: el teorema de Parseval es el puente matematico que conecta la funcion de autocorrelacion con la densidad espectral de potencia.

### Relacion con la Serie de Fourier

Para señales periodicas, el teorema toma la forma:

$$\boxed{P_{avg} = \frac{1}{T_0} \int_{T_0} |x(t)|^2 dt = \sum_{n=-\infty}^{\infty} |c_n|^2}$$

Donde $c_n$ son los coeficientes de la serie de Fourier. La potencia promedio es simplemente la suma de las potencias de cada componente frecuencial. [analysis]

### Generalizacion: Teorema de Parseval Generalizado

Para dos señales $x(t)$ e $y(t)$:

$$\boxed{\int_{-\infty}^{\infty} x(t) y^*(t) dt = \int_{-\infty}^{\infty} X(f) Y^*(f) df}$$

Esta forma es util para calcular correlaciones cruzadas y verificar ortogonalidad entre señales (clave en CDMA y OFDM). [analysis]

## De Parseval al Diseño de Sistemas

Sin el teorema de Parseval, no podriamos: [analysis]
- Calcular la potencia de ruido en un ancho de banda $B$
- Evaluar la eficiencia energetica de modulaciones
- Diseñar filtros que maximicen SNR
- Verificar que la energia se conserva en conversiones ADC/DAC

→ [[../herramientas-matematicas/teorema-parseval|Teorema de Parseval]]
→ [[../herramientas-matematicas/densidad-espectral-potencia|Densidad Espectral de Potencia]]
→ [[../herramientas-matematicas/senales-energia-potencia|Señales de Energia vs Potencia]]

## Ver Tambien

- [[../herramientas-matematicas/teorema-parseval|Teorema de Parseval]]
- [[../herramientas-matematicas/densidad-espectral-potencia|Densidad Espectral de Potencia]]
- [[../herramientas-matematicas/senales-energia-potencia|Señales de Energia vs Potencia]]
- [[../herramientas-matematicas/teorema-convolucion|Teorema de Convolucion]]
- [[../conceptos-integradores/aportes-fourier|Aportes de Fourier]]
- [[../conceptos-integradores/aportes-shannon|Aportes de Shannon]]
