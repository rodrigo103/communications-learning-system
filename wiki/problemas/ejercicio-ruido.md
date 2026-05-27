---
tags:
  - wiki/problemas
  - wiki/ruido
source_file: outputs/solutions/ejercicio_ruido_complete_20251115.md
curso: Sistemas de Comunicaciones
unidad: 7
---

# Ejercicio de Ruido — Amplificador y Sistema en Cascada

> **Last verified:** 2025-11-15 | **Verified by:** source

## Enunciado

Se tiene un amplificador con ganancia $G_{dB} = 50$ dB, ancho de banda $BW = 20$ kHz, potencia de ruido a la salida $P_{n,out} = 72 \times 10^{-12}$ W. La densidad espectral de ruido a la entrada es $\eta_{in} = 12 \times 10^{-21}$ W/Hz. Temperatura de referencia $T_0 = 290$ K.

**Datos dados:**
| Parámetro | Valor |
|-----------|-------|
| $G_{dB}$ | 50 dB |
| $BW$ | 20 kHz |
| $P_{n,out}$ | $72 \times 10^{-12}$ W |
| $\eta_{in}$ | $12 \times 10^{-21}$ W/Hz |
| $T_0$ | 290 K |

Calcular: (a) figura de ruido $F$, (b) temperatura equivalente de ruido $T_e$, (c) $F_{total}$ de dos amplificadores idénticos en cascada, (d) $T_{total}$ de la cascada, (e) SNR de salida con $S_{in} = 10^{-15}$ W.

## Solución

### (a) Figura de ruido F

**Paso 1: Convertir ganancia**
$$G = 10^{G_{dB}/10} = 10^{50/10} = 10^5 = 100,000$$

**Paso 2: Potencia de ruido de entrada**
$$P_{n,in} = \eta_{in} \cdot BW = (12 \times 10^{-21})(20 \times 10^3) = 2.4 \times 10^{-16} \text{ W}$$

**Paso 3: Figura de ruido**

$$F = \frac{P_{n,out}}{G \cdot P_{n,in}} = \frac{72 \times 10^{-12}}{10^5 \times 2.4 \times 10^{-16}} = \frac{72 \times 10^{-12}}{2.4 \times 10^{-11}} = 3$$

$$\boxed{F = 3 \text{ (lineal)} = 4.77 \text{ dB}}$$

### (b) Temperatura equivalente de ruido

$$T_e = (F - 1) \cdot T_0 = (3 - 1) \times 290 = 580 \text{ K}$$

$$\boxed{T_e = 580 \text{ K}}$$

Relación de comprobación: $F = 1 + T_e/T_0 = 1 + 580/290 = 3$ ✓

### (c) Figura de ruido de cascada (Friis)

Aplicando la [[../ruido/formula-friis|fórmula de Friis]] para dos etapas idénticas:

$$F_{total} = F_1 + \frac{F_2 - 1}{G_1} = 3 + \frac{3 - 1}{10^5} = 3 + 0.00002 = 3.00002$$

$$\boxed{F_{total} = 3.00002 \text{ (lineal)} \approx 4.77 \text{ dB}}$$

### (d) Temperatura total de cascada

$$T_{total} = (F_{total} - 1) \cdot T_0 = (3.00002 - 1) \times 290 \approx 580 \text{ K}$$

Alternativamente: $T_{total} = T_{e1} + T_{e2}/G_1 = 580 + 580/10^5 \approx 580 \text{ K}$

$$\boxed{T_{total} \approx 580 \text{ K}}$$

### (e) SNR de salida

**Paso 1: SNR de entrada**

$$SNR_{in} = \frac{S_{in}}{P_{n,in}} = \frac{10^{-15}}{2.4 \times 10^{-16}} = 4.167 = 6.20 \text{ dB}$$

**Paso 2: SNR de salida**

$$SNR_{out} = \frac{SNR_{in}}{F} = \frac{4.167}{3} = 1.389 = 1.43 \text{ dB}$$

$$\boxed{SNR_{out} = 1.389 \text{ (lineal)} = 1.43 \text{ dB}}$$

Verificación: $SNR_{out,dB} = SNR_{in,dB} - F_{dB} = 6.20 - 4.77 = 1.43$ dB ✓

## Resumen de resultados

| Parte | Concepto | Resultado |
|-------|----------|-----------|
| (a) | Figura de ruido | $F = 3$ (4.77 dB) |
| (b) | Temperatura de ruido | $T_e = 580$ K |
| (c) | F cascada | $F_{total} = 3.00002$ (4.77 dB) |
| (d) | T cascada | $T_{total} \approx 580$ K |
| (e) | SNR salida | $SNR_{out} = 1.389$ (1.43 dB) |

## Análisis y conclusiones

### Dominancia de la primera etapa
La segunda etapa contribuye solo $0.00002$ a $F_{total}$ (0.0007% del total). Con $G_1 = 50$ dB, las etapas posteriores son irrelevantes para el ruido [analysis].

### Degradación de SNR
El amplificador degrada la SNR exactamente en su figura de ruido: de 6.20 dB a 1.43 dB (pérdida de 4.77 dB = $F_{dB}$). Un $SNR_{out}$ de 1.43 dB es muy bajo — se necesitaría mayor señal de entrada o un amplificador con menor $F$ para comunicación aceptable.

### Fórmulas clave utilizadas
- $F = P_{n,out} / (G \cdot P_{n,in})$ — definición de figura de ruido
- $T_e = (F-1)T_0$ — relación ruido-temperatura
- $F_{total} = F_1 + (F_2-1)/G_1$ — [[../ruido/formula-friis|Friis]]
- $SNR_{out} = SNR_{in}/F$ — degradación de SNR

## Ver también

- [[../ruido/factor-ruido-temperatura]]
- [[../ruido/formula-friis]]
- [[../ruido/relacion-snr]]
- [[../ruido/fuentes-ruido]]
- [[../derivaciones/ecuacion-friis]]
- [[../ruido/ruido-termico]]
