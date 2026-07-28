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

## Las 5 fórmulas

| # | Nombre | Fórmula | Notas |
|---|---|---|---|
| 1 | **Información de un símbolo** | $\boxed{I_i = \log_2\dfrac{1}{p_i} = -\log_2 p_i}$ | Menos probable → más información |
| 2 | **Entropía** (información media) | $\boxed{H = -\sum_i p_i\log_2 p_i}$ | bits/símbolo. Es el promedio de $I_i$ pesado por $p_i$ |
| 3 | **Entropía máxima** | $\boxed{H_{max} = \log_2 M}$ | Cuando los $M$ símbolos son **equiprobables** |
| 4 | **Tasa de información** | $\boxed{R = r\,H}$ | símbolos/s $\times$ bits/símbolo $=$ bps |
| 5 | **Shannon-Hartley** | $\boxed{C = B\log_2\!\left(1+\dfrac{S}{N}\right)}$ | Capacidad máxima del canal, bps |

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

$$\ell = \log_2 8 = 3 \ \Rightarrow\ D = \frac{61{,}44\text{M}}{3} = 20{,}48\text{ Mbaud} \ \Rightarrow\ B_{min} = \boxed{20{,}48\text{ MHz}}$$

$20{,}48 > 9{,}228$ MHz → **✅ FACTIBLE** (está por encima del mínimo de Shannon)

**h) Con 1024-QAM — ¿factible?**

$$\ell = \log_2 1024 = 10 \ \Rightarrow\ D = \frac{61{,}44\text{M}}{10} = 6{,}144\text{ Mbaud} \ \Rightarrow\ B_{min} = \boxed{6{,}144\text{ MHz}}$$

$6{,}144 < 9{,}228$ MHz → **❌ NO FACTIBLE** — necesitaría menos ancho de banda que el mínimo teórico de Shannon para esa SNR. Con 20 dB de SNR **no alcanza** para sostener 10 bits/símbolo.

## Cómo calcular $R$ de fuentes compuestas

Los enunciados suelen describir la fuente en capas (imagen → líneas → puntos → niveles). La receta es **multiplicar en cadena hasta llegar a bits/segundo**, cuidando las unidades:

$$R\ \left[\tfrac{\text{bits}}{\text{s}}\right] = \underbrace{\text{elementos por trama}}_{\text{conteo}} \times \underbrace{H}_{\text{bits/elemento}} \times \underbrace{\text{tramas por segundo}}_{1/\text{s}}$$

**Si los símbolos NO son equiprobables**, en vez de $H=\log_2M$ hay que usar $H=-\sum p_i\log_2p_i$ — es el caso del ítem que aparece 5 veces en el corpus ("*si el carácter espacio tiene probabilidad 1/7, cada uno de los diez caracteres…*").

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
