---
tags:
  - wiki/introduccion
source_file: explicaciones_anki/unidad_01/carta_02_necesidad-modulacion.md
curso: Sistemas de Comunicaciones
unidad: 1
---

# Necesidad de la Modulacion

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_01/carta_02_necesidad-modulacion]]]

## Definicion

La modulacion es la tecnica fundamental que traslada una señal de informacion de baja frecuencia (banda base) a una frecuencia portadora $f_c$ mucho mayor, permitiendo la transmision eficiente a traves del medio de comunicacion. Sin modulacion, las comunicaciones inalambricas modernas serian imposibles [source — [[../../explicaciones_anki/unidad_01/carta_02_necesidad-modulacion]]].

## Las Cinco Razones Fundamentales

### 1. Adaptacion al Canal de Transmision

Las señales de baja frecuencia no se propagan eficientemente. La modulacion traslada la informacion a frecuencias donde el medio tiene buena propagacion [source — [[../../explicaciones_anki/unidad_01/carta_02_necesidad-modulacion]]]:

$$s_{modulada}(t) = A_c[1 + m(t)]\cos(2\pi f_c t)$$

donde $f_c \gg f_{max}$ de la moduladora $m(t)$.

### 2. Tamaño Practico de Antenas

Para radiar eficientemente, la antena debe ser comparable a la longitud de onda [source — [[../../explicaciones_anki/unidad_01/carta_02_necesidad-modulacion]]]:

$$\boxed{L_{antena} \approx \frac{\lambda}{4} = \frac{c}{4f}}$$

| Señal | Frecuencia | $\lambda$ | Antena $\lambda/4$ | Practico? |
|-------|------------|-----------|---------------------|-----------|
| Voz directa | 1 kHz | 300 km | 75 km | Imposible |
| AM (1 MHz) | 1 MHz | 300 m | 75 m | Posible |
| FM (100 MHz) | 100 MHz | 3 m | 75 cm | Practico |
| Celular (1.9 GHz) | 1.9 GHz | 15.8 cm | 4 cm | Muy practico |

### 3. Multiplexacion: Compartir el Canal

Sin modulacion todas las señales en banda base se mezclarian. Con FDM cada usuario modula a una portadora diferente [source — [[../../explicaciones_anki/unidad_01/carta_02_necesidad-modulacion]]]:

```
|--U1--|  |--U2--|  |--U3--|
100.0    100.2    100.4   MHz
```

Ver [[../modulacion-analogica/multiplex-fdm]] para multiplexacion por frecuencia y [[../modulacion-pulsos/multiplex-tdm]] para multiplexacion temporal.

### 4. Inmunidad a Ruido e Interferencias

La modulacion permite tecnicas de mejora de SNR [analysis]. Para FM:

$$SNR_{salida} = 3\beta^2 \cdot SNR_{entrada}$$

donde $\beta$ es el indice de modulacion. Para FM broadcast ($\beta \approx 5$): mejora de SNR $\approx 75\times$ (18.75 dB).

### 5. Uso Eficiente del Espectro

El [[../introduccion/espectro-electromagnetico]] es un recurso limitado. La modulacion permite asignacion organizada de bandas, reutilizacion de frecuencias y tecnicas avanzadas como OFDM. [source — [[../../explicaciones_anki/unidad_01/carta_02_necesidad-modulacion]]]

## Relacion Frecuencia-Antena

La ecuacion fundamental que relaciona frecuencia y tamaño de antena:

$$\boxed{L_{antena} = \frac{\lambda}{4} = \frac{c}{4f}}$$

donde $c = 3 \times 10^8$ m/s. Sin modulacion a frecuencias altas, las antenas serian impracticamente grandes [source — [[../../explicaciones_anki/unidad_01/carta_02_necesidad-modulacion]]].

## Analogia

El espectro electromagnetico como autopista: sin modulacion todos los vehiculos intentan usar el mismo carril (frecuencias bajas) → embotellamiento total. Con modulacion cada uno usa un carril diferente (frecuencia portadora) → trafico fluido [analysis].

## Ejemplos de Modulacion en Sistemas Reales

| Sistema | Esquema de Modulacion | Frecuencia |
|---------|----------------------|------------|
| Radio AM | AM-DSB-FC | 530-1700 kHz |
| Radio FM | FM banda ancha | 88-108 MHz |
| WiFi | OFDM + QAM | 2.4/5 GHz |
| 4G/5G | OFDMA + QAM | 700 MHz - 3.5 GHz |
| GPS | BPSK + Spread Spectrum | 1.575 GHz |

## Puntos Clave

- **Sin modulacion = sin comunicaciones modernas**: es absolutamente esencial [source — [[../../explicaciones_anki/unidad_01/carta_02_necesidad-modulacion]]]
- **Frecuencia determina propagacion**: cada banda tiene caracteristicas unicas [analysis]
- **Espectro = recurso limitado**: como bienes raices electromagneticos [source — [[../../explicaciones_anki/unidad_01/carta_02_necesidad-modulacion]]]

## Ver tambien

- [[../introduccion/modelo-shannon]]
- [[../introduccion/espectro-electromagnetico]]
- [[../modulacion-analogica/am-vs-dsb-sc]]
- [[../modulacion-analogica/multiplex-fdm]]
- [[../modulacion-pulsos/multiplex-tdm]]
- [[../modulacion-digital/ask-fsk-psk]]
- [[../../explicaciones_anki/conceptos_integradores/carta_60_evolucion_historica_sistemas_modulacion|Evolucion historica]] — De AM a 5G
