---
tags:
  - wiki/teoria-informacion
  - wiki/planificacion
curso: Sistemas de Comunicaciones
unidad: 9
---

# Teoría de la Información — Formulario de examen (compacto)

> **Last verified:** 2026-07-28 | **Verified by:** analysis + patrón real de ejercicios en `exercises/finales/md/`

> **Para qué es esta nota**: versión operativa para resolver bajo reloj. Conceptual en [[entropia-fuente|Entropía de Fuente]] y [[capacidad-canal-shannon|Capacidad de Canal]].
>
> **TI aparece en 52,4% de los 42 finales únicos.** Casi siempre **combinada con Modulación Digital**: se calcula una tasa de información y después se pregunta si tal modulación puede transportarla.

## Glosario de símbolos

| Símbolo | Nombre | Unidad |
|---|---|---|
| $p_i$ | Probabilidad del símbolo $i$ | adimensional, $\sum p_i = 1$ |
| $I_i$ | **Información** del símbolo $i$ | bits |
| $H$ | **Entropía** de la fuente | bits/símbolo |
| $H_{max}$ | Entropía máxima (equiprobables) | bits/símbolo |
| $r$ | Tasa de emisión de **símbolos** | símbolos/s |
| $R$ | **Tasa de información** | bps |
| $C$ | **Capacidad** del canal | bps |
| $B$ | Ancho de banda del canal | Hz |
| $S/N$ | Relación señal a ruido | adimensional (lineal) |

## Símbolo, binit y bit — tres cosas distintas

La cátedra es **más rigurosa que la mayoría** acá: usa "**binits**" explícitamente (6+ apariciones en el corpus, ej. *"64000 Binits/Sg"*), lo que implica distinguir **tres** conceptos: [analysis]

| Concepto | Qué es | Unidad |
|---|---|---|
| **Símbolo** | Una **forma de onda transmitida**, sostenida durante $T_s$ (un punto de constelación) | símbolos/s = **baudios** |
| **Binit** (dígito binario) | Un **0 o un 1** — un valor lógico | binits/s |
| **Bit** (Shannon) | Unidad de **información** — cuánto reduce la incertidumbre | bits/s |

### Símbolo vs bit

Un símbolo es **una sola forma de onda enviada al canal**, y puede llevar varios bits: $\ell = \log_2M$ bits por símbolo.

**Ejemplo QPSK a 1000 símbolos/s**: se envían 1000 formas de onda por segundo (una cada 1 ms), cada una codifica 2 binits (00, 01, 10, 11) → flujo de 2000 binits/s.

Se confunden porque **en sistemas binarios ($M=2$) coinciden**: 1 símbolo = 1 binit. Recién con $M>2$ se separan.

> **Por qué importa**: el **ancho de banda depende de la tasa de símbolos**, no de la de bits. Por eso subir $M$ reduce el ancho de banda sin bajar la tasa de bits — es todo el negocio de QAM.

### Binit vs bit

Un binit transporta **1 bit de información solo si los dos valores son equiprobables**. Si $p(0)=0{,}9$ y $p(1)=0{,}1$:

$$H = -0{,}9\log_2 0{,}9 - 0{,}1\log_2 0{,}1 = 0{,}469\ \text{bits/binit}$$

Se manda 1 binit pero se transporta solo 0,469 bits de información. **El resto es redundancia** — exactamente lo que la compresión elimina. Por eso:

$$\boxed{R_{\text{información}} = r\,H \ \leq\ R_{\text{binario}} = \ell\,D}$$

con igualdad **solo si todo es equiprobable**.

### El cuadro completo

$$\underbrace{D\ [\text{símbolos/s}]}_{\text{fija el ancho de banda}} \xrightarrow{\ \times\ell\ } \underbrace{R_b\ [\text{binits/s}]}_{\text{flujo en el canal}} \xrightarrow{\ \times H/\ell\ } \underbrace{R\ [\text{bits/s}]}_{\text{información real}}$$

