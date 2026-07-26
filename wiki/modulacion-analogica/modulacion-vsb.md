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

### Por que TV usa VSB — el razonamiento desde el problema

El "vestigio" tiene sentido si se sigue la cadena de descartes, no como definicion suelta: [analysis]

**1. AM comun (DSB) desperdicia la mitad.** Modulando el video en AM quedan dos bandas laterales espejadas, 4,2 MHz arriba y 4,2 MHz abajo de la portadora — 8,4 MHz totales, y las dos llevan *exactamente la misma informacion*. Demasiado caro para un espectro donde entran decenas de canales.

**2. SSB seria lo natural… y no funciona.** Filtrar una banda lateral entera dejaria 4,2 MHz, pero aca aparece la limitacion clave: **el video tiene contenido hasta continua (DC)**. Eso significa que las dos bandas laterales se *tocan* en la portadora, sin ningun hueco entre ellas.

> **La comparacion que lo hace evidente**: la voz telefonica no tiene energia por debajo de ~300 Hz, asi que en DSB queda un hueco de 600 Hz entre las dos bandas laterales — ese hueco es el espacio de transicion donde el filtro puede caer. En video ese hueco **no existe**: cortar una banda lateral pediria un filtro con flanco infinitamente abrupto exactamente en la portadora. Fisicamente irrealizable.

**3. El compromiso (VSB).** Se transmite una banda lateral completa (la superior) **mas un pedacito — un vestigio — de la inferior**. Ese vestigio no aporta informacion nueva: su unica funcion es darle al filtro un flanco suave donde caer, en vez de un acantilado.

**Por que no se duplican las frecuencias bajas.** El flanco del filtro se diseña **antisimetrico respecto de la portadora**: en la portadora misma la respuesta vale $0{,}5$, y lo que se le saca de un lado se le deja del otro. Resultado:

- Frecuencias **altas** del video (detalle fino) → llegan como banda lateral unica, amplitud completa.
- Frecuencias **bajas** (areas grandes, brillo promedio) → llegan por *las dos* bandas laterales, cada una a mitad de amplitud → se suman y dan la amplitud correcta.

La antisimetria hace que la respuesta total sea plana en todo el rango: las bajas viajan "en DSB a media amplitud", las altas "en SSB a amplitud completa", y la transicion es continua. Es exactamente la [[#Condicion de Simetria Vestigial|condicion de simetria vestigial]] de mas arriba ($H(f_c+f)+H(f_c-f)=1$) leida en terminos fisicos.

**La portadora se transmite, no se suprime** — justamente para que el receptor pueda usar un **detector de envolvente barato** en lugar de deteccion sincronica. Con millones de televisores en la calle, conviene poner el costo en el transmisor (uno solo) y no en el receptor (millones). Misma logica que la de [[../modulacion-analogica/am-vs-dsb-sc|AM comercial vs DSB-SC]].

### TV Analogica NTSC — canal de 6 MHz

| Parametro | Valor |
|-----------|-------|
| Portadora de video | a 1,25 MHz del borde inferior del canal |
| Vestigio (banda lateral inferior transmitida) | ~0,75 MHz por debajo de la portadora |
| Luminancia (banda lateral superior) | hasta 4,2 MHz sobre la portadora |
| Subportadora de color | 3,58 MHz sobre la de video |
| Portadora de audio (FM) | 4,5 MHz sobre la de video |
| Ancho ocupado por video (borde inferior → tope) | $1{,}25+4{,}2 = 5{,}45$ MHz |
| Eficiencia espectral | $4{,}2/5{,}45 = 77\%$ |

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
