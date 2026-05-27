---
tags:
  - wiki/derivaciones
  - wiki/modulacion-analogica
source_file: outputs/derivations/AM_20251115.md
curso: Sistemas de Comunicaciones
unidad: 3
---

# Derivación Completa de Modulación AM

> **Last verified:** 2025-11-15 | **Verified by:** source

## Señal portadora y mensaje

La señal de mensaje (banda base) es $m(t) = A_m \cos(2\pi f_m t)$ y la portadora de alta frecuencia $c(t) = A_c \cos(2\pi f_c t)$, con $f_c \gg f_m$.

El principio fundamental de AM consiste en **variar la amplitud de la portadora** proporcionalmente al mensaje.

## Derivación paso a paso

### Paso 1: Amplitud variable en el tiempo

$$A(t) = A_c + k_a m(t)$$

### Paso 2: Forma normalizada con índice de modulación

$$A(t) = A_c[1 + \mu m_n(t)]$$

donde $\mu = \frac{k_a A_m}{A_c}$ es el índice de modulación (típicamente $\mu \leq 1$ para evitar sobremodulación) [source].

### Paso 3: Señal modulada

$$s_{AM}(t) = A(t) \cdot \cos(2\pi f_c t) = A_c[1 + \mu \cos(2\pi f_m t)] \cos(2\pi f_c t)$$

### Paso 4: Expansión con identidad trigonométrica

Aplicando $\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$:

$$s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{A_c \mu}{2} \cos(2\pi(f_c - f_m)t) + \frac{A_c \mu}{2} \cos(2\pi(f_c + f_m)t)$$

### Componentes espectrales

1. **Portadora:** frecuencia $f_c$, amplitud $A_c$
2. **Banda lateral inferior (LSB):** frecuencia $f_c - f_m$, amplitud $\frac{A_c \mu}{2}$
3. **Banda lateral superior (USB):** frecuencia $f_c + f_m$, amplitud $\frac{A_c \mu}{2}$

## Resultados clave

### Forma compacta

$$\boxed{s_{AM}(t) = A_c[1 + \mu \cos(2\pi f_m t)] \cos(2\pi f_c t)}$$

### Ancho de banda

$$\boxed{BW_{AM} = 2f_m}$$

AM requiere el doble del ancho de banda del mensaje porque transmite ambas bandas laterales [source].

### Distribución de potencia

- Potencia de portadora: $P_c = \frac{A_c^2}{2R}$
- Potencia de cada banda lateral: $P_{SB} = \frac{A_c^2 \mu^2}{8R}$
- Potencia total: $P_{total} = \frac{A_c^2}{2R}\left(1 + \frac{\mu^2}{2}\right)$

### Eficiencia de potencia

Solo las bandas laterales transportan información. La eficiencia es:

$$\eta = \frac{P_{sidebands}}{P_{total}} = \frac{\mu^2}{2 + \mu^2}$$

Eficiencia máxima con $\mu = 1$:

$$\boxed{\eta_{max} = \frac{1}{3} = 33.33\%}$$

Esta baja eficiencia es la principal debilidad de AM [analysis]. La portadora consume el 67% de la potencia sin transportar información. Esto motivó el desarrollo de variantes como [[modulacion-analogica/am-vs-dsb-sc|DSB-SC]] (supresión de portadora) y SSB (banda lateral única).

### Sobremodulación

Si $\mu > 1$, ocurre **sobremodulación**: la envolvente se vuelve negativa, causando distorsión en la demodulación por detector de envolvente.

## Interpretación física

- **Dominio del tiempo:** La envolvente sigue la forma $A_c[1 + \mu m_n(t)]$ modulada a frecuencia $f_c$
- **Dominio de la frecuencia:** El espectro en banda base se traslada a $\pm f_c$, creando portadora + dos bandas laterales

## Aplicaciones

- Radio AM broadcasting (540–1600 kHz)
- Comunicaciones aeronáuticas
- Radio CB (Citizen's Band)

## Ver también

- [[modulacion-analogica/am-vs-dsb-sc]]
- [[modulacion-analogica/indice-modulacion-am]]
- [[ruido/snr-modulacion-lineal]]
- [[modulacion-analogica/deteccion-coherente]]
