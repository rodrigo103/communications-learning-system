---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial.md
curso: Sistemas de Comunicaciones
unidad: 3
---

# Modulacion VSB (Banda Lateral Vestigial)

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]

## Definicion

VSB (Vestigial Sideband) es un compromiso entre DSB y SSB: transmite **una banda lateral completa** y un **vestigio** (porcion) de la otra banda lateral [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]. Su ancho de banda:

$$\boxed{BW_{VSB} = f_m + f_v}$$

donde $f_v$ es la frecuencia del vestigio, tipicamente $f_v \approx (0.1\text{--}0.25)f_m$.

### VSB no es un esquema aparte: es el continuo entre SSB y DSB

$f_v$ **es literalmente el ancho de la banda de transicion del filtro** — "cuanto necesita tu filtro para pasar de 1 a 0". Eso convierte a $BW_{VSB}=f_m+f_v$ en una familia parametrizada por la calidad del filtro, con SSB y DSB como los dos extremos: [analysis]

| Filtro | $f_v$ | $BW$ | Que resulta |
|---|---|---|---|
| Ideal (irrealizable) | $0$ | $f_m$ | **SSB** |
| Muy bueno | chico | apenas $>f_m$ | VSB angosto |
| Malo | grande | acercandose a $2f_m$ | VSB ancho |
| Ninguno | $f_m$ | $2f_m$ | **DSB** |

Consecuencia practica: el "$25\text{--}30\%$ mas de BW que SSB" de la seccion siguiente **no es una constante de la naturaleza** — es el precio que pagaba la tecnologia de filtros analogicos de los años 40-50. La TV digital, que filtra digitalmente con flancos mucho mas abruptos, logra un vestigio bastante menor que los 0,75 MHz de NTSC dentro de los mismos 6 MHz.

## Por que VSB

Para señales con contenido DC significativo (ej: video) [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]:
- **DSB**: demasiado ancho de banda ($2f_m$) 
- **SSB**: no puede transmitir DC ni frecuencias muy bajas (requiere filtros irrealizables)
- **VSB**: transmite todo el espectro usando solo $25\text{--}30\%$ mas BW que SSB

## Condicion de Simetria Vestigial

Para recuperacion perfecta, el filtro VSB debe satisfacer [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]:

$$\boxed{H_{VSB}(f_c + f) + H_{VSB}(f_c - f) = 1 \quad \text{para } |f| < f_v}$$

Esta condicion asegura que las contribuciones de ambas bandas se sumen correctamente en la demodulacion. El vestigio "rellena" lo que falta de la banda suprimida [analysis].

## Generacion

1. Generar DSB-SC: $s_{DSB}(t) = m(t)\cos(\omega_c t)$
2. Aplicar filtro VSB con respuesta de roll-off alrededor de $f_c$

El filtro VSB tiene roll-off tipico de $0.5\text{--}1.5$ MHz en TV analogica.

## Demodulacion

Multiplicando por $2\cos(\omega_c t)$ y filtrando paso-bajo [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]:

$$m_{recuperada}(t) = m(t) \cdot [H_{VSB}(f_c + f) + H_{VSB}(f_c - f)] = m(t)$$

Por la condicion de simetria, la recuperacion es **perfecta**.

## Aplicacion Principal: Television

### ¿De donde salen los 4,2 MHz de ancho de banda de video?

No es un numero arbitrario — sale del **barrido**, y conecta directo con Nyquist. Cadena NTSC: [analysis]

- 525 lineas/cuadro $\times$ 30 cuadros/s = 15.750 lineas/s → periodo de linea $63{,}5\,\mu$s
- De ese periodo, ~$52{,}6\,\mu$s son **linea activa** (el resto es retrazado/blanking)
- Lineas activas: ~485. Con **factor de Kell** ($\approx0{,}7$, porque las lineas de barrido no se alinean con los detalles de la imagen) → resolucion vertical efectiva $\approx340$
- Para que la resolucion horizontal iguale a la vertical con aspecto 4:3 → $340\times\tfrac43\approx453$ elementos por linea

