# Examen Final SC — 17/07/2025

*Fuente: `F_Comu_2025_07_17_Doallo_res.pdf`*

**Requisitos para rendir el final:** Tener aprobadas Electrónica Aplicada I, Medios de Enlace, Análisis de Señales y Sistemas y Probabilidad y Estadísticas. Están exceptuados aquellos que regularizaron la materia en el último ciclo lectivo.

**Forma de evaluación:** El examen se aprueba si la sumatoria alcanza seis o más, sin redondeo. Para aprobar se debe desarrollar al menos el 25% del total de cada punto. Consecuentemente un punto sin desarrollo alguno implica que el examen está desaprobado; por más que el resto esté bien.

*Nota: examen escaneado a mano (hoja de respuesta del estudiante "Doallo"). Cada ejercicio indica en la hoja de resolución en qué final anterior se basó el estudiante (variante numérica); se transcribe fielmente el desarrollo.*

---

## Ejercicio 1: Modulación exponencial [2,5 puntos]

**Enunciado:**

Una portadora de frecuencia 146 MHz es modulada exponencialmente por un tono según la siguiente expresión, obtenida a la salida del modulador:

$$x(t) = 100\cdot\cos\left[2\pi\cdot146\times10^6\cdot t + 2{,}5\cdot\sin(4000\pi t)\right] \text{ [Volts]}$$

Se pide:

a) La desviación máxima de frecuencia, $\Delta f$. [0,25 puntos]

b) La desviación máxima de fase, $\Delta\varphi$. [0,25 puntos]

c) El ancho de banda de transmisión, $B_T$. [0,5 puntos]

d) Si el modulador (considerado ideal) fuera de frecuencia, con constante de desviación de frecuencia de 10 KHz/Volt, ¿Cuál sería la expresión matemática de la señal modulante o mensaje? [0,5 puntos]

e) Si la señal $x(t)$ se pasa por **tres duplicadores** de frecuencia en serie sin afectar su amplitud, ¿cuál es la expresión matemática de salida? [0,5 puntos]

f) Cuando se reduce a la mitad la frecuencia del tono modulante, manteniendo invariable su amplitud, a la salida del modulador se obtiene:

$$x(t) = 100\cdot\cos\left[2\pi\cdot146\times10^6\cdot t + 5\cdot\sin(2000\pi t)\right] \text{ [Volts]}$$

¿Podría determinar si es un modulador de fase o de frecuencia? Justifique su respuesta. [0,5 puntos]

<details>
<summary>Respuesta</summary>

**a)** $\beta = 2{,}5$ (índice de modulación), $\beta = \dfrac{\Delta f}{f_m}$, con $f_m = 2$ kHz (de $4000\pi t = 2\pi\cdot2000\cdot t$) $\Rightarrow \Delta f = 5$ kHz

**b)** $\Delta\theta = \beta \Rightarrow \Delta\varphi = 2{,}5$ rad

**c)** $B_T = 2(\beta+1)f_m$, con $\beta=2{,}5$: $B_T = 18$ kHz

**d)** Si el modulador fuera FM: $2{,}5\sin(4000\pi t) = 2\pi D_f\displaystyle\int_{}^{t} m(\lambda)\,d\lambda$

Derivando ambos miembros: $\dfrac{d}{dt}\left[2{,}5\sin(4000\pi t)\right] = 2\pi D_f\cdot m(t)$

$2{,}5\cos(4000\pi t)\cdot 4000\pi = 2\pi D_f\cdot m(t)$

$m(t) = \dfrac{2{,}5\cdot 2000}{10\text{ kHz/Volt}}\cdot\cos(4000\pi t)$

$$\boxed{m(t) = 0{,}5\cos(4000\pi t)}$$

**e)** Al pasar por tres duplicadores de frecuencia en serie ($2^3 = 8$), tanto la frecuencia de portadora como el índice de fase se multiplican por 8:

$$\boxed{x_1(t) = 100\cdot\cos\left[2\pi\cdot1{,}168\text{ GHz}\cdot t + 20\sin(4000\pi t)\right]}$$

**f)** Se reduce a la mitad la frecuencia del tono modulante y el índice se duplica ($2{,}5 \to 5$) $\Rightarrow$ es un modulador de **FM** (en FM, $\beta = \Delta f/f_m$ es inversamente proporcional a $f_m$ para una misma $\Delta f$; al reducir $f_m$ a la mitad, $\beta$ se duplica, tal como se observa).

</details>

---

## Ejercicio 2: Modulación por codificación de pulsos [2,5 puntos]

**Enunciado:**

a) Mencione dos condiciones límites que debe tener la señal modulante para ser transmitida. [0,25 puntos]

