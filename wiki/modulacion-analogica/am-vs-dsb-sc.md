---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc.md
curso: Sistemas de Comunicaciones
unidad: 3
---

# AM-DSB-FC vs DSB-SC: Comparacion

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]

## Definiciones

### AM-DSB-FC (AM Convencional)

Contiene portadora mas ambas bandas laterales [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]:

$$s_{AM}(t) = A_c[1 + m\cdot m_n(t)]\cos(2\pi f_c t)$$

donde $m$ (sin argumento) es el indice de modulacion — adimensional, $m\leq1$ — y $m_n(t)$ es la moduladora **normalizada a pico 1**, exactamente el mismo simbolo y rol que en [[../derivaciones/modulacion-am#Paso 2 Forma normalizada con índice de modulación|Derivacion de AM, Paso 2]] ($A(t)=A_c[1+m\,m_n(t)]$, con $m=\frac{kA_m}{A_c}$). Notacion de indice ya unificada entre ambos documentos (24/07, $\mu\to m$, $k_a\to k$) contra evidencia de los 42 finales unicos: $m$ aparece limpio en 4 de las 14 resoluciones completas, $\mu$ en solo 1 (usado ahi de forma inconsistente), y $k_a$ en ninguna.

**Ojo con $m_n(t)$ vs $m(t)$**: este documento tambien usa el simbolo (sin subindice) $m(t)$ para la moduladora **cruda**, con su propia amplitud adentro (ej. $m(t)=A_m\cos(2\pi f_mt)$) — es la que aparece en la seccion de DSB-SC mas abajo, en "Metodos de Generacion", y en "Deteccion". Esa es la misma convencion de [[../derivaciones/modulacion-am#Señal portadora y mensaje|modulacion-am.md]] (que define $m(t)=A_m\cos(2\pi f_mt)$ arriba de todo), y coincide con como los finales reales suelen dar la moduladora — ej. `F_Comu_2023-12-14.md` la da directo como $m(t)=A_m\cos(2\pi\cdot1000t)+A_m\cos(2\pi\cdot2000t+\theta(t))$, con $A_m$ adentro. Hasta el 25/07 este documento usaba el mismo bare "$m(t)$" para ambas cosas (la cruda de DSB-SC y la normalizada de AM) — colision corregida acá: $m_n(t)$ solo aparece en el contexto de AM (donde el indice $m$ ya se factoreo aparte), $m(t)$ en todo el resto. [analysis]

Expandiendo:

$$s_{AM}(t) = \underbrace{A_c\cos(2\pi f_c t)}_{\text{portadora}} + \underbrace{A_c\, m\, m_n(t)\cos(2\pi f_c t)}_{\text{bandas laterales}}$$

### DSB-SC (Doble Banda con Portadora Suprimida)

Sin termino de portadora independiente [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]:

$$s_{DSB-SC}(t) = A_c m(t)\cos(2\pi f_c t)$$

## Comparacion Espectral

| Propiedad      | AM-DSB-FC                                                                                          | DSB-SC                                            |
| -------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Ancho de banda | $BW = 2f_m$                                                                                        | $BW = 2f_m$                                       |
| Portadora      | Presente (gasta potencia)                                                                          | Suprimida                                         |
| Espectro       | $S_{AM}(f) = \frac{A_c}{2}[\delta(f-f_c) + \delta(f+f_c)] + \frac{A_cm}{2}[M_n(f-f_c) + M_n(f+f_c)]$ | $S_{DSB}(f) = \frac{A_c}{2}[M(f-f_c) + M(f+f_c)]$ |

> Nota: el termino de $S_{AM}(f)$ sale de aplicar la propiedad de modulacion de Fourier al termino de bandas laterales ya expandido arriba ($A_c\,m\,m_n(t)\cos(2\pi f_ct)$) — antes decia solo "+ bandas", que escondia la dependencia en el indice de modulacion y dejaba la fila asimetrica respecto al lado DSB-SC (que si estaba en forma cerrada). Notar que $M_n(f)$ (transformada de la moduladora **normalizada**) y $M(f)$ (transformada de la moduladora **cruda**, en la fila de DSB-SC) no son el mismo objeto — la fila de AM ya tiene el indice $m$ factoreado aparte, la de DSB-SC no factorea nada. [analysis]
>
> **Deduccion de $\mathcal{F}\{m_n(t)\cos(2\pi f_ct)\}$**: se sustituye el coseno por su forma de Euler directamente adentro de la integral de Fourier. Partiendo de la definicion:
> $$\mathcal{F}\{m_n(t)\cos(2\pi f_ct)\} = \int m_n(t)\cos(2\pi f_ct)\,e^{-j2\pi ft}\,dt$$
> Con $\cos(2\pi f_ct)=\frac12(e^{j2\pi f_ct}+e^{-j2\pi f_ct})$:
> $$= \frac12\int m_n(t)\,e^{-j2\pi(f-f_c)t}\,dt + \frac12\int m_n(t)\,e^{-j2\pi(f+f_c)t}\,dt$$
> Cada integral es exactamente la definicion de $M_n(\cdot)$ evaluada en un argumento corrido (poner $f\mp f_c$ donde en $M_n(f)=\int m_n(t)e^{-j2\pi ft}dt$ dice "$f$"):
> $$\mathcal{F}\{m_n(t)\cos(2\pi f_ct)\} = \frac12\big[M_n(f-f_c)+M_n(f+f_c)\big]$$
> Esto es la propiedad de **Modulacion** de [[../conceptos-integradores/aportes-fourier|Aportes de Fourier]] ($x(t)e^{j2\pi f_ct}\leftrightarrow X(f-f_c)$) aplicada dos veces (una por cada exponencial de Euler) y promediada — multiplicar por una exponencial compleja corre el espectro; el coseno, al ser suma de dos exponenciales, lo corre a ambos lados ($\pm f_c$) simultaneamente. Con la constante $A_c\,m$ por linealidad se llega al termino completo de la tabla. La misma propiedad, aplicada a la moduladora cruda $m(t)$ en vez de $m_n(t)$, es exactamente como se llega a la fila de DSB-SC de al lado (sin el indice $m$ de por medio, porque DSB-SC no lo factorea). [analysis]

## Eficiencia de Potencia

Para AM con moduladora sinusoidal e indice $m$:

$$\boxed{\eta_{AM} = \frac{m^2}{2 + m^2}}$$

Para modulacion maxima ($m = 1$):

$$\eta_{max} = \frac{1}{3} = 33.33\%$$

Para DSB-SC:

$$\boxed{\eta_{DSB-SC} = 100\%}$$

Toda la potencia transmitida esta en las bandas laterales (informacion util).

### ¿Por que no se puede pensar a DSB-SC como AM con $m=1$?

Es tentador pensar "$\eta_{DSB-SC}=100\%$, y a mayor $m$ mayor eficiencia, asi que DSB-SC debe ser el caso $m\to\infty$ o $m=1$ de AM" — pero es un error, y vale la pena ver por que con cuidado. [analysis]

**$m=1$ no apaga la portadora.** En $s_{AM}(t)=A_c[1+m\,m_n(t)]\cos(2\pi f_ct)$, la potencia de portadora es $P_c=A_c^2/2R$ — **no depende de $m$**. Poner $m=1$ da "modulacion al 100%" en el sentido de *profundidad de envolvente* (la envolvente $A_c[1+m_n(t)]$ toca cero en el minimo), pero el termino $A_c\cos(2\pi f_ct)$ sigue exactamente igual de fuerte. Confundir "$100\%$ de profundidad de modulacion" con "$100\%$ de potencia en bandas laterales" es el error — son dos cosas distintas que comparten el numero $100\%$ por casualidad. Chequeo directo: en $m=1$, $\eta_{AM}=1/3\approx33\%$ (no $100\%$); para que $\eta_{AM}\to100\%$ haria falta $m\to\infty$, fuera del rango valido ($m\leq1$ para no sobremodular).

**La relacion correcta no es un limite de la forma factoreada, es una decision de circuito.** Partiendo de la forma sin factorear, $A(t)=A_c+k\,m(t)$:

$$s(t) = \underbrace{A_c\cos(2\pi f_ct)}_{\text{portadora}} + \underbrace{k\,m(t)\cos(2\pi f_ct)}_{\text{producto}}$$

Portadora y producto tienen constantes **independientes**: $A_c$ y $k$. Pensar "DSB-SC es AM con $A_c\to0$" mezcla mal las cosas — si de verdad $A_c\to0$ ahi, el termino sobreviviente queda con constante $k$ (no $A_c$), y escribir la formula de DSB-SC como "$A_c\,m(t)\cos(2\pi f_ct)$" (mas abajo, y en la definicion de arriba) usa esa letra para una constante *distinta*, no la que se fue a cero. La imagen fisica correcta, sin necesidad de ningun limite, es la de un **oscilador local compartido**: con la misma amplitud $A_c$ de referencia se puede armar AM (sumandola aparte antes de modular: $[A_c+k\,m(t)]\cos(\cdot)$) o DSB-SC (usandola directo como escala del producto, sin sumarla aparte: $A_c\,m(t)\cos(\cdot)$ — la cuenta de la seccion "Forma alternativa" en [[../derivaciones/modulacion-am#Paso 1 Amplitud variable en el tiempo|Derivacion de AM, Paso 1]]). Lo que cambia entre los dos no es la amplitud del oscilador, es la **decision de sumarlo aparte o no** — por eso "Metodos de Generacion" (abajo) describe topologias de circuito distintas, no un mismo circuito con una perilla de $m$ girada a un valor extremo.

**Por eso el indice de $m$ no esta definido para DSB-SC** — no por una division por cero en un limite, sino porque $m=kA_m/A_c$ mide "cuanto vaivén tiene el mensaje *relativo a un termino de portadora aditivo*", y DSB-SC nunca tuvo ese termino aditivo para empezar. No es que su valor se indefina al acercarse a un limite; es que la estructura "$1+m\cdot(\ldots)$" directamente no aplica a la señal de DSB-SC.

## Metodos de Generacion

**AM-DSB-FC**: modulador de ley cuadratica (sumar $m(t)+c(t)$, pasar por un dispositivo no lineal, filtrar pasabanda en $f_c$ con ancho $2f_m$) o modulacion de alto nivel (variar la alimentacion de la etapa final de RF). Ver detalle en [[../derivaciones/modulacion-am|Derivacion de AM]]. [analysis]

**DSB-SC**: acá el filtrado *no alcanza*. La portadora pura queda exactamente en $f_c$, pegada a las bandas laterales — para una señal real (con contenido cerca de $f_m\to0$) no existe un filtro que corte solo la portadora sin comerse tambien las frecuencias mas bajas del mensaje. Por eso se necesita **cancelar la portadora por simetria de circuito**, no filtrarla en frecuencia:
- **Modulador balanceado de diodos (ring modulator)**: 4 diodos en puente, manejados por la portadora — por simetria, la portadora se cancela a la salida y sobrevive solo el producto $m(t)c(t)$.
- **Celda de Gilbert / multiplicador analogico**: circuito diferencial de transistores que implementa directamente $m(t)\times c(t)$ (multiplicador de 4 cuadrantes; hay chips dedicados, ej. AD633).
- Equivalente conceptual: dos moduladores de ley cuadratica identicos, con $c(t)$ igual en ambos pero $m(t)$ de signo opuesto — al restar las salidas, la portadora (comun a ambos) se cancela y el producto se duplica.

## Metodos de Deteccion

| Aspecto | AM-DSB-FC | DSB-SC |
|---------|-----------|---------|
| Deteccion | Envolvente (simple) | Coherente (requiere sincronismo) |
| Complejidad Rx | Baja | Alta |
| Sincronizacion | No necesaria | Critica |
| Costo receptor | Economico | Costoso |

**Por que DSB-SC no puede usar detector de envolvente**: usando el teorema pasabanda de Hilbert, la señal analitica de $s(t)=m(t)\cos(2\pi f_ct)$ es $s_a(t)=m(t)e^{j2\pi f_ct}$, y su envolvente es $a(t)=|s_a(t)|=|m(t)|$ — el valor absoluto de $m(t)$, no $m(t)$ mismo. Un detector de envolvente recuperaria $|m(t)|$, perdiendo el signo cada vez que $m(t)$ cruza por cero. Por eso DSB-SC necesita **deteccion coherente/sincrona**: generar localmente una replica de $c(t)$ sincronizada en fase y frecuencia (lazo de Costas o PLL) y multiplicar por ella para recuperar $m(t)$. Ver [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]]. [analysis]

## Ejemplo Numerico

Estacion AM con $m_{promedio} = 0.3$, $P_{total} = 50$ kW:

$$\eta = \frac{0.09}{2.09} = 0.043$$

- Potencia util: $0.043 \times 50 = 2.15$ kW
- Potencia desperdiciada en portadora: $47.85$ kW
- Con DSB-SC se necesitarian solo $2.15$ kW para misma calidad
- Mejora en SNR: $10\log_{10}(50/2.15) \approx 13.6$ dB

## Trade-off Fundamental

AM-DSB-FC: **simplicidad** (deteccion de envolvente) a costa de eficiencia
DSB-SC: **eficiencia** (100% potencia en informacion) a costa de complejidad (requiere deteccion coherente) [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]

## Aplicaciones Tipicas

- **AM-DSB-FC**: radio AM comercial (530-1700 kHz), aviacion, donde receptores economicos importan [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]
- **DSB-SC**: enlaces punto a punto, satelites, donde la potencia es escasa y costosa [analysis]

## Puntos Clave

- ✓ Ambos esquemas tienen el mismo ancho de banda: $BW = 2f_m$ [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]
- ✓ La portadora no transmite informacion pero facilita demodulacion [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]
- ✓ Eficiencia maxima de AM: $33.33\%$ (con $m=1$) [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]
- ✓ DSB-SC requiere sincronizacion de portadora para demodulacion [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]

## Ver tambien

- [[../modulacion-analogica/indice-modulacion-am]]
- [[../modulacion-analogica/modulacion-ssb]]
- [[../modulacion-analogica/modulacion-vsb]]
- [[../derivaciones/modulacion-am]]
- [[../ruido/snr-modulacion-lineal]]
