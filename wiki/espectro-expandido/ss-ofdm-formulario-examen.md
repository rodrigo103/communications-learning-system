---
tags:
  - wiki/espectro-expandido
  - wiki/planificacion
curso: Sistemas de Comunicaciones
unidad: 10
---

# Espectro Expandido y OFDM — Formulario de examen (compacto)

> **Last verified:** 2026-07-28 | **Verified by:** analysis + patrón real de ejercicios en `exercises/finales/md/`

> **57,1% de los 42 finales únicos** — el segundo tema más frecuente después de PCM. Son **dos sub-temas casi independientes**: DSSS (ganancia de procesamiento) y OFDM (subportadoras ortogonales).

## Glosario

| Símbolo | Nombre | Unidad |
|---|---|---|
| $L$ | Etapas del **LFSR** (registro de desplazamiento) | conteo |
| $N$ | Longitud de la **secuencia PN** | chips |
| $R_c$ | **Tasa de chips** | chips/s |
| $R_b$ | Tasa de bits (datos) | bps |
| $G_p$ | **Ganancia de procesamiento** | adimensional (se da en dB) |
| $B_{datos}$ | Ancho de banda **sin expandir** (solo BPSK con datos) | Hz — vale $2R_b$ |
| $B_{SS}$ | Ancho de banda **expandido** (spread spectrum) | Hz — vale $2R_c$ |
| $N_p$ | Cantidad de **subportadoras** OFDM | conteo |
| $\ell$ | Bits por símbolo de cada subportadora | bits/símbolo |
| $T_S$ | **Tiempo de símbolo OFDM** | s |
| $\Delta f$ | **Espaciado** entre subportadoras | Hz |
| $B_T$ | Ancho de banda total | Hz |

---

# Parte 1 — DSSS (Espectro Expandido por Secuencia Directa)

## Las 4 fórmulas

| #   | Fórmula                                                      | Notas                                                                                                                                      |
| --- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | $\boxed{N = 2^L - 1}$                                        | Longitud de secuencia máxima de un LFSR de $L$ etapas                                                                                      |
| 2   | $\boxed{R_c = \dfrac{N}{T_{sec}}}$                           | Tasa de chips ($T_{sec}$ = período de la secuencia)                                                                                        |
| 3   | $\boxed{G_p = \dfrac{R_c}{R_b} = \dfrac{B_{SS}}{B_{datos}}}$ | **Ganancia de procesamiento**. Las dos formas son equivalentes porque $\frac{B_{SS}}{B_{datos}}=\frac{2R_c}{2R_b}$ — **los 2 se cancelan** |
| 4   | $\boxed{B_{SS} = 2R_c}$ &nbsp;&nbsp; (y $B_{datos}=2R_b$)     | Anchos de banda **después** y **antes** de expandir (nulo a nulo, DS-BPSK). De acá sale directo la equivalencia de la fórmula 3            |

> **Qué significa $G_p$**: cuánto se ensancha el espectro, y equivalentemente **cuánta ventaja se gana contra interferencia**. Al despreader, la señal útil se recomprime mientras el interferente se dispersa → mejora efectiva de SNR en $G_p$.

