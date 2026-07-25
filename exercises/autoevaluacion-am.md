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

7. Para DSB-SC: ¿por qué no se puede usar un detector de envolvente simple para demodularlo? ¿Qué se necesita en su lugar?

8. Tenés un modulador de ley cuadrática $v_{out}=a\cdot v_{in}+b\cdot v_{in}^2$ con $v_{in}=m(t)+c(t)$. ¿Qué tenés que hacer para que el sistema pase de modular en AM a modular en DSB-SC?
