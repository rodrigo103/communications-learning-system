# Examen Final SC — 30/07/2026

*Fuente: `exercises/finales/miFinal/F_Comu_2026-07-30_miFinal.pdf` (fotos de las hojas de enunciado, tomadas al finalizar)*

> ⚠️ **Este es el final que rindió Rodrigo (Videla, Rodrigo).** Las cuatro hojas son los **enunciados con las marcas de corrección** del equipo docente; las hojas de resolución manuscritas no están fotografiadas. Se transcriben las marcas visibles (✓ / ✗ / trazos) junto a cada ítem, y las calificaciones por punto.

**Datos de la mesa:** 30/07/2026, comienzo 17:20, hora de finalización 21 Hs. N° de hojas entregadas: 1 por problema.

**Requisitos para rendir el final:** Tener aprobadas: Electrónica Aplicada I, Medios de Enlace, Análisis de Señales y Sistemas y Probabilidad y Estadísticas. Están exceptuados aquellos que regularizaron la materia en el último ciclo lectivo.

**Forma de evaluación:** El examen se aprueba si la sumatoria alcanza seis o más, sin redondeo. Para aprobar se debe desarrollar al menos el 25% del total de cada punto. Consecuentemente un punto sin desarrollo alguno implica que el examen está desaprobado; por más que el resto esté bien.

## Resultado

| Problema | Tema | Puntaje | Obtenido | Evaluador |
|---|---|---|---|---|
| 1 | Modulación lineal | 2,5 | **0,5** | RF |
| 2 | Modulación exponencial | 2,5 | **1,5** | RD |
| 3 | SS/OFDM | 2,5 | **1,40** | RF |
| 4 | Teoría de la información | 2,5 | **0,5** | RD |
| | **Total** | **10** | **3,90** | |

**Nota final asentada: 4 (CUATRO) — desaprobado.**

> En el recuadro del Problema 2 hay un valor tachado antes del 1,5, y una segunda casilla con **1,2** en verde e iniciales distintas — posible segunda corrección o revisión. La suma de la primera columna (0,5 + 1,5 + 1,40 + 0,5) da 3,90, consistente con el 4 asentado en la carátula.

---

## Ejercicio 1: Modulación lineal [2,5 puntos] — obtenido 0,5

**Enunciado:**

Un mensaje compuesto por tres tonos provenientes de fuentes distintas,

$$m(t) = A_1\cos(2\pi f_1 t) + 0{,}8\,A_1\cos(2\pi f_2 t) + 1{,}6\,A_1\cos(2\pi f_3 t)$$

modula al **80%, referido al valor pico del mensaje compuesto**, una señal de Amplitud Modulada (AM) que se transmite con una **potencia total normalizada de 252,025 Watts**. Se pide determinar:

a) Potencia normalizada de la portadora en Watts y dBW. [0,5 puntos] *(marca roja al margen)*

b) Potencia normalizada emitida en banda lateral superior en Watts y dBW. [0,5 puntos]

c) Densidad espectral de potencia de la señal modulada, considerando sólo frecuencias positivas, como se vería en un analizador de espectro en ausencia de ruido y expresada en Watts. [0,5 puntos] *(marca roja al margen)*

d) Eficiencia energética de la señal modulada. [0,25 puntos] *(trazo al margen)*

e) El factor de cresta de $m(t)$. [0,25 puntos] *(trazo al margen)*

f) Potencia pico de envolvente normalizada de la señal modulada en Watts y dBW. [0,5 puntos] *(trazo al margen)*

**Nota:** suponga $f_1 < f_2 < f_3$

---

## Ejercicio 2: Modulación exponencial [2,5 puntos] — obtenido 1,5

**Enunciado:**

Dada la siguiente expresión de una portadora modulada en frecuencia:

$$x_c(t) = 100\cos\left[2\pi\cdot 90\cdot 10^6\, t + 2\sin\left(18{,}85\cdot 10^3\, t\right)\right]$$

Determinar:

a) Índice de modulación. [0,25 puntos] — ✅

b) Ancho de banda de la señal modulante. [0,5 puntos] — ✅

c) Máxima desviación de frecuencia. [0,5 puntos] — ✅

d) Ancho de banda de la señal modulada. [0,5 puntos] — ❌

e) Potencia media sobre una antena con 50 ohms de impedancia expresada en dBW. [0,25 puntos] — ✅

f) Si a la portadora modulada se la pasa por un triplicador de frecuencia cuál será el nuevo valor del ancho de banda. [0,5 puntos] — ❌

---

## Ejercicio 3: SS/OFDM [2,5 puntos] — obtenido 1,40

**Enunciado:**

Sea un sistema OFDM como el de la figura:

