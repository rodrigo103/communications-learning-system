---
tags:
  - wiki/derivaciones
  - wiki/ruido
source_file: outputs/derivations/Friis_Cascade_20251115.md
curso: Sistemas de Comunicaciones
unidad: 7
---

# Derivación de la Fórmula de Friis para Cascada

> **Last verified:** 2025-11-15 | **Verified by:** source

## Definiciones previas

### Figura de ruido (Noise Figure)

La figura de ruido cuantifica cuánto degrada un dispositivo la SNR:

$$F = \frac{SNR_{in}}{SNR_{out}} = \frac{N_{out}}{G \cdot N_{in}}$$

- $F = 1$ (0 dB): dispositivo ideal sin ruido añadido
- $F > 1$: el dispositivo añade ruido, degradando la SNR [source — [[../../outputs/derivations/Friis_Cascade_20251115]]]

### Ruido añadido por una etapa

A partir de la definición de $F$:

$$\boxed{N_{added,1} = N_1 G_1 (F_1 - 1)}$$

## Derivación para dos etapas

Consideremos dos etapas en cascada con ganancias $G_1, G_2$ y figuras de ruido $F_1, F_2$.

### Salida de etapa 1

$$S_2 = G_1 S_1$$
$$N_2 = G_1 N_1 + N_{added,1} = G_1 N_1 F_1$$

### Salida de etapa 2

El ruido añadido por la etapa 2, referido a su entrada:

$$N_{added,2} = G_2 \cdot (G_1 N_1) \cdot (F_2 - 1)$$

**Punto clave:** El ruido añadido por la etapa 2 depende de la potencia de ruido térmico a su entrada ($G_1 N_1$), no del ruido total ($G_1 N_1 F_1$) [analysis].

Ruido total a la salida:

$$N_3 = \underbrace{G_1 G_2 N_1}_{\text{ruido térmico amplificado}} + \underbrace{G_2 G_1 N_1(F_1 - 1)}_{\text{ruido etapa 1 amplificado}} + \underbrace{G_2 G_1 N_1 (F_2 - 1)}_{\text{ruido añadido etapa 2}}$$

### Figura de ruido total

$$F_{total} = \frac{N_3}{G_1 G_2 N_1} = 1 + (F_1 - 1) + (F_2 - 1)$$

**¡Incorrecto!** El ruido de la etapa 2 debe referirse a la entrada del sistema, dividiendo por $G_1$:

$$F_{total} = F_1 + \frac{F_2 - 1}{G_1}$$

$$\boxed{F_{total} = F_1 + \frac{F_2 - 1}{G_1}}$$

## Generalización a N etapas

$$\boxed{F_{total} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots + \frac{F_N - 1}{\prod_{i=1}^{N-1} G_i}}$$

Forma compacta:

$$\boxed{F_{total} = F_1 + \sum_{n=2}^{N} \frac{F_n - 1}{\prod_{i=1}^{n-1} G_i}}$$

### Versión en temperatura de ruido

$$T_{total} = T_1 + \frac{T_2}{G_1} + \frac{T_3}{G_1 G_2} + \cdots$$

donde $T_e = T_0(F - 1)$ [source — [[../../outputs/derivations/Friis_Cascade_20251115]]].

## Interpretación física

### La primera etapa domina

Cada etapa subsiguiente ve su contribución dividida por la ganancia acumulada de las etapas anteriores. Si $G_1$ es grande, el término $(F_2 - 1)/G_1$ se vuelve insignificante [analysis].

### Ejemplo numérico

| Etapa | F (lin) | G (lin) | Contribución a F_total |
|-------|---------|---------|------------------------|
| 1 (LNA) | 1.5 | 100 | 1.500 (95.4%) |
| 2 (Mixer) | 8 | 10 | 0.070 (4.5%) |
| 3 (IF Amp) | 3 | 1000 | 0.002 (0.1%) |
| **Total** | | | **1.572** |

## Reglas de diseño

1. **Invertir en la primera etapa:** LNA con bajo $F_1$ y alta $G_1$
2. **Nunca atenuar antes de amplificar:** una atenuación $L$ antes del LNA multiplica $F_{total}$ por $L$
3. **LNA cerca de la antena:** minimizar pérdidas de cable antes de la primera amplificación
4. **Etapas posteriores:** pueden ser más económicas y ruidosas

Precaución: La fórmula de Friis usa valores **lineales** (no dB). Convertir siempre antes de aplicar [analysis].

## Ver también

- [[../ruido/formula-friis]]
- [[../ruido/factor-ruido-temperatura]]
- [[../ruido/relacion-snr]]
- [[../ruido/fuentes-ruido]]
- [[../ruido/ruido-termico]]
- [[../ruido/lna-diseno-receptor]]