> **Las unidades del $2$ en $B_{SS}=2R_c$** — es el **mismo caso** que $B_{n\text{-}n}=2D$ en [[../modulacion-digital/digital-formulario-examen#De dónde sale el $2D$, y las unidades del paso $D \to B$|Digital]], no una analogía: en DS-BPSK **el chip hace de símbolo**. El chip es un pulso rectangular de duración $T_c=1/R_c$, su espectro es una sinc con primer nulo en $f=1/T_c=R_c$, y al modular el lóbulo se extiende $R_c$ hacia cada lado de $f_c$. Descomposición completa: [analysis]
> $$B_{SS} = \underbrace{2}_{\substack{\text{lados del lóbulo}\\\text{adimensional}}} \times \underbrace{1\ \tfrac{\text{ciclo}}{\text{chip}}}_{\kappa,\ \text{conversión}} \times \underbrace{R_c\ \tfrac{\text{chips}}{\text{s}}}_{\text{tasa}} = 2R_c\ \left[\tfrac{\text{ciclos}}{\text{s}}\right]$$
> El **2 es geométrico** (los dos lados); la conversión real es $\kappa=1$ ciclo/chip, invisible porque vale 1. Contenido físico: en la frecuencia del primer nulo entra exactamente un ciclo en la duración de un chip.

> **El patrón de ejercicio** (aparece 9 veces): dan LFSR y período → sacar $R_c$ → sacar $G_p$ y $B$ → después piden **rediseñar para un $G_p$ objetivo** manteniendo $R_b$. Ahí se despeja al revés: $R_c = G_p\cdot R_b$.

## Ejemplo verificado (`F_Comu_2023-02-16`)

LFSR de $L=8$, período de secuencia $104{,}99\ \mu$s, datos BPSK a $R_b = 19{,}2$ kbps.

$$N = 2^8-1 = 255\ \text{chips} \ \Rightarrow\ R_c = \frac{255}{104{,}99\ \mu s} = \boxed{2{,}43\ \text{Mchips/s}}$$

$$G_p = \frac{2{,}43\times10^6}{19{,}2\times10^3} = 126{,}5 \equiv \boxed{21{,}0\ \text{dB}} \qquad B_{SS} = 2R_c = \boxed{4{,}86\ \text{MHz}}$$

*(Chequeo por la otra vía: $B_{datos}=2R_b=38{,}4$ kHz, y $B_{SS}/B_{datos}=4{,}86\text{M}/38{,}4\text{k}=126{,}5$ ✓ — mismo $G_p$.)*

**Para $G_p = 30$ dB $= 1000$ con la misma $R_b$:**

$$R_c' = G_p\cdot R_b = 1000\times19{,}2\text{k} = \boxed{19{,}2\ \text{Mchips/s}} \ \Rightarrow\ B_{SS}' = 2R_c' = \boxed{38{,}4\ \text{MHz}}$$

Hay que **subir la tasa de chips ~8 veces** (LFSR más largo o reloj más rápido). El precio: el ancho de banda crece en la misma proporción — **$G_p$ se compra con espectro**.

---

# Parte 2 — OFDM

## Las 4 fórmulas

| # | Fórmula | Notas |
|---|---|---|
| 1 | $\boxed{\text{bits/símbolo OFDM} = N_p\cdot\ell}$ | Todas las subportadoras transmiten en paralelo |
| 2 | $\boxed{T_S = \dfrac{N_p\,\ell}{R_b}}$ | Tiempo de símbolo OFDM |
| 3 | $\boxed{\Delta f = \dfrac{1}{T_S}}$ | **Espaciado entre subportadoras** — la condición de ortogonalidad |
| 4 | $\boxed{B_T = N_p\cdot\Delta f}$ | Ancho de banda total |

> **La clave de OFDM**: $\Delta f = 1/T_S$ **no es una elección de diseño, es la condición de ortogonalidad**. Con ese espaciado exacto, cada subportadora tiene un **nulo** en la frecuencia de todas las demás → se pueden superponer sin interferirse. Por eso OFDM es espectralmente tan eficiente: las subportadoras se solapan pero no se estorban.

> **Las unidades de la cadena $T_S \to \Delta f \to B_T$** — acá el factor de conversión **significa algo concreto**, a diferencia de los otros casos: [analysis]
>
> $$T_S = \frac{N_p\ell\ [\text{bits/símbolo}]}{R_b\ [\text{bits/s}]} = \left[\frac{\text{s}}{\text{símbolo}}\right] \qquad\Longrightarrow\qquad \frac{1}{T_S} = \left[\frac{\text{símbolos}}{\text{s}}\right] \xrightarrow{\ \kappa\ } [\text{Hz}]$$
>
> De nuevo aparece $\kappa=1$ ciclo/símbolo. Pero mientras en Nyquist o en el nulo a nulo ese $\kappa$ era casi un tecnicismo, **acá es literalmente la definición de ortogonalidad**:
>
> $$\boxed{\text{Dos subportadoras vecinas difieren en exactamente 1 ciclo por período de símbolo}}$$
>
> **Demostración**: dos subportadoras son ortogonales sobre $[0,T_S]$ si $\int_0^{T_S}e^{j2\pi(f_1-f_2)t}dt = 0$, lo que ocurre cuando $(f_1-f_2)T_S$ es un **entero no nulo**. El espaciado **mínimo** corresponde al entero 1:
> $$\Delta f\cdot T_S = 1 \quad\Rightarrow\quad \Delta f = \frac{1}{T_S}$$
> O sea: en un período de símbolo, cada subportadora completa **exactamente un ciclo más** que su vecina. Ese "1 ciclo por símbolo" **es** el $\kappa$ y **es** el mecanismo físico de la ortogonalidad — no es contabilidad de unidades.
>
> **El paso siguiente sí es limpio**: $B_T = N_p\cdot\Delta f$ con $N_p$ un conteo puro (adimensional) → Hz $\times$ número $=$ Hz, sin conversiones ocultas.

> **¿Dónde vive exactamente el $\kappa$ en $\Delta f = 1/T_S$?** En el **numerador** — es la constante 1 escrita implícitamente, $\Delta f = \dfrac{\kappa}{T_S}$. Pero se ve mejor **sin despejar**: [analysis]
> $$\Delta f\cdot T_S = \kappa, \qquad \underbrace{\Delta f}_{\text{ciclos/s}}\times\underbrace{T_S}_{\text{s/símbolo}} = \left[\frac{\text{ciclos}}{\text{símbolo}}\right]$$
> **El producto $\Delta f\,T_S$ tiene naturalmente unidades de ciclos/símbolo**, y $\kappa$ es su valor. No es un factor que se agrega: **es la magnitud que la condición de ortogonalidad iguala a un entero**.
>
> **Y acá está la diferencia con todos los otros $\kappa$ del curso:**
>
> | Caso | $\kappa$ | ¿De dónde sale? |
> |---|---|---|
> | Nyquist, nulo a nulo, chips, muestreo | $1$ | **Fijo por la física** — es donde cae el nulo de la sinc, no se elige |
> | **OFDM** | $1,2,3,\ldots$ | **Entero libre** — cualquiera da ortogonalidad; **se elige 1** |
>
> La ortogonalidad se cumple para **cualquier $\kappa$ entero**: con $\kappa=2$ las subportadoras seguirían siendo ortogonales, pero el espaciado y el ancho de banda total se duplicarían — desperdicio puro. **Se elige $\kappa=1$ porque es el mínimo espaciado ortogonal**, y de ahí sale la eficiencia espectral de OFDM.
>
> Entonces el $1$ del numerador de $\Delta f=1/T_S$ **no es un 1 trivial**: es una decisión de diseño — empaquetar lo más apretado posible sin perder ortogonalidad.

> **Consecuencia contraintuitiva**: $T_S$ es **larguísimo** comparado con una sola portadora ($1{,}024$ ms vs $0{,}625\ \mu$s en el ejemplo — **1600 veces más**). Eso es una **ventaja**: símbolos largos toleran mucho mejor la dispersión temporal del canal (multipath), que es el motivo real de usar OFDM.

**Posición de las subportadoras** (relativas a $f_c$, con $N_p$ par y espectro centrado):

$$f_k = f_c \pm \left(k+\tfrac12\right)\Delta f, \qquad k=0,1,\ldots,\tfrac{N_p}{2}-1$$

Las **dos centrales** quedan en $f_c\pm\frac{\Delta f}{2}$ — no hay ninguna exactamente en $f_c$.

## Ejemplo verificado (`F_Comu_2022-07-21_res`)

$R_b = 16$ Mbps, $N_p = 4096$ subportadoras, cada una en 16-QAM.

**a) Tiempo de símbolo OFDM**

$$\ell = \log_2 16 = 4 \ \Rightarrow\ \text{bits/símbolo} = 4096\times4 = 16\,384$$

$$T_S = \frac{16\,384\ \text{bits}}{16\times10^6\ \text{bps}} = \boxed{1{,}024\ \text{ms}}$$

**b) Ancho de banda mínimo ideal**

