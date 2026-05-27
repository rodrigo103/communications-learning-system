---
tags:
  - wiki/derivaciones
  - wiki/ruido
source_file: outputs/derivations/Friis_Cascade_parallel_20251115.md
curso: Sistemas de Comunicaciones
unidad: 7
---

# Ecuación de Friis — Derivación Extendida

> **Last verified:** 2025-11-15 | **Verified by:** [source — [[../../outputs/derivations/Friis_Cascade_parallel_20251115]]]

**Versión extendida** de la derivación canónica de la fórmula de Friis para ruido en cascada. Complementa [[ecuacion-friis]] con dos enfoques de derivación, múltiples ejemplos numéricos, reglas de diseño prácticas y análisis de temperatura de ruido.

---

## Definición fundamental de figura de ruido [source]

$$F = \frac{\text{SNR}_{\text{in}}}{\text{SNR}_{\text{out}}}$$

Un componente ideal tiene $F = 1$ (0 dB); componentes reales tienen $F > 1$ [source].

### En función de potencia [source]

$$F = \frac{P_{N,\text{out}}}{G \cdot P_{N,\text{in}}}$$

### Ruido añadido [source]

$$P_{N,\text{out}} = G \cdot P_{N,\text{in}} + P_{N,\text{added}}$$

$$F = 1 + \frac{P_{N,\text{added}}}{G \cdot P_{N,\text{in}}}$$

Referencia estándar [source]: $P_{N,\text{in}} = kT_0B$ con $k = 1.38 \times 10^{-23}$ J/K, $T_0 = 290$ K.

**Ruido añadido referido a la entrada** [source]:

$$N_{\text{added, input-referred}} = (F-1) \cdot kT_0B$$

---

## Derivación: dos etapas [source]

Sistema: Etapa 1 ($G_1, F_1$) $\to$ Etapa 2 ($G_2, F_2$)

Señal a la salida [source]:

$$S_{\text{out}} = G_1 G_2 \cdot S_{\text{in}}$$

Ruido a la salida [source]:

$$N_{\text{out}} = G_2 \cdot (F_1 G_1 kT_0B) + (F_2 - 1) G_2 kT_0B$$

$$N_{\text{out}} = G_1 G_2 kT_0B \left[F_1 + \frac{F_2 - 1}{G_1}\right]$$

Figura de ruido total [source]:

$$\boxed{F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1}}$$

---

## Generalización a N etapas [source]

### Tres etapas

$$F_{123} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2}$$

### N etapas

$$\boxed{F_{\text{total}} = F_1 + \sum_{i=2}^{N} \frac{F_i - 1}{\prod_{j=1}^{i-1} G_j}}$$

Demostración por inducción incluida en la fuente [source].

---

## Forma en temperatura de ruido [source]

Relación temperatura-figura de ruido [source]:

$$T_e = (F - 1) \cdot T_0 \quad \Longleftrightarrow \quad F = 1 + \frac{T_e}{T_0}$$

### Cascada en temperatura [source]

$$\boxed{T_{e,\text{total}} = T_{e,1} + \frac{T_{e,2}}{G_1} + \frac{T_{e,3}}{G_1 G_2} + \cdots}$$

---

## Por qué domina la primera etapa [source]

$$F_{\text{total}} = \underbrace{F_1}_{\text{impacto total}} + \underbrace{\frac{F_2-1}{G_1}}_{\text{reducido por } G_1} + \underbrace{\frac{F_3-1}{G_1 G_2}}_{\text{reducido por } G_1 G_2} + \cdots$$

**Analogía** [source]: Gritar en una sala ruidosa — si la etapa 1 amplifica fuertemente, la señal ya es mucho más fuerte que cualquier ruido nuevo añadido por etapas posteriores.

---

## Ejemplo numérico: receptor de tres etapas [source]

| Etapa | Componente | Ganancia (dB) | Ganancia (lineal) | NF (dB) | NF (lineal) |
|-------|-----------|--------------|-------------------|---------|-------------|
| 1 | LNA | 20 dB | 100 | 1.5 dB | 1.41 |
| 2 | Mixer | -6 dB | 0.25 | 8 dB | 6.31 |
| 3 | IF Amp | 30 dB | 1000 | 3 dB | 2.00 |

