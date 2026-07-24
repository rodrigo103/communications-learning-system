# Examen Final SC — 24/02/2022 (con resolución)

*Fuente: `F_Comu_2022-02-24_X_res.pdf`*

*Nota: este PDF es el escaneo manuscrito de la hoja de un estudiante real (Nicolás Rositt, Legajo 137211-7), corregida por el profesor con marcas de verificación (un símbolo similar a la letra griega β, a veces con superíndice "⁻" indicando una salvedad menor), checkmarks, y anotaciones puntuales ("R", "NO"). Se observan notas parciales manuscritas por ejercicio: Ejercicio 1 = 2,4/2,5; Ejercicio 2 = 1,5/2,5; Ejercicio 3 = 2,0/2,5; Ejercicio 4 = 2,0/2,5 (suma ≈ 7,9/10; no hay una nota final explícita en el documento, es una suma de las parciales visibles). En el Ejercicio 3 (OFDM) el estudiante desarrolló todo el cálculo con prefijo kilo (Kbps, kHz, kS/s), pero su propio resultado intermedio de $T_b=10,42$ ns/bit ya fija la escala correcta en nanosegundos/Megabits; el profesor marcó esta confusión de unidades circulando la "K" y anotando "M" en varios resultados. Se transcribe el desarrollo tal como aparece, con la unidad corregida (Mega) y aclarando el valor tal como fue escrito originalmente (Kilo).*

**Requisitos para rendir el final:** Tener aprobadas: Electrónica Aplicada I, Medios de Enlace, Análisis de Señales y Sistemas y Probabilidad y Estadísticas. Están exceptuados aquellos que regularizaron la materia en el último ciclo lectivo.

**Forma de evaluación:** El examen se aprueba si la sumatoria alcanza seis o más, sin redondeo. Para aprobar se debe desarrollar al menos el 25% del total de cada punto. Consecuentemente un punto sin desarrollo alguno implica que el examen está desaprobado; por más que el resto esté bien.

---

## Ejercicio 1: Modulación exponencial [2,5 puntos]

**Enunciado:**

1. La señal de audio está modulada en FM. El ancho de banda disponible para acomodar la señal de audio es de 50 KHz. Si la señal moduladora de audio contiene frecuencias entre 30 Hz y 15 KHz, determinar su amplitud máxima para hacer uso óptimo del ancho de banda disponible.

   La constante de desviación de frecuencia del modulador de FM es de $10^4$ Hz/V. [0,5 puntos]

2. En la siguiente figura se muestra el diagrama en bloques de un transmisor de FM, el ancho de banda de la señal modulante va de 20 Hz a 5 KHz. La frecuencia de la portadora a la salida del sistema debe ser 145 MHz y su ancho de banda a la salida de 25 KHz.

   [Diagrama en bloques: Modulador de FM ($f_{mod} = 3\text{ MHz}$, $\Delta F=?$) → mezclador ($\times$) [con entrada de Oscilador local, $f_O=?$] → Filtro Pasabanda ($f_c=?$, $B_T=?$) → Multiplicador de frecuencia $\times 8$ → Amplificador → Salida]

   Se solicita:

   a) Halle el ancho de banda mínimo y la frecuencia central requeridos para el filtro pasa banda (Considérese Brickwall). [0,5 puntos]

   b) Calcule la frecuencia del oscilador local, $f_O$, considerando que el filtro pasa banda opera con la suma de los espectros de las señales a la entrada del multiplicador. [0,5 puntos]

   c) Determine la desviación pico del modulador de FM, en el primer bloque del diagrama. [0,5 puntos]

   d) Si dispone de un oscilador local de 6,0625 MHz, ¿Qué ajustes habría que hacer al sistema para que se mantenga la frecuencia de portadora a la salida (145 MHz) y su ancho de banda a la salida (25 KHz) invariables? [0,5 puntos]

<details>
<summary>Respuesta</summary>

**1)** Datos: $BW$ disponible $=50\text{ kHz}$, $f_m$: 30 Hz a 15 kHz, $k_f=1\times10^4\text{ Hz/V}$.