[Diagrama en bloques de un transmisor OFDM: $m(t)$ datos seriales → Serial a paralelo → IFFT → Paralelo a serial → dos ramas en cuadratura, $x(t)$ multiplicada por $\cos(\omega_c t)$ y $y(t)$ por $\text{sen}(\omega_c t)$, sumadas con signo $+$ y $-$ en un sumador $\Sigma$ → señal OFDM $v(t) = x(t)\cos(\omega_c t) - y(t)\,\text{sen}(\omega_c t)$. El bloque de RF incluye un oscilador de portadora $f_c$ y un corrimiento de fase de $-90°$.]

Siendo $m(t)$ el mensaje digital binario que ingresa a una tasa de binits, $R_b = 16$ Mbps, considerando que el sistema genera una señal OFDM de **8192 portadoras** y la modulación de cada portadora es **16-QAM**, se pide:

a) Calcular el tiempo de símbolo de OFDM, $T_S$. [0,5 puntos] — ✅

b) Calcular el ancho de banda mínimo ideal ($B_T$) de la señal OFDM. [0,25 puntos] — ✅

c) Determinar las frecuencias de las dos subportadoras inferiores, las dos subportadoras más próximas a la frecuencia central y las dos superiores. Todas relativas a una frecuencia de transmisión central, "$f_{central}$". [0,5 puntos] — *(marca "B" al margen)*

d) Representar el espectro de potencia de salida si la cadena de binits de entrada fuera una sucesión continua de **"0110's"**. [0,5 puntos] — *(trazo al margen)*

e) Siendo que la frecuencia central a la que va a ser transmitida esta señal es de **3,9 GHz**, proponga y justifique un valor adecuado para $f_c$ en el oscilador de portadora de la figura. [0,5 puntos] — ❌

f) Calcule el tiempo de símbolo si la tasa de binits citada en vez de transmitir en OFDM, se envía con una sola portadora modulada en **1024-QAM**, $T_{S1c}$. [0,25 puntos] — ✅

---

## Ejercicio 4: Teoría de la información [2,5 puntos] — obtenido 0,5

**Enunciado:**

Una fuente de información estacionaria sin memoria produce **seis símbolos diferentes**, con probabilidades: **1/4, 1/4, 1/8, 1/8, 1/8 y 1/8**.

Estos son emitidos a una velocidad de **200 símbolos por segundo** y se los quiere transmitir por un canal binario que tiene una **capacidad máxima $C$ igual a 580 bps**.

a) Determinar si la fuente puede transmitirse por el canal especificado. Justifique. [0,5 puntos] — ✅

b) En caso de ser factible establecer una **técnica de codificación binaria de la fuente** tal que pueda ser transmitida por el canal. [0,5 puntos] — *(sin marca)*

c) ¿Cuál sería la **velocidad de la codificación binaria** propuesta? [0,5 puntos] — *(sin marca)*

d) Una fuente de datos produce **16 símbolos** distintos, independientes y equiprobables, y estos se transmiten agrupados en **bloques de 15** separados por un **pulso de sincronización**; dentro del bloque cada símbolo tiene una duración de **1 μSg** y el pulso de sincronización dura **5 μSg**. Determine la tasa de información. [1 punto] — *(sin marca)*

---

## Observaciones para la preparación de septiembre

**Los cuatro temas coinciden exactamente con los de mayor frecuencia del corpus**: Lineal, Exponencial, SS/OFDM y Teoría de la Información. No apareció PCM como problema propio, ni Ruido, ni Modulación Digital como tema separado.

**El Ejercicio 3 es prácticamente el mismo problema que `F_Comu_2022-07-21`**, que sí se había estudiado: misma $R_b = 16$ Mbps, misma 16-QAM por subportadora, mismos ítems (tiempo de símbolo, ancho de banda, frecuencias de subportadoras relativas a la central, $f_c$ para centrar en 3,9 GHz, y comparación contra una sola portadora en 1024-QAM). Cambian **8192 subportadoras en vez de 4096** y la entrada patológica es **"0110" repetido** en vez de todo ceros. Fue el mejor puntaje de los cuatro (1,40).

**El Ejercicio 4 b) y c) son codificación de fuente** (asignar un código binario de longitud variable a símbolos con $p = 1/4, 1/4, 1/8, 1/8, 1/8, 1/8$ — un caso donde Huffman/Shannon-Fano da longitudes exactas de 2,2,3,3,3,3 y $\bar L = H = 2{,}5$ bits/símbolo). **Valen 1 punto combinados.** Ese contenido había sido descartado del formulario por no aparecer en el corpus de 42 finales — y acá apareció.

**El Ejercicio 2 d) y f) son las dos fórmulas centrales del tema**: Carson ($B_T = 2(\Delta f + f_m)$) y el efecto de un multiplicador de frecuencia ($\times n$ escala $f_c$, $\Delta f$ y $\beta$, pero **no** $f_m$). Ambas estaban en el formulario.

**El Ejercicio 1 es AM multitono con factor de cresta**, con el criterio de índice referido al **valor pico del mensaje compuesto** — el caso que exige normalizar por $\max|m(t)| = A_1(1 + 0{,}8 + 1{,}6) = 3{,}4\,A_1$ y no por cada tono por separado.
