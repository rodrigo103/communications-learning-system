---
tags:
  - outputs/solutions
curso: Sistemas de Comunicaciones
fecha: 2026-07-30
---

# Resolución completa — Final del 30/07/2026

> Enunciado y marcas de corrección en [[../../exercises/finales/md/F_Comu_2026-07-30_miFinal|F_Comu_2026-07-30_miFinal]]. Obtenido: **3,90/10**. Acá está resuelto entero, con el método y las trampas de cada ítem.

| Problema | Tema | Obtenido | Dónde estuvo el problema |
|---|---|---|---|
| 1 | Modulación lineal | 0,5 / 2,5 | Normalizar el índice al **pico del mensaje compuesto** |
| 2 | Modulación exponencial | 1,5 / 2,5 | Carson y el triplicador — ambos en el formulario |
| 3 | SS/OFDM | 1,40 / 2,5 | El corrimiento de medio espaciado de $f_c$ |
| 4 | Teoría de la información | 0,5 / 2,5 | Codificación de fuente (Huffman) + overhead de sincronismo |

---

## Problema 1 — Modulación lineal (AM multitono)

$$m(t) = A_1\cos(2\pi f_1t) + 0{,}8A_1\cos(2\pi f_2t) + 1{,}6A_1\cos(2\pi f_3t)$$

Modula al **80% referido al valor pico del mensaje compuesto**; $P_{total} = 252{,}025$ W normalizada.

### El paso que decide todo el ejercicio

"Referido al valor pico del mensaje compuesto" significa que el índice **total** vale 0,8, y ese 0,8 se reparte entre los tres tonos **en proporción a sus amplitudes**:

$$\lvert m\rvert_{max} = A_1(1+0{,}8+1{,}6) = 3{,}4\,A_1 \qquad\Longrightarrow\qquad m_i = 0{,}8\cdot\frac{A_i}{3{,}4A_1}$$

$$\boxed{m_1 = \tfrac{0{,}8}{3{,}4} = 0{,}2353 \qquad m_2 = \tfrac{0{,}64}{3{,}4} = 0{,}1882 \qquad m_3 = \tfrac{1{,}28}{3{,}4} = 0{,}3765}$$

Verificación obligatoria: $\sum m_i = 0{,}8$ ✓ — que es exactamente la condición de "modula al 80%" y, de paso, confirma que **no hay sobremodulación** ($\sum m_i \leq 1$).

⚠️ **El error natural es tomar $m_1=1$, $m_2=0{,}8$, $m_3=1{,}6$ o normalizar por el tono mayor.** Ninguna de las dos cumple $\sum m_i = 0{,}8$.

### a) Potencia de portadora

$$P_{total} = P_c\left(1+\frac{\sum m_i^2}{2}\right), \qquad \sum m_i^2 = 0{,}23253$$

$$P_c = \frac{252{,}025}{1{,}116263} = \boxed{225{,}78\ \text{W}} = \boxed{23{,}54\ \text{dBW}}$$

*(Chequeo: $A_c=\sqrt{2P_c}=21{,}25$ V y $A_1 = 0{,}8\cdot 21{,}25/3{,}4 = 5$ V — los tonos valen 5, 4 y 8 V. Números redondos: el enunciado estaba diseñado así.)*

### b) Potencia en banda lateral superior

Cada tono aporta $P_c m_i^2/4$ a **cada** banda lateral:

$$P_{BLS} = \frac{P_c}{4}\sum m_i^2 = \frac{225{,}78}{4}(0{,}23253) = \boxed{13{,}125\ \text{W}} = \boxed{11{,}18\ \text{dBW}}$$

### c) Densidad espectral de potencia (solo frecuencias positivas)

"Sólo frecuencias positivas, como se vería en un analizador" pide el espectro **unilateral**. Se arma en dos pasos: primero el bilateral y después se pliega.

**1. Bilateral.** Cada coseno real se reparte en dos deltas, en $+f$ y en $-f$, y cada una lleva la mitad de su potencia (el cuadrado de su coeficiente):

$$A\cos(2\pi f_0t) = \tfrac{A}{2}e^{j2\pi f_0t} + \tfrac{A}{2}e^{-j2\pi f_0t} \;\Longrightarrow\; \tfrac{A^2}{4}\ \text{en } {+f_0}\ \ \text{y}\ \ \tfrac{A^2}{4}\ \text{en } {-f_0}$$