El peor caso es blanco-negro alternado, donde **dos elementos = un ciclo**:

$$f_{max} = \frac{453}{2\times52{,}6\,\mu s} \approx 4{,}3\text{ MHz}\quad(\to 4{,}2\text{ MHz nominal})$$

> **Conexion con teoria de la informacion — es Nyquist leido al reves.** Escrito como tasa de elementos: $453/52{,}6\mu s = 8{,}6$ Melementos/s, y $B=R/2$. Esa es exactamente la relacion $f_s\geq2B$ del [[../herramientas-matematicas/teorema-muestreo|Teorema de Muestreo]]: el ancho de banda no es una propiedad intrinseca del video, es **la tasa de muestras independientes dividida por dos**.
>
> Y cierra por el otro lado con **Shannon-Hartley**: con SNR tipica de broadcast (~50 dB), $C=4{,}2\text{M}\times\log_2(1+10^5)\approx70$ Mbps — y el video digital crudo equivalente ($640\times480\times30\times8$ bits) da ~74 Mbps. **Coinciden porque la TV analogica es esencialmente sin comprimir**: manda cada cuadro entero, 30 veces por segundo, sin explotar redundancia espacial ni temporal. La ATSC digital mete HD (que crudo serian ~1,5 Gbps) en los *mismos* 6 MHz gracias a compresion MPEG (~80:1) — exactamente la redundancia que el teorema de codificacion de fuente de Shannon dice que era removible, y que la analogica desperdiciaba. Ver [[../teoria-informacion/redundancia-compresion|Redundancia y Compresion]] y [[../teoria-informacion/teorema-shannon-hartley|Teorema de Shannon-Hartley]].

### Que significa cada frecuencia en video (por que la continua es el brillo)

El barrido **convierte espacio en tiempo de forma lineal** — la camara recorre la linea horizontal a velocidad constante — asi que "que tan rapido varia el brillo en el espacio" se traduce directo en "que tan rapido varia la señal en el tiempo". Con $\tau=52{,}6\mu s/453\approx0{,}116\,\mu$s por elemento, un patron cuyo ciclo espacial abarca $N$ elementos da: [analysis]

$$f = \frac{1}{N\tau}$$

Frecuencia temporal **inversamente proporcional al tamaño espacial** del detalle:

| Que hay en la imagen | Ciclo abarca | Frecuencia |
|---|---|---|
| Brillo uniforme en toda la linea (sin variacion) | $N\to\infty$ | **DC (0 Hz)** |
| Degrade u objeto que ocupa toda la pantalla | 453 elementos | ~19 kHz |
| Objeto de ~1/5 del ancho de pantalla | ~86 elementos | ~100 kHz |
| Detalle mas fino posible (blanco/negro alternado) | 2 elementos | **4,3 MHz** |

**Por que la continua es literalmente el brillo promedio**: la componente de continua de cualquier señal es su valor medio, $M(0)=\int m(t)\,dt$. Como $m(t)$ *es* el brillo a lo largo del barrido, su valor medio **es** el brillo promedio de lo que se esta barriendo. No es analogia — es la misma cantidad.

De ahi que pasaaltar duela tanto: cortar debajo de 100 kHz elimina todo lo mas grande que ~1/5 de la pantalla (el cielo, la pared del fondo, la cara de la persona) y deja solo bordes y textura — el aspecto de "deteccion de bordes" mencionado arriba.

> **Detalle practico**: la TV real **si recupera la continua en el receptor**, usando el nivel de blanking/sync transmitido como referencia fija (circuito de *DC restoration*). Pero eso solo repone el nivel absoluto — el contenido de baja frecuencia (las variaciones lentas entre areas grandes) igual hay que transmitirlo, y es lo que VSB protege.

### Por que TV usa VSB — el razonamiento desde el problema

El "vestigio" tiene sentido si se sigue la cadena de descartes, no como definicion suelta: [analysis]

