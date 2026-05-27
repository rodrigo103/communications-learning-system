---
tags:
  - wiki/teoria-informacion
source_file: explicaciones_anki/unidad_09/carta_49_analogico_vs_digital_teoria_informacion.md
curso: Sistemas de Comunicaciones
unidad: 9
---

# Sistema Ideal de Comunicaciones: Analogico vs Digital

> **Last verified:** 2025-11-16 | **Verified by:** source

## El Marco de Shannon

Claude Shannon (1948) establecio que existe un esquema de comunicacion "ideal" basado en codificacion digital: [source]

- Para cualquier tasa $R < C$ (capacidad del canal), existe un codigo que permite transmitir con error arbitrariamente pequeno.
- Este resultado **solo es valido para sistemas digitales**. Los sistemas analogicos no pueden alcanzar comunicacion libre de errores.

Este teorema revolucionario explica la transicion masiva de sistemas analogicos a digitales en las ultimas decadas.

## Comparacion Fundamental

### Sistema Analogico

$$s_{rx}(t) = s_{tx}(t) + n(t)$$

- El ruido $n(t)$ es **inseparable** de la senal
- Degradacion gradual y monotona con el ruido
- Cada etapa de amplificacion agrega mas ruido: $SNR_{salida} < SNR_{entrada}$
- No existe metodo para eliminar el ruido sin conocimiento previo de la senal original [analysis]

Caracteristicas: [source]
- SNR disminuye con cada repetidor
- No alcanza la capacidad de Shannon
- Imposible regenerar sin perdida
- Calidad depende de la distancia

### Sistema Digital

$$\hat{s} = \arg\min_{s_i} d(r, s_i)$$

- El receptor toma **decisiones** discretas sobre que simbolo se transmitio
- Si el ruido es insuficiente para cambiar la decision: recuperacion perfecta
- **Regeneracion perfecta** en cada repetidor (ver [[conceptos-integradores/compromisos-diseno]]) [analysis]

Caracteristicas: [source]
- Operacion libre de errores posible si $R < C$
- Degradacion abrupta en umbral ("cliff effect")
- Puede acercarse arbitrariamente a la capacidad con codificacion
- BER puede hacerse arbitrariamente pequeno (a costa de complejidad y latencia)

## Analisis Cuantitativo

### Limite de Shannon para Digital

$$\boxed{P_e < \epsilon \quad \text{para cualquier } R < C, \epsilon > 0}$$

Con codificacion optima, la probabilidad de error decae exponencialmente con la longitud del bloque. [source]

### Limite para Sistemas Analogicos

Para senales analogicas con SNR finito, la distorsion minima:

$$D = \frac{\sigma_x^2}{1 + SNR}$$

**Nunca puede ser cero** para SNR finito. Siempre hay degradacion residual.

## Efecto de Umbral (Cliff Effect)

- **Sistemas digitales**: comportamiento de "todo o nada"
  - Por encima del umbral de SNR: BER $\approx 10^{-11}$ (calidad perfecta)
  - Por debajo: falla total (imposible decodificar)
  
- **Sistemas analogicos**: degradacion gradual
  - La calidad disminuye suavemente al bajar SNR
  - Ventaja en escenarios marginales (ej: radio AM de emergencia) [analysis]

## Ejemplo Comparativo

Canal con $B = 1$ MHz, $SNR = 15$ dB ($= 31.6$):

$$C_{Shannon} = 10^6 \times \log_2(32.6) \approx 5.04 \text{ Mbps}$$

- **FM de banda ancha (analogico)**: $\sim 1.6$ Mbps equivalentes $\to$ **32% de eficiencia**
- **64-QAM + Turbo codes (digital)**: $\sim 4.5$ Mbps con BER $< 10^{-9}$ $\to$ **89% de eficiencia**

El sistema digital aprovecha casi 3 veces mejor el canal. [analysis]

## Ventajas y Desventajas

| Aspecto | Analogico | Digital |
|---------|-----------|---------|
| Ruido | Acumulativo | No acumulativo (regeneracion) |
| SNR minimo | Funciona con SNR muy bajo | Requiere SNR > umbral |
| Complejidad | Baja | Alta (ADC, DSP, sincronizacion) |
| Latencia | Minima | Significativa (procesamiento) |
| Limite teorico | No alcanzable | Alcanzable con codificacion |

## Errores Comunes

- **Pensar que digital siempre es mejor**: bajo el umbral de SNR, analogico puede dar algo util donde digital falla completamente
- **Ignorar latencia digital**: procesamiento (FEC, interleaving) introduce retardo
- **Digitalizar no mejora una senal degradada**: "garbage in, garbage out"

## Ver tambien

- [[teoria-informacion/teorema-shannon-hartley]]
- [[teoria-informacion/capacidad-canal-shannon]]
- [[introduccion/modelo-shannon]]
- [[conceptos-integradores/comparacion-global-modulaciones]]
- [[conceptos-integradores/compromisos-diseno]]
- [[conceptos-integradores/evolucion-sistemas]]
