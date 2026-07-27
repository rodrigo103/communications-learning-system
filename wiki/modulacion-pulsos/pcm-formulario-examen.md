---
tags:
  - wiki/modulacion-pulsos
  - wiki/planificacion
curso: Sistemas de Comunicaciones
unidad: 5
---

# PCM — Formulario de examen (compacto)

> **Last verified:** 2026-07-26 | **Verified by:** analysis + patrón real de ejercicios en `exercises/finales/md/`

> **Para qué es esta nota**: versión operativa y compacta para resolver ejercicios bajo reloj, armada sobre el patrón real de los finales. Para la explicación conceptual completa ver [[pcm-cuantificacion|PCM: Muestreo, Cuantificación y Codificación]] y [[../herramientas-matematicas/teorema-muestreo|Teorema de Muestreo]].
>
> **PCM es el tema más testeado de todos: 71,4% de los 42 finales únicos** (ver [[../planificacion/plan-11-dias-final#Frecuencia de Temas en los Finales|Frecuencia de Temas]]).

## La cadena PCM — 6 fórmulas

$$\text{Analógica} \to \boxed{\text{Muestreo}} \to \boxed{\text{Cuantificación}} \to \boxed{\text{Codificación}} \to \text{bits}$$

| # | Fórmula | Qué es |
|---|---|---|
| 1 | $\boxed{f_s \geq 2B}$ | **Nyquist** — frecuencia de muestreo mínima |
| 2 | $\boxed{M = 2^n}$ | $M$ niveles con $n$ bits por muestra |
| 3 | $\boxed{q = \dfrac{V_{pp}}{M}}$ | Paso de cuantificación. **Error máximo $= q/2$** |
| 4 | $\boxed{P_q = \dfrac{q^2}{12}}$ | Potencia de ruido de cuantificación |
| 5 | $\boxed{R_b = n\,f_s}$ | Tasa de bits [bps] |
| 6a | $\boxed{R_s = \dfrac{R_b}{\log_2 M_{mod}}}$ | Tasa de **símbolos** [baudios] |
| 6b | $\boxed{B_{min} = R_s \text{ (pasabanda)}}$ | Ancho de banda mínimo [Hz] |

## SNR de cuantificación — esta cátedra usa factor de cresta

Los finales suelen dar el dato como **"factor de cresta $F_C$"** ($=$ pico/RMS), no como "señal senoidal". La fórmula que usan:

$$\boxed{SNR_Q = \frac{3M^2}{F_C^2}}$$

**La fórmula famosa $SNR_Q \approx 6n + 1{,}76$ dB es el caso particular** con $F_C=\sqrt2$ (senoidal): $3M^2/2 = 1{,}5M^2$, y en dB da $10\log_{10}(1{,}5) + 20n\log_{10}2 = 1{,}76 + 6{,}02n$. **Es la misma fórmula, no dos distintas.**

| Si el enunciado dice… | Usar |
|---|---|
| "factor de cresta $F_C = \ldots$" | $SNR_Q = 3M^2/F_C^2$ |
| "señal senoidal" | $SNR_Q \approx 6n+1{,}76$ dB (o la de arriba con $F_C=\sqrt2$) |

Regla mnemotécnica del $6n$: **cada bit agregado mejora la SNR en ~6 dB** (duplicar $M$ cuadruplica $SNR_Q$).

## La trampa del ancho de banda (error frecuente)

Es donde se equivocó el estudiante en `exercises/finales/md/F_Comu_2024-11-14_res.md` y se lo marcaron mal.

**Son dos pasos con unidades distintas, no uno solo:**

$$R_b\ [\text{bps}] \xrightarrow{\ \div\log_2 M_{mod}\ } R_s\ [\text{baudios}] \xrightarrow{\ \text{Nyquist}\ } B_{min}\ [\text{Hz}]$$

| Paso                    | Fórmula                             | Unidad                   | Qué significa                                                                      |
| ----------------------- | ----------------------------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| **1. Tasa de símbolos** | $R_s = \dfrac{R_b}{\log_2 M_{mod}}$ | **baudios** (símbolos/s) | Cada símbolo lleva $\log_2M_{mod}$ bits, así que se mandan menos símbolos que bits |
| **2a. BW banda base**   | $B_{min} = R_s/2$                   | **Hz**                   | Nyquist: con ancho $B$ se pueden mandar $2B$ símbolos/s sin ISI                    |
| **2b. BW pasabanda**    | $B_{min} = R_s$                     | **Hz**                   | Modular duplica el ancho de banda (espectro copiado a $\pm f_c$)                   |

> **¿Por qué $B_{min}$ y $R_s$ dan el mismo número en pasabanda?** No es una identidad — es una **cancelación**: Nyquist aporta un $\tfrac12$ ($B=R_s/2$) y modular aporta un $2$, y $2\times\tfrac{R_s}{2}=R_s$. Son magnitudes **distintas** (una cuenta símbolos por segundo, la otra mide una extensión del eje de frecuencias); que ambas sean dimensionalmente $1/\text{s}$ es lo que permite que coincidan sin contradicción. **En banda base NO coinciden** ($B=R_s/2$), lo que confirma que no son lo mismo. [analysis]

> **¿Cómo se pasa de bps a baudios? ¿El denominador tiene unidades?** Sí — es **bits/símbolo**, y ahí está la conversión: [analysis]
> $$R_s\left[\frac{\text{símbolos}}{\text{s}}\right] = \frac{R_b\left[\frac{\text{bits}}{\text{s}}\right]}{\log_2 M_{mod}\left[\frac{\text{bits}}{\text{símbolo}}\right]}$$
> Los **bits se cancelan** y queda símbolos/s. Ejemplo QPSK: $\dfrac{64000\ \text{bits/s}}{2\ \text{bits/símbolo}} = 32000\ \text{símbolos/s} = 32$ kbaud.
>
> **Por qué $\log_2M_{mod}$ son bits por símbolo**: un símbolo elegido entre $M_{mod}$ posibilidades necesita $\log_2M_{mod}$ dígitos binarios para identificarse (con $M_{mod}=4$: 00, 01, 10, 11 → 2 bits). Es el mismo $\log_2$ de la entropía en [[../teoria-informacion/entropia-fuente|Teoría de la Información]] — un símbolo equiprobable entre $M$ transporta $\log_2M$ bits.
>
> **El detalle fino**: matemáticamente $\log_2M$ es un número puro (adimensional), pero "bit" y "símbolo" no son dimensiones físicas sino **unidades de conteo** (como el radián). Por eso:
>
> | Magnitud | Dimensión física | Qué cuenta |
> |---|---|---|
> | $R_b$ [bps] | $1/\text{s}$ | bits por segundo |
> | $R_s$ [baudios] | $1/\text{s}$ | símbolos por segundo |
> | $B$ [Hz] | $1/\text{s}$ | extensión en el eje de frecuencias |
>
> **Las tres son dimensionalmente $1/\text{s}$** — de ahí que puedan dar el mismo número sin contradicción. Lo que las distingue es *qué* cuentan, no la dimensión. Mismo fenómeno que Hz vs. rad/s.

**No confundir $M$ con $M_{mod}$**: $M$ = niveles de cuantificación del ADC (define $n=\log_2M$ bits por muestra); $M_{mod}$ = puntos de la constelación de la modulación digital (define cuántos bits van por símbolo). Son cosas distintas y aparecen las dos en el mismo ejercicio.

### Justificación del paso $R_s \to B_{min}$ (criterio de Nyquist sin ISI)

El puente entre tasa de símbolos y ancho de banda es el **criterio de Nyquist para señalización sin interferencia entre símbolos (ISI)**: por un canal pasabajos ideal de ancho $B$ se pueden transmitir como máximo $2B$ símbolos independientes por segundo. [analysis]

$$R_{s,max} = 2B \quad\Longrightarrow\quad \boxed{B_{min} = \frac{R_s}{2}}$$

**Demostración constructiva (el pulso sinc).** Transmitiendo con $p(t)=\operatorname{sinc}(t/T_s)=\dfrac{\sin(\pi t/T_s)}{\pi t/T_s}$, donde $T_s=1/R_s$ es el período de símbolo. La propiedad clave:

$$p(0)=1, \qquad p(kT_s)=0 \ \ \forall k\neq0 \quad(\text{porque }\sin(\pi k)=0)$$

Mandando $y(t)=\sum_k a_k\,p(t-kT_s)$ y muestreando en $t=mT_s$:

$$y(mT_s)=\sum_k a_k\,p\big((m-k)T_s\big) = a_m$$

Todos los términos con $k\neq m$ se anulan: **cada muestra recupera exactamente su propio símbolo, ISI cero**. Y el ancho de banda de ese pulso sale de su transformada, $\operatorname{sinc}(t/T_s)\leftrightarrow T_s\operatorname{rect}(fT_s)$ — un rectángulo no nulo solo para $|f|<\frac{1}{2T_s}=\frac{R_s}{2}$. O sea: el sinc **logra** ISI cero usando exactamente $R_s/2$ Hz, y Nyquist probó que no se puede hacer mejor.

**Es el teorema de muestreo dado vuelta.** El [[../herramientas-matematicas/teorema-muestreo|teorema de muestreo]] dice que una señal de ancho $B$ queda determinada por $2B$ muestras/segundo — o sea que **un canal de ancho $B$ tiene $2B$ grados de libertad por segundo**, y no se pueden especificar más números independientes que eso. Para mandar $R_s$ símbolos independientes hace falta $R_s\leq2B$. Es literalmente $f_s\geq2B$ aplicado al canal en vez de a la señal fuente.

**Por qué pasabanda duplica**: modular por $\cos(2\pi f_ct)$ copia el espectro a $\pm f_c$.

| | Contenido en frecuencias positivas | Ancho |
|---|---|---|
| Banda base | $(0,\ W)$ | $W$ |
| Pasabanda | $(f_c{-}W,\ f_c{+}W)$ | $2W$ |

Con $W=R_s/2$, pasabanda ocupa $2\times R_s/2=R_s$. Es el mismo "modular duplica el ancho de banda" de AM ($BW=2f_m$), no una regla nueva.

**Detalle práctico — roll-off**: el sinc ideal es irrealizable (dura infinito, pide filtro brick-wall). En la práctica se usa **coseno realzado** con factor $\alpha$:

$$B = \frac{R_s}{2}(1+\alpha)\ \text{[banda base]}, \qquad B = R_s(1+\alpha)\ \text{[pasabanda]}$$

Mismo trade-off que en [[../modulacion-analogica/modulacion-vsb|VSB]]: filtro ideal irrealizable → hay que pagar banda de transición. **Cuando el enunciado dice "ancho de banda mínimo *ideal*"** (que es como lo piden casi siempre en los finales) **es $\alpha=0$** y se usan las fórmulas limpias.

## Ejemplo completo verificado

**Enunciado** (de `F_Comu_2024-11-14_res.md`): señal 4 V pico a pico, valor medio nulo, $B=4$ kHz, factor de cresta $F_C=4$, cuantificada linealmente en $M=256$ niveles, modulada en QPSK.

| Paso | Cuenta | Resultado |
|---|---|---|
| Paso de cuantificación | $q = V_{pp}/M = 4/256$ | $15{,}6$ mV |
| Error máximo | $q/2$ | $\mathbf{7{,}81}$ **mV** |
| Ruido de cuantificación | $P_q = q^2/12$ | $\mathbf{20{,}35\ \mu}$**W** |
| SNR de cuantificación | $3M^2/F_C^2 = 3(256)^2/4^2 = 12288$ | $\mathbf{40{,}9}$ **dB** |
| Frecuencia de muestreo | $f_s = 2B = 2\times4$ kHz | $\mathbf{8}$ **kHz** |
| Bits por muestra | $n = \log_2 256$ | $8$ |
| Tasa de bits | $R_b = n f_s = 8\times8$ kHz | $\mathbf{64}$ **kbps** |
| Tasa de símbolos (QPSK, $M_{mod}=4$) | $R_s = R_b/\log_2 4 = 64\text{k}/2$ | $32$ **kbaud** |
| Ancho de banda mínimo (pasabanda) | $B_{min} = R_s$ *(mismo número, otra unidad)* | $\mathbf{32}$ **kHz** |

**Variante típica — muestrear por encima de Nyquist**: si $f_s$ es 25% superior a la mínima teórica, $f_s' = 10$ kHz y **todo escala $\times1{,}25$**: $R_b = 80$ kbps, $R_s = 40$ kbaud, $B_{min} = 40$ kHz. La SNR de cuantificación **no cambia** (depende solo de $M$ y $F_C$, no de $f_s$).

## Qué preguntan los finales (frecuencias reales)

Del relevamiento sobre los ejercicios de PCM del corpus:

- "Calcular el ancho de banda mínimo" — 7 apariciones
- "Calcular la tasa de información en bits por segundo" — 7
- "Calcular la eficiencia espectral para ancho de banda mínimo" — 7
- "Dibujar el diagrama en bloques de un sistema transmisor PAM/TDM" — 6
- "Ventaja de esta señal vs. transmitir la misma tasa con otro esquema" — 6

Notar que **casi todo termina en ancho de banda o tasa de bits** — la cadena de arriba resuelta de punta a punta cubre la mayoría.

## Ver también

- [[pcm-cuantificacion|PCM: Muestreo, Cuantificación y Codificación]] — explicación conceptual completa
- [[../herramientas-matematicas/teorema-muestreo|Teorema de Muestreo]] — de dónde sale $f_s\geq2B$
- [[companding|Companding]] — Ley A / Ley $\mu$, cuando la SNR debe ser independiente del nivel
- [[multiplex-tdm|Multiplexación TDM]] — aparece combinado con PAM en varios finales
- [[muestreo-ideal-natural|Muestreo Ideal y Natural]]
- [[../modulacion-digital/constelaciones|Constelaciones]] — para el $M_{mod}$ del último paso
- [[../planificacion/formulario-imprimible|Formulario Imprimible]]
