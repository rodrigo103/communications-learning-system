# Carta 55: Prefijo Cíclico - El Guardián de la Ortogonalidad en OFDM

> **Unidad 10**: Espectro Expandido y OFDM

---

## 🎯 Pregunta

Explique qué es el prefijo cíclico en OFDM y por qué es necesario.

---

## 📝 Respuesta Breve (de la carta original)

El **prefijo cíclico (CP)** es una copia de la parte final del símbolo OFDM que se añade al principio.

**Funcionamiento**:
1. Símbolo OFDM de duración $T_s$
2. Se copian últimos $T_g$ segundos
3. Se añaden al inicio → símbolo total: $T_s + T_g$

**Por qué es necesario**:

**Problema sin CP**:
- Multitrayecto causa **ISI** (interferencia entre símbolos)
- Destruye ortogonalidad entre subportadoras → **ICI** (interferencia entre portadoras)

**Solución con CP**:
- Si $T_g >$ delay spread del canal:
  - Convierte convolución lineal en circular
  - Preserva ortogonalidad
  - Elimina ISI e ICI
  - Ecualización simple: solo un coeficiente complejo por subportadora

**Costo**: overhead típico 10-25% (reduce tasa efectiva)

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

**¿Por qué el prefijo cíclico es crucial?** El prefijo cíclico (CP) es el héroe anónimo de OFDM - sin él, toda la elegancia matemática de OFDM colapsa en presencia de multitrayecto. Es una solución brillantemente simple a un problema complejo: cómo mantener la ortogonalidad entre subportadoras cuando las señales llegan por múltiples caminos con diferentes retardos. El CP transforma lo que sería un desastre de interferencias en un problema matemático trivial.

**¿Dónde es crítico el CP?**
- **Ambientes urbanos densos**: reflexiones en edificios causan delays de microsegundos
- **Indoor**: paredes y muebles crean múltiples trayectos
- **TV broadcast**: señales viajan kilómetros con múltiples reflexiones
- **Comunicaciones submarinas**: reverberación acústica severa

**¿Cuándo no necesitarías CP?**
- Canal AWGN puro (solo ruido, sin multitrayecto)
- Comunicaciones en espacio libre sin reflexiones
- Sistemas con símbolo tan largo que ISI es despreciable

**Historia:** Peled y Ruiz (1980) introdujeron el concepto de CP en el contexto de DMT (Discrete Multitone) para DSL. Su genialidad fue reconocer que agregar redundancia cíclica convierte la convolución lineal del canal en convolución circular, compatible con DFT.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Convolución lineal vs. circular
- Teorema de convolución y DFT
- Respuesta al impulso de canales multitrayecto
- ISI (Inter-Symbol Interference)
- ICI (Inter-Carrier Interference)

#### Desarrollo Paso a Paso

**Paso 1: El Problema del Multitrayecto**

Un canal multitrayecto tiene respuesta al impulso:
$$h(t) = \sum_{l=0}^{L-1} \alpha_l \delta(t - \tau_l)$$

La señal recibida es la convolución:
$$r(t) = s(t) * h(t) = \sum_{l=0}^{L-1} \alpha_l s(t - \tau_l)$$

Cada símbolo OFDM es afectado por el símbolo anterior → ISI.

**Paso 2: Construcción del Prefijo Cíclico**

Para un símbolo OFDM $s(t)$ de duración $T_s$:

1. **Identificar la cola**: últimos $T_g$ segundos del símbolo
2. **Copiar al inicio**: prepend esta porción
3. **Símbolo extendido**: duración total $T_s + T_g$

Matemáticamente:
$$s_{CP}(t) = \begin{cases}
s(t + T_s) & \text{para } -T_g \leq t < 0 \\
s(t) & \text{para } 0 \leq t < T_s
\end{cases}$$

**Paso 3: Efecto Mágico del CP**

