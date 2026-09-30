---
tags:
  - outputs/solutions
curso: Sistemas de Comunicaciones
fecha: 2026-09-29
---

# Resolución completa — Final del 29/09/2026

> Enunciado, marcas de corrección y lo entregado en [[../../exercises/finales/md/F_Comu_2026-09-29_miFinal|F_Comu_2026-09-29_miFinal]]. Obtenido: **7,75/10 → 8, aprobado**. Acá está resuelto entero; los ítems que se corrigieron con descuento llevan ❌ o ⚠️.

| Problema | Tema | Obtenido | Dónde estuvo el descuento |
|---|---|---|---|
| 1 | Modulación lineal | 2,5 / 2,5 | — |
| 2 | PCM | 1,3 / 2,5 | Bit-rate de **una** señal en vez de las cuatro; dB con $20\log$; sistema con sincronismo |
| 3 | Ruido | 1,75 / 2,5 | **Umbral de FM** sin verificar (e y f) |
| 4 | OFDM | 2,20 / 2,5 | Bits por símbolo OFDM (c) y un descuento menor en d) |

---

## Problema 1 — Modulación lineal (AM, uno y dos tonos)

$f_c = 750$ kHz, $A_c = 1800$ V, $R = 50\ \Omega$ (potencias sobre la antena, **no** normalizadas), $m = 0{,}8$.

### a) Potencia de la portadora

$$P_c = \frac{A_c^2}{2R} = \frac{1800^2}{2\cdot50} = \boxed{32\,400\ \text{W}} = \boxed{45{,}11\ \text{dBW}}$$

### b) Potencia media total, un tono

$$P_{total} = P_c\left(1+\frac{m^2}{2}\right) = 32\,400\,(1{,}32) = \boxed{42\,768\ \text{W}} = \boxed{46{,}31\ \text{dBW}}$$

### c) PEP, un tono

$$PEP = P_c(1+m)^2 = 32\,400\,(1{,}8)^2 = \boxed{104\,976\ \text{W}} = \boxed{50{,}21\ \text{dBW}}$$

### d) Potencia media total, dos tonos de igual amplitud

"El índice de modulación sigue en 0,8" es el índice **total**, referido al pico del mensaje compuesto. Se reparte en proporción a las amplitudes, y como son iguales:

$$m_i = m\,\frac{A_i}{\sum_j A_j} = 0{,}8\cdot\frac{A}{2A} = 0{,}4 \qquad \text{(chequeo: } 0{,}4+0{,}4 = 0{,}8\ ✓)$$

$$P_{total} = P_c\left(1+\frac{m_1^2+m_2^2}{2}\right) = 32\,400\left(1+\frac{0{,}16+0{,}16}{2}\right) = 32\,400\,(1{,}16) = \boxed{37\,584\ \text{W}} = \boxed{45{,}75\ \text{dBW}}$$

Con el mismo índice total, **dos tonos llevan menos potencia a las laterales que uno**: $\sum m_i^2/2 = 0{,}16$ contra $m^2/2 = 0{,}32$. El mensaje de dos tonos tiene más factor de cresta ($F_C = 2$ contra $\sqrt2$), y a igual pico, más $F_C$ es menos potencia.

### e) PEP, dos tonos

La envolvente máxima es $A_c(1+m_{tot})$, cuando los dos tonos coinciden en su pico. Depende del índice **total**, que no cambió:

$$PEP = P_c(1+m_{tot})^2 = \boxed{104\,976\ \text{W}} = \boxed{50{,}21\ \text{dBW}}$$

Igual que en c): el pico no cambia, lo que baja es la potencia media.

---

## Problema 2 — PCM/TDM de cuatro señales de video

### a) Frecuencia de muestreo

$$f_s = 1{,}25\cdot 2\,f_m = 1{,}25\cdot 2\cdot 4{,}5\ \text{MHz} = \boxed{11{,}25\ \text{MHz}}\ \ (\text{Mmuestras/s por señal})$$

### b) Binits por muestra

$$n = \log_2 1024 = \boxed{10\ \text{binits/muestra}}$$

### c) Bit-rate y ancho de banda mínimo — ⚠️ (R)

