---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis.md
curso: Sistemas de Comunicaciones
unidad: 4
---

# Preenfasis y Deenfasis en FM

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]]

## Definicion

Preenfasis y deenfasis son tecnicas complementarias de procesamiento que mejoran la relacion señal-ruido (SNR) en FM, especialmente en altas frecuencias [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]].

## El Problema: Ruido Triangular en FM

Despues de la demodulacion FM, la DEP del ruido **no es uniforme**: crece con el cuadrado de la frecuencia [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]]:

$$S_n(f) = K \cdot f^2$$

- A 15 kHz, el ruido es $225\times$ mas fuerte que a 1 kHz
- Se percibe como un **siseo molesto** en frecuencias agudas

## La Solucion

### Preenfasis (Transmisor)

Filtro pasa-altos que **amplifica las altas frecuencias** del audio **antes** de modular [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]]:

$$\boxed{H_p(f) = 1 + j\frac{f}{f_1}}$$

$$f_1 = \frac{1}{2\pi\tau}$$

### Deenfasis (Receptor)

Filtro pasa-bajos que **atenua las altas frecuencias después** de demodular [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]]:

$$\boxed{H_d(f) = \frac{1}{1 + j\frac{f}{f_1}}}$$

### Compensacion Exacta

$$\boxed{H_p(f) \cdot H_d(f) = 1}$$

La respuesta en frecuencia total es **plana** (el audio se restaura fielmente), pero el ruido de alta frecuencia agregado durante la transmision es atenuado por $H_d(f)$ [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]].

## Estandares

| Region | $\tau$ | $f_1$ | Mejora SNR @ 15 kHz |
|--------|--------|-------|---------------------|
| USA/Japon | 75 $\mu$s | 2.12 kHz | $\approx 13.5$ dB |
| Europa/Australia | 50 $\mu$s | 3.18 kHz | $\approx 11.3$ dB |

La diferencia historica refleja distintas preferencias de sonido y caracteristicas de audio [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]].

## Mejora de SNR

La mejora en SNR con preenfasis/deenfasis es [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]]:

$$\boxed{\text{Mejora SNR} \approx 13.5 \text{ dB (estandar 75 }\mu\text{s)}}$$

Esta mejora **no cuesta ancho de banda adicional** — es una de las razones clave por las que FM supera a AM en calidad [analysis].

## Ejemplo de Diseño

Para FM broadcast USA ($\tau = 75$ $\mu$s):

- Frecuencia de corte: $f_1 = \frac{1}{2\pi \cdot 75 \cdot 10^{-6}} = 2122$ Hz
- Ganancia de preenfasis a 15 kHz: $|H_p| = \sqrt{1 + (15000/2122)^2} = 7.14 = 17.1$ dB
- Componentes RC tipicos: $R = 600\;\Omega$, $C = 125$ nF

## Analogia

Imagina una fiesta ruidosa: elevas mas la voz en tonos agudos (preenfasis) porque se pierden mas facilmente. Tu amigo "filtra" mentalmente (deenfasis) tu voz exagerada para entender el mensaje normal, pero el ruido de fondo queda atenuado — recibes el mensaje con menos interferencia [analysis].

## Aplicaciones Relacionadas

- **Discos de vinilo**: curva RIAA (mismo principio)
- **Grabacion magnetica**: curvas NAB, IEC
- **Dolby Noise Reduction**: evolucion del concepto para cassettes

## Puntos Clave

- ✓ El ruido en FM crece con $f^2$ despues del discriminador [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]]
- ✓ Preenfasis/deenfasis mejora SNR sin costo de ancho de banda [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]]
- ✓ Mejora tipica: 10-13 dB en altas frecuencias [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]]
- ✓ $H_p(f) \cdot H_d(f) = 1$: respuesta plana total [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]]
- ✓ USA = 75 $\mu$s, Europa = 50 $\mu$s [source — [[../../explicaciones_anki/unidad_04/carta_20_preenfasis_deenfasis]]]

## Ver tambien

- [[../modulacion-analogica/fm-estereo]]
- [[../modulacion-analogica/modulador-fm]]
- [[../ruido/snr-modulacion-exponencial]]
- [[../ruido/efecto-umbral]]