Con CP suficientemente largo ($T_g > \tau_{max}$):
- La porción del símbolo actual afectada por ISI está en el CP
- Al descartar el CP en recepción, removemos toda la ISI
- La parte útil del símbolo solo ve interferencia de sí mismo (cíclica)

#### Derivación Matemática

**Sin Prefijo Cíclico:**

Señal OFDM transmitida (símbolo n):
$$s_n(t) = \sum_{k=0}^{N-1} X_{n,k} e^{j2\pi k t/T_s} \quad \text{para } 0 \leq t \leq T_s$$

Señal recibida con canal $h(t)$:
$$r(t) = s_n(t) * h(t) + s_{n-1}(t) * h(t)$$

El segundo término es ISI del símbolo anterior.

Después de DFT en el receptor:
$$Y_{n,k} = H_k X_{n,k} + \sum_{m \neq k} I_{k,m} X_{n,m} + \text{ISI}_{n-1}$$

Donde $I_{k,m}$ representa ICI (interferencia entre portadoras).

**Con Prefijo Cíclico:**

Símbolo extendido:
$$s_{CP,n}(t) = \sum_{k=0}^{N-1} X_{n,k} e^{j2\pi k t/T_s} \quad \text{para } -T_g \leq t \leq T_s$$

Clave: el CP hace que la convolución lineal aparezca como circular en la ventana de observación.

Después de remover CP y aplicar DFT:
$$\boxed{Y_{n,k} = H_k X_{n,k} + N_k}$$

¡No hay ISI ni ICI! Solo multiplicación por la respuesta en frecuencia del canal.

**Demostración de la Convolución Circular:**

Con CP, la convolución sobre $[0, T_s]$ es:
$$r(t) = \int_0^{\tau_{max}} h(\tau) s_{CP}(t-\tau) d\tau$$

Como $s_{CP}(t) = s_{CP}(t + T_s)$ para $t \in [-T_g, 0]$:
$$r(t) = h(t) \circledast s(t)$$

Y sabemos que DFT{convolución circular} = producto de DFTs.

### 🔬 Intuición y Analogías

**Analogía principal: El amortiguador de un tren**

Imagina cada símbolo OFDM como un vagón de tren:
- **Sin CP**: los vagones chocan directamente (ISI)
- **Con CP**: cada vagón tiene un amortiguador que absorbe el impacto
- El amortiguador (CP) se comprime y daña, pero protege la carga (datos)
- Descartamos el amortiguador dañado al llegar

**Intuición temporal:**

Piensa en ecos en una catedral:
1. **Gritas una palabra** (transmites símbolo OFDM)
2. **Eco de la palabra anterior** llega durante los primeros milisegundos
3. **CP = silencio inicial planeado** donde esperamos que lleguen ecos
4. **Ignoramos los primeros milisegundos** (descartamos CP)
5. **Escuchamos la parte limpia** (procesamos símbolo sin ISI)

**Visualización de la "magia circular":**

Sin CP:
```
Símbolo n-1: [====DATOS====]
Símbolo n:                  [====DATOS====]
                               ↑
                          ISI contamina inicio
```

Con CP:
```
Símbolo n-1: [====DATOS====]
Símbolo n:                  [CP][====DATOS====]
                             ↑  ↑
                      ISI solo   Datos limpios
                      afecta CP
```

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Dimensionamiento de CP en WiFi 802.11n

**Situación:** Diseñar CP para ambiente indoor típico

**Datos del canal:**
| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| Delay spread RMS | 50 ns | Ambiente oficina |
| Delay spread máximo | 250 ns | 5× RMS (regla práctica) |
| Ancho de banda | 20 MHz | Canal WiFi |
| Subportadoras | 64 | FFT size |

**Solución paso a paso:**

1. **Duración símbolo útil:**
   $$T_s = \frac{1}{\Delta f} = \frac{N}{BW} = \frac{64}{20 \text{ MHz}} = 3.2 \text{ μs}$$

2. **CP mínimo requerido:**
   $$T_g > \tau_{max} = 250 \text{ ns}$$

