# Simulacro — PCM sobre 16-QAM (30/07/2026)

> Practicar cronometrado: **30 minutos**, sin abrir la sección `<details>` de respuesta hasta terminar o agotar el tiempo. Seis ítems encadenados: cada uno usa el resultado del anterior.

**Nota:** simulacro preparado el día del final del 30/07/2026 (segundo simulacro de ese día). No proviene de un final real.

## Enunciado

**Problema — PCM sobre 16-QAM [2,5 puntos]**

Una señal de audio de **15 kHz** de ancho de banda se digitaliza con un ADC de cuantificación lineal de **256 niveles**, rango de entrada **8 V pico a pico**, y **factor de cresta 3**. Se muestrea un **20% por encima** de la frecuencia mínima de Nyquist.

El flujo resultante se transmite en **16-QAM**, con **amplitud máxima de constelación $9\sqrt{2}$ mV** (pico), símbolos equiprobables, sobre un canal con densidad espectral de ruido **$N_0 = 2\times10^{-12}$ W/Hz**. Potencia normalizada ($R=1\ \Omega$).

a) Frecuencia de muestreo y tasa de bits. [0,4 puntos]

b) Paso de cuantificación, error máximo de cuantificación y relación señal a ruido de cuantificación en dB. [0,4 puntos]

c) Velocidad de señalización, ancho de banda de nulo a nulo y ancho de banda mínimo ideal. [0,4 puntos]

d) Potencia media transmitida, expresada en dBm. [0,4 puntos]

e) Relación $E_b/N_0$ y probabilidad de error de bit. [0,5 puntos]

f) Eficiencia espectral a ancho de banda mínimo. Verifique si la modulación es realizable según el límite de Hartley-Shannon, tomando como ancho de banda equivalente de ruido el calculado en c) para el nulo a nulo. [0,4 puntos]

**Avisos que acompañaban el enunciado:**

- Hay **dos $M$ distintos** en el enunciado. Cuidado con cuál va en cada fórmula.
- La **amplitud máxima no es la amplitud media**, y la constelación no tiene envolvente constante.
- El ítem e) da un argumento de $Q(\cdot)$ que se lee del ábaco. Si da un número absurdo (mayor a 7 o menor a 1), revisar d) antes de seguir.

---

<details>
<summary><strong>Respuesta</strong></summary>

**a)** Nyquist es $2B = 30$ kHz, y se muestrea un 20% por encima:

$$f_s = 1{,}2\cdot 2B = 1{,}2\cdot 30\text{ kHz} = \boxed{36\text{ kHz}}$$

$$n = \log_2 256 = 8\ \text{bits/muestra} \quad\Rightarrow\quad R_b = n\,f_s = 8\cdot 36\times10^3 = \boxed{288\text{ kbps}}$$

**b)** Acá $M = 256$ son los **niveles del ADC**:

$$q = \frac{V_{pp}}{M} = \frac{8\text{ V}}{256} = \boxed{31{,}25\text{ mV}} \qquad e_{max} = \frac{q}{2} = \boxed{15{,}625\text{ mV}}$$

$$SNR_Q = \frac{3M^2}{F_C^2} = \frac{3\,(256)^2}{3^2} = 21845 \equiv \boxed{43{,}39\text{ dB}}$$

Chequeo en dB: $6{,}02\,n + 4{,}77 - 20\log F_C = 48{,}16 + 4{,}77 - 9{,}54 = 43{,}39$ dB ✓

**c)** Desde acá $M = 16$ es la **constelación**, $\ell = \log_2 16 = 4$ bits/símbolo:

$$D = \frac{R_b}{\ell} = \frac{288\text{ kbps}}{4} = \boxed{72\text{ kbaud}}$$

$$B_{nulo\text{-}nulo} = 2D = \boxed{144\text{ kHz}} \qquad B_{min} = D = \boxed{72\text{ kHz}}$$

**d)** La amplitud máxima es la **esquina** de la constelación, con niveles $\pm a, \pm 3a$ en cada eje:

$$\lvert s\rvert_{max} = \sqrt{(3a)^2 + (3a)^2} = 3a\sqrt2 = 9\sqrt2\text{ mV} \quad\Rightarrow\quad a = 3\text{ mV} = 3\times10^{-3}\text{ V}$$

Con las potencias de diez escritas **antes** de elevar al cuadrado:

$$\langle\lvert s\rvert^2\rangle = \frac{2(M-1)}{3}\,a^2 = 10\,a^2 = 10\,(9\times10^{-6}\text{ V}^2) = 90\times10^{-6}\text{ V}^2$$

$$S = \frac{\langle\lvert s\rvert^2\rangle}{2} = 45\times10^{-6}\text{ W} = \boxed{45\ \mu\text{W}} \;\Rightarrow\; 10\log\frac{45\times10^{-6}}{10^{-3}} = \boxed{-13{,}47\text{ dBm}}$$

Cota de control: la potencia media no puede superar la del símbolo más grande, $S \leq \lvert s\rvert_{max}^2/2 = 81\ \mu$W ✓

**e)**

$$E_b = \frac{S}{R_b} = \frac{45\times10^{-6}}{288\times10^3} = 1{,}5625\times10^{-10}\text{ J} \qquad \frac{E_b}{N_0} = \frac{1{,}5625\times10^{-10}}{2\times10^{-12}} = \boxed{78{,}1} \equiv \boxed{18{,}93\text{ dB}}$$

$$P_e \approx 4\,Q\!\left(\sqrt{\frac{3\,E_b}{(M-1)N_0}}\right) = 4\,Q\!\left(\sqrt{\frac{3\cdot 78{,}1}{15}}\right) = 4\,Q(3{,}95)$$

Del ábaco, $Q(3{,}95) \approx 3{,}9\times10^{-5}$, así que

$$P_e \approx 4\,(3{,}9\times10^{-5}) = \boxed{1{,}6\times10^{-4}}$$

(con $Q$ exacto: $1{,}5\times10^{-4}$). **Lo que se pide es $P_e$, no $Q$:** el 4 de adelante es parte de la respuesta.

**f)** Eficiencia espectral a ancho de banda mínimo:

$$\eta = \frac{R_b}{B_{min}} = \frac{288\text{ kbps}}{72\text{ kHz}} = \boxed{4\text{ bit/s/Hz}}$$

Ruido en el ancho de banda de nulo a nulo:

$$N = N_0\,B_{nulo\text{-}nulo} = 2\times10^{-12}\cdot 144\times10^3 = 2{,}88\times10^{-7}\text{ W} \qquad \frac{S}{N} = \frac{45\times10^{-6}}{2{,}88\times10^{-7}} = 156{,}25 \equiv 21{,}94\text{ dB}$$

Límite de Hartley-Shannon:

$$\left.\frac{C}{B}\right|_{max} = \log_2\!\left(1 + \frac{S}{N}\right) = \log_2 157{,}25 = 7{,}30\text{ bit/s/Hz}$$

Como $\eta = 4 < 7{,}30$, **la modulación es realizable**. Dicho con capacidad: $C = B_{min}\log_2(1+S/N) = 72\text{ kHz}\cdot 7{,}30 = 525$ kbps $> 288$ kbps.

---

### Lo que pasó al resolverlo el 30/07

| Ítem | Entregado | Correcto | Tipo de error |
|---|---|---|---|
| d) | $S = 15$ mW | $S = 45\ \mu$W | Prefijo al cuadrado: con amplitudes en mV y $R=1\ \Omega$, la potencia cae en μW, no en mW |
| e), primer intento | $E_b/N_0 = 28031$ | $78{,}1$ | Arrastrado de d). El argumento de $Q$ daba ~75, fuera del ábaco |
| e) | $3{,}9\times10^{-5}$ | $1{,}6\times10^{-4}$ | Entregó $Q(3{,}95)$ en vez de $P_e = 4\,Q(3{,}95)$ |

a), b), c) y f) no llegaron a corregirse ese día.

</details>
