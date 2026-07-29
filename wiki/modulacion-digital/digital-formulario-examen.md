---
tags:
  - wiki/modulacion-digital
  - wiki/planificacion
curso: Sistemas de Comunicaciones
unidad: 6
---

# Modulación Digital — Formulario de examen (compacto)

> **Last verified:** 2026-07-27 | **Verified by:** analysis + patrón real de ejercicios en `exercises/finales/md/`

> **Para qué es esta nota**: versión operativa para resolver bajo reloj. Explicación conceptual completa en [[ask-fsk-psk|ASK, FSK, PSK]], [[modulacion-qam|Modulación QAM]] y [[probabilidad-error|Probabilidad de Error (BER)]].
>
> **Modulación Digital aparece en 40,5% de los 42 finales únicos.** Menos que PCM o AM/FM, pero sus fórmulas se reusan en Ruido/BER, así que rinde doble.

## Glosario de símbolos

| Símbolo | Nombre | Unidad | Notas |
|---|---|---|---|
| $M$ | Puntos de la **constelación** | conteo | 16-QAM → $M=16$. En PCM $M$ es otra cosa (niveles del ADC) |
| $\ell$ | **Bits por símbolo** | bits/símbolo | $\ell=\log_2M$. Es el $n$ de PCM pero para símbolos |
| $R_b$ | **Tasa de bits** | bps | Dato del enunciado o viene de PCM |
| $D$ | **Tasa de símbolos** (velocidad de señalización) | baudios | $D=R_b/\ell$. También se escribe $R_s$ |
| $\alpha$ | **Factor de roll-off** del coseno realzado | adimensional, $0\le\alpha\le1$ | $\alpha=0$ → Nyquist ideal |
| $B$ | Ancho de banda ocupado | Hz | Tres variantes: $2D$, $D$, $D(1+\alpha)$ |
| $B_N$ | Ancho de banda **equivalente de ruido** | Hz | Casi siempre lo da el enunciado |
| $f_c$ | Frecuencia de **portadora** | Hz | |
| $I$, $Q$ | Componentes **en fase** y **en cuadratura** | V | Coordenadas del punto de constelación |
| $\lvert s\rvert$ | **Magnitud del símbolo** | V | $=\sqrt{I^2+Q^2}$. Amplitud pico de la sinusoide transmitida |
| $a$ | **Unidad de grilla** de QAM | V | Niveles en $\pm a,\pm3a,\ldots$ ⚠️ Ningún símbolo *vale* $a$ |
| $A$ | **Radio** de la constelación PSK | V | Todos los símbolos valen $A$ |
| $d_{min}$ | **Distancia mínima** entre puntos | V | Lo que decide la inmunidad al ruido |
| $S$ | Potencia de **señal** | W | $S=\langle\lvert s\rvert^2\rangle/2$ |
| $N$ | Potencia de **ruido** | W | $N=N_0B_N$ |
| $N_0$ | **Densidad** espectral de ruido | W/Hz ($\equiv$ J) | |
| $E_b$ | **Energía por bit** | J/bit | $E_b=S/R_b$ |
| $T_b$ | Duración de un **bit** | s | $T_b=1/R_b$ |
| $T_s$ | Duración de un **símbolo** | s | $T_s=1/D$ |
| $P_e$ | Probabilidad de error (**BER**) | adimensional | |
| $Q(\cdot)$ | Función **Q** (cola de la gaussiana) | adimensional | Se lee del ábaco anexo |

> ⚠️ **Colisiones a vigilar**: [analysis]
> - **$M$ (aquí) vs $M$ (en PCM)** — constelación vs niveles del ADC. Por eso en la nota de PCM se lo llama $M_{mod}$ cuando aparecen juntos.
> - **$a$ vs $A$** — unidad de grilla (QAM) vs radio (PSK). Ver detalle más abajo.
> - **$T_b$ vs $T_s$** — duración de bit vs de símbolo. Se relacionan por $T_s = \ell\,T_b$.
> - **$N$ vs $N_0$** — potencia [W] vs densidad [W/Hz]. Se conectan multiplicando por un ancho de banda.

## Cadena de fórmulas

$$R_b\ [\text{bps}] \to \ell \to D\ [\text{baudios}] \to B\ [\text{Hz}] \to SNR \to BER$$

| # | Nombre | Fórmula | Qué es y para qué sirve |
|---|---|---|---|
| 1 | **Bits por símbolo** (orden de la modulación) | $\boxed{\ell = \log_2 M}$ | Cuántos bits codifica cada punto de la constelación. Define la modulación: QPSK → $\ell=2$; 16-QAM → $\ell=4$; 64-QAM → $\ell=6$. Unidad: bits/símbolo |
| 2 | **Tasa de símbolos** (velocidad de señalización) | $\boxed{D = \dfrac{R_b}{\ell}}$ | Cuántos símbolos por segundo salen al canal. **Es lo que determina el ancho de banda**, no $R_b$. Unidad: baudios. También se escribe $R_s$ |
| 3 | **Potencia de señal** | $\boxed{S = \dfrac{\langle\lvert s\rvert^2\rangle}{2}}$ | Potencia media transmitida. El $/2$ es pico→RMS del portador. $\langle\lvert s\rvert^2\rangle$ depende de la constelación (ver tabla abajo). Unidad: W (normalizada, $R=1$) |
| 4 | **Potencia de ruido** en la banda | $\boxed{N = N_0\,B_N}$ | Ruido total que entra al receptor. $N_0$ = densidad espectral de ruido [W/Hz], $B_N$ = ancho de banda equivalente de ruido. Unidad: W |
| 5 | **Energía por bit** | $\boxed{E_b = \dfrac{S}{R_b} = S\,T_b}$ | Energía que el transmisor gasta en cada bit: potencia $\times$ duración de bit ($T_b=1/R_b$). Unidad: **J/bit** $\left(\frac{\text{J/s}}{\text{bits/s}}\right)$ |
| 6 | **Relación $E_b/N_0$** | $\boxed{\dfrac{E_b}{N_0} = \dfrac{S}{R_b\,N_0}}$ *(directa)* $\boxed{\dfrac{E_b}{N_0} = SNR\cdot\dfrac{B}{R_b}}$ *(vía SNR)* | La métrica universal de calidad de un enlace digital — **es lo que entra en la fórmula de BER**. Adimensional (se suele dar en dB) |

> ⚠️ **Preferí siempre la ruta directa** $\frac{E_b}{N_0}=\frac{S}{R_bN_0}$: solo necesita potencia, tasa de bits y densidad de ruido — **ni ancho de banda ni SNR**. La ruta vía SNR sirve cuando te dan la SNR ya calculada, pero **arrastra cualquier error previo** y falla si el enunciado cambia $N_0$ entre ítems (que es exactamente lo que hace el ejercicio resuelto abajo, a propósito).

> **Unidades de $E_b/N_0$: adimensional** — y el porqué es que $N_0$ resulta ser una **energía**: [analysis]
> $$\frac{\text{W}}{\text{Hz}} = \frac{\text{J}/\text{s}}{1/\text{s}} = \text{J} \qquad\Longrightarrow\qquad \frac{E_b}{N_0} = \frac{[\text{J/bit}]}{[\text{J}]} \to \text{número puro}$$
>
> **Interpretación física**: $N_0$ es la potencia de ruido en 1 Hz de ancho de banda, y resolver 1 Hz requiere observar 1 segundo (Nyquist otra vez) — así que $N_0$ = potencia $\times$ 1 s = **energía de ruido por grado de libertad del canal**. Comparar $E_b$ (energía de señal por bit) contra $N_0$ (energía de ruido por dimensión) es comparar energía contra energía: por eso es *la* métrica justa para enlaces digitales.
>
> *(Nota de honestidad: acá las etiquetas semánticas —"por bit" y "por dimensión"— no se cancelan tan limpio como los bits/símbolo de la cadena PCM→Digital; lo que sí cierra sin discusión es el argumento **dimensional**: J sobre J. Eso es lo que habilita el dB.)*
>
> **Consecuencias prácticas**: se puede expresar en **dB** (solo los números puros admiten logaritmo); es el argumento de $Q(\cdot)$, que también requiere entrada adimensional; y el límite de Shannon $E_b/N_0 > \ln 2 = -1{,}59$ dB es un valor de esta misma magnitud.

