---
tags:
  - wiki/herramientas-matematicas
  - wiki/planificacion
curso: Sistemas de Comunicaciones
---

# Nyquist explicado de cero

> **Last verified:** 2026-07-29 | **Verified by:** analysis

> **Por qué esta nota**: "Nyquist" aparece en el curso en cinco lugares distintos con fórmulas que parecen no tener relación ($f_s\geq2B$, $B=R_s/2$, $B=R_s$, $B=2R_s$, $B=\frac{R_s}{2}(1+\alpha)$). **Hay una sola idea de fondo.** Todo lo demás es contabilidad.

---

# 1. La única idea

> ## Un canal de ancho de banda $B$ puede transportar $2B$ números independientes por segundo.

Eso es todo. Nada más.

Pensalo como **casilleros**: el canal te ofrece $2B$ casilleros por segundo, y en cada uno podés escribir un número que elegís libremente. No hay forma de conseguir más casilleros sin agrandar $B$.

$$\boxed{\text{casilleros por segundo} = 2B}$$

**Ejemplo**: un canal de 1 kHz te da 2000 casilleros por segundo. Si querés mandar 3000 números por segundo, no entran. Punto.

---

# 2. ¿De dónde sale el "2"?

Esta es la parte que casi nunca se explica bien (y que yo antes te expliqué mal con el cuento del "pico y valle" — olvidate de eso).

Tomá una señal limitada a $B$ Hz, mirada durante un tiempo $T$. Se puede escribir como suma de senos y cosenos:

$$x(t) = \sum_{n} \Big[\underbrace{a_n}_{\text{coseno}}\cos\!\big(2\pi \tfrac{n}{T} t\big) + \underbrace{b_n}_{\text{seno}}\sin\!\big(2\pi \tfrac{n}{T}t\big)\Big]$$

Contemos cuántos números hacen falta para describirla:

| Cosa | Cuántas |
|---|---|
| Frecuencias posibles (de $1/T$ hasta $B$) | $B\,T$ |
| Números por frecuencia | **2** ($a_n$ y $b_n$) |
| **Total de números** | $2BT$ |

Dividiendo por el tiempo $T$:

$$\frac{2BT\ \text{números}}{T\ \text{segundos}} = 2B\ \frac{\text{números}}{\text{segundo}}$$

> **El "2" es porque cada frecuencia lleva DOS números**: cuánto coseno y cuánto seno. (Equivalentemente: una amplitud y una fase.) No es un 2 arbitrario ni una aproximación.

---

# 3. Los dos teoremas de Nyquist = la misma idea, dos direcciones

Acá está el origen de la confusión: **hay dos teoremas con el mismo nombre**, y son la misma idea leída al revés.

| | **Teorema de muestreo** | **Criterio de señalización** |
|---|---|---|
| **Pregunta** | Tengo una señal. ¿Cuántos números necesito para guardarla? | Quiero mandar números. ¿Cuántos me caben? |
| **Respuesta** | $2B$ por segundo | $2B$ por segundo |
| **Fórmula** | $f_s \geq 2B$ | $R_s \leq 2B$ |
| **Dirección** | Señal → números (**análisis**) | Números → señal (**síntesis**) |
| **Unidad del 2** | muestras/ciclo | símbolos/ciclo |
| **Dónde aparece** | PCM: frecuencia de muestreo | Digital y PCM: ancho de banda mínimo |

**Los dos dicen "$2B$ casilleros por segundo".** Uno dice "necesitás llenar todos para no perder nada"; el otro dice "no podés llenar más que esos".

> Son **duales**, no idénticos. Pero si entendés los casilleros, entendés los dos.

---

# 4. ¿Cómo se llenan los casilleros? — las formas de pulso

Ya sabés que tenés $2B$ casilleros por segundo. Ahora: **¿cuántos casilleros gasta cada símbolo que mandás?**

Ahí es donde entra la forma del pulso. Y la respuesta cambia según el pulso:

| Pulso | Casilleros por símbolo | $B$ necesario (banda base) |
|---|---|---|
| **Sinc** (ideal) | **1** — el mínimo posible | $B = \dfrac{R_s}{2}$ |
| **Coseno realzado** | $1+\alpha$ | $B = \dfrac{R_s}{2}(1+\alpha)$ |
| **Rectangular** (lóbulo principal) | **2** | $B = R_s$ |

**Verificación de la primera fila**: si cada símbolo gasta 1 casillero y hay $2B$ casilleros/s, entonces caben $R_s = 2B$ símbolos/s → $B = R_s/2$ ✓

**Y de la última**: si cada símbolo gasta 2 casilleros, caben $R_s = 2B/2 = B$ símbolos/s → $B = R_s$ ✓

> ⚠️ **Importante y contraintuitivo**: el pulso rectangular **no está haciendo nada ilegal**. Cumple perfectamente el criterio (no genera ISI: cada pulso vive en su propia ranura de tiempo). Simplemente **gasta el doble de casilleros de los necesarios** — es desprolijo, no incorrecto.
>
> Y el sinc gasta exactamente 1 casillero por símbolo, que es el mínimo teórico. Por eso es **la cota**: nadie puede gastar menos de un casillero por símbolo.

---

# 5. Banda base vs pasabanda: ¿por qué el $\times2$?

Otra fuente de confusión. La razón **no** es "el espectro se copia" (eso es una consecuencia, no la causa). La razón es:

> **En banda base los símbolos son números reales (1 casillero cada uno).**
> **En pasabanda los símbolos son números complejos: $I + jQ$, o sea DOS números (2 casilleros cada uno).**

| | Símbolo | Casilleros/símbolo | $B$ para $R_s$ símbolos/s |
|---|---|---|---|
| **Banda base** | real ($\pm V$) | 1 | $B = R_s/2$ |
| **Pasabanda** | complejo ($I+jQ$) | 2 | $B = R_s$ |

**Cuenta pasabanda**: $R_s$ símbolos complejos $\times$ 2 casilleros $= 2R_s$ casilleros/s. Y hay $2B$ casilleros/s disponibles → $2B = 2R_s$ → $\boxed{B = R_s}$ ✓

> **Chequeo con QPSK y BPSK** (los dos son pasabanda, los dos con $B=R_s$):
> - **QPSK** pone información en $I$ **y** en $Q$ → usa **todos** los casilleros → 2 bits/símbolo
> - **BPSK** pone información solo en $I$ ($Q=0$) → **desperdicia la mitad** → 1 bit/símbolo
>
> **Y eso explica de una vez por qué QPSK da el doble de bits en el mismo ancho de banda sin empeorar la BER**: no hace magia, simplemente usa casilleros que BPSK dejaba vacíos. [analysis]

---

# 6. "Nulo a nulo" no es Nyquist

Esta es otra cosa distinta, y mezclarla con lo anterior es la mitad del quilombo.

**Nyquist** responde: *¿cuántos símbolos caben?* → una **cota**.
**Nulo a nulo** responde: *¿hasta dónde se extiende el espectro de este pulso?* → una **medida de ocupación**.

Para un pulso rectangular de duración $T_s$, el espectro es una sinc cuyo **primer nulo** cae en:

$$f = \frac{1}{T_s} = R_s \quad\text{(banda base)}$$

Y como el lóbulo principal es simétrico, en pasabanda ocupa $2R_s$.

> **No es un mínimo de nada** — es simplemente dónde el espectro de ese pulso particular cruza cero por primera vez. Se usa como medida práctica porque **el lóbulo principal concentra ~90% de la potencia**.

## ⚠️ La trampa que más confunde

$B = R_s$ aparece **dos veces, por razones sin ninguna relación**:

| $B=R_s$ | ¿De dónde sale? |
|---|---|
| Mínimo de Nyquist **pasabanda** | $\frac{R_s}{2}\times2$ (símbolos complejos) |
| Nulo a nulo en **banda base** | primer nulo de la sinc, en $1/T_s$ |

