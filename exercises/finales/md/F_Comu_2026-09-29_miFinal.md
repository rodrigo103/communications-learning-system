# Examen Final SC — 29/09/2026

*Fuente: `exercises/finales/F_Comu_2026-09-29_miFinal.pdf` (fotos de las hojas de enunciado) y `exercises/finales/miFinal_2026-09-29/` (enunciados + hojas de resolución, fotografiadas al finalizar)*

> ⚠️ **Este es el final que rindió Rodrigo (Videla, Rodrigo). APROBADO con 8 (ocho).** Las cuatro hojas de enunciado tienen las **marcas de corrección** del equipo docente. A diferencia de julio, también están fotografiadas las hojas de resolución de los cuatro problemas. Se transcriben las marcas visibles junto a cada ítem y lo escrito en cada hoja.

**Datos de la mesa:** 29/09/2026, hora de finalización 21 Hs. N° de hojas entregadas: 4 (hojas de resolución numeradas 1/4 y 2/4; las de los problemas 3 y 4 sin número, y el 3 sigue en una hoja adicional). Cada hoja de enunciado lleva impreso "25/09/2026 - 19:54" (fecha de generación del documento).

**Requisitos para rendir el final:** Tener aprobadas: Electrónica Aplicada I, Medios de Enlace, Análisis de Señales y Sistemas y Probabilidad y Estadísticas. Están exceptuados aquellos que regularizaron la materia en el último ciclo lectivo.

**Forma de evaluación:** El examen se aprueba si la sumatoria alcanza seis o más, sin redondeo. Para aprobar se debe desarrollar al menos el 25% del total de cada punto. Consecuentemente un punto sin desarrollo alguno implica que el examen está desaprobado; por más que el resto esté bien.

## Resultado

| Problema | Tema | Puntaje | Obtenido | Evaluador |
|---|---|---|---|---|
| 1 | Modulación lineal | 2,5 | **2,5** | RD (iniciales poco legibles) |
| 2 | PCM | 2,5 | **1,3** | RD (iniciales poco legibles) |
| 3 | Ruido | 2,5 | **1,75** | RF |
| 4 | OFDM | 2,5 | **2,20** | JM (iniciales poco legibles) |
| | **Total** | **10** | **7,75** | |

**Nota final asentada: 8 (OCHO) — aprobado.** (Escrita arriba de la primera hoja de enunciado.)

---

## Ejercicio 1: Modulación lineal [2,5 puntos] — obtenido 2,5

**Enunciado:**

Una estación de radio de AM transmite a una frecuencia de portadora, $f_c = 750$ KHz. La amplitud pico de la portadora sin modular es de **1800 Volts** y se aplica sobre la antena con impedancia resistiva, $R = 50$ Ohms. La señal modulante es un tono senoidal y el índice de modulación, $m = 0{,}8$.

Determine:

a) la potencia media de la portadora sin modular (sobre la antena) de 50 Ohms, expresada en dBW. [0,5 puntos] — ✅

b) la potencia media total de la señal transmitida sobre la antena, expresada en dBW. [0,5 puntos] — ✅

c) la potencia de pico de envolvente de la señal transmitida sobre la antena, expresada en dBW. [0,5 puntos] — ✅

d) la potencia media total de la señal transmitida expresada en dBW, si ahora la señal modulante son **dos tonos senoidales de la misma amplitud** y el índice de modulación sigue en 0,8. [0,5 puntos] — ✅

e) la potencia de pico de envolvente de la señal transmitida expresada en dBW, si ahora la señal modulante son dos tonos senoidales de la misma amplitud y el índice de modulación sigue en 0,8. [0,5 puntos] — ✅

**Resolución entregada (hoja 1/4):**

