---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_08/carta_43_efecto-enfasis-fm-am.md
curso: Sistemas de Comunicaciones
unidad: 8
---

# Efecto de Enfasis en FM y AM

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_08/carta_43_efecto-enfasis-fm-am]]]

El pre-enfasis y de-enfasis son tecnicas complementarias que mejoran significativamente la SNR en sistemas FM, explotando la forma del espectro de ruido a la salida del demodulador.

## Espectro de ruido en FM

El ruido a la salida de un demodulador FM tiene un espectro **triangular** (creciente con la frecuencia):

$$\boxed{S_{n,\text{out}}(f) = \frac{2N_0 f^2}{A^2}}$$

El ruido crece cuadraticamente con $f$: las frecuencias altas de la senal demodulada son mucho mas ruidosas que las bajas. [source — [[../../explicaciones_anki/unidad_08/carta_43_efecto-enfasis-fm-am]]]

## Pre-enfasis y De-enfasis

Para compensar este espectro no uniforme se usan filtros complementarios:

### Pre-enfasis (en el transmisor)

Realza las frecuencias altas de la senal moduladora antes de la modulacion FM:

$$\boxed{H_{\text{pre}}(f) = 1 + j\left(\frac{f}{f_1}\right)}$$

donde $f_1 = 1/(2\pi\tau)$ es la frecuencia de corte.

### De-enfasis (en el receptor)

Atenua las frecuencias altas despues de la demodulacion, restaurando la senal original:

$$H_{\text{de}}(f) = \frac{1}{1 + j(f/f_1)}$$

### Condicion de complementariedad

Los filtros son inversos entre si:

$$\boxed{H_{\text{pre}}(f) \cdot H_{\text{de}}(f) = 1}$$

La senal de audio no sufre distorsion neta, pero el ruido de alta frecuencia (que es el dominante en FM) es fuertemente atenuado por el de-enfasis. [analysis]

## Constantes de tiempo estandar

| Estandar | $\tau$ | Region |
|---|---|---|
| FCC | 75 $\mu$s | USA, Japon |
| CCIR | 50 $\mu$s | Europa, resto del mundo |

La constante de tiempo determina la frecuencia a partir de la cual actua el enfasis. [source — [[../../explicaciones_anki/unidad_08/carta_43_efecto-enfasis-fm-am]]]

## Mejora total de SNR

El enfasis proporciona una mejora adicional de **10-13 dB** sobre la ganancia inherente de FM ($3\beta^2$). En total:

$$(\text{SNR}_o/\text{SNR}_i)_{\text{FM+enfasis}} \approx (\text{SNR}_o/\text{SNR}_i)_{\text{FM}} + 13\text{ dB}$$

FM con enfasis mejora la SNR en **mas de 30 dB** respecto a AM. Esto justifica la asignacion de 200 kHz por canal en FM broadcast: el ancho de banda extra se intercambia por calidad de audio excepcional. [analysis]

## Por que AM no se beneficia igual

En deteccion de envolvente de AM, el espectro de ruido de salida es esencialmente **plano** (ruido blanco). El pre-enfasis no ofrece ventaja porque no hay una zona del espectro donde concentrar la mejora. El enfasis es efectivo precisamente porque el ruido FM tiene un espectro no uniforme (triangular). [analysis]

## Analogos en sistemas digitales

En comunicaciones digitales, conceptos similares aparecen como:

- **Spectral shaping / water-filling:** asignar mas potencia a subportadoras con mejor SNR
- **Modulacion adaptativa:** usar constelaciones mas densas en subportadoras con mejor canal

## Ver también

- [[../modulacion-analogica/preenfasis-deenfasis]] — Pre-enfasis y de-enfasis
- [[../ruido/snr-modulacion-exponencial]] — S/R en modulacion exponencial
- [[../ruido/snr-modulacion-lineal]] — S/R en modulacion lineal
- [[../ruido/efecto-umbral]] — Efecto umbral
- [[../ruido/intercomparacion-sistemas]] — Intercomparacion
- [[../modulacion-analogica/fm-estereo]] — FM estereo
