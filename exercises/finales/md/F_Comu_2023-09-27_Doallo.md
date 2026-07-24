# Examen Final SC — 27/09/2023

*Fuente: `F_Comu_2023-09-27_Doallo.pdf`*

> **Nota:** este documento es un examen **en blanco** (sin resolución de ningún estudiante) — no hay sección de Respuesta. Hora de finalización indicada en el enunciado: 21 Hs.

**Requisitos para rendir el final:** Tener aprobadas Electrónica Aplicada I, Medios de Enlace, Análisis de Señales y Sistemas y Probabilidad y Estadísticas. Están exceptuados aquellos que regularizaron la materia en el último ciclo lectivo.

**Forma de evaluación:** El examen se aprueba si la sumatoria alcanza seis o más, sin redondeo. Para aprobar se debe desarrollar al menos el 25% del total de cada punto. Consecuentemente un punto sin desarrollo alguno implica que el examen está desaprobado; por más que el resto esté bien.

---

## Ejercicio 1: Modulación lineal [2,5 puntos]

**Enunciado:**

En un modulador/transmisor de AM se inyecta una señal modulante senoidal representada por $m(t) = A_m\cos(2\pi\cdot5000\cdot t)$, con $A_m = 4$ Volts y en su salida, sobre una impedancia de carga de 50 Ohms, se visualiza mediante un osciloscopio la siguiente forma de onda donde la amplitud máxima de la señal modulada alcanza 180 Volts y la mínima 20 Volts (valores pico). Asuma frecuencia de portadora 1 MHz.

*(Diagrama: envolvente de AM en el osciloscopio, mostrando "Amplitud máx." y "Amplitud mín." marcadas sobre la forma de onda modulada en el tiempo.)*

Determinar:

a) Amplitud de la portadora. [0,25 puntos]

b) Índice de modulación. [0,25 puntos]

c) Expresión de la onda modulada $s(t)$, en función de $m(t)$. [0,25 puntos]

d) Potencia de la portadora ($P_C$) sobre la carga en dBW. [0,25 puntos]

e) Potencia de cada una de las bandas laterales ($P_{SSB}$) sobre la carga en dBW. [0,25 puntos]

f) Potencia pico de envolvente sobre la carga en dBW. [0,25 puntos]

g) Qué valor debería alcanzar $A_m$ para lograr 90% de índice de modulación manteniéndose la amplitud de portadora del enunciado original. [0,5 puntos]

h) La potencia total sobre la carga, expresada en dBW, si ahora la señal modulante es una cuadrada de 8 Volts de amplitud pico a pico, con valor medio nulo, 50% de ciclo de actividad y 100 Hz de frecuencia. [0,5 puntos]

---

## Ejercicio 2: PCM [2,5 puntos]

**Enunciado:**

Se desea grabar digitalmente señales de audio en un CD usando PCM. Considerando que la señal de audio tiene un ancho de banda de 15 kHz y que las muestras se cuantifican en 65.536 niveles distribuidos uniformemente. Determinar:

a) La frecuencia mínima ideal de muestreo (tasa de Nyquist). [0,25 puntos]

b) La cantidad de dígitos binarios utilizados para codificar cada muestra. [0,5 puntos]

c) La tasa de transmisión binaria para muestreo a tasa de Nyquist. [0,25 puntos]

d) La tasa de bits para el caso de utilizar una frecuencia de muestreo de 44.100 Hz. [0,5 puntos]

e) La relación señal a ruido de cuantificación para la señal de amplitud máxima posible, expresada en dB, si la señal de audio tiene un factor de cresta de 2,5. [0,5 puntos]

f) La mínima amplitud relativa a la amplitud máxima, que asegure relación señal a ruido de cuantificación de 50 dB si la señal de audio tiene un factor de cresta de 2,5. [0,5 puntos]

---

## Ejercicio 3: Ruido [2,5 puntos]

**Enunciado:**

Un sistema de transmisión por cable, a temperatura $T=T_0$, con atenuación de 2 dB/Km, distancia total de 120 Km y 6 secciones de repetición iguales tiene en el destinatario una relación señal a ruido, $(S/N)_D = 30$ dB.

En cada sección de repetición, aquí representada, se observa que la ganancia del repetidor, considerado ideal ($F=1$), compensa la atenuación del cable:

$$\text{Cable}\ (g_c = 1/L_c,\ \mathcal{T}_{amb}=\mathcal{T}_0) \to \text{Repeater}\ (g_r = L_c,\ F_r)$$

Se pide:

a) Encontrar el nuevo valor de $(S/N)_D$ si el número de secciones de repetición se incrementa a 12. Considerando: la misma distancia, relación señal a ruido a la entrada del sistema y demás condiciones citadas en el enunciado. [0,75 puntos]

b) La relación señal a ruido a la entrada del sistema. [0,5 puntos]

c) Ídem a) considerando ahora que los repetidores poseen una cifra de ruido de 6 dB. [0,75 puntos]

d) Considerando el escenario del enunciado (6 secciones) y si cada sección fuese compuesta primero por el repetidor y luego el cable. ¿Qué ventajas y/o problemas encuentra?, ¿Sería viable? Suponga el caso en que la potencia a la entrada y a la salida del sistema es de 100 miliwatts. Justifique la respuesta. [0,5 puntos]

La temperatura equivalente de ruido a la entrada del sistema de transmisión por cable, en la primera etapa, es $T_0$.

---

## Ejercicio 4: OFDM [2,5 puntos]

**Enunciado:**

Dada una señal OFDM compuesta por 48 portadoras, cada una de ellas modulada en 16-QAM, con duración de símbolo OFDM de cuarenta microsegundos. Se pide:

a) Calcular la tasa de información en bits por segundo que transporta la señal. [0,5 puntos]

b) Calcular el ancho de banda mínimo. [0,3 puntos]

c) Calcular la cantidad de bits que transporta en cada símbolo OFDM. [0,3 puntos]

d) Calcular la eficiencia espectral para ancho de banda mínimo. [0,4 puntos]

e) Calcular el ancho de banda mínimo si en vez de transmitir la señal OFDM se transmite la misma tasa de información (calculada en a) pero en una sola portadora modulada en 16-QAM. [0,5 puntos]

f) Indicar la ventaja de emplear la señal descrita en el enunciado versus transmitir la misma tasa de información (calculada en a) pero en una sola portadora modulada en 16-QAM. [0,5 puntos]

---