**Potencia según la constelación** (el $\langle\lvert s\rvert^2\rangle$ de la fórmula 3):

| Constelación | $\langle\lvert s\rvert^2\rangle$ | Potencia $S=\langle\lvert s\rvert^2\rangle/2$ |
|---|---|---|
| **$M$-QAM cuadrada** (niveles $\pm a,\pm3a,\ldots$) | $\dfrac{2(M-1)}{3}a^2$ | $\boxed{S = \dfrac{(M-1)a^2}{3}}$ |
| **$M$-PSK** (radio $A$, envolvente constante) | $A^2$ | $\boxed{S = \dfrac{A^2}{2}}$ |

> ⚠️ **El $a$ de QAM y el $A$ de PSK NO son lo mismo** — las letras distintas (minúscula vs mayúscula) lo marcan a propósito: [analysis]
>
> | | QAM: $a$ | PSK: $A$ |
> |---|---|---|
> | Qué es | **Unidad de la grilla** — mitad del espaciado entre niveles adyacentes | **Radio de la circunferencia** |
> | Relación con los símbolos | **Ningún símbolo tiene magnitud $a$** (los más cercanos están en $(\pm a,\pm a)$, con $\lvert s\rvert=a\sqrt2$) | **Todos los símbolos tienen magnitud $A$** |
> | $d_{min}$ | $2a$ | $2A\sin(\pi/M)$ |
>
> $a$ es una **unidad de coordenadas** (parámetro de la grilla); $A$ es una **magnitud real de los símbolos**. Por eso las fórmulas de potencia se ven tan distintas: miden cosas diferentes.
>
> **Chequeo con QPSK** (que es a la vez 4-QAM y 4-PSK, así que ambas fórmulas deben coincidir):
> $$\text{4-QAM: } \tfrac{2(4-1)}{3}a^2 = 2a^2 \qquad\text{4-PSK: } A^2 \qquad\Longrightarrow\qquad \boxed{A = a\sqrt2}$$
> Y se verifica geométricamente: los puntos $(\pm a,\pm a)$ están sobre una circunferencia de radio $\sqrt{a^2+a^2}=a\sqrt2$ ✓
>
> **Para comparar $M$-QAM contra $M$-PSK con $M>4$** son constelaciones distintas, así que no hay relación automática — hay que **imponerla** según el criterio del enunciado. Ej. "a igualdad de amplitud máxima" en 16-QAM vs 16-PSK: $A = 3a\sqrt2 \Rightarrow a = 0{,}236A$.

> **A dBm** (lo piden explícitamente en 4 ejercicios del corpus): $P_{dBm} = 10\log_{10}\!\left(\dfrac{P}{1\text{ mW}}\right)$. Ojo con el denominador — es **mW**, no W. Para pasar de dBW a dBm se suman 30 dB.

> **El error clásico**: calcular $S$ usando la **amplitud máxima** de la constelación en vez del promedio, u olvidar el $/2$ del portador. En 16-QAM eso da $18a^2$ (máximo) o $10a^2$ (promedio sin $/2$) en vez del correcto $5a^2$ — ver el ejercicio resuelto abajo, donde los dos estudiantes perdieron el punto justamente ahí.

> **¿Por qué $E_b/N_0$ y no directamente SNR?** Porque la SNR depende del ancho de banda elegido, así que **no permite comparar modulaciones distintas de forma justa**. $E_b/N_0$ normaliza por bit y por densidad de ruido, y queda independiente de $B$ y de $R_b$ — por eso todas las curvas de BER se grafican contra $E_b/N_0$ y no contra SNR. La fórmula 5 es el puente entre ambas. Detalle en [[../conceptos-integradores/eb-n0-vs-snr|$E_b/N_0$ vs SNR]]. [analysis]

### ¿$\ell$ es lo mismo que el $n$ de PCM?

Misma **fórmula**, cosas **distintas** — y los símbolos distintos ($n$ vs $\ell$, ambos usados así por la cátedra) están justamente para no mezclarlas: [analysis]