- a) $P_c = \dfrac{A_c^2}{2R} = \dfrac{(1800\text{ V})^2}{2\cdot 50\,\Omega} = 32{,}4$ kW $\equiv$ **45,1 dBW** ✓
- b) $P_{total} = P_c\left(1+\dfrac{m^2}{2}\right) = 32{,}4\text{ kW}\left(1+\dfrac{0{,}8^2}{2}\right) = 42{,}768$ kW $\equiv$ **46,31 dBW** ✓
- c) $PEP = P_c(1+m)^2 = 32{,}4\text{ kW}(1+0{,}8)^2 = 104{,}976$ kW $\equiv$ **50,21 dBW** ✓
- d) $m(t) = A_1\sin(2\pi f_1t) + A_2\sin(2\pi f_2t)$; $m_{tot} = 0{,}8 = m_1+m_2$; "si las amplitudes de los tonos son iguales, los índices de modulación también" → $m_1 = m_2 = 0{,}4$; $P_{total} = P_c\left(1+\dfrac{\sum m_i^2}{2}\right) = P_c\left(1+\dfrac{0{,}4^2+0{,}4^2}{2}\right) = 37{,}584$ kW $\equiv$ **45,75 dBW** ✓
- e) $PEP = P_c(1+m_{tot})^2 = 104{,}976$ kW $\equiv$ **50,21 dBW** ✓

---

## Ejercicio 2: PCM [2,5 puntos] — obtenido 1,3

**Enunciado:**

Cuatro señales de video analógica, cada una con un ancho de banda de **4,5 MHz**, se muestrean, cuantifican y codifican para obtener una señal PCM/TDM.

a) Determine la frecuencia de muestreo (sampling rate) de cada una de las señales, si deben muestrearse a una tasa **25% superior** a la tasa de Nyquist. [0,25 puntos] — ✅

b) Si las muestras se cuantifican en **1024 niveles**, determine el número de dígitos binarios requeridos para codificar cada muestra. [0,25 puntos] — ✅

c) Determine la tasa de pulsos binarios (bit-rate) de la señal codificada, y el ancho de banda mínimo ideal requerido para transmitir **las cuatro señales** PCM/TDM en código NRZ. [0,5 puntos] — **R** (regular)

d) Si la señal de video tiene un **rango dinámico de 3 dB**, un **factor de cresta de 4** y se utiliza cuantificación uniforme, determine la relación señal a ruido de cuantificación mínima obtenida [0,75 puntos] — ✓ parcial (tilde con punto)

e) La señal cuantificada y codificada determinada en c) se transmite por un servicio de comunicación de **472.500.000 bits por segundo**. Proponga un sistema que permita enviar las cuatro señales y el sincronismo. [0,75 puntos] — ❌

**Resolución entregada (hoja 2/4):**

- a) $f_m = 4{,}5$ MHz; $BW = 1{,}25\cdot 2\cdot f_m =$ **11,25 MHz** $\equiv 11{,}25$ M muestras/seg ✓
- b) $M = 1024$; $n = \log_2 M = \log_2 1024 =$ **10 binits/muestra** ✓
- c) $R_s = n\cdot f_s = 10\ \tfrac{\text{binits}}{\text{muestra}}\cdot 11{,}25\ \tfrac{\text{M muestras}}{\text{seg}} =$ **112,5 M binits/seg** — el corrector anota "**×4**" arriba del resultado. $B_{min} = R_s\cdot\dfrac{4}{2} =$ **225 MHz** (anotado: "4 señales TDM", "2 por ser banda base") ✓. Marca del ítem: **R**.
- d) $F_c = 4$; $SNR_Q = 3M^2\cdot\dfrac{1}{F_c^2} = 3\cdot\dfrac{1024^2}{4^2} = 196\,608 \equiv 20\log(\ ) =$ **105,87 dB** — el valor en dB está **tachado con una cruz**; al margen, tilde con guion.
- e) "$C = 472{,}5$ **G**bits/seg" — ❌ (sin sistema propuesto; además el dato es 472,5 **M**bits/s).

---

## Ejercicio 3: Ruido [2,5 puntos] — obtenido 1,75

**Enunciado:**

Se tiene un sistema de comunicaciones con una potencia de transmisión $P_T = 250$ Watts, la atenuación en el canal es de **55 dB** y densidad espectral de potencia de ruido es $2\times10^{-10}$ W/Hz a la entrada del demodulador considerado ideal. El ancho de banda del mensaje es **15 KHz** y el factor de cresta es **2**.

a) Determinar la relación señal a ruido de posdetección si se utiliza modulación de banda lateral única, expresada en dB. [0,25 puntos] — ✅