**1. AM comun (DSB) desperdicia la mitad.** Modulando el video en AM quedan dos bandas laterales espejadas, 4,2 MHz arriba y 4,2 MHz abajo de la portadora — 8,4 MHz totales, y las dos llevan *exactamente la misma informacion*. Demasiado caro para un espectro donde entran decenas de canales.

**2. SSB seria lo natural… y no funciona.** Filtrar una banda lateral entera dejaria 4,2 MHz, pero aca aparece la limitacion clave: **el video tiene contenido hasta continua (DC)**. Eso significa que las dos bandas laterales se *tocan* en la portadora, sin ningun hueco entre ellas.

> **La comparacion que lo hace evidente**: la voz telefonica no tiene energia por debajo de ~300 Hz, asi que en DSB queda un hueco de 600 Hz entre las dos bandas laterales — ese hueco es el espacio de transicion donde el filtro puede caer. En video ese hueco **no existe**: cortar una banda lateral pediria un filtro con flanco infinitamente abrupto exactamente en la portadora. Fisicamente irrealizable.

> **¿Y por que no correr los 4,2 MHz un poco hacia arriba para fabricar el hueco? ¿La continua es fundamentalmente distinta de, digamos, 100 kHz?** Dos capas de respuesta, y la segunda es la que decide. [analysis]
>
> **Capa matematica: "correr" una señal real no es una operacion disponible.** El espectro de $m(t)$ real no va de 0 a 4,2 MHz — va de $-4{,}2$ a $+4{,}2$ MHz, con simetria hermitica ($M(-f)=M^*(f)$). Para correrlo 100 kHz habria que multiplicar por $e^{j2\pi\cdot100\text{k}\,t}$, lo que **vuelve compleja la señal** — y por un canal real no se puede transmitir algo complejo. Multiplicando por $\cos(2\pi\cdot100\text{k}\,t)$ (real, que si se puede) salen *dos* copias, en $+100$k y $-100$k, que se superponen y se destruyen entre si, porque el corrimiento (0,1 MHz) es muchisimo menor que el ancho de la señal (4,2 MHz).
>
> Aca esta lo especial de $f=0$: es el **unico punto fijo del eje de frecuencias** ($f=-f$ solo en cero). Por eso la copia espejada se toca a si misma justo ahi, y por eso al modular a $f_c$ la continua mapea exactamente *a la portadora* — el borde inferior de la banda superior y el borde superior de la inferior convergen al mismo punto. El hueco disponible para el filtro es $2f_{min}$ del mensaje: 600 Hz en voz, **cero** en video.
>
> **Capa practica — y aca esta la respuesta de fondo: si, es fundamentalmente distinto.** Lo que *si* se podria hacer (en vez de "correr") es **filtrar pasaaltos el video**, sacandole todo lo de abajo de 100 kHz: eso crearia el hueco de 200 kHz y haria viable el filtro SSB. Tecnicamente funciona. El problema es **que se pierde**: en video, la continua y las frecuencias muy bajas son el **brillo promedio y las areas grandes uniformes** (ver "Que significa cada frecuencia" abajo). Un video pasaaltado se ve como una deteccion de bordes — contornos sobre gris uniforme, sin poder distinguir un cielo brillante de una habitacion oscura. En voz, en cambio, debajo de 300 Hz no hay practicamente nada (ni energia significativa en el habla, ni sensibilidad auditiva relevante), asi que tirarlo sale gratis.
>
> **Conclusion**: como componentes de señal, la continua y los 100 kHz no difieren en naturaleza — ambos son contenido espectral legitimo. Pero **en video la continua carga informacion perceptualmente esencial y en voz no**, y esa asimetria es la que decide todo. VSB existe precisamente porque el video no puede pagar el precio que la voz si puede.

**3. El compromiso (VSB).** Se transmite una banda lateral completa (la superior) **mas un pedacito — un vestigio — de la inferior**.

