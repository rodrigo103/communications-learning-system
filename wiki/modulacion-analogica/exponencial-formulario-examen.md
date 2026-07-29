---
tags:
  - wiki/modulacion-analogica
  - wiki/planificacion
curso: Sistemas de Comunicaciones
unidad: 4
---

# Modulación Exponencial (FM / PM) — Formulario de examen

> **Last verified:** 2026-07-29 | **Verified by:** analysis + patrón real de ejercicios en `exercises/finales/md/`

> **61,9% de los 42 finales únicos** — empatado con Modulación Lineal. Conceptual completo en [[../derivaciones/modulacion-fm-carson|Derivación de FM y Carson]].

## Glosario

| Símbolo | Nombre | Unidad |
|---|---|---|
| $A_c$ | Amplitud de portadora | V |
| $f_c$ | Frecuencia de portadora | Hz |
| $f_m$ | Frecuencia de la moduladora | Hz |
| $A_m$ | Amplitud de la moduladora | V |
| $\Delta f$ | **Desviación máxima de frecuencia** | Hz |
| $\Delta\phi$ | **Desviación máxima de fase** | rad |
| $\beta$ | **Índice de modulación** | adimensional |
| $k_f$ | Sensibilidad de frecuencia | Hz/V |
| $k_p$ | Sensibilidad de fase | rad/V |
| $B_T$ | Ancho de banda de transmisión | Hz |
| $n$ | Factor de un multiplicador de frecuencia | conteo |

## Las fórmulas

$$\boxed{s_{FM}(t) = A_c\cos\big(2\pi f_ct + \beta\sin(2\pi f_mt)\big)}$$

| # | Fórmula | Notas |
|---|---|---|
| 1 | $\boxed{f_i(t) = f_c + \Delta f\cos(2\pi f_mt)}$ | Frecuencia instantánea $=\frac{1}{2\pi}\frac{d\phi}{dt}$ |
| 2 | $\boxed{\Delta f = k_fA_m = \beta f_m}$ | Desviación máxima |
| 3 | $\boxed{\beta = \dfrac{\Delta f}{f_m}}$ | Índice de modulación |
| 4 | $\boxed{B_T = 2(\Delta f + f_m) = 2f_m(\beta+1)}$ | **Regla de Carson** (~98% de la potencia) |
| 5 | $\boxed{P = \dfrac{A_c^2}{2R}}$ | **Constante — no depende de la modulación** |

> ⚠️ **La trampa #1 del tema**: en FM la **potencia no cambia** al modular. Amplitud constante siempre. Distinto de AM, donde modular sube la potencia total.

## FM vs PM — qué queda invariante en cada una

Es la razón de que los finales pidan **$\Delta f$ y $\Delta\phi$ por separado** (aparecen 4-6 veces cada uno):

| | FM | PM |
|---|---|---|
| Lo que es proporcional a $A_m$ | $\Delta f = k_fA_m$ | $\Delta\phi = k_pA_m$ |
| Índice | $\beta = \dfrac{k_fA_m}{f_m}$ | $\beta = \Delta\phi = k_pA_m$ |
| Si **se duplica $f_m$** (con $A_m$ fijo) | $\Delta f$ **igual**, $\beta$ a la mitad | $\Delta\phi$ **igual**, $\Delta f$ **se duplica** |
| Si **se duplica $A_m$** | $\Delta f$ y $\beta$ se duplican | $\Delta\phi$ y $\beta$ se duplican |

> 📌 **Pregunta frecuente** (aparece 5 veces): *"cuando se duplica la frecuencia del tono modulante manteniendo invariable su amplitud, a la salida del modulador se observa…"* — la respuesta depende de si es FM o PM. **En FM $\beta$ cae a la mitad; en PM $\beta$ no cambia** (y por eso $\Delta f$ se duplica).

## Clasificación

| Tipo | Condición | $B_T$ aproximado |
|---|---|---|
| **NBFM** | $\beta < 0{,}3$ | $\approx 2f_m$ (como AM) |
| **WBFM** | $\beta > 1$ | $\approx 2\Delta f$ |

## Multiplicadores y mezcladores — el patrón más testeado

| Bloque | $f_c$ | $\Delta f$ | $\beta$ | $f_m$ | Amplitud |
|---|---|---|---|---|---|
| **Multiplicador $\times n$** | $nf_c$ | $n\Delta f$ | $n\beta$ | **igual** | igual* |
| **Mezclador** (OL $f_{OL}$) | $f_c\pm f_{OL}$ | **igual** | **igual** | igual | igual |

\* *el limitador posterior la normaliza; los enunciados lo aclaran*