Por la regla de Carson, $BW=2(\beta+1)f_{m,max}$, con $\beta=\dfrac{k_f\cdot A_m}{f_{m,max}}$ (siendo $k_f\cdot A_m=\Delta f$).

Despejando $\beta$:

$$\beta=\frac{BW}{2f_{m,max}}-1=\frac{50\text{ kHz}}{2\cdot 15\text{ kHz}}-1=\frac{2}{3}$$

Despejando la amplitud:

$$A_m=\frac{\beta\cdot f_{m,max}}{k_f}=\frac{\frac{2}{3}\cdot 15\text{ kHz}}{10^4\text{ Hz/V}}$$

$$\boxed{A_m=1\text{ V}}$$

**2)** Datos de la segunda parte: $f_m$: 20 Hz a 5 kHz, $f_{mod}=3\text{ MHz}$, $f_c$(salida)$=145\text{ MHz}$, $BW$(salida)$=25\text{ kHz}$, multiplicador $\times 8$.

**a)** Los osciladores no modifican $\Delta f$ (ni por lo tanto $\beta$), pero los multiplicadores sí modifican tanto $\Delta f$ como la frecuencia, modificando $\beta$.

$$\beta=\frac{BW_{FM}}{2f_{m,max}}-1=\frac{25\text{ kHz}}{2\cdot 5\text{ kHz}}-1=1,5$$

$$\Delta f=\beta\cdot f_{m,max}=1,5\cdot 5\text{ kHz}=7,5\text{ kHz}$$

Antes del multiplicador $\times 8$:

$$f_{c,\text{filtro}}=\frac{145\text{ MHz}}{8}=18,125\text{ MHz}, \qquad \Delta f_{\text{filtro}}=\frac{7,5\text{ kHz}}{8}=937,5\text{ Hz}$$

$$\beta_{\text{filtro}}=\frac{\Delta f_{\text{filtro}}}{f_{m,max}}=\frac{937,5\text{ Hz}}{5\text{ kHz}}=0,1875$$

Como $\beta_{\text{filtro}}<0,5$, en ese punto de la cadena se puede considerar NBFM, por lo que el ancho de banda del filtro pasabanda es:

$$BW_{\text{filtro}}=2f_{m,max}=2\cdot 5\text{ kHz}=10\text{ kHz}$$

$$\boxed{f_c=18,125\text{ MHz}\ ;\ BW=10\text{ kHz}}$$

**b)** El filtro pasabanda opera con la suma de las frecuencias a la entrada del mezclador: $f_{c,\text{filtro}}=f_{osc}+f_{mod}$

$$f_{osc}=f_{c,\text{filtro}}-f_{mod}=18,125\text{ MHz}-3\text{ MHz}=\boxed{15,125\text{ MHz}}$$

**c)** La desviación pico del modulador de FM (primer bloque del diagrama) es la ya calculada antes del multiplicador:

$$\boxed{\Delta f=937,5\text{ Hz}}$$

**d)** Con un nuevo oscilador local de 6,0625 MHz:

$$f_{c,\text{filtro}}'=f_{osc}'+f_{mod}=6,0625\text{ MHz}+3\text{ MHz}=9,0625\text{ MHz}$$

Para mantener $f_c$ de salida $=145\text{ MHz}$, el multiplicador necesario es:

$$\text{Multiplicador}=\frac{f_c}{f_{c,\text{filtro}}'}=\frac{145\text{ MHz}}{9,0625\text{ MHz}}=\boxed{16}$$

Hay que cambiar el multiplicador de $\times 8$ a $\times 16$. Esto por sí solo aumentaría el $\Delta f$ (y por lo tanto el $BW$ de salida), pero si además se reduce a la mitad la amplitud de la señal modulante, se puede mantener el mismo $BW$ de salida (25 kHz).

**Propuesta final del estudiante:** cambiar el multiplicador a $\times 16$ y reducir a la mitad (½) la amplitud de la señal modulante.

*(Todo el Ejercicio 1 fue marcado como correcto por el profesor — checkmarks en cada inciso. Nota parcial visible: 2,4/2,5.)*

</details>

---

## Ejercicio 2: PCM [2,5 puntos]

**Enunciado:**

Se desea armar un multiplex en el tiempo con ancho de banda mínimo ideal de señales PAM/TDM, integrado por: dos canales de voz con un ancho de banda de 3.400 Hz cada uno, un canal de 850 Hz y tres de 1.700 Hz.

Se pide:

a) Dibujar el diagrama en bloques de sistema transmisor y receptor PAM/TDM, asumiendo que el sincronismo es externo. [0,5 puntos]

