---
tags:
  - wiki/espectro-expandido
source_file: explicaciones_anki/unidad_10/carta_51_dsss-vs-fhss.md
curso: Sistemas de Comunicaciones
unidad: 10
---

# FHSS — Frequency Hopping Spread Spectrum

> **Last verified:** 2025-11-16 | **Verified by:** source

## Principio

**FHSS** (Frequency Hopping Spread Spectrum) expande el espectro cambiando rapidamente la frecuencia de la portadora segun un patron pseudoaleatorio. La senal "salta" entre multiples frecuencias disponibles, usando una sola frecuencia a la vez. [source]

$$s_{FHSS}(t) = d(t) \cdot \cos(2\pi f_i(t) \cdot t)$$

Donde $f_i(t)$ salta entre $M$ frecuencias disponibles: $f_i \in \{f_1, f_2, \dots, f_M\}$.

## Tipos de Hopping

### Slow Hopping ($T_{hop} > T_{bit}$)
- Varios bits por salto
- Mas simple de implementar
- Menor robustez contra jamming
- Usado en: Bluetooth clasico

### Fast Hopping ($T_{hop} < T_{bit}$)
- Varios saltos por bit
- Mayor robustez (diversidad frecuencial por bit)
- Mas complejo (sincronizacion mas exigente)
- Usado en: sistemas militares

La probabilidad de que un jammer afecte un hop: $P_{hit} = k/M$ donde $k$ es el numero de frecuencias interferidas.

## Ganancia de Procesamiento

Para FHSS con $M$ frecuencias disponibles e interferencia en $k$ de ellas:

$$\boxed{G_{p,FHSS} \approx \frac{M}{k}}$$

Ejemplo: $M = 79$ canales, jammer en 1 canal $\to G_p \approx 79 \approx 19$ dB.

A diferencia de DSSS, la ganancia en FHSS se obtiene por **promediacion estadistica** sobre los saltos, no por expansion instantanea del espectro. [analysis]

## Bluetooth como Caso de Estudio

Bluetooth usa FHSS adaptativo en la banda ISM de 2.4 GHz:

| Parametro | Valor |
|-----------|-------|
| Canales | 79 de 1 MHz |
| Saltos por segundo | 1600 |
| Duracion de slot | 625 $\mu$s |
| Banda total | 2.400 – 2.485 GHz |

**Adaptive Frequency Hopping (AFH)**: detecta canales con interferencia WiFi y los evita dinamicamente. Si WiFi ocupa 22 canales Bluetooth, AFH usa los 57 restantes, eliminando virtualmente las colisiones. [analysis]

Sin AFH: $P_{col} = 1/79 \approx 1.3\%$. Con AFH: $P_{col} \approx 0$ (idealmente).

## Comparacion DSSS vs FHSS

| Aspecto | DSSS | FHSS |
|---------|------|------|
| **Expansion** | Dominio de codigo | Dominio frecuencial |
| **Espectro** | Banda ancha continua | Pico que salta |
| **Contra ruido continuo** | Excelente | Bueno |
| **Contra jammer parcial** | Bueno | Excelente |
| **Contra jammer banda ancha** | Malo | Malo |
| **Sincronizacion** | Alineacion de codigo | Alineacion de saltos |
| **Near-far** | Critico | Menos critico |
| **Aplicacion tipica** | GPS, CDMA | Bluetooth, militar |

## Ventajas y Desventajas

**Ventajas de FHSS**: [analysis]
- Implementacion mas simple (no requiere correladores complejos)
- Excelente contra interferencia de banda angosta y jamming pulsado
- Puede adaptar dinamicamente el conjunto de saltos (AFH)
- Menos sensible al problema near-far que CDMA

**Desventajas**:
- Menor ganancia de procesamiento que DSSS
- Requiere sintetizadores de frecuencia agiles
- Sensible a jamming de banda ancha (afecta todos los canales)

## Aplicaciones

| Sistema | Tecnica | Caracteristica |
|---------|---------|----------------|
| Bluetooth | FHSS (AFH) | 79 canales, coexistencia con WiFi |
| 802.11 legacy | FHSS | Primeras versiones de WiFi |
| Militar tactico | FHSS rapido | Anti-jamming |
| Radios HF | FHSS lento | Comunicaciones seguras |

## Errores Comunes

- Pensar que FHSS siempre evita interferencias: solo si la interferencia es parcial en frecuencia
- Confundir slow-FH con fast-FH: implican comportamientos muy diferentes ante errores de rafaga
- Asumir que FHSS es siempre mas simple: los sintetizadores de frecuencia agiles tienen su propia complejidad

## Ver tambien

- [[espectro-expandido/cdma]]
- [[espectro-expandido/dsss]]
- [[espectro-expandido/ofdm]]
- [[espectro-expandido/aplicaciones-spread-spectrum]]
