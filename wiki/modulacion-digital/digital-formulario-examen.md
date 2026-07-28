---
tags:
  - wiki/modulacion-digital
  - wiki/planificacion
curso: Sistemas de Comunicaciones
unidad: 6
---

# Modulación Digital — Formulario de examen (compacto)

> **Last verified:** 2026-07-27 | **Verified by:** analysis + patrón real de ejercicios en `exercises/finales/md/`

> **Para qué es esta nota**: versión operativa para resolver bajo reloj. Explicación conceptual completa en [[ask-fsk-psk|ASK, FSK, PSK]], [[modulacion-qam|Modulación QAM]] y [[probabilidad-error|Probabilidad de Error (BER)]].
>
> **Modulación Digital aparece en 40,5% de los 42 finales únicos.** Menos que PCM o AM/FM, pero sus fórmulas se reusan en Ruido/BER, así que rinde doble.

## Cadena de fórmulas

$$R_b\ [\text{bps}] \to \ell \to D\ [\text{baudios}] \to B\ [\text{Hz}] \to SNR \to BER$$

| # | Nombre | Fórmula | Qué es y para qué sirve |
|---|---|---|---|
| 1 | **Bits por símbolo** (orden de la modulación) | $\boxed{\ell = \log_2 M}$ | Cuántos bits codifica cada punto de la constelación. Define la modulación: QPSK → $\ell=2$; 16-QAM → $\ell=4$; 64-QAM → $\ell=6$. Unidad: bits/símbolo |
| 2 | **Tasa de símbolos** (velocidad de señalización) | $\boxed{D = \dfrac{R_b}{\ell}}$ | Cuántos símbolos por segundo salen al canal. **Es lo que determina el ancho de banda**, no $R_b$. Unidad: baudios. También se escribe $R_s$ |
| 3 | **Potencia de ruido** en la banda | $\boxed{N = N_0\,B_N}$ | Ruido total que entra al receptor. $N_0$ = densidad espectral de ruido [W/Hz], $B_N$ = ancho de banda equivalente de ruido. Unidad: W |
| 4 | **Energía por bit** | $\boxed{E_b = \dfrac{S}{R_b} = S\,T_b}$ | Energía que el transmisor gasta en cada bit: potencia $\times$ duración de bit ($T_b=1/R_b$). Unidad: Joules |
| 5 | **Relación $E_b/N_0$** | $\boxed{\dfrac{E_b}{N_0} = SNR\cdot\dfrac{B}{R_b}}$ | La métrica universal de calidad de un enlace digital — **es lo que entra en la fórmula de BER**. Adimensional (se suele dar en dB) |

> **¿Por qué $E_b/N_0$ y no directamente SNR?** Porque la SNR depende del ancho de banda elegido, así que **no permite comparar modulaciones distintas de forma justa**. $E_b/N_0$ normaliza por bit y por densidad de ruido, y queda independiente de $B$ y de $R_b$ — por eso todas las curvas de BER se grafican contra $E_b/N_0$ y no contra SNR. La fórmula 5 es el puente entre ambas. Detalle en [[../conceptos-integradores/eb-n0-vs-snr|$E_b/N_0$ vs SNR]]. [analysis]

### ¿$\ell$ es lo mismo que el $n$ de PCM?

Misma **fórmula**, cosas **distintas** — y los símbolos distintos ($n$ vs $\ell$, ambos usados así por la cátedra) están justamente para no mezclarlas: [analysis]

