# Solución — Modulación Digital: diseño sobre canal telefónico

**Origen del enunciado:** `exercises/finales/md/F_Comu_2019-02-25.md`, Ejercicio 4 (Modulación digital, 2,5 puntos). El mismo enunciado aparece también en `F_Comu_2019-05-24.md` — **patrón repetido en el corpus**.
**Resuelto:** 2026-07-28, por Rodrigo — segundo ejercicio cronometrado del plan.
**Tiempo: 17:29** (límite 30 min) — buena velocidad; lo que faltó fue conocimiento puntual, no tiempo.
**Resultado: a) ✓ · b) no resuelto · c) ✓ · d) ✓ parcial · e) parcial**

> **Nota metodológica**: este ejercicio va **al revés** de los típicos — no dan la modulación para calcular el ancho de banda, dan el canal y hay que **elegir** la modulación. Es más exigente conceptualmente.

---

## Enunciado

Dado un canal limitado en una banda de **300 a 3300 Hz**, se desea establecer una transmisión **simplex** a una tasa de **2400 símbolos/s**, con el objetivo de lograr una tasa de información de **9600 b/s**.

a) Seleccionar la modulación QAM apropiada. [0,25 pts]
b) Seleccionar la frecuencia de portadora y el factor de roll-off del filtro coseno elevado que permita utilizar la banda completa del canal. [0,75 pts]
c) Ídem con transmisión **half-duplex**; responder a) y b). [0,5 pts]
d) Ídem con transmisión **full-duplex**; responder a) y b). [0,5 pts]
e) Comparando **16QAM versus 16PSK a igualdad de amplitud máxima**, ¿cuál es más resistente a ruido (AWGN)? Justificar. [0,5 pts]

---

## Resolución

### Datos de partida

$$B_{canal} = 3300 - 300 = 3000\text{ Hz}, \qquad D = 2400\text{ baudios}, \qquad R_b = 9600\text{ bps}$$

### a) Modulación QAM apropiada

$$\ell = \frac{R_b}{D} = \frac{9600}{2400} = 4\ \frac{\text{bits}}{\text{símbolo}} \ \Rightarrow\ M = 2^\ell = 2^4 = \boxed{16\text{-QAM}}$$

### b) Portadora y factor de roll-off

**Roll-off** — se iguala el ancho de banda ocupado (pasabanda, coseno realzado) al disponible:

$$B = D(1+\alpha) \ \Rightarrow\ 3000 = 2400\,(1+\alpha) \ \Rightarrow\ 1+\alpha = 1{,}25 \ \Rightarrow\ \boxed{\alpha = 0{,}25}$$

**Portadora** — al **centro del canal**, porque el espectro pasabanda es simétrico respecto de $f_c$ y así entra completo:

$$f_c = \frac{300+3300}{2} = \boxed{1800\text{ Hz}}$$

> **Este fue el ítem no resuelto.** Es mecánico una vez que se ve el planteo: *"usar la banda completa"* → igualar $D(1+\alpha)$ al ancho disponible y despejar $\alpha$; la portadora al medio por simetría. Ver [[../../wiki/modulacion-digital/digital-formulario-examen#Los tres anchos de banda — no confundirlos|los tres anchos de banda]].

### c) Half-duplex — **igual que simplex**

$$\boxed{\text{16-QAM}, \quad \alpha = 0{,}25, \quad f_c = 1800\text{ Hz}}$$

**Half-duplex significa que ambos sentidos comparten el canal alternando en el tiempo**, no simultáneamente. Cuando a un extremo le toca transmitir, dispone del canal **completo** (3000 Hz). Por eso no cambia nada respecto de simplex.

*(Punto que se falla seguido: se tiende a suponer que "dos sentidos" implica dividir la banda, y eso solo pasa en full-duplex.)*

### d) Full-duplex — **acá sí se divide la banda**

Full-duplex = ambos sentidos **simultáneos**, así que se divide el canal en frecuencia:

$$B_{sentido} = \frac{3000}{2} = 1500\text{ Hz cada uno}$$

Manteniendo $\alpha = 0{,}25$:

$$D = \frac{B_{sentido}}{1+\alpha} = \frac{1500}{1{,}25} = 1200\text{ baudios}$$

$$\ell = \frac{R_b}{D} = \frac{9600}{1200} = 8 \ \Rightarrow\ M = 2^8 = \boxed{256\text{-QAM}}$$

**Portadoras** — una por sub-banda, cada una en su centro:

$$\text{Sub-banda 1: } 300\text{–}1800\text{ Hz} \Rightarrow f_{c1} = \boxed{1050\text{ Hz}}$$
$$\text{Sub-banda 2: } 1800\text{–}3300\text{ Hz} \Rightarrow f_{c2} = \boxed{2550\text{ Hz}}$$

> **Por qué $\ell=8$ y no otro**: la restricción es $B=D(1+\alpha)=1500$ con $0\le\alpha\le1$, o sea $D\in[750,1500]$, lo que da $\ell = 9600/D \in [6{,}4;\ 12{,}8]$. Los valores válidos para QAM cuadrada (ℓ par) son 8, 10 y 12 → $M=256$, $1024$, $4096$. **Se elige el menor ($M=256$)** porque a menor $M$, mayor distancia entre puntos de constelación y mejor inmunidad al ruido. Además deja $\alpha=0{,}25$, el mismo filtro de los ítems anteriores.

**Resumen de los tres modos** — la tabla que sintetiza el ejercicio:

| Modo | Cómo comparte el canal | BW por sentido | Modulación | $f_c$ |
|---|---|---|---|---|
| **Simplex** | Un solo sentido | 3000 Hz | 16-QAM | 1800 Hz |
| **Half-duplex** | Alterna en el tiempo | 3000 Hz (por turnos) | **16-QAM** (igual) | 1800 Hz |
| **Full-duplex** | Divide en frecuencia | 1500 Hz | **256-QAM** | 1050 y 2550 Hz |

### e) 16-QAM vs 16-PSK a igual amplitud máxima

**Lo que decide la resistencia al ruido AWGN no es la potencia sino la distancia mínima $d_{min}$** entre puntos de constelación — un error ocurre cuando el ruido empuja el símbolo recibido más allá de la mitad de camino hacia un vecino.

**16-PSK**: los 16 puntos sobre una circunferencia de radio $A$ (la amplitud máxima), separados $2\pi/16$:

$$d_{min}^{PSK} = 2A\sin\frac{\pi}{16} = 2A(0{,}1951) = 0{,}390\,A$$

**16-QAM**: grilla 4×4 con niveles $\pm a,\pm3a$. La amplitud máxima es la esquina, $3a\sqrt2 = A$, de donde $a = A/(3\sqrt2) = 0{,}236A$:

$$d_{min}^{QAM} = 2a = 0{,}471\,A$$

**Comparación:**

$$\frac{d_{min}^{QAM}}{d_{min}^{PSK}} = \frac{0{,}471}{0{,}390} = 1{,}21 \qquad (\approx 1{,}7\text{ dB de ventaja})$$

$$\boxed{\text{16-QAM es más resistente al ruido}}$$

**Razón intuitiva**: PSK desperdicia el plano I/Q poniendo todos los puntos sobre una circunferencia, mientras QAM los distribuye por toda el área disponible. Para el mismo radio máximo, los puntos de QAM quedan más separados.

> **La duda que apareció al resolver — potencia de PSK**: para $M$-PSK, $\langle\lvert s\rvert^2\rangle = A^2$ (todos los símbolos están a la misma distancia del origen, así que el promedio es trivial), y la potencia media es $S = A^2/2$. Contrasta con QAM cuadrada, donde $\langle\lvert s\rvert^2\rangle = \frac{2(M-1)}{3}a^2$ porque los puntos tienen magnitudes distintas. Ver la tabla en [[../../wiki/modulacion-digital/digital-formulario-examen#Cadena de fórmulas|el formulario de Digital]].
>
### Comparando las potencias medias: de dónde sale el factor 1,8

Con $A = 3a\sqrt2$ (igual amplitud máxima), o sea $A^2 = 18a^2$:

$$\frac{\langle\lvert s\rvert^2\rangle_{PSK}}{\langle\lvert s\rvert^2\rangle_{QAM}} = \frac{18a^2}{10a^2} = 1{,}8$$

**Ese 1,8 es la relación pico-a-promedio de potencia (PAPR) de la constelación 16-QAM.** No es coincidencia que aparezca acá: como PSK tiene envolvente constante (su promedio *es* su pico), compararlas a igual pico equivale a comparar el promedio de PSK contra el promedio de QAM — y eso da exactamente el PAPR de QAM.

$$\text{PAPR}_{16\text{-QAM}} = \frac{\lvert s\rvert^2_{max}}{\langle\lvert s\rvert^2\rangle} = \frac{18a^2}{10a^2} = 1{,}8 \quad (2{,}55\text{ dB})$$

**Significado práctico — dimensionamiento del amplificador**: el amplificador se dimensiona por el **pico** pero entrega útilmente el **promedio**. Con PAPR 1,8 hace falta un amplificador capaz de $18a^2$ para transmitir solo $10a^2$ medios: **2,55 dB de back-off desperdiciado**. PSK tiene PAPR $=1$ (0 dB) y puede trabajar saturado.

### La comparación a igual amplitud máxima subestima a QAM

| Criterio | $d_{min}$ QAM | $d_{min}$ PSK | Ventaja QAM |
|---|---|---|---|
| **Igual amplitud máxima** (lo que pide el enunciado) | $0{,}471A$ | $0{,}390A$ | $1{,}21\times$ → **1,7 dB** |
| **Igual potencia media** (comparación justa) | $0{,}632\sqrt P$ | $0{,}390\sqrt P$ | $1{,}62\times$ → **4,2 dB** |

A igual amplitud máxima QAM gana en $d_{min}$ **y además usa 44% menos potencia media** — gana por partida doble. Igualando potencia media (que es lo que realmente cuesta), la ventaja sube a ~4 dB, que es el número que suele citar la bibliografía para 16-QAM vs 16-PSK.

### ¿En qué es mejor 16-PSK entonces?

QAM gana en inmunidad al ruido, pero PSK tiene ventajas reales — todas derivadas de la **envolvente constante**:

| Aspecto | Por qué gana PSK |
|---|---|
| **Eficiencia del amplificador** | PAPR $=1$ → el HPA trabaja **saturado**, en su punto de máxima eficiencia (~60-70% vs ~30% con back-off). Decisivo cuando la energía es el recurso escaso: satélites, equipos a batería |
| **Tolerancia a no linealidad** | Al no llevar información en la amplitud, la compresión/distorsión del amplificador **no destruye datos**. QAM sí se degrada: la no linealidad deforma la grilla de amplitudes |
| **Recuperación de portadora y sincronismo** | Con envolvente constante el lazo de portadora es más simple y robusto |
| **Detección diferencial** | DPSK permite demodular **sin recuperar portadora** (con ~3 dB de penalidad). QAM no tiene equivalente práctico — necesita referencia de amplitud sí o sí |
| **AGC en el receptor** | No hace falta control de ganancia preciso: la amplitud no lleva información |

**El resumen del trade-off**: QAM invierte el plano I/Q completo para maximizar $d_{min}$ por unidad de potencia media, pero exige un **amplificador lineal con headroom**. PSK sacrifica $d_{min}$ a cambio de **poder saturar el amplificador**. Cuál conviene depende de si el cuello de botella es el ancho de banda (→ QAM) o la potencia disponible (→ PSK).

Por eso: **satélites y espacio profundo → PSK**; **cable, WiFi, DVB-C, LTE → QAM**.

---

## Qué aprender de este ejercicio

1. **El ejercicio va al revés**: dan canal y tasas, piden elegir modulación. La cadena es $\ell = R_b/D \to M=2^\ell$.
2. **$B=D(1+\alpha)$ despejando $\alpha$** — el ítem que faltó. "Usar la banda completa" significa igualar el ancho ocupado al disponible.
3. **Portadora al centro** de la banda (o de cada sub-banda), por simetría del espectro pasabanda.
4. **Simplex / half-duplex / full-duplex**: solo el último divide la banda. Half-duplex alterna en el tiempo y usa el canal completo.
5. **$d_{min}$, no la potencia**, decide la inmunidad al ruido a igualdad de amplitud máxima.

## Ver también

- [[../../wiki/modulacion-digital/digital-formulario-examen|Modulación Digital — Formulario de examen]]
- [[../../wiki/modulacion-digital/constelaciones|Constelaciones]]
- [[../../wiki/modulacion-digital/eficiencia-espectral|Eficiencia Espectral]]
- [[../../wiki/modulacion-pulsos/pcm-formulario-examen|PCM — Formulario de examen]] — la etapa previa de la cadena
