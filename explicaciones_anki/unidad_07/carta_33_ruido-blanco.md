# Carta 33: Ruido Blanco - El Modelo Fundamental del Ruido en Comunicaciones

> **Unidad 7**: Ruido

---

## 🎯 Pregunta

¿Defina ruido blanco y explique por qué es un modelo útil en comunicaciones?

---

## 📝 Respuesta Breve (de la carta original)

**Ruido blanco** es ruido aleatorio con densidad espectral de potencia constante para todas las frecuencias.

**Características**:
- DEP: $N_0 = kT$ (W/Hz) constante (convención unilateral)
- Potencia infinita (en ancho de banda infinito)
- Proceso estacionario, gaussiano
- Autocorrelación: función delta $R_n(\tau) = N_0\delta(\tau)$

**Por qué es útil**:
1. **Modelo simplificado**: aproxima bien el ruido térmico
2. **Análisis matemático simple**: independencia espectral
3. **Peor caso razonable**: conservador pero realista
4. **Banda limitada**: en sistemas reales se filtra a BW finito

**Realidad**: ruido "blanco filtrado" con potencia $N = N_0 \cdot B = kTB$

**Nota**: Algunos textos usan $N_0 = 4kT$ (convención bilateral antigua). Usamos $N_0 = kT$ (convención unilateral moderna, más simple).

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El **ruido blanco** es uno de los conceptos más fundamentales en sistemas de comunicaciones, comparable en importancia a conceptos como la transformada de Fourier o el teorema del muestreo. Su nombre proviene de una analogía con la luz blanca, que contiene todas las frecuencias del espectro visible con igual intensidad.

**¿Por qué es importante este concepto?** El ruido está presente en todo sistema de comunicaciones real. Desde el sutil silbido térmico en un receptor de radio hasta las interferencias complejas en sistemas satelitales, el ruido determina los límites fundamentales de lo que podemos comunicar. El modelo de ruido blanco proporciona la abstracción matemática perfecta para analizar estos fenómenos.

**¿Dónde se aplica?** El ruido blanco aparece en:
- **Receptores de radio y TV**: como el "estático" o "nieve"
- **Comunicaciones satelitales**: limitando la sensibilidad del receptor
- **Enlaces de fibra óptica**: en detectores y amplificadores
- **Sistemas celulares**: determinando cobertura y capacidad
- **WiFi y Bluetooth**: afectando alcance y velocidad

**Historia**: El concepto fue formalizado en los trabajos pioneros de Norbert Wiener en la década de 1920, quien desarrolló la teoría matemática de procesos estocásticos. Claude Shannon lo adoptó como modelo fundamental en su teoría de la información (1948), estableciéndolo como estándar en el análisis de sistemas de comunicación.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Densidad Espectral de Potencia (DEP)**: distribución de potencia en frecuencia
- **Procesos estocásticos**: señales aleatorias con propiedades estadísticas
- **Función de autocorrelación**: medida de similitud de una señal consigo misma
- **Delta de Dirac**: función impulso idealizada

#### Desarrollo Paso a Paso

**Paso 1: Definición Espectral**

El ruido blanco se define por su densidad espectral de potencia:

**Representación bilateral** (frecuencias positivas y negativas):
$$S_n(f) = \frac{N_0}{2} = \frac{kT}{2} \text{ para } -\infty < f < \infty$$

**Representación unilateral** (solo frecuencias positivas, convención moderna):
$$S_n(f) = N_0 = kT \text{ para } f > 0$$

En este curso usaremos la **convención unilateral** por simplicidad: $N_0 = kT$ [W/Hz].

**Paso 2: Propiedades Temporales**

La función de autocorrelación se obtiene como la transformada inversa de Fourier de la DEP:

**Para representación bilateral**:
$$R_n(\tau) = \mathcal{F}^{-1}\{S_n(f)\} = \mathcal{F}^{-1}\{\frac{kT}{2}\} = \frac{kT}{2}\delta(\tau)$$

