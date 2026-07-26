# Autoevaluación — AM (Día 2, antes del ejercicio cronometrado)

Contestar sin mirar `wiki/derivaciones/modulacion-am.md` ni `wiki/modulacion-analogica/am-vs-dsb-sc.md`. El objetivo es chequear si hace falta repasar algo antes de meterse al ejercicio real cronometrado a 30 min.

1. Escribí la forma compacta de $s_{AM}(t)$ y decí qué representa cada símbolo ($A_c$, $\mu$, $f_c$, $f_m$).

$$\boxed{s_{AM}(t) = A_c[1 + \mu \cos(2\pi f_m t)] \cos(2\pi f_c t)}$$
$A_c$: Amplitud de la portadora
$f_m$: ~~Frecuencia de a portadora~~ — **❌ Corrección: es la frecuencia de la señal moduladora/mensaje**, no de la portadora. Quedó definida igual que $f_c$, probablemente un copy-paste sin cambiar. Ojo con esto en el examen: confundir $f_m$ con $f_c$ arruina cualquier cuenta de ancho de banda o bandas laterales.
$f_c$: Frecuencia de la portadora *(correcto, con typo "de a" → "de la")*
$\mu$: Representa al indice de modulación, contiene una constante $k_a$ para que $\mu$ no sea mayor a 1, lo que provocaría inversión de fase y pérdida de información, ni muy chico, lo que haría que la eficiencia sea peor. **✓ Correcto** — y buena observación lo de la inversión de fase: es exactamente el mismo mecanismo de la sobremodulación que ya vimos ($A(t)<0$ equivale a $|A(t)|\cos(\omega_ct+\pi)$, un salto de fase de 180°), la misma idea que aparece en la envolvente de DSB-SC.

2. ¿Por qué $A(t)=A_c+k_am(t)$ y no simplemente $m(t)\cdot c(t)$? Si multiplicaras directo, ¿qué señal obtendrías?

Si multiplicara directo obtendría DSB-SC.
Se elige esa forma para poder mantener la portadora, lo cual tiene beneficios al simplificar los receptores, los cuales pueden hacerlo por detección de envolvente en lugar de necesitar detección coherente.

**✓ Correcto, sin correcciones.**

3. Para $s_{AM}(t)$ modulada por un solo tono, ¿cuántas líneas espectrales tiene $S_{AM}(f)$, en qué frecuencias, y con qué alturas relativas (en función de $A_c$ y $\mu$)?

Tiene tres lineas espectrales. Una correspondiente a la portadora en $f_c$ y otras dos correspondientes a las bandas laterales en $f_c - f_m$ y $f_c + f_m$.
La altura de la linea correspondiente a la portadora es $A_c$ y la altura correspondiente a cada banda lateral es $A_c * \mu / 2$

**❌ Las alturas están mal. Las frecuencias están bien.** $S_{AM}(f)$ no es ambiguo — es la transformada de Fourier de $s_{AM}(t)$, ya derivada formalmente arriba en `modulacion-am.md`, y tiene un único valor correcto:

$$S_{AM}(f) = \frac{A_c}{2}[\delta(f-f_c)+\delta(f+f_c)] + \frac{A_c\mu}{4}[\delta(f-f_c-f_m)+\delta(f+f_c+f_m)] + \frac{A_c\mu}{4}[\delta(f-f_c+f_m)+\delta(f+f_c-f_m)]$$

Eso da **6 líneas** (no 3 — faltan los espejos en $-f_c$, $-(f_c-f_m)$, $-(f_c+f_m)$, porque $s_{AM}(t)$ es real y su espectro tiene simetría hermítica), con alturas $A_c/2$ para la portadora y $A_c\mu/4$ para cada banda lateral — **la mitad** de lo que se puso ($A_c$ y $A_c\mu/2$). Esos valores puestos son en realidad las amplitudes de los cosenos reales del Paso 4 (una cosa distinta), no el valor de $S_{AM}(f)$: cada coseno real se reparte en dos exponenciales complejas al pasar a Fourier, una a $+f$ y otra a $-f$, cada una con la mitad de la amplitud. Confundir esas dos cosas es exactamente el error, no una forma alternativa de contarlo — "3 líneas con amplitudes reales" es una descripción coloquial del espectro, válida si te piden "las componentes de la señal", pero no es lo que vale $S_{AM}(f)$ cuando se pide por su nombre.

