---
tags:
  - wiki/derivaciones
  - wiki/modulacion-analogica
source_file: outputs/derivations/AM_parallel_20251115.md
curso: Sistemas de Comunicaciones
unidad: 3
---

# Derivación Extendida de AM

> **Last verified:** 2025-11-15 | **Verified by:** [source — [[../../outputs/derivations/AM_parallel_20251115]]]

**Versión extendida** de la derivación canónica de modulación AM. Complementa [[modulacion-am]] con un enfoque paso a paso exhaustivo que incluye explicaciones pedagógicas detalladas, preguntas "Why this step?" y análisis físico en cada etapa.

---

## Señales de partida

**Portadora** [source]:

$$c(t) = A_c \cos(2\pi f_c t)$$

**Mensaje** [source]:

$$m(t) = A_m \cos(2\pi f_m t), \quad f_m \ll f_c$$

**Índice de modulación** [source]:

$$\mu = \frac{A_m}{A_c}, \quad 0 \leq \mu \leq 1$$

---

## Derivación paso a paso

### 1. Variación de amplitud [source]

La amplitud instantánea de la portadora debe seguir la señal mensaje [analysis]:

$$A(t) = A_c + m(t) = A_c[1 + \mu \cos(2\pi f_m t)]$$

La amplitud varía entre $A_c(1-\mu)$ y $A_c(1+\mu)$ [source].

### 2. Formación de la señal AM [source]

$$s_{AM}(t) = A(t) \cdot \cos(2\pi f_c t) = A_c[1 + \mu \cos(2\pi f_m t)] \cos(2\pi f_c t)$$

### 3. Identidad trigonométrica [source]

Aplicando $\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$:

### 4. Expresión espectral [source]

$$\boxed{s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{A_c \mu}{2} \cos(2\pi(f_c - f_m)t) + \frac{A_c \mu}{2} \cos(2\pi(f_c + f_m)t)}$$

Tres componentes [source]:
1. **Portadora** en $f_c$ — amplitud $A_c$
2. **LSB** en $f_c - f_m$ — amplitud $A_c\mu/2$
3. **USB** en $f_c + f_m$ — amplitud $A_c\mu/2$

### 5. Transformada de Fourier [source]

$$S_{AM}(f) = \frac{A_c}{2}[\delta(f - f_c) + \delta(f + f_c)] + \frac{A_c \mu}{4}[\delta(f - (f_c - f_m)) + \delta(f + (f_c - f_m))] + \frac{A_c \mu}{4}[\delta(f - (f_c + f_m)) + \delta(f + (f_c + f_m))]$$

### 6. Ancho de banda [source]

$$\boxed{BW = 2f_m}$$

Para señales mensaje complejas de ancho de banda $B$ [source]:

$$\boxed{BW_{AM} = 2B}$$

---

## Análisis de potencia [source]

### Potencia de portadora

$$P_c = \frac{A_c^2}{2R}$$

### Potencia de bandas laterales

$$P_{sidebands} = P_{LSB} + P_{USB} = \frac{A_c^2 \mu^2}{4R}$$

### Potencia total

$$\boxed{P_{total} = P_c\left(1 + \frac{\mu^2}{2}\right)}$$

### Eficiencia [source]

$$\boxed{\eta = \frac{\mu^2}{2 + \mu^2} \times 100\%}$$

### Eficiencia máxima ($\mu = 1$) [source]

$$\boxed{\eta_{max} = 33.33\%}$$

| $\mu$ | $\eta$ (%) |
|-------|-----------|
| 0.1 | 0.50% |
| 0.3 | 4.29% |
| 0.5 | 11.11% |
| 0.7 | 19.60% |
| 1.0 | 33.33% |

---

## Lo que aporta esta versión

Respecto a la derivación canónica en [[modulacion-am]], esta versión extendida añade [analysis]:

- **Explicaciones "Why this step?"** para cada paso de la derivación, con razonamiento físico y matemático explícito
- **Espectro de Fourier completo** con impulsos en frecuencias positivas y negativas
- **Interpretación física detallada** del significado de cada componente espectral
- **Análisis completo de potencia** con desglose de LSB, USB, portadora y deducción completa de la eficiencia
- **Tablas de eficiencia vs. $\mu$** que muestran numéricamente el rendimiento
- **Sección de aplicaciones** (broadcasting AM, aviación, CB, ASK, QAM moderno)
- **Diagrama espectral ASCII** con las tres líneas espectrales
- **Resumen visual** de los 9 pasos de derivación en formato compacto
- **Discusión sobre redundancia**: ambas bandas laterales contienen la misma información [source]
- **Principio de detección de envolvente** como ventaja práctica de AM

---

## Ver también

- [[modulacion-am]] — Derivación canónica de AM
- [[../modulacion-analogica/am-vs-dsb-sc]] — Comparación AM vs DSB-SC
- [[../modulacion-analogica/indice-modulacion-am]] — Índice de modulación
- [[../ruido/snr-modulacion-lineal]] — S/R en modulación lineal
