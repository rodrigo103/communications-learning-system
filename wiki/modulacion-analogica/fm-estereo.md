---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_04/carta_21_comparacion_fm_pm.md
curso: Sistemas de Comunicaciones
unidad: 4
---

# FM Estereo

> **Last verified:** 2025-11-16 | **Verified by:** [analysis]

## Principio de Transmision

La radio FM estereo transmite dos canales de audio (izquierdo L y derecho R) dentro del ancho de banda asignado de 200 kHz usando multiplexacion por division de frecuencia (FDM) [source — [[../../explicaciones_anki/unidad_04/carta_21_comparacion_fm_pm]]].

## Señal Multiplex (MPX)

La señal compuesta que modula la portadora FM contiene [source — [[../../explicaciones_anki/unidad_04/carta_21_comparacion_fm_pm]]]:

| Componente | Frecuencia | Contenido | Funcion |
|-----------|------------|-----------|---------|
| L+R | 50 Hz - 15 kHz (banda base) | Suma de canales | Compatibilidad mono |
| L-R | 23-53 kHz (DSB-SC) | Diferencia de canales | Informacion estereo |
| Piloto | 19 kHz | Tono de referencia | Sincronizacion |
| RDS (opcional) | 57 kHz | Datos digitales | Informacion de estacion |

## Espectro de la Señal MPX

```
|----L+R----| piloto |------L-R (DSB-SC)------| RDS |
0          19 kHz  23 kHz              53 kHz  57 kHz
             ↑
        Subportadora suprimida en 38 kHz
```

## Ecuacion de la Señal MPX

$$\boxed{s_{MPX}(t) = [L(t) + R(t)] + [L(t) - R(t)]\cos(2\pi \cdot 38\text{k} \cdot t) + A_p\cos(2\pi \cdot 19\text{k} \cdot t)}$$

Donde $A_p$ es la amplitud del piloto (tipicamente 8-10% de la desviacion maxima) [source — [[../../explicaciones_anki/unidad_04/carta_21_comparacion_fm_pm]]].

## Proceso de Modulacion

1. **Matriz de codificacion**: genera $L+R$ y $L-R$ a partir de $L$ y $R$
2. **Piloto de 19 kHz**: genera subportadora de 38 kHz (frecuencia doble)
3. **Modulacion DSB-SC**: $L-R$ modula en amplitud a la subportadora de 38 kHz (portadora suprimida)
4. **Suma**: $L+R$ (banda base) + $L-R$ modulado + piloto
5. **Preenfasis**: se aplica por separado a L y R antes de la matriz
6. **Modulacion FM**: la señal MPX modula en frecuencia a la portadora principal (88-108 MHz)

## Compatibilidad Mono/Estereo

- **Receptor mono**: solo demodula $L+R$ (ignora $L-R$ y piloto) → escucha ambos canales combinados [source — [[../../explicaciones_anki/unidad_04/carta_21_comparacion_fm_pm]]]
- **Receptor estereo**: detecta el piloto → activa decodificador → recupera $L$ y $R$:

$$L = \frac{(L+R) + (L-R)}{2}, \quad R = \frac{(L+R) - (L-R)}{2}$$

## Parametros del Sistema

| Parametro | Valor | Observacion |
|-----------|-------|-------------|
| Desviacion total | $\pm 75$ kHz | 100% modulacion |
| Desviacion por piloto | $\pm 6-7.5$ kHz | 8-10% del total |
| Desviacion por L+R | $\pm 67.5$ kHz max | 90% restante |
| Preenfasis | 75 $\mu$s (USA), 50 $\mu$s (EU) | Aplicado a L y R |
| Ancho de banda RF | 200 kHz por canal | Segun FCC/ITU |

## Receptor FM Estereo

Diagrama de bloques tipico:

```
RF → FI (10.7 MHz) → Discriminador FM → Señal MPX → Decodificador Estereo → L, R
                                                ↓
                                        Filtro piloto 19 kHz → ×2 → 38 kHz subportadora
```

El decodificador estereo:
1. Extrae el piloto de 19 kHz
2. Duplica a 38 kHz (oscilador local para demodular $L-R$)
3. Demodula $L-R$ (DSB-SC) de la subportadora
4. Suma/resta con $L+R$ para obtener $L$ y $R$

## Ventajas

- **Compatibilidad inversa**: receptores mono funcionan sin modificacion [source — [[../../explicaciones_anki/unidad_04/carta_21_comparacion_fm_pm]]]
- **Eficiencia espectral**: dos canales de audio en el mismo BW que mono
- **Calidad**: SNR comparable a mono gracias a preenfasis/deenfasis

## Relacion con FDM

FM estereo es un ejemplo practico de [[../modulacion-analogica/multiplex-fdm]]: multiplexa tres señales ($L+R$, $L-R$, piloto) en frecuencia sobre la misma portadora FM [analysis].

## Puntos Clave

- ✓ $L+R$ en banda base para compatibilidad mono [source — [[../../explicaciones_anki/unidad_04/carta_21_comparacion_fm_pm]]]
- ✓ $L-R$ modulado en DSB-SC a 38 kHz (subportadora suprimida) [source — [[../../explicaciones_anki/unidad_04/carta_21_comparacion_fm_pm]]]
- ✓ Piloto de 19 kHz para regenerar subportadora [source — [[../../explicaciones_anki/unidad_04/carta_21_comparacion_fm_pm]]]
- ✓ Preenfasis aplicado a L y R antes de la matriz [source — [[../../explicaciones_anki/unidad_04/carta_21_comparacion_fm_pm]]]

## Ver tambien

- [[../modulacion-analogica/fm-vs-pm]]
- [[../modulacion-analogica/preenfasis-deenfasis]]
- [[../modulacion-analogica/multiplex-fdm]]
- [[../modulacion-analogica/ancho-banda-carson]]
