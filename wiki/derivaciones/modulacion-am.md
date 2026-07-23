---
tags:
  - wiki/derivaciones
  - wiki/modulacion-analogica
source_file: outputs/derivations/AM_20251115.md
curso: Sistemas de Comunicaciones
unidad: 3
---

# Derivación Completa de Modulación AM

> **Last verified:** 2025-11-15 | **Verified by:** source

## Señal portadora y mensaje

La señal de mensaje (banda base) es $m(t) = A_m \cos(2\pi f_m t)$ y la portadora de alta frecuencia $c(t) = A_c \cos(2\pi f_c t)$, con $f_c \gg f_m$. Notar que en $c(t)$, la amplitud $A_c$ es una **constante** — no depende de $t$, es un numero fijo que multiplica al coseno.

El principio fundamental de AM consiste en **variar la amplitud de la portadora** proporcionalmente al mensaje: en vez de dejar esa amplitud fija en $A_c$, se la reemplaza por una funcion del tiempo, $A(t)$, que dependa de $m(t)$. La señal transmitida queda entonces $s_{AM}(t) = A(t)\cos(2\pi f_ct)$ — mismo coseno de portadora que antes, pero con el numero $A_c$ cambiado por la funcion $A(t)$. [analysis]

## Derivación paso a paso

### Paso 1: Amplitud variable en el tiempo

Falta definir concretamente que forma tiene $A(t)$. Ahi no hay una deduccion desde primeros principios — es una **eleccion de diseño**, que es justamente lo que define a la modulacion AM (a diferencia de FM, PM, u otras formas de modular). Se elige la relacion mas simple posible entre $A(t)$ y $m(t)$: afin (lineal con un offset), por dos razones concretas: [analysis]

- El offset $A_c$ garantiza que **siempre haya portadora presente**, incluso cuando $m(t)=0$ — eso es lo que permite despues usar un detector de envolvente simple en el receptor (no necesita conocer la fase de la portadora, solo "seguir" la amplitud).
- La relacion **lineal** (proporcional, via la constante $k_a$) hace que la envolvente reproduzca la forma de $m(t)$ sin distorsion, siempre que $A(t)$ no se vuelva negativa (ver "Sobremodulacion" mas abajo).

$$A(t) = A_c + k_a m(t)$$

> **Forma alternativa — ¿por que no definir AM multiplicando $m(t)$ y $c(t)$ directo?** Se puede, pero da otra cosa. $m(t)\cdot c(t) = \frac{A_mA_c}{2}[\cos(2\pi(f_c-f_m)t)+\cos(2\pi(f_c+f_m)t)]$ — no aparece termino en $f_c$ solo, sin portadora: eso es exactamente **DSB-SC** (ver [[../modulacion-analogica/am-vs-dsb-sc|AM-DSB-FC vs DSB-SC]]), no AM con portadora completa. [analysis]
>
> El problema de quedarse solo con el producto: usando el teorema pasabanda de Hilbert ($f_c\gg f_m$), la señal analitica de $s(t)=m(t)\cos(2\pi f_ct)$ es $s_a(t)=m(t)e^{j2\pi f_ct}$ (ver [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]]), y su envolvente es $a(t)=|s_a(t)|=|m(t)|$ — el **valor absoluto** de $m(t)$, no $m(t)$ mismo. Un detector de envolvente simple (diodo + RC) recuperaria $|m(t)|$, perdiendo el signo cada vez que $m(t)$ cruza por cero — informacion destruida, no recuperable con ese circuito.
>
> Multiplicar y sumar la portadora de vuelta resuelve esto, y ademas es una forma mas directa de motivar el Paso 1: $s_{AM}(t) = A_c\cos(2\pi f_ct) + k_a\,m(t)\cos(2\pi f_ct) = c(t) + k_a\,m(t)\,c(t)$ — portadora pura **mas** el producto (DSB-SC) escalado por $k_a$. Factoreando el $\cos(2\pi f_ct)$ comun se recupera exactamente $[A_c+k_am(t)]\cos(2\pi f_ct)$. Ese termino sumado ($c(t)$) es justamente lo que garantiza $A(t)\geq0$ y hace posible el detector de envolvente simple.

### Paso 2: Forma normalizada con índice de modulación

$$A(t) = A_c[1 + \mu m_n(t)]$$

donde $\mu = \frac{k_a A_m}{A_c}$ es el índice de modulación (típicamente $\mu \leq 1$ para evitar sobremodulación) [source — [[../../outputs/derivations/AM_20251115]]].

### Paso 3: Señal modulada

$$s_{AM}(t) = A(t) \cdot \cos(2\pi f_c t) = A_c[1 + \mu \cos(2\pi f_m t)] \cos(2\pi f_c t)$$

### Paso 4: Expansión con identidad trigonométrica

Aplicando $\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$:

$$s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{A_c \mu}{2} \cos(2\pi(f_c - f_m)t) + \frac{A_c \mu}{2} \cos(2\pi(f_c + f_m)t)$$

### Componentes espectrales

1. **Portadora:** frecuencia $f_c$, amplitud $A_c$
2. **Banda lateral inferior (LSB):** frecuencia $f_c - f_m$, amplitud $\frac{A_c \mu}{2}$
3. **Banda lateral superior (USB):** frecuencia $f_c + f_m$, amplitud $\frac{A_c \mu}{2}$

## Resultados clave

### Forma compacta

$$\boxed{s_{AM}(t) = A_c[1 + \mu \cos(2\pi f_m t)] \cos(2\pi f_c t)}$$