**Para representación unilateral** (equivalente en potencia):
$$R_n(\tau) = N_0\delta(\tau) = kT\delta(\tau)$$

Esta función delta implica que:
- El ruido en instantes diferentes es completamente decorrelacionado
- No hay "memoria" entre muestras sucesivas
- Cada muestra es independiente de todas las demás

**Paso 3: Características Estadísticas**

El ruido blanco gaussiano (el caso más común) tiene:
- **Media**: $\mu = 0$ (valor esperado cero)
- **Varianza**: $\sigma^2 = \infty$ (en banda infinita)
- **Distribución**: Gaussiana para cada muestra temporal

#### Derivación Matemática

**Partiendo de la definición de potencia:**

**Representación bilateral**: La potencia total del ruido blanco sería:

$$P_{total} = \int_{-\infty}^{\infty} \frac{kT}{2} df = \infty$$

**Problema aparente:** ¡Potencia infinita!

**Solución práctica:** En sistemas reales, el ruido siempre es filtrado.

**Representación unilateral** (solo frecuencias positivas):

$$P_{real} = \int_{0}^{B} N_0 df = \int_{0}^{B} kT \, df = kTB$$

donde B es el ancho de banda del sistema.

**Clave**: Usando la convención unilateral ($N_0 = kT$), la fórmula de potencia es directa: $N = N_0 B = kTB$

**Relación con temperatura:**

El ruido térmico (Johnson-Nyquist) tiene densidad espectral de potencia disponible:

$$N_0 = kT$$

donde:
- $k = 1.38 \times 10^{-23}$ J/K (constante de Boltzmann)
- $T$ = temperatura absoluta en Kelvin
- Esta es la convención **unilateral moderna** (solo frecuencias positivas)

**Nota histórica**: La fórmula original de Nyquist para voltaje de ruido es $\overline{v_n^2} = 4kTRB$. El factor 4 aparece en voltaje, pero la potencia disponible (con carga adaptada) es $P = \frac{\overline{v_n^2}}{4R} = kTB$, sin el factor 4.

### 🔬 Intuición y Analogías

**Analogía principal:**
Imagina el ruido blanco como una "lluvia de fotones" completamente aleatoria. Cada "gota" (muestra) cae independientemente, sin relación con las anteriores o posteriores. La intensidad de la lluvia (densidad espectral) es constante en todo momento y lugar (frecuencia).

**Intuición física:**
El ruido térmico surge del movimiento aleatorio de electrones en conductores. A temperatura ambiente, billones de electrones se mueven caóticamente, generando fluctuaciones de voltaje microscópicas. La suma de todas estas contribuciones aleatorias produce ruido blanco.

**Visualización:**
- En el dominio del tiempo: señal completamente aleatoria, como el trazo de un sismógrafo durante un temblor
- En el dominio de la frecuencia: espectro plano, como una línea horizontal
- En osciloscopio: patrón cambiante e impredecible, "grass" o césped

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Cálculo de Potencia de Ruido en Receptor FM

**Situación:** Un receptor FM con ancho de banda de 200 kHz opera a temperatura ambiente (290 K).

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Ancho de banda (B) | 200 | kHz |
| Temperatura (T) | 290 | K |
| Constante de Boltzmann (k) | 1.38×10⁻²³ | J/K |

**Solución paso a paso:**

1. **Densidad espectral de ruido térmico (convención unilateral):**
   $$N_0 = kT = 1.38 \times 10^{-23} \times 290$$
   $$N_0 = 4.0 \times 10^{-21} \text{ W/Hz}$$

   En dBm/Hz: $N_0 = 10\log_{10}(4.0 \times 10^{-21}/10^{-3}) = -174$ dBm/Hz

2. **Potencia de ruido en el ancho de banda:**
   $$N = N_0 \times B = 4.0 \times 10^{-21} \times 200 \times 10^3$$
   $$N = 8.0 \times 10^{-16} \text{ W}$$

