# Carta 27: Comparación de Modulaciones Digitales Básicas (ASK, FSK, PSK)

> **Unidad 6**: Modulación Digital

---

## 🎯 Pregunta

Compare ASK, FSK y PSK en términos de eficiencia espectral y robustez ante ruido.

---

## 📝 Respuesta Breve (de la carta original)

**ASK (Amplitude Shift Keying)**:
- Varía amplitud de portadora
- Eficiencia espectral: moderada
- Robustez: **baja** (muy sensible a ruido)
- Uso: limitado, fibra óptica (OOK)

**FSK (Frequency Shift Keying)**:
- Varía frecuencia de portadora
- Eficiencia espectral: baja (mayor BW)
- Robustez: **buena** (amplitud constante)
- Uso: modems, comunicaciones HF

**PSK (Phase Shift Keying)**:
- Varía fase de portadora
- Eficiencia espectral: **alta** (especialmente M-PSK)
- Robustez: muy buena con detección coherente
- Uso: **preferida** en comunicaciones modernas

**Ranking general**: PSK > FSK > ASK

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

Las modulaciones digitales básicas (ASK, FSK, PSK) representan los tres métodos fundamentales para transmitir información digital mediante una portadora analógica. Cada técnica modifica un parámetro diferente de la portadora: amplitud, frecuencia o fase, respectivamente. Esta diferenciación fundamental determina sus características de desempeño, complejidad y aplicabilidad.

**¿Por qué es importante este concepto?** En la transición del mundo analógico al digital, necesitamos técnicas para transmitir bits (información digital) a través de canales analógicos (ondas electromagnéticas). Estas tres modulaciones forman la base de todas las comunicaciones digitales modernas, desde tu WiFi hasta las comunicaciones satelitales.

**¿Dónde se aplica?** ASK se encuentra en sistemas de fibra óptica y RFID. FSK domina en comunicaciones robustas de baja velocidad como modems antiguos y telemetría. PSK y sus variantes son el corazón de WiFi, 4G/5G y comunicaciones satelitales modernas.

**Historia**: ASK fue la primera modulación digital implementada (telegrafía), seguida por FSK en los años 1900s para radiotelétipo. PSK se desarrolló en los 1950s cuando los circuitos de recuperación de fase se hicieron prácticos, revolucionando las comunicaciones digitales.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Señal portadora sinusoidal: $s(t) = A\cos(2\pi f_c t + \phi)$
- Representación de información binaria (bits)
- Concepto de símbolo digital y velocidad de señalización
- Ancho de banda de señales moduladas

#### Desarrollo Paso a Paso

**Paso 1: Señal portadora base**

La portadora no modulada tiene tres parámetros modificables:
$$s_c(t) = A_c\cos(2\pi f_c t + \phi_c)$$

donde:
- $A_c$ = amplitud de la portadora
- $f_c$ = frecuencia de la portadora
- $\phi_c$ = fase de la portadora

**Paso 2: Principio de cada modulación**

**ASK (Amplitude Shift Keying):**
$$s_{ASK}(t) = A(t)\cos(2\pi f_c t)$$
donde $A(t) = \begin{cases} A_1 & \text{para bit "1"} \\ A_0 & \text{para bit "0"} \end{cases}$

En el caso más simple (OOK - On-Off Keying): $A_0 = 0$, $A_1 = A_c$

**FSK (Frequency Shift Keying):**
$$s_{FSK}(t) = A_c\cos(2\pi f(t) t)$$
donde $f(t) = \begin{cases} f_1 & \text{para bit "1"} \\ f_0 & \text{para bit "0"} \end{cases}$

**PSK (Phase Shift Keying):**
$$s_{PSK}(t) = A_c\cos(2\pi f_c t + \phi(t))$$
donde $\phi(t) = \begin{cases} \phi_1 & \text{para bit "1"} \\ \phi_0 & \text{para bit "0"} \end{cases}$

Para BPSK binario: $\phi_0 = 0°$, $\phi_1 = 180°$

**Paso 3: Análisis espectral y de ancho de banda**

**ASK/PSK:**
- Ancho de banda: $BW = 2R_s$ donde $R_s$ es la velocidad de símbolo
- Para señalización rectangular ideal

