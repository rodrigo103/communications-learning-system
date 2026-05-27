---
tags:
  - wiki/conceptos-integradores
source_file: explicaciones_anki/conceptos_integradores/carta_56_tradeoff_bw_potencia_shannon.md
curso: Sistemas de Comunicaciones
unidad: 9-10
---

# Compromisos Fundamentales de Diseno

> **Last verified:** 2025-11-16 | **Verified by:** source

## El Triangulo de Diseno

Todo sistema de comunicaciones enfrenta tres compromisos (trade-offs) fundamentales e inevitables, derivados del limite de Shannon: [source]

$$\boxed{C = B \log_2\left(1 + \frac{S}{N}\right)}$$

1. **Ancho de Banda vs Potencia**: recursos intercambiables pero con rendimientos diferentes
2. **Eficiencia Espectral vs Eficiencia de Potencia**: no se pueden maximizar simultaneamente
3. **Complejidad vs Desempeno**: acercarse al limite de Shannon requiere codificacion y procesamiento complejos

---

## 1. Trade-off Ancho de Banda — Potencia

La ecuacion de Shannon revela que $B$ y $S/N$ pueden intercambiarse:

$$\boxed{C = B \log_2\left(1 + \frac{S}{N}\right)}$$

### Alto SNR: priorizar BW

$$C \approx B \log_2(S/N)$$

- Duplicar BW duplica $C$ (lineal)
- Duplicar potencia: ganancia logaritmica minima
- Ejemplo: fibra optica (BW abundante, SNR alto) [analysis]

### Bajo SNR: intercambio flexible

$$C \approx 1.44 \cdot B \cdot \frac{S}{N}$$

- Ambos recursos igualmente valiosos
- Ejemplo: GPS (BW abundante, potencia extremadamente limitada)
- Spread spectrum: $G_p = BW_{SS}/BW_{info}$ intercambia BW por robustez

**Punto de equilibrio**: en $SNR \approx 1$ (0 dB), las derivadas parciales son iguales.

---

## 2. Trade-off Eficiencia Espectral — Eficiencia de Potencia

Relacion derivada de Shannon: [source]

$$\boxed{\frac{E_b}{N_0} = \frac{2^{\eta} - 1}{\eta}, \quad \eta = \frac{R_b}{B}}$$

Esto impone:

- **Alta $\eta_B$** $\Rightarrow$ alto $E_b/N_0$ requerido $\Rightarrow$ **baja eficiencia de potencia**
- **Alta $\eta_P$** $\Rightarrow$ bajo $E_b/N_0$ $\Rightarrow$ baja $\eta_B$

### Ejemplos extremos

| Sistema | Prioridad | $\eta_B$ | $E_b/N_0$ tipico |
|---------|-----------|----------|-------------------|
| Espacio profundo | Max $\eta_P$ | $<0.1$ | 2-3 dB |
| GPS | $\eta_P$ | $\sim 0.00002$ | Operacion bajo ruido |
| GSM (2G) | Balance | 1.35 | 8-10 dB |
| LTE | $\eta_B$ | 1.5-5 | 10-20 dB |
| Fibra optica | Max $\eta_B$ | 8+ | 20-25 dB |

### Limite Fundamental

$$\boxed{\lim_{\eta \to 0} \frac{E_b}{N_0} = \ln(2) \approx -1.59 \text{ dB}}$$

Ningun sistema, sin importar cuanto ancho de banda use, puede operar por debajo de -1.59 dB de $E_b/N_0$. [source]

---

## 3. Complejidad vs Desempeno

Acercarse al limite de Shannon requiere:
- **Codigos de bloque largos**: latencia proporcional a la longitud
- **Decodificacion iterativa**: Turbo y LDPC requieren multiples iteraciones
- **Procesamiento digital**: FFT para OFDM, correladores para CDMA

### Curva de rendimientos decrecientes

| Gap a Shannon | Tecnologia necesaria | Complejidad | Latencia |
|--------------|---------------------|-------------|----------|
| 8-10 dB | Codigos convolucionales simples | Baja | Baja |
| 3-5 dB | Turbo codes, LDPC | Media | Media |
| 1-2 dB | LDPC largos, Polar codes | Alta | Alta |
| $< 1$ dB | Codigos optimos teoricos | Extrema | Inviable |

Los sistemas practicos operan tipicamente a 1-3 dB del limite de Shannon. [analysis]

---

## 4. Regeneracion Digital vs Amplificacion Analogica

Compromiso fundamental en sistemas de larga distancia: [source]

### Amplificacion analogica

- Amplifica senal + ruido: $SNR_{out} < SNR_{in}$
- Degradacion acumulativa con cada etapa
- $SNR_{N} \approx SNR_{in} / (N \cdot F)$ para $N$ etapas con figura de ruido $F$

### Regeneracion digital

- Decide bits discretos (0 o 1), regenera pulso limpio
- **Ruido no acumulativo**: si $SNR >$ umbral en cada seccion
- $BER_{total} \approx N \cdot BER_{seccion}$ (lineal en probabilidad, no en amplitud)
- Permite distancias ilimitadas con suficiente cantidad de regeneradores

| Aspecto | Analogico | Digital |
|---------|-----------|---------|
| Ruido | Acumulativo | No acumulativo |
| Distancia | Limitada | Ilimitada (con regeneradores) |
| SNR minimo | Funciona con muy bajo | Requiere umbral |
| Complejidad | Baja | Alta |
| Costo | Bajo | Alto (hardware) |

### Implicacion de Diseno

La regeneracion digital explica por que:
- Los cables submarinos de fibra optica pueden cruzar oceanos
- Las comunicaciones espaciales (Voyager) son viables
- Las redes celulares modernas usan backhaul digital

---

## 5. Relacion $E_b/N_0$ vs SNR

Conversion fundamental para diseno: [source]

$$\boxed{\frac{E_b}{N_0} = SNR \cdot \frac{B}{R_b}}$$

En dB: $(E_b/N_0)_{dB} = SNR_{dB} + 10\log_{10}(B/R_b)$

- **SNR**: mide potencia total en el ancho de banda — natural para pensar en amplificadores y ruido
- **$E_b/N_0$**: normalizado por tasa de bits — permite comparacion justa entre sistemas con diferentes velocidades

Para modulacion M-aria con $B \approx R_s$: $SNR \approx \frac{E_b}{N_0} \cdot \log_2(M)$.

---

## Resumen de Decisiones de Diseno

| Si el recurso limitante es... | Entonces priorizar... | mediante... |
|------------------------------|----------------------|-------------|
| Espectro | Eficiencia espectral | QAM alto orden, MIMO |
| Potencia | Eficiencia de potencia | Spread spectrum, codigos potentes |
| Ambos | Adaptacion | AMC (LTE, 5G, WiFi) |
| Costo | Simplicidad | GMSK, FSK, esquemas no coherentes |
| Latencia | Codigos cortos | Codigos de bloque, no convolucionales |

## Errores Comunes

- Optimizar solo una metrica ignorando las demas
- No considerar el regimen de operacion (alto vs bajo SNR) al elegir estrategia
- Asumir que mas regeneradores siempre es mejor (costo, latencia, complejidad)
- Usar $E_b/N_0$ para sistemas analogicos (no tiene sentido sin "bits")

## Ver tambien

- [[conceptos-integradores/comparacion-global-modulaciones]]
- [[conceptos-integradores/seleccion-modulacion]]
- [[conceptos-integradores/aplicaciones-reales]]
- [[ruido/intercomparacion-sistemas]]
- [[teoria-informacion/teorema-shannon-hartley]]
- [[conceptos-integradores/evolucion-sistemas]]
