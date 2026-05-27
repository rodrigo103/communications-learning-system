---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc.md
curso: Sistemas de Comunicaciones
unidad: 3
---

# AM-DSB-FC vs DSB-SC: Comparacion

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]

## Definiciones

### AM-DSB-FC (AM Convencional)

Contiene portadora mas ambas bandas laterales [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]:

$$s_{AM}(t) = A_c[1 + k_a m(t)]\cos(2\pi f_c t)$$

Expandiendo:

$$s_{AM}(t) = \underbrace{A_c\cos(2\pi f_c t)}_{\text{portadora}} + \underbrace{A_c k_a m(t)\cos(2\pi f_c t)}_{\text{bandas laterales}}$$

### DSB-SC (Doble Banda con Portadora Suprimida)

Sin termino de portadora independiente [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]:

$$s_{DSB-SC}(t) = A_c m(t)\cos(2\pi f_c t)$$

## Comparacion Espectral

| Propiedad | AM-DSB-FC | DSB-SC |
|-----------|-----------|---------|
| Ancho de banda | $BW = 2f_m$ | $BW = 2f_m$ |
| Portadora | Presente (gasta potencia) | Suprimida |
| Espectro | $S_{AM}(f) = \frac{A_c}{2}[\delta(f-f_c) + \delta(f+f_c)] + \text{bandas}$ | $S_{DSB}(f) = \frac{A_c}{2}[M(f-f_c) + M(f+f_c)]$ |

## Eficiencia de Potencia

Para AM con moduladora sinusoidal e indice $m$:

$$\boxed{\eta_{AM} = \frac{m^2}{2 + m^2}}$$

Para modulacion maxima ($m = 1$):

$$\eta_{max} = \frac{1}{3} = 33.33\%$$

Para DSB-SC:

$$\boxed{\eta_{DSB-SC} = 100\%}$$

Toda la potencia transmitida esta en las bandas laterales (informacion util).

## Metodos de Deteccion

| Aspecto | AM-DSB-FC | DSB-SC |
|---------|-----------|---------|
| Deteccion | Envolvente (simple) | Coherente (requiere sincronismo) |
| Complejidad Rx | Baja | Alta |
| Sincronizacion | No necesaria | Critica |
| Costo receptor | Economico | Costoso |

## Ejemplo Numerico

Estacion AM con $m_{promedio} = 0.3$, $P_{total} = 50$ kW:

$$\eta = \frac{0.09}{2.09} = 0.043$$

- Potencia util: $0.043 \times 50 = 2.15$ kW
- Potencia desperdiciada en portadora: $47.85$ kW
- Con DSB-SC se necesitarian solo $2.15$ kW para misma calidad
- Mejora en SNR: $10\log_{10}(50/2.15) \approx 13.6$ dB

## Trade-off Fundamental

AM-DSB-FC: **simplicidad** (deteccion de envolvente) a costa de eficiencia
DSB-SC: **eficiencia** (100% potencia en informacion) a costa de complejidad (requiere deteccion coherente) [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]

## Aplicaciones Tipicas

- **AM-DSB-FC**: radio AM comercial (530-1700 kHz), aviacion, donde receptores economicos importan [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]
- **DSB-SC**: enlaces punto a punto, satelites, donde la potencia es escasa y costosa [analysis]

## Puntos Clave

- ✓ Ambos esquemas tienen el mismo ancho de banda: $BW = 2f_m$ [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]
- ✓ La portadora no transmite informacion pero facilita demodulacion [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]
- ✓ Eficiencia maxima de AM: $33.33\%$ (con $m=1$) [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]
- ✓ DSB-SC requiere sincronizacion de portadora para demodulacion [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]

## Ver tambien

- [[../modulacion-analogica/indice-modulacion-am]]
- [[../modulacion-analogica/modulacion-ssb]]
- [[../modulacion-analogica/modulacion-vsb]]
- [[../derivaciones/modulacion-am]]
- [[../ruido/snr-modulacion-lineal]]