**Cómo distinguirlas en un ejercicio**: fijate si la señal es de banda base o pasabanda, y qué pulso usa.

---

# 7. La contabilidad de unidades (el $\kappa$)

Todas estas fórmulas convierten **una tasa** (símbolos/s, muestras/s) en **un ancho de banda** (Hz = ciclos/s). Y toda conversión así tiene la forma:

$$\boxed{B\left[\tfrac{\text{ciclos}}{\text{s}}\right] = \underbrace{\kappa\left[\tfrac{\text{ciclos}}{\text{símbolo}}\right]}_{\text{factor de conversión}} \times \underbrace{R_s\left[\tfrac{\text{símbolos}}{\text{s}}\right]}_{\text{tasa}}}$$

Los "símbolos" se cancelan y queda Hz. **El $\kappa$ es lo único que cambia entre fórmulas:**

| Fórmula | $\kappa$ | Se descompone en… |
|---|---|---|
| $B=R_s/2$ (BB, sinc) | $\tfrac12$ | 1 casillero/símbolo, y 2 casilleros por ciclo |
| $B=R_s$ (PB, sinc) | $1$ | 2 casilleros/símbolo (complejo), 2 por ciclo |
| $B=\tfrac{R_s}{2}(1+\alpha)$ (BB, cos. realz.) | $\tfrac{1+\alpha}{2}$ | $(1+\alpha)$ casilleros/símbolo |
| $B=R_s$ (BB, nulo a nulo) | $1$ | *no es casilleros — es dónde cae el nulo* |
| $B=2R_s$ (PB, nulo a nulo) | $2$ | nulo $\times$ 2 lados del lóbulo |
| $f_s=2B$ (muestreo) | $\kappa^{-1}=2$ | 2 muestras/ciclo *(dirección inversa)* |

> **Casi siempre $\kappa$ vale 1 y por eso es invisible** — pero está, y saber que está evita creer que "baudios = Hz". **No son la misma magnitud**: los baudios cuentan símbolos por segundo, los Hz miden un ancho del eje de frecuencias. Que a veces den el mismo número es una coincidencia de la conversión, no una identidad.

---

# 8. Resumen: la tabla que hay que tener

**La idea:** $2B$ casilleros por segundo. Todo lo demás es cuántos casilleros gasta cada cosa.

| Situación | Fórmula | Casilleros/símbolo |
|---|---|---|
| Muestreo de una señal | $f_s\geq2B$ | *(dirección inversa)* |
| **Mínimo ideal**, banda base | $B=\dfrac{R_s}{2}$ | 1 (sinc) |
| **Mínimo ideal**, pasabanda | $B=R_s$ | 2 (complejo) |
| **Con roll-off $\alpha$**, banda base | $B=\dfrac{R_s}{2}(1+\alpha)$ | $1+\alpha$ |
| **Con roll-off $\alpha$**, pasabanda | $B=R_s(1+\alpha)$ | $2(1+\alpha)$ |
| **Nulo a nulo**, banda base | $B=R_s$ | *(no aplica — es ocupación)* |
| **Nulo a nulo**, pasabanda | $B=2R_s$ | *(no aplica)* |

## Cómo saber cuál usar en el examen

| Si el enunciado dice… | Usar |
|---|---|
| "ancho de banda mínimo **ideal**" | el del sinc ($\alpha=0$) |
| "**nulo a nulo**" | el del rectangular |
| Da un **$\alpha$** | el del coseno realzado |
| No aclara, y la señal es **modulada** | pasabanda |
| No aclara, y **no hay portadora** | banda base |

## Ver también

- [[pulsos-y-cota-de-nyquist|Pulsos y la cota de Nyquist]] — la demostración formal de por qué el sinc es la cota (espectro plegado)
- [[teorema-muestreo|Teorema de Muestreo]] — el otro teorema
- [[../modulacion-digital/digital-formulario-examen|Digital — Formulario]] · [[../modulacion-pulsos/pcm-formulario-examen|PCM — Formulario]]