4. Si la moduladora tiene tres tonos de 500 Hz, 1200 Hz y 800 Hz, ¿cuál es el ancho de banda de la señal AM resultante?

El ancho de banda es $2*f_{max}$ , por lo tanto el ancho de banda de la señal resultante será 2400 Hz.

**✓ Correcto.** $f_{max}=1200$ Hz (el tono más agudo, no la suma de los tres), $BW=2\times1200=2400$ Hz.

5. Con $A_c=20$V, $\mu=0{,}6$, $R=50\,\Omega$: calculá $P_c$, la potencia de cada banda lateral, y $P_{total}$.

$P_c$ = 4 W
$P_{banda\ lateral}$ = 0,36 W
$P_{total}$ = 4,72 W

6. ¿Qué es la Potencia Pico de Envolvente (PEP) y cómo se relaciona con $A_c$ y $\mu$?

PEP = 10,24 W

**⚠️ El número está bien, pero la pregunta no está respondida — faltan las dos partes conceptuales.** Verificación del número: $PEP=P_c(1+m)^2=4\times(1{,}6)^2=4\times2{,}56=10{,}24$ W ✓, usando $P_c=4$ W y $m=0{,}6$ de la pregunta 5. Pero eso es solo el resultado numérico de un caso particular — la pregunta pedía **qué es** la PEP (definición conceptual) y **cómo se relaciona** con $A_c$ y $\mu$ (la fórmula general), y ninguna de las dos cosas está en la respuesta.

- **Qué es**: la potencia instantánea *máxima* que alcanza la envolvente de la señal modulada — a diferencia de $P_{total}$ (un promedio sobre todo el ciclo del mensaje), la PEP es el valor en el peor instante (el pico de la envolvente). Importa para diseño de transmisores: el amplificador de salida tiene que soportar ese pico sin saturar, aunque en promedio maneje mucha menos potencia.
- **Cómo se relaciona con $A_c$ y $\mu$**: la envolvente máxima es $A_{max}=A_c(1+m)$ (cuando el coseno de la moduladora vale $+1$), y $PEP=\dfrac{A_{max}^2}{2R}=\dfrac{A_c^2(1+m)^2}{2R}=P_c(1+m)^2$. Para $m=1$ (máxima modulación sin sobremodular), $PEP=4P_c$, mientras que $P_{total}=1{,}5P_c$ — el pico es $\approx2{,}67$ veces la potencia promedio total.

7. Para DSB-SC: ¿por qué no se puede usar un detector de envolvente simple para demodularlo? ¿Qué se necesita en su lugar?

**Respuesta (Claude):** Usando el teorema pasabanda de Hilbert, la señal analítica de $s(t)=A_c\,m(t)\cos(2\pi f_ct)$ es $s_a(t)=A_c\,m(t)e^{j2\pi f_ct}$, y su envolvente es $a(t)=|s_a(t)|=A_c\,|m(t)|$ (con $A_c>0$) — proporcional al **valor absoluto** de $m(t)$, no a $m(t)$ mismo.