b) PCM para enviar canales de telefonía emplea cuantificación no lineal, ¿por qué? Justifique su respuesta. [0,25 puntos]

c) Pensando en la recepción de un canal telefónico de 3,4 KHz de ancho de banda (considerando que el factor de cresta del mensaje es 3), utilizando PCM con tasa de error de bit en el canal de $10^{-7}$ y 8 bits de cuantificación lineal. ¿Qué relación señal a ruido se tiene a la salida del receptor? [0,5 puntos]

*Nota: Supuesto el receptor ideal, no aporta ruido a la señal recibida.*

d) ¿Qué tiene más importancia en la relación señal a ruido determinada en c), el ruido por cuantificación o el ruido por error de bit? Justifique la respuesta. [0,25 puntos]

e) En las condiciones del punto c), ¿Hasta qué valor de Cifra de ruido total del receptor es admisible si se quiere 28,4 dB de relación señal a ruido a la salida del mismo? Justifique su respuesta. [0,75 puntos]

*Nota: Supuesta la entrada y todo el sistema a temperatura ambiente, $T_0=290$ K y modulación BPSK y filtro acoplado en el receptor.*

f) En las condiciones del punto c), ¿Qué relación señal a ruido a la entrada del receptor es necesaria si se quiere 46 dB de relación señal a ruido a la salida del mismo? Justifique su respuesta. [0,5 puntos]

*Nota: Supuesta la entrada y todo el sistema a temperatura ambiente, $T_0=290$ K y modulación BPSK y filtro acoplado en el receptor.*

<details>
<summary>Respuesta</summary>

**a)** Amplitud menor a la del ADC (cuanto más cercano al límite, mejor). Frecuencia máxima inferior a la mitad de la frecuencia de muestreo del ADC (Nyquist). [0,25]

**b)** Emplea Ley A o $\mu$ para reducir el ruido de cuantificación (equipara la SNR para señales de baja amplitud, típicas en voz). [0,25]

**c)** $$\frac{S}{N} = \frac{3M^2}{1+4\cdot P_e\cdot(M^2-1)}\cdot\frac{1}{F_c^2}$$

Con $M=256$ (8 bits), $F_c=3$, $P_e=10^{-7}$: $S/N = 691{,}82 = 28{,}4$ dB

**d)** $4\cdot P_e\cdot(M^2-1) = 0{,}026 \ll 1 \Rightarrow$ el ruido de cuantificación tiene más importancia. [0,25]

**e)** Con $F_c=3$, $M=256$: $S/N = 691{,}82$ (28,4 dB) — mismo resultado de c).

Despejando la $P_e$ que produciría este mismo resultado sin la aproximación: $P_e' = 1{,}17\times10^{-4}$

- Con $P_e=10^{-7} \Rightarrow z=5{,}2 \Rightarrow E_b/N_0 = 11{,}3$ dB
- Con $P_e'=1{,}17\times10^{-4} \Rightarrow z'=3{,}68 \Rightarrow E_b'/N_0 = 8{,}3$ dB

$$CF = \frac{E_b}{N_0} - \frac{E_b'}{N_0} \Rightarrow \boxed{CF = 3\text{ dB}}$$

**f)** No se puede lograr, porque incluso con $P_e=0$ (BER nulo): $S/N' = \dfrac{3M^2}{F_c^2} \Rightarrow S/N = 45{,}4$ dB $< 46$ dB solicitados. Ya es ruido de cuantificación, que el receptor no puede mejorar.

</details>

---

## Ejercicio 3: Modulación digital [2,5 puntos]

**Enunciado:**

Dada una señal digital pasabanda 16 QAM con frecuencia de portadora de 50 MHz, Amplitud máxima de 6 milivolts (Pico), símbolos equiprobables y una tasa de transporte 256.000 bits por segundo.

Se pide:

a) Determinar el ancho de banda de nulo a nulo. [0,5 puntos]

b) La densidad espectral de potencia normalizada de la señal, 384 KHz entorno de la frecuencia de portadora, con suficiente detalle. [0,5 puntos]

c) Determinar la potencia normalizada de la señal, expresada en dBm. [0,5 puntos]

d) Determinar la densidad de potencia normalizada de la señal, expresada en dBm/Hz, en 50,096 MHz. [0,5 puntos]

e) Si el ancho de banda equivalente de ruido es igual al ancho de banda calculado en a) y la densidad espectral de ruido $8\times10^{-15}$ Watts/Hz, determinar la relación señal a ruido. [0,5 puntos]

<details>
<summary>Respuesta</summary>