$$F_{\text{total}} = 1.41 + \frac{5.31}{100} + \frac{1.00}{25} = 1.5031 \text{ (1.77 dB)}$$

| Etapa | Término | Valor | Contribución |
|-------|---------|-------|-------------|
| 1 | $F_1$ | 1.4100 | 93.8% |
| 2 | $(F_2-1)/G_1$ | 0.0531 | 3.5% |
| 3 | $(F_3-1)/(G_1 G_2)$ | 0.0400 | 2.7% |

---

## Reglas de diseño [source]

### Regla de los 20 dB

Si $G_1 \geq 100$ (20 dB) y $F_2 \approx 6$ [source]:

$$\frac{F_2-1}{G_1} = \frac{5}{100} = 0.05$$

Esto añade solo ~0.22 dB a $F_{\text{total}}$ [analysis]. Conclusión: la NF del sistema $\approx$ NF del LNA.

### Posicionamiento del LNA [source]

- **LNA después del mixer** $\to F = 6 + 0.41/0.25 = 7.64$ (8.8 dB) — MAL
- **LNA antes del mixer** $\to F = 1.41 + 5/100 = 1.46$ (1.6 dB) — BIEN

**Conclusión**: siempre colocar LNA primero, lo más cerca posible de la antena [source].

### Pérdidas antes del LNA [source]

Cualquier pérdida antes del LNA (cables, filtros) se suma directamente a la NF del sistema:

$$F_{\text{filter}} = \frac{1}{G_{\text{filter}}} = L_{\text{insertion}}$$

Ejemplo: filtro con 1 dB de pérdida de inserción $\to$ 1 dB de NF, que con LNA posterior da $F_{\text{total}} = 1.78$ (2.5 dB) vs. 1.77 dB sin el filtro [source].

---

## Ejemplo real: receptor GPS L1 [source]

Sistema típico con antena, cable, filtro SAW, LNA, mixer, amplificador FI.

NF del sistema: ~4.5 dB (dominada por pérdidas de antena y filtro) [source].

**Mejora**: antena activa (LNA en la antena, antes del cable) reduce NF a ~1.5 dB [source].

---

## Lo que aporta esta versión

Respecto a la derivación canónica en [[ecuacion-friis]], esta versión extendida añade [analysis]:

- **Dos enfoques de derivación**: desde degradación de SNR y desde modelo de ruido referido a la entrada
- **Derivación completa a dos etapas** antes de generalizar a N, con cada paso algebraico explícito
- **Demostración por inducción** de la fórmula de N etapas
- **Forma en temperatura de ruido** ($T_e$) con ejemplos de conversión entre $F$ y $T_e$
- **Ejemplo criogénico**: telescopio con LNA a 20 K, $T_{e,\text{sys}} = 5.15$ K, $F = 0.08$ dB
- **Múltiples escenarios numéricos**: LNA bueno vs. barato, ganancia alta vs. baja, filtro antes vs. después
- **Análisis de contribución porcentual** por etapa
- **Regla práctica de los 20 dB** con justificación matemática
- **Reglas de diseño explícitas**: maximizar $G_1$, minimizar $F_1$, minimizar pérdidas pre-LNA, colocar LNA junto a la antena
- **Técnicas avanzadas**: enfriamiento criogénico, amplificadores balanceados, amplificación distribuida
- **Caso real de receptor GPS** con cálculo completo
- **Perspectiva histórica**: referencia al paper original de Harald T. Friis (1944, Proceedings of the IRE) [source]

---

## Ver también

- [[ecuacion-friis]] — Derivación canónica de Friis
- [[../ruido/formula-friis]] — Fórmula de Friis (concepto)
- [[../ruido/factor-ruido-temperatura]] — Factor de ruido y temperatura
- [[../ruido/relacion-snr]] — Relación Señal a Ruido
- [[../ruido/lna-diseno-receptor]] — Diseño de receptor
- [[../ruido/ruido-termico]] — Ruido térmico
