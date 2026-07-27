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
| 5 | $\boxed{R_b = n\,f_s}$ | Tasa de bits (bit rate) |
| 6 | $\boxed{B_{min} = \dfrac{R_b}{\log_2 M_{mod}}}$ | Ancho de banda mínimo **pasabanda** (modulado) |

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

Es donde se equivocó el estudiante en `exercises/finales/md/F_Comu_2024-11-14_res.md` y se lo marcaron mal:

| Caso | $B_{min}$ |
|---|---|
| **Banda base** | $R_s/2$ |
| **Pasabanda** (modulado: QPSK, QAM, PSK…) | $R_s = \dfrac{R_b}{\log_2 M_{mod}}$ |

con $R_s$ = tasa de símbolos $= R_b/\log_2 M_{mod}$.

**Pasabanda es el doble de banda base** — modular duplica el ancho de banda, mismo motivo de siempre: el espectro se copia a $\pm f_c$. No confundir $M$ (niveles de cuantificación del ADC) con $M_{mod}$ (puntos de la constelación de la modulación digital): son cosas distintas y aparecen las dos en el mismo ejercicio.

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
| Tasa de símbolos (QPSK, $M_{mod}=4$) | $R_s = R_b/\log_2 4 = 64\text{k}/2$ | $32$ kbaud |
| Ancho de banda mínimo | $B_{min} = R_s$ | $\mathbf{32}$ **kHz** |

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