**a)** $R_b=256000$ bps; $\ell=4$ (16-QAM) $\Rightarrow D = R_b/\ell = 64.000$ baudios

$$\boxed{B_{null-null} = 2D = 128 \text{ kHz}}$$

**b)** Espectro (lóbulo principal centrado en $f_c=50$ MHz, primeros nulos en $f_c\pm64$ kHz, con lóbulos secundarios hasta $\pm128$ kHz y $\pm192$ kHz): nivel relativo del primer lóbulo secundario $\approx -13{,}5$ dB respecto al pico, y $\approx -4{,}4$ dB en el punto marcado a 384 kHz de la portadora (ver diagrama manuscrito con nulos marcados en $-192$k, $-128$k, $-64$k, $+64$k, $+128$k, $+192$k respecto a $f_c$).

**c)** Constelación 16-QAM con radios: $\Delta_1 = 6$ mV, $\Delta_2=\sqrt{20}$ mV, $\Delta_3 = 2$ mV.

$$Pot = \frac{\Delta_1^2}{2}\cdot\frac{1}{4} + \frac{\Delta_2^2}{2}\cdot\frac{1}{2} + \frac{\Delta_3^2}{2}\cdot\frac{1}{4}$$

$$\boxed{Pot = 10\ \mu W = -20 \text{ dBm}}$$

**d)** $$PSD = K\left(\frac{\sin(\pi f \ell T_b)}{\pi f \ell T_b}\right)^2, \quad K = 2\cdot Pot\cdot\ell\cdot T_b$$

Con $\ell=4$, $T_b=1/256000$: $K = 312{,}5$ pW/Hz

$$PSD(96\text{ kHz offset}) = \frac{K}{(1{,}5\pi)^2} = 14{,}072 \text{ pW/Hz}$$

$$PSD_{S(f)} = \frac{PSD}{4} = 3{,}5 \text{ pW/Hz}$$

$$\boxed{PSD(50{,}096\text{ MHz}) = -84{,}5 \text{ dBm/Hz}}$$

**e)** $B_N = 128$ kHz $\Rightarrow N = B_N\cdot8\times10^{-15}\text{ W/Hz} = 1{,}024\times10^{-9}$ W

$S = 10\ \mu W = 1\times10^{-5}$ W

$$S/N = 9766 \Rightarrow \boxed{S/N = 39{,}9 \text{ dB}}$$

</details>

---

## Ejercicio 4: Teoría de la información [2,5 puntos]

**Enunciado:**

De acuerdo a las características de la televisión monocromática de 625 líneas por imagen, 25 imágenes por segundo y 720 puntos por línea. Calcular:

a) Tasa de información mínima requerida al canal de transmisión, asumiendo que el sistema utiliza 12 niveles de grises equiprobables por punto. [0,5 puntos]

b) El ancho de banda mínimo si se necesita una relación señal a ruido de 30 dB. [0,5 puntos]

c) Si esta señal se digitaliza utilizando una codificación de 4 bits por punto, qué ancho de banda mínimo sería necesario en banda base. [0,5 puntos]

d) Si dispongo de un canal de 10 MHz, qué modulación sugiere con un factor de roll-off de 0,25. Justifique su respuesta indicando el ancho de banda requerido utilizando esa modulación propuesta. [0,5 puntos]

e) En las condiciones del punto anterior, ¿Cuál es la mínima relación señal a ruido ideal? [0,5 puntos]

<details>
<summary>Respuesta</summary>

**a)** $$R = 625\times720\times25\times\log_2(12) \Rightarrow \boxed{R = 40{,}336 \text{ Mb/s}}$$

**b)** $C = B\log_2(1+S/N)$, con $S/N = 1000$ (30 dB):

$$\boxed{B_{min} = 4{,}0463 \text{ MHz}}$$

**c)** $R_b = 625\times720\times25\times4 \Rightarrow R_b = 45\times10^6$ bits/s

$$\boxed{B_{min} = \frac{R_b}{2} = 22{,}5 \text{ MHz}}$$

**d)** $D = \dfrac{B_T}{1+r}$; con $B_T=10$ MHz, $r=0{,}25 \Rightarrow D = 8\times10^6$ baudios.

$R_b = 45\times10^6$ binits/s; $\ell = R_b/D = 5{,}625 \Rightarrow \ell = 6$ (redondeando hacia arriba)

$$\boxed{\ell=6 \Rightarrow \text{64-QAM}}$$

**e)** Con $\ell=6$: $D = R_b/\ell = 45\times10^6/6 = 7{,}5\times10^6$ baudios

$B_T = D\cdot(1+0{,}25)$

$$\boxed{B_{T,min} = 9{,}375 \text{ MHz}}$$

</details>