b) Dibujar el diagrama en bloques de sistema sólo del transmisor, pero atendiendo el envío del sincronismo también. [0,5 puntos]

c) Cuál es el ancho de banda mínimo ideal a la salida de a) y de b). [0,3 puntos]

d) Si en vez de armar un multiplex en el tiempo se emplea uno en frecuencia FDM (Considere filtros ideales, Brickwall), ¿Cuál sería el ancho de banda mínimo ideal? [0,6 puntos]

e) Implementar (Diagrama en bloques sólo del transmisor) de lo propuesto en d) [0,6 puntos]

<details>
<summary>Respuesta</summary>

Datos: 2 canales de 3.400 Hz, 1 canal de 850 Hz, 3 canales de 1.700 Hz (6 canales en total).

**a)-b)** El estudiante arma el multiplex PAM/TDM por etapas, sobremuestreando los canales de menor ancho de banda para simplificar la combinación:

- Una primera rama combina el canal de 850 Hz (sobremuestreado a 3.400 muestras/s) con un canal de 1.700 Hz, mediante un conmutador que entrega 6.800 muestras/s.
- Otra rama combina dos canales de 1.700 Hz de la misma manera, también a 6.800 muestras/s.
- Los dos canales de 3.400 Hz restantes se incorporan sin sobremuestreo adicional.
- Todas las ramas confluyen en un conmutador final a 27.200 muestras/s, que tras un filtro pasabajos ideal entrega una salida efectiva de 13.600 Hz.
- En b) se repite el mismo esquema, incorporando además un canal de sincronismo (agrupado junto con el canal de 850 Hz en la primera etapa de sobremuestreo), manteniendo la misma tasa combinada de 27.200 muestras/s → 13.600 Hz de salida.

**c)** El ancho de banda mínimo ideal a la salida es de $\boxed{13.600\text{ Hz}}$ para ambos casos (a y b).

**d)-e)** El estudiante resuelve d) y e) en conjunto, con un único diagrama de transmisor FDM: cada uno de los 6 canales (más el sincronismo) pasa por un filtro pasabajos, luego un mezclador con un oscilador individual ($Osc_1$ a $Osc_{10}$) y un filtro pasabanda, sumando finalmente todas las bandas trasladadas en frecuencia para formar la señal FDM compuesta.

Conclusión del estudiante: *"El ancho de banda mínimo ideal es de 13.600 Hz, igual que en TDM por utilizar filtros ideales tipo brickwall."*

**El profesor marcó esta conclusión como incorrecta** (la circuló y anotó "NO" al lado). El documento no deja registrado explícitamente cuál sería, según el profesor, el ancho de banda correcto para el caso FDM.

*(Nota parcial visible para este ejercicio: 1,5/2,5. En el margen del enunciado, los incisos a) y b) fueron marcados como correctos, c) con una marca de revisión parcial ("R"), d) sin marca dedicada — al resolverse junto con e) —, y e) con una marca de "correcto con salvedad", coherente con el "NO" sobre la conclusión final de d).)*

</details>

---

## Ejercicio 3: OFDM [2,5 puntos]

**Enunciado:**

Dado una señal OFDM compuesta por 24 portadoras cada una de ellas moduladas en 16-QAM con duración de símbolo OFDM de un microsegundo. Se pide:

a) Calcular la tasa de información en bits por segundo que transporta la señal. [0,5 puntos]

b) Calcular el ancho de banda mínimo. [0,3 puntos]

c) Calcular la cantidad de bits que transporta en cada símbolo OFDM. [0,3 puntos]

d) Calcular la eficiencia espectral para ancho de banda mínimo. [0,4 puntos]