3. **CP estándar 802.11n:**
   - CP corto: 400 ns (para indoor)
   - CP largo: 800 ns (para outdoor/MIMO)

4. **Overhead calculado:**
   $$\text{Eficiencia} = \frac{T_s}{T_s + T_g} = \frac{3.2}{3.2 + 0.8} = 80\%$$

**Interpretación:** El 20% del tiempo se "desperdicia" en CP, pero es esencial para operación robusta.

---

#### Ejemplo 2: Análisis de ISI/ICI con y sin CP

**Contexto:** Sistema OFDM con canal de dos trayectos

**Modelo de canal:**
- Trayecto directo: amplitud = 1, retardo = 0
- Trayecto reflejado: amplitud = 0.5, retardo = 1 μs

**Sistema OFDM:**
| Parámetro | Valor |
|-----------|-------|
| Duración símbolo | 10 μs |
| Número subportadoras | 16 |
| Δf | 100 kHz |

**Caso 1: Sin CP**

Respuesta en frecuencia del canal:
$$H(f) = 1 + 0.5e^{-j2\pi f \times 1\mu s}$$

Problema: El retardo causa que parte del símbolo anterior interfiera:
- ISI afecta primeros 1 μs del símbolo (10% contaminado)
- Ortogonalidad destruida → ICI entre todas las subportadoras
- BER degradado severamente

**Caso 2: Con CP de 1.5 μs**

- CP absorbe completamente el retardo de 1 μs
- Después de descartar CP: solo efecto multiplicativo
- Por subportadora k:
  $$H_k = 1 + 0.5e^{-j2\pi k \times 0.1} = 1 + 0.5e^{-j0.2\pi k}$$

Ecualización simple:
$$\hat{X}_k = \frac{Y_k}{H_k}$$

**Resultados de simulación:**
| Métrica | Sin CP | Con CP |
|---------|--------|---------|
| BER @ 10 dB SNR | 10⁻² | 10⁻⁵ |
| ICI power | -15 dB | -∞ (cero) |
| Complejidad ecualización | O(N²) | O(N) |

---

#### Ejemplo 3: Trade-off de longitud de CP

**¿Cuánto CP es óptimo?**

**Escenario:** Diseño de sistema para diferentes ambientes

**Análisis de trade-off:**

| CP Length | Eficiencia | Ambiente soportado | Pros | Contras |
|-----------|------------|-------------------|------|---------|
| 1/32 Ts | 96.9% | Indoor limpio | Máximo throughput | Falla con eco largo |
| 1/16 Ts | 93.8% | Indoor típico | Buen balance | - |
| 1/8 Ts | 87.5% | Outdoor urbano | Robusto | 12.5% overhead |
| 1/4 Ts | 75% | Montañoso/SFN | Muy robusto | 25% pérdida capacity |

**Ejemplo numérico LTE:**

Para Δf = 15 kHz → Ts = 66.7 μs

CP normal: 4.7 μs → soporta celdas hasta ~1.4 km
CP extendido: 16.7 μs → soporta celdas hasta ~5 km

Trade-off:
- CP normal: eficiencia 93%, cobertura estándar
- CP extendido: eficiencia 80%, cobertura rural

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **OFDM básico** (Carta 53): CP es componente esencial
- **Multitrayecto**: fenómeno que CP mitiga
- **DFT/FFT**: convolución circular es clave
- **Ecualización**: CP la simplifica dramáticamente

#### Alternativas y Variantes
1. **Zero Padding (ZP)**: ceros en lugar de copia cíclica
   - Ventaja: menor potencia transmitida
   - Desventaja: ecualización más compleja

2. **Unique Word (UW-OFDM)**: secuencia conocida como guarda
   - Ventaja: puede usarse para sincronización
   - Desventaja: no preserva circularidad perfecta

3. **Windowing**: ventanas suaves en transiciones
   - Reduce emisiones fuera de banda
   - Compatible con CP

