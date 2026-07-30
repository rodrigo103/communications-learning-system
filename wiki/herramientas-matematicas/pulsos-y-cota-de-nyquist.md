---
tags:
  - wiki/herramientas-matematicas
  - wiki/planificacion
curso: Sistemas de Comunicaciones
unidad: 6
---

# Formas de pulso y la cota de Nyquist

> **Last verified:** 2026-07-29 | **Verified by:** analysis

> **Para qué es esta nota**: responde tres preguntas que se cruzan en los ejercicios de ancho de banda — *¿por qué el sinc es la cota teórica?*, *¿qué pulso se usa en la práctica?* y *¿por qué el enunciado distingue "mínimo ideal" de "nulo a nulo"?*
>
> Relacionado: [[../modulacion-pulsos/pcm-formulario-examen#Justificación del paso $R_s \to B_{min}$ (criterio de Nyquist sin ISI)|criterio de Nyquist sin ISI]] y [[../modulacion-digital/digital-formulario-examen#Los tres anchos de banda — no confundirlos|los tres anchos de banda]].

## Los tres pulsos, en una tabla

| Pulso | $B$ (banda base) | ¿Realizable? | Dónde se usa |
|---|---|---|---|
| **Sinc** (Nyquist ideal) | $\dfrac{R_s}{2}$ | ❌ **No** | Solo como **cota teórica** |
| **Rectangular** (NRZ) | $R_s$ (nulo a nulo) | ✅ Trivial | Banda base sobre cable, sistemas simples |
| **Coseno realzado** | $\dfrac{R_s}{2}(1+\alpha)$ | ✅ Sí (FIR digital) | **Todo sistema de radio real** |

---

## Por qué el sinc es la cota teórica

Son dos partes: el sinc **alcanza** $R_s/2$, y **nada puede bajar de ahí**.

### Parte 1 — el sinc lo alcanza

$\operatorname{sinc}(t/T_s)$ tiene espectro **rectangular** de ancho $1/T_s = R_s$ (de $-R_s/2$ a $+R_s/2$) → ancho de banda unilateral $R_s/2$. Y cumple ISI cero porque $p(kT_s)=0$ para todo $k\neq0$.

### Parte 2 — nada puede bajar de ahí *(el teorema)*

El **criterio de Nyquist** establece que ISI cero en los instantes de muestreo equivale a que el **espectro plegado sea constante**:

$$\sum_k P\!\left(f - \frac{k}{T_s}\right) = \text{constante}$$

O sea: las **réplicas del espectro, espaciadas $1/T_s = R_s$**, deben **cubrir todo el eje de frecuencias sin huecos**.

Cada réplica tiene ancho $2B$ (de $-B$ a $+B$). Para que réplicas espaciadas $R_s$ se toquen o solapen sin dejar huecos:

$$2B \geq R_s \quad\Longrightarrow\quad \boxed{B \geq \frac{R_s}{2}}$$

> **Si $B < R_s/2$**, las réplicas quedan **separadas**: hay bandas donde la suma vale cero, el espectro plegado no es constante, y la **ISI es inevitable**. No es que sea difícil — es imposible. [analysis]

### Por qué el sinc es el *único* que toca la cota

En la igualdad ($2B = R_s$ exacto) las réplicas encajan **borde a borde, sin solaparse**. Para que la suma sea constante en esa situación, cada réplica debe ser **exactamente un rectángulo plano** de ancho $R_s$ — cualquier otra forma dejaría ondulaciones en la suma.

Y la antitransformada de un rectángulo es el sinc:

$$\text{rectángulo en frecuencia} \ \xleftrightarrow{\ \mathcal F\ } \ \text{sinc en tiempo}$$

Por eso el sinc no es "una buena opción": es **la única** que alcanza el límite.

### Lectura complementaria: grados de libertad

Un canal real de ancho $B$ tiene **exactamente $2B$ grados de libertad por segundo**. No se pueden meter más de $2B$ símbolos independientes por segundo, y **el sinc es el pulso que usa exactamente todos sin desperdiciar ninguno.**

---

## ⚠️ Los DOS teoremas de Nyquist — no son el mismo

Se confunden constantemente porque comparten el nombre, el "2" y el hecho de fondo. Pero son **enunciados distintos**: [analysis]

| | **Teorema de muestreo** | **Criterio de señalización** (1er criterio de Nyquist) |
|---|---|---|
| **Enunciado** | $f_s \geq 2B$ | $R_s \leq 2B$ |
| **Sobre qué** | Convertir una señal continua en muestras | Transmitir símbolos discretos por un canal |
| **Dirección** | **Análisis**: señal → números | **Síntesis**: números → señal |
| **Unidad del "2"** | muestras/ciclo | símbolos/ciclo |
| **Dónde se usa** | PCM (frecuencia de muestreo) | Digital, PCM (ancho de banda mínimo) |

**Lo que comparten** — y la razón de que aparezca el mismo 2:

> **Un canal (o señal) real de ancho de banda $B$ tiene exactamente $2B$ grados de libertad por segundo.**
>
> - **Muestreo** dice: *hacen falta* $2B$ números por segundo para describir la señal
> - **Señalización** dice: se pueden *elegir libremente* $2B$ números por segundo para transmitir
>
> Mismo espacio de $2B$ dimensiones por segundo, leído en direcciones opuestas. **Son duales.**

> **Sobre el mnemónico "pico y valle"**: se suele decir que hacen falta 2 muestras por ciclo "para ver el pico y el valle". Sirve para recordar el número, pero **no es riguroso**: muestreando una sinusoide exactamente a 2 muestras/ciclo justo en los cruces por cero se obtienen **todos ceros** y se pierde la señal. Por eso el teorema estricto pide $f_s>2B$, no $\geq$. El argumento correcto es el de **aliasing / grados de libertad**, no el de los extremos. [analysis]

**Las tres apariciones del criterio de señalización en esta vault son el mismo teorema**, en distinto contexto:
- [[../modulacion-digital/digital-formulario-examen#Los tres anchos de banda — no confundirlos|Digital — los tres anchos de banda]] (con distintas formas de pulso)
- [[../modulacion-pulsos/pcm-formulario-examen#Justificación del paso $R_s \to B_{min}$ (criterio de Nyquist sin ISI)|PCM — justificación del paso $R_s\to B_{min}$]]
- Esta nota (la demostración de la cota)

Mientras que $f_s\geq2B$ (fórmula 1 del [[../modulacion-pulsos/pcm-formulario-examen|formulario de PCM]]) es **el otro teorema**.

---

## Por qué el sinc no se usa en la práctica

Tres problemas, y el tercero es el decisivo:

1. **Dura infinito** — se extiende de $-\infty$ a $+\infty$, o sea es **no causal**: habría que conocer el futuro
2. **Decae como $1/t$** — muy lento. Truncarlo es obligatorio, y lo que se corta genera ISI
3. **Sensibilidad extrema al jitter de temporización** ← *el que lo mata*. Como las colas decaen tan despacio, muestrear apenas corrido hace que **las colas de muchísimos símbolos contribuyan simultáneamente**, y la ISI acumulada puede ser enorme

## El pulso rectangular: el otro extremo

- **Trivial de generar**: una llave que conmuta un nivel
- Pero su espectro es una sinc, que **se desparrama**: primer lóbulo lateral a solo $-13{,}3$ dB → **interfiere a los canales vecinos**
- Su ancho nulo a nulo es $R_s$ en banda base ($2R_s$ pasabanda) — **el doble del mínimo de Nyquist**

Se usa en banda base sobre cable dedicado (sin vecinos a quién molestar) y en sistemas simples o de bajo costo.

## Coseno realzado: lo que se usa de verdad

$$\boxed{B = \frac{R_s}{2}(1+\alpha)\ \text{[banda base]}, \qquad B = R_s(1+\alpha)\ \text{[pasabanda]}}$$

con $\alpha\in[0,1]$ típicamente **0,2 a 0,35** en sistemas reales.

**El compromiso**: paga $\alpha$ de exceso de banda a cambio de que **las colas decaigan mucho más rápido** ($\sim1/t^3$ para $\alpha>0$), lo que lo vuelve tolerante al jitter y truncable sin drama.

### Cómo se genera concretamente

$$\text{símbolos} \to \boxed{\text{sobremuestreo}} \to \boxed{\text{FIR coseno realzado}} \to \boxed{\text{D/A}} \to \boxed{\text{filtro analógico}}$$

**No se "genera un sinc"** — se insertan ceros entre los símbolos y se **calcula numéricamente** la salida de un filtro FIR cuya respuesta al impulso es un coseno realzado truncado. Con DSP es trivial.

### Raíz de coseno realzado (RRC) — el detalle elegante

En la práctica el coseno realzado se **reparte mitad y mitad** entre transmisor y receptor: cada uno usa $\sqrt{H(f)}$.

$$\underbrace{\sqrt{H(f)}}_{\text{TX}} \times \underbrace{\sqrt{H(f)}}_{\text{RX}} = \underbrace{H(f)}_{\text{coseno realzado completo}}$$

**Ventaja doble**: la cascada da el coseno realzado completo (ISI cero) **y** el filtro del receptor queda siendo el **filtro acoplado** al del transmisor (BER óptima). Dos requisitos con un solo diseño.

---

## Para el examen

| Cuando el enunciado dice… | Usar | Pulso implícito |
|---|---|---|
| "ancho de banda mínimo **ideal**" | $R_s/2$ (BB) o $R_s$ (PB) | Sinc, $\alpha=0$ |
| "**nulo a nulo**" | $R_s$ (BB) o $2R_s$ (PB) | Rectangular |
| Da un **factor de roll-off $\alpha$** | $\frac{R_s}{2}(1+\alpha)$ o $R_s(1+\alpha)$ | Coseno realzado |

> ⚠️ **La tensión que aparece seguido**: el enunciado dice "pulsos rectangulares" y después pide "ancho de banda **mínimo**". Estrictamente son incompatibles — los rectangulares no alcanzan el mínimo. **Responder el mínimo (lo que preguntan) y aclarar en una línea** que la señal descrita, siendo rectangular, ocupa el doble. Así queda claro que se entiende la diferencia, independientemente de qué esperara el corrector. [analysis]

## Qué parte de cada fórmula es Nyquist (y qué parte no)

Las fórmulas de ancho de banda mezclan **tres ingredientes distintos**, y solo uno es el criterio de Nyquist. Separarlos evita confusiones: [analysis]

| Ingrediente | Qué es | ¿Es Nyquist? |
|---|---|---|
| **1. Cota de ISI cero** | $B\geq R_s/2$ en banda base | ✅ **Sí — esto es el criterio** |
| **2. Duplicación pasabanda** | $\times2$ al modular | ❌ No — es la **propiedad de modulación de Fourier** (espectro copiado a $\pm f_c$) |
| **3. Forma de pulso** | Cuánto exceso de banda se usa | ❌ No — es **elección de diseño** |

**Descomposición de cada caso:**

| Fórmula | Cota Nyquist | $\times2$ pasabanda | Forma de pulso |
|---|---|---|---|
| $B=R_s/2$ (BB, sinc) | ✅ **en la igualdad** | — | sinc, exceso 0 |
| $B=R_s$ (PB, sinc) | ✅ en la igualdad | ✅ | sinc |
| $B=\frac{R_s}{2}(1+\alpha)$ (BB, cos. realzado) | ✅ **satisfecho, no en la cota** | — | exceso $\alpha$ |
| $B=R_s$ (BB, nulo a nulo rect.) | ✅ satisfecho | — | rectangular, lóbulo en $R_s$ |
| $B=2R_s$ (PB, nulo a nulo rect.) | ✅ satisfecho | ✅ | rectangular |

### El pulso rectangular SÍ cumple Nyquist

Conviene aclararlo porque suele malinterpretarse: cada pulso rectangular está **confinado a su propia ranura**, así que $p(kT_s)=0$ para $k\neq0$ → **ISI cero**. Verificable también por espectro plegado, usando la identidad $\sum_k\operatorname{sinc}(x-k)=1$ (constante ✓).

**No viola el criterio — simplemente no lo alcanza con eficiencia**: su espectro se extiende infinitamente y el lóbulo principal ya ocupa el doble del mínimo.

### ⚠️ La trampa: $B = R_s$ significa dos cosas distintas

| $B=R_s$ significa… | Cuando… | Por qué |
|---|---|---|
| Mínimo de Nyquist **pasabanda** | pulso sinc, modulado | $\frac{R_s}{2}\times2$ |
| Nulo a nulo en **banda base** | pulso rectangular, sin modular | primer nulo en $1/T_s$ |

**Mismo número, dos orígenes sin relación entre sí.** Si un ejercicio da $R_s$ como ancho de banda, hay que identificar cuál de los dos es — y la pista está en si la señal es de banda base o pasabanda, y en qué pulso usa.

## Ver también

- [[../modulacion-digital/digital-formulario-examen|Modulación Digital — Formulario]] · [[../modulacion-pulsos/pcm-formulario-examen|PCM — Formulario]]
- [[teorema-muestreo|Teorema de Muestreo]] — los $2B$ grados de libertad
- [[../modulacion-analogica/modulacion-vsb|VSB]] — el mismo trade-off "filtro ideal irrealizable vs banda de transición"
- [[../modulacion-digital/probabilidad-error|Probabilidad de Error]] — el filtro acoplado que el RRC implementa