En los ejercicios donde todo es equiprobable (la mayoría) los dos últimos coinciden y se usan indistintamente. Pero cuando el enunciado da probabilidades distintas — como el ítem que aparece **7 veces** en el corpus (*"si el carácter espacio tiene probabilidad 1/7…"*) — **hay que separarlos**: ahí $H<\log_2M$ y la tasa de información es menor que la binaria.

## Las 5 fórmulas

| #   | Nombre                           | Fórmula                                            | Notas                                                  |
| --- | -------------------------------- | -------------------------------------------------- | ------------------------------------------------------ |
| 1   | **Información de un símbolo**    | $\boxed{I_i = \log_2\dfrac{1}{p_i} = -\log_2 p_i}$ | Menos probable → más información                       |
| 2   | **Entropía** (información media) | $\boxed{H = -\sum_i p_i\log_2 p_i}$                | bits/símbolo. Es el promedio de $I_i$ pesado por $p_i$ |
| 3   | **Entropía máxima**              | $\boxed{H_{max} = \log_2 M}$                       | Cuando los $M$ símbolos son **equiprobables**          |
| 4   | **Tasa de información**          | $\boxed{R = r\,H}$                                 | símbolos/s $\times$ bits/símbolo $=$ bps               |
| 5   | **Shannon-Hartley**              | $\boxed{C = B\log_2\!\left(1+\dfrac{S}{N}\right)}$ | Capacidad máxima del canal, bps                        |

> **Las dos formas de escribir la entropía son idénticas** — $\log_2\frac{1}{p_i} = -\log_2 p_i$, así que: [analysis]
> $$H = -\sum_i p_i\log_2 p_i \quad\equiv\quad H = \sum_i p_i\log_2\frac{1}{p_i} = \sum_i p_i\,I_i$$
> **Para calcular a mano conviene la del recíproco**: como $p_i<1$, se tiene $1/p_i>1$ y **todos los términos salen positivos** — no hay signos que arrastrar. La forma con el menos adelante es más compacta pero obliga a manejar $\log_2 p_i<0$ en cada término.
>
> **La resolución del propio final usa la del recíproco**: $H=\tfrac17\log_2 7 + 10\cdot\tfrac{3}{56}\log_2\tfrac{56}{3} + 72\cdot\tfrac{1}{224}\log_2 224$ — escribieron $\log_2 7$, no $-\log_2\tfrac17$. Con varios grupos de términos, arrastrar signos bajo reloj es donde se cometen errores.

> **Redundancia**: $\boxed{\text{Red} = 1-\dfrac{H}{H_{max}}}$ — cuánto se puede comprimir sin perder información.

> **Límite de Shannon**: $\boxed{\dfrac{E_b}{N_0} > \ln 2 = -1{,}59\text{ dB}}$ — por debajo de eso **no hay comunicación confiable posible**, sin importar el esquema. Sale de $C=B\log_2(1+S/N)$ con $S=E_bR_b$, $N=N_0B$, tomando $R_b\to C$ y $B\to\infty$.

## El patrón dominante: ¿es factible esta modulación?

Es la estructura que más se repite, y la punchline de casi todos los ejercicios:

$$\text{Fuente} \xrightarrow{\ R = rH\ } \text{tasa de info} \xrightarrow{\ \text{Shannon}\ } B_{min}^{teórico} \quad\text{vs}\quad \text{Digital} \to B_{min}^{real}$$

1. **Calcular $R$** de la fuente (fórmulas 1-4)
2. **Calcular $B_{min}$ teórico** despejando de Shannon-Hartley: $B = \dfrac{R}{\log_2(1+S/N)}$
3. **Calcular $B_{min}$ real** de la modulación propuesta: $B = D = \dfrac{R}{\log_2 M_{mod}}$ (ver [[../modulacion-digital/digital-formulario-examen|formulario de Digital]])
4. **Comparar:**

