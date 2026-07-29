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
| $N_p$ | Cantidad de **subportadoras** OFDM | conteo |
| $\ell$ | Bits por símbolo de cada subportadora | bits/símbolo |
| $T_S$ | **Tiempo de símbolo OFDM** | s |
| $\Delta f$ | **Espaciado** entre subportadoras | Hz |
| $B_T$ | Ancho de banda total | Hz |

---

# Parte 1 — DSSS (Espectro Expandido por Secuencia Directa)

## Las 4 fórmulas

| # | Fórmula | Notas |
|---|---|---|
| 1 | $\boxed{N = 2^L - 1}$ | Longitud de secuencia máxima de un LFSR de $L$ etapas |
| 2 | $\boxed{R_c = \dfrac{N}{T_{sec}}}$ | Tasa de chips ($T_{sec}$ = período de la secuencia) |
| 3 | $\boxed{G_p = \dfrac{R_c}{R_b} = \dfrac{B_{SS}}{B_{datos}}}$ | **Ganancia de procesamiento** |
| 4 | $\boxed{B = 2R_c}$ | Ancho de banda transmitido (nulo a nulo, DS-BPSK) |

> **Qué significa $G_p$**: cuánto se ensancha el espectro, y equivalentemente **cuánta ventaja se gana contra interferencia**. Al despreader, la señal útil se recomprime mientras el interferente se dispersa → mejora efectiva de SNR en $G_p$.

> **El patrón de ejercicio** (aparece 9 veces): dan LFSR y período → sacar $R_c$ → sacar $G_p$ y $B$ → después piden **rediseñar para un $G_p$ objetivo** manteniendo $R_b$. Ahí se despeja al revés: $R_c = G_p\cdot R_b$.

## Ejemplo verificado (`F_Comu_2023-02-16`)

LFSR de $L=8$, período de secuencia $104{,}99\ \mu$s, datos BPSK a $R_b = 19{,}2$ kbps.

$$N = 2^8-1 = 255\ \text{chips} \ \Rightarrow\ R_c = \frac{255}{104{,}99\ \mu s} = \boxed{2{,}43\ \text{Mchips/s}}$$

$$G_p = \frac{2{,}43\times10^6}{19{,}2\times10^3} = 126{,}5 \equiv \boxed{21{,}0\ \text{dB}} \qquad B = 2R_c = \boxed{4{,}86\ \text{MHz}}$$

**Para $G_p = 30$ dB $= 1000$ con la misma $R_b$:**

$$R_c' = G_p\cdot R_b = 1000\times19{,}2\text{k} = \boxed{19{,}2\ \text{Mchips/s}} \ \Rightarrow\ B' = 2R_c' = \boxed{38{,}4\ \text{MHz}}$$

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

| | Frecuencia |
|---|---|
| Dos **centrales** | $f_c \pm 488{,}28$ Hz $\ \left(=\pm\tfrac{\Delta f}{2}\right)$ |
| Dos **inferiores** | $f_c - 1{,}9995$ MHz y $f_c - 1{,}9985$ MHz |
| Dos **superiores** | $f_c + 1{,}9985$ MHz y $f_c + 1{,}9995$ MHz |

**d) Si la entrada fuera una sucesión continua de ceros**

Todas las subportadoras transmitirían el mismo símbolo fijo → el espectro deja de ser continuo y se vuelve **4096 deltas de Dirac separadas $976{,}56$ Hz**. (Sin variación de datos no hay ensanchamiento espectral: cada subportadora queda como un tono puro.)

**e) Valor adecuado de $f_c$ para transmitir centrado en 3,9 GHz**

$$f_c = 3{,}9\ \text{GHz} - 488{,}28\ \text{Hz}$$

Como las subportadoras están en $f_c\pm(k+\frac12)\Delta f$ y **ninguna cae en $f_c$**, hay que correr el oscilador media separación para que el conjunto quede centrado en 3,9 GHz.

**f) Tiempo de símbolo con una sola portadora en 1024-QAM**

$$\ell = \log_2 1024 = 10 \ \Rightarrow\ D = \frac{16\text{M}}{10} = 1{,}6\ \text{Mbaud} \ \Rightarrow\ T_{S1c} = \frac{1}{1{,}6\text{M}} = \boxed{0{,}625\ \mu\text{s}}$$

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