$$\Delta f = \frac{1}{T_S} = \frac{1}{1{,}024\text{ms}} = 976{,}56\ \text{Hz} \ \Rightarrow\ B_T = 4096\times976{,}56 = \boxed{4\ \text{MHz}}$$

**c) Frecuencias de subportadoras** (relativas a $f_c$)

**Por qué medio espaciado y no múltiplos enteros**: con $N_p$ **par** (4096) no se puede poner una subportadora en $f_c$ y mantener la simetría — quedarían 1 central + pares, o sea un número impar. Corriendo todo medio espaciado:

$$f_k = f_c \pm\left(k+\tfrac12\right)\Delta f, \qquad k=0,1,\ldots,\underbrace{2047}_{N_p/2-1}$$

quedan **2048 arriba + 2048 abajo = 4096** ✓, simétricas respecto de $f_c$, y **ninguna exactamente en $f_c$**.

**Los valores** (con $\Delta f = 976{,}5625$ Hz):

$$\text{centrales }(k=0):\quad f_c \pm 0{,}5\times976{,}5625 = f_c \pm 488{,}28\ \text{Hz}$$
$$k=2047:\quad 2047{,}5\times976{,}5625 = 1{,}999{,}512\ \text{Hz}$$
$$k=2046:\quad 2046{,}5\times976{,}5625 = 1{,}998{,}535\ \text{Hz}$$