3. **En dBm:**
   $$N_{dBm} = 10\log_{10}\left(\frac{8.0 \times 10^{-16}}{10^{-3}}\right)$$
   $$\boxed{N_{dBm} = -121 \text{ dBm}}$$

**Interpretación:** Este es el "piso de ruido" fundamental del receptor. Cualquier señal debe estar por encima de este nivel para ser detectada.

---

#### Ejemplo 2: Sistema WiFi 802.11n

**Contexto:** Router WiFi operando en 2.4 GHz con canal de 20 MHz

**Análisis del ruido:**
- Ancho de banda: B = 20 MHz
- Temperatura efectiva del sistema: ~400 K (incluye figura de ruido del receptor)
- $N_0 = kT = 1.38 \times 10^{-23} \times 400 = 5.52 \times 10^{-21}$ W/Hz

**Potencia de ruido:**
$$N = N_0 \times B = 5.52 \times 10^{-21} \times 20 \times 10^6 = 1.1 \times 10^{-13} \text{ W}$$

En dBm: **-100 dBm**

**Implicación práctica:** Para una señal WiFi típica de -70 dBm, tenemos SNR = 30 dB, permitiendo velocidades de hasta 150 Mbps con 64-QAM.

---

#### Ejemplo 3: Límites Fundamentales - Caso Extremo

**¿Qué pasa cuando...?**

**Si N₀ → 0 (temperatura absoluta cero):**
- No hay ruido térmico
- Límite cuántico domina (ruido shot)
- Imposible en práctica (3° ley termodinámica)

**Si B → ∞ (ancho de banda infinito):**
- Potencia de ruido → ∞
- Físicamente imposible
- Siempre existe filtrado natural

**Caso especial - Ruido banda angosta:**
Si filtramos ruido blanco a banda angosta:
- Envolvente: distribución de Rayleigh
- Fase: distribución uniforme
- Se comporta como señal cuasi-sinusoidal con amplitud y fase aleatorias

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Temperatura de ruido** (Carta 34): Forma alternativa de expresar N₀
- **Figura de ruido** (Carta 35): Mide cuánto ruido agrega un dispositivo
- **Fórmula de Friis** (Carta 36): Cómo se acumula el ruido en cascada
- **Ruido de banda angosta** (Carta 37): Ruido blanco filtrado
- **Teorema de Shannon-Hartley** (Carta 45): Límite fundamental con ruido blanco

#### Dependencias (lo que necesitas saber primero)
1. **Densidad espectral de potencia** → Para entender la caracterización espectral
2. **Procesos aleatorios** → Base estadística del modelo
3. **Transformada de Fourier** → Relación tiempo-frecuencia

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Cálculo de SNR**: Base para todos los análisis de desempeño
2. **Diseño de receptores**: Determina sensibilidad mínima
3. **Link budget**: Cálculo de alcance de comunicaciones
4. **BER vs Eb/N₀**: Curvas fundamentales de desempeño

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La diferencia entre ruido blanco teórico (banda infinita) y práctico (banda limitada)
- Por qué la autocorrelación es una delta (decorrelación completa)
- Cómo calcular potencia de ruido dado N₀ y ancho de banda
- La conexión con temperatura física (ruido térmico)

#### Tipos de problemas típicos
1. **Cálculo de potencia de ruido**: Dado T y B, encontrar N en watts y dBm
   - Estrategia: Usar $N = kTB$ (para sistemas a temperatura T)

2. **Análisis de cascada**: Múltiples etapas con diferentes temperaturas de ruido
   - Estrategia: Aplicar fórmula de Friis considerando ganancia

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir N₀ = kT (potencia) con la fórmula de voltaje 4kTRB**
- Por qué ocurre: Textos antiguos usan $N_0 = 4kT$ (convención bilateral)
- Cómo evitarlo: Usar la convención moderna **unilateral**: $N_0 = kT$ [W/Hz]
- Explicación: El factor 4 aparece en voltaje ($\overline{v_n^2} = 4kTRB$), pero la potencia disponible es $N = kTB$
- Ver archivo `aclaracion_densidad_espectral_ruido.md` para detalles completos