b) Determinar la relación señal a ruido de posdetección si se utiliza modulación de doble banda lateral sin portadora, expresada en dB. [0,25 puntos] — ✅

c) Determinar la relación señal a ruido de posdetección si se utiliza modulación de amplitud con 90% de índice de modulación, expresada en dB. [0,5 puntos] — ✅

d) Determinar la relación señal a ruido de posdetección si se utiliza modulación de frecuencia con desvío pico de frecuencia de **75 KHz**, expresada en dB. [0,5 puntos] — ✅

e) Idem d) pero con densidad espectral de potencia de ruido es $2\times10^{-9}$ W/Hz a la entrada. [0,5 puntos] — ❌ (en rojo)

f) Indicar cuál de las modulaciones anteriores requiere menor **potencia de transmisión** para lograr una relación señal a ruido de posdetección superior a **15 dB** y determinar su valor, expresado en dBm. [0,5 puntos] — **R** (en rojo)

**Resolución entregada (hoja sin número + hoja de continuación; arriba a la derecha dice "10 lg( )"):**

- Datos: $P_T = 250$ W; $N_0 = 2\cdot10^{-10}$ W/Hz; $\alpha = 55$ dB $\equiv 316\,227$ veces; $W = 15$ kHz; $F_c = 2$.
- a) $(S/N)_{D,SSB} = \gamma = \dfrac{S_R}{N_0\,W} = 263{,}524 \equiv$ **24,2 dB** ✓, con $S_R = \dfrac{250\text{ W}}{316\,227} = 790{,}569\ \mu$W.
- b) "SNR de posdetección DSB-SC es igual a la de SSB": $\gamma =$ **24,2 dB** ✓
- c) $m = 0{,}9$, AM: $(S/N)_{D,AM} = \gamma\cdot\dfrac{m^2/F_c^2}{1+m^2/F_c^2} = \gamma_{SSB}\cdot\dfrac{81}{481} = 44{,}377 \equiv$ **16,47 dB** ✓
- d) $(S/N)_{D,FM} = \gamma\cdot 3\left(\dfrac{\Delta f}{W}\right)^2\dfrac{1}{F_c^2} = 263{,}524\cdot 3\left(\dfrac{75\text{ kHz}}{15\text{ kHz}}\right)^2\dfrac{1}{2^2} = 4941{,}075 \equiv$ **36,94 dB** ✓
- e) $\gamma' = 26{,}352 \equiv 14{,}208$ dB; $(S/N)'_{D,FM} = \gamma'\cdot 3\left(\dfrac{75}{15}\right)^2\dfrac{1}{2^2} = 494{,}11 \equiv$ **26,94 dB** — al margen, en rojo: "**NO CUMPLE UMBRAL**".
- f) "La que requiere menor potencia de transmisión es FM". Sigue en la hoja de continuación: $\gamma = \dfrac{(S/N)_{D,FM}}{75/4} = \dfrac{31{,}622}{18{,}75} = 1{,}6865 = \dfrac{P_T/316\,227}{N_0\,W} \Rightarrow$ **$P_T = 1{,}6$ W** — en rojo: "**NO**" junto al resultado y "**Es FM pero $P_T$ no es correcta**".

---

## Ejercicio 4: OFDM [2,5 puntos] — obtenido 2,20

**Enunciado:**

Dado una señal OFDM compuesta por **24 portadoras** cada una de ellas moduladas en **16QAM** con duración de símbolo OFDM de **96 microsegundos**. Se pide:

a) Calcular la tasa de información en bits por segundo que transporta la señal. [0,5 puntos] — **B**

b) Calcular el ancho de banda mínimo. [0,5 puntos] — **B**

c) Calcular la cantidad de bits que transporta en cada símbolo OFDM. [0,25 puntos] — **M**

d) Calcular la eficiencia espectral para ancho de banda mínimo. [0,5 puntos] — **B−**

e) Calcular el ancho de banda mínimo si en vez de transmitir la señal OFDM se transmite la misma tasa de información (calculada en a) ) pero en una sola portadora modulada en 16-QAM. [0,25 puntos] — **B**

f) Indicar la ventaja de emplear la señal descrita en el enunciado versus transmitir la misma tasa de información (calculada en a) ) pero en una sola portadora modulada en 16-QAM. [0,5 puntos] — **B**

