---
tags:
  - wiki/planificacion
curso: Sistemas de Comunicaciones

---

## 1 · Muestreo / PCM / Cuantificación

|     | Fórmula                                                                 | Qué es                                               | Unidades — cómo se cancela                                                                                                                                                                     | Notas                                                                                   |
| --- | ----------------------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| ●   | $f_s \geq 2B$                                                           | **Nyquist** — frecuencia de muestreo mínima          | $\tfrac{\text{muestras}}{\text{s}} \geq \tfrac{\text{muestras}}{\text{ciclo}}\times\tfrac{\text{ciclos}}{\text{s}}$ → **muestras/s**                                                           | Evita aliasing                                                                          |
|     | $M = 2^n$                                                               | $M$ niveles con $n$ bits/muestra                     | **No hay contabilidad** — $n$ es exponente, conteo puro → **niveles**                                                                                                                          | $n=\log_2M$                                                                             |
|     | $q = \dfrac{V_{pp}}{M}$                                                 | Paso de cuantificación                               | $\tfrac{\text{V}}{\text{niveles}}$ → **V**, altura de un escalón                                                                                                                               | **Error máximo $=q/2$**                                                                 |
|     | $P_q = \dfrac{q^2}{12}$                                                 | Ruido de cuantificación                              | $\text{V}^2\div$ adimensional → **V²** ($=$ W con $R=1$)                                                                                                                                       | El 12 es la varianza de una uniforme en $[-q/2,\,q/2]$                                  |
| ●   | $SNR_Q = \dfrac{3M^2}{F_C^2}$                                           | **SNR de cuantificación — la forma de esta cátedra** | $\tfrac{\text{conteo}^2}{(\text{V}/\text{V})^2}$ — se cancela todo, incluso el $q^2$ de la derivación → **adimensional**                                                                       | $F_C=$ factor de cresta $=$ pico/RMS. Que sea adimensional **es lo que habilita el dB** |
|     | $SNR_Q \approx 6{,}02\,n+1{,}76$ dB                                     | Caso senoidal ($F_C=\sqrt2$)                         | El $6{,}02\,n$ **es** $20\log_{10}2^n$ → **dB**                                                                                                                                                | Es la misma fórmula, no otra                                                        |
|     | $SNR_Q = 3M^2\left\langle\left(\dfrac{m(t)}{V_p}\right)^2\right\rangle$ | Forma general                                        | $\left\langle(m/V_p)^2\right\rangle = 1/F_C^2$, cociente de tensiones → **adimensional**                                                                                                       | Uniforme ($F_C=\sqrt3$) $\Rightarrow SNR_Q=M^2$                                         |
| ●   | $R_b = n\,f_s$                                                          | Tasa de bits                                         | $\tfrac{\text{bits}}{\text{muestra}}\times\tfrac{\text{muestras}}{\text{s}}$ → **bits/s**                                                                                                      | Telefonía: $n=8$, $f_s=8$k → 64 kbps                                                    |
|     | $\left(\dfrac{S}{N}\right)_{sal} = \dfrac{SNR_Q}{1+4P_e(M^2-1)}$        | **SNR con errores de canal**                         | adimensional $\div$ adimensional ($P_e$ es probabilidad) → **adimensional**                                                                                                                    | "Antes del canal" $=$ numerador solo ($P_e\to0$)                                        |
|     | $R_s = \dfrac{R_b}{\log_2 M_{mod}}$                                     | Tasa de símbolos                                     | $\tfrac{\text{bits}}{\text{s}}\div\tfrac{\text{bits}}{\text{símbolo}}$ → **símbolos/s** $=$ baudios                                                                                            | $M_{mod}$ = constelación, **no** los niveles del ADC                                    |
| ●   | $B_{min}=R_s$ (pasabanda) $\quad B_{min}=R_s/2$ (banda base)            | Ancho de banda mínimo                                | $\tfrac{\text{símbolos}}{\text{s}}\div\tfrac{\text{símbolos}}{\text{ciclo}}$ → **ciclos/s** $=$ **Hz**. En pasabanda el $\kappa=1\ \tfrac{\text{ciclo}}{\text{símbolo}}$ cancela el $\tfrac12$ | Con roll-off: $\times(1+\alpha)$                                                        |
| ●   | $\eta = \dfrac{R_b}{B}$                                                 | **Eficiencia espectral**                             | $\tfrac{\text{bits}}{\text{s}}\div\tfrac{\text{ciclos}}{\text{s}}$ → **bits/ciclo** $=$ bits/s/Hz                                                                                              | A $B$ mínimo pasabanda: $\eta=\ell$; banda base: $\eta=2\ell$                           |
|     | $B_{pulso} = \dfrac{1}{\tau}$                                           | Ancho de banda de un pulso PAM                       | $1\div\text{s}$ → **Hz**                                                                                                                                                                       | $\tau$ = ancho del pulso                                                                |

**Los tres factores de conversión** — todos son del mismo tipo ("cuántos X por Y") y **cambian qué se está contando sin cambiar la dimensión**:

