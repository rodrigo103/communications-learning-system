---
tags:
  - wiki/ruido
  - wiki/planificacion
curso: Sistemas de Comunicaciones
unidad: 7
---

# Ruido — Formulario de examen (compacto)

> **Last verified:** 2026-07-28 | **Verified by:** analysis + patrón real de ejercicios en `exercises/finales/md/`

> **Para qué es esta nota**: versión operativa para resolver bajo reloj. Explicación conceptual en [[ruido-termico|Ruido Térmico]], [[temperatura-ruido|Temperatura de Ruido]] y [[formula-friis|Fórmula de Friis]].
>
> **Ruido aparece en 52,4% de los 42 finales únicos.** El patrón dominante es la **cascada de repetidores**.

## Glosario de símbolos

| Símbolo | Nombre | Unidad | Notas |
|---|---|---|---|
| $S$ | Potencia de **señal** | W | |
| $N$ | Potencia de **ruido** | W | |
| $N_0$ | **Densidad** espectral de ruido | W/Hz | Potencia de ruido *por Hz*. Dimensionalmente es energía (J) |
| $S/N$ | Relación señal a ruido (SNR) | adimensional | Se expresa en dB: $10\log_{10}(S/N)$ |
| $(S/N)_D$ | SNR en el **destino** (salida del sistema) | adimensional | Notación de los enunciados |
| $k$ | Constante de **Boltzmann** | J/K | $1{,}38\times10^{-23}$ |
| $T$ | Temperatura absoluta | K | |
| $T_0$ | Temperatura de **referencia** | K | $290$ K por convención |
| $T_e$ | Temperatura **equivalente de ruido** | K | Ruido propio de un dispositivo, expresado como temperatura |
| $B$ | Ancho de banda | Hz | $B_N$ = ancho equivalente **de ruido** |
| $F$ | **Factor de ruido** | adimensional, $\geq1$ | Cuánto degrada la SNR un dispositivo. En dB se llama **cifra de ruido** |
| $F_i$ | Factor de ruido de la **etapa $i$** | adimensional | $F_1$ = primera etapa, etc. |
| $F_T$ | Factor de ruido **total** de la cascada | adimensional | La "T" es de *total* |

> ⚠️ **"Factor de ruido" ≠ "cifra de ruido" — y la cátedra respeta la distinción con total consistencia** (verificado sobre el corpus): [analysis]
>
> | Término | Cómo aparece en los finales | Unidad |
> |---|---|---|
> | **"factor de ruido"** | "factor de ruido 4", "factor de ruido igual a uno ($F=1$)", "factor de ruido total de 40" | **siempre lineal** |
> | **"cifra de ruido"** | "cifra de ruido de **6 dB**" (7 apariciones) | **siempre en dB** |
> | "figura de ruido" | **cero apariciones** (es traducción del inglés *noise figure*) | — |
>
> $$\text{factor de ruido} = F\ \text{(lineal)}, \qquad \text{cifra de ruido} = 10\log_{10}F\ \text{[dB]}$$
>
> **El vocabulario del enunciado te dice las unidades** — información gratis al leer. Si dice "factor de ruido 4" es $F=4$ lineal (equivalente a 6 dB de cifra); si dijera "cifra de ruido de 4 dB" sería $F=2{,}51$.
| $G$ | **Ganancia** de potencia | adimensional, lineal | $G>1$ amplifica, $G<1$ atenúa |
| $G_i$ | Ganancia de la **etapa $i$** | adimensional | |
| $L$ | **Pérdida** (atenuación) | adimensional, $\geq1$ | $L = 1/G$. En un cable, $L$ es cuánto atenúa |
| $L_c$ | Pérdida de **un tramo de cable** | adimensional | Un solo tramo entre repetidores |
| $L_{TOTAL}$ | Pérdida **de todo el enlace** | adimensional | Se reparte entre los tramos |
| $n$ | **Cantidad de secciones** de repetición | conteo | *(ver aviso abajo)* |

> ⚠️ **Ojo con dos colisiones de notación:**
> - **$N$ vs $n$**: $N$ (mayúscula) es **potencia de ruido**; $n$ (minúscula) es **cantidad de secciones**. Los enunciados a veces usan $N$ para las secciones — leer por contexto.
> - **$F$ y $L$ y $G$ son adimensionales pero casi siempre se dan en dB en el enunciado.** Friis **solo funciona en lineal**: hay que convertir antes de aplicarla ($X = 10^{X_{dB}/10}$) y recién pasar el resultado a dB. Es el error #3 de la lista del final de esta nota. [analysis]

