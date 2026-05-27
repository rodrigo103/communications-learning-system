---
tags:
  - wiki/problemas
  - wiki/modulacion-analogica
source_file: outputs/solutions/Ejercicio_TP5_3_solution.md
curso: Sistemas de Comunicaciones
unidad: 4
---

# TP5 Ejercicio 3 — Análisis de SNR en Receptor FM

> **Last verified:** 2025-12-09 | **Verified by:** source

## Enunciado

Un receptor FM tiene un filtro FI de 200 kHz y un filtro pasabajos de salida ideal con $f_c = 15$ kHz. Recibe una señal modulada por un tono con $f_m = 5$ kHz y $\Delta f = 75$ kHz. La relación señal-ruido promedio a la entrada del amplificador FI es 40 dB.

Calcular: (a) S/N después del filtro de salida si $F_{FI} = 1$, (b) S/N si $T_{e,FI} = 72.50$ K, (c) Índice de modulación necesario para mejorar 6 dB el S/N de (a).

## Datos

| Variable | Valor |
|----------|-------|
| $B_{FI}$ | 200 kHz |
| $f_c$ (LPF) | 15 kHz |
| $f_m$ | 5 kHz |
| $\Delta f$ | 75 kHz |
| $(S/N)_R$ | 40 dB = 10,000 |
| $F_{FI}$ (a) | 1 |
| $T_{e,FI}$ (b) | 72.50 K |

**Parámetros calculados:**
- $\beta = \Delta f / f_m = 75/5 = 15$
- $B_T$ (Carson) = $2(\Delta f + f_m) = 2(75 + 5) = 160$ kHz
- $W/B_T = f_m / B_T = 5/160 = 0.03125$ (¡crítico!)

## Fórmula clave: Haykin para SNR en FM

$$\boxed{\left(\frac{S}{N}\right)_D = 3\beta^2 \left(\frac{W}{B_T}\right) \left(\frac{S}{N}\right)_R}$$

donde $W = f_m$ (ancho de banda del mensaje), $B_T$ es el ancho de banda de transmisión (Carson). El factor $W/B_T$ es **siempre < 1** en FM de banda ancha [source].

## Solución

### (a) SNR de salida con $F_{FI} = 1$ (sin ruido añadido)

Aplicación directa de Haykin:

$$\begin{aligned}
\left(\frac{S}{N}\right)_D &= 3 \times (15)^2 \times 0.03125 \times 10,000 \\
&= 3 \times 225 \times 0.03125 \times 10,000 \\
&= 21.09375 \times 10,000 = 210,938
\end{aligned}$$

$$\boxed{(S/N)_D = 210,938 \text{ (lineal)} = 53.2 \text{ dB}}$$

**Ganancia de procesamiento FM:** $53.2 - 40 = 13.2$ dB. FM intercambia ancho de banda (160 kHz para señal de 5 kHz) por mejora de SNR [analysis].

### (b) SNR de salida con $T_{e,FI} = 72.50$ K

**Paso 1: Figura de ruido desde temperatura**

$$F_{FI} = 1 + \frac{T_e}{T_0} = 1 + \frac{72.50}{290} = 1.25 \text{ (0.97 dB)}$$

**Paso 2: SNR de entrada degradada**

$$(S/N)_{R,deg} = \frac{(S/N)_R}{F} = \frac{10,000}{1.25} = 8,000 = 39.03 \text{ dB}$$

**Paso 3: Aplicar Haykin**

$$\begin{aligned}
\left(\frac{S}{N}\right)_D &= 3 \times 225 \times 0.03125 \times 8,000 \\
&= 21.09375 \times 8,000 = 168,750
\end{aligned}$$

$$\boxed{(S/N)_D = 168,750 \text{ (lineal)} = 52.3 \text{ dB}}$$

Degradación: $53.2 - 52.3 \approx 0.9$ dB (aproximadamente $F_{dB} = 0.97$ dB) ✓

### (c) $\beta$ necesario para +6 dB

Se requiere $(S/N)_{D,target} = 4 \times (S/N)_{D,a}$. Usando la forma con Carson:

$$\left(\frac{S}{N}\right)_D = \frac{3\beta^2}{2(\beta+1)} \cdot (S/N)_R$$

Planteando $\frac{\beta_{new}^2}{\beta_{new}+1} / \frac{15^2}{16} = 4$:

$$\frac{\beta_{new}^2}{\beta_{new}+1} = 56.25 \Rightarrow \beta_{new}^2 - 56.25\beta_{new} - 56.25 = 0$$

$$\boxed{\beta_{new} = 57.23, \quad \Delta f_{new} = 286.2 \text{ kHz}}$$

**Problema práctico:** $B_{T,new} = 2(286.2 + 5) = 582.4$ kHz **excede los 200 kHz** del filtro FI disponible. Con el filtro fijo, el $\beta$ máximo es $\beta_{max} = 19$ (mejora máxima ~1.08 dB, no 6 dB) [analysis].

## Resumen

| Parte | Resultado | Notas |
|-------|-----------|-------|
| (a) | $(S/N)_D = 53.2$ dB | $F=1$, $B_T=160$ kHz (Carson) |
| (b) | $(S/N)_D = 52.3$ dB | $T_e=72.5$ K, $F=1.25$ |
| (c) | $\beta=57.2$, $\Delta f=286$ kHz | Requiere 582 kHz BW (impracticable!) |

## Aprendizajes clave

- El factor $W/B_T$ (no $B_T/W$) es crítico en la fórmula de Haykin. Error común: invertirlo da ganancias absurdas [analysis]
- La figura de ruido del FI degrada la SNR de entrada **antes** de aplicar la ganancia FM
- Al cambiar $\beta$, $B_T$ también cambia por Carson — no se puede aumentar arbitrariamente sin verificar restricciones de filtro
- **Trade-off BW-SNR:** Mejorar SNR 6 dB requiere cuadruplicar $\beta^2/(\beta+1)$, lo que demanda mucho más ancho de banda

## Ver también

- [[modulacion-analogica/ancho-banda-carson]]
- [[modulacion-analogica/fm-banda-ancha]]
- [[derivaciones/modulacion-fm-carson]]
- [[ruido/formula-friis]]
- [[ruido/factor-ruido-temperatura]]
- [[ruido/relacion-snr]]
- [[ruido/efecto-umbral-fm]]