Son $2+4N = 14$ deltas: la portadora con $P_c/2$ en $\pm f_c$, y cada lateral con $P_c m_i^2/8$ en $\pm(f_c \pm f_i)$.

**2. Plegado.** La mitad negativa se **suma** sobre la positiva, no se corta: $G_1(f) = 2\,G(f)$ para $f>0$. Cada raya queda con la potencia completa de su coseno, y quedan $1+2N = 7$ rayas (la tabla agrupa cada par $f_c \pm f_i$ en una fila):

| Frecuencia | Bilateral: cada delta, en $+f$ y en $-f$ | Unilateral: plegado, solo $f>0$ |
|---|---|---|
| $f_c$ | $112{,}89$ W | $\mathbf{225{,}78}$ **W** |
| $f_c \pm f_1$ | $1{,}5625$ W | $\mathbf{3{,}125}$ **W** |
| $f_c \pm f_2$ | $1{,}00$ W | $\mathbf{2{,}00}$ **W** |
| $f_c \pm f_3$ | $4{,}00$ W | $\mathbf{8{,}00}$ **W** |

Cada raya lateral unilateral vale $P_cm_i^2/4 = (kA_i)^2/8$, con $kA_1 = 5$ V.

$$\text{Verificación: } 225{,}78 + 2(3{,}125+2+8) = 252{,}03\ \text{W} = P_{total} \ ✓$$

> ⚠️ **Por qué no $P_c/2$:** $P_c/2$ es la delta en $+f_c$ del **bilateral**. Si se grafica el bilateral cortado en $f>0$, sin plegar, las rayas suman $112{,}89 + 2(1{,}5625+1+4) = 126$ W, la mitad de $P_{total}$. Un transmisor de 252 W no se ve como 126 W en un analizador.
>
> Un analizador muestra **potencia por raya**, no densidad continua, porque la señal tiene espectro discreto. Conviene anotar en la hoja la convención: "unilateral, $G_1(f)=2G(f)$".

### d) Eficiencia energética

$$\eta = \frac{P_{BL,total}}{P_{total}} = \frac{2(13{,}125)}{252{,}025} = \frac{\sum m_i^2/2}{1+\sum m_i^2/2} = \boxed{10{,}42\%}$$

Muy por debajo del 33% máximo de AM, porque el índice total es 0,8 pero **repartido** entre tres tonos: cada uno aporta poco al cuadrado.

### e) Factor de cresta de $m(t)$

$$m_{rms} = A_1\sqrt{\frac{1+0{,}64+2{,}56}{2}} = A_1\sqrt{2{,}1} = 1{,}4491\,A_1$$

$$F_C = \frac{A_m}{m_{rms}} = \frac{3{,}4}{1{,}4491} = \boxed{2{,}346}$$

*(Coherente con todo lo anterior: $P_{total}=P_c[1+m^2/F_C^2] = P_c[1+0{,}64/5{,}505]$ ✓)*

### f) PEP

$$PEP = P_c(1+m)^2 = 225{,}78\,(1{,}8)^2 = \boxed{731{,}5\ \text{W}} = \boxed{28{,}64\ \text{dBW}}$$

con $m = 0{,}8$ el índice **total** — el mismo que define la envolvente máxima $A_c(1+0{,}8)$.

---

## Problema 2 — Modulación exponencial

$$x_c(t) = 100\cos\left[2\pi\cdot90\cdot10^6\,t + 2\sin(18{,}85\cdot10^3\,t)\right]$$

Se lee todo de la expresión, comparando contra $s_{FM}(t)=A_c\cos(2\pi f_ct+\beta\sin 2\pi f_mt)$.

### a) Índice de modulación

$$\boxed{\beta = 2}$$

### b) Ancho de banda de la señal modulante

El argumento del seno es $\omega_m t$ con $\omega_m = 18{,}85\times10^3$ rad/s:

$$f_m = \frac{18\,850}{2\pi} = \boxed{3\ \text{kHz}}$$

⚠️ El $18{,}85\cdot10^3$ está en **rad/s**, no en Hz. Es tono único, así que el ancho de banda del mensaje es $f_m$.

### c) Máxima desviación de frecuencia

$$\Delta f = \beta f_m = 2(3\ \text{kHz}) = \boxed{6\ \text{kHz}}$$