| Resultado | Interpretación |
|---|---|
| $B_{real} > B_{Shannon}$ | ✅ **Factible** — está por encima del mínimo teórico |
| $B_{real} < B_{Shannon}$ | ❌ **No factible** — violaría el límite de Shannon |

> **La idea de fondo**: Shannon-Hartley da una **cota inferior** al ancho de banda. Ningún esquema real puede necesitar *menos* que eso. Si tu cuenta da menos, la modulación no puede funcionar en ese canal — no es que sea "difícil", es **imposible**. [analysis]
>
> ⚠️ **Ojo con la intuición invertida**: subir $M$ (más bits por símbolo) **reduce** el ancho de banda necesario, lo que parece siempre bueno — pero al bajar de la cota de Shannon deja de ser realizable con esa SNR. El límite físico no lo pone el ancho de banda sino la **combinación de ancho de banda y SNR**.

## Ejercicio resuelto (`F_Comu_2022-12-22_res.md`)

**Enunciado**: imagen de video monocromático de 640 líneas × 480 puntos, cada punto con 256 niveles **equiprobables**, 25 imágenes/s. Se recibe con SNR de 20 dB a la entrada del receptor (ideal) y potencia de ruido $10^{-12}$ W.

**a) Velocidad de información de la imagen**

$$\text{puntos/imagen} = 640\times480 = 307\,200$$
$$H = \log_2 256 = 8\ \text{bits/punto} \quad(\text{equiprobables})$$
$$R = 307\,200\ \tfrac{\text{puntos}}{\text{imagen}} \times 8\ \tfrac{\text{bits}}{\text{punto}} \times 25\ \tfrac{\text{imágenes}}{\text{s}} = \boxed{61{,}44\text{ Mbps}}$$

**e) Ancho de banda mínimo según Hartley-Shannon**

$$S/N = 20\text{ dB} = 100 \ \Rightarrow\ \log_2(1+100) = \log_2 101 = 6{,}658$$
$$B = \frac{C}{\log_2(1+S/N)} = \frac{61{,}44\text{M}}{6{,}658} = \boxed{9{,}228\text{ MHz}}$$

**f) Potencia de señal a la entrada**

$$S = (S/N)\cdot N = 100\times10^{-12} = 10^{-10}\text{ W}$$
$$P_{dBm} = 10\log_{10}\!\left(\frac{10^{-10}}{10^{-3}}\right) = \boxed{-70\text{ dBm}}$$

**g) Con 8-PSK — ¿factible?**

$$\ell = \log_2 8 = 3 \ \Rightarrow\ D = \frac{61{,}44\text{ Mbps}}{3\ \text{bits/símbolo}} = 20{,}48\ \textbf{Mbaudios}$$

$$\xrightarrow{\ \text{Nyquist pasabanda: } B_{min}=D\ }\ B_{min} = \boxed{20{,}48\ \textbf{MHz}}$$

$$\underbrace{20{,}48\text{ MHz}}_{\text{lo que necesita 8-PSK}} > \underbrace{9{,}228\text{ MHz}}_{\text{mínimo de Shannon}} \ \Rightarrow\ \textbf{✅ FACTIBLE}$$

**h) Con 1024-QAM — ¿factible?**

$$\ell = \log_2 1024 = 10 \ \Rightarrow\ D = \frac{61{,}44\text{ Mbps}}{10\ \text{bits/símbolo}} = 6{,}144\ \textbf{Mbaudios}$$

$$\xrightarrow{\ B_{min}=D\ }\ B_{min} = \boxed{6{,}144\ \textbf{MHz}}$$

$$\underbrace{6{,}144\text{ MHz}}_{\text{lo que necesita 1024-QAM}} < \underbrace{9{,}228\text{ MHz}}_{\text{mínimo de Shannon}} \ \Rightarrow\ \textbf{❌ NO FACTIBLE}$$

Necesitaría **menos** ancho de banda que el mínimo teórico de Shannon para esa SNR — imposible. Con 20 dB de SNR no alcanza para sostener 10 bits/símbolo.

