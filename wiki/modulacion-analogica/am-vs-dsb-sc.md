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

$$s_{AM}(t) = A_c[1 + k_a m(t)]\cos(2\pi f_c t)$$

Expandiendo:

$$s_{AM}(t) = \underbrace{A_c\cos(2\pi f_c t)}_{\text{portadora}} + \underbrace{A_c k_a m(t)\cos(2\pi f_c t)}_{\text{bandas laterales}}$$

### DSB-SC (Doble Banda con Portadora Suprimida)

Sin termino de portadora independiente [source — [[../../explicaciones_anki/unidad_03/carta_10_am-dsb-vs-dsbsc]]]:

$$s_{DSB-SC}(t) = A_c m(t)\cos(2\pi f_c t)$$

## Comparacion Espectral

| Propiedad | AM-DSB-FC | DSB-SC |
|-----------|-----------|---------|
| Ancho de banda | $BW = 2f_m$ | $BW = 2f_m$ |
| Portadora | Presente (gasta potencia) | Suprimida |
| Espectro | $S_{AM}(f) = \frac{A_c}{2}[\delta(f-f_c) + \delta(f+f_c)] + \text{bandas}$ | $S_{DSB}(f) = \frac{A_c}{2}[M(f-f_c) + M(f+f_c)]$ |

## Eficiencia de Potencia

Para AM con moduladora sinusoidal e indice $m$:

$$\boxed{\eta_{AM} = \frac{m^2}{2 + m^2}}$$

Para modulacion maxima ($m = 1$):

$$\eta_{max} = \frac{1}{3} = 33.33\%$$

Para DSB-SC:

$$\boxed{\eta_{DSB-SC} = 100\%}$$

Toda la potencia transmitida esta en las bandas laterales (informacion util).

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