El ítem pide la tasa de **la señal codificada que se transmite**, la PCM/TDM con las **cuatro** señales:

$$R_b = 4\cdot n\cdot f_s = 4\cdot 10\cdot 11{,}25\times10^6 = \boxed{450\ \text{Mbps}}$$

En NRZ (banda base), el mínimo ideal de Nyquist es la mitad de la tasa de pulsos:

$$B_{min} = \frac{R_b}{2} = \boxed{225\ \text{MHz}}$$

⚠️ **Lo que pasó**: se informó $R_b = 112{,}5$ Mbps, la tasa de **una** señal, y el ×4 se aplicó recién en el ancho de banda (225 MHz, bien).

**El enunciado es ambiguo**, pero tres cosas indican que se pedía el de las cuatro:

1. **La introducción define qué es "la señal codificada"**: "Cuatro señales de video [...] se muestrean, cuantifican y codifican para obtener **una señal PCM/TDM**". Es una sola señal que resulta de las cuatro; "la señal codificada" de c), en singular, es esa.
2. **El ítem e) la usa así**: "La señal cuantificada y codificada **determinada en c)** se transmite por un servicio de 472,5 Mbps [...] que permita enviar **las cuatro señales** y el sincronismo". Para comparar contra 472,5 Mbps hace falta el total, 450 Mbps.
3. **El corrector escribió "×4"** al lado de los 112,5 Mbinits/s.

Lo que apoya la otra lectura es la **negrita** en "**las cuatro señales**", que aparece solo en la parte del ancho de banda: se puede leer como contraste (bit-rate de cada una, ancho de banda de las cuatro). La marca fue "R" y no ✗, o sea puntaje parcial: probablemente por el ancho de banda correcto, y quizás también por la ambigüedad.

**Frente a un ítem ambiguo, escribir las dos cosas con su nombre**: "112,5 Mbps por señal; **450 Mbps la señal PCM/TDM**". Cuesta un renglón y cubre las dos lecturas.

### d) SNR de cuantificación mínima — ⚠️ (parcial)

Con cuantificación uniforme y la señal ocupando todo el rango del cuantificador:

$$SNR_Q = \frac{3M^2}{F_C^2} = \frac{3\cdot 1024^2}{4^2} = 196\,608 \ \Rightarrow\ 10\log(196\,608) = 52{,}94\ \text{dB}$$

(chequeo: $6{,}02\,n + 4{,}77 - 20\log F_C = 60{,}21 + 4{,}77 - 12{,}04 = 52{,}94$ dB ✓)

El **rango dinámico de 3 dB** significa que el nivel de la señal varía 3 dB. Con cuantificación uniforme, el ruido de cuantificación es fijo ($q^2/12$), así que la SNR es **mínima** cuando la señal está en su nivel más bajo, 3 dB por debajo del máximo:

$$SNR_{Q,min} = 52{,}94 - 3 = \boxed{49{,}94\ \text{dB}}$$

⚠️ **Lo que pasó**: la cuenta lineal ($196\,608$) estaba bien, pero se pasó a dB con $20\log$ (105,87 dB, tachado). Tampoco se descontaron los 3 dB del rango dinámico.

**Por qué va $10\log$ aunque en PCM "haya 20"**: $SNR_Q$ es potencia de señal sobre potencia de ruido de cuantificación ($q^2/12$ es una potencia), así que es una relación de **potencias**. Lo que es "de tensiones" son $M$ (cuántos escalones $q$ entran en $V_{pp}$) y $F_C$ (pico sobre RMS), y por eso **vienen al cuadrado** dentro de $3M^2/F_C^2$. El 20 aparece solo si se desarma la fórmula:

$$10\log\frac{3M^2}{F_C^2} = \underbrace{10\log3}_{4{,}77} + \underbrace{20\log M}_{60{,}21} - \underbrace{20\log F_C}_{12{,}04} = 52{,}94\ \text{dB}$$

Aplicar $20\log$ al número entero cuenta el cuadrado **dos veces**: $105{,}87 = 2\times52{,}94$. Chequeo rápido: son unos 6 dB por bit, así que con 10 bits la SNR ronda los 60 dB; 105,87 dB serían más de 10 dB por bit.