> **¿Para que sirve el vestigio exactamente?** Conviene invertir la pregunta: el vestigio **no es un ingrediente que se agrega por una razon** — es una consecuencia forzada. El unico requisito real es la [[#Condicion de Simetria Vestigial|condicion de simetria]] $H(f_c+f)+H(f_c-f)=1$, y todo lo demas sale de ahi. [analysis]
>
> **Dato que lo aclara: el SSB ideal tambien cumple esa condicion** — con $H=1$ arriba de $f_c$ y $H=0$ abajo, la suma da $1+0=1$. O sea, la condicion no es "de VSB": **VSB es el conjunto de soluciones *realizables* de esa misma ecuacion**, y SSB ideal es el miembro degenerado (irrealizable) de la misma familia.
>
> **De ahi sale el vestigio, obligado.** Si el flanco es gradual (unica forma realizable), entonces $H(f_c+f)<1$ cerca de $f_c$. Pero la condicion exige $H(f_c-f)=1-H(f_c+f)$, con lo cual $H(f_c-f)>0$: **sobrevive banda lateral inferior, si o si**. Eso es el vestigio.
>
> **La distincion que si importa es entre *existencia* y *forma*** (no entre "darle espacio al filtro" y "compensar la atenuacion" — esas dos descripciones son el mismo hecho visto de dos angulos):
> - **Que exista** el vestigio ⟸ el filtro necesita transicion gradual. Aca "hay lugar donde caer" y "sobra banda inferior" son literalmente lo mismo.
> - **Que forma tenga** ⟸ el requisito extra, y es lo unico no trivial: **gradual no alcanza**. Un filtro que caiga de $1$ a $0$ entre $f_c$ y $f_c+0{,}75$ MHz tambien es gradual y realizable, pero no deja vestigio y da $H(f_c+f)+H(f_c-f)=r(f)\neq1$ → distorsiona. Lo que hace que funcione es la **antisimetria**, no la suavidad.
>
> Y si, el vestigio **no aporta informacion nueva** (ambas bandas laterales llevan la misma informacion — es una copia parcial de lo que ya esta en la superior); lo que aporta es la **amplitud** que la antisimetria necesita para que la suma de las dos contribuciones de $1$.

**Por que no se duplican las frecuencias bajas.** El flanco del filtro se diseña **antisimetrico respecto de la portadora**: en la portadora misma la respuesta vale $0{,}5$, y lo que se le saca de un lado se le deja del otro. Resultado:

- Frecuencias **altas** del video (detalle fino) → llegan como banda lateral unica, amplitud completa.
- Frecuencias **bajas** (areas grandes, brillo promedio) → llegan por *las dos* bandas laterales, cada una a mitad de amplitud → se suman y dan la amplitud correcta.

La antisimetria hace que la respuesta total sea plana en todo el rango: las bajas viajan "en DSB a media amplitud", las altas "en SSB a amplitud completa", y la transicion es continua. Es exactamente la [[#Condicion de Simetria Vestigial|condicion de simetria vestigial]] de mas arriba ($H(f_c+f)+H(f_c-f)=1$) leida en terminos fisicos.

> **¿El receptor podria ignorar el vestigio y demodular "como si fuera SSB"? No — se suma solo, automaticamente.** La deteccion coherente **pliega las dos bandas laterales sobre banda base**; no hay forma de leer una sola. Multiplicando por $2\cos(\omega_ct)$ y filtrando pasabajos, la salida en la frecuencia de banda base $f$ es [analysis]
> $$Y_{LP}(f) = \tfrac12 M(f)\big[H(f_c+f) + H(f_c-f)\big]$$
> Cada $f$ recibe contribucion de **ambos** lados — de $f_c+f$ (banda superior) y de $f_c-f$ (zona del vestigio) — y el receptor no elige: la multiplicacion por el coseno las junta inherentemente. De ahi sale la suma de la condicion de simetria; no es una convencion, es lo que la demodulacion hace.
>
> **Matiz importante**: para $f>f_v$ (arriba de ~0,75 MHz, o sea el ~82% de los 4,2 MHz) el vestigio ya no tiene contenido, $H(f_c-f)=0$, y esas frecuencias **si** llegan exactamente como SSB a amplitud completa. Solo las bajas ($f<f_v$) dependen de la suma de los dos lados.

> **¿Entonces el vestigio sirve para "transmitir potencia"? No — la palabra precisa es *amplitud*, y la diferencia importa.** [analysis]
>
> **Se suman amplitudes, no potencias**: cerca de $f_c$ la banda superior aporta $0{,}5$ y el vestigio $0{,}5$, y dan $1$. Si se sumaran potencias daria $\sqrt{0{,}5^2+0{,}5^2}=0{,}707$, no $1$. La suma es **coherente** (en fase, como fasores) — eso es lo que dice $H(f_c+f)+H(f_c-f)=1$, es una ecuacion de amplitudes.
>
> **El objetivo es respuesta en frecuencia plana, no entregar energia.** Sin vestigio, las altas llegan con amplitud $1$ y las bajas cayendo hacia $0{,}5$: las bajas quedan a **mitad de amplitud relativa a las altas** → distorsion de respuesta (imagen lavada, bordes sobre-marcados — el mismo efecto de pasaalto parcial).
>
> **El test que lo deja claro**: no se arregla subiendo la potencia del transmisor. Amplificar sube *todo* por igual y la relacion bajas/altas queda igual de mal. Es un problema de **forma** de la respuesta, no de **nivel**.
>
> **Donde si aparece la potencia, como efecto lateral**: se podria corregir la forma con un ecualizador en el receptor que amplifique $\times2$ las bajas — pero eso amplificaria tambien el ruido de esa banda, con penalidad de SNR. Con vestigio, la señal de las dos bandas se suma coherentemente ($0{,}5+0{,}5=1$) mientras el ruido de cada una se suma incoherentemente ($\sim\sqrt2$), dando ~3 dB mejor SNR ahi que la alternativa de ecualizar. Real, pero beneficio secundario — la razon de ser sigue siendo la respuesta plana.

**La portadora se transmite, no se suprime** — justamente para que el receptor pueda usar un **detector de envolvente barato** en lugar de deteccion sincronica. Con millones de televisores en la calle, conviene poner el costo en el transmisor (uno solo) y no en el receptor (millones). Misma logica que la de [[../modulacion-analogica/am-vs-dsb-sc|AM comercial vs DSB-SC]].

### TV Analogica NTSC — canal de 6 MHz

> **¿Que es "el borde inferior del canal"?** Es el limite inferior del **slot de 6 MHz que la regulacion le asigna a ese canal** — un numero administrativo, no algo de la señal en si. Cada canal de TV ocupa un bloque fijo de 6 MHz del espectro (canal 2 = 54-60 MHz, canal 6 = 82-88 MHz, etc.), y todo lo de la tabla de abajo se ubica *dentro* de ese bloque, medido desde su borde. [analysis]
>
> **Presupuesto completo del canal 6 (82-88 MHz)**, para ver como se reparten los 6 MHz:
>
> | Frecuencia | Que hay |
> |---|---|
> | 82,00 MHz | **borde inferior del canal** |
> | 82,00-82,50 | banda de guarda (0,5 MHz) |
> | 82,50-83,25 | vestigio (0,75 MHz) |
> | **83,25 MHz** | **portadora de video** ($82{,}00+1{,}25$) |
> | hasta 87,45 | banda lateral superior (4,2 MHz) |
> | 86,83 | subportadora de color ($+3{,}58$) |
> | 87,75 | portadora de audio FM ($+4{,}5$) |
> | 88,00 MHz | borde superior del canal |
>
> La tabla de abajo da los mismos valores en forma **relativa** (para que sirvan en cualquier canal); esta los muestra absolutos en un canal concreto.

> **¿Los canales son contiguos? ¿Eso no complica ubicar la portadora de cada uno?** Son contiguos (canal 2 = 54-60, canal 3 = 60-66: el borde superior de uno *es* el inferior del siguiente), pero **no complica nada** — y esa es justamente la razon de diseño del offset fijo. [analysis]
>
> Entre el contenido real de dos canales vecinos queda: portadora de audio del canal 2 en $54+1{,}25+4{,}5=59{,}75$ MHz → guarda superior hasta 60,00 → guarda inferior del canal 3 hasta 60,50 → vestigio del canal 3 (60,50-61,25) → portadora de video del canal 3 en **61,25** MHz. O sea $0{,}25+0{,}5=0{,}75$ MHz de guarda combinada.
>
> **Por que el calculo no se complica**: la portadora esta siempre a 1,25 MHz del borde inferior de **su propio** canal, con layout interno identico en todos. Entonces $f_{portadora}(N)=f_{borde\,inf}(N)+1{,}25$ MHz — no hay que mirar al vecino para nada. Estandarizar el offset una vez convierte el problema en aritmetica trivial sobre la grilla de 6 MHz; la asimetria (1,25 abajo, 4,75 arriba de la portadora) refleja que VSB es asimetrico, pero esta congelada en el estandar, no se recalcula por canal. En SSB el layout seria mas simple (sin vestigio, la banda arranca en el borde), pero la facilidad de calculo viene de lo mismo en ambos casos: fijar el offset una sola vez.
>
> **El problema real de la adyacencia no es el calculo, es la interferencia**: el audio del canal 2 (59,75, portadora FM fuerte) queda a solo **1,5 MHz** de la portadora de video del canal 3 (61,25), lo que genera batidos visibles. La solucion fue regulatoria, no matematica: **no se asignaban canales adyacentes en la misma plaza** (una ciudad recibia 2, 4, 6 pero no 3, 5) — la regla de "canales tabu".

| Parametro                                       | Valor                                   |
| ----------------------------------------------- | --------------------------------------- |
| Portadora de video                              | a 1,25 MHz del borde inferior del canal (ej. 83,25 MHz en canal 6) |
| Vestigio (banda lateral inferior transmitida)   | ~0,75 MHz por debajo de la portadora    |
| Luminancia (banda lateral superior)             | hasta 4,2 MHz sobre la portadora        |
| Subportadora de color                           | 3,58 MHz sobre la de video              |
| Portadora de audio (FM)                         | 4,5 MHz sobre la de video               |
| Ancho ocupado por video (borde inferior → tope) | $1{,}25+4{,}2 = 5{,}45$ MHz             |
| Eficiencia espectral                            | $4{,}2/5{,}45 = 77\%$                   |

> ⚠️ **Ojo con dos numeros que se confunden facil** (esta nota tenia antes "Vestigio inferior: 1,25 MHz", que mezclaba los dos): [analysis]
> - **1,25 MHz** = distancia del **borde inferior del canal a la portadora de video**. Incluye el vestigio *mas* una banda de guarda de ~0,5 MHz.
> - **0,75 MHz** = el **vestigio propiamente dicho**, la porcion de banda lateral inferior que efectivamente se transmite.
>
> Los dos son correctos, pero miden cosas distintas — usar 1,25 MHz como "el vestigio" sobreestima el $f_v$ de la formula $BW_{VSB}=f_m+f_v$.

Comparacion: DSB requeriria $8{,}4$ MHz (54% mas) [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]].

### TV Digital ATSC (8-VSB)

Usa modulacion 8-VSB (8 niveles) con VSB para transmision terrestre en canales de 6 MHz [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]].

## Analogia

VSB es como empacar inteligentemente para un viaje: no puedes llevar todo (DSB), pero tampoco solo lo minimo (SSB pierde cosas esenciales). VSB lleva un conjunto completo y solo los elementos esenciales del otro — perfecto balance [analysis].

## Puntos Clave

- ✓ VSB preserva DC: critico para video y datos [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]
- ✓ Condicion de simetria vestigial: clave para demodulacion sin distorsion [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]
- ✓ Compromiso optimo entre eficiencia espectral y complejidad [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]
- ✓ Roll-off tipico: $f_v/f_m = 0.1\text{--}0.25$

## Ver tambien

- [[../modulacion-analogica/modulacion-ssb]]
- [[../modulacion-analogica/am-vs-dsb-sc]]
- [[../introduccion/espectro-electromagnetico]]
