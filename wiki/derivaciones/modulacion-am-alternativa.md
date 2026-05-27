---
tags:
  - wiki/derivaciones
  - wiki/modulacion-analogica
source_file: outputs/derivations/AM_subagent_20251115.md
curso: Sistemas de Comunicaciones
unidad: 3
---

# Derivación Alternativa de AM (Subagente)

> **Last verified:** 2025-11-15 | **Verified by:** [source — [[../../outputs/derivations/AM_subagent_20251115]]]

**Versión alternativa** de la derivación de modulación AM generada por subagente. Complementa la derivación canónica en [[modulacion-am]] con una perspectiva que enfatiza la conexión con la transformada de Fourier, tablas de variables estructuradas y secciones de "Physical meaning" a lo largo del desarrollo.

---

## Señales de partida

**Mensaje** (banda base) [source]:

$$m(t) = A_m \cos(2\pi f_m t)$$

**Portadora** (alta frecuencia) [source]:

$$c(t) = A_c \cos(2\pi f_c t), \quad f_c \gg f_m$$

| Símbolo | Descripción | Unidades | Rango típico |
|---------|-------------|----------|-------------|
| $s_{AM}(t)$ | Señal modulada AM | V | — |
| $A_c$ | Amplitud de portadora | V | $> 0$ |
| $A_m$ | Amplitud de mensaje | V | $> 0$ |
| $\mu$ | Índice de modulación ($A_m/A_c$) | adimensional | 0 a 1 |
| $f_c$ | Frecuencia de portadora | Hz | kHz a GHz |
| $f_m$ | Frecuencia de mensaje | Hz | Hz a kHz |

---

## Derivación

### Paso 1: Principio de modulación [source]

Se crea una amplitud variable con componente continua y alterna [analysis]:

$$A(t) = A_c + m(t)$$

La componente DC ($A_c$) es el nivel sin modular; la AC ($m(t)$) transporta la información [source].

### Paso 2: Sustitución explícita [source]

$$A(t) = A_c + A_m \cos(2\pi f_m t)$$

Con $\cos = +1$: amplitud máxima $A_c + A_m$; con $\cos = -1$: amplitud mínima $A_c - A_m$ [source].

### Paso 3: Señal modulada [source]

$$s_{AM}(t) = [A_c + A_m \cos(2\pi f_m t)] \cos(2\pi f_c t)$$

### Paso 4: Expansión distributiva [source]

$$s_{AM}(t) = A_c \cos(2\pi f_c t) + A_m \cos(2\pi f_m t) \cos(2\pi f_c t)$$

### Paso 5: Identidad trigonométrica [source]

$$\cos(2\pi f_m t) \cos(2\pi f_c t) = \frac{1}{2}[\cos(2\pi(f_c - f_m)t) + \cos(2\pi(f_c + f_m)t)]$$

### Paso 6: Representación espectral [source]

$$s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{A_m}{2}\cos(2\pi(f_c - f_m)t) + \frac{A_m}{2}\cos(2\pi(f_c + f_m)t)$$

### Paso 7: Índice de modulación [source]

Sustituyendo $A_m = \mu A_c$:

$$s_{AM}(t) = A_c \left[\cos(2\pi f_c t) + \frac{\mu}{2}\cos(2\pi(f_c - f_m)t) + \frac{\mu}{2}\cos(2\pi(f_c + f_m)t)\right]$$

### Paso 8: Forma compacta [source]

$$\boxed{s_{AM}(t) = A_c[1 + \mu \cos(2\pi f_m t)]\cos(2\pi f_c t)}$$

**Interpretación física**: la envolvente $A_c[1 + \mu \cos(2\pi f_m t)]$ varía entre $A_c(1-\mu)$ y $A_c(1+\mu)$ y contiene directamente la señal mensaje [source].

---

## Forma expandida final [source]

$$\boxed{s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{\mu A_c}{2}\cos(2\pi(f_c - f_m)t) + \frac{\mu A_c}{2}\cos(2\pi(f_c + f_m)t)}$$

---

## Restricciones del índice de modulación [source]

$$0 \leq \mu \leq 1$$

- $\mu = 0$: sin modulación (portadora pura)
- $0 < \mu < 1$: submodulación (segura, sin distorsión) [analysis]
- $\mu = 1$: modulación 100% (máxima eficiencia sin distorsión) [source]
- $\mu > 1$: sobremodulación (distorsión y splatter espectral) [source]

---

## Análisis de ancho de banda y potencia

### Ancho de banda [source]

$$\boxed{B_{AM} = 2f_m}$$

Para señal compleja con frecuencia máxima $f_{m,max}$ [source]:

$$B_{AM} = 2f_{m,max}$$

### Potencia de portadora [source]

$$P_c = \frac{A_c^2}{2R}$$

### Potencia de bandas laterales [source]

$$P_{sidebands} = \frac{\mu^2 A_c^2}{4R} = \frac{\mu^2}{2} \cdot P_c$$

### Potencia total [source]

$$\boxed{P_{total} = P_c\left(1 + \frac{\mu^2}{2}\right)}$$

### Eficiencia [source]

$$\eta = \frac{\mu^2}{2 + \mu^2}$$

$$\boxed{\eta_{max} = \frac{1}{3} = 33.33\% \quad (\text{para } \mu = 1)}$$

---

## Conexión con Fourier [source]

Propiedad de traslación de frecuencia [source]:

$$m(t) \cos(2\pi f_c t) \xrightarrow{\mathcal{F}} \frac{1}{2}[M(f - f_c) + M(f + f_c)]$$

**Interpretación** [analysis]: Multiplicar por coseno en tiempo equivale a desplazar y escalar el espectro en frecuencia. Este es el principio fundamental del heterodinaje.

---

## Lo que aporta esta versión

Respecto a la derivación canónica en [[modulacion-am]], esta versión alternativa añade [analysis]:

- **Tabla de variables estructurada** con descripciones, unidades y rangos típicos de cada parámetro
- **Conexión explícita con la transformada de Fourier** y la propiedad de traslación en frecuencia
- **Secciones "Physical meaning"** que interpretan físicamente cada componente espectral
- **Restricciones detalladas de $\mu$** con las cuatro regiones (sin modulación, submodulación, 100%, sobremodulación)
- **Interpretación en dominio temporal**: analogía de la envolvente como "contorno" de la portadora
- **Interpretación en dominio frecuencial**: significado de cada línea espectral
- **Aplicaciones prácticas y limitaciones**: generación, detección, ventajas y desventajas
- **Discusión de técnicas derivadas**: DSB-SC, SSB, VSB como respuesta a las ineficiencias de AM [source]

---

## Ver también

- [[modulacion-am]] — Derivación canónica
- [[modulacion-am-extendida]] — Derivación extendida (versión exhaustiva)
- [[../herramientas-matematicas/teorema-convolucion]] — Teorema de convolución
- [[../modulacion-analogica/am-vs-dsb-sc]] — AM vs DSB-SC