> **El formulario inducía este error**: en la tabla de decibeles, $SNR_Q$ figuraba entre "los tres lugares con 20", y además con la constante mal (1,76, que es la del caso senoidal, en vez de 4,77). Se corrigió el 30/09: ahora dice que el 20 es de $M$ y $F_C$ por separado y que $SNR_Q$ entera va con $10\log$.

> La lectura "mínima = máxima − rango dinámico" es la interpretación física del enunciado; en el corpus no hay otro ítem con "rango dinámico" en dB de la señal para contrastarla.

### e) Sistema con sincronismo sobre 472,5 Mbps — ❌

Una **trama** TDM toma una muestra de cada señal, y hay tantas tramas por segundo como muestras por señal:

$$\text{tramas/s} = f_s = 11{,}25\times10^6 \qquad \text{datos por trama} = 4\cdot10 = 40\ \text{binits}$$

El servicio entrega:

$$\frac{472{,}5\times10^6\ \text{binits/s}}{11{,}25\times10^6\ \text{tramas/s}} = 42\ \text{binits/trama}$$

Sobran exactamente **2 binits por trama** para sincronismo:

| Sinc | Señal 1 | Señal 2 | Señal 3 | Señal 4 |
|---|---|---|---|---|
| 2 binits | 10 binits | 10 binits | 10 binits | 10 binits |

$$\boxed{\text{Trama de 42 binits: 2 de sincronismo + 4}\times10\text{ de datos, a 11,25 Mtramas/s}}$$

Duración de trama: $1/11{,}25\ \text{MHz} = 88{,}9$ ns. Capacidad dedicada a sincronismo: $2\times11{,}25\times10^6 = 22{,}5$ Mbps $= 472{,}5 - 450$ ✓.

⚠️ **Lo que pasó**: se escribió "$C = 472{,}5$ Gbits/s" (el dato es **M**bits/s) y no se propuso sistema. El ítem se resuelve dividiendo la tasa del servicio por las tramas por segundo.

---

## Problema 3 — Ruido: SNR de posdetección

### Datos y $\gamma$

$$L = 55\ \text{dB} = 10^{5{,}5} = 316\,228 \qquad S_R = \frac{250}{316\,228} = 790{,}6\ \mu\text{W}$$

$$\gamma = \frac{S_R}{N_0\,W} = \frac{790{,}6\times10^{-6}}{2\times10^{-10}\cdot 15\times10^3} = 263{,}5 \equiv 24{,}21\ \text{dB}$$

Factor de cresta 2 → $\langle m_n^2\rangle = 1/F_C^2 = 1/4$.

### a) SSB

$$(S/N)_D = \gamma = \boxed{24{,}21\ \text{dB}}$$

### b) DSB-SC

$$(S/N)_D = \gamma = \boxed{24{,}21\ \text{dB}}$$

Con detección coherente, DSB-SC y SSB **empatan**.

### c) AM con $m = 0{,}9$

$$(S/N)_D = \frac{m^2\langle m_n^2\rangle}{1+m^2\langle m_n^2\rangle}\,\gamma = \frac{0{,}81/4}{1+0{,}81/4}\,\gamma = \frac{81}{481}\,(263{,}5) = 44{,}38 \equiv \boxed{16{,}47\ \text{dB}}$$

### d) FM con $\Delta f = 75$ kHz

$$(S/N)_D = 3\left(\frac{\Delta f}{W}\right)^2\langle m_n^2\rangle\,\gamma = 3\,(5)^2\,\frac14\,(263{,}5) = 18{,}75\,(263{,}5) = 4941 \equiv \boxed{36{,}94\ \text{dB}}$$

**Chequeo de umbral** (hay que hacerlo siempre en FM). La SNR de predetección se mide en el ancho de banda de transmisión, $B_T = 2(\Delta f + W) = 180$ kHz:

$$\left(\frac{S}{N}\right)_{pre} = \frac{S_R}{N_0\,B_T} = \gamma\,\frac{W}{B_T} = 263{,}5\cdot\frac{15}{180} = 21{,}96 \equiv 13{,}4\ \text{dB} \;>\; 10\ \text{dB}\ ✓$$

Está sobre el umbral: la fórmula vale.

### e) FM con $N_0 = 2\times10^{-9}$ W/Hz — ❌