> Las marcas de este problema son letras: **B** (bien), **B−** (bien con descuento), **M** (mal). Son consistentes con el 2,20: todo bien salvo c) (0 de 0,25) y un descuento de 0,05 en d).

**Resolución entregada (hoja sin número, `20260929_211606.jpg`; marcas de la hoja en rojo y correcciones en rosa):**

- Datos: $N_p = 24$; 16 QAM; $T_s = 96\ \mu$seg.
- a) $\ell = \log_2 M = \log_2 16 = 4$ binits/símbolo ✓; $T_s = \dfrac{N_p\,\ell}{R_b} \Rightarrow R_b = \dfrac{N_p\,\ell}{T_s} = \dfrac{24\cdot 4\ \text{binits/símbolo}}{96\ \mu\text{seg}} =$ **1 Mbits/seg** ✓
- b) $B_T = N_p\cdot\dfrac{1}{T_s} = \dfrac{24}{96\ \mu\text{seg}} =$ **250 kHz** ✓
- c) $\ell = \log_2 M = \log_2 16 = 4$ binits/símbolo $=$ **4 bits/símbolo** — el corrector tacha "símbolo" y escribe "**port.**" (4 binits por portadora), tacha el resultado recuadrado y anota al margen "**96 bits/símb**".
- d) $\eta = \dfrac{R_b}{B} = \dfrac{1\ \text{Mbit/seg}}{250\ \text{kHz}} =$ **4 bits/símbolo** — al margen, el corrector anota "**4 bits/Hz**" (las unidades).
- e) $B_T = \dfrac{1}{T_s} = \dfrac{1}{\ell/R_b} = \dfrac{R_b}{\ell} = \dfrac{1\ \text{Mbits/seg}}{4\ \text{bits/símbolo}} =$ **250 kHz**, "es igual" ✓
- f) "La ventaja es que OFDM reduce la ISI (interferencia inter-símbolo) debido a que sus tiempos de símbolo son más largos y, en consecuencia, se reduce el solapamiento. En particular es de interés reducir la ISI por multitrayecto, que predomina en entornos urbanos por los rebotes de las señales en edificios." ✓ "Para 16-QAM, $T_s = 4\ \mu$seg, que está en el mismo orden de magnitud que los ecos urbanos de aprox. $1\ \mu$seg, imposibilitando la transmisión. OFDM, con $T_s$ mucho mayor, esquiva el problema." ✓

---

## Observaciones

**De 3,90 a 7,75.** Respecto de julio se mantuvieron **Modulación lineal** y **OFDM**; salieron Exponencial y Teoría de la Información como problemas propios, y entraron **PCM** y **Ruido**.

**El Ejercicio 3 es el mismo problema que `F_Comu_2022-12-01`**, con los mismos datos (250 W, 55 dB, $2\times10^{-10}$ W/Hz, 15 kHz). Allá el mensaje se describe con "relación potencia pico a potencia promedio de 4", que es lo mismo que factor de cresta 2 ($F_C^2 = 4$). En `F_Comu_2024-07-25` aparece una variante (500 W, 58 dB) donde el f) pide la potencia de transmisión "**instantánea, máxima**".

**El Ejercicio 4 es el mismo problema que `F_Comu_2022-12-15`, `F_Comu_2024-02-15` y `F_Comu_2024-05-13`** (24 portadoras, 16QAM, 96 μs).

**El Ejercicio 1 d) es AM multitono con el índice total repartido entre los tonos**: con dos tonos de igual amplitud, $m_1 = m_2 = m_{tot}/2 = 0{,}4$. Salió bien.

**Los puntos perdidos se concentran en ejecución, no en fórmulas**: en el 2 c) se informó el bit-rate de **una** señal y la corrección esperaba el de las cuatro (el corrector anota "×4"; el enunciado admite las dos lecturas); en el 2 d) el paso a dB se hizo con $20\log$ en vez de $10\log$ (el formulario listaba $SNR_Q$ entre los casos con 20); en el 3 e) y f) no se verificó el umbral de FM; en el 4 c) se dieron los bits de una subportadora (4) en vez de los del símbolo OFDM (96), y en el 4 d) la eficiencia quedó con unidades de bits/símbolo.