*Cómo se llega de $s(t)$ a $s_a(t)$ (tres pasos, no es un salto directo):*
1. **Definición**: $s_a(t)=s(t)+j\,\hat s(t)$, con $\hat s(t)=\mathcal{H}\{s(t)\}$.
2. **Linealidad + teorema pasabanda**: $\hat s(t)=\mathcal{H}\{A_c\,m(t)\cos(2\pi f_ct)\}=A_c\cdot\mathcal{H}\{m(t)\cos(2\pi f_ct)\}=A_c\,m(t)\sin(2\pi f_ct)$ — el último paso usa el [[../wiki/herramientas-matematicas/transformada-hilbert#Aplicaciones en Comunicaciones|teorema de la señal pasabanda]], $\mathcal{H}\{m(t)\cos(2\pi f_ct)\}=m(t)\sin(2\pi f_ct)$, válido porque $m(t)$ es banda base y $f_c>f_m$ (misma condición de siempre).
3. **Euler**: $s_a(t)=A_c\,m(t)\cos(2\pi f_ct)+j\,A_c\,m(t)\sin(2\pi f_ct)=A_c\,m(t)[\cos(2\pi f_ct)+j\sin(2\pi f_ct)]=A_c\,m(t)e^{j2\pi f_ct}$.

Derivación completa con la demostración del teorema pasabanda en [[../wiki/modulacion-analogica/am-vs-dsb-sc|AM-DSB-FC vs DSB-SC]]. Un detector de envolvente simple (diodo + RC) recuperaría $|m(t)|$, perdiendo el signo cada vez que $m(t)$ cruza por cero — información destruida, no recuperable con ese circuito (a diferencia de AM completa, donde el offset $A_c$ garantiza que la envolvente nunca cambie de signo).

En su lugar hace falta **detección coherente/síncrona**: generar localmente una réplica de la portadora $c(t)$, sincronizada en fase y frecuencia exacta con la del transmisor (típicamente con un lazo de Costas o un PLL enganchado a algún resto de portadora o a una tonalidad piloto), y multiplicar la señal recibida por esa réplica antes de filtrar pasabajos. Esto reconstruye $m(t)$ con su signo correcto. El costo es la complejidad extra del receptor (sincronización crítica) frente a la simpleza del detector de envolvente de AM — el trade-off central entre ambos esquemas.

8. Tenés un modulador de ley cuadrática $v_{out}=a\cdot v_{in}+b\cdot v_{in}^2$ con $v_{in}=m(t)+c(t)$. ¿Qué tenés que hacer para que el sistema pase de modular en AM a modular en DSB-SC?

**Respuesta (Claude):** Con un solo modulador de este tipo, **no alcanza con cambiar el filtrado** — hay que cambiar la topología del circuito. Viendo por qué: expandiendo,

$$v_{out} = \underbrace{a\,m(t)}_{\text{BB}} + \underbrace{a\,c(t)}_{f_c} + \underbrace{b\,m^2(t)}_{\text{BB}} + \underbrace{2b\,m(t)c(t)}_{f_c\pm f_m} + \underbrace{b\,c^2(t)}_{\text{DC}+2f_c}$$

El término de portadora pura ($a\,c(t)$, en $f_c$ exacto) y el término de producto/bandas laterales ($2b\,m(t)c(t)$, en $f_c\pm f_m$) caen **dentro del mismo filtro pasabanda** centrado en $f_c$ — no existe un filtro que deje pasar las bandas laterales y bloquee justo la frecuencia central $f_c$ sin ser un filtro "notch" imposible de hacer ideal. Por eso un solo modulador de ley cuadrática, filtrado de cualquier forma, siempre te da AM completa (portadora + producto juntos), nunca DSB-SC puro.

Lo que hace falta es **cancelar la portadora por simetría**, usando **dos moduladores de ley cuadrática idénticos**, con el mismo $c(t)$ en ambos pero $m(t)$ de signo opuesto en cada uno ($v_{in,1}=m(t)+c(t)$, $v_{in,2}=-m(t)+c(t)$), y **restar** las dos salidas:

$$v_{out,1}-v_{out,2} = \big[a\,m(t)+a\,c(t)+b\,m^2(t)+2b\,m(t)c(t)+b\,c^2(t)\big] - \big[-a\,m(t)+a\,c(t)+b\,m^2(t)-2b\,m(t)c(t)+b\,c^2(t)\big] = 2a\,m(t)+4b\,m(t)c(t)$$

Los términos de portadora pura ($a\,c(t)$, igual en ambos) y de $c^2(t)$ se **cancelan exactos** en la resta (mismo signo en los dos), mientras que el producto $m(t)c(t)$ se **duplica** (signos opuestos que se restan, dando el doble). Filtrando pasabanda en $f_c$ para sacar el término de banda base $2a\,m(t)$, queda solo $4b\,m(t)c(t)$ — DSB-SC puro, sin portadora. Este es el mismo principio del modulador balanceado/ring modulator y de la celda de Gilbert (ver [[../wiki/modulacion-analogica/am-vs-dsb-sc|AM-DSB-FC vs DSB-SC]], sección "Métodos de Generación").