### d) Ancho de banda de la señal modulada — Carson ❌

$$B_T = 2(\Delta f + f_m) = 2(6+3) = \boxed{18\ \text{kHz}}$$

### e) Potencia media sobre 50 Ω

$$P = \frac{A_c^2}{2R} = \frac{100^2}{2(50)} = \boxed{100\ \text{W}} = \boxed{20\ \text{dBW}}$$

⚠️ **En FM la potencia no depende de la modulación** — solo de $A_c$. Acá además hay que usar $R=50\ \Omega$ real, no normalizar.

### f) Con triplicador de frecuencia ❌

El multiplicador **multiplica la fase entera**, así que escala $f_c$, $\Delta f$ y $\beta$, pero **$f_m$ no se toca**:

| | Antes | Después de $\times3$ |
|---|---|---|
| $f_c$ | 90 MHz | 270 MHz |
| $\Delta f$ | 6 kHz | **18 kHz** |
| $\beta$ | 2 | 6 |
| $f_m$ | 3 kHz | **3 kHz** |

$$B_T' = 2(\Delta f' + f_m) = 2(18+3) = \boxed{42\ \text{kHz}}$$

⚠️ **No es $3\times18 = 54$ kHz.** El ancho de banda no se triplica, porque $f_m$ queda igual: $2(3\Delta f + f_m) \neq 3\cdot2(\Delta f+f_m)$.

---

## Problema 3 — SS/OFDM

$R_b = 16$ Mbps, $N_p = 8192$ subportadoras, 16-QAM por subportadora.

### a) Tiempo de símbolo OFDM

$$\ell = \log_2 16 = 4\ \tfrac{\text{bits}}{\text{símbolo}} \quad\Rightarrow\quad \text{bits/símbolo OFDM} = 8192\times4 = 32\,768$$

$$T_S = \frac{32\,768}{16\times10^6} = \boxed{2{,}048\ \text{ms}}$$

### b) Ancho de banda mínimo ideal

$$\Delta f = \frac{1}{T_S} = 488{,}28\ \text{Hz} \quad\Rightarrow\quad B_T = N_p\,\Delta f = 8192(488{,}28) = \boxed{4\ \text{MHz}}$$

### c) Frecuencias de las subportadoras

Con $N_p$ **par** no hay ninguna en el centro; quedan corridas medio espaciado y simétricas:

$$f_k = f_{central} \pm \left(k+\tfrac12\right)\Delta f, \qquad k = 0,1,\ldots,4095$$

| | Frecuencia relativa a $f_{central}$ |
|---|---|
| Dos **más próximas al centro** ($k=0$) | $\pm 244{,}14$ Hz |
| Dos **inferiores** ($k=4095$, $4094$) | $-1{,}999756$ MHz y $-1{,}999268$ MHz |
| Dos **superiores** ($k=4094$, $4095$) | $+1{,}999268$ MHz y $+1{,}999756$ MHz |

**Verificación**: la extrema está a $1{,}999756$ MHz del centro y ocupa medio espaciado más hacia afuera:

$$B_T = 2(1{,}999756 + 0{,}000244)\ \text{MHz} = 4\ \text{MHz} \ ✓$$

### d) Espectro con entrada "0110" repetida

Con 16-QAM se toman **4 binits por símbolo**, y el patrón "0110" tiene período 4: **todos los grupos son idénticos**, así que las 8192 subportadoras transmiten siempre **el mismo punto de constelación**, símbolo tras símbolo.

$$\Rightarrow\ \text{señal periódica de período } T_S \ \Rightarrow\ \boxed{\text{espectro de líneas: 8192 deltas separadas } 488{,}28\text{ Hz}}$$

Cada subportadora queda como un **tono puro sin modular**. La DEP de una señal digital va con $\sigma_a^2$ (la varianza de los símbolos): **sin variación de datos no hay ensanchamiento**. El espectro continuo de OFDM lo produce la información, no las portadoras.

⚠️ **"0110" no es amplitud cero**: mapea a un punto específico de la grilla, y ninguno de los 16 puntos está en el origen.

**Consecuencia en el tiempo** (vale mencionarla): las 8192 subportadoras se suman **en fase** en $t=0$, dando $\text{PAPR} = N_p = 8192 \equiv 39{,}1$ dB. Es el peor caso posible, e inviable para cualquier amplificador — por eso los sistemas reales llevan un *scrambler* que aleatoriza los datos antes de mapear.

