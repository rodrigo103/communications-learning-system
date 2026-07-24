# Autoevaluación — AM (Día 2, antes del ejercicio cronometrado)

Contestar sin mirar `wiki/derivaciones/modulacion-am.md` ni `wiki/modulacion-analogica/am-vs-dsb-sc.md`. El objetivo es chequear si hace falta repasar algo antes de meterse al ejercicio real cronometrado a 30 min.

1. Escribí la forma compacta de $s_{AM}(t)$ y decí qué representa cada símbolo ($A_c$, $\mu$, $f_c$, $f_m$).

$$\boxed{s_{AM}(t) = A_c[1 + \mu \cos(2\pi f_m t)] \cos(2\pi f_c t)}$$
$A_c$: Amplitud de la portadora
$f_m$: Frecuencia de a portadora
$f_c$: Frecuencia de a portadora
$\mu$: Representa al indice de modulación, contiene una constante $k_a$ para que $\mu$ no sea mayor a 1, lo que provocaría inversión de fase y pérdida de información, ni muy chico, lo que haría que la eficiencia sea peor.

2. ¿Por qué $A(t)=A_c+k_am(t)$ y no simplemente $m(t)\cdot c(t)$? Si multiplicaras directo, ¿qué señal obtendrías?

Si multiplicara directo obtendría DSB-SC,.
Se elige esa forma para poder mantener la portadora, lo cual tiene beneficios al simplificar los receptores, los cuales pueden hacerlo por detección de envolvente en lugar de necesitar detección coherente.

3. Para $s_{AM}(t)$ modulada por un solo tono, ¿cuántas líneas espectrales tiene $S_{AM}(f)$, en qué frecuencias, y con qué alturas relativas (en función de $A_c$ y $\mu$)?

Tiene tres lineas espectrales. Una correspondiente a la portadora en $f_c$ y otras dos correspondientes a las bandas laterales en $f_c - f_m$ y $f_c + f_m$.
La altura de la linea correspondiente a la portadora es $A_c$ y la altura correspondiente a cada banda lateral es $A_c * \mu / 2$

4. Si la moduladora tiene tres tonos de 500 Hz, 1200 Hz y 800 Hz, ¿cuál es el ancho de banda de la señal AM resultante?

El ancho de banda es $2*f_{max}$ , por lo tanto el ancho de banda de la señal resultante será 2400 Hz.

5. Con $A_c=20$V, $\mu=0{,}6$, $R=50\,\Omega$: calculá $P_c$, la potencia de cada banda lateral, y $P_{total}$.

6. ¿Qué es la Potencia Pico de Envolvente (PEP) y cómo se relaciona con $A_c$ y $\mu$?

7. Para DSB-SC: ¿por qué no se puede usar un detector de envolvente simple para demodularlo? ¿Qué se necesita en su lugar?

8. Tenés un modulador de ley cuadrática $v_{out}=a\cdot v_{in}+b\cdot v_{in}^2$ con $v_{in}=m(t)+c(t)$. ¿Qué tenés que hacer para que el sistema pase de modular en AM a modular en DSB-SC?
