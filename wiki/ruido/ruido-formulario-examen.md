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