$$\gamma' = \frac{\gamma}{10} = 26{,}35 \equiv 14{,}21\ \text{dB} \qquad \left(\frac{S}{N}\right)_{pre} = 26{,}35\cdot\frac{15}{180} = 2{,}20 \equiv 3{,}4\ \text{dB} \;<\; 10\ \text{dB}$$

$$\boxed{\text{Por debajo del umbral: la } (S/N)_D \text{ colapsa y la fórmula de FM no es válida}}$$

La fórmula daría $18{,}75\cdot26{,}35 = 494 \equiv 26{,}94$ dB, pero ese número no existe: bajo el umbral aparecen los *clicks* y la SNR cae abruptamente.

⚠️ **Lo que pasó**: se aplicó la fórmula (26,94 dB) sin verificar el umbral; el corrector anotó "NO CUMPLE UMBRAL". Que el ítem diga "Idem d) pero con 10 veces más ruido" es la señal para mirar el umbral.

### f) Menor potencia de transmisión para $(S/N)_D > 15$ dB — ⚠️ (R)

Objetivo: $(S/N)_D = 10^{1{,}5} = 31{,}62$. Para cada modulación, el $\gamma$ necesario y la $P_T = \gamma\,N_0\,W\cdot L$ (con $N_0 = 2\times10^{-10}$):

| Modulación | $\gamma$ necesario | $P_T$ media | En dBm |
|---|---|---|---|
| SSB / DSB-SC | $31{,}62$ | 30,0 W | 44,77 dBm |
| AM ($m = 0{,}9$) | $31{,}62\cdot481/81 = 187{,}8$ | 178,1 W | 52,51 dBm |
| FM, fórmula sola | $31{,}62/18{,}75 = 1{,}69$ | 1,60 W | 32,04 dBm |
| **FM, respetando el umbral** | $10\cdot B_T/W = 120$ | **113,8 W** | **50,56 dBm** |

**La fila "FM, fórmula sola" no es realizable.** Con $\gamma = 1{,}69$, la SNR de predetección es $1{,}69\cdot15/180 = 0{,}14$ ($-8{,}5$ dB), muy por debajo del umbral. En FM la potencia mínima la fija **el umbral**, no el objetivo de 15 dB:

$$\left(\frac{S}{N}\right)_{pre} = 10 \;\Rightarrow\; S_R = 10\,N_0\,B_T = 10\cdot2\times10^{-10}\cdot180\times10^3 = 360\ \mu\text{W}$$

$$P_T = S_R\cdot L = 360\times10^{-6}\cdot316\,228 = \boxed{113{,}8\ \text{W}} = \boxed{50{,}56\ \text{dBm}}$$

y ahí $(S/N)_D = 18{,}75\cdot120 = 2250 \equiv 33{,}5$ dB, holgadamente arriba de 15 dB.

**¿Cuál requiere menos?** Depende de qué potencia se compare:

- **Potencia media:** SSB/DSB-SC, con 30 W (44,77 dBm).
- **Potencia pico** (instantánea máxima, lo que dimensiona el amplificador): FM tiene envolvente constante, así que su pico es la media, 113,8 W. DSB-SC tiene pico $F_C^2 = 4$ veces la media: $4\cdot30 = 120$ W (50,79 dBm). **Gana FM**, por poco.

$$\boxed{\text{FM},\ P_T = 113{,}8\ \text{W} = 50{,}56\ \text{dBm}}$$

La corrección ("Es FM pero $P_T$ no es correcta") da **FM** como respuesta, lo que corresponde a comparar potencia pico, como pide explícitamente la versión de este problema en `F_Comu_2024-07-25` ("potencia de transmisión, instantánea, máxima"). El valor que hace a FM la de menor potencia es el limitado por umbral, 113,8 W.

> En SSB el pico depende de $m(t)$ y de su transformada de Hilbert, así que no se puede calcular con los datos; por eso la comparación natural es contra DSB-SC.

⚠️ **Lo que pasó**: la elección de FM estuvo bien; los 1,6 W salen de la fórmula de FM sin el umbral, el mismo olvido del e).

---

## Problema 4 — OFDM