#### Impacto en el Sistema
1. **Sincronización**: CP ayuda a encontrar inicio de símbolo
2. **Estimación de canal**: correlación del CP
3. **Eficiencia energética**: CP transmite potencia "inútil"
4. **Latencia**: CP añade retardo fijo

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- Por qué la convolución circular es importante
- Relación exacta entre longitud CP y delay spread
- Trade-off fundamental: robustez vs. eficiencia
- Por qué CP debe ser copia cíclica, no ceros

#### Tipos de problemas típicos
1. **Dimensionar CP**: Dado delay spread, calcular CP mínimo
   - Estrategia: TCP > τmax, considerar overhead aceptable

2. **Análisis de eficiencia**: Calcular pérdida por CP
   - Estrategia: η = Ts/(Ts + TCP)

3. **Demostración matemática**: Probar que CP preserva ortogonalidad
   - Estrategia: mostrar convolución circular en DFT

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Pensar que CP es solo "tiempo muerto"**
- Por qué ocurre: se ve como overhead desperdiciado
- Realidad: CP contiene señal útil (copia del final)
- Importancia: mantiene continuidad de fase

❌ **Error #2: CP demasiado corto "casi funciona"**
- Por qué ocurre: querer maximizar eficiencia
- Realidad: si TCP < τmax, falla catastróficamente
- Regla: mejor CP largo que corto

❌ **Error #3: Confundir CP con banda de guarda**
- CP: guarda en tiempo, contiene señal
- Banda de guarda: guarda en frecuencia, sin señal
- Diferencia: CP es esencial para ortogonalidad, banda de guarda no

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Condición CP: TCP > τmax (delay spread máximo)
Eficiencia: η = Ts/(Ts + TCP)
Overhead: γ = TCP/(Ts + TCP)
Símbolo total: Ttotal = Ts + TCP
Distancia eco: d = c × TCP (para SFN)
```

#### Conceptos Fundamentales
- ✓ **CP convierte convolución lineal en circular**: la magia matemática
- ✓ **Trade-off fundamental**: robustez vs. throughput
- ✓ **CP debe ser cíclico**: zeros no preservan ortogonalidad
- ✓ **Dimensionar para peor caso**: mejor conservador que optimista

#### Reglas Mnemotécnicas
- 🧠 **CP = "Copia Protectora"**: protege datos del multitrayecto
- 🧠 **"Circular Paradise"**: CP crea el paraíso de la convolución circular
- 🧠 **"Guard the Orthogonality"**: CP guarda la ortogonalidad

#### Valores Típicos de CP
| Sistema | CP/Ts ratio | TCP típico | Uso |
|---------|-------------|------------|-----|
| WiFi | 1/4 o 1/8 | 0.8 μs | Indoor |
| LTE | 1/14 normal | 4.7 μs | Celular |
| DVB-T | 1/32 a 1/4 | Variable | TV broadcast |
| DSL/DMT | 1/16 | 32 μs | Cable telefónico |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Paper fundamental**: Peled & Ruiz 1980 - introducción del CP
- **Análisis detallado**: Muquet et al. "Cyclic Prefixing or Zero Padding"
- **Libro**: Wang & Giannakis "Wireless Multicarrier Communications"
- **Simulación**: GNU Radio - bloques OFDM incluyen CP configurable

#### Temas Avanzados
1. **CP adaptativo**: ajustar longitud según condiciones
2. **Insufficient CP compensation**: técnicas cuando TCP < τmax
3. **CP-free OFDM**: nuevas técnicas sin CP
4. **Fractional CP**: CP no entero para optimización fina

#### Preguntas para Reflexionar
- ¿Por qué no usar CP muy largo siempre?
- ¿Puede recuperarse información del CP descartado?
- ¿Cómo afecta el Doppler la efectividad del CP?
- ¿Existen esquemas que eliminen la necesidad de CP?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 35 minutos
**Prerequisitos críticos**: OFDM, convolución, DFT, multitrayecto
**Tags**: `#cyclic-prefix` `#ofdm` `#multipath` `#isi` `#ici` `#guard-interval`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*