### e) Valor de $f_c$ para centrar en 3,9 GHz ❌

Se resuelve en tres pasos.

**1. El oscilador siempre cae sobre una subportadora.** La IFFT arma las subportadoras en banda base, en $k\,\Delta f$. La de $k=0$ es continua (frecuencia cero). El mezclador corre todo el espectro en $f_c$, así que la subportadora $k=0$ termina **exactamente en $f_c$**.

**2. En el centro de la banda no hay ninguna subportadora.** Por c), con $N_p = 8192$ (par) las subportadoras quedan simétricas respecto de la frecuencia central, y las dos más próximas están a $\pm\Delta f/2 = \pm 244{,}14$ Hz. Justo en el centro no hay ninguna.

**3. Entonces $f_c$ no puede ser 3,9 GHz.** Si lo fuera, habría una subportadora en 3,9 GHz y todo el conjunto quedaría corrido medio espaciado. $f_c$ tiene que coincidir con una de las dos subportadoras centrales:

$$f_c = 3{,}9\ \text{GHz} - \frac{\Delta f}{2} = 3{,}9\ \text{GHz} - 244{,}14\ \text{Hz} = \boxed{3\,899\,999\,755{,}86\ \text{Hz}}$$

**Por qué el signo menos:** es la central inferior, la que usa la resolución de la cátedra del mismo problema con 4096 subportadoras (F_Comu_2022-07-21: "3,9 GHz − 488,28 Hz", que es medio espaciado de ese caso). El signo depende de cómo se numeren los índices de la IFFT, es decir, si la subportadora que sobra (8192 es par) queda arriba o abajo. Tomando la central superior, $+244{,}14$ Hz, el razonamiento es el mismo. Lo que se evalúa es el **medio espaciado** y la **justificación**, así que conviene escribir los tres pasos.

> ⚠️ Responder $f_c = 3{,}9$ GHz está mal: en F_Comu_2023-02-23 esa respuesta está marcada "NO". Es suponer que el oscilador queda en el centro de la banda, y eso solo pasa con una cantidad impar de subportadoras.

### f) Tiempo de símbolo con una sola portadora en 1024-QAM

$$\ell = \log_2 1024 = 10 \quad\Rightarrow\quad D = \frac{16\ \text{Mbps}}{10} = 1{,}6\ \text{Mbaud} \quad\Rightarrow\quad T_{S1c} = \boxed{0{,}625\ \mu\text{s}}$$

**El contraste es el punto del ítem:**

$$\frac{T_S}{T_{S1c}} = \frac{2{,}048\ \text{ms}}{0{,}625\ \mu\text{s}} = 3276{,}8 = N_p\cdot\frac{\ell_{OFDM}}{\ell_{1c}} = 8192\cdot\frac{4}{10} \ ✓$$

Un símbolo OFDM dura **3277 veces más**. Ahí está toda la ventaja: un eco de ~1 μs es el 0,05% de un símbolo OFDM y se superpone a **1,6 símbolos** con una sola portadora.

---

## Problema 4 — Teoría de la información

Fuente sin memoria, 6 símbolos con $p = \{\tfrac14,\tfrac14,\tfrac18,\tfrac18,\tfrac18,\tfrac18\}$, emitidos a $r=200$ símbolos/s. Canal binario con $C = 580$ bps.

### a) ¿Se puede transmitir?

$$H = 2\left(\tfrac14\log_2 4\right) + 4\left(\tfrac18\log_2 8\right) = 1 + 1{,}5 = \boxed{2{,}5\ \tfrac{\text{bits}}{\text{símbolo}}}$$

$$R = r\,H = 200(2{,}5) = \boxed{500\ \text{bps}}$$

$$500\ \text{bps} < 580\ \text{bps} = C \quad\Rightarrow\quad \boxed{\textbf{SÍ es transmisible}}$$

**La justificación es el teorema de codificación de canal**: si $R < C$ existe una codificación que permite transmitir con probabilidad de error arbitrariamente pequeña. Si fuera $R > C$ sería **imposible**, no difícil.

### b) Técnica de codificación binaria

Las seis probabilidades son **potencias exactas de $\tfrac12$** ($2^{-2},2^{-2},2^{-3},2^{-3},2^{-3},2^{-3}$), así que **Huffman da un código absolutamente óptimo** con $\bar L = H$:

| Símbolo | $p_i$ | $l_i$ | Código |
|---|---|---|---|
| $s_1$ | 1/4 | 2 | `00` |
| $s_2$ | 1/4 | 2 | `01` |
| $s_3$ | 1/8 | 3 | `100` |
| $s_4$ | 1/8 | 3 | `101` |
| $s_5$ | 1/8 | 3 | `110` |
| $s_6$ | 1/8 | 3 | `111` |

**Construcción (Huffman)**: se combinan repetidamente los dos nodos de menor probabilidad — dos $\tfrac18$ dan $\tfrac14$, los otros dos $\tfrac18$ dan otro $\tfrac14$, y quedan cuatro nodos de $\tfrac14$ que se emparejan en dos de $\tfrac12$. De ahí las longitudes 2, 2, 3, 3, 3, 3.

**Verificaciones:**

$$\bar L = 2\left(\tfrac14\right)(2) + 4\left(\tfrac18\right)(3) = 1 + 1{,}5 = 2{,}5\ \tfrac{\text{bits}}{\text{símbolo}} = H \quad\Rightarrow\quad \eta = 100\%$$

$$\text{Kraft-McMillan: } \sum_i 2^{-l_i} = 2(2^{-2}) + 4(2^{-3}) = 0{,}5+0{,}5 = 1 \ ✓$$

La **igualdad** en Kraft dice que el código es *completo*: no sobra ninguna rama del árbol. Y es **de prefijo** (ningún código es principio de otro), así que se decodifica unívocamente sin separadores.

### c) Velocidad de la codificación binaria

$$R_b = r\,\bar L = 200(2{,}5) = \boxed{500\ \text{binits/s}}$$

Coincide con $R$ **porque $\bar L = H$**: el código no agrega redundancia. Y $500 < 580$ ✓ — confirma por la vía constructiva lo que a) afirmó por la vía teórica.

> **La conexión entre a), b) y c)**: a) dice que es posible, b) exhibe el código que lo logra, c) mide su velocidad y verifica que entra en el canal. Es el mismo número (2,5 bits/símbolo) leído tres veces: como entropía, como longitud media y como tasa binaria.

### d) Tasa de información con bloques y sincronismo

$$H = \log_2 16 = 4\ \tfrac{\text{bits}}{\text{símbolo}} \quad (\text{equiprobables})$$

| | |
|---|---|
| Información por bloque | $15 \times 4 = 60$ bits |
| Duración del bloque | $15(1\ \mu s) + 5\ \mu s = 20\ \mu s$ |

$$R = \frac{60\ \text{bits}}{20\ \mu\text{s}} = \boxed{3\ \text{Mbps}}$$

⚠️ **El pulso de sincronización ocupa tiempo pero no lleva información** — es determinístico, el receptor ya sabe que está. Entra en el denominador y no en el numerador.

Sin overhead la tasa sería $4$ Mbps ($1$ símbolo/μs × 4 bits): **el sincronismo cuesta el 25%**.

---

## Lo que este final dice para septiembre

**Ningún ítem pedía una fórmula que no estuviera en el formulario, salvo la codificación de fuente del Problema 4.** Todo lo demás —Carson, el triplicador, la cadena OFDM, la potencia en FM, el reparto multitono, PEP, factor de cresta— estaba escrito y verificado.

Los tres puntos donde se concentró la pérdida:

1. **Normalizar el índice al pico compuesto** (P1). Es un solo paso al principio, y si sale mal se cae el ejercicio entero: los seis ítems dependen de $m_i$. Ese ejercicio valía 2,5 y se llevó 0,5.
2. **Aplicar la fórmula del multiplicador sin pensar** (P2f). $\times3$ escala $\Delta f$, no $B_T$.
3. **Codificación de fuente** (P4b y c). Un punto entero, y era el caso más limpio posible — probabilidades que son potencias de $\tfrac12$, donde Huffman da $\bar L = H$ exacto.

Ver también: [[../../wiki/planificacion/formulario-imprimible|Formulario]] · [[../../wiki/planificacion/diagramas-en-bloques|Diagramas en bloques]] · [[../../exercises/finales/md/F_Comu_2026-07-30_miFinal|Enunciado con las correcciones]]