**FSK:**
- Ancho de banda (aproximación de Carson): $BW = 2(\Delta f + R_s)$
- donde $\Delta f = |f_1 - f_0|/2$ es la desviación de frecuencia

#### Derivación Matemática

**Probabilidad de error para cada modulación:**

**ASK coherente (OOK):**
$$P_e = Q\left(\sqrt{\frac{E_b}{2N_0}}\right)$$

**FSK coherente ortogonal:**
$$P_e = Q\left(\sqrt{\frac{E_b}{N_0}}\right)$$

**PSK coherente (BPSK):**
$$P_e = Q\left(\sqrt{\frac{2E_b}{N_0}}\right)$$

donde $Q(x)$ es la función Q gaussiana y $E_b/N_0$ es la relación energía por bit a densidad de ruido.

### 🔬 Intuición y Analogías

**Analogía principal:**

Imagina transmitir información usando una linterna:
- **ASK**: Varías la intensidad de la luz (brillante = 1, tenue = 0)
- **FSK**: Cambias el color de la luz (rojo = 1, azul = 0)
- **PSK**: Giras un polarizador (vertical = 1, horizontal = 0)

**Intuición física:**

- **ASK** es como gritar más fuerte o más suave - el ruido ambiental afecta directamente la percepción
- **FSK** es como silbar diferentes notas - más robusto porque la amplitud no importa
- **PSK** es como girar una antena - requiere referencia precisa pero muy eficiente

**Visualización:**

En el dominio del tiempo:
- ASK: envolvente variable
- FSK: frecuencia instantánea variable
- PSK: discontinuidades de fase en transiciones

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Transmisión de la secuencia "101" a 1000 bps

**Situación:** Transmitir la secuencia binaria "101" usando cada modulación

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Frecuencia portadora | 10 | kHz |
| Tasa de bits | 1000 | bps |
| Amplitud portadora | 1 | V |

**Solución para cada modulación:**

1. **ASK (OOK):**
   - Bit "1": $s(t) = 1\cos(2\pi \cdot 10^4 t)$ V
   - Bit "0": $s(t) = 0$ V
   - Ancho de banda: $BW = 2 \times 1000 = 2$ kHz

2. **FSK (con Δf = 500 Hz):**
   - Bit "1": $s(t) = 1\cos(2\pi \cdot 10500 t)$ V
   - Bit "0": $s(t) = 1\cos(2\pi \cdot 9500 t)$ V
   - Ancho de banda: $BW = 2(500 + 1000) = 3$ kHz

3. **BPSK:**
   - Bit "1": $s(t) = 1\cos(2\pi \cdot 10^4 t)$ V
   - Bit "0": $s(t) = -1\cos(2\pi \cdot 10^4 t)$ V
   - Ancho de banda: $BW = 2 \times 1000 = 2$ kHz

**Interpretación:** FSK requiere 50% más ancho de banda que ASK/PSK

---

#### Ejemplo 2: Sistema WiFi 802.11b (aplicación real)

**Contexto:** WiFi 802.11b usa DBPSK/DQPSK para transmisión robusta

- Frecuencia: 2.4 GHz
- Tasa básica: 1 Mbps con DBPSK
- Tasa mejorada: 2 Mbps con DQPSK
- Por qué PSK: máxima eficiencia espectral en canal limitado
- Ancho de banda del canal: 22 MHz
- Potencia típica: 100 mW (20 dBm)

El sistema elige PSK porque:
1. Eficiencia espectral permite múltiples canales en banda ISM
2. Robustez adecuada para ambiente indoor con multitrayecto
3. Detección coherente práctica a estas frecuencias

---

#### Ejemplo 3: Comparación de BER para Eb/N0 = 10 dB

**¿Qué pasa cuando tenemos la misma energía por bit?**

Para $E_b/N_0 = 10$ dB = 10 (lineal):

- **ASK (OOK):** $P_e = Q(\sqrt{5}) = Q(2.24) \approx 1.25 \times 10^{-2}$
- **FSK ortogonal:** $P_e = Q(\sqrt{10}) = Q(3.16) \approx 7.9 \times 10^{-4}$
- **BPSK:** $P_e = Q(\sqrt{20}) = Q(4.47) \approx 3.9 \times 10^{-6}$