e) Calcular el ancho de banda mínimo si en vez de transmitir la señal OFDM se transmite la misma tasa de información (calculada en c)) pero en una sola portadora modulada en 16-QAM. [0,5 puntos]

f) Indicar la ventaja de emplear la señal descrita en el enunciado versus transmitir la misma tasa de información (calculada en a)) pero en una sola portadora modulada en 16-QAM. [0,5 puntos]

<details>
<summary>Respuesta</summary>

Datos: 24 portadoras, 16-QAM, $T_{S,OFDM}=1\ \mu\text{s}$.

*Nota de unidades: el estudiante desarrolló todo el ejercicio con prefijo kilo (Kbps, kHz, kS/s), pero su propio resultado de $T_b$ = 1 μs / 96 bits = 10,42 ns/bit ya fija la escala correcta en nanosegundos/Megabits. El profesor corrigió esto en el margen, circulando la "K" y escribiendo "M" en varios resultados. Se transcriben los valores con la unidad corregida (Mega), aclarando entre paréntesis el valor tal como fue escrito originalmente (Kilo).*

**a)** 24 portadoras, 16-QAM → 4 bits/símbolo por portadora, 1 símbolo por portadora por símbolo OFDM $\Rightarrow$ $24\times 4=96$ bits transportados por cada símbolo OFDM.

$$T_b=\frac{T_{S,OFDM}}{\text{cant. bits}}=\frac{1\ \mu s}{96\text{ bits}}=10,42\text{ ns/bit}$$

$$R_b(\text{conjunto})=\frac{1}{T_b}=\boxed{96\text{ Mbps}}\quad\text{(escrito originalmente "96 Kbps", corregido por el profesor)}$$

**b)** $R_s=\dfrac{1}{T_{S,OFDM}}=1\text{ MS/s}$ (escrito originalmente "1 kS/s")

$$BW_{min}=(N+1)\cdot R_s=(24+1)\cdot 1\text{ MS/s}=\boxed{25\text{ MHz}}\quad\text{(escrito originalmente "25 kHz")}$$

**c)** En cada símbolo OFDM se transportan $\boxed{96\text{ bits}}$ en total: cada una de las 24 subportadoras envía un símbolo de 4 bits (16-QAM).

**d)** 

$$\eta=\frac{R_b}{B_T}=\frac{96\text{ Mbps}}{25\text{ MHz}}=\boxed{3,84\text{ bit/Hz}}$$

(Este cociente da el mismo valor numérico independientemente de si se usa la escala kilo o mega, siempre que numerador y denominador sean consistentes entre sí.)

**e)** Una sola portadora de 16-QAM transportando los mismos 96 Mbps (escrito "96 Kbps"):

$$R_s=\frac{R_b}{4}=24\text{ MS/s (escrito "24 kS/seg")}, \qquad T_s=\frac{1}{R_s}\approx 41,7\text{ ns}$$

(el estudiante escribió "$T_s=41,67\ \mu$seg", arrastrando el mismo error de prefijo de escala)

$$BW_{min}=2W=R_s(1+F_R),\ \text{con } F_R=0\text{ (ideal)} \Rightarrow BW_{min}=\frac{R_b}{4}=R_s$$

$$\boxed{BW_{min}=24\text{ MHz}}\quad\text{(escrito originalmente "24 kHz")}$$

**f)** OFDM (multiplexación por división de frecuencias ortogonales) es muy robusta frente a multitrayectos (multipath); se protege de los desvanecimientos por condiciones meteorológicas y de interferencias. La clave de su eficiencia espectral está en la ortogonalidad de sus portadoras.

*(Nota parcial visible para este ejercicio: 2,0/2,5 — coherente con la confusión sistemática de unidades kilo/mega detectada por el profesor.)*

</details>

---

## Ejercicio 4: Teoría de la información [2,5 puntos]

**Enunciado:**

Una imagen de video monocromático formada por 640 líneas que contienen, cada una, 480 puntos luminosos. Donde cada punto luminoso puede tener uno de 256 niveles considerados equiprobables y la velocidad de las imágenes es de 25 imágenes por segundo, es recibida con relación señal a ruido a la entrada del receptor (considerado ideal) de 20 dB y la potencia de ruido es de $1\times10^{-12}$ Watts. Se pide:

a) Calcular la velocidad de la información producida por la imagen. [0,25 puntos]

b) Calcular el ancho de banda mínimo según Hartley-Shannon para realizar una transmisión sin pérdida de información. [0,5 puntos]

c) Calcular la potencia de la señal a la entrada del receptor del punto anterior. [0,25 puntos]

d) Si se desea transmitir la tasa de información determinada en el punto a) utilizando 8-PSK, Calcular el ancho de banda mínimo ideal necesario en el canal de transmisión y determinar si sería factible o no. [0,75 puntos]

e) Ídem d) pero utilizando 1024-QAM. [0,75 puntos]

<details>
<summary>Respuesta</summary>

Datos: imagen de 640 líneas × 480 puntos, 256 niveles equiprobables, 25 imágenes/s, $(S/N)_{Rx}=20\text{ dB}$, $N=1\times10^{-12}\text{ W}$.

**a)** Entropía por punto (256 niveles equiprobables): $H_{punto}=\log_2(256)=8\text{ bits/punto}$

$$H_{linea}=480\ \frac{\text{puntos}}{\text{línea}}\times 8\ \frac{\text{bits}}{\text{punto}}=3.840\text{ bits/línea}$$

$$H_{imagen}=640\ \frac{\text{líneas}}{\text{imagen}}\times 3.840\ \frac{\text{bits}}{\text{línea}}=2.457.600\text{ bits/imagen}$$

$$R_I=25\ \frac{\text{imág}}{\text{s}}\times 2.457.600\ \frac{\text{bits}}{\text{imagen}}=\boxed{61,44\text{ Mbits/s}}$$

**b)** $(S/N)_{Rx}=20\text{ dB}=100$ (veces)

Por Hartley-Shannon, $C=B\log_2(1+S/N)$, con $C=R_I$ (transmisión sin pérdida de información):

$$B=\frac{R_I}{\log_2(1+S/N)}=\frac{61,44\text{ Mbits/s}}{\log_2(101)}\approx\boxed{9,23\text{ MHz}}$$

**c)** $S/N=100$, $N=1\times10^{-12}\text{ W}$

$$S=(S/N)\cdot N=100\cdot 1\times10^{-12}\text{ W}=1\times10^{-10}\text{ W}=\boxed{100\text{ pW}}$$

**d)** Para transmitir $R_I=61,44\text{ Mbits/s}$ con 8-PSK (8 estados $\Rightarrow$ 3 bits/símbolo):

$$R_s=\frac{R_b}{3}, \qquad BW_{min}=2W=R_s(1+F_R),\ \text{con } F_R=0\text{ (ideal)} \Rightarrow BW_{min}=\frac{R_b}{3}$$

$$BW_{min}=\frac{61,44\text{ Mbits/s}}{3}=\boxed{20,48\text{ MHz}}$$

**e)** Para 1024-QAM (1024 estados $\Rightarrow$ 10 bits/símbolo):

$$R_s=\frac{R_b}{10} \Rightarrow BW_{min}=\frac{R_b}{10}=\frac{61,44\text{ Mbits/s}}{10}=\boxed{6,144\text{ MHz}}$$

Conclusión del estudiante: *"Si se quiere mantener la relación señal a ruido en la entrada del receptor de 20 dB, entonces nos conviene la modulación de 1024-QAM que tiene un ancho de banda inferior al calculado en la fórmula de Hartley-Shannon."*

**El profesor marcó esta conclusión como incorrecta**, anotando *"Hay que calcular Ts para c/u"* — es decir, faltaba el análisis de factibilidad explícito que pedía el enunciado en d) y e) (verificar el tiempo de símbolo / la relación señal a ruido requerida para cada esquema de modulación), en vez de comparar directamente el ancho de banda mínimo contra el valor obtenido con la fórmula de Hartley-Shannon.

*(Nota parcial visible para este ejercicio: 2,0/2,5; los incisos a), b) y c) fueron marcados como correctos con checkmarks (✓), mientras que d) y e) recibieron una marca de incompleto, coherente con la observación del profesor sobre la falta del análisis de factibilidad.)*

</details>

---