24 portadoras, 16-QAM ($\ell = 4$), $T_S = 96\ \mu$s.

### a) Tasa de información

$$\text{binits por símbolo OFDM} = 24\cdot4 = 96 \qquad R = \frac{96}{96\ \mu\text{s}} = \boxed{1\ \text{Mbps}}$$

### b) Ancho de banda mínimo

$$\Delta f = \frac{1}{T_S} = 10{,}417\ \text{kHz} \qquad B = N_p\,\Delta f = 24\cdot10{,}417 = \boxed{250\ \text{kHz}}$$

(Con los medios lóbulos de los bordes, $(N_p+1)\Delta f = 260{,}4$ kHz; en `F_Comu_2022-07-21` la resolución acepta las dos formas.)

### c) Bits por símbolo OFDM — ❌ (M)

$$N_p\cdot\ell = 24\cdot4 = \boxed{96\ \text{bits/símbolo OFDM}}$$

Es el número intermedio de a): cada símbolo OFDM lleva un símbolo 16-QAM (4 bits) **en cada una** de las 24 subportadoras, en paralelo. (La hoja de este problema no está fotografiada, así que no se sabe qué se respondió.)

### d) Eficiencia espectral a ancho de banda mínimo — (B−)

$$\eta = \frac{R}{B} = \frac{1\ \text{Mbps}}{250\ \text{kHz}} = \boxed{4\ \text{bit/s/Hz}}$$

Igual a $\ell$: OFDM con subportadoras ortogonales no pierde eficiencia respecto de la modulación de cada subportadora.

### e) Una sola portadora 16-QAM

$$D = \frac{R}{\ell} = \frac{1\ \text{Mbps}}{4} = 250\ \text{kbaud} \qquad B_{min} = D = \boxed{250\ \text{kHz}}$$

El **mismo** ancho de banda que OFDM (en el caso ideal): OFDM no gana en espectro.

### f) Ventaja de OFDM

Con una sola portadora, el símbolo dura $T_s = 1/250\ \text{kbaud} = 4\ \mu$s; en OFDM dura **96 μs**, 24 veces más. Por eso:

- **Robustez al multitrayecto**: un eco de algunos μs se superpone a varios símbolos de 4 μs (ISI), pero es una fracción chica de un símbolo de 96 μs.
- **Cada subportadora ve un canal plano** (su $\Delta f$ es angosto), así que se ecualiza con una multiplicación compleja por subportadora, en vez de un ecualizador temporal complejo.
- El prefijo cíclico que absorbe los ecos cuesta poco sobre un símbolo largo.

---

## Lo que este final dice

**De 3,90 a 7,75, con los mismos tipos de errores pero menos.** Ningún descuento fue por una fórmula ausente del formulario. El umbral de FM estaba ("$SNR_{umbral}\approx10$ dB"), aunque sin aclarar que esa SNR se mide en $B_T$. Los 2,25 puntos perdidos:

| Ítem | Perdido (aprox.) | Tipo de error |
|---|---|---|
| P2 c) | parte de 0,5 | Bit-rate de una señal; el enunciado admitía las dos lecturas: **dar los dos valores** |
| P2 d) | parte de 0,75 | **$20\log$ sobre una relación de potencias** (el formulario lo inducía); sin los −3 dB |
| P2 e) | 0,75 | Sin sistema propuesto; **prefijo** mal copiado (G por M) |
| P3 e) | 0,5 | **Umbral de FM** sin verificar |
| P3 f) | 0,25 | El mismo umbral, arrastrado |
| P4 c), d) | 0,30 | Bits por símbolo OFDM; descuento menor |

Dos descuentos tienen parte de explicación externa: el enunciado ambiguo en P2 c) y el formulario en P2 d). Los que quedan como modo de falla propio son el **prefijo** (G por M, el mismo tipo de error que mV² en julio) y el **umbral de FM sin verificar**: en FM, toda SNR de posdetección se valida contra el umbral antes de informarla.

Ver también: [[../../wiki/planificacion/formulario-imprimible|Formulario]] · [[MiFinal_completo_F_Comu_2026-07-30|Resolución del final de julio]] · [[../../exercises/finales/md/F_Comu_2026-09-29_miFinal|Enunciado con las correcciones]]