## Las 6 fórmulas

| # | Nombre | Fórmula | Notas |
|---|---|---|---|
| 1 | **Ruido térmico** | $\boxed{N = kTB}$ | $k=1{,}38\times10^{-23}$ J/K. También $N_0 = kT$ [W/Hz] |
| 2 | **Figura (cifra) de ruido** | $\boxed{F = \dfrac{(S/N)_{in}}{(S/N)_{out}}}$ | Cuánto **degrada** la SNR. Adimensional, $F\geq1$. En dB: $F_{dB}=10\log_{10}F$ |
| 3 | **Temperatura equivalente** | $\boxed{T_e = (F-1)\,T_0}$ | $T_0 = 290$ K (referencia estándar). Inversa: $F = 1+\dfrac{T_e}{T_0}$ |
| 4 | **Friis (cascada)** | $\boxed{F_T = F_1 + \dfrac{F_2-1}{G_1} + \dfrac{F_3-1}{G_1G_2}+\cdots}$ | **La primera etapa domina** — por eso el LNA va primero |
| 5 | **Friis en temperatura** | $\boxed{T_e = T_1 + \dfrac{T_2}{G_1} + \dfrac{T_3}{G_1G_2}+\cdots}$ | Equivalente a 4; a veces más cómoda |
| 6 | **Elemento pasivo** (cable, atenuador) | $\boxed{F = L, \quad G = 1/L}$ | La **pérdida es igual a la figura de ruido**. Clave para los ejercicios de repetidores |

### De dónde sale $T_e = (F-1)T_0$ (deducción de la fórmula 3)

La fórmula 3 no es una definición arbitraria — sale de aplicar $N=kTB$ dos veces. [analysis]

**Paso 1 — ruido total referido a la entrada.** Son dos aportes: el ruido que trae la fuente ($kT_0B$) más el ruido propio del dispositivo, expresado como si viniera de una fuente a temperatura $T_{eq}$ ($kT_{eq}B$):

$$N_{i,total} = kT_0B + kT_{eq}B = kB\,(T_0+T_{eq})$$

**Paso 2 — ruido a la salida.** Todo lo anterior amplificado por $G$:

$$N_o = G\,N_{i,total} = G\,kB\,(T_0+T_{eq})$$

**Paso 3 — aplicar la definición de factor de ruido:**

$$F = \frac{N_o}{N_i\,G} = \frac{G\,kB\,(T_0+T_{eq})}{kT_0B\cdot G} = \frac{T_0+T_{eq}}{T_0} = \boxed{1+\frac{T_{eq}}{T_0}}$$

que es exactamente $T_e = (F-1)T_0$ despejada al revés. **El $kB$ y el $G$ se cancelan** — por eso $F$ no depende ni del ancho de banda ni de la ganancia, solo de la relación entre el ruido propio del dispositivo y el de referencia.

> **Las dos definiciones equivalentes de $F$** (conviene conocer ambas, según qué datos den):
> $$F = \frac{(S/N)_{in}}{(S/N)_{out}} \qquad\Longleftrightarrow\qquad F = \frac{N_o}{N_i\,G}$$
> Son lo mismo: $\frac{S_i/N_i}{S_o/N_o} = \frac{S_iN_o}{N_iS_o} \overset{S_o=GS_i}{=} \frac{N_o}{N_iG}$. La primera se lee *"cuánto degrada la SNR"*; la segunda, *"ruido real a la salida sobre el ruido que habría si el dispositivo fuera perfecto"* — más física.

### $F$ de catálogo vs degradación real (la distinción que cuesta puntos)

Hay **dos cosas parecidas** que conviene no mezclar: [analysis]

$$\boxed{F_{\text{spec}} = 1+\frac{T_{eq}}{T_0}}\ \text{(catálogo, fijo)} \qquad\qquad \boxed{\text{Degradación} = 1+\frac{T_{eq}}{T_{fuente}}}\ \text{(situación concreta)}$$

**Por qué existe la distinción**: la definición general $F=\frac{(S/N)_{in}}{(S/N)_{out}}$ **depende de qué se conecte a la entrada**. Así no serviría como especificación — el mismo amplificador tendría "distinto $F$" según la fuente. Por eso la norma **fija la referencia en $T_0 = 290$ K**: el *noise figure* de catálogo se mide siempre con una fuente a esa temperatura. **Coinciden solo cuando la fuente está a $T_0$**, que es el caso habitual y por eso casi siempre se confunden.