> **Por qué**: el multiplicador **multiplica la fase entera**, $n\phi(t) = 2\pi(nf_c)t + n\beta\sin(2\pi f_mt)$ — $\beta$ es coeficiente **afuera** del seno (escala), $f_m$ vive **adentro del argumento** (no se toca). El mezclador suma una fase **sin modulación** ($2\pi f_{OL}t$), así que solo mueve la portadora. Derivación completa en [[../derivaciones/modulacion-fm-carson#Multiplicadores y mezcladores de frecuencia (el patrón más testeado)|Derivación de FM]].

> **Por eso Armstrong usa los dos**: multiplicadores para **subir $\beta$** (de NBFM a WBFM) y mezcladores para **ubicar la portadora final** sin arruinar el $\beta$ conseguido. Ver [[modulador-armstrong|Modulador Armstrong]].

## Diseño de un modulador Armstrong (procedimiento)

Es el ejercicio típico: dan los parámetros de **entrada** (etapa NBFM) y de **salida** (transmisor), y piden los factores de multiplicación y el oscilador local.

$$\text{NBFM}(f_1,\Delta f_1) \to \boxed{\times n_1} \to \boxed{\text{Mezclador } f_{OL}} \to \boxed{\times n_2} \to \text{salida}(f_c,\Delta f)$$

**Paso 1 — La multiplicación total la fija la desviación** (el mezclador no la toca):

$$\boxed{n_{total} = n_1 n_2 = \frac{\Delta f_{salida}}{\Delta f_{NBFM}}}$$

**Paso 2 — La portadora no cierra sola.** Si multiplicaras todo sin mezclar, quedaría $n_{total}\cdot f_1$, que **no** coincide con $f_c$ pedida. El mezclador corrige esa diferencia.

**Paso 3 — Despejar $f_{OL}$** según dónde esté el mezclador. Con la estructura $\times n_1 \to$ mezclador $\to \times n_2$:

$$f_c = n_2\big(n_1f_1 \pm f_{OL}\big) \quad\Longrightarrow\quad \boxed{f_{OL} = \left|\frac{f_c}{n_2} - n_1f_1\right|}$$

> **El grado de libertad**: $n_1$ y $n_2$ solo deben cumplir $n_1n_2 = n_{total}$; el reparto lo elegís vos (por eso hay varias soluciones válidas). Conviene elegir factores que se armen con duplicadores/triplicadores en cascada, y que dejen $f_{OL}$ en un valor razonable. **Justificá la elección por escrito.**

**Ancho de banda en cada etapa:**

| Punto | $BW$ |
|---|---|
| Salida del **NBFM** | $\approx 2f_m$ (banda angosta, $\beta\ll1$) |
| **Transmisión** (salida final) | Carson: $2(\Delta f + f_m)$ |

⚠️ **Si la modulante es una banda** (ej. "de 30 Hz a 15 kHz"), usar $f_m = f_{m,max}$ — la componente más alta.

## Espectro (Bessel) y SNR

$$s_{FM}(t) = A_c\sum_{n=-\infty}^{\infty}J_n(\beta)\cos\big[2\pi(f_c+nf_m)t\big]$$

**Infinitas bandas laterales** (a diferencia de AM que tiene 2), con amplitudes $J_n(\beta)$ que decaen. Conservación de potencia: $\sum J_n^2(\beta)=1$.

**SNR a la salida del discriminador:**

$$\boxed{\left(\frac{S}{N}\right)_D = 3\beta^2(\beta+1)\,\gamma}, \qquad \gamma = \frac{S_R}{N_0W}$$

**El trade-off de FM**: la mejora va con $\beta^2$ pero el ancho de banda con $(\beta+1)$ — **se compra SNR gastando espectro**, cuadrático a favor contra lineal en contra. Por eso FM broadcast usa $\beta=5$ y no más. Ver [[../ruido/ruido-formulario-examen#SNR en modulaciones analógicas — la referencia $\gamma$|Ruido — la referencia $\gamma$]].

## Los errores que cuestan puntos

1. **Creer que la potencia cambia al modular** — en FM es constante, $P=A_c^2/2R$
2. **Multiplicar $f_m$ por $n$ en un multiplicador** — $f_m$ **no** cambia; sí $f_c$, $\Delta f$ y $\beta$
3. **Confundir multiplicador con mezclador** — el mezclador **no** toca $\Delta f$ ni $\beta$
4. **Aplicar Carson con $\Delta f$ en vez de $\beta$ o viceversa** — usar $2(\Delta f+f_m)$, que es equivalente a $2f_m(\beta+1)$
5. **En PM, olvidar que $\Delta f$ depende de $f_m$** — $\Delta f = k_pA_mf_m$, a diferencia de FM

## Ver también

- [[../derivaciones/modulacion-fm-carson|Derivación de FM y Regla de Carson]] — con multiplicadores, mezcladores e implementación física
- [[fm-vs-pm|FM vs PM]] · [[fm-banda-angosta|NBFM vs WBFM]] · [[modulador-armstrong|Modulador Armstrong]]
- [[../../outputs/solutions/FM_multiplicador_F_Comu_2023-02-16|Ejercicio resuelto — FM con cuadruplicador]]
- [[lineal-formulario-examen|Formulario de Modulación Lineal]] — el otro 61,9%