| | Frecuencia |
|---|---|
| Dos **centrales** | $f_c \pm 488{,}28$ Hz $\ \left(=\pm\tfrac{\Delta f}{2}\right)$ |
| Dos **inferiores** | $f_c - 1{,}99951$ MHz y $f_c - 1{,}99854$ MHz |
| Dos **superiores** | $f_c + 1{,}99854$ MHz y $f_c + 1{,}99951$ MHz |

> **Chequeo de consistencia con $B_T$**: de centro a centro entre las extremas hay $2\times1{,}999{,}512 = 3{,}999{,}023$ Hz. El ancho **ocupado** suma media celda de cada lado (cada subportadora ocupa su propio $\Delta f$):
> $$B_T = 3{,}999{,}023 + 976{,}56 = 4{,}000{,}000\ \text{Hz} \ ✓$$
> Coincide exacto con $N_p\Delta f$. **De acá sale el "4 MHz o 4,001 MHz"** de la resolución transcripta: contando $N_p+1$ espaciados en vez de $N_p$ da $4097\times976{,}5625 = 4{,}001$ MHz. **La respuesta correcta es 4 MHz exactos.** [analysis]

> **Detalle práctico**: que **no haya subportadora en $f_c$** es conveniente — tras la bajada a banda base $f_c$ mapea a continua, donde los receptores tienen problemas (offset de DC, fuga del oscilador local). Los sistemas reales (WiFi, LTE) usan $N_p$ impar con una **subportadora nula** en el centro para lo mismo; acá se consigue el mismo efecto con el corrimiento de medio espaciado.

**d) Si la entrada fuera una sucesión continua de ceros**

**Qué cambia**: normalmente cada subportadora lleva un símbolo 16-QAM que **cambia** de un símbolo OFDM al siguiente. Esa variación aleatoria es lo que produce el espectro **continuo** — cada subportadora aporta una $\text{sinc}^2$ (por el enventanado rectangular de duración $T_S$) y al promediar sobre datos aleatorios se solapan en algo aproximadamente plano.

Con entrada constante, **todas las subportadoras transmiten siempre el mismo símbolo** → la señal se vuelve **periódica** con período $T_S$, y una señal periódica tiene **espectro de líneas**:

$$\boxed{4096\ \text{deltas de Dirac, separadas } \Delta f = 976{,}56\text{ Hz}}$$

Cada subportadora queda como un **tono puro** sin modular.

> **La idea de fondo, que conecta con Digital**: la DEP de una señal digital es $S(f)=\frac{\sigma_a^2}{T_s}|P(f)|^2$ — proporcional a la **varianza de los símbolos**. Sin variación de datos no hay ensanchamiento espectral. **El espectro continuo de OFDM lo produce la información, no las portadoras.** Ver [[../modulacion-digital/digital-formulario-examen|Digital — DEP]]. [analysis]

