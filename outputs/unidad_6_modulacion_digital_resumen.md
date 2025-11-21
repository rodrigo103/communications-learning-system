# Unidad 6: Modulación Digital - Resumen Completo

**Documento**: Resumen independiente de la Unidad 6
**Fecha**: 2025-11-21
**Curso**: Sistemas de Comunicaciones (UTN)
**Objetivo**: Explicación concisa y clara con derivaciones paso a paso

---

## Índice

1. [Introducción](#1-introducción)
2. [Fundamentos Teóricos](#2-fundamentos-teóricos)
3. [Técnicas de Modulación](#3-técnicas-de-modulación)
4. [Análisis de Desempeño](#4-análisis-de-desempeño)
5. [Conformación de Pulsos e ISI](#5-conformación-de-pulsos-e-isi)
6. [Implementación](#6-implementación)
7. [Aplicaciones](#7-aplicaciones)
8. [Comparaciones y Trade-offs](#8-comparaciones-y-trade-offs)

---

## 1. Introducción

### ¿Qué es la Modulación Digital?

La modulación digital es el proceso de **codificar información digital (bits) en señales analógicas** para su transmisión a través de un canal de comunicación. A diferencia de la modulación analógica (Unidades 3-4), aquí el mensaje original es discreto (secuencia de bits).

### ¿Por qué es importante?

En la era digital, prácticamente todas las comunicaciones modernas usan modulación digital:
- **WiFi, 4G/5G**: transmisión de datos inalámbrica
- **TV Digital, Radio DAB**: broadcasting digital
- **Satélites, enlaces de fibra óptica**: comunicaciones de larga distancia

### Concepto Clave: Símbolo vs Bit

- **Bit**: Unidad mínima de información (0 o 1)
- **Símbolo**: Estado físico distinguible de la señal que puede representar múltiples bits

**Ejemplo**: En QPSK, cada símbolo representa 2 bits (00, 01, 10, 11)

---

## 2. Fundamentos Teóricos

### 2.1 Representación en Espacio de Señales

**Prerequisito**: Conocimiento de series de Fourier (Unidad 2) y señales ortogonales

Cualquier señal de duración finita puede expresarse como combinación lineal de funciones base ortogonales:

$$s(t) = \sum_{n=1}^{N} a_n \phi_n(t)$$

donde:
- $\phi_n(t)$: funciones base ortonormales
- $a_n$: coeficientes (determinan el símbolo transmitido)
- $N$: dimensionalidad del espacio de señales

**Condición de ortonormalidad**:
$$\langle \phi_i, \phi_j \rangle = \int_{0}^{T} \phi_i(t)\phi_j(t)dt = \delta_{ij} = \begin{cases} 1 & i=j \\ 0 & i \neq j \end{cases}$$

### 2.2 Diagramas de Constelación

Un **diagrama de constelación** es la representación gráfica de todos los símbolos posibles en el plano complejo (I-Q).

**Representación compleja de señal modulada**:
$$s(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)$$

En banda base equivalente:
$$\tilde{s}(t) = I(t) + jQ(t) = A(t)e^{j\phi(t)}$$

donde:
- **I(t)**: componente en fase (In-phase)
- **Q(t)**: componente en cuadratura (Quadrature)
- **A(t)**: amplitud instantánea
- **φ(t)**: fase instantánea

**Propiedades importantes**:
1. **Distancia euclidiana entre símbolos**:
   $$d_{ij} = |s_i - s_j| = \sqrt{(I_i - I_j)^2 + (Q_i - Q_j)^2}$$

2. **Distancia mínima** (determina robustez ante ruido):
   $$d_{min} = \min_{i \neq j} d_{ij}$$

3. **Energía promedio por símbolo**:
   $$E_s = \frac{1}{M}\sum_{k=1}^{M} (I_k^2 + Q_k^2)$$

### 2.3 Filtro Adaptado (Matched Filter)

**Teorema**: Para maximizar la SNR en presencia de ruido blanco gaussiano (AWGN), el filtro óptimo del receptor es el **adaptado a la señal transmitida**.

**Respuesta impulsiva del filtro adaptado**:
$$h(t) = s^*(T - t)$$

donde $s(t)$ es la señal transmitida y $T$ es la duración del símbolo.

**SNR máxima alcanzada**:
$$\text{SNR}_{max} = \frac{2E_s}{N_0}$$

donde:
- $E_s$: energía del símbolo
- $N_0$: densidad espectral de potencia del ruido

### 2.4 Criterio de Nyquist

**Prerequisito**: Teorema del muestreo (Unidad 5)

Para transmisión sin interferencia intersimbólica (ISI), el pulso debe satisfacer:

$$p(nT_s) = \begin{cases} 1 & n=0 \\ 0 & n \neq 0 \end{cases}$$

**Ancho de banda mínimo de Nyquist**:
$$B_{min} = \frac{R_s}{2} = \frac{1}{2T_s}$$

donde $R_s$ es la velocidad de señalización (símbolos/segundo).

---

## 3. Técnicas de Modulación

### 3.1 ASK (Amplitude Shift Keying)

Modula la **amplitud** de la portadora según los datos.

#### ASK Binaria (OOK - On-Off Keying)

$$s_0(t) = 0 \quad \text{(bit 0)}$$
$$s_1(t) = A\cos(2\pi f_c t) \quad \text{(bit 1)}$$

**Ventajas**: Implementación muy simple
**Desventajas**: Muy susceptible a ruido, pobre eficiencia energética

#### M-ASK

Con M niveles de amplitud:
$$s_k(t) = A_k\cos(2\pi f_c t), \quad k = 0, 1, ..., M-1$$

**Bits por símbolo**: $\log_2(M)$

### 3.2 FSK (Frequency Shift Keying)

Modula la **frecuencia** de la portadora según los datos.

#### FSK Binaria (BFSK)

$$s_0(t) = A\cos(2\pi f_0 t) \quad \text{(bit 0)}$$
$$s_1(t) = A\cos(2\pi f_1 t) \quad \text{(bit 1)}$$

**Separación de frecuencias**: $\Delta f = f_1 - f_0$

**Condición de ortogonalidad**:
$$\Delta f = \frac{n}{2T_b}, \quad n \in \mathbb{Z}^+$$

#### Variantes Importantes

**MSK (Minimum Shift Keying)**:
- Separación mínima: $\Delta f = \frac{1}{4T_b}$
- Fase continua (mejor espectro)
- Envolvente constante

**GMSK (Gaussian MSK)**:
- MSK con filtro gaussiano previo
- Usado en GSM
- Parámetro BT (ancho de banda × duración de bit)

**Ventajas de FSK**:
- Envolvente constante (amplificadores no lineales OK)
- Buena inmunidad al ruido

**Desventajas**:
- Ancho de banda mayor que PSK/QAM

### 3.3 PSK (Phase Shift Keying)

Modula la **fase** de la portadora según los datos.

#### BPSK (Binary PSK)

La modulación binaria más robusta:

$$s_0(t) = A\cos(2\pi f_c t) \quad \text{(bit 0)}$$
$$s_1(t) = -A\cos(2\pi f_c t) = A\cos(2\pi f_c t + \pi) \quad \text{(bit 1)}$$

**Diferencia de fase**: $\Delta\phi = \pi$ radianes

**Representación en constelación**: 2 puntos en el eje I en $(\pm A, 0)$

#### QPSK (Quadrature PSK)

Dobla la eficiencia espectral de BPSK:

$$s(t) = A\cos(2\pi f_c t + \phi_k), \quad \phi_k \in \{\frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}\}$$

**Representación alternativa I-Q**:
$$s(t) = \frac{A}{\sqrt{2}}\cos(2\pi f_c t) \pm \frac{A}{\sqrt{2}}\sin(2\pi f_c t)$$

**Bits por símbolo**: 2 bits
**Velocidad de símbolo**: $R_s = \frac{R_b}{2}$ (donde $R_b$ es la tasa de bits)

**Constelación**: 4 puntos en las esquinas de un cuadrado

**Derivación de coordenadas QPSK**:

Para energía promedio unitaria ($E_s = 1$):
$$E_s = \frac{1}{4}\sum_{k=1}^{4}(I_k^2 + Q_k^2) = 1$$

Con simetría, $I_k = \pm a$, $Q_k = \pm a$:
$$E_s = \frac{1}{4}[4(a^2 + a^2)] = 2a^2 = 1$$
$$\boxed{a = \frac{1}{\sqrt{2}} \approx 0.707}$$

#### M-PSK

Con M fases uniformemente espaciadas:
$$\phi_k = \frac{2\pi k}{M}, \quad k = 0, 1, ..., M-1$$

**Ejemplos comunes**:
- 8-PSK: 8 fases, 3 bits/símbolo
- 16-PSK: 16 fases, 4 bits/símbolo (rara vez usado, QAM es mejor)

**Ventajas de PSK**:
- Excelente eficiencia energética
- Envolvente constante (BPSK, QPSK, 8-PSK)

**Desventajas**:
- Requiere detección coherente (recuperación de portadora)

### 3.4 QAM (Quadrature Amplitude Modulation)

**La técnica más usada en comunicaciones modernas** porque combina:
- Modulación de amplitud (ASK)
- Modulación de fase (PSK)

#### Señal QAM General

$$s(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)$$

donde $I(t)$ y $Q(t)$ toman valores discretos.

#### Derivación de Eficiencia Espectral

Para M-QAM:
$$M = 2^k \quad \Rightarrow \quad k = \log_2(M) \text{ bits/símbolo}$$

**Tasa de bits**:
$$R_b = R_s \cdot \log_2(M)$$

**Ancho de banda mínimo** (criterio de Nyquist):
$$B_{min} = \frac{R_s}{2}$$

**Eficiencia espectral ideal**:
$$\boxed{\eta = \frac{R_b}{B} = 2\log_2(M) \text{ bits/s/Hz}}$$

Con pulsos de coseno realzado (factor de roll-off $\alpha$):
$$\eta_{real} = \frac{2\log_2(M)}{1+\alpha} \text{ bits/s/Hz}$$

#### Ejemplos de QAM

**16-QAM**:
- 16 puntos en grilla 4×4
- 4 bits/símbolo
- $\eta \approx 4$ bits/s/Hz (con $\alpha=0$)
- Aplicaciones: cable modems, DVB-C

**64-QAM**:
- 64 puntos en grilla 8×8
- 6 bits/símbolo
- $\eta \approx 6$ bits/s/Hz
- Aplicaciones: WiFi 802.11a/g/n, LTE

**256-QAM**:
- 256 puntos en grilla 16×16
- 8 bits/símbolo
- $\eta \approx 8$ bits/s/Hz
- Aplicaciones: WiFi 802.11ac, LTE-Advanced

**1024-QAM**:
- 1024 puntos
- 10 bits/símbolo
- $\eta \approx 10$ bits/s/Hz
- Aplicaciones: WiFi 6 (802.11ax), 5G

**Ventajas de QAM**:
- Máxima eficiencia espectral
- Adaptabilidad (ajustar M según el canal)

**Desventajas**:
- Envolvente variable (requiere amplificador lineal)
- Sensible al ruido (especialmente con M grande)

---

## 4. Análisis de Desempeño

### 4.1 Relación Eb/N0

**Prerequisito**: Conceptos de ruido (Unidad 7)

$$E_b = \frac{E_s}{\log_2(M)} = \frac{P_{avg} \cdot T_s}{\log_2(M)}$$

donde:
- $E_b$: energía por bit
- $E_s$: energía por símbolo
- $P_{avg}$: potencia promedio transmitida
- $T_s$: duración del símbolo

$$N_0 = \text{densidad espectral de potencia del ruido (W/Hz)}$$

### 4.2 Probabilidad de Error de Bit (BER)

La **función Q** aparece en todos los cálculos de BER:
$$Q(x) = \frac{1}{\sqrt{2\pi}}\int_{x}^{\infty} e^{-t^2/2}dt$$

**Aproximaciones útiles**:
- $Q(3) \approx 1.35 \times 10^{-3}$
- $Q(4) \approx 3.17 \times 10^{-5}$
- $Q(5) \approx 2.87 \times 10^{-7}$
- $Q(6) \approx 9.87 \times 10^{-10}$

#### BER para Modulaciones Comunes

**BPSK (detección coherente)**:
$$\boxed{P_e = Q\left(\sqrt{\frac{2E_b}{N_0}}\right)}$$

**Derivación**:
1. BPSK transmite $s_0 = -\sqrt{E_s}$ o $s_1 = +\sqrt{E_s}$
2. Con ruido AWGN: $r = s + n$ donde $n \sim \mathcal{N}(0, N_0/2)$
3. Criterio de decisión: si $r > 0 \Rightarrow$ decide $s_1$
4. Error ocurre si:
   - Transmite $s_1 = \sqrt{E_s}$ pero $r < 0$
   - Probabilidad: $P(n < -\sqrt{E_s})$
5. Estandarizando:
   $$P_e = P\left(\frac{n}{\sqrt{N_0/2}} < -\frac{\sqrt{E_s}}{\sqrt{N_0/2}}\right) = Q\left(\sqrt{\frac{2E_s}{N_0}}\right)$$
6. Para BPSK: $E_s = E_b$ (1 bit/símbolo)

**QPSK (detección coherente)**:
$$\boxed{P_e \approx Q\left(\sqrt{\frac{2E_b}{N_0}}\right)}$$

Nota: ¡Misma que BPSK! Esto es porque QPSK puede verse como dos canales BPSK ortogonales.

**FSK Binaria (coherente)**:
$$\boxed{P_e = Q\left(\sqrt{\frac{E_b}{N_0}}\right)}$$

**FSK Binaria (no coherente)**:
$$\boxed{P_e = \frac{1}{2}e^{-E_b/(2N_0)}}$$

**M-PSK General**:
$$P_e \approx \frac{2}{\log_2(M)}Q\left(\sqrt{2\frac{E_b}{N_0}\log_2(M)}\sin\frac{\pi}{M}\right)$$

**M-QAM Cuadrada (M=2^k, k par)**:
$$P_e \approx \frac{4}{\log_2(M)}\left(1 - \frac{1}{\sqrt{M}}\right)Q\left(\sqrt{\frac{3\log_2(M)}{M-1}\frac{E_b}{N_0}}\right)$$

### 4.3 Eficiencia Espectral

$$\eta = \frac{R_b}{B} \text{ (bits/s/Hz)}$$

**Valores típicos con coseno realzado** ($\alpha = 0.5$):
- BPSK: $\eta \approx 0.67$ bits/s/Hz
- QPSK: $\eta \approx 1.33$ bits/s/Hz
- 8-PSK: $\eta \approx 2$ bits/s/Hz
- 16-QAM: $\eta \approx 2.67$ bits/s/Hz
- 64-QAM: $\eta \approx 4$ bits/s/Hz
- 256-QAM: $\eta \approx 5.33$ bits/s/Hz

### 4.4 Eficiencia Energética

Valores aproximados de $E_b/N_0$ requeridos para $BER = 10^{-5}$:

| Modulación | $E_b/N_0$ (dB) | Comentario |
|------------|----------------|------------|
| BPSK | 9.6 | Óptimo |
| QPSK | 9.6 | Igual que BPSK |
| 8-PSK | 14 | Penalidad 4.4 dB |
| 16-QAM | 14.5 | Similar a 8-PSK |
| 64-QAM | 18.5 | Penalidad 8.9 dB |
| 256-QAM | 23 | Penalidad 13.4 dB |

**Trade-off fundamental**:
- Mayor M → Mayor eficiencia espectral → Peor eficiencia energética

---

## 5. Conformación de Pulsos e ISI

### 5.1 Interferencia Intersimbólica (ISI)

**Definición**: Superposición indeseada entre símbolos consecutivos debido a:
1. Limitación de ancho de banda del canal
2. Propagación multitrayecto
3. Filtros no ideales

**Efecto**: Degrada la BER, cierra el "ojo" en diagramas de ojo.

### 5.2 Pulso Nyquist Ideal

$$p(t) = \text{sinc}\left(\frac{t}{T_s}\right) = \frac{\sin(\pi t/T_s)}{\pi t/T_s}$$

**Propiedades**:
- Cruces por cero en $t = nT_s$ para $n \neq 0$
- Ancho de banda: $B = \frac{1}{2T_s}$ (mínimo de Nyquist)

**Problema**: No realizable (duración infinita, no causal)

### 5.3 Filtro de Coseno Realzado (Raised Cosine)

**Respuesta en frecuencia**:

$$H_{RC}(f) = \begin{cases}
T_s & |f| \leq \frac{1-\alpha}{2T_s} \\
\frac{T_s}{2}\left[1 + \cos\left(\frac{\pi T_s}{\alpha}\left(|f| - \frac{1-\alpha}{2T_s}\right)\right)\right] & \frac{1-\alpha}{2T_s} < |f| \leq \frac{1+\alpha}{2T_s} \\
0 & |f| > \frac{1+\alpha}{2T_s}
\end{cases}$$

**Respuesta temporal**:
$$p_{RC}(t) = \text{sinc}\left(\frac{t}{T_s}\right) \cdot \frac{\cos(\pi\alpha t/T_s)}{1 - (2\alpha t/T_s)^2}$$

**Factor de roll-off** $\alpha \in [0, 1]$:
- $\alpha = 0$: Filtro Nyquist ideal (no realizable)
- $\alpha = 0.5$: Compromiso típico
- $\alpha = 1$: Transición más suave (más ancho de banda)

**Ancho de banda**:
$$\boxed{B = \frac{1 + \alpha}{2T_s} = \frac{R_s(1+\alpha)}{2}}$$

**Propiedad clave**: Mantiene cruces por cero en $t = nT_s$ para todo $\alpha$.

### 5.4 Filtro de Raíz de Coseno Realzado (Root Raised Cosine - RRC)

**Idea**: Dividir la conformación entre transmisor y receptor:
$$H_{RC}(f) = |H_{RRC}(f)|^2$$

**Ventajas**:
1. El filtro adaptado del receptor se combina con RRC del transmisor
2. Minimiza potencia pico
3. Sistema total tiene respuesta de coseno realzado

**Implementación práctica**: RRC en TX y RRC en RX

### 5.5 Diagramas de Ojo

**Definición**: Superposición de múltiples períodos de símbolo en un osciloscopio.

**Interpretaciones**:
- **Apertura vertical**: Margen de ruido
- **Apertura horizontal**: Margen de timing (jitter)
- **Ojo cerrado**: Alta ISI o ruido
- **Ojo abierto**: Buena calidad de señal

**Punto óptimo de muestreo**: Centro del ojo (máxima apertura)

---

## 6. Implementación

### 6.1 Transmisor I-Q

**Diagrama de bloques**:
```
Bits → Serial/Paralelo → Mapeo → División I/Q → DAC → Filtros → Modulador I-Q → RF
                                       ↓                              ↑
                                    Símbolos                     Oscilador Local
```

**Proceso**:
1. **Bits seriales** se convierten en paralelo
2. **Mapeo**: Grupos de bits → símbolos (coordenadas I, Q)
3. **DAC**: Digital → Analógico
4. **Filtros conformadores** (típicamente RRC)
5. **Modulador I-Q**:
   $$s(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)$$

### 6.2 Receptor Coherente

**Diagrama de bloques**:
```
RF → Demodulador I-Q → Filtros → ADC → Muestreo → Decisión → Bits
        ↑                                   ↑
   Recuperación                      Recuperación
   de Portadora                      de Reloj
```

**Proceso**:
1. **Demodulación I-Q**: Multiplica por $\cos(2\pi f_c t)$ y $\sin(2\pi f_c t)$
2. **Filtros adaptados** (RRC)
3. **ADC**: Analógico → Digital
4. **Muestreo**: En instantes óptimos
5. **Decisión**: Mapeo de símbolos recibidos a bits

### 6.3 Sincronización

#### Recuperación de Portadora

**Técnicas**:
1. **Lazo de Costas**: Para BPSK, QPSK
2. **Squaring loop**: Elimina modulación elevando al cuadrado
3. **Decision-directed**: Usa símbolos decididos para estimar error de fase
4. **Tono piloto**: Transmite referencia de frecuencia conocida

#### Recuperación de Reloj (Symbol Timing)

**Algoritmos comunes**:
1. **Early-Late Gate**: Compara muestras antes y después del punto óptimo
2. **Gardner**: No requiere sincronización previa
3. **Mueller-Müller**: Decision-directed

### 6.4 Imperfecciones Típicas

**Desbalance I-Q**:
- Ganancia: $A_I \neq A_Q$
- Fase: $\phi \neq 90°$ (no perfectamente ortogonales)
- Resultado: Constelación distorsionada (elíptica)

**Offset de Frecuencia**:
- Causa: Diferencia entre osciladores TX y RX
- Efecto: Constelación rota en el tiempo

**Ruido de Fase**:
- Causa: Inestabilidad del oscilador local
- Efecto: Nube difusa en la constelación

---

## 7. Aplicaciones

### 7.1 WiFi (802.11)

| Estándar | Año | Modulación | Tasa máxima | Banda |
|----------|-----|------------|-------------|-------|
| 802.11b | 1999 | BPSK, QPSK | 11 Mbps | 2.4 GHz |
| 802.11a/g | 2003 | hasta 64-QAM | 54 Mbps | 2.4/5 GHz |
| 802.11n | 2009 | hasta 64-QAM | 600 Mbps | 2.4/5 GHz |
| 802.11ac | 2013 | hasta 256-QAM | 6.9 Gbps | 5 GHz |
| 802.11ax (WiFi 6) | 2019 | hasta 1024-QAM | 9.6 Gbps | 2.4/5 GHz |

**Modulación Adaptativa**: Ajusta M según calidad del enlace (SNR)

### 7.2 Redes Celulares

**4G LTE**:
- Downlink: hasta 256-QAM
- Uplink: hasta 64-QAM
- OFDMA: Múltiples subportadoras, cada una con QAM

**5G NR**:
- Hasta 256-QAM (puede llegar a 1024-QAM en condiciones ideales)
- Bandas de frecuencia: sub-6 GHz y mmWave (24-100 GHz)
- Massive MIMO

### 7.3 Comunicaciones por Cable

**DOCSIS (Cable Modems)**:
- DOCSIS 3.0: hasta 256-QAM
- DOCSIS 3.1: hasta 4096-QAM
- DOCSIS 4.0: hasta 16384-QAM (en desarrollo)

**DVB-C (TV Digital por Cable)**:
- 16-QAM, 64-QAM, 256-QAM

### 7.4 Comunicaciones Satelitales

**DVB-S (Satélites)**:
- DVB-S: QPSK
- DVB-S2: 8-PSK, 16-APSK, 32-APSK

**Espacio Profundo**:
- BPSK (máxima robustez para SNR extremadamente bajo)

### 7.5 Bluetooth

- **Bluetooth Classic**: GFSK (Gaussian FSK)
- **Bluetooth Enhanced Data Rate**: π/4-DQPSK, 8-DPSK

---

## 8. Comparaciones y Trade-offs

### 8.1 Comparación de Modulaciones

| Modulación | Eficiencia Espectral | Eficiencia Energética | Envolvente | Complejidad | Aplicación Típica |
|------------|----------------------|-----------------------|------------|-------------|-------------------|
| BPSK | ⭐ | ⭐⭐⭐⭐⭐ | Constante | Baja | Satélite |
| QPSK | ⭐⭐ | ⭐⭐⭐⭐⭐ | Constante | Baja | Satélite, LTE |
| 8-PSK | ⭐⭐⭐ | ⭐⭐⭐ | Constante | Media | Satélite |
| 16-QAM | ⭐⭐⭐⭐ | ⭐⭐⭐ | Variable | Media | WiFi, LTE |
| 64-QAM | ⭐⭐⭐⭐⭐ | ⭐⭐ | Variable | Alta | WiFi, LTE |
| 256-QAM | ⭐⭐⭐⭐⭐⭐ | ⭐ | Variable | Muy Alta | WiFi 5, Cable |

### 8.2 Trade-offs Fundamentales

#### 1. Eficiencia Espectral vs Energética
- **Mayor M**: Más bits/símbolo → Mejor η → Peor $E_b/N_0$ requerida
- **Menor M**: Menos bits/símbolo → Peor η → Mejor $E_b/N_0$ requerida

#### 2. Envolvente Constante vs Variable
- **PSK, FSK**: Envolvente constante → Amplificadores no lineales OK → Satelital
- **QAM**: Envolvente variable → Amplificadores lineales → Terrestre

#### 3. Coherente vs No Coherente
- **Coherente**: Mejor BER (~3 dB de ventaja) → Receptor complejo
- **No coherente**: Peor BER → Receptor simple

#### 4. Ancho de Banda vs Potencia
- **FSK**: Ancho de banda grande, buena eficiencia energética
- **QAM**: Ancho de banda pequeño, requiere alta SNR

### 8.3 Selección de Modulación

**Criterios de selección**:

1. **Ancho de banda limitado**: Usar QAM alta (64/256-QAM)
2. **Potencia limitada**: Usar BPSK o QPSK
3. **Amplificador no lineal**: Usar PSK o FSK (envolvente constante)
4. **Canal con desvanecimiento**: Usar M bajo con codificación
5. **Alto throughput con buen SNR**: Usar QAM alta (256/1024-QAM)

### 8.4 Modulación Adaptativa

**Concepto**: Ajustar M dinámicamente según condiciones del canal

**Ejemplo - LTE**:
- SNR > 25 dB → 256-QAM (máxima capacidad)
- SNR 15-25 dB → 64-QAM (balance)
- SNR 10-15 dB → 16-QAM (robustez)
- SNR 5-10 dB → QPSK (máxima robustez)
- SNR < 5 dB → Posible pérdida de conexión

**Beneficio**: Maximiza throughput promedio manteniendo conectividad

---

## Resumen de Fórmulas Esenciales

### Relaciones Básicas
$$R_b = R_s \cdot \log_2(M)$$
$$E_b = \frac{E_s}{\log_2(M)}$$
$$\eta = \frac{R_b}{B} = \frac{2\log_2(M)}{1+\alpha}$$
$$B = \frac{R_s(1+\alpha)}{2}$$

### Probabilidad de Error
$$P_e^{BPSK} = Q\left(\sqrt{\frac{2E_b}{N_0}}\right)$$
$$P_e^{QPSK} \approx Q\left(\sqrt{\frac{2E_b}{N_0}}\right)$$
$$P_e^{FSK} = Q\left(\sqrt{\frac{E_b}{N_0}}\right) \text{ (coherente)}$$

### Señales
$$s_{QAM}(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)$$
$$d = \sqrt{(I_1-I_2)^2 + (Q_1-Q_2)^2}$$

---

## Conceptos que Requieren Otras Unidades

- **Ruido (Unidad 7)**: Para entender $N_0$, AWGN, y cálculos de SNR
- **Teoría de Fourier (Unidad 2)**: Para análisis espectral de señales moduladas
- **Teorema del Muestreo (Unidad 5)**: Base del criterio de Nyquist
- **Teoría de la Información (Unidad 9)**: Límite de Shannon, capacidad del canal

---

## Preguntas Frecuentes

### ¿Por qué no se habla de 4-QAM?

**Respuesta corta**: Porque 4-QAM es **matemáticamente equivalente a QPSK**.

**Respuesta detallada**:

#### Equivalencia Matemática

Consideremos el diseño óptimo de una constelación con M = 4 símbolos:

**Objetivo**: Maximizar la distancia mínima $d_{min}$ para energía promedio fija $E_s$

**Análisis geométrico**:
1. Con 4 puntos, la configuración óptima que maximiza $d_{min}$ es colocarlos en las esquinas de un cuadrado
2. Para energía promedio unitaria:
   $$E_s = \frac{1}{4}\sum_{k=1}^{4}(I_k^2 + Q_k^2) = 1$$
3. Con simetría: puntos en $(\pm a, \pm a)$
4. Resolviendo: $a = 1/\sqrt{2}$

**Resultado**: ¡Esta es exactamente la constelación QPSK!

#### Representaciones Equivalentes

**Como 4-QAM** (perspectiva de amplitud y fase):
$$s_k(t) = A_I \cos(2\pi f_c t) - A_Q \sin(2\pi f_c t)$$
donde $(A_I, A_Q) \in \{(\pm a, \pm a)\}$

**Como QPSK** (perspectiva de fase):
$$s_k(t) = A\cos(2\pi f_c t + \phi_k)$$
donde $\phi_k \in \{\pi/4, 3\pi/4, 5\pi/4, 7\pi/4\}$

Usando identidades trigonométricas:
$$A\cos(2\pi f_c t + \phi_k) = A\cos(\phi_k)\cos(2\pi f_c t) - A\sin(\phi_k)\sin(2\pi f_c t)$$

Para $\phi_1 = \pi/4$:
$$\cos(\pi/4) = \sin(\pi/4) = \frac{1}{\sqrt{2}}$$

Entonces:
$$s_1(t) = \frac{A}{\sqrt{2}}\cos(2\pi f_c t) - \frac{A}{\sqrt{2}}\sin(2\pi f_c t)$$

**¡Son idénticas!** Solo cambia la perspectiva de análisis.

#### Visualización de la Constelación

```
        Q
        |
  01 •  |  • 00      (Visto como QPSK: 4 fases)
        |
  ------+------ I
        |
  11 •  |  • 10      (Visto como 4-QAM: 4 combinaciones I-Q)
        |
```

Los 4 puntos están en las mismas posiciones independientemente de cómo los describamos.

#### Desempeño Idéntico

Ambas modulaciones tienen:
- **Bits por símbolo**: 2
- **Distancia mínima**: $d_{min} = \sqrt{2} \cdot a$
- **BER**: $P_e = Q(\sqrt{2E_b/N_0})$
- **Eficiencia espectral**: $\eta = 2$ bits/s/Hz (ideal)
- **Ancho de banda**: Mismo $B = R_s(1+\alpha)/2$

#### ¿Por qué la nomenclatura?

**Convención histórica**:
- **PSK** se usa cuando los puntos están en un **círculo** (amplitud constante)
- **QAM** se usa cuando los puntos están en una **grilla rectangular** (amplitud variable)

Para M = 4:
- Los 4 puntos pueden verse como un círculo (QPSK)
- O como una grilla 2×2 (4-QAM)
- Son lo mismo, pero **QPSK** es el nombre estándar

**A partir de M = 16**:
- Ya no hay ambigüedad: 16-QAM es una grilla 4×4
- 16-PSK sería 16 puntos en un círculo (menos eficiente, rara vez usado)
- La distinción PSK vs QAM se vuelve significativa

#### Casos Similares

Este no es el único caso de "doble nombre":

1. **BPSK = 2-ASK (antipodal)**
   - Ambos tienen 2 símbolos en el eje I
   - BPSK enfatiza la fase ($0$ y $\pi$)
   - 2-ASK antipodal enfatiza la amplitud ($+A$ y $-A$)

2. **8-PSK vs 8-QAM**
   - Aquí SÍ son diferentes:
   - 8-PSK: 8 puntos en círculo (amplitud constante)
   - 8-QAM: Puede ser rectangular (pero rara)

#### Conclusión

**No se habla de 4-QAM porque**:
1. Es idéntico a QPSK en todos los aspectos prácticos
2. La nomenclatura **QPSK** es la estándar y universalmente aceptada
3. El término **QAM** se reserva típicamente para $M \geq 16$ donde la constelación rectangular es claramente distinta de M-PSK
4. Usar "4-QAM" sería técnicamente correcto pero confuso e innecesario

**Regla práctica**:
- M = 2, 4, 8: Usa nomenclatura PSK (o FSK/ASK según corresponda)
- M ≥ 16: Usa QAM para constelaciones rectangulares
- Si ves "4-QAM" en algún texto, entiende que es simplemente otro nombre para QPSK

---

**Fin del Resumen de la Unidad 6**