### Ancho de banda

El ancho de banda absoluto es la diferencia entre la componente espectral mas alta y la mas baja con energia no nula (ver [[../herramientas-matematicas/ancho-de-banda|Ancho de Banda]]). De los "Componentes espectrales" derivados en el Paso 4, las tres componentes de $s_{AM}(t)$ estan en $f_c-f_m$ (LSB), $f_c$ (portadora) y $f_c+f_m$ (USB) — la portadora queda en el medio, asi que no afecta los extremos. Entonces: [analysis]

$$BW_{AM} = f_{max} - f_{min} = (f_c+f_m) - (f_c-f_m) = 2f_m$$

$$\boxed{BW_{AM} = 2f_m}$$

AM requiere el doble del ancho de banda del mensaje porque transmite ambas bandas laterales [source — [[../../outputs/derivations/AM_20251115]]].

**Generalizacion a multiples tonos** (frecuente en los finales, ej. "modulada por tres tonos senoidales"): si la señal moduladora tiene varias componentes de frecuencia $f_{m,1}, f_{m,2}, \ldots$, cada una genera su propio par de bandas laterales alrededor de $f_c$. El ancho de banda queda determinado por la componente de **mayor frecuencia**, no por la suma de todas: [analysis]

$$BW_{AM} = 2f_{m,max}$$

Esto es consistente con la definicion: las bandas laterales de $f_{m,max}$ son las que quedan mas lejos de $f_c$, y todas las demas caen dentro de ese rango.

### Distribución de potencia

- Potencia de portadora: $P_c = \frac{A_c^2}{2R}$
- Potencia de cada banda lateral: $P_{SB} = \frac{A_c^2 \mu^2}{8R}$
- Potencia total: $P_{total} = \frac{A_c^2}{2R}\left(1 + \frac{\mu^2}{2}\right)$

### Eficiencia de potencia

Solo las bandas laterales transportan información. La eficiencia es:

$$\eta = \frac{P_{sidebands}}{P_{total}} = \frac{\mu^2}{2 + \mu^2}$$

Eficiencia máxima con $\mu = 1$:

$$\boxed{\eta_{max} = \frac{1}{3} = 33.33\%}$$

Esta baja eficiencia es la principal debilidad de AM [analysis]. La portadora consume el 67% de la potencia sin transportar información. Esto motivó el desarrollo de variantes como [[../modulacion-analogica/am-vs-dsb-sc|DSB-SC]] (supresión de portadora) y SSB (banda lateral única).

### Sobremodulación

Si $\mu > 1$, ocurre **sobremodulación**: la envolvente se vuelve negativa, causando distorsión en la demodulación por detector de envolvente.

## Interpretación física

- **Dominio del tiempo:** La envolvente sigue la forma $A_c[1 + \mu m_n(t)]$ modulada a frecuencia $f_c$
- **Dominio de la frecuencia:** El espectro en banda base se traslada a $\pm f_c$, creando portadora + dos bandas laterales

## Generacion practica

**Modulador de ley cuadratica** (el metodo clasico de libro): se suma $m(t)+c(t)$ y se pasa por un dispositivo no lineal (diodo, o transistor en su zona no lineal) con caracteristica $v_{out}=a_1v_{in}+a_2v_{in}^2$. Con $v_{in}=m(t)+c(t)$: [analysis]

$$v_{out} = \underbrace{a_1m(t)}_{\text{banda base}} + \underbrace{a_1c(t)}_{f_c} + \underbrace{a_2m^2(t)}_{\text{banda base}} + \underbrace{2a_2m(t)c(t)}_{f_c\pm f_m} + \underbrace{a_2c^2(t)}_{\text{DC}+2f_c}$$

Cinco terminos en tres zonas de frecuencia distintas. Un **filtro pasabanda centrado en $f_c$ con ancho $2f_m$** (exactamente el $BW_{AM}$ derivado arriba) deja pasar solo $a_1c(t)+2a_2m(t)c(t)$ — portadora mas producto, que es precisamente $A_c'[1+\mu\cos(2\pi f_mt)]\cos(2\pi f_ct)$ con $A_c'=a_1A_c$ y $\mu=2a_2A_m/a_1$.

**Modulacion de alto nivel** (transmisores de mayor potencia, broadcast clasico): en vez de un diodo de bajo nivel, se varia directamente la tension de alimentacion de la etapa final de RF (la que amplifica la portadora) con $m(t)$ amplificado a alta potencia — mismo principio $A(t)=A_c+k_am(t)$, implementado modulando la fuente de la etapa de salida en vez de un dispositivo de bajo nivel seguido de amplificacion lineal.

Ver [[../modulacion-analogica/am-vs-dsb-sc|AM-DSB-FC vs DSB-SC]] para como se genera DSB-SC (no es el mismo metodo — necesita cancelacion balanceada, no alcanza con filtrar).

## Aplicaciones

- Radio AM broadcasting (540–1600 kHz)
- Comunicaciones aeronáuticas
- Radio CB (Citizen's Band)

## Ver también

- [[../modulacion-analogica/am-vs-dsb-sc]]
- [[../modulacion-analogica/indice-modulacion-am]]
- [[../ruido/snr-modulacion-lineal]]
- [[../modulacion-analogica/deteccion-coherente]]
- [[../derivaciones/modulacion-am-extendida]] — Version extendida y didactica
- [[../derivaciones/modulacion-am-alternativa]] — Version alternativa (subagente)