**e) Valor adecuado de $f_c$ para transmitir centrado en 3,9 GHz**

**El razonamiento**: las subportadoras no quedan centradas exactamente en el oscilador. Con la indexación que produce una IFFT (4096 salidas, de $-2048$ a $+2047$), el conjunto queda **corrido medio espaciado** respecto de $f_c$. Para que el espectro quede centrado en 3,9 GHz hay que compensar ese corrimiento:

$$|\text{corrimiento}| = \frac{\Delta f}{2} = \boxed{488{,}28\ \text{Hz}}$$

> ⚠️ **Sobre el signo**: la resolución transcripta dice $f_c = 3{,}9\text{ GHz} - 488{,}28$ Hz; con la indexación estándar de IFFT ($k=-N/2$ a $N/2-1$) da **$+488{,}28$**. **El signo depende de la convención de indexación** y no se puede verificar cuál usó el estudiante. **La magnitud (medio espaciado) es lo seguro y es lo que evalúa el ítem** — en el examen conviene *escribir explícitamente qué convención se usa* y justificar el corrimiento, para que el corrector vea el razonamiento aunque el signo dependa del criterio. [analysis]

**f) Tiempo de símbolo con una sola portadora en 1024-QAM**

$$\ell = \log_2 1024 = 10 \ \Rightarrow\ D = \frac{16\text{M}}{10} = 1{,}6\ \text{Mbaud} \ \Rightarrow\ T_{S1c} = \frac{1}{1{,}6\text{M}} = \boxed{0{,}625\ \mu\text{s}}$$

**El punto del ítem es el contraste:**

$$\frac{T_S^{OFDM}}{T_S^{1c}} = \frac{1{,}024\text{ ms}}{0{,}625\ \mu\text{s}} = \mathbf{1638}$$

Y ese factor sale de la estructura, no es casual:

$$\frac{T_S^{OFDM}}{T_S^{1c}} = N_p\cdot\frac{\ell_{OFDM}}{\ell_{1c}} = 4096\times\frac{4}{10} = 1638{,}4 \ ✓$$

> **Por qué eso es la ventaja de OFDM**: si el canal tiene dispersión temporal por multitrayecto (ecos de ~1 μs), con una sola portadora el eco se superpone a los ~1,6 símbolos siguientes → **ISI severa**. Con OFDM, 1 μs sobre 1024 μs de símbolo es un **0,1%** — despreciable, y el [[prefijo-ciclico|prefijo cíclico]] lo elimina del todo. **Ese es el motivo real de usar OFDM**, no la eficiencia espectral.

> ⚠️ **En la transcripción de este final las respuestas de d) y e) están intercambiadas** respecto de los ítems del enunciado — verificado recalculando. Acá están puestas donde corresponden.

## Los errores que cuestan puntos

1. **Olvidar el $-1$ en $N=2^L-1$** — la secuencia máxima nunca incluye el estado todo-ceros
2. **Confundir $R_c$ con $R_b$** en $G_p$ — la ganancia es chips sobre bits, siempre $>1$
3. **Calcular $\Delta f$ como $B_T/N_p$ sin verificar $\Delta f=1/T_S$** — dan lo mismo, pero la ortogonalidad es la que manda
4. **Poner una subportadora en $f_c$** — con $N_p$ par no hay ninguna en el centro exacto

## Ver también

- [[dsss|DSSS]] · [[fhss|FHSS]] · [[cdma|CDMA]] · [[ofdm|OFDM]]
- [[prefijo-ciclico|Prefijo Cíclico]] — protección contra multipath (aparece en 1 final)
- [[../modulacion-digital/digital-formulario-examen|Modulación Digital]] — el $\ell=\log_2M$ de cada subportadora
- [[../herramientas-matematicas/transformada-hilbert#OFDM|Transformada de Hilbert — OFDM]] — de dónde sale $v(t)=x(t)\cos\omega_ct - y(t)\sin\omega_ct$