**Lo que físicamente pasa**: el dispositivo agrega una cantidad **fija** de ruido propio ($N_a$, o equivalentemente $T_{eq}$), independiente de lo que entre:

$$N_{out} = G\,(N_i+N_a)$$

Si $N_i$ sube y $N_a$ queda igual, el aporte del amplificador **pesa proporcionalmente menos** → degrada menos. No es un artificio de definición.

**El ejemplo que lo hace evidente** — LNA satelital con $T_{eq}=50$ K:

| Fuente | Degradación real |
|---|---|
| A $T_0=290$ K (banco de medición) | $1+\frac{50}{290}=1{,}17$ → **0,7 dB** ← *lo que dice el catálogo* |
| Antena mirando cielo frío, $T_{ant}=20$ K | $1+\frac{50}{20}=3{,}5$ → **5,4 dB** |

**El mismo LNA degrada 0,7 dB o 5,4 dB según a qué se conecte.** Por eso en sistemas de bajo ruido (satélites, radioastronomía) se trabaja con $T_{eq}$ y no con $F$: $T_{eq}$ es propiedad del dispositivo, sin ambigüedad de referencia.

> **Cómo redactarlo en el examen**: si un ítem cambia el ruido de entrada, conviene **explicitar el supuesto**: *"el ruido propio del amplificador no cambia, por lo tanto la degradación efectiva pasa de $F$ a $1+T_{eq}/T_{fuente}$"*. Si el corrector esperaba la lectura simple, al menos ve el razonamiento — y con la regla del 25% mínimo por punto, eso suma. Ver el caso resuelto en [[../../outputs/solutions/Ruido_amplificador_F_Comu_2019-02-25|Ruido — amplificador (F_Comu_2019-02-25)]], ítem c).

### ¿Cuándo hace falta $B_N$ en las cuentas?

**Regla general: $B_N$ hace falta cuando necesitás potencias absolutas, no cuando trabajás con cocientes.** [analysis]

| Necesitás… | ¿Hace falta $B$? |
|---|---|
| SNR de entrada dada la de salida y $F$ | ❌ No — todo son cocientes |
| Convertir entre $N$ [W] y $N_0$ [W/Hz] | ✅ Sí |
| Potencia de ruido absoluta desde temperatura ($N=kTB$) | ✅ Sí |
| Expresar un resultado en dBm o W | ✅ Sí |
| Comparar SNR antes/después de un cambio | ❌ No |

> Muchos enunciados dan $B_{eq}$ y $G$ aunque el camino más corto no los use — o habilitan una ruta alternativa, o son distractores. **No forzar su uso**: si se llega al resultado con cocientes, está bien.

### ¿Qué es el ancho de banda equivalente de ruido ($B_N$)?

Es un **truco de definición** para convertir una integral en una multiplicación. [analysis]

**El problema**: un filtro real no corta en vertical — tiene flancos graduales y deja pasar ruido fuera de la banda nominal. La potencia de ruido que realmente pasa es

$$N = \int_0^\infty N_0\,|H(f)|^2\,df$$

una integral distinta para cada filtro.

**La solución**: se define un **filtro rectangular ideal equivalente** con (1) la misma ganancia máxima $|H(f_0)|$ y (2) que deje pasar la misma potencia de ruido total. Su ancho es $B_N$:

$$N_0|H(f_0)|^2 B_N = \int_0^\infty N_0|H(f)|^2df \quad\Longrightarrow\quad \boxed{B_N = \frac{1}{|H(f_0)|^2}\int_0^\infty|H(f)|^2df}$$

**Imagen mental**: es el **rectángulo con la misma área** que la curva $|H(f)|^2$, a la misma altura. Se reemplaza la curva de bordes suaves por un rectángulo equivalente. Por eso $N = N_0B_N$ es **exacta**, no aproximada — $B_N$ está definido precisamente para que lo sea.

**Comparado con el ancho de banda de −3 dB**: $B_N$ es **siempre mayor**, porque las colas del filtro también dejan pasar ruido.

| Filtro | $B_N/B_{3dB}$ |
|---|---|
| RC de un polo | $\pi/2 = 1{,}57$ |
| Butterworth 2 polos | $1{,}11$ |
| Butterworth 3 polos | $1{,}05$ |
| Ideal (brick-wall) | $1$ |

Cuanto más abrupto el filtro, más se parecen.

> **En el examen casi siempre te lo dan** — como dato directo ("ancho de banda equivalente de ruido $B_{eq}=25$ kHz") o por referencia ("tomar el ancho equivalente de ruido igual al calculado en a)"). Rara vez hay que calcular la integral.

> **Atajos numéricos que conviene memorizar:**
> - $T_0 = 290$ K
> - $kT_0 = 4\times10^{-21}$ W/Hz $= \mathbf{-174}$ **dBm/Hz** ← el número más útil de todo el tema
> - $F$ en dB → lineal: $F = 10^{F_{dB}/10}$. Ej: 3 dB → 2; 6 dB → 4; 10 dB → 10

## Relación entrada/salida en dB (la que más se usa)

$$\boxed{\left(\frac{S}{N}\right)_{out}\bigg|_{dB} = \left(\frac{S}{N}\right)_{in}\bigg|_{dB} - F_T\big|_{dB}}$$

**La figura de ruido total, en dB, es literalmente cuántos dB de SNR se pierden.** De ahí que se despeje en cualquier dirección según lo que pidan.

## El patrón estrella: cascada de repetidores

Es el que más aparece. Configuración: $n$ secciones idénticas, cada una **cable (pérdida $L_c$) + repetidor (ganancia $G_r = L_c$)** — el repetidor compensa exactamente la atenuación del tramo.

### Caso repetidores ideales ($F_r = 1$)

$$\boxed{F_T = n\,L_c - (n-1)}$$

**Deducción** (por qué se telescopa): con cable ($F=L_c$, $G=1/L_c$) alternando con repetidor ($F=1$, $G=L_c$), los productos de ganancia acumulada valen $G_1G_2 = \frac{1}{L_c}L_c = 1$ después de cada par. Entonces cada tramo de cable posterior al primero aporta $\frac{L_c-1}{1} = L_c-1$, y los repetidores aportan $0$ (porque $F_r-1=0$):

$$F_T = L_c + (n-1)(L_c-1) = n L_c - (n-1)$$

### Cómo se reparte la pérdida

$$L_{TOTAL}\big|_{dB} = \text{atenuación [dB/km]} \times \text{distancia [km]}, \qquad L_c\big|_{dB} = \frac{L_{TOTAL}\big|_{dB}}{n}$$

⚠️ **Ojo**: se divide **en dB**, y recién después se pasa a lineal. Con $L_{TOTAL}=200$ dB y $n=5$: $L_c = 40$ dB $= 10^4$ (no $200/5$ en lineal).

### Por qué conviene poner más repetidores

Con más secciones, cada tramo de cable atenúa menos y $L_c$ baja **exponencialmente** (porque se divide en dB), mientras que $F_T \approx n L_c$ solo crece linealmente en $n$. Gana la caída de $L_c$:

| $n$ | $L_c$ [dB] | $L_c$ lineal | $F_T = nL_c-(n-1)$ | $F_T$ [dB] |
|---|---|---|---|---|
| 5 | 40 | $10^4$ | $49\,996$ | 47,0 |
| 10 | 20 | $10^2$ | $991$ | 29,9 |
| 20 | 10 | $10$ | $181$ | 22,6 |

**Duplicar la cantidad de repetidores mejoró la SNR en ~17 dB.** Ese es el resultado que los ejercicios quieren que veas.

## Ejercicio resuelto (`F_Comu_2025-02-20_res.md`)

**Enunciado**: cable a $T=T_0$, atenuación 2 dB/km, 100 km, 5 secciones de repetición, $(S/N)_D = 30$ dB en destino. Repetidores ideales ($F=1$) que compensan exactamente la atenuación.

**a) SNR a la entrada del sistema**

$$L_{TOTAL} = 2\ \tfrac{\text{dB}}{\text{km}}\times100\text{ km} = 200\text{ dB} \ \Rightarrow\ L_c = \frac{200}{5} = 40\text{ dB} = 10^4$$

$$F_T = 5(10^4) - 4 = 49\,996 \equiv 46{,}99\text{ dB}$$

$$\left(\frac{S}{N}\right)_{in} = \left(\frac{S}{N}\right)_{out} + F_T = 30 + 46{,}99 = \boxed{76{,}9\text{ dB}}$$

**b) Con 10 secciones** (misma distancia y misma SNR de entrada)

$$L_c = \frac{200}{10} = 20\text{ dB} = 10^2 \ \Rightarrow\ F_T = 10(10^2)-9 = 991 \equiv 29{,}9\text{ dB}$$

$$\left(\frac{S}{N}\right)_{out} = 76{,}9 - 29{,}9 = \boxed{47\text{ dB}}$$

**Ganancia de 17 dB** solo por duplicar los repetidores, sin tocar la potencia transmitida.

**c) Con repetidores de $F_r = 6$ dB $= 4$**

Ahora los repetidores **sí aportan**. Cada uno agrega $\frac{F_r-1}{G_{acum}}$, y como después de cada cable la ganancia acumulada es $1/L_c$, cada repetidor aporta $(F_r-1)L_c$:

$$F_T = \underbrace{n L_c - (n-1)}_{\text{cables}} + \underbrace{n(F_r-1)L_c}_{\text{repetidores}}$$

Con $n=10$, $L_c=100$, $F_r=4$: $F_T = 991 + 10(3)(100) = 991+3000 = 3991 \equiv 36{,}0$ dB

$$\left(\frac{S}{N}\right)_{out} = 76{,}9 - 36{,}0 \approx \boxed{40{,}9\text{ dB}}$$

**d) Si cada sección fuera repetidor primero y después cable**

**Sería mejor en ruido**: poniendo el elemento con ganancia primero, la fórmula de Friis divide las contribuciones posteriores por esa ganancia — el cable degrada mucho menos. Es el mismo principio del **LNA al frente** en un receptor.

**Pero no es viable en la práctica**: el repetidor tendría que entregar la potencia amplificada al inicio del tramo, y con 40 dB de ganancia sobre 100 mW se necesitarían **1000 W** de salida. Inviable por consumo, disipación, no linealidad y seguridad. Por eso los sistemas reales atenúan primero y amplifican después, aceptando la penalidad de ruido.

## SNR en modulaciones analógicas — la referencia $\gamma$

Los finales usan $\gamma$ como **patrón de comparación** entre modulaciones. Lo definen en el propio enunciado (ej. `F_Comu_2019-02-11`: *"$\gamma = S_R/N_R$ en banda base"*): [analysis]

$$\boxed{\gamma = \frac{S_R}{N_0\,W}}$$

| Símbolo | Qué es |
|---|---|
| $S_R$ | Potencia de señal **recibida** |
| $W$ | Ancho de banda del **mensaje** (banda base) |
| $N_0W$ | Potencia de ruido **en la banda del mensaje** |

**Interpretación**: $\gamma$ es la SNR que se tendría transmitiendo el mensaje **directo en banda base**, sin modular, con esa misma potencia recibida. Es el punto de referencia contra el cual se mide si una modulación mejora o empeora las cosas — **el mismo rol que cumple $E_b/N_0$ en digital**.

| Modulación | $(S/N)_D$ | Comparación |
|---|---|---|
| Banda base | $\gamma$ | referencia |
| AM (detección de envolvente) | $<\gamma$ | **peor** que banda base |
| DSB-SC / SSB (coherente) | $\gamma$ | igual |
| **WBFM** | $3\beta^2(\beta+1)\,\gamma$ | **mucho mejor** — es el motivo de usar FM |

> **Es el mismo $(S/N)_{in}$** de la fórmula en [[snr-modulacion-exponencial|SNR en Modulaciones Exponenciales]]; $\gamma$ solo lo hace explícito al aclarar que se mide en el ancho de banda base $W$.

**El trade-off de FM que esto revela**: la mejora va con $\beta^2$, pero el ancho de banda ocupado va con $(\beta+1)$ por Carson. **Se compra SNR gastando espectro** — cuadráticamente a favor, linealmente en contra. Por eso FM broadcast usa $\beta=5$ y no más.

## Los errores que cuestan puntos

1. **Dividir la pérdida total en lineal en vez de en dB** — $L_c$ sale de dividir los dB, después se convierte
2. **Olvidar que un cable tiene $F = L$** — un elemento pasivo degrada la SNR exactamente en su pérdida
3. **Sumar figuras de ruido en dB** — Friis se aplica **en lineal**, recién el resultado se pasa a dB
4. **Confundir $F$ con $T_e$** — se relacionan por $T_e=(F-1)T_0$, no son intercambiables

## Ver también

- [[ruido-termico|Ruido Térmico]] — de dónde sale $N=kTB$
- [[temperatura-ruido|Temperatura de Ruido]] y [[factor-ruido-temperatura|Factor de Ruido y Temperatura Equivalente]]
- [[formula-friis|Fórmula de Friis]] · [[../derivaciones/ecuacion-friis|Derivación completa]]
- [[relacion-snr|Relación Señal-Ruido]]
- [[aclaracion-densidad-espectral-ruido|Densidad Espectral de Ruido]] — convención unilateral/bilateral
- [[../modulacion-digital/digital-formulario-examen|Modulación Digital]] — el puente $E_b/N_0 = SNR\cdot B/R_b$ para llegar al BER