❌ **Error #2: Usar temperatura en Celsius en lugar de Kelvin**
- Por qué ocurre: Costumbre de usar °C
- Cómo evitarlo: SIEMPRE convertir a Kelvin (T_K = T_C + 273.15)

❌ **Error #3: Confundir ruido blanco con ruido gaussiano**
- Distinción importante:
  - Blanco → propiedad espectral (todas las frecuencias)
  - Gaussiano → propiedad estadística (distribución normal)
  - Puede ser blanco pero no gaussiano, o gaussiano pero no blanco

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
N₀ = kT                      [Densidad espectral unilateral, W/Hz]
N = N₀ × B = kTB             [Potencia de ruido en banda B]
N₀ = -174 dBm/Hz             [A temperatura ambiente T=290K]
N_dBm = -174 + 10log₁₀(B)    [Potencia total, B en Hz]
```

**Nota histórica**: La fórmula de voltaje de Nyquist es $\overline{v_n^2} = 4kTRB$, pero la potencia disponible es $N = kTB$ (sin el factor 4).

#### Conceptos Fundamentales
- ✓ **Ruido blanco = DEP constante**: Todas las frecuencias contribuyen igual
- ✓ **Decorrelación temporal completa**: R(τ) = δ(τ)
- ✓ **Siempre filtrado en práctica**: Banda limitada en sistemas reales
- ✓ **Modelo pesimista pero útil**: Simplifica análisis manteniendo validez

#### Reglas Mnemotécnicas
- 🧠 **"kTB"**: Recuerda "Kate Beckinsale" para kTB (potencia = kT × Bandwidth)
- 🧠 **"-174 dBm/Hz"**: Piso de ruido a temperatura ambiente (memorizar)

#### Valores Típicos (para referencias rápidas)

| Parámetro | Valor Típico | Aplicación |
|-----------|--------------|------------|
| N₀ @ 290K | -174 dBm/Hz | Sistemas terrestres |
| N₀ @ 50K | -183 dBm/Hz | LNA criogénico |
| Piso de ruido WiFi (20 MHz) | -101 dBm | 802.11 típico |
| Piso de ruido GPS (2 MHz) | -111 dBm | Receptor GPS |
| Piso de ruido celular (180 kHz) | -121 dBm | GSM |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**:
  - Haykin, "Communication Systems", Cap. 5.1-5.3
  - Carlson, "Communication Systems", Cap. 8
- **Papers clásicos**:
  - Johnson (1928) "Thermal Agitation of Electricity in Conductors"
  - Nyquist (1928) "Thermal Agitation of Electric Charge"
- **Simulaciones**:
  - GNU Radio: Generador de ruido AWGN
  - MATLAB: función `awgn()`, `randn()`

#### Temas Relacionados para Explorar
1. **Ruido de cuantización**: En sistemas digitales
2. **Ruido shot (Schottky)**: En dispositivos semiconductores
3. **Ruido flicker (1/f)**: En bajas frecuencias
4. **Ruido cuántico**: Límite fundamental en óptica

#### Preguntas para Reflexionar
- ¿Por qué no existe verdadero ruido blanco en la naturaleza?
- ¿Qué pasaría si pudiéramos eliminar completamente el ruido térmico?
- ¿Cómo afecta el ruido blanco a diferentes tipos de modulación?
- ¿Por qué el modelo de ruido blanco gaussiano es tan ubicuo en comunicaciones?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 30 minutos
**Prerequisitos críticos**: Densidad espectral de potencia, procesos aleatorios
**Tags**: `#ruido` `#ruido-blanco` `#AWGN` `#densidad-espectral` `#fundamentos`

---

*Generado el: 2024-11-16*
*Última revisión: 2025-11-22 - Actualizado a convención unilateral moderna (N₀ = kT)*