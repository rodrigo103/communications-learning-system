# Ejercicio propuesto — AM Multitono (Día 2)

> Practicar cronometrado: **30 minutos**, sin mirar la sección `<details>` de respuesta hasta terminar o agotar el tiempo. Cubre lo derivado en [[../wiki/derivaciones/modulacion-am|Derivación Completa de AM]]: BW multitono, potencia con la fórmula $P=P_c+\sum P_{SSB,i}$, PEP en el peor caso, chequeo de sobremodulación, y comparación de eficiencia con DSB-SC.

**Nota:** este es un ejercicio de práctica preparado para esta sesión (no proviene de un final real) — sirve para aplicar la teoría de AM antes de pasar a los ejercicios reales en `exercises/finales/md/`.

## Enunciado

Un transmisor de AM opera con portadora $A_c = 100$ V, $f_c = 1$ MHz, entregando su potencia sobre una carga $R = 50\,\Omega$. Se modula simultáneamente con dos tonos normalizados a pico 1:

$$m_n(t) = 0{,}5\cos(2\pi \cdot 3\text{kHz} \cdot t) + 0{,}3\cos(2\pi \cdot 5\text{kHz} \cdot t)$$

(es decir, índice de modulación $m_1=0{,}5$ para el tono de 3 kHz e $m_2=0{,}3$ para el de 5 kHz).

Se pide:

a) Ancho de banda de la señal AM resultante.

b) Potencia de portadora, potencia de cada banda lateral (individual, no el par), y potencia total.

c) Potencia Pico de Envolvente (PEP), en el peor caso (todos los tonos en fase simultáneamente).

d) ¿La modulación está sobremodulada? Justificar con el criterio correcto (no alcanza con mirar un índice a la vez).

e) Si en cambio se transmitiera la misma información en DSB-SC (misma $A_c$, misma moduladora), ¿cuál sería la eficiencia de potencia, y cuánta potencia se ahorraría respecto al caso AM completo?

---

<details>
<summary><strong>Respuesta</strong></summary>

**a) Ancho de banda**

$BW = 2f_{max}$, con $f_{max}=5$ kHz (el tono más agudo, no la suma):

$$BW = 2 \times 5\text{kHz} = 10\text{kHz}$$

**b) Potencias**

Portadora: $P_c = \dfrac{A_c^2}{2R} = \dfrac{100^2}{2\times50} = \dfrac{10000}{100} = 100$ W.

Para señal multitono, cada tono aporta su propio par de bandas laterales de forma independiente (ortogonales entre sí, mismo argumento de la sección "Distribución de potencia" de la derivación de AM). La potencia combinada de ambas bandas de un tono $i$ es $P_{SSB,i} = P_c\,\dfrac{m_i^2}{2}$ — así que cada banda lateral individual (una sola, no el par) es la mitad de eso: $P_c\,m_i^2/4$.

- Tono 1 ($m_1=0{,}5$): banda lateral individual $= 100\times0{,}5^2/4 = 6{,}25$ W (hay dos: LSB y USB, $6{,}25$ W cada una)
- Tono 2 ($m_2=0{,}3$): banda lateral individual $= 100\times0{,}3^2/4 = 2{,}25$ W (cada una)

Potencia total:

$$P_{total} = P_c + \sum_i P_{SSB,i} = 100 + \left(100\cdot\frac{0{,}5^2}{2}\right) + \left(100\cdot\frac{0{,}3^2}{2}\right) = 100+12{,}5+4{,}5 = 117\text{ W}$$

**c) PEP**

Peor caso: los dos cosenos valen $+1$ al mismo tiempo, dando la envolvente máxima $A_{max}=A_c(1+m_1+m_2)$:

$$A_{max} = 100\,(1+0{,}5+0{,}3) = 180\text{ V}$$

$$PEP = \frac{A_{max}^2}{2R} = \frac{180^2}{100} = 324\text{ W} \quad\left(=P_c(1+m_1+m_2)^2=100\times1{,}8^2=324\text{ W}\;\checkmark\right)$$

**d) Sobremodulación**

El criterio correcto para multitono no es "cada $m_i\leq1$ por separado" — es sobre la **suma**, porque el peor caso de envolvente mínima ocurre cuando todos los tonos llegan a $-1$ a la vez: $A_{min}\geq A_c\left(1-\sum_i m_i\right)$.

$$\sum_i m_i = 0{,}5+0{,}3 = 0{,}8 \leq 1 \quad\Rightarrow\quad \textbf{no hay sobremodulación}$$

($A_{min}\geq100(1-0{,}8)=20$ V $>0$, la envolvente nunca se vuelve negativa.) Si $m_1$ y $m_2$ se miraran por separado ($0{,}5\leq1$ y $0{,}3\leq1$) el chequeo parecería trivialmente satisfecho sin decir nada sobre el caso combinado — el criterio real es la suma.

**e) Comparación con DSB-SC**

Eficiencia de AM: $\eta_{AM} = \dfrac{P_{sidebands}}{P_{total}} = \dfrac{12{,}5+4{,}5}{117} = \dfrac{17}{117} \approx 14{,}5\%$.

En DSB-SC, toda la potencia transmitida va a las bandas laterales (no hay portadora): $\eta_{DSB-SC}=100\%$. Para transportar la misma información (las mismas bandas laterales, $17$ W) alcanzaría con esos $17$ W en vez de los $117$ W totales de AM — un ahorro de $100$ W (exactamente $P_c$, la potencia que en AM se gasta solo en mantener la portadora para poder usar detector de envolvente).

</details>

## Ver también

- [[../wiki/derivaciones/modulacion-am|Derivación Completa de AM]] — todas las fórmulas usadas acá
- [[../wiki/modulacion-analogica/am-vs-dsb-sc|AM-DSB-FC vs DSB-SC]]
- [[../exercises/autoevaluacion-am|Autoevaluación AM]]