**Conclusión:** Para la misma energía, BPSK es ~3200 veces mejor que ASK

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Constelaciones** (Carta 28): Representación gráfica de estas modulaciones
- **QAM** (Carta 29): Combinación de ASK y PSK
- **Detección coherente/no coherente** (Carta 32): Afecta desempeño de cada tipo
- **BER** (Carta 31): Métrica fundamental de comparación

#### Dependencias (lo que necesitas saber primero)
1. Teorema de muestreo → Para entender digitalización
2. Análisis de Fourier → Para calcular anchos de banda
3. Probabilidad y procesos aleatorios → Para análisis de ruido

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Modulaciones multinivel**: M-ASK, M-FSK, M-PSK
2. **Modulaciones híbridas**: QAM combina ASK+PSK
3. **OFDM**: Usa PSK/QAM en subportadoras

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- Trade-off fundamental: eficiencia espectral vs. robustez
- Por qué PSK domina en sistemas modernos
- Cuándo cada modulación es apropiada
- Cálculo de ancho de banda para cada tipo

#### Tipos de problemas típicos
1. **Cálculo de BW**: Dado R_s y parámetros, calcular BW para cada modulación
2. **Comparación de BER**: Graficar o calcular Pe vs Eb/N0
3. **Selección de modulación**: Elegir la apropiada para un escenario dado

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir eficiencia espectral con eficiencia de potencia**
- Por qué ocurre: Son métricas diferentes pero relacionadas
- Cómo evitarlo: Eficiencia espectral = bits/s/Hz, eficiencia de potencia = Eb/N0 requerido
- Ejemplo: FSK tiene baja eficiencia espectral pero buena eficiencia de potencia

❌ **Error #2: Asumir que ASK siempre es OOK**
- Por qué ocurre: OOK es el caso más común
- Cómo evitarlo: ASK puede tener múltiples niveles (M-ASK)
- Distinción: OOK es ASK binario con A0=0

❌ **Error #3: Ignorar el tipo de detección al comparar**
- Por qué ocurre: Las fórmulas cambian significativamente
- Cómo evitarlo: Siempre especificar coherente vs no coherente
- Impacto: ~3 dB de penalidad para detección no coherente

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
BW_ASK = BW_PSK = 2Rs (señalización rectangular)
BW_FSK = 2(Δf + Rs) (aproximación de Carson)
Pe_BPSK < Pe_FSK < Pe_ASK (para mismo Eb/N0)
```

#### Conceptos Fundamentales
- ✓ **PSK es superior**: Mejor balance eficiencia-robustez
- ✓ **FSK para robustez extrema**: Cuando la simplicidad y robustez importan más que eficiencia
- ✓ **ASK casi obsoleto**: Solo en aplicaciones muy específicas (fibra óptica)

#### Reglas Mnemotécnicas
- 🧠 **"PFA" (Phase-Frequency-Amplitude)**: Orden de preferencia en sistemas modernos
- 🧠 **"2Rs para binarios"**: Ancho de banda de ASK/PSK binarios

#### Valores Típicos (para referencias rápidas)

| Modulación | BW (binario) | Pe @ 10dB | Aplicación típica |
|------------|--------------|-----------|-------------------|
| ASK | 2Rs | 10^-2 | Fibra óptica |
| FSK | 3-4Rs | 10^-4 | HF, telemetría |
| PSK | 2Rs | 10^-6 | WiFi, satélite |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**: Proakis & Salehi Cap. 4-5, Haykin Cap. 6
- **Simulaciones**: GNU Radio para ver señales en tiempo real
- **Papers**: "Digital Modulation Techniques" - Fuqin Xiong

#### Temas Relacionados para Explorar
1. Modulaciones CPM (Continuous Phase Modulation)
2. Técnicas de modulación diferencial (DPSK, DFSK)
3. Modulación TCM (Trellis Coded Modulation)

#### Preguntas para Reflexionar
- ¿Por qué no existe una modulación que varíe los tres parámetros simultáneamente de forma independiente?
- ¿Cómo afecta la no-linealidad del amplificador a cada tipo de modulación?
- ¿Qué pasaría si el canal tiene desvanecimiento selectivo en frecuencia?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 25 minutos
**Prerequisitos críticos**: Análisis de Fourier, portadora sinusoidal, ruido gaussiano
**Tags**: `#modulacion-digital` `#ASK` `#FSK` `#PSK` `#comparacion` `#eficiencia-espectral`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*