| Factor                 | Unidad                            | Dónde vive                           |
| ---------------------- | --------------------------------- | ------------------------------------ |
| $n = \log_2M$          | bits/**muestra**                  | digitalización (fuente)              |
| $\ell = \log_2M_{mod}$ | bits/**símbolo**                  | transmisión                          |
| $2$ (Nyquist)          | muestras/ciclo *o* símbolos/ciclo | muestrear *o* señalizar — son duales |

**La cadena completa** (la composición de los tres factores, y donde se cometen los dos errores más caros):

$$f_s\ \left[\tfrac{\text{muestras}}{\text{s}}\right] \xrightarrow{\ \times n\ (\text{bits/muestra})\ } R_b\ [\text{bps}] \xrightarrow{\ \div\ell\ (\text{bits/símbolo})\ } D\ [\text{baudios}] \xrightarrow{\ \text{Nyquist}\ } B\ [\text{Hz}]$$
$$f_s = 8\text{ kmuestras/s} \ \to\ R_b = 64\text{ kbps} \ \to\ R_s = 32\text{ kbaud} \ \to\ B = 32\text{ kHz}$$
**Companding** — *"¿por qué se emplea Ley A o μ?" → **para equiparar la SNR en señales de baja amplitud**, típicas en voz*: $C_\mu(x)=\operatorname{sgn}(x)\dfrac{\ln(1+\mu|x/V_{max}|)}{\ln(1+\mu)}$ con $\mu=255$ (USA/Japón); A-law con $A=87{,}6$ (Europa), lineal cerca de 0 y log lejos; **no son compatibles entre sí**. Mejora de rango dinámico $\approx20\log_{10}\mu$ ($\mu=255\to\ 48$ dB). **Delta**: slope overload si $\delta f_s < \max|dx/dt|$; $R_{DM}=f_s$ (1 bit/muestra); ADM: $\delta[n]=\delta[n-1]\cdot K$ si misma dirección, $/K$ si cambia ($K\approx1{,}5$).

---

## 2 · Modulación Lineal (AM / DSB-SC / SSB / VSB)

> **Notación de la cátedra**: el índice es **$m$** (no $\mu$ ni $k_a$), la sensibilidad es **$k$**, la moduladora normalizada a pico 1 es **$m_n(t)$**.

|  | Fórmula | Qué es | Notas |
|---|---|---|---|
| ● | $s_{AM}(t) = A_c\big[1+m\,m_n(t)\big]\cos(2\pi f_ct)$ | **Señal AM** | Un tono: $m_n(t)=\cos(2\pi f_mt)$ |
|  | $S_{AM}(f)=\tfrac{A_c}{2}\delta(f{\mp}f_c) + \tfrac{A_c\,m}{4}\delta(f{\mp}f_c{\mp}f_m) + \tfrac{A_c\,m}{4}\delta(f{\mp}f_c{\pm}f_m)$ | **Espectro: 6 deltas** | 2 de portadora ($A_c/2$) + 4 laterales ($A_c m/4$) |
| ● | $m = \dfrac{k\,A_m}{A_c} \qquad m = \dfrac{A_{max}-A_{min}}{A_{max}+A_{min}}$ | Índice de modulación | La 2ª cuando dan medidas de envolvente |
| ● | $P_c = \dfrac{A_c^2}{2R}$ | Potencia de portadora | $R=1\,\Omega$ si no dan dato (normalizada) |
|  | $P_{SB} = \dfrac{A_c^2m^2}{8R} = \dfrac{P_c\,m^2}{4}$ | Potencia de **cada** banda lateral | En dBW: $10\log_{10}(P_{SB}/1\text{W})$ |
| ● | $P_{total} = P_c\left(1+\dfrac{m^2}{2}\right)$ | **Potencia total, un tono** | De memoria |
|  | $P_{total} = P_c\left[1+m^2\langle m_n^2\rangle\right] = P_c\left[1+\dfrac{m^2}{F_C^2}\right]$ | Forma general / con factor de cresta | Tono: $\langle m_n^2\rangle=\tfrac12$ |
|  | $P_{total} = P_c\left(1+\dfrac{\sum_i m_i^2}{2}\right)$ | **AM multitono** | Sumar $m_i^2/2$ de cada tono |
| ● | $PEP = \dfrac{A_{max}^2}{2R} = P_c(1+m)^2$ | Potencia pico de envolvente | Pico, **no** promedio |
|  | $\eta_{AM} = \dfrac{m^2}{2+m^2}$ | Eficiencia de potencia | Máx $33{,}3\%$ en $m=1$. DSB/SSB: $100\%$ |
|  | $\sum_i m_i \leq 1$ | **Sobremodulación en multitono** | El criterio es sobre la **suma**, no cada $m_i$ |
|  | $s_{DSB}(t)=A_c\,m(t)\cos(2\pi f_ct)$ | DSB-SC | $S_{DSB}(f)=\tfrac{A_c}{2}[M(f{-}f_c)+M(f{+}f_c)]$ |
|  | $s_{SSB}(t)=\tfrac{A_c}{2}\big[m(t)\cos\omega_ct \mp \hat m(t)\sin\omega_ct\big]$ | SSB: $-$ es USB, $+$ es LSB | $\hat m$ = transformada de Hilbert |
| ● | $BW_{AM}=BW_{DSB}=2f_m \quad BW_{SSB}=f_m \quad BW_{VSB}=f_m+f_v$ | Anchos de banda | **Multitono: $BW=2f_{m,max}$**, no la suma |
|  | $H(f_c{+}f)+H(f_c{-}f)=1$ para $\lvert f\rvert<f_v$ | Simetría vestigial del filtro VSB | Condición de recuperación perfecta |
|  | $P_{dBW}=10\log_{10}\!\left(\dfrac{P}{1\text{ W}}\right) \quad P_{dBm}=P_{dBW}+30$ | Conversión a dB | $0$ dBW $=30$ dBm |

> ⚠️ **La trampa del factor 2**: las alturas de las deltas son **la mitad** de las amplitudes de los cosenos reales ($A_c$ y $A_cm/2$), porque cada coseno real se reparte en dos exponenciales complejas.

**Tabla comparativa**:

| | AM | DSB-SC | SSB | VSB |
|---|---|---|---|---|
| **BW** | $2f_m$ | $2f_m$ | $f_m$ | $f_m+f_v$ |
| **Eficiencia** | $\leq33\%$ | 100% | 100% | ~100% |
| **Portadora** | Sí | Suprimida | Suprimida | Sí (reducida) |
| **Detección** | Envolvente (barata) | Coherente | Coherente | Envolvente |
| **Transmite DC** | Sí | Sí | **No** | **Sí** |
| **Uso típico** | Radio AM, aviación | Enlaces punto a punto | HF, telefonía | **TV analógica** |

> **Por qué DSB-SC no puede usar detector de envolvente**: la envolvente de $A_cm(t)\cos\omega_ct$ es $A_c|m(t)|$ — el **valor absoluto**, que pierde el signo en cada cruce por cero.
> **Por qué TV usa VSB y no SSB**: el video tiene contenido hasta continua, así que las bandas laterales se tocan en $f_c$ y no hay hueco donde el filtro pueda caer.

**Modulador de ley cuadrática**: con $v_{out}=a\,v_{in}+b\,v_{in}^2$ y $v_{in}=m(t)+c(t)$,

$$v_{out} = \underbrace{a\,m}_{\text{BB}} + \underbrace{a\,c}_{f_c} + \underbrace{b\,m^2}_{\text{BB},\,2f_m} + \underbrace{2b\,m\,c}_{f_c\pm f_m} + \underbrace{b\,c^2}_{\text{DC},\,2f_c}$$

El **filtro pasabanda** centrado en $f_c$ con ancho $2f_m$ deja pasar $a\,c+2b\,m\,c$, que es AM completa con $A_c'=a\,A_c$ y $m = \dfrac{2b\,A_m}{a}$. **Para DSB-SC hacen falta dos moduladores** con $m(t)$ de signo opuesto y restar: la portadora (común) se cancela. Filtrando no alcanza.

---

## 3 · Modulación Exponencial (FM / PM)

| | Fórmula | Qué es | Notas |
|---|---|---|---|
| ● | $s_{FM}(t)=A_c\cos\big(2\pi f_ct+\beta\sin(2\pi f_mt)\big)$ | **Señal FM**, tono único | General: $2\pi k_f\!\int\! m(\tau)d\tau$ en la fase |
| | $s_{PM}(t)=A_c\cos\big(2\pi f_ct+k_p\,m(t)\big)$ | Señal PM | $\Delta\phi = k_pA_m$ |
| | $f_i(t)=f_c+k_f\,m(t)$; con un tono: $f_c+\Delta f\cos(2\pi f_mt)$ | Frecuencia instantánea $=\dfrac{1}{2\pi}\dfrac{d\phi}{dt}$ | En PM: $\phi_i = 2\pi f_ct+k_pm(t)$ |
| | $\text{FM}[m(t)] \equiv \text{PM}\!\left[\int m\,dt\right]$ | **Dualidad FM↔PM** | La base de los moduladores indirectos: integrar antes de un modulador de fase da FM |
| ● | $\Delta f = k_f A_m = \beta f_m$ | Desviación máxima de frecuencia | $k_f$ en Hz/V |
| ● | $\beta = \dfrac{\Delta f}{f_m}$ | Índice de modulación FM | En PM: $\beta = \Delta\phi = k_pA_m$ |
| ● | $B_T = 2(\Delta f+f_m) = 2f_m(\beta+1)$ | **Regla de Carson** | ~98% de la potencia |
| ● | $P = \dfrac{A_c^2}{2R}$ | **Potencia — CONSTANTE, no depende de la modulación** | La trampa #1 del tema |
| | $s_{FM}(t)=A_c\sum_n J_n(\beta)\cos\big[2\pi(f_c+nf_m)t\big]$ | Espectro de Bessel | **Infinitas** laterales; $\sum J_n^2(\beta)=1$ |

**Clasificación**: NBFM si $\beta<0{,}3$ → $B_T\approx2f_m$ (como AM). WBFM si $\beta>1$ → $B_T\approx2\Delta f$.

**FM vs PM — qué queda invariante**:

| | FM | PM |
|---|---|---|
| Proporcional a $A_m$ | $\Delta f = k_fA_m$ | $\Delta\phi = k_pA_m$ |
| Índice | $\beta = \dfrac{k_fA_m}{f_m}$ | $\beta = \Delta\phi = k_pA_m$ |
| **Desviación de frecuencia** | $\Delta f = k_fA_m$ — **no depende de $f_m$** | $\Delta f = \beta f_m = k_pA_mf_m$ — **crece con $f_m$** |
| **Si se duplica $f_m$** (con $A_m$ fijo) | $\Delta f$ **igual**, $\beta$ **a la mitad** | $\Delta\phi$ **igual**, $\Delta f$ **se duplica** |
| Si se duplica $A_m$ | $\Delta f$ y $\beta$ se duplican | $\Delta\phi$ y $\beta$ se duplican |

> **Si se duplica la frecuencia del tono modulante manteniendo su amplitud**: **en FM $\beta$ cae a la mitad; en PM $\beta$ no cambia** (y por eso $\Delta f$ se duplica).

**Multiplicadores y mezcladores**:

| Bloque | $f_c$ | $\Delta f$ | $\beta$ | $f_m$ | $BW$ |
|---|---|---|---|---|---|
| **Multiplicador $\times n$** | $n f_c$ | $n\,\Delta f$ | $n\beta$ | **igual** | cambia (Carson con el nuevo $\Delta f$) |
| **Mezclador** (OL en $f_{OL}$) | $f_c\pm f_{OL}$ | **igual** | **igual** | igual | **igual** |

> **Por qué**: el multiplicador multiplica **la fase entera**, $n\phi(t)=2\pi(nf_c)t+n\beta\sin(2\pi f_mt)$ — $\beta$ es coeficiente **afuera** del seno (escala), $f_m$ vive **adentro** del argumento (no se toca). El mezclador suma una fase **sin modulación** ($2\pi f_{OL}t$), así que solo mueve la portadora.

**Modulador Armstrong** — estructura $\text{NBFM}(f_1,\Delta f_1) \to \times n_1 \to \text{Mezclador}(f_{OL}) \to \times n_2 \to (f_c,\Delta f)$:

$$n_{total}=n_1n_2 = \frac{\Delta f_{salida}}{\Delta f_{NBFM}} \qquad\qquad f_{OL}=\left|\frac{f_c}{n_2}-n_1f_1\right|$$

**La multiplicación total la fija la desviación** (el mezclador no la toca); el mezclador corrige la portadora, que no cierra sola. $n_1$ y $n_2$ solo deben cumplir $n_1n_2=n_{total}$ — el reparto lo elegís vos, **justificalo por escrito**. $BW$ a la salida del NBFM $\approx2f_m$; en transmisión, Carson. ⚠️ Si la modulante es una banda ("de 30 Hz a 15 kHz"), usar $f_m=f_{m,max}$.

---

## 4 · SNR de posdetección

$$\boxed{\gamma = \frac{S_R}{N_0\,W}} \qquad \begin{array}{l} S_R = \text{potencia recibida} \\ W = \text{ancho de banda del mensaje} \\ N_0W = \text{ruido en la banda del mensaje} \end{array}$$

$\gamma$ es la SNR que se tendría transmitiendo el mensaje **directo en banda base**, con esa misma potencia recibida — el patrón de comparación. Mismo rol que $E_b/N_0$ en digital.

| Modulación | $(S/N)_D$ | Respecto de $\gamma$ |
|---|---|---|
| **Banda base** | $\gamma$ | 0 dB (referencia) |
| **DSB-SC** (coherente) | $\gamma$ | **0 dB** |
| **SSB** (coherente) | $\gamma$ | **0 dB** |
| **AM** (envolvente), índice $m$ | $\dfrac{m^2\langle m_n^2\rangle}{1+m^2\langle m_n^2\rangle}\,\gamma = \eta_{AM}\,\gamma$ | **negativo — siempre peor** |
| **FM** | $3\Delta^2x^2\,\gamma$, con $\Delta=\dfrac{\Delta f}{W}$, $x^2=\left\langle\left(\dfrac{m(t)}{A_m}\right)^2\right\rangle$ | **muy positivo** |

**Valores para tono senoidal** ($\langle m_n^2\rangle = x^2 = \tfrac12$):

| Caso | Cuenta | vs $\gamma$ |
|---|---|---|
| AM con $m=0{,}9$ | $0{,}405/1{,}405 = 0{,}288$ | $\mathbf{-5{,}4}$ **dB** |
| AM con $m=1$ (máximo posible) | $0{,}5/1{,}5 = 1/3$ | $-4{,}8$ dB |
| DSB-SC / SSB | $1$ | $0$ dB |
| FM, $\Delta f=75$ kHz, $W=15$ kHz ($\beta=5$) | $3(25)(0{,}5)=37{,}5$ | $\mathbf{+15{,}7}$ **dB** |

> 		**La lectura conceptual**: **AM con detección de envolvente es peor que transmitir en banda base** (nunca supera $-4{,}8$ dB), porque gasta la mayor parte de la potencia en la portadora, que no lleva información. DSB-SC y SSB **empatan**. **Solo FM mejora**, comprando SNR con ancho de banda: la mejora va con $\beta^2$ pero el $BW$ con $(\beta+1)$ — cuadrático a favor contra lineal en contra. Notar que $(S/N)_D^{AM}=\eta_{AM}\gamma$: **la eficiencia de potencia de AM es exactamente su penalidad de SNR**.

> ⚠️ **Variantes de la fórmula de FM**: distintos textos escriben $3\beta^2\gamma$, $3\beta^2(\beta+1)\gamma$ o $3\Delta^2x^2\gamma$. **Si el enunciado la da, usar esa.**

**Umbral**: $SNR_{umbral}\approx10$ dB (AM y discriminador FM convencional); PLL ~7 dB, FMFB ~4-5 dB. Por debajo, colapso de SNR. DSB-SC y SSB coherentes **no tienen efecto umbral**. **Pre/de-énfasis**: mejora $\approx10$–$13$ dB, $\tau=75\,\mu$s (USA/Japón) o $50\,\mu$s (Europa).

---

## 5 · Ruido / Friis / Enlaces

> ⚠️ **"Factor de ruido" $\neq$ "cifra de ruido"**: "factor de ruido 4" es **lineal**; "cifra de ruido de 6 dB" es **en dB**. **El vocabulario del enunciado te dice las unidades.**

|     | Fórmula                                                                                                               | Qué es                                                 | Notas                                                                                        |
| --- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| ●   | $N = kTB$                                                                                                             | **Ruido térmico**                                      | $k=1{,}38\times10^{-23}$ J/K. También $N_0=kT$ [W/Hz]                                        |
|     | $v_n^2 = 4kTRB$                                                                                                       | Ruido térmico visto como **tensión** (Johnson-Nyquist) | Sobre una resistencia $R$. La potencia **disponible** sigue siendo $kTB$                     |
| ●   | $F = \dfrac{(S/N)_{in}}{(S/N)_{out}} = \dfrac{N_o}{N_i\,G}$                                                           | **Factor de ruido** (adimensional, $\geq1$)            | 2ª forma: "ruido real vs el de un dispositivo perfecto"                                      |
| ●   | $T_e = (F-1)\,T_0 \qquad F = 1+\dfrac{T_e}{T_0}$                                                                      | Temperatura equivalente de ruido                       | $T_0=290$ K de referencia                                                                    |
| ●   | $F_T = F_1 + \dfrac{F_2-1}{G_1} + \dfrac{F_3-1}{G_1G_2}+\cdots$                                                       | **Friis (cascada)**                                    | **La 1ª etapa domina** → LNA primero. **En lineal**                                          |
|     | $T_e = T_1+\dfrac{T_2}{G_1}+\dfrac{T_3}{G_1G_2}+\cdots$                                                               | Friis en temperaturas                                  | Equivalente; a veces más cómoda                                                              |
| ●   | $F = L$, $\quad G = 1/L$                                                                                              | **Elemento pasivo** (cable, atenuador)                 | **La pérdida es igual a la figura de ruido**                                                 |
| ●   | $\left(\dfrac{S}{N}\right)_{out}\Big\rvert_{dB} = \left(\dfrac{S}{N}\right)_{in}\Big\rvert_{dB} - F_T\Big\rvert_{dB}$ | La relación que más se usa                             | En lineal es $(S/N)_{out} = (S/N)_{in}/F_T$. $F_T$ en dB **es** cuántos dB de SNR se pierden |
|     | $T_{sys}=T_{antena}+T_{receptor}$                                                                                     | Temperatura de sistema                                 | Aditiva                                                                                      |
|     | $B_N = \dfrac{1}{\lvert H(f_0)\rvert^2}\displaystyle\int_0^\infty \lvert H(f)\rvert^2df$                              | Ancho de banda **equivalente de ruido**                | Hace $N=N_0B_N$ **exacta**. Casi siempre lo dan                                              |

> ⚠️ **Friis solo funciona en lineal.** $F$, $L$ y $G$ son adimensionales pero casi siempre los dan en dB: convertir con $X=10^{X_{dB}/10}$ **antes** de aplicar Friis, y recién pasar el resultado a dB.

> **$B_N$ hace falta cuando necesitás potencias absolutas, no cuando trabajás con cocientes.** Sí para: $N=kTB$, convertir $N\leftrightarrow N_0$, expresar en dBm o W. No para: despejar SNR de entrada dada la de salida y $F$, comparar SNR antes/después. Muchos enunciados dan $B_{eq}$ y $G$ como distractores — **no forzar su uso**.

### El patrón estrella: cascada de repetidores

$n$ secciones idénticas de **cable ($L_c$) + repetidor ($G_r=L_c$)** — el repetidor compensa exactamente la atenuación.

$$L_{TOTAL}\big|_{dB} = \text{atenuación}\left[\tfrac{\text{dB}}{\text{km}}\right]\times d[\text{km}], \qquad L_c\big|_{dB} = \frac{L_{TOTAL}\big|_{dB}}{n}$$

$$\boxed{F_T = n\,L_c-(n-1)}\ \text{(repetidores ideales, } F_r=1) \qquad \boxed{F_T = \underbrace{nL_c-(n-1)}_{\text{cables}} + \underbrace{n(F_r-1)L_c}_{\text{repetidores}}}$$

⚠️ **Se divide en dB, y recién después se pasa a lineal.** Con $L_{TOTAL}=200$ dB y $n=5$: $L_c=40$ dB $=10^4$ (no $200/5$ en lineal).

**Por qué conviene poner más repetidores**: $L_c$ baja **exponencialmente** (se divide en dB) mientras $F_T\approx nL_c$ crece solo linealmente.

| $n$ | $L_c$ [dB] | $L_c$ lineal | $F_T$ | $F_T$ [dB] |
|---|---|---|---|---|
| 5 | 40 | $10^4$ | $49\,996$ | 47,0 |
| 10 | 20 | $10^2$ | $991$ | 29,9 |
| 20 | 10 | $10$ | $181$ | 22,6 |

**Duplicar los repetidores mejoró la SNR ~17 dB** sin tocar la potencia transmitida. Y **repetidor primero + cable después sería mejor en ruido** (Friis divide lo posterior por la ganancia, igual que el LNA al frente) pero **inviable**: 40 dB sobre 100 mW pediría 1000 W de salida.

### Balance de enlace

$$L_{FSPL}\big|_{dB} = 32{,}44 + 20\log_{10}\!\big(f_{[MHz]}\big) + 20\log_{10}\!\big(d_{[km]}\big)$$

⚠️ **$f$ en MHz y $d$ en km** — la constante cambia con las unidades (a veces se escribe $32{,}442$ o se redondea a 33). Sale de $L=(4\pi d/\lambda)^2$. **Crece 6 dB al duplicar distancia o frecuencia.**

$$\left(\frac{S}{N}\right)_{RX} = P_{TX}+G_{TX}-L_{FSPL}-L_{otras}+G_{RX}-N \qquad\text{(todo en dB)}$$

$$\boxed{N_{dBm} = -174 + 10\log_{10}B_{[Hz]} + F_{[dB]}} \qquad (kT_0 = 4\times10^{-21}\ \text{W/Hz} = -174\ \text{dBm/Hz})$$

### $F$ de catálogo vs degradación real

$$F_{spec} = 1+\frac{T_{eq}}{T_0}\ \text{(catálogo, fijo)} \qquad\qquad \text{Degradación} = 1+\frac{T_{eq}}{T_{fuente}}\ \text{(situación concreta)}$$

El dispositivo agrega ruido propio **fijo** ($N_{out}=G(N_i+N_a)$, con $N_a=kT_{eq}B$): si $N_i$ sube, ese aporte **pesa proporcionalmente menos** → degrada menos. La norma fija la referencia en $T_0=290$ K para que $F$ sirva como especificación. **Coinciden solo cuando la fuente está a $T_0$.** Ejemplo: LNA con $T_{eq}=50$ K degrada **0,7 dB** en el banco ($T_0$) y **5,4 dB** con antena a cielo frío ($T_{ant}=20$ K) — el mismo LNA.

> **Cómo enunciar el supuesto** si cambia el ruido de entrada: *"el ruido propio del amplificador no cambia, por lo tanto la degradación efectiva pasa de $F$ a $1+T_{eq}/T_{fuente}$"*.

---

## 6 · Teoría de la Información

> Casi siempre **combinada con Modulación Digital**: se calcula una tasa de información y después se pregunta si tal modulación puede transportarla.

| | Fórmula | Qué es | Notas |
|---|---|---|---|
| | $I_i = \log_2\dfrac{1}{p_i} = -\log_2 p_i$ | Información de un símbolo [bits] | Menos probable → más información |
| ● | $H = -\sum_i p_i\log_2 p_i = \sum_i p_i\log_2\dfrac{1}{p_i}$ | **Entropía** [bits/símbolo] | **Para calcular a mano usar la del recíproco**: todos los términos salen positivos |
| | $H_{max} = \log_2 M$ | Entropía máxima | **Solo si son equiprobables** |
| ● | $R = r\,H$ | **Tasa de información** [bps] | $r$ = símbolos/s $\times$ $H$ = bits/símbolo |
| ● | $C = B\log_2\!\left(1+\dfrac{S}{N}\right)$ | **Shannon-Hartley** [bps] | $S/N$ **LINEAL**, no dB. 20 dB → 100 |
| | $\text{Red} = 1-\dfrac{H}{H_{max}}$ | Redundancia ($\eta=H/H_{max}$) | Cuánto se puede comprimir sin perder |
| ● | $\dfrac{E_b}{N_0} > \ln 2 = -1{,}59$ dB | **Límite absoluto de Shannon** | Ningún esquema opera por debajo |
| | $C_\infty = \dfrac{S}{N_0\ln2} = 1{,}44\dfrac{S}{N_0}$ | Capacidad con $B\to\infty$ | Límite **finito** aun con banda infinita |
| | $C\approx B\log_2(S/N)$ si $S/N\gg1$ $\quad$ $C\approx1{,}44\,B\,S/N$ si $S/N\ll1$ | Los dos regímenes de Shannon | Limitado por **banda** (log) vs por **potencia** (lineal) |
| | $\left(\dfrac{S}{N}\right)_{sal} = \left[1+\left(\dfrac{S}{N}\right)_{ent}\right]^{B_T/B}-1$ | **Sistema ideal** | Ver demostración abajo |

**Símbolo, binit y bit — tres cosas distintas** (la cátedra usa \"binits\" explícitamente):

| Concepto | Qué es | Unidad |
|---|---|---|
| **Símbolo** | Una **forma de onda** transmitida, sostenida durante $T_s$ (un punto de constelación) | símbolos/s $=$ **baudios** |
| **Binit** | Un **0 o un 1** — un valor lógico | binits/s |
| **Bit** (Shannon) | Unidad de **información** — cuánto reduce la incertidumbre | bits/s |

$$\underbrace{D\ [\text{símbolos/s}]}_{\text{fija el ancho de banda}} \xrightarrow{\ \times\ell\ } \underbrace{R_b\ [\text{binits/s}]}_{\text{flujo en el canal}} \xrightarrow{\ \times H/\ell\ } \underbrace{R\ [\text{bits/s}]}_{\text{información real}}$$

$$R_{\text{información}} = r\,H \ \leq\ R_{\text{binario}} = \ell\,D \qquad \text{(con igualdad solo si todo es equiprobable)}$$

Un binit transporta 1 bit **solo si los dos valores son equiprobables**: con $p=\{0{,}9;\,0{,}1\}$, $H=0{,}469$ bits/binit — el resto es redundancia. **El ancho de banda depende de la tasa de símbolos, no de la de bits** (todo el negocio de QAM).

### El patrón dominante: ¿es factible esta modulación?

$$\text{Fuente} \xrightarrow{\ R=rH\ } \text{tasa de info} \xrightarrow{\ \text{Shannon}\ } B_{Shannon}=\frac{R}{\log_2(1+S/N)} \quad\text{vs}\quad B_{real} = D = \frac{R}{\ell}$$

| Resultado | Interpretación |
|---|---|
| $B_{real} > B_{Shannon}$ | ✅ **Factible** — está por encima del mínimo teórico |
| $B_{real} < B_{Shannon}$ | ❌ **No factible** — violaría el límite de Shannon |

> **Shannon marca un PISO, no un techo.** Necesitar más ancho de banda que el mínimo es normal (todo esquema real lo hace); necesitar *menos* sería imposible — no "difícil", **imposible**. ⚠️ **Ojo con la intuición invertida**: subir $M$ **reduce** el $BW$ necesario, lo que parece siempre bueno, pero al bajar de la cota de Shannon deja de ser realizable con esa SNR.

**Fuentes compuestas** (imagen → líneas → puntos → niveles): multiplicar en cadena hasta bits/s.

$$R\left[\tfrac{\text{bits}}{\text{s}}\right] = \underbrace{\text{elementos por trama}}_{\text{conteo}} \times \underbrace{H}_{\text{bits/elemento}} \times \underbrace{\text{tramas por segundo}}_{1/\text{s}}$$

### Enlace asincrónico con trama de caracteres

Un enlace a $R_b$ binits/s transmite caracteres de $N_t$ binits **de trama completa**, de los cuales solo unos pocos son el dato: el ASCII son 7, y el resto es **overhead** (paridad, arranque, parada).

| Se pide | Cómo sale |
|---|---|
| Caracteres por segundo | $\dfrac{R_b\ [\text{binits/s}]}{N_t\ [\text{binits/carácter}]}$ — **dividir por la trama completa, no por los 7 del dato** |
| Tiempo de un texto | $\dfrac{\text{caracteres del texto}}{\text{caracteres/s}}$; contar **el espacio entre palabras** como un carácter más |
| $H$ por carácter, y por palabra | $H=\sum_i p_i\log_2\frac{1}{p_i}$; por palabra: $\times$ (caracteres/palabra **+ 1** por el espacio) |
| Tasa de información | $R = \text{caracteres/s}\times H$ — **no** es $R_b$ |

**Cuando las probabilidades vienen por familias** (un grupo de $n_1$ caracteres con probabilidad $p_1$, otro de $n_2$ con $p_2$, …), la entropía se agrupa y **se calcula de una sola pasada**:

$$\boxed{H = \sum_k n_k\,p_k\log_2\frac{1}{p_k}} \qquad\text{con la verificación obligatoria}\quad \sum_k n_k\,p_k = 1$$

Chequear que las probabilidades sumen 1 **antes** de calcular: si no suman, hay un grupo mal contado y todo lo que sigue arrastra el error.

> **Las tres tasas conviviendo**: por el cable van $R_b$ **binits/s**, que son $R_b/N_t$ **caracteres/s** (los símbolos de la fuente), que transportan $R = (R_b/N_t)\,H$ **bits/s** de información real. **Se pierde dos veces**: primero el overhead de trama ($7/N_t$), y después porque $H < \log_2(\text{alfabeto})$ al no ser los caracteres equiprobables. Con $N_t=10$ y un alfabeto de ~90 caracteres, la eficiencia total ronda el 50%.

**Demostración del sistema ideal** (un sistema ideal no pierde información, así que las capacidades a un lado y otro deben igualarse):

$$\underbrace{B_T\log_2\!\left[1+\left(\tfrac{S}{N}\right)_{ent}\right]}_{C\ \text{del canal de transmisión}} = \underbrace{B\log_2\!\left[1+\left(\tfrac{S}{N}\right)_{sal}\right]}_{C\ \text{en banda base}} \ \Longrightarrow\ 1+\left(\tfrac{S}{N}\right)_{sal} = \left[1+\left(\tfrac{S}{N}\right)_{ent}\right]^{B_T/B}$$

**Interpretación**: ensanchar la banda mejora la SNR **exponencialmente** (exponente $B_T/B$). FM logra mejora $\propto\beta^2$ (polinómica) — por eso FM no es óptimo, solo bueno.

**Derivación del límite $-1{,}59$ dB**: en $C=B\log_2(1+S/N)$ poner $S=E_bC$ (al límite $R_b=C$) y $N=N_0B$; con $\eta=C/B$ queda $\dfrac{E_b}{N_0}=\dfrac{2^\eta-1}{\eta}$, y $\lim_{\eta\to0}=\ln2$ ($\to-1{,}59$ dB).

° **Codificación de fuente**: $\bar L=\sum p_il_i$; $\dfrac{H}{\log_2M}\leq\dfrac{\bar L_s}{s}<\dfrac{H}{\log_2M}+\dfrac1s$ (extensión de orden $s$); Kraft-McMillan $\sum M^{-l_i}\leq1$; $\eta=\dfrac{H}{\bar L\log_2M}$. ° **Códigos de canal**: $e_d=d_{min}-1$ detectables, $e_c=\lfloor(d_{min}-1)/2\rfloor$ corregibles, tasa $k/n$, Singleton $d_{min}\leq n-k+1$.

---

## 7 · Modulación Digital / BER

|  | Fórmula | Qué es | Notas |
|---|---|---|---|
| ● | $\ell = \log_2 M$ | Bits por símbolo | QPSK → 2; 16-QAM → 4; 64-QAM → 6 |
| ● | $D = \dfrac{R_b}{\ell}$ | Tasa de símbolos [baudios] | **Es lo que fija el ancho de banda**, no $R_b$ |
|  | $s_{QAM}(t) = I\cos(2\pi f_ct) - Q\sin(2\pi f_ct) = \lvert s\rvert\cos(2\pi f_ct+\phi)$ | **Señal QAM** — dos portadoras en cuadratura | $\lvert s\rvert=\sqrt{I^2+Q^2}$, $\phi=\arctan(Q/I)$: cartesianas → polares |
| ● | $S = \dfrac{\langle\lvert s\rvert^2\rangle}{2}$ | **Potencia media transmitida** | El $/2$ es pico→RMS del **portador** |
|  | $\langle\lvert s\rvert^2\rangle = \dfrac{2(M-1)}{3}a^2$ ($M$-QAM) $\ \to\ S=\dfrac{(M-1)a^2}{3}$ | Potencia de QAM cuadrada | Niveles $\pm a,\pm3a,\ldots$ |
|  | $\langle\lvert s\rvert^2\rangle = A^2$ ($M$-PSK) $\ \to\ S=\dfrac{A^2}{2}$ | Potencia de PSK | Envolvente constante |
|  | $N = N_0\,B_N$ | Potencia de ruido en la banda | $N_0$ es **densidad** [W/Hz $\equiv$ J] |
| ● | $E_b = \dfrac{S}{R_b} = S\,T_b$ | Energía por bit [J/bit] | $T_b=1/R_b$ |
| ● | $\dfrac{E_b}{N_0} = \dfrac{S}{R_b\,N_0}$ *(directa)* $\qquad \dfrac{E_b}{N_0} = SNR\cdot\dfrac{B}{R_b}$ *(vía SNR)* | La métrica que entra en el BER | **Preferí la directa** |
|  | $\dfrac{E_s}{N_0} = \dfrac{E_b}{N_0}\log_2M$ | Energía por **símbolo** | $E_s = \ell\,E_b$: el símbolo lleva $\ell$ bits |
|  | $BER \approx \dfrac{SER}{\log_2M}$ | Puente BER ↔ SER con **mapeo Gray** | Gray hace que 1 error de símbolo $\approx$ 1 bit errado |

> ⚠️ **Preferí siempre la ruta directa** $\frac{E_b}{N_0}=\frac{S}{R_bN_0}$: solo necesita potencia, tasa de bits y densidad de ruido — **ni ancho de banda ni SNR**. La vía SNR arrastra cualquier error previo y falla si el enunciado **cambia $N_0$ entre ítems** (que es exactamente lo que hacen a propósito).

> **En 16-QAM**: calcular $S$ con la **amplitud máxima** de la constelación, u olvidar el $/2$ del portador. Son **dos efectos distintos**: promedio sobre la constelación (factor $18/10=1{,}8$ en 16-QAM) **y** pico→RMS del portador (factor 2). **Ante una amplitud máxima, verificar si la señal tiene amplitud constante antes de calcular potencia.**

> ⚠️ **$a$ (QAM) y $A$ (PSK) NO son lo mismo**: $a$ es la **unidad de grilla** (mitad del espaciado; **ningún símbolo vale $a$**), $A$ es el **radio** (todos los símbolos valen $A$). Puente en QPSK, que es a la vez 4-QAM y 4-PSK: $\tfrac{2(4-1)}{3}a^2 = 2a^2 = A^2 \Rightarrow A=a\sqrt2$ ✓ (los puntos $(\pm a,\pm a)$ están a distancia $a\sqrt2$ del origen).

### Los tres anchos de banda — no confundirlos

| Cuál | Fórmula | Cuándo |
|---|---|---|
| **Nulo a nulo** | $B = 2D$ | Pulso rectangular, lóbulo principal |
| **Mínimo (Nyquist ideal)** | $B = D$ | Cuando dice "ancho de banda mínimo ideal" ($\alpha=0$) |
| **Con roll-off** | $B = D(1+\alpha)$ | Coseno realzado real; el enunciado da $\alpha$ |

En **banda base** todo se divide por 2: $B_{min}=D/2$, $B=\dfrac{D}{2}(1+\alpha)$. Para **FSK** manda Carson, no Nyquist: $\ \boxed{B_{FSK}=2(\Delta f+D)}$ con $\Delta f = \dfrac{|f_1-f_0|}{2}$.

**Eficiencia espectral**: $\ \eta = \dfrac{R_b}{B}$ [bits/s/Hz] $\Rightarrow$ a $B$ mínimo pasabanda $\eta=\ell$; con roll-off $\eta=\dfrac{\ell}{1+\alpha}$; en banda base el doble.

> **Los dos "2" distintos**: el de Nyquist ($R_s=2B$) es **2 símbolos/ciclo**, un factor de conversión con contenido físico; el de nulo a nulo ($B=2D$) son **2 lados del lóbulo**, pura simetría geométrica. Consecuencia: $B_{n\text{-}n}=2B_{min}$ en pasabanda — **el precio de usar pulsos rectangulares** en vez de sinc.

### BER — tabla completa

| Modulación | $P_e$ |
|---|---|
| **BPSK** | $Q\!\left(\sqrt{2E_b/N_0}\right)$ |
| **QPSK** | $Q\!\left(\sqrt{2E_b/N_0}\right)$ — **igual que BPSK** |
| **$M$-PSK** | $\approx Q\!\left(\sqrt{2E_b/N_0}\,\sin(\pi/M)\right)$ |
| **$M$-QAM** | $\approx 4\,Q\!\left(\sqrt{3E_b/\big[(M-1)N_0\big]}\right)$ |
| **FSK coherente** | $Q\!\left(\sqrt{E_b/N_0}\right)$ |
| **FSK no coherente** | $\tfrac12 e^{-E_b/2N_0}$ |
| **DPSK** | $\tfrac12 e^{-E_b/N_0}$ |
| **OOK / unipolar** | $Q\!\left(\sqrt{E_b/N_0}\right)$ |

- **BPSK y QPSK dan lo mismo por bit** — QPSK transmite el doble de bits en el mismo $BW$ **sin penalidad de BER**.
- **Las no coherentes** tienen forma **exponencial**, no $Q(\cdot)$, y pagan ~3 dB a cambio de no necesitar recuperación de portadora.
- **Al subir $M$**: mejor eficiencia espectral, **peor BER** a igual $E_b/N_0$ (los puntos quedan más juntos).

### La forma general: energía diferencia $E_d$ (todas las de arriba son casos particulares)

$$\boxed{P_e = Q\!\left(\sqrt{\frac{E_d}{2N_0}}\right)} \qquad \boxed{E_d = \int_0^{T_b}\big|s_1(t)-s_0(t)\big|^2dt = d_{min}^2}$$

**Es la forma que dan los enunciados** en los ejercicios de banda base con NRZ. Y unifica todo:

$$P_e = Q\!\left(\sqrt{\frac{E_d}{2N_0}}\right) = Q\!\left(\frac{d_{min}}{\sqrt{2N_0}}\right) = Q\!\left(\frac{d_{min}}{2\sigma}\right), \qquad \sigma^2 = \frac{N_0}{2}$$

| Señalización | $s_1,\ s_0$ | $E_d$ | $S$ | $E_d$ vs $E_b$ | $P_e$ |
|---|---|---|---|---|---|
| **Antipodal** (polar NRZ, BPSK) | $+V,\ -V$ | $4V^2T_b$ | $V^2$ | $4E_b$ | $Q\!\left(\sqrt{2E_b/N_0}\right)$ |
| **Unipolar** (NRZ, OOK) | $V,\ 0$ | $V^2T_b$ | $\dfrac{V^2}{2}$ | $2E_b$ | $Q\!\left(\sqrt{E_b/N_0}\right)$ |
| **Ortogonal** (FSK coherente) | ortogonales | $2E_b$ | — | $2E_b$ | $Q\!\left(\sqrt{E_b/N_0}\right)$ |

**Para unipolar NRZ**: $\quad S = \dfrac{V^2}{2}, \qquad E_d = V^2T_b = 2S\,T_b = \dfrac{2S}{R_b}$

> **$E_b$ vs $E_d$ — no son lo mismo, y no compiten**: $E_b=S\,T_b$ mide el **costo** energético; $E_d$ mide la **distinguibilidad**. $E_d$ es la cantidad fundamental (una sola fórmula, válida para cualquier señalización); $E_b$ funciona **una vez fijado el esquema**, porque ahí $E_d=k\,E_b$ con $k$ conocido. **Las distintas fórmulas de la tabla de BER SON los distintos $k$**: $k=4$ antipodal, $k=2$ unipolar/ortogonal — de ahí los 3 dB. La tabla se escribe en $E_b$ porque es lo que **cuesta** y permite comparar esquemas de forma justa.

**Receta para una señalización que NO esté en la tabla** (4 pasos, no hay que memorizar nada):

1. $E_d = \displaystyle\int_0^{T_b}\big|s_1(t)-s_0(t)\big|^2dt$ — **integrar siempre sobre todo $T_b$**; donde los dos símbolos coinciden el integrando vale cero y no aporta
2. $E_b = \dfrac{E_1+E_0}{2}$ (símbolos equiprobables), con $E_i=\int_0^{T_b}|s_i|^2dt$
3. $k = E_d/E_b$
4. $P_e = Q\!\left(\sqrt{\dfrac{k\,E_b}{2N_0}}\right)$

**Ejemplo — polar RZ** (pulso solo en la primera mitad, $\pm V$ y luego 0): $E_d = (2V)^2\tfrac{T_b}{2} = 2V^2T_b$, $E_b = \tfrac{V^2T_b}{2}$, $k=4$ → **mismo BER que BPSK**. Acortar el pulso **no empeora la BER a igual $E_b$**, solo duplica el ancho de banda. El precio de RZ es espectral, no de error.

### Cómo se arman las constelaciones (de dónde salen las coordenadas)

**QAM cuadrada**: grilla $L\times L$ con $L=\sqrt M$ niveles por eje, en **múltiplos impares** de $a$: $\pm a,\pm3a,\ldots,\pm(L-1)a$.

| $M$ | $L=\sqrt M$ | Niveles por eje | $d_{min}$ | $\lvert s\rvert_{max}$ |
|---|---|---|---|---|
| 4 (QPSK) | 2 | $\pm a$ | $2a$ | $a\sqrt2$ |
| 16 | 4 | $\pm a,\pm3a$ | $2a$ | $3a\sqrt2$ |
| 64 | 8 | $\pm a,\pm3a,\pm5a,\pm7a$ | $2a$ | $7a\sqrt2$ |
| 256 | 16 | $\pm a,\ldots,\pm15a$ | $2a$ | $15a\sqrt2$ |

**Cómo sacar $a$** del dato que dé el enunciado: $|s|_{max}=(L-1)a\sqrt2$ · $\langle|s|^2\rangle=\tfrac{2(M-1)}{3}a^2$ · $d_{min}=2a$.

**PSK**: puntos sobre una circunferencia de radio $A$ a ángulos $2\pi k/M$:

$$s_k = \left(A\cos\tfrac{2\pi k}{M},\ A\sin\tfrac{2\pi k}{M}\right), \qquad d_{min} = 2A\sin\tfrac{\pi}{M}$$

En general, para cualquier constelación: $\ d_{min} = \min_{i\neq j}\lVert s_i-s_j\rVert$.

**Todos los puntos con la misma magnitud** → envolvente constante, **sin factor de cresta de constelación**. Por eso PSK se usa donde el amplificador trabaja saturado (satélite) y QAM donde importa la eficiencia espectral. **Lo que decide la inmunidad al ruido es $d_{min}$, no la potencia** — literalmente, porque $d_{min}^2$ **es** el $E_d$ del BER.

**Espaciado uniforme y simétrico respecto de cero** porque maximiza $d_{min}$ a potencia media dada, y da media nula (si no, se gastaría potencia en una continua que no lleva información).

### Densidad espectral de potencia

$$S(f) = \frac{\sigma_a^2}{T_s}\,|P(f)|^2 \quad\Longrightarrow\quad \text{pulso rectangular} \to \operatorname{sinc}^2$$

**Nulos en $f_c\pm kD$** ($k=1,2,3\ldots$); lóbulo principal de $f_c-D$ a $f_c+D$, ancho $2D$. Al modular, la DEP de banda base se copia a $\pm f_c$ **y se divide por 4** (el $\tfrac12$ de amplitud al cuadrado). Eje vertical: **densidad** [W/Hz].

| Lóbulo | Altura relativa | En dB |
|---|---|---|
| Principal (~90% de la potencia) | $1$ | $0$ dB |
| 1er lateral | $0{,}047$ | $\mathbf{-13{,}3}$ **dB** |
| 2do lateral | $0{,}016$ | $-17{,}8$ dB |
| 3er lateral | $0{,}008$ | $-20{,}8$ dB |

---

## 8 · Espectro Expandido / OFDM

**Son dos sub-temas casi independientes.** DSSS: ganancia de procesamiento. OFDM: subportadoras ortogonales.

### DSSS — las 4 fórmulas

| | Fórmula | Notas |
|---|---|---|
| ● | $N = 2^L-1$ | Longitud de secuencia máxima de un LFSR de $L$ etapas [chips]. **El $-1$**: nunca incluye el estado todo-ceros |
| | $R_c = \dfrac{N}{T_{sec}}$ | Tasa de chips [chips/s]; $T_{sec}$ = período de la secuencia |
| ● | $G_p = \dfrac{R_c}{R_b} = \dfrac{B_{SS}}{B_{datos}}$ | **Ganancia de procesamiento** (siempre $>1$). Las dos formas son equivalentes: los 2 se cancelan |
| | $B_{SS} = 2R_c$, $\quad B_{datos}=2R_b$ | Nulo a nulo, DS-BPSK — **en DS-BPSK el chip hace de símbolo** |

**Qué significa $G_p$**: cuánto se ensancha el espectro y, equivalentemente, **cuánta ventaja se gana contra interferencia** — al despreader la señal útil se recomprime mientras el interferente se dispersa: $SNR_{out}=G_p\,SNR_{in}$.

**El patrón típico**: dan LFSR y período → sacar $R_c$ → sacar $G_p$ y $B$ → **rediseñar para un $G_p$ objetivo** manteniendo $R_b$, despejando al revés: $\boxed{R_c = G_p\cdot R_b}$. El precio: el $BW$ crece en la misma proporción — **$G_p$ se compra con espectro**.

° **FHSS / CDMA**: $G_{p,FHSS}\approx M/k$, $P_{hit}=k/M$ ($M$ canales, $k$ interferidos); señal CDMA del usuario $k$: $s_k(t)=A_kd_k(t)c_k(t)\cos(\omega_ct+\phi_k)$.

### OFDM — las 4 fórmulas

| | Fórmula | Notas |
|---|---|---|
| | $\text{bits/símbolo OFDM} = N_p\cdot\ell$ | Todas las subportadoras transmiten **en paralelo** |
| ● | $T_S = \dfrac{N_p\,\ell}{R_b}$ | Tiempo de símbolo OFDM. **No es libre: la fija el caudal** |
| ● | $\Delta f = \dfrac{1}{T_S}$ | **Espaciado — es la condición de ortogonalidad**, no una elección |
| | $B_T = N_p\cdot\Delta f$ | Ancho de banda total. También $N_p = B_T/\Delta f$ |
| | $f_k = f_c\pm\left(k+\tfrac12\right)\Delta f$, $\ k=0\ldots\tfrac{N_p}{2}-1$ | Posición de subportadoras ($N_p$ par). **Ninguna exactamente en $f_c$** |
| | $T_{CP} > \tau_{max}$, $\quad \eta_{CP} = \dfrac{T_S}{T_S+T_{CP}}$ | **Prefijo cíclico**: debe cubrir el delay spread. Overhead: WiFi ~80%, LTE ~93% |
| | $Y_k = H(f_k)X_k+N_k \ \Rightarrow\ \hat X_k = \dfrac{Y_k}{H(f_k)}$ | **Ecualización por subportadora**: una división compleja, trivial con CP |

**La cadena**: $R_b$ serie $\xrightarrow{S/P} N_p$ grupos de $\ell$ bits $\xrightarrow{\text{mapeo QAM}} N_p$ símbolos $\xrightarrow{\textbf{IFFT}}$ muestras $\xrightarrow{P/S}$ señal. En recepción: bajada a banda base → **FFT** sobre un período de símbolo → $N_p$ valores complejos → demapeo → P/S. El orden de los bits es **convención previa** (el índice $k$ *es* la posición) — no se transmite info extra. **Por eso el sincronismo es crítico**: errar la ventana o correrse una subportadora arruina el bloque entero.

**Por qué $\Delta f=1/T_S$**: dos subportadoras son ortogonales sobre $[0,T_S]$ si $(f_1-f_2)T_S$ es entero no nulo; el espaciado **mínimo** es el entero 1. O sea: **cada subportadora completa exactamente un ciclo más que su vecina por período de símbolo**. Con ese espaciado, cada una tiene un **nulo** en la frecuencia de todas las demás → se solapan sin estorbarse.

**Por qué conviene que cada subportadora sea lenta** (la comparación contra una sola portadora a igual tasa):

1. **ISI por multitrayecto — la razón central.** Un eco urbano de ~1 μs se superpone a ~2 símbolos si son de 0,625 μs (una portadora, 1024-QAM), pero es el **0,1%** de un símbolo OFDM de 1024 μs. **OFDM esquiva el problema en vez de resolverlo** — no hace falta ecualizador de arrastre.
2. **Cada subportadora ve un canal plano.** En $\Delta f$ (~1 kHz) el canal es esencialmente constante, así que actúa como **una multiplicación compleja**, corregible con **un ecualizador de un solo tap**. Reemplaza un ecualizador temporal complejo por $N_p$ multiplicaciones triviales.
3. **El prefijo cíclico sale barato**: una guarda de 10 μs cuesta ~1% sobre 1024 μs, y 1600% sobre 0,625 μs.
4. **Bit loading adaptativo** (water-filling, como ADSL) y **rechazo de interferencia de banda angosta** (mata unas pocas subportadoras, el resto sobrevive).

**El precio**: **PAPR alto** (suma coherente de muchas subportadoras), **sensibilidad a error de frecuencia** (rompe la ortogonalidad → ICI), **latencia**.

> **Con entrada constante (todo ceros) el espectro se vuelve de líneas**: todas las subportadoras transmiten siempre el mismo símbolo → señal **periódica** de período $T_S$ → $N_p$ **deltas** separadas $\Delta f$. ⚠️ `0000` **no es amplitud cero**: es un punto específico de la grilla, y ninguno de los 16 puntos está en el origen. Y en el tiempo es peor: los $N_p$ tonos se suman **en fase** en $t=0$, dando $\text{PAPR}=N_p$ (con 4096: **36,1 dB**) — un tren de pulsos angostísimos, inviable para cualquier amplificador. **Por eso los sistemas reales usan un scrambler.** La DEP $\propto\sigma_a^2$: **el espectro continuo de OFDM lo produce la información, no las portadoras.**

---

## 9 · La función $Q(x)$ — cómo evaluarla

**$Q(x)$ no tiene forma cerrada** — es la integral de cola de la gaussiana, sin primitiva elemental. **No se calcula: se lee.** **Se lee del ábaco de $Q(k)$**: última página, $Q(k)$ vs $k$ en escala logarítmica, con $k$ de 0 a 7. **Si no aparece, se puede pedir al equipo docente** — el reglamento habilita consultas.

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| $Q(x)$ | $0{,}5$ | $1{,}6{\times}10^{-1}$ | $2{,}3{\times}10^{-2}$ | $1{,}3{\times}10^{-3}$ | $3{,}2{\times}10^{-5}$ | $2{,}9{\times}10^{-7}$ | $10^{-9}$ | $10^{-12}$ |

**En sentido inverso** (dado un BER objetivo, hallar el $x$ necesario): $10^{-3}\to3{,}1$; $10^{-6}\to4{,}75$; $10^{-9}\to6{,}0$.

**Casio fx-991LAX (ClassWiz)**: Menú → **Distribución** → **DA normal** (Acumulada; ⚠️ **no** "DP normal", que es la densidad). Cargar **Inferior $=x$, Superior $=99$**, $\sigma=1$, $\mu=0$ → el resultado **es $Q(x)$ directo**. Verificación: Inferior $=3$ debe dar $1{,}3499\times10^{-3}$.

> ⚠️ **Nunca** calcular $\Phi(x)$ y restar $1-\Phi(x)$: para $x=5$, $\Phi=0{,}9999997133$ y al restar se pierden casi todos los dígitos. Ir directo por la cola.

**Otras salidas**: $Q(x)=\tfrac12\operatorname{erfc}\!\left(\tfrac{x}{\sqrt2}\right)$; asintótica para $x\gtrsim3$: $Q(x)\approx\dfrac{e^{-x^2/2}}{x\sqrt{2\pi}}$ (error ~4% en $x=4{,}4$).

**Estrategia**: usar **las dos fuentes** — leer el ábaco y confirmar con la calculadora. Leer mal una escala logarítmica es fácil.

---

## 10 · Herramientas matemáticas (transversal)

| Fórmula | Qué es |
|---|---|
| $X(f)=\displaystyle\int x(t)e^{-j2\pi ft}dt$ | Transformada de Fourier |
| $x(t)=\sum_n c_ne^{j2\pi nf_0t}$, $\ f_0=1/T_0$ | Serie de Fourier (señal periódica) |
| $\displaystyle\int\lvert x(t)\rvert^2dt = \int\lvert X(f)\rvert^2df$ | **Parseval** (conservación de energía) |
| $x_1(t)*x_2(t) \leftrightarrow X_1(f)X_2(f)$ | Teorema de convolución |
| $\hat X(f) = -j\operatorname{sgn}(f)X(f)$ | **Hilbert** — desfasaje de $90°$ |
| $x_a(t)=x(t)+j\hat x(t)$; $\ a(t)=\sqrt{x^2+\hat x^2}$ | Señal analítica → envolvente y fase instantánea |
| $\mathcal{H}\{m(t)\cos\omega_ct\} = m(t)\sin\omega_ct$ | **Teorema pasabanda** (requiere $f_c > W$) |
| $\operatorname{rect}(t/\tau) \leftrightarrow \tau\operatorname{sinc}(f\tau)$ | Par rect↔sinc (de acá salen todos los $\operatorname{sinc}$ del curso) |
| $\operatorname{sinc}(t/T)\leftrightarrow T\operatorname{rect}(fT)$ | El dual — **es el pulso que logra ISI cero en $R_s/2$ Hz** |
| $m(t)\cos\omega_ct \leftrightarrow \tfrac12[M(f{-}f_c)+M(f{+}f_c)]$ | Propiedad de modulación — **el $\tfrac12$ que genera el "factor 2"** |
| $\log_2 x = \dfrac{\log_{10}x}{\log_{10}2} = \dfrac{\ln x}{\ln 2}$ | Log base 2 en la calculadora |
| $X_{lineal} = 10^{X_{dB}/10}$ | dB → lineal (para Friis, Shannon, todo) |

**Criterio de Nyquist sin ISI**: por un canal pasabajos de ancho $B$ se pueden mandar como máximo $2B$ símbolos independientes por segundo ($R_s\leq2B \Rightarrow B_{min}=R_s/2$). **Es el teorema de muestreo dado vuelta**: un canal de ancho $B$ tiene **$2B$ grados de libertad por segundo**, y no se pueden especificar más números independientes que eso. Los dos "2" son duales: uno para **muestrear** ($f_s\geq2B$, muestras/ciclo), otro para **transmitir** ($R_s\leq2B$, símbolos/ciclo).

### Decibeles — cuándo $10\log$ y cuándo $20\log$

**Hay una sola regla: $10\log_{10}$ de una relación de POTENCIAS.** El 20 no es otra regla — aparece cuando **lo de adentro está al cuadrado** y el exponente sale afuera:

$$\boxed{10\log_{10}\big(X^2\big) = 20\log_{10}(X)}$$

Eso pasa por **dos motivos distintos**, y conviene no mezclarlos:

| Motivo | Cuándo | Ejemplo |
|---|---|---|
| **1. La magnitud es una amplitud** (tensión, campo) y $P\propto V^2$ | Te dan volts y querés dB de potencia | $10\log\dfrac{V_2^2}{V_1^2} = 20\log\dfrac{V_2}{V_1}$ |
| **2. La relación de potencias YA es un cuadrado** | La fórmula misma tiene un $(\cdot)^2$ | FSPL, $M^2$ de $SNR_Q$ |

**Los cuatro lugares del programa donde aparece el 20:**

| Dónde | De dónde sale el 20 |
|---|---|
| **FSPL** $=32{,}44+20\log f_{[MHz]}+20\log d_{[km]}$ | $L=(4\pi d/\lambda)^2$ — **motivo 2**, no es una amplitud |
| **$SNR_Q$ en dB** $= 10\log\dfrac{3M^2}{F_C^2} = 1{,}76+20\log M-20\log F_C$ | El $M^2$ y el $F_C^2$ |
| **El famoso $6{,}02\,n$** | Es literalmente eso: $20\log(2^n)=20n\log2 = 6{,}02n$. **Por eso cada bit da $+6$ dB y no $+3$** |
| Companding $\approx20\log\mu$ | Es un rango dinámico (relación de amplitudes) |

> ⚠️ **Todo lo demás va con $10\log$, sin excepción**: $F$ (cifra de ruido), $G$, $L_c$, Friis, SNR, $\gamma$, $E_b/N_0$, $G_p$, capacidades, potencias, PEP. **El chequeo rápido**: ¿lo de adentro está al cuadrado, o me dieron **volts**? → 20. ¿Me dieron **watts** o una relación de potencias? → 10.

**dBm y dBW** — siempre $10\log$, son potencias:

$$P_{dBm} = 10\log_{10}\!\left(\frac{P}{1\ \text{mW}}\right) \qquad P_{dBW} = 10\log_{10}\!\left(\frac{P}{1\ \text{W}}\right) \qquad P_{dBm} = P_{dBW}+30$$

⚠️ **Ojo con el denominador de dBm: es mW, no W.** Es el error de dedo típico.

| Potencia | dBm | Potencia | dBm |
|---|---|---|---|
| 1 mW | **0 dBm** | 5 µW | $10\log(5\times10^{-3}) = \mathbf{-23{,}0}$ dBm |
| 1 W | 30 dBm ($=0$ dBW) | $kT_0$ | $-174$ dBm/Hz |

> **dBm es un nivel ABSOLUTO** (referido a 1 mW); **dB es una RELACIÓN**. Por eso en el balance de enlace se mezclan sin problema — $\underbrace{P_{TX}}_{\text{dBm}} + \underbrace{G_{TX}-L_{FSPL}+G_{RX}}_{\text{dB}} = \underbrace{P_{RX}}_{\text{dBm}}$ — pero **restar dos dBm da dB**, y **sumar dos dBm no significa nada**.

---

## 12 · Constantes y valores típicos

| Constante / valor | Significado |
|---|---|
| $k = 1{,}38\times10^{-23}$ J/K | Constante de Boltzmann |
| $T_0 = 290$ K | Temperatura de referencia estándar (ruido) |
| $kT_0 = 4\times10^{-21}$ W/Hz $= -174$ dBm/Hz | **El número más útil de todo el tema de ruido** |
| $N_{dBm} = -174+10\log_{10}B+F_{dB}$ | Piso de ruido a $T_0$ |
| $\ln 2 = 0{,}693 \to -1{,}59$ dB | Límite absoluto de $E_b/N_0$ |
| $0$ dBW $= 30$ dBm | Conversión dBW ↔ dBm |
| 3 dB → 2 · 6 dB → 4 · 10 dB → 10 · 20 dB → 100 | Conversiones dB de memoria |
| $F_C=\sqrt2$ (senoidal), $\sqrt3$ (uniforme) | Factores de cresta usuales |
| $\eta_{AM}^{max} = 1/3 = 33{,}3\%$ | En $m=1$ |
| $SNR_{umbral}\approx10$ dB | Umbral AM / discriminador FM convencional |
| FM broadcast: $\Delta f=75$ kHz, $f_m=15$ kHz, $\beta=5$, $B_T=200$ kHz | Valores estándar de radio FM |
| PCM telefonía: $f_s=8$ kHz, $n=8$ bits, $R_b=64$ kbps | Estándar G.711 |
| CD audio: $f_s=44{,}1$ kHz, $n=16$ bits, estéreo | $R_b = 1{,}41$ Mbps |
| $\mu=255$ (USA/Japón), $A=87{,}6$ (Europa) | Companding (Ley μ / Ley A) |

---

## 13 · Errores frecuentes

**Transversales**

1. **Olvidar el factor de cresta** al calcular potencia desde una amplitud máxima. Aparece en AM, en PCM y en QAM.
2. **Convertir dB ↔ lineal en el momento equivocado.** Friis y Shannon-Hartley van **en lineal**; la división de $L_{TOTAL}$ entre secciones va **en dB**.
3. **Arrastrar un error** de un ítem al siguiente. El corrector lo marca ("arrastra error") pero **descuenta igual**. Si un ítem repite un dato que ya estaba, sospechá que quiere la **ruta independiente**.

**Por tema**

| Tema | El error |
|---|---|
| **AM** | El factor 2 del espectro ($A_c/2$ y $A_cm/4$) · sobremodulación multitono es $\sum m_i\leq1$ · $BW$ multitono es $2f_{m,max}$ · confundir $m$ (índice) con $m(t)$ |
| **FM** | Creer que **la potencia cambia** al modular (no cambia) · multiplicar $f_m$ por $n$ (no se toca) · confundir multiplicador con mezclador · en PM olvidar que $\Delta f$ depende de $f_m$ |
| **PCM** | Confundir $R_b$ con $R_s$ · confundir $R_s$ con $B$ (el 2 de banda base/pasabanda) · confundir $M$ con $M_{mod}$ |
| **Ruido** | Dividir la pérdida total en lineal en vez de en dB · olvidar que un cable tiene $F=L$ · sumar figuras de ruido en dB · confundir $F$ con $T_e$ |
| **Digital** | Confundir los tres anchos de banda ($2D$ / $D$ / $D(1+\alpha)$) · usar la amplitud máxima en vez del promedio de constelación · olvidar el $/2$ del portador |
| **TI** | Usar $\log_2M$ cuando **no** son equiprobables · meter la SNR en dB dentro de Shannon-Hartley · invertir la conclusión de factibilidad (**más** $BW$ que Shannon = factible) |
| **SS/OFDM** | Olvidar el $-1$ en $N=2^L-1$ · confundir $R_c$ con $R_b$ · poner una subportadora en $f_c$ |