| | PCM | Digital |
|---|---|---|
| Símbolo | $n$ | $\ell$ |
| Qué cuenta $M$ | **Niveles del ADC** | **Puntos de la constelación** |
| Unidad | bits/**muestra** | bits/**símbolo** |
| Etapa | Digitalización (fuente) | Transmisión |

**Son números independientes**: en el ejercicio del CD-Audio, $n=16$ bits/muestra (ADC de 65536 niveles); si eso se transmite en QPSK, $\ell=2$ bits/símbolo. Nada obliga a que coincidan, y en `F_Comu_2024-11-14_res.md` aparecen los dos en el mismo problema ($M=256$ niveles → $n=8$; QPSK → $\ell=2$).

**Dónde se conectan — la cadena completa:**

$$\frac{\text{muestras}}{\text{s}} \xrightarrow{\ \times n\ } \frac{\text{bits}}{\text{s}} \xrightarrow{\ \div\ell\ } \frac{\text{símbolos}}{\text{s}} \xrightarrow{\ \text{Nyquist}\ } \text{Hz}$$

$$f_s \xrightarrow{\ \times n\ } R_b \xrightarrow{\ \div\ell\ } D \xrightarrow{\ \times1\ \text{(pasabanda)}\ } B$$

$n$ **multiplica** al entrar y $\ell$ **divide** al salir: los dos son factores de conversión del mismo tipo ("bits por algo"), actuando en etapas distintas y en direcciones opuestas — $n$ convierte muestras→bits, $\ell$ convierte bits→símbolos. Ver la contabilidad de unidades completa en [[../modulacion-pulsos/pcm-formulario-examen#Cómo funcionan las unidades en toda la cadena|PCM — Cómo funcionan las unidades]].

## Los tres anchos de banda — no confundirlos

Los finales piden los tres y son distintos. Confundirlos es el error más frecuente:

| Cuál                       | Fórmula           | Cuándo se usa                                                                                   |
| -------------------------- | ----------------- | ----------------------------------------------------------------------------------------------- |
| **Nulo a nulo**            | $B = 2D$          | Pulso rectangular, ancho del lóbulo principal. **Lo piden explícitamente 4 veces en el corpus** |
| **Mínimo (Nyquist ideal)** | $B = D$           | Cuando dice "ancho de banda mínimo ideal" ($\alpha=0$)                                          |
| **Con roll-off**           | $B = D(1+\alpha)$ | Coseno realzado real; el enunciado da $\alpha$                                                  |

Ver la justificación del $B=D$ pasabanda en [[../modulacion-pulsos/pcm-formulario-examen#Justificación del paso $R_s \to B_{min}$ (criterio de Nyquist sin ISI)|criterio de Nyquist sin ISI]] — es la misma relación, con $D$ en lugar de $R_s$.

### De dónde sale el $2D$, y las unidades del paso $D \to B$

**Origen del nulo a nulo**: un pulso rectangular de duración $T_s=1/D$ tiene espectro $\text{sinc}(fT_s)$, con **primer nulo** donde $f\,T_s=1$, o sea $f=1/T_s=D$. En pasabanda ese lóbulo queda centrado en $f_c$ y se extiende $D$ hacia cada lado → ancho total $2D$. [analysis]

**La conversión de unidades**: $D$ está en símbolos/s y $B$ en ciclos/s, así que **tiene que haber un factor de conversión** — y lo hay, solo que vale 1 y por eso no se escribe:

$$f_0 = \kappa\cdot\frac{1}{T_s}, \qquad \kappa = 1\ \frac{\text{ciclo}}{\text{símbolo}}$$

**Contenido físico de $\kappa$**: en la frecuencia del primer nulo entra **exactamente un ciclo de la sinusoide en una duración de símbolo**. Eso es lo que hace que los números coincidan; es invisible en la fórmula solo porque su valor numérico es 1.

La contabilidad completa tiene entonces **tres** factores, no dos:

$$B_{n\text{-}n} = \underbrace{2}_{\substack{\text{lados del lóbulo} \\ \text{adimensional}}} \times \underbrace{1\ \tfrac{\text{ciclo}}{\text{símbolo}}}_{\kappa,\ \text{conversión}} \times \underbrace{D\ \tfrac{\text{símbolos}}{\text{s}}}_{\text{tasa}} = 2D\ \left[\tfrac{\text{ciclos}}{\text{s}}\right]$$

**Y esto unifica los tres anchos de banda** — son la misma relación con distinto $\kappa$ total:

| Relación | $\kappa$ total [ciclos/símbolo] | De dónde sale |
|---|---|---|
| $B = D/2$ (Nyquist banda base) | $1/2$ | los 2 símbolos/ciclo de Nyquist, invertidos |
| $B = D$ (Nyquist pasabanda) | $1$ | anclaje puro: 1 ciclo/símbolo |
| $B = 2D$ (nulo a nulo, pulso rectangular) | $2$ | anclaje $\times$ 2 lados del lóbulo |

> **Ojo con los dos "2" distintos**: el de Nyquist ($R_s=2B$) es **2 símbolos/ciclo**, un factor de conversión con contenido físico; el de nulo a nulo ($B=2D$) es **2 lados**, pura simetría geométrica. Se confunden fácil porque ambos relacionan $B$ con $D$. [analysis]
>
> **Consecuencia útil**: $B_{n\text{-}n} = 2\,B_{min}$ en pasabanda. Esa duplicación es **el precio de usar pulsos rectangulares** en vez de pulsos sinc — rectangular en tiempo se desparrama en frecuencia (sinc), mientras que sinc en tiempo da un rectángulo compacto en frecuencia. Mismo trade-off tiempo-frecuencia de siempre.

## BER — tabla completa

| Modulación | $P_e$ |
|---|---|
| **BPSK** | $Q\!\left(\sqrt{2E_b/N_0}\right)$ |
| **QPSK** | $Q\!\left(\sqrt{2E_b/N_0}\right)$ — **igual que BPSK** |
| **$M$-PSK** | $\approx Q\!\left(\sqrt{2E_b/N_0}\,\sin(\pi/M)\right)$ |
| **$M$-QAM** | $\approx 4\,Q\!\left(\sqrt{3E_b/\big[(M-1)N_0\big]}\right)$ |
| **FSK coherente** | $Q\!\left(\sqrt{E_b/N_0}\right)$ |
| **FSK no coherente** | $\tfrac12 e^{-E_b/2N_0}$ |
| **DPSK** | $\tfrac12 e^{-E_b/N_0}$ |

*(Versiones de la cátedra, ver [[../resumenes/modulacion-digital-unidad6|Resumen Unidad 6]]. Existen formas más precisas con prefactores $\frac{4}{\ell}(1-\frac{1}{\sqrt M})$ para QAM y $\frac{2}{\ell}$ para PSK, pero para el examen conviene usar estas.)*

**Dos lecturas conceptuales que preguntan:**

- **BPSK y QPSK dan lo mismo por bit** — QPSK transmite el doble de bits en el mismo ancho de banda **sin penalidad de BER**. Por eso se usa tanto.
- **Las no coherentes (FSK no coh., DPSK) tienen forma exponencial**, no $Q(\cdot)$ — y pagan ~3 dB de penalidad frente a sus versiones coherentes, a cambio de no necesitar recuperación de portadora.
- **Al subir $M$**: se gana eficiencia espectral ($\ell$ bits/símbolo) pero **empeora la BER** para el mismo $E_b/N_0$ — los puntos quedan más juntos. Ver [[constelaciones|Constelaciones]].

### La forma general con filtro acoplado: energía diferencia $E_d$

Todas las fórmulas de BER de la tabla son **casos particulares** de un solo resultado. Con filtro acoplado, la probabilidad de error depende únicamente de la **energía de la señal diferencia** entre los dos símbolos: [analysis]

$$\boxed{P_e = Q\!\left(\sqrt{\frac{E_d}{2N_0}}\right)}, \qquad \boxed{E_d = \int_0^{T_b}\big|s_1(t)-s_0(t)\big|^2dt}$$

**Es la forma que dan los enunciados** cuando el ejercicio es de banda base con NRZ.

| Señalización | $s_1,\ s_0$ | $E_d$ | $S$ (potencia media) | $E_d$ en función de $E_b$ | $P_e$ |
|---|---|---|---|---|---|
| **Antipodal** (polar NRZ, BPSK) | $+V,\ -V$ | $4V^2T_b$ | $V^2$ | $\boxed{4E_b}$ | $Q\!\left(\sqrt{\tfrac{2E_b}{N_0}}\right)$ |
| **Unipolar** (NRZ, OOK) | $V,\ 0$ | $V^2T_b$ | $\boxed{\dfrac{V^2}{2}}$ | $\boxed{2E_b}$ | $Q\!\left(\sqrt{\tfrac{E_b}{N_0}}\right)$ |
| **Ortogonal** (FSK coherente) | ortogonales | $2E_b$ | — | $2E_b$ | $Q\!\left(\sqrt{\tfrac{E_b}{N_0}}\right)$ |

**Fórmulas útiles para unipolar NRZ** (el caso que piden en banda base):

$$\boxed{S = \frac{V^2}{2}} \qquad \boxed{E_d = V^2T_b = 2S\,T_b = \frac{2S}{R_b}}$$

> ### $E_b$ vs $E_d$ — no son lo mismo
>
> | | $E_b$ | $E_d$ |
> |---|---|---|
> | **Qué es** | Energía **por bit** que gasta el transmisor | Energía de la **señal diferencia** entre símbolos |
> | **Fórmula** | $E_b = S\,T_b = \dfrac{S}{R_b}$ | $E_d = \int_0^{T_b}\lvert s_1-s_0\rvert^2dt$ |
> | **Mide** | **Costo** energético | **Distinguibilidad** |
>
> **Cómo se relacionan con el BER — en dos niveles, no en competencia**: [analysis]
>
> - **$E_d$ es la cantidad fundamental**: una sola fórmula, $P_e=Q\!\left(\sqrt{E_d/2N_0}\right)$, válida para **cualquier** señalización
> - **$E_b$ funciona una vez fijado el esquema**, porque ahí $E_d = k\,E_b$ con $k$ conocido
>
> **Y las distintas fórmulas de la [[#BER — tabla completa|tabla de BER]] SON los distintos $k$** — no son fórmulas independientes:
>
> | Esquema | $k=E_d/E_b$ | Sustituyendo en $Q\!\left(\sqrt{E_d/2N_0}\right)$ | Queda |
> |---|---|---|---|
> | BPSK/QPSK | **4** | $Q\!\left(\sqrt{4E_b/2N_0}\right)$ | $Q\!\left(\sqrt{2E_b/N_0}\right)$ ✓ |
> | Unipolar / FSK coh. | **2** | $Q\!\left(\sqrt{2E_b/2N_0}\right)$ | $Q\!\left(\sqrt{E_b/N_0}\right)$ ✓ |
>
> **Por qué la tabla se escribe en $E_b$ y no en $E_d$**: porque $E_b$ es lo que **cuesta**, así que permite comparar esquemas de forma justa — el mismo motivo por el que las curvas de BER se grafican contra $E_b/N_0$.
>
> **Y por qué $E_d$ es el que manda conceptualmente**: el trabajo del receptor es **distinguir** $s_1$ de $s_0$. No importa cuánta energía tiene cada símbolo, sino **qué tan diferentes son entre sí** — dos símbolos enormes pero casi idénticos son difíciles de distinguir; dos chicos pero opuestos son fáciles. El cociente $k=E_d/E_b$ mide la **eficiencia del esquema para convertir energía en distinguibilidad**: 4 es el máximo binario (antipodal), 2 el de unipolar/ortogonal — de ahí los 3 dB.

### Receta para una señalización que NO esté en la tabla

Si el enunciado define una señalización distinta, **no hace falta memorizar su fórmula** — se deduce en 4 pasos:

1. **$E_d = \displaystyle\int_0^{T_b}\big|s_1(t)-s_0(t)\big|^2dt$** — energía de la diferencia
2. **$E_b = \dfrac{E_1+E_0}{2}$** (símbolos equiprobables), con $E_i=\int|s_i|^2dt$ — energía media por bit
3. **$k = E_d/E_b$**
4. **$P_e = Q\!\left(\sqrt{\dfrac{k\,E_b}{2N_0}}\right)$**

**Ejemplo A — Polar RZ** (pulso solo en la primera mitad del bit): $s_1=+V$ y $s_0=-V$ durante $T_b/2$, luego 0.

La diferencia de señales vale $2V$ en la primera mitad y **cero** en la segunda (ahí ambos símbolos son 0), así que integrando sobre **todo $T_b$**:

$$E_d = \int_0^{T_b}\lvert s_1-s_0\rvert^2dt = \underbrace{\int_0^{T_b/2}(2V)^2dt}_{2V^2T_b} + \underbrace{\int_{T_b/2}^{T_b}0\,dt}_{0} = 2V^2T_b$$

$$E_b = \frac{E_1+E_0}{2} = \frac{V^2T_b/2 + V^2T_b/2}{2} = \frac{V^2T_b}{2}$$

$$k = \frac{2V^2T_b}{V^2T_b/2} = 4 \quad\Rightarrow\quad P_e = Q\!\left(\sqrt{\frac{2E_b}{N_0}}\right)$$

**Mismo BER que BPSK.** Resultado que sorprende y vale entenderlo: acortar el pulso **no empeora la BER** a igual $E_b$ — solo **duplica el ancho de banda** (porque $T$ del pulso se redujo a la mitad). El precio de RZ es espectral, no de error.

**Ejemplo B — Unipolar con offset** ($s_1=V$, $s_0=V/2$): un esquema mal diseñado, para ver hasta dónde llega el método.

$$E_d = \left(V-\tfrac{V}{2}\right)^2T_b = \frac{V^2T_b}{4} \qquad E_b = \frac{V^2T_b + V^2T_b/4}{2} = \frac{5V^2T_b}{8}$$

$$k = \frac{V^2T_b/4}{5V^2T_b/8} = 0{,}4 \quad\Rightarrow\quad P_e = Q\!\left(\sqrt{\frac{0{,}2\,E_b}{N_0}}\right)$$

**10 dB peor que antipodal** ($2E_b/N_0$ contra $0{,}2E_b/N_0$ → factor 10). La razón: casi toda la energía se va en un **offset de continua común a los dos símbolos**, que no aporta nada a distinguirlos. Es la misma lección que la portadora en AM — potencia gastada en algo que no lleva información.

**Ejemplo C — NRZ, verificando la receta contra la tabla.** Los dos formatos NRZ ya están en la tabla; aplicar la receta debe reproducirlos (buen chequeo de que el método está bien usado).

**C1 · Polar NRZ (antipodal)**: $s_1=+V$, $s_0=-V$, ambos durante **todo** $T_b$.

$$E_d = \int_0^{T_b}\big(V-(-V)\big)^2dt = 4V^2T_b \qquad E_b = \frac{V^2T_b+V^2T_b}{2} = V^2T_b$$

$$k = \frac{4V^2T_b}{V^2T_b} = 4 \quad\Rightarrow\quad P_e = Q\!\left(\sqrt{\frac{2E_b}{N_0}}\right) \ ✓\ \text{(coincide con la tabla)}$$

**C2 · Unipolar NRZ** (el caso de los ejercicios de banda base): $s_1=V$, $s_0=0$, durante todo $T_b$.

$$E_d = \int_0^{T_b}(V-0)^2dt = V^2T_b \qquad E_b = \frac{V^2T_b+0}{2} = \frac{V^2T_b}{2}$$

$$k = \frac{V^2T_b}{V^2T_b/2} = 2 \quad\Rightarrow\quad P_e = Q\!\left(\sqrt{\frac{E_b}{N_0}}\right) \ ✓$$

> Notar que de $E_b = V^2T_b/2$ sale directo $\boxed{S = \dfrac{E_b}{T_b} = \dfrac{V^2}{2}}$ — la fórmula de potencia media de unipolar. **Todo sale de la misma receta**, no hay que memorizarla aparte.

> ⚠️ **Sutileza entre A y C1** (ambos con $k=4$): **mismo $k$ no significa misma performance a igual amplitud $V$.** Para el mismo $V$, RZ tiene $E_b = V^2T_b/2$ y NRZ tiene $E_b=V^2T_b$ — o sea RZ gasta **la mitad** de energía por bit. Lo que dice $k=4$ es que **a igual $E_b$ rinden idéntico**; para llegar a ese mismo $E_b$, RZ necesita $V_{RZ}=\sqrt2\,V_{NRZ}$. [analysis]
>
> ### La unificación: $E_d = d_{min}^2$
>
> $E_d$ es literalmente el **cuadrado de la distancia mínima** en el espacio de señales:
> $$E_d = \|s_1-s_0\|^2 = d_{min}^2$$
> Con lo cual **las tres formas del BER son la misma fórmula**:
> $$P_e = Q\!\left(\sqrt{\frac{E_d}{2N_0}}\right) = Q\!\left(\frac{d_{min}}{\sqrt{2N_0}}\right) = Q\!\left(\frac{d_{min}}{2\sigma}\right), \qquad \sigma^2=\frac{N_0}{2}$$
>
> **Y eso cierra el círculo con la comparación 16-QAM vs 16-PSK**: ahí se concluyó que *"lo que decide la inmunidad al ruido es $d_{min}$, no la potencia"*. Acá se ve **por qué es literalmente cierto** — $d_{min}^2$ **es** el $E_d$ que entra en la fórmula del BER. Toda la teoría de constelaciones y toda la de BER binario son la misma cosa vista desde dos lados.
>
> **Verificación de consistencia**: con $E_d=2E_b$ (unipolar), $P_e = Q\left(\sqrt{\frac{2E_b}{2N_0}}\right)=Q\left(\sqrt{\frac{E_b}{N_0}}\right)$ ✓ — coincide con la tabla de BER de arriba. Con $E_d=4E_b$ (antipodal): $Q\left(\sqrt{\frac{4E_b}{2N_0}}\right)=Q\left(\sqrt{\frac{2E_b}{N_0}}\right)$ ✓

> **El límite absoluto de Shannon** (piso de $E_b/N_0$, válido para *cualquier* esquema):
> $$\boxed{\frac{E_b}{N_0} > \ln 2 = -1{,}59\text{ dB}}$$
> Por debajo de eso **no hay comunicación confiable posible**, ni con ancho de banda infinito ni con la mejor codificación. Derivación paso a paso en [[../teoria-informacion/ti-formulario-examen|TI — Límite de Shannon]].

### Cómo se evalúa $Q(x)$ en el examen

**$Q(x)$ no tiene forma cerrada** — es la integral de cola de la gaussiana, sin primitiva elemental. No se calcula: **se lee de una tabla o ábaco**.

> ✅ **Los finales traen el ábaco anexado.** Confirmado en `F_Comu_2019-09-24` y `F_Comu_2022-02-16`: última página con carta de $Q(k)$ vs $k$ en escala logarítmica, eje $k$ de 0 a 7 y $Q(k)$ de $10^{-12}$ a 1. **No hay que memorizar la tabla** — pero sí conviene tener valores ancla para verificar que se está leyendo bien el gráfico.

**Valores ancla** (para chequear la lectura del ábaco):

| $x$ | $Q(x)$ |
|---|---|
| 0 | $0{,}5$ |
| 1 | $1{,}6\times10^{-1}$ |
| 2 | $2{,}3\times10^{-2}$ |
| 3 | $1{,}3\times10^{-3}$ |
| 4 | $3{,}2\times10^{-5}$ |
| 5 | $2{,}9\times10^{-7}$ |
| 6 | $10^{-9}$ |
| 7 | $10^{-12}$ |

**En sentido inverso** (dado un BER objetivo, hallar el $x$ necesario) — sale seguido:

| BER objetivo | $x$ requerido |
|---|---|
| $10^{-3}$ | $3{,}1$ |
| $10^{-6}$ | $4{,}75$ |
| $10^{-9}$ | $6{,}0$ |

**Con calculadora científica — receta para la Casio fx-991LAX** (ClassWiz, la que se va a usar):

1. Menú → **Distribución**
2. Elegir **DA normal** (Distribución Acumulada). ⚠️ **No** "DP normal", que es la *densidad* — la altura de la campana, no el área
3. Cargar: **Inferior** $=x$, **Superior** $=99$ (hace de infinito), $\sigma=1$, $\mu=0$
4. El resultado **es $Q(x)$ directo**

> **Verificación**: con Inferior $=3$ debe dar $1{,}3499\times10^{-3}$. [analysis]
>
> ⚠️ **Detalle de precisión que importa**: cargar siempre Inferior $=x$, Superior $=99$ — **nunca** calcular $\Phi(x)$ (Inferior $=-99$) y después restar $1-\Phi(x)$. Para $x=5$, $\Phi(5)=0{,}9999997133$: al restar de 1 se pierden casi todos los dígitos significativos. Yendo directo por la cola sale con precisión completa ($2{,}87\times10^{-7}$). Con BERs de $10^{-6}$ o $10^{-9}$ es justo el régimen donde este problema muerde.
>
> *(En modelos viejos fx-991ES con funciones P/Q/R en modo STAT hay una trampa extra: la "$Q(t)$" de Casio es el área de $0$ a $t$, **no** nuestra $Q$ — ahí hay que usar $R(t)$. La ClassWiz usa el menú Distribución y evita esa confusión.)*

**Otras salidas:**
- **Si tiene $\operatorname{erfc}$**: $\boxed{Q(x) = \tfrac12\operatorname{erfc}\!\left(\tfrac{x}{\sqrt2}\right)}$
- **Aproximación asintótica** (buena para $x\gtrsim3$): $Q(x)\approx\dfrac{e^{-x^2/2}}{x\sqrt{2\pi}}$ — con $x=4{,}42$ da $5{,}2\times10^{-6}$ contra el valor real $\approx5\times10^{-6}$, error del 4%

**Estrategia recomendada**: usar **las dos fuentes**. Leer el ábaco (rápido, y es lo que la cátedra provee) y confirmar con la calculadora. Leer mal una escala logarítmica es fácil, y dos fuentes independientes lo detectan.

## Cómo se arman las constelaciones (de dónde salen las coordenadas)

No hay que memorizar cada constelación — hay una regla fija. [analysis]

### QAM cuadrada ($M=4,16,64,256\ldots$)

Grilla $L\times L$ con $L=\sqrt M$ niveles por eje, **uniformemente espaciados y simétricos respecto de cero**, lo que los deja en **múltiplos impares** de $a$:

$$\pm a,\ \pm3a,\ \pm5a,\ \ldots,\ \pm(L-1)a$$

| $M$ | $L=\sqrt M$ | Niveles por eje |
|---|---|---|
| 4 (QPSK) | 2 | $\pm a$ |
| 16 | 4 | $\pm a,\pm3a$ |
| 64 | 8 | $\pm a,\pm3a,\pm5a,\pm7a$ |
| 256 | 16 | $\pm a,\ldots,\pm15a$ |

**Por qué así**: espaciado uniforme **maximiza la distancia mínima** para una potencia media dada (o sea minimiza la BER), y la simetría respecto de cero da **media nula** — si no, se gastaría potencia en una componente de continua que no lleva información.

### Cómo sacar el valor de $a$

Del dato que dé el enunciado, que es siempre uno de estos tres:

| Si el enunciado da… | Relación | Despeje |
|---|---|---|
| **Amplitud máxima** (punto esquina) | $\lvert s\rvert_{max} = (L-1)a\sqrt2$ | $a = \dfrac{\lvert s\rvert_{max}}{(L-1)\sqrt2}$ |
| **Potencia media** | $\langle\lvert s\rvert^2\rangle = \dfrac{2(M-1)}{3}a^2$ | $a=\sqrt{\dfrac{3\langle\lvert s\rvert^2\rangle}{2(M-1)}}$ |
| **Distancia mínima** $d_{min}$ | $d_{min} = 2a$ | $a = d_{min}/2$ |

### PSK — distinto, y más simple

Los puntos van **sobre una circunferencia** de radio $A$, a ángulos $2\pi k/M$:

$$s_k = \Big(A\cos\tfrac{2\pi k}{M},\ A\sin\tfrac{2\pi k}{M}\Big), \qquad d_{min} = 2A\sin\tfrac{\pi}{M}$$

**Todos los puntos tienen la misma magnitud $A$** → envolvente constante. Consecuencia práctica: en PSK **no hay factor de cresta de constelación** ($\langle\lvert s\rvert^2\rangle = A^2$ directo), a diferencia de QAM. Por eso PSK se usa donde el amplificador trabaja saturado (enlaces satelitales) y QAM donde importa más la eficiencia espectral.

*(QAM no cuadrada — $M=8,32,128$ — usa constelaciones en cruz; no aparecieron en el corpus de finales.)*

### Receta para el examen

1. Identificar $M$ y si es QAM o PSK
2. QAM: $L=\sqrt M$, niveles $\pm a,\pm3a,\ldots,\pm(L-1)a$
3. Sacar $a$ del dato dado (tabla de arriba)
4. Potencia: $\langle\lvert s\rvert^2\rangle=\frac{2(M-1)}{3}a^2$, y después **dividir por 2** (pico→RMS del portador)

Ver también [[constelaciones|Constelaciones]] para los diagramas I/Q.

## Ejercicio resuelto — 16-QAM (`F_Comu_2026-02-26_res.md`)

> ⚠️ **Los dos estudiantes que rindieron este ejercicio lo reprobaron** (1,5/2,5 y 0,75/2,5). Vale la pena estudiar dónde fallaron.

**Enunciado**: señal digital pasabanda 16-QAM, $f_c=50$ MHz, amplitud máxima $3\sqrt2$ mV (pico), símbolos equiprobables, $R_b = 256$ kbps, $N_0 = 4\times10^{-14}$ W/Hz.

**a) Ancho de banda de nulo a nulo**

$$\ell = \log_2 16 = 4 \ \Rightarrow\ D = \frac{256\text{k}}{4} = 64\text{ kbaudios} \ \Rightarrow\ \boxed{B_{n\text{-}n} = 2D = 128\text{ kHz}}$$

**b) Densidad espectral de potencia**

Lóbulo principal centrado en $f_c$, con **nulos en $f_c\pm64$ kHz, $\pm128$ kHz, $\pm192$ kHz** (múltiplos de $D$). Forma $\text{sinc}^2$, típica de señalización pasabanda con pulso rectangular.

> **Justificación completa de la DEP** (no está cubierto en otra nota de la vault — `densidad-espectral-potencia.md` trata Wiener-Khinchin en general, no este caso). [analysis]
>
> **¿Qué hay en el eje vertical?** **Densidad espectral de potencia**, en W/Hz (o V²/Hz si es normalizada) — es decir, **potencia por unidad de ancho de banda**, no amplitud ni potencia. Integrar la curva sobre toda la frecuencia devuelve la potencia total $S$. Por eso la unidad tiene "/Hz": es una densidad, igual que $N_0$ del ruido.
>
> **¿Por qué sinc — y por qué al cuadrado?** La señal es una secuencia *aleatoria* de símbolos, cada uno con forma de pulso $p(t)$. Para símbolos independientes y equiprobables:
> $$S(f) = \frac{\sigma_a^2}{T_s}\,|P(f)|^2$$
> con $P(f)=\mathcal F\{p(t)\}$ y $\sigma_a^2$ la varianza de los símbolos. La cadena es:
>
> | Paso | Resultado |
> |---|---|
> | Pulso **rectangular** de duración $T_s$ en el tiempo | $p(t)$ |
> | Su transformada de Fourier | $P(f)=A\,T_s\operatorname{sinc}(fT_s)$ → **sinc** |
> | La DEP es $\|P(f)\|^2$ (magnitud al cuadrado, porque es potencia) | $\propto\operatorname{sinc}^2(fT_s)$ → **sinc²** |
>
> O sea: **sinc** aparece por ser la transformada del rectángulo; **el cuadrado** aparece porque la DEP es una magnitud de potencia. Al modular, esa DEP de banda base se copia a $\pm f_c$ y **se divide por 4**: $S_{pb}(f)=\tfrac14[S_{bb}(f-f_c)+S_{bb}(f+f_c)]$.
>
> **¿Por qué $\tfrac14$ y no $\tfrac12$?** Porque **el $\tfrac12$ es de amplitud y la DEP es potencia** — se eleva al cuadrado:
> $$\mathcal F\{m(t)\cos(2\pi f_ct)\} = \tfrac12\big[M(f-f_c)+M(f+f_c)\big] \ \longrightarrow\ \left(\tfrac12\right)^2 = \tfrac14$$
> La propiedad de modulación pone $\tfrac12$ en **cada copia** (viene de Euler: el coseno son dos exponenciales, cada una con la mitad). Como la DEP va con $|\cdot|^2$, ese $\tfrac12$ se vuelve $\tfrac14$.
>
> **Chequeo por conservación de potencia** — si fuera $\tfrac12$ por copia la potencia total quedaría igual que en banda base, lo cual es falso:
> $$\int S_{pb}(f)\,df = \tfrac14P_m + \tfrac14P_m = \frac{P_m}{2}$$
> Dos copias, $\tfrac14$ cada una → factor total $\tfrac12$. Coincide exacto con la cuenta en el tiempo, $P_s=\langle m^2\cos^2\rangle=\tfrac12\langle m^2\rangle$, usando $\langle\cos^2\rangle=\tfrac12$: **modular parte la potencia al medio**, y el $\tfrac14$ por copia es lo que hace cerrar la contabilidad.
>
> **Es el mismo "factor 2" recurrente del curso** — el que costó puntos en la pregunta 3 de `exercises/autoevaluacion-am.md` (las deltas de $S_{AM}(f)$ valen $A_c/2$ y $A_c m/4$, no $A_c$ y $A_cm/2$):
>
> | Dónde | Magnitud real | Al pasar a frecuencia |
> |---|---|---|
> | Coseno → deltas (AM) | $A_c$ | $A_c/2$ por delta |
> | Espectro → DEP (Digital) | $\tfrac12$ por copia | $\tfrac14$ por copia |
>
> **Cada coseno real se reparte en dos mitades**, y si además se está en una magnitud de potencia, esas mitades se elevan al cuadrado.
>
> *(Detalle técnico: el $\tfrac14$ por copia vale porque las dos copias **no se superponen**, o sea $f_c>W$ — la misma condición pasabanda de [[../herramientas-matematicas/transformada-hilbert#Aplicaciones en Comunicaciones|Hilbert]]. Si se solaparan habría términos cruzados.)*
>
> **¿Dónde caen los nulos?** $\operatorname{sinc}^2(fT_s)$ se anula donde $fT_s$ es entero no nulo, o sea en $f=\pm kD$ (con $D=1/T_s$). Trasladado a pasabanda: **$f_c\pm kD$** para $k=1,2,3\ldots$ — en este ejercicio $f_c\pm64$, $\pm128$, $\pm192$ kHz. El lóbulo principal va de $f_c-D$ a $f_c+D$, ancho $2D$.
>
> **Alturas relativas de los lóbulos** (valores estándar de $\operatorname{sinc}^2$, sirven para dibujar "con suficiente detalle"):
>
> | Lóbulo | Altura relativa al pico | En dB |
> |---|---|---|
> | Principal | $1$ | $0$ dB |
> | 1er lateral | $0{,}047$ | $\mathbf{-13{,}3}$ **dB** |
> | 2do lateral | $0{,}016$ | $-17{,}8$ dB |
> | 3er lateral | $0{,}008$ | $-20{,}8$ dB |
>
> El **lóbulo principal concentra ~90% de la potencia total** — por eso el ancho de banda de nulo a nulo es una medida razonable pese a que el espectro se extiende infinitamente. El $-13{,}3$ dB del primer lateral es el número clásico del pulso rectangular, y es la razón de que se usen pulsos conformados (coseno realzado) cuando importa no interferir a los canales vecinos: bajan muchísimo los lóbulos laterales a cambio de $\alpha$ de exceso de banda.

**c) Potencia normalizada** — ⚠️ **acá cayeron los dos.** Cuenta completa en 4 pasos:

> **Notación usada acá:**
> - $\lvert s\rvert$ = **magnitud del símbolo** en el plano I/Q, o sea la distancia del punto de constelación al origen: $\lvert s\rvert = \sqrt{I^2+Q^2}$. Físicamente es la **amplitud pico** de la sinusoide que se transmite para ese símbolo (ver Paso 3). Cada punto de la constelación tiene su propio $\lvert s\rvert$.
>   - **Por qué la letra $s$**: por **señal** — la misma $s$ de $s_{AM}(t)$, $s_{FM}(t)$, $s_{DSB\text{-}SC}(t)$ usada en todo el curso. En modulación digital $s_i$ denota el $i$-ésimo elemento del **alfabeto de señales**: los $M$ puntos de la constelación son $s_1,\ldots,s_M$. Las barras $\lvert\cdot\rvert$ son módulo de vector, porque cada símbolo es un punto/vector del plano I/Q.
>   - **Por qué esa distancia es una tensión**: sale de la señal transmitida, $s(t)=I\cos(\omega_ct)-Q\sin(\omega_ct)$. Como $s(t)$ es una tensión [V] y $\cos/\sin$ son adimensionales, **$I$ y $Q$ tienen que estar en volts** — los ejes del plano I/Q están en volts, y la distancia al origen también.
> - $\langle\lvert s\rvert^2\rangle$ = **valor cuadrático medio de esa magnitud, promediado sobre los $M$ símbolos** de la constelación:
> $$\langle\lvert s\rvert^2\rangle = \frac{1}{M}\sum_{i=1}^{M}\lvert s_i\rvert^2$$
> (con símbolos equiprobables, que es lo que dice el enunciado; si no lo fueran habría que pesar por probabilidad).
>
> ⚠️ **Ojo con el $\langle\cdot\rangle$**: acá es un **promedio sobre la constelación** (16 puntos discretos), **no** el promedio temporal $\lim_{T\to\infty}\frac1T\int$ que se usa en [[../derivaciones/modulacion-am#Distribución de potencia|AM]]. Es la misma notación sobrecargada de siempre — se distingue por el contexto: ahí se promedia sobre el tiempo, acá sobre el alfabeto de símbolos. [analysis]

**Paso 1 — sacar la constelación del dato.** 16-QAM es una grilla 4×4 con niveles I/Q en $\pm a,\pm3a$. Los 16 puntos tienen **tres magnitudes distintas**:

| Puntos      | Coordenadas                      | $\lvert s\rvert=\sqrt{I^2+Q^2}$ | Cuántos |
| ----------- | -------------------------------- | ------------------------------- | ------- |
| Interiores  | $(\pm a,\pm a)$                  | $a\sqrt2$                       | 4       |
| Intermedios | $(\pm a,\pm3a)$, $(\pm3a,\pm a)$ | $a\sqrt{10}$                    | 8       |
| Esquinas    | $(\pm3a,\pm3a)$                  | $3a\sqrt2$                      | 4       |

La **amplitud máxima** del enunciado ($3\sqrt2$ mV) corresponde a las esquinas: $3a\sqrt2=3\sqrt2$ mV $\Rightarrow \boxed{a=1\text{ mV}}$. De ahí los tres niveles $\sqrt2$, $\sqrt{10}$, $3\sqrt2$ mV.

**Paso 2 — promediar sobre la constelación** (símbolos equiprobables):

$$\langle\lvert s\rvert^2\rangle = \frac{4(2a^2)+8(10a^2)+4(18a^2)}{16} = \frac{160}{16}a^2 = 10a^2$$

Con $a=1$ mV $=10^{-3}$ V, o sea $a^2 = 10^{-6}$ V²:

$$\langle\lvert s\rvert^2\rangle = 10a^2 = 10^{-5}\text{ V}^2$$

Fórmula general para no rehacer la tabla ($M$-QAM cuadrada con niveles $\pm a,\pm3a,\ldots$):

$$\boxed{\langle\lvert s\rvert^2\rangle = \frac{2(M-1)}{3}\,a^2} \qquad (M=16 \to \tfrac{2\cdot15}{3}a^2 = 10a^2 \ ✓)$$

**Paso 3 — pico → promedio del portador** ← *el paso que se saltearon*. $\lvert s\rvert$ es la **amplitud pico** de la sinusoide transmitida, porque el símbolo viaja como

$$s(t) = I\cos(\omega_ct)-Q\sin(\omega_ct) = \lvert s\rvert\cos(\omega_ct+\phi)$$

y una sinusoide de pico $A$ tiene potencia media $A^2/2$, **no** $A^2$:

> ### Qué es $s(t)=I\cos(\omega_ct)-Q\sin(\omega_ct)$, y de dónde sale el $\lvert s\rvert^2/2$
>
> **1. Qué significa la expresión.** Son **dos portadoras de la misma frecuencia desfasadas 90°** ($\cos$ y $\sin$ están en cuadratura). QAM manda **dos números independientes simultáneamente**, uno en cada una: [analysis]
> - $I$ (*in-phase*) = cuánto se le pone a la portadora coseno
> - $Q$ (*quadrature*) = cuánto se le pone a la portadora seno
>
> $I$ y $Q$ son **constantes durante todo el símbolo** — son las coordenadas del punto de constelación. El receptor puede separarlas porque $\cos$ y $\sin$ son ortogonales.
>
> **2. Por qué esa suma es *una sola* sinusoide.** Dos sinusoides de la misma frecuencia siempre suman una sola sinusoide de esa frecuencia; cambian solo amplitud y fase. Expandiendo el lado derecho con el coseno de una suma:
> $$R\cos(\omega_ct+\phi) = R\cos\phi\,\cos(\omega_ct) - R\sin\phi\,\sin(\omega_ct)$$
> Comparando término a término con $I\cos(\omega_ct)-Q\sin(\omega_ct)$: $I=R\cos\phi$ y $Q=R\sin\phi$. Elevando al cuadrado y sumando ($\cos^2\phi+\sin^2\phi=1$):
> $$R = \sqrt{I^2+Q^2} = \lvert s\rvert, \qquad \phi = \arctan\frac{Q}{I}$$
> **Es literalmente el pasaje de coordenadas cartesianas a polares**: $(I,Q)$ es el punto en cartesianas, $(\lvert s\rvert,\phi)$ el mismo punto en polares.
>
> *Ejemplo*: $I=3$, $Q=4$ → $\lvert s\rvert=5$, $\phi=53{,}1°$, o sea $3\cos(\omega t)-4\sin(\omega t)=5\cos(\omega t+53{,}1°)$. Verificando en $t=0$: izquierda $=3$; derecha $=5\cos(53{,}1°)=3$ ✓
>
> **3. Recién ahora aparece el coseno cuadrado.** Colapsado a $s(t)=\lvert s\rvert\cos(\omega_ct+\phi)$ — **una sola sinusoide de amplitud pico $\lvert s\rvert$** — al elevar al cuadrado sí queda un coseno cuadrado. Por ángulo doble:
> $$s^2(t) = \lvert s\rvert^2\cos^2(\omega_ct+\phi) = \frac{\lvert s\rvert^2}{2}\big[1+\cos(2\omega_ct+2\phi)\big]$$
> El segundo término tiene frecuencia $2\omega_c\neq0$ y **promedia a cero**, quedando $\langle s^2\rangle=\lvert s\rvert^2/2$. Es el mismo $\langle\cos^2\rangle=\tfrac12$ de [[../derivaciones/modulacion-am#Distribución de potencia|AM]]. Equivalente: $A_{rms}=A/\sqrt2$ y $P=A_{rms}^2$. **El $\lvert s\rvert^2$ sería la potencia instantánea en el pico**, que ocurre un instante por ciclo — la media es la mitad.
>
> **4. Ruta alternativa, sin colapsar a polares.** Se puede calcular la potencia directo:
> $$\langle s^2\rangle = \big\langle (I\cos - Q\sin)^2\big\rangle = I^2\underbrace{\langle\cos^2\rangle}_{1/2} - 2IQ\underbrace{\langle\cos\sin\rangle}_{0} + Q^2\underbrace{\langle\sin^2\rangle}_{1/2} = \frac{I^2+Q^2}{2} = \frac{\lvert s\rvert^2}{2}$$
> El término cruzado se anula **por la ortogonalidad entre $\cos$ y $\sin$** — la misma ortogonalidad que permite al receptor separar $I$ de $Q$. Mismo resultado, y muestra dónde hace el trabajo la cuadratura.

$$P = \frac{\langle\lvert s\rvert^2\rangle}{2} = \frac{10^{-5}\text{ V}^2}{2} = 5\times10^{-6}\text{ V}^2 = \boxed{5\ \mu\text{W}}$$

(el último paso, V² → W, es la convención de **potencia normalizada** con $R=1\,\Omega$)

**Paso 4 — a dBm** (como pedía el enunciado):

$$P_{dBm} = 10\log_{10}\!\left(\frac{5\times10^{-6}}{10^{-3}}\right) = 10\log_{10}(5\times10^{-3}) = \boxed{-23{,}0\text{ dBm}}$$

*(Ninguno de los dos consignó el valor en dBm de forma legible.)*

> **Qué falló exactamente**: el estudiante llegó a $10\,\mu$W, o sea **hizo bien el promedio sobre la constelación** (paso 2) pero **olvidó el $/2$ del portador** (paso 3). Eso es lo que el corrector llamó "factor de cresta": el $\sqrt2$ entre pico y RMS de la sinusoide.
>
> **Son dos efectos distintos, conviene no mezclarlos:**
>
> | Efecto | Factor en potencia | ¿Lo aplicó? |
> |---|---|---|
> | Promedio sobre la constelación (máx vs medio de $\lvert s\rvert$) | $18/10 = 1{,}8$ | ✅ Sí |
> | Pico → RMS del portador sinusoidal | $2$ | ❌ **No** |
>
> El factor de cresta aparece sistemáticamente en esta cátedra — también en [[../modulacion-pulsos/pcm-formulario-examen#SNR de cuantificación — esta cátedra usa factor de cresta|PCM]] y en [[../derivaciones/modulacion-am#¿Cual metodo conviene usar en el examen?|AM]]. Conviene tenerlo como reflejo: **si te dan una amplitud máxima y te piden potencia, preguntate si la señal tiene amplitud constante o no.**

**d) Relación señal a ruido**

$$N = N_0 B_N = 4\times10^{-14}\times128\times10^3 = 5{,}12\text{ nW}$$

$$SNR = \frac{5\ \mu\text{W}}{5{,}12\ \text{nW}} = 976{,}6 \ \Rightarrow\ \boxed{SNR \approx 29{,}9\text{ dB}}$$

> **¿De dónde sale $B_N$?** **Lo da el enunciado**: dice *"si el ancho de banda equivalente de ruido **es igual al ancho de banda calculado en a)**"*, o sea usar los 128 kHz. No hay que deducirlo. [analysis]
>
> Conceptualmente, el **ancho de banda equivalente de ruido** es el ancho de un filtro rectangular ideal que dejaría pasar la misma potencia de ruido que el filtro real:
> $$B_N = \frac{1}{\lvert H(f_0)\rvert^2}\int_0^\infty \lvert H(f)\rvert^2\,df$$
> Como los filtros reales tienen flancos graduales, se define este equivalente ideal para simplificar la cuenta. En los finales **casi siempre te lo dan**, o te dicen que lo tomes igual a algún ancho de banda ya calculado. **Unidad: Hz.**
>
> **¿De dónde sale $N=N_0B_N$?** El ruido térmico se modela como **blanco**: densidad espectral de potencia $N_0$ **constante** en toda frecuencia [W/Hz]. El receptor solo deja pasar una banda de ancho $B_N$, así que la potencia que entra es la densidad integrada sobre esa banda:
> $$N = \int_{\text{banda}} N_0\,df = N_0\cdot B_N$$
> Al ser $N_0$ constante, la integral es simplemente **densidad $\times$ ancho**. Chequeo de unidades:
> $$N_0\left[\tfrac{\text{W}}{\text{Hz}}\right]\times B_N\,[\text{Hz}] = [\text{W}] \ ✓$$
> Los Hz se cancelan — misma lógica que la DEP del punto b): $N_0$ es una **densidad** (potencia por unidad de ancho de banda), y para obtener potencia hay que multiplicarla por un ancho.
>
> **El $N$ en la SNR** es esa potencia de ruido, y $S$ la potencia de señal del punto c). El cociente es adimensional (W/W), que es lo que permite expresarlo en dB.
>
> ⚠️ **Trampa de convención**: algunos textos dan la densidad espectral **bilateral** como $N_0/2$, y ahí la cuenta cambia por un factor 2. Esta cátedra da $N_0$ directo en W/Hz y espera $N=N_0B$ (convención **unilateral**). Si un enunciado dice "densidad espectral bilateral", ojo. Ver [[../ruido/aclaracion-densidad-espectral-ruido|Aclaración sobre Densidad Espectral de Ruido]].

*(El estudiante había obtenido 32,99 dB arrastrando la potencia sin corregir; el corrector anotó "arrastra error" — igual descuenta.)*

**e) BER con filtro acoplado (QPSK)** — *ninguno de los dos llegó*

⚠️ **Ojo: el enunciado da un $N_0$ distinto acá** ($2\times10^{-12}$ W/Hz) que en el punto d) ($4\times10^{-14}$ W/Hz). **No se puede reciclar la SNR de d)** — hay que ir por la ruta directa:

$$E_b = \frac{S}{R_b} = \frac{5\times10^{-6}}{256\times10^3} = 1{,}953\times10^{-11}\text{ J}$$

$$\frac{E_b}{N_0} = \frac{1{,}953\times10^{-11}}{2\times10^{-12}} = 9{,}77 \quad(\approx 9{,}9\text{ dB})$$

$$P_e^{QPSK} = Q\!\left(\sqrt{\frac{2E_b}{N_0}}\right) = Q\!\left(\sqrt{19{,}53}\right) = Q(4{,}42) \approx \boxed{5\times10^{-6}}$$

> **Por qué el examen cambia $N_0$ entre d) y e)**: es **deliberado**, para que e) no dependa de d) y no se arrastren errores. Obliga a usar $\dfrac{E_b}{N_0}=\dfrac{S}{R_b N_0}$, que **no necesita ni el ancho de banda ni la SNR** — solo potencia, tasa de bits y densidad de ruido. Si en el examen ves que un ítem repite un dato que ya estaba, sospechá que quiere la ruta independiente. [analysis]
>
> **Dónde entra que sea QPSK**: solo para **elegir la fórmula** de BER. No afecta $E_b/N_0$, porque $E_b=S/R_b$ depende únicamente de potencia total y tasa de bits, no de la modulación. Si fuera 16-QAM, el mismo $E_b/N_0$ daría un BER **peor** al usar la fórmula de $M$-QAM.

## Los cuatro errores que cuestan el ejercicio

Del análisis de cómo fallaron los estudiantes reales:

1. **Confundir los tres anchos de banda** — nulo a nulo ($2D$) vs mínimo ideal ($D$) vs con roll-off ($D(1+\alpha)$)
2. **Olvidar el factor de cresta** al calcular potencia desde la amplitud máxima de la constelación
3. **Arrastrar el error** de un ítem al siguiente — el corrector lo marca ("arrastra error") pero **descuenta igual**
4. **No llegar al BER** por quedarse trabado antes. Recordar la regla del examen: **25% desarrollado por punto como mínimo**; conviene plantear la fórmula aunque no se termine la cuenta

## Ver también

- [[ask-fsk-psk|ASK, FSK, PSK]] — las tres modulaciones básicas
- [[modulacion-qam|Modulación QAM]]
- [[constelaciones|Constelaciones]] — diagramas I/Q, de donde sale el factor de cresta
- [[probabilidad-error|Probabilidad de Error (BER)]] — curvas BER vs $E_b/N_0$
- [[eficiencia-espectral|Eficiencia Espectral]]
- [[../modulacion-pulsos/pcm-formulario-examen|PCM — Formulario de examen]] — la cadena previa (PCM genera los bits que esto transmite)
- [[../conceptos-integradores/eb-n0-vs-snr|$E_b/N_0$ vs SNR]] — el puente de la fórmula 5, en detalle
- [[../conceptos-integradores/pcm-vs-modulacion-digital|PCM vs Modulación Digital]] — cómo se conectan y diferencian
- [[../planificacion/formulario-imprimible|Formulario Imprimible]]