> ⚠️ **Ojo con el paso $D\to B$**: son **magnitudes distintas** (baudios = símbolos/s; Hz = ancho del intervalo de frecuencias) que dan **el mismo número** en pasabanda, por la cancelación de Nyquist ($\kappa=1$ ciclo/símbolo). No es un cambio de unidad gratuito — es la relación $B_{min}=D$, y hay que escribirla explícitamente. La comparación final con Shannon es **MHz contra MHz**, que es lo que la hace válida. Ver [[../modulacion-digital/digital-formulario-examen#De dónde sale el $2D$, y las unidades del paso $D \to B$|el detalle del paso $D\to B$]]. [analysis]

### La misma cuenta en prosa (para justificar por escrito en el examen)

> Con 8-PSK cada símbolo codifica 3 bits, porque hay 8 puntos de constelación y $\log_2 8 = 3$. Para transportar 61,44 Mbps hacen falta entonces $61{,}44/3 = 20{,}48$ millones de símbolos por segundo. Por Nyquist, enviar 20,48 Mbaudios en pasabanda exige un ancho de banda de al menos 20,48 MHz. Shannon, por su lado, establece que con 20 dB de SNR **ningún** esquema puede transportar esa tasa en menos de 9,228 MHz. Como 8-PSK pide 20,48 MHz —o sea **más** que ese mínimo teórico— la modulación es realizable.

Tres frases, tres pasos: **cuántos bits por símbolo → cuántos símbolos por segundo → cuánto ancho de banda**, y recién ahí la comparación.

**Lo que conviene dejar explícito por escrito es por qué "más" significa factible**: Shannon marca un **piso**, no un techo. Necesitar más ancho de banda que el mínimo es normal (todo esquema real lo hace); necesitar *menos* sería violar el límite.

Versión de una línea para el ítem h): *"1024-QAM requeriría solo 6,144 MHz, por debajo del piso de Shannon de 9,228 MHz para esta SNR — imposible."*

## Cómo calcular $R$ de fuentes compuestas

Los enunciados suelen describir la fuente en capas (imagen → líneas → puntos → niveles). La receta es **multiplicar en cadena hasta llegar a bits/segundo**, cuidando las unidades:

$$R\ \left[\tfrac{\text{bits}}{\text{s}}\right] = \underbrace{\text{elementos por trama}}_{\text{conteo}} \times \underbrace{H}_{\text{bits/elemento}} \times \underbrace{\text{tramas por segundo}}_{1/\text{s}}$$

**Si los símbolos NO son equiprobables**, en vez de $H=\log_2M$ hay que usar $H=-\sum p_i\log_2p_i$ — es el caso del ítem que aparece 7 veces en el corpus ("*si el carácter espacio tiene probabilidad 1/7, cada uno de los diez caracteres…*").

## Codificación de fuente (baja prioridad para el examen)

> ⚠️ **Huffman / códigos compactos aparecen en CERO de los 42 finales** como ejercicio. Esta sección está por completitud conceptual — no es donde invertir tiempo de estudio. [analysis]

### ¿Hace falta saber codificación para calcular la tasa de información? **No.**

| Pregunta | Herramienta |
|---|---|
| ¿**Cuánta** información produce la fuente? | **Entropía** ($H$, $R=rH$) — esto es lo que piden los finales |
| ¿**Cómo** representarla con la menor cantidad de bits? | **Codificación de fuente** (Huffman, extensión) |

$R$ es una **propiedad de la fuente**, independiente de cómo se la codifique después.

**Pero la conexión conceptual importa**: el teorema de codificación de fuente es *lo que justifica* que la entropía sea la medida correcta. Demuestra que $H\leq\bar L<H+1$ (y $\to H$ con extensión), o sea que **no se puede bajar de $H$ bits por símbolo y se puede acercar tanto como se quiera**. Por eso $H$ *es* la información: es el piso irreducible.

### Notación

$n$ = símbolos distintos de la **fuente**; $M$ = símbolos distintos del **código** (binario → $M=2$).

### Codificación directa

Una palabra código por cada símbolo fuente: $\bar L = \sum_{i=1}^n p_i\,l_i$

**El problema**: $l_i$ debe ser entero. Con fuente binaria $p=\{0{,}9;\,0{,}1\}$ → $H=0{,}469$ bits pero $\bar L = 1$ forzosamente:

$$\eta = \frac{H}{\bar L} = 46{,}9\%$$

Más de la mitad desperdiciada, y **ningún código directo lo mejora** — no se puede asignar "media palabra".

### Extensión de la fuente

Agrupar $s$ símbolos en bloques y codificar los bloques (la extensión de orden $s$ tiene $n^s$ símbolos). Como la entropía es aditiva para símbolos independientes, $H(S^s)=s\,H(S)$, y aplicando el teorema a la extensión y dividiendo por $s$:

$$\boxed{\frac{H(S)}{\log_2M} \ \leq\ \frac{\bar L_s}{s} \ <\ \frac{H(S)}{\log_2M}+\frac{1}{s}}$$

**El truco está en que el "+1" queda dividido por $s$**: agrandando el bloque, la cota superior se acerca tanto como se quiera a la entropía.

**El ejemplo anterior con $s=2$** — bloques con $p=\{0{,}81;\,0{,}09;\,0{,}09;\,0{,}01\}$, Huffman da longitudes $\{1,2,3,3\}$:

$$\bar L_2 = 0{,}81(1)+0{,}09(2)+0{,}09(3)+0{,}01(3)=1{,}29 \ \Rightarrow\ \frac{\bar L_2}{2}=0{,}645$$

$$\eta = \frac{0{,}469}{0{,}645} = \mathbf{72{,}7\%}$$

De 46,9% a 72,7% **sin cambiar fuente ni canal**, solo agrupando de a dos.

### Palabras código y Kraft-McMillan

La **palabra código** es la secuencia asignada a un símbolo (o bloque); su longitud $l_i$ se mide en símbolos de código. Las **palabras de longitud variable** son las que permiten dar códigos cortos a los símbolos frecuentes, con la restricción:

$$\sum_{i=1}^{n} M^{-l_i} \leq 1 \qquad\text{(Kraft-McMillan general)}$$

Garantiza que exista un código de prefijo con esas longitudes: cada palabra de longitud $l_i$ "ocupa" una fracción $M^{-l_i}$ del árbol. La versión binaria ($\sum2^{-l_i}\leq1$) está en [[codigo-compacto|Códigos Compactos]].

**Eficiencia general**: $\eta = \dfrac{H}{\bar L\,\log_2M}$

## Los errores que cuestan puntos

1. **Usar $\log_2 M$ cuando los símbolos no son equiprobables** — solo vale si son equiprobables; si no, hay que hacer la suma completa
2. **Meter la SNR en dB dentro de Shannon-Hartley** — la fórmula va con $S/N$ **lineal**. 20 dB → 100, no 20
3. **Confundir $\log_2$ con $\log_{10}$** — en la calculadora: $\log_2 x = \dfrac{\log_{10}x}{\log_{10}2} = \dfrac{\ln x}{\ln 2}$
4. **Invertir la conclusión de factibilidad** — más ancho de banda que Shannon = factible; menos = imposible

## Ver también

- [[entropia-fuente|Entropía de Fuente]] · [[capacidad-canal-shannon|Capacidad de Canal y Shannon-Hartley]]
- [[teorema-shannon-hartley|Teorema de Shannon-Hartley]] · [[../derivaciones/teorema-shannon-hartley|Derivación completa]]
- [[codigo-compacto|Código Compacto (Huffman)]] y [[codigos-deteccion-error|Códigos de Detección de Errores]] — *no aparecieron como ejercicio en ningún final*
- [[../conceptos-integradores/aportes-shannon|Aportes de Shannon]]
- [[../modulacion-digital/digital-formulario-examen|Modulación Digital]] — con el que casi siempre se combina