| | PCM | Digital |
|---|---|---|
| Símbolo | $n$ | $\ell$ |
| Qué cuenta $M$ | **Niveles del ADC** | **Puntos de la constelación** |
| Unidad | bits/**muestra** | bits/**símbolo** |
| Etapa | Digitalización (fuente) | Transmisión |

**Son números independientes**: en el ejercicio del CD-Audio, $n=16$ bits/muestra (ADC de 65536 niveles); si eso se transmite en QPSK, $\ell=2$ bits/símbolo. Nada obliga a que coincidan, y en `F_Comu_2024-11-14_res.md` aparecen los dos en el mismo problema ($M=256$ niveles → $n=8$; QPSK → $\ell=2$).

**Dónde se conectan — la cadena completa:**

$$\frac{\text{muestras}}{\text{s}} \xrightarrow{\ \times n\ } \frac{\text{bits}}{\text{s}} \xrightarrow{\ \div\ell\ } \frac{\text{símbolos}}{\text{s}} \xrightarrow{\ \text{Nyquist}\ } \text{Hz}$$

$$f_s \xrightarrow{\ \times n\ } R_b \xrightarrow{\ \div\ell\ } D \xrightarrow{\ \times1\ \text{(pasabanda)}\ } B$$

$n$ **multiplica** al entrar y $\ell$ **divide** al salir: los dos son factores de conversión del mismo tipo ("bits por algo"), actuando en etapas distintas y en direcciones opuestas — $n$ convierte muestras→bits, $\ell$ convierte bits→símbolos. Ver la contabilidad de unidades completa en [[../modulacion-pulsos/pcm-formulario-examen#Cómo funcionan las unidades en toda la cadena|PCM — Cómo funcionan las unidades]].

## Los tres anchos de banda — no confundirlos

Los finales piden los tres y son distintos. Confundirlos es el error más frecuente:

| Cuál                       | Fórmula           | Cuándo se usa                                                                                   |
| -------------------------- | ----------------- | ----------------------------------------------------------------------------------------------- |
| **Nulo a nulo**            | $B = 2D$          | Pulso rectangular, ancho del lóbulo principal. **Lo piden explícitamente 4 veces en el corpus** |
| **Mínimo (Nyquist ideal)** | $B = D$           | Cuando dice "ancho de banda mínimo ideal" ($\alpha=0$)                                          |
| **Con roll-off**           | $B = D(1+\alpha)$ | Coseno realzado real; el enunciado da $\alpha$                                                  |

Ver la justificación del $B=D$ pasabanda en [[../modulacion-pulsos/pcm-formulario-examen#Justificación del paso $R_s \to B_{min}$ (criterio de Nyquist sin ISI)|criterio de Nyquist sin ISI]] — es la misma relación, con $D$ en lugar de $R_s$.

### De dónde sale el $2D$, y las unidades del paso $D \to B$

**Origen del nulo a nulo**: un pulso rectangular de duración $T_s=1/D$ tiene espectro $\text{sinc}(fT_s)$, con **primer nulo** donde $f\,T_s=1$, o sea $f=1/T_s=D$. En pasabanda ese lóbulo queda centrado en $f_c$ y se extiende $D$ hacia cada lado → ancho total $2D$. [analysis]

**La conversión de unidades**: $D$ está en símbolos/s y $B$ en ciclos/s, así que **tiene que haber un factor de conversión** — y lo hay, solo que vale 1 y por eso no se escribe:

$$f_0 = \kappa\cdot\frac{1}{T_s}, \qquad \kappa = 1\ \frac{\text{ciclo}}{\text{símbolo}}$$

**Contenido físico de $\kappa$**: en la frecuencia del primer nulo entra **exactamente un ciclo de la sinusoide en una duración de símbolo**. Eso es lo que hace que los números coincidan; es invisible en la fórmula solo porque su valor numérico es 1.

La contabilidad completa tiene entonces **tres** factores, no dos:

$$B_{n\text{-}n} = \underbrace{2}_{\substack{\text{lados del lóbulo} \\ \text{adimensional}}} \times \underbrace{1\ \tfrac{\text{ciclo}}{\text{símbolo}}}_{\kappa,\ \text{conversión}} \times \underbrace{D\ \tfrac{\text{símbolos}}{\text{s}}}_{\text{tasa}} = 2D\ \left[\tfrac{\text{ciclos}}{\text{s}}\right]$$

**Y esto unifica los tres anchos de banda** — son la misma relación con distinto $\kappa$ total:

| Relación | $\kappa$ total [ciclos/símbolo] | De dónde sale |
|---|---|---|
| $B = D/2$ (Nyquist banda base) | $1/2$ | los 2 símbolos/ciclo de Nyquist, invertidos |
| $B = D$ (Nyquist pasabanda) | $1$ | anclaje puro: 1 ciclo/símbolo |
| $B = 2D$ (nulo a nulo, pulso rectangular) | $2$ | anclaje $\times$ 2 lados del lóbulo |

> **Ojo con los dos "2" distintos**: el de Nyquist ($R_s=2B$) es **2 símbolos/ciclo**, un factor de conversión con contenido físico; el de nulo a nulo ($B=2D$) es **2 lados**, pura simetría geométrica. Se confunden fácil porque ambos relacionan $B$ con $D$. [analysis]
>
> **Consecuencia útil**: $B_{n\text{-}n} = 2\,B_{min}$ en pasabanda. Esa duplicación es **el precio de usar pulsos rectangulares** en vez de pulsos sinc — rectangular en tiempo se desparrama en frecuencia (sinc), mientras que sinc en tiempo da un rectángulo compacto en frecuencia. Mismo trade-off tiempo-frecuencia de siempre.

## BER — las fórmulas a tener

$$\boxed{P_e^{BPSK} = P_e^{QPSK} = Q\!\left(\sqrt{\frac{2E_b}{N_0}}\right)}, \qquad \boxed{P_e^{FSK\ coh} = Q\!\left(\sqrt{\frac{E_b}{N_0}}\right)}$$

**BPSK y QPSK dan lo mismo por bit** — QPSK transmite el doble de bits en el mismo ancho de banda **sin penalidad de BER**. Es la razón de que QPSK sea tan usada, y un punto conceptual que los finales preguntan.

Para $M$-QAM:

$$P_e \approx \frac{4}{\ell}\left(1-\frac{1}{\sqrt M}\right)Q\!\left(\sqrt{\frac{3\,\ell\,E_b}{(M-1)N_0}}\right)$$

**El trade-off central**: al subir $M$ se gana eficiencia espectral ($\ell$ bits por símbolo) pero **empeora la BER** para el mismo $E_b/N_0$ — los puntos de la constelación quedan más juntos. Ver [[constelaciones|Constelaciones]].

## Ejercicio resuelto — 16-QAM (`F_Comu_2026-02-26_res.md`)

> ⚠️ **Los dos estudiantes que rindieron este ejercicio lo reprobaron** (1,5/2,5 y 0,75/2,5). Vale la pena estudiar dónde fallaron.

**Enunciado**: señal digital pasabanda 16-QAM, $f_c=50$ MHz, amplitud máxima $3\sqrt2$ mV (pico), símbolos equiprobables, $R_b = 256$ kbps, $N_0 = 4\times10^{-14}$ W/Hz.

**a) Ancho de banda de nulo a nulo**

$$\ell = \log_2 16 = 4 \ \Rightarrow\ D = \frac{256\text{k}}{4} = 64\text{ kbaudios} \ \Rightarrow\ \boxed{B_{n\text{-}n} = 2D = 128\text{ kHz}}$$

**b) Densidad espectral de potencia**

Lóbulo principal centrado en $f_c$, con **nulos en $f_c\pm64$ kHz, $\pm128$ kHz, $\pm192$ kHz** (múltiplos de $D$). Forma $\text{sinc}^2$, típica de señalización pasabanda con pulso rectangular.

> **Justificación completa de la DEP** (no está cubierto en otra nota de la vault — `densidad-espectral-potencia.md` trata Wiener-Khinchin en general, no este caso). [analysis]
>
> **¿Qué hay en el eje vertical?** **Densidad espectral de potencia**, en W/Hz (o V²/Hz si es normalizada) — es decir, **potencia por unidad de ancho de banda**, no amplitud ni potencia. Integrar la curva sobre toda la frecuencia devuelve la potencia total $S$. Por eso la unidad tiene "/Hz": es una densidad, igual que $N_0$ del ruido.
>
> **¿Por qué sinc — y por qué al cuadrado?** La señal es una secuencia *aleatoria* de símbolos, cada uno con forma de pulso $p(t)$. Para símbolos independientes y equiprobables:
> $$S(f) = \frac{\sigma_a^2}{T_s}\,|P(f)|^2$$
> con $P(f)=\mathcal F\{p(t)\}$ y $\sigma_a^2$ la varianza de los símbolos. La cadena es:
>
> | Paso | Resultado |
> |---|---|
> | Pulso **rectangular** de duración $T_s$ en el tiempo | $p(t)$ |
> | Su transformada de Fourier | $P(f)=A\,T_s\operatorname{sinc}(fT_s)$ → **sinc** |
> | La DEP es $\|P(f)\|^2$ (magnitud al cuadrado, porque es potencia) | $\propto\operatorname{sinc}^2(fT_s)$ → **sinc²** |
>
> O sea: **sinc** aparece por ser la transformada del rectángulo; **el cuadrado** aparece porque la DEP es una magnitud de potencia. Al modular, esa DEP de banda base se copia a $\pm f_c$ y **se divide por 4**: $S_{pb}(f)=\tfrac14[S_{bb}(f-f_c)+S_{bb}(f+f_c)]$.
>
> **¿Por qué $\tfrac14$ y no $\tfrac12$?** Porque **el $\tfrac12$ es de amplitud y la DEP es potencia** — se eleva al cuadrado:
> $$\mathcal F\{m(t)\cos(2\pi f_ct)\} = \tfrac12\big[M(f-f_c)+M(f+f_c)\big] \ \longrightarrow\ \left(\tfrac12\right)^2 = \tfrac14$$
> La propiedad de modulación pone $\tfrac12$ en **cada copia** (viene de Euler: el coseno son dos exponenciales, cada una con la mitad). Como la DEP va con $|\cdot|^2$, ese $\tfrac12$ se vuelve $\tfrac14$.
>
> **Chequeo por conservación de potencia** — si fuera $\tfrac12$ por copia la potencia total quedaría igual que en banda base, lo cual es falso:
> $$\int S_{pb}(f)\,df = \tfrac14P_m + \tfrac14P_m = \frac{P_m}{2}$$
> Dos copias, $\tfrac14$ cada una → factor total $\tfrac12$. Coincide exacto con la cuenta en el tiempo, $P_s=\langle m^2\cos^2\rangle=\tfrac12\langle m^2\rangle$, usando $\langle\cos^2\rangle=\tfrac12$: **modular parte la potencia al medio**, y el $\tfrac14$ por copia es lo que hace cerrar la contabilidad.
>
> **Es el mismo "factor 2" recurrente del curso** — el que costó puntos en la pregunta 3 de `exercises/autoevaluacion-am.md` (las deltas de $S_{AM}(f)$ valen $A_c/2$ y $A_c m/4$, no $A_c$ y $A_cm/2$):
>
> | Dónde | Magnitud real | Al pasar a frecuencia |
> |---|---|---|
> | Coseno → deltas (AM) | $A_c$ | $A_c/2$ por delta |
> | Espectro → DEP (Digital) | $\tfrac12$ por copia | $\tfrac14$ por copia |
>
> **Cada coseno real se reparte en dos mitades**, y si además se está en una magnitud de potencia, esas mitades se elevan al cuadrado.
>
> *(Detalle técnico: el $\tfrac14$ por copia vale porque las dos copias **no se superponen**, o sea $f_c>W$ — la misma condición pasabanda de [[../herramientas-matematicas/transformada-hilbert#Aplicaciones en Comunicaciones|Hilbert]]. Si se solaparan habría términos cruzados.)*
>
> **¿Dónde caen los nulos?** $\operatorname{sinc}^2(fT_s)$ se anula donde $fT_s$ es entero no nulo, o sea en $f=\pm kD$ (con $D=1/T_s$). Trasladado a pasabanda: **$f_c\pm kD$** para $k=1,2,3\ldots$ — en este ejercicio $f_c\pm64$, $\pm128$, $\pm192$ kHz. El lóbulo principal va de $f_c-D$ a $f_c+D$, ancho $2D$.
>
> **Alturas relativas de los lóbulos** (valores estándar de $\operatorname{sinc}^2$, sirven para dibujar "con suficiente detalle"):
>
> | Lóbulo | Altura relativa al pico | En dB |
> |---|---|---|
> | Principal | $1$ | $0$ dB |
> | 1er lateral | $0{,}047$ | $\mathbf{-13{,}3}$ **dB** |
> | 2do lateral | $0{,}016$ | $-17{,}8$ dB |
> | 3er lateral | $0{,}008$ | $-20{,}8$ dB |
>
> El **lóbulo principal concentra ~90% de la potencia total** — por eso el ancho de banda de nulo a nulo es una medida razonable pese a que el espectro se extiende infinitamente. El $-13{,}3$ dB del primer lateral es el número clásico del pulso rectangular, y es la razón de que se usen pulsos conformados (coseno realzado) cuando importa no interferir a los canales vecinos: bajan muchísimo los lóbulos laterales a cambio de $\alpha$ de exceso de banda.

**c) Potencia normalizada** — ⚠️ **acá cayeron los dos.** Cuenta completa en 4 pasos:

**Paso 1 — sacar la constelación del dato.** 16-QAM es una grilla 4×4 con niveles I/Q en $\pm a,\pm3a$. Los 16 puntos tienen **tres magnitudes distintas**:

| Puntos | Coordenadas | $\lvert s\rvert=\sqrt{I^2+Q^2}$ | Cuántos |
|---|---|---|---|
| Interiores | $(\pm a,\pm a)$ | $a\sqrt2$ | 4 |
| Intermedios | $(\pm a,\pm3a)$, $(\pm3a,\pm a)$ | $a\sqrt{10}$ | 8 |
| Esquinas | $(\pm3a,\pm3a)$ | $3a\sqrt2$ | 4 |

La **amplitud máxima** del enunciado ($3\sqrt2$ mV) corresponde a las esquinas: $3a\sqrt2=3\sqrt2$ mV $\Rightarrow \boxed{a=1\text{ mV}}$. De ahí los tres niveles $\sqrt2$, $\sqrt{10}$, $3\sqrt2$ mV.

**Paso 2 — promediar sobre la constelación** (símbolos equiprobables):

$$\langle\lvert s\rvert^2\rangle = \frac{4(2a^2)+8(10a^2)+4(18a^2)}{16} = \frac{160}{16}a^2 = 10a^2 = 10\text{ mV}^2$$

Fórmula general para no rehacer la tabla ($M$-QAM cuadrada con niveles $\pm a,\pm3a,\ldots$):

$$\boxed{\langle\lvert s\rvert^2\rangle = \frac{2(M-1)}{3}\,a^2} \qquad (M=16 \to \tfrac{2\cdot15}{3}a^2 = 10a^2 \ ✓)$$

**Paso 3 — pico → promedio del portador** ← *el paso que se saltearon*. $\lvert s\rvert$ es la **amplitud pico** de la sinusoide transmitida, porque el símbolo viaja como

$$s(t) = I\cos(\omega_ct)-Q\sin(\omega_ct) = \lvert s\rvert\cos(\omega_ct+\phi)$$

y una sinusoide de pico $A$ tiene potencia media $A^2/2$, **no** $A^2$:

$$P = \frac{\langle\lvert s\rvert^2\rangle}{2} = \frac{10\text{ mV}^2}{2} = \boxed{5\ \mu\text{W}}$$

**Paso 4 — a dBm** (como pedía el enunciado):

$$P_{dBm} = 10\log_{10}\!\left(\frac{5\times10^{-6}}{10^{-3}}\right) = 10\log_{10}(5\times10^{-3}) = \boxed{-23{,}0\text{ dBm}}$$

*(Ninguno de los dos consignó el valor en dBm de forma legible.)*

> **Qué falló exactamente**: el estudiante llegó a $10\,\mu$W, o sea **hizo bien el promedio sobre la constelación** (paso 2) pero **olvidó el $/2$ del portador** (paso 3). Eso es lo que el corrector llamó "factor de cresta": el $\sqrt2$ entre pico y RMS de la sinusoide.
>
> **Son dos efectos distintos, conviene no mezclarlos:**
>
> | Efecto | Factor en potencia | ¿Lo aplicó? |
> |---|---|---|
> | Promedio sobre la constelación (máx vs medio de $\lvert s\rvert$) | $18/10 = 1{,}8$ | ✅ Sí |
> | Pico → RMS del portador sinusoidal | $2$ | ❌ **No** |
>
> El factor de cresta aparece sistemáticamente en esta cátedra — también en [[../modulacion-pulsos/pcm-formulario-examen#SNR de cuantificación — esta cátedra usa factor de cresta|PCM]] y en [[../derivaciones/modulacion-am#¿Cual metodo conviene usar en el examen?|AM]]. Conviene tenerlo como reflejo: **si te dan una amplitud máxima y te piden potencia, preguntate si la señal tiene amplitud constante o no.**

**d) Relación señal a ruido**

$$N = N_0 B_N = 4\times10^{-14}\times128\times10^3 = 5{,}12\text{ nW}$$

$$SNR = \frac{5\ \mu\text{W}}{5{,}12\ \text{nW}} = 976{,}6 \ \Rightarrow\ \boxed{SNR \approx 29{,}9\text{ dB}}$$

*(El estudiante había obtenido 32,99 dB arrastrando la potencia sin corregir; el corrector anotó "arrastra error" — igual descuenta.)*

**e) BER con filtro acoplado (QPSK)** — *ninguno de los dos llegó*

$$\frac{E_b}{N_0} = SNR\cdot\frac{B}{R_b} = 976{,}6\times\frac{128\text{k}}{256\text{k}} = 488$$

$$P_e = Q\!\left(\sqrt{2\times488}\right) = Q(31{,}2) \approx 0$$

BER prácticamente nula — el enlace tiene muchísimo margen.

## Los cuatro errores que cuestan el ejercicio

Del análisis de cómo fallaron los estudiantes reales:

1. **Confundir los tres anchos de banda** — nulo a nulo ($2D$) vs mínimo ideal ($D$) vs con roll-off ($D(1+\alpha)$)
2. **Olvidar el factor de cresta** al calcular potencia desde la amplitud máxima de la constelación
3. **Arrastrar el error** de un ítem al siguiente — el corrector lo marca ("arrastra error") pero **descuenta igual**
4. **No llegar al BER** por quedarse trabado antes. Recordar la regla del examen: **25% desarrollado por punto como mínimo**; conviene plantear la fórmula aunque no se termine la cuenta

## Ver también

- [[ask-fsk-psk|ASK, FSK, PSK]] — las tres modulaciones básicas
- [[modulacion-qam|Modulación QAM]]
- [[constelaciones|Constelaciones]] — diagramas I/Q, de donde sale el factor de cresta
- [[probabilidad-error|Probabilidad de Error (BER)]] — curvas BER vs $E_b/N_0$
- [[eficiencia-espectral|Eficiencia Espectral]]
- [[../modulacion-pulsos/pcm-formulario-examen|PCM — Formulario de examen]] — la cadena previa (PCM genera los bits que esto transmite)
- [[../conceptos-integradores/eb-n0-vs-snr|$E_b/N_0$ vs SNR]] — el puente de la fórmula 5, en detalle
- [[../planificacion/formulario-imprimible|Formulario Imprimible]]
