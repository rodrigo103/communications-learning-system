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

### Expresion del espectro $S_{AM}(f)$

Para pasar de la lista de componentes de arriba a una expresion formal $S_{AM}(f)=\mathcal{F}\{s_{AM}(t)\}$, se escribe cada coseno via Euler ($\cos\theta=\tfrac12(e^{j\theta}+e^{-j\theta})$) y se usa el par $e^{j2\pi f_0t}\leftrightarrow\delta(f-f_0)$. Partiendo de $s_{AM}(t)=A_c\cos(2\pi f_ct)+A_c\mu\cos(2\pi f_mt)\cos(2\pi f_ct)$: [analysis]

$$s_{AM}(t) = \frac{A_c}{2}e^{j2\pi f_ct}+\frac{A_c}{2}e^{-j2\pi f_ct} + \frac{A_c\mu}{4}\Big[e^{j2\pi(f_c+f_m)t}+e^{j2\pi(f_c-f_m)t}+e^{-j2\pi(f_c-f_m)t}+e^{-j2\pi(f_c+f_m)t}\Big]$$

(el termino del producto se expande via Euler en las dos exponenciales de $\cos(2\pi f_mt)$ multiplicando a las dos de $\cos(2\pi f_ct)$, dando 4 exponenciales — no hace falta pasar por la identidad producto-a-suma de nuevo, es el mismo resultado por otro camino). Aplicando la transformada termino a termino:

$$\boxed{S_{AM}(f) = \frac{A_c}{2}\big[\delta(f-f_c)+\delta(f+f_c)\big] + \frac{A_c\mu}{4}\big[\delta(f-f_c-f_m)+\delta(f+f_c+f_m)\big] + \frac{A_c\mu}{4}\big[\delta(f-f_c+f_m)+\delta(f+f_c-f_m)\big]}$$

Seis deltas en total: dos grandes en $\pm f_c$ de altura $A_c/2$ (portadora), y cuatro mas chicas en $\pm(f_c+f_m)$ y $\pm(f_c-f_m)$ de altura $A_c\mu/4$ cada una (bandas laterales). **Ojo con el factor 2**: la altura de cada delta ($A_c\mu/4$) es la *mitad* de la amplitud de banda lateral que aparece en la forma real del Paso 4 ($A_c\mu/2$) — es la misma razon por la que $\cos(2\pi f_0t)$ da dos deltas de altura $\tfrac12$ en vez de una de altura $1$ (ver [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]], donde se derivo el mismo par para coseno/seno): cada exponencial compleja se lleva la mitad de la amplitud real, repartida entre $+f$ y $-f$. Consistente con que $s_{AM}(t)$ es real (asi que $S_{AM}(f)$ tiene que cumplir simetria hermitica, $S_{AM}(-f)=S_{AM}^*(f)$ — acá se cumple trivialmente porque todas las alturas son reales y positivas, y estan puestas en pares simetricos $\pm f$).

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

#### Deduccion via Parseval (a partir de $S_{AM}(f)$)

$s_{AM}(t)$ es una señal de potencia (periodica, energia infinita), asi que no aplica el Parseval de energia ($\int|x|^2dt=\int|X|^2df$, que daria infinito de los dos lados) — aplica la version para señales de potencia: si $x(t)=\sum_k c_k e^{j2\pi f_kt}$ es una suma de exponenciales complejas (como la que se armo arriba con Euler para llegar a $S_{AM}(f)$), la potencia media es $P=\frac{1}{R}\sum_k|c_k|^2$ — cada linea espectral aporta su propia potencia, y se suman porque son ortogonales entre si. [analysis]

De $S_{AM}(f)$ ya derivado, los coeficientes $c_k$ son las alturas de las deltas: dos en $\pm f_c$ con $c=A_c/2$, y cuatro en $\pm(f_c\pm f_m)$ con $c=A_c\mu/4$. Sumando $|c_k|^2$:

$$\sum_k|c_k|^2 = \underbrace{2\left(\frac{A_c}{2}\right)^2}_{\text{portadora}} + \underbrace{4\left(\frac{A_c\mu}{4}\right)^2}_{\text{bandas laterales}} = \frac{A_c^2}{2} + \frac{A_c^2\mu^2}{4}$$

$$P_{total} = \frac{1}{R}\left[\frac{A_c^2}{2}+\frac{A_c^2\mu^2}{4}\right] = \frac{A_c^2}{2R}\left(1+\frac{\mu^2}{2}\right) \checkmark$$

Y por separado: portadora (dos deltas en $\pm f_c$) aporta $P_c=\frac{2(A_c/2)^2}{R}=\frac{A_c^2}{2R}$ — cada banda lateral (un par de deltas, ej. $\pm(f_c+f_m)$) aporta $P_{SB}=\frac{2(A_c\mu/4)^2}{R}=\frac{A_c^2\mu^2}{8R}$. Coincide exacto con los valores de arriba.

#### Deduccion en el dominio del tiempo (el otro metodo)

Sin pasar por frecuencia: la potencia media se define como $P=\langle s_{AM}^2(t)\rangle/R$, con $\langle\cdot\rangle$ el promedio temporal. Partiendo de la forma expandida del Paso 4 (tres cosenos reales, uno por componente): [analysis]

> **Curiosidad (no hace falta para el final): $\langle\cdot\rangle$ no es el bra-ket de mecanica cuantica, pero tampoco es pura coincidencia de simbolo.** $\langle A^2(t)\rangle$ acá es unario (se aplica a una sola funcion), mientras que el bra-ket $\langle\psi|\phi\rangle$ es un producto interno entre dos estados — cosas distintas. Pero ambos son casos particulares del mismo concepto general: un producto interno en un espacio de funciones se define como $\langle f,g\rangle=\int f(t)g^*(t)\,dt$, y el promedio temporal es ese producto interno con $g=1$ (la funcion constante, que es literalmente el coeficiente de Fourier de orden cero): $\langle x(t)\rangle_T=\frac1T\langle x,1\rangle_{[0,T]}$. El bra-ket $\langle\psi|\phi\rangle=\int\psi^*(x)\phi(x)\,dx$ es la misma estructura, aplicada a funciones de onda. No es casualidad que se llame asi — es el mismo David Hilbert de la [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]]: mecanica cuantica y procesamiento de señales comparten tanta matematica (Fourier, ortogonalidad, completitud) porque ambas se construyen sobre la teoria de espacios de Hilbert que el desarrollo. La proxima vez que aparezca $\langle\cdot\rangle$ en cualquier lado — probabilidad (esperanza, $\langle X\rangle=E[X]$), mecanica estadistica (promedio de ensamble), mecanica cuantica (bra-ket) o señales (promedio temporal, como aca) — es la misma familia de idea reutilizada, con distinto contenido segun el campo.
>
> **¿La serie/transformada de Fourier tambien se puede escribir asi? Si, y de hecho es la forma "correcta"/mas profunda — pero no es la notacion usual en este curso.** Los coeficientes de la serie de Fourier, $c_n=\frac{1}{T_0}\int_0^{T_0}x(t)e^{-j2\pi nf_0t}dt$, son literalmente $c_n=\frac{1}{T_0}\langle x(t),e^{j2\pi nf_0t}\rangle_{[0,T_0]}$ — el promedio temporal ($n=0$) es el caso particular de "proyectar sobre la funcion constante". La serie de Fourier completa es proyectar $x(t)$ sobre una base ortogonal de exponenciales complejas, igual que proyectar un vector sobre $\hat x,\hat y,\hat z$. La Transformada de Fourier tiene la misma estructura, $X(f)=\langle x(t),e^{j2\pi ft}\rangle$, salvo que la "base" es un continuo (una funcion por cada $f\in\mathbb R$), no numerable — el mismo problema tecnico que tiene la mecanica cuantica con posicion/momento, resuelto con espacios de Hilbert amañados (*rigged Hilbert spaces*). De hecho es literalmente el mismo par: en QM, $\langle x|p\rangle=\frac{1}{\sqrt{2\pi\hbar}}e^{ipx/\hbar}$ (la onda plana), y la funcion de onda en representacion de momento $\tilde\psi(p)=\langle p|\psi\rangle$ resulta ser, salvo constantes, la Transformada de Fourier de $\psi(x)=\langle x|\psi\rangle$ — el cambio de base posicion↔momento en QM es el mismo par de Fourier que $s(t)\leftrightarrow S(f)$. En ingenieria de comunicaciones nunca se escribe asi (siempre la integral directa) porque se prioriza el calculo, no la estructura abstracta — pero por debajo es la misma matematica. [analysis]
>
> **¿Y la convolucion? Si, con un matiz: un producto interno da un numero, la convolucion da una funcion de $t$.** La conexion es que la convolucion es, para cada valor fijo de $t$, un producto interno distinto: $(x*h)(t)=\int x(\tau)h(t-\tau)d\tau$. Definiendo, para cada $t$ fijo, $g_t(\tau):=h^*(t-\tau)$ (el kernel conjugado, invertido en el tiempo y corrido a $t$), se tiene $g_t^*(\tau)=h(t-\tau)$, y entonces $(x*h)(t)=\langle x(\tau),g_t(\tau)\rangle_\tau$ — la convolucion es una familia de productos internos, uno por cada instante de salida $t$, contra copias corridas (e invertidas) del kernel. No es solo curiosidad: es la teoria del **filtro acoplado/receptor de correlacion** que ya se usa en Ruido — el filtro acoplado tiene $h(t)=s^*(T-t)$ (la plantilla conjugada e invertida en el tiempo) especificamente para que, al convolucionar la señal recibida con $h$, en el instante de muestreo la salida sea exactamente $\langle r,s\rangle$ — la correlacion entre lo recibido y la plantilla esperada. De ahi sale la formula $P_e=Q(\sqrt{2E_b/N_0})$ que se usa para BER. Tambien es la misma estructura que la propiedad de cedazo usada para Hilbert: $x(t)=\int x(\tau)\delta(t-\tau)d\tau=\langle x,\delta(t-\cdot)\rangle$, con $h=\delta$. [analysis]
>
> **¿De donde sale el limite en $\langle f(t)\rangle=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}f(t)\,dt$?** Para una señal de potencia (persiste para siempre, como $s_{AM}(t)$), la integral directa $\int_{-\infty}^\infty f(t)\,dt$ diverge — no sirve. La solucion: **truncar** a una ventana finita $[-T/2,T/2]$ (ahi la integral da un numero finito), **normalizar** dividiendo por $T$ (convierte "acumulado en la ventana" en "promedio por unidad de tiempo"), y recien ahi **tomar el limite** $T\to\infty$ — para que el resultado no dependa de que ventana particular se eligio, sino que capture el comportamiento de largo plazo. Chequeo de que da lo esperado: si $f(t)$ es periodica de periodo $T_0$ y $T$ es multiplo exacto de $T_0$, el promedio en la ventana da **exactamente** $\frac{1}{T_0}\int_0^{T_0}f(t)\,dt$ — el promedio de siempre sobre un periodo, sin aproximacion; el limite no hace falta para el caso periodico simple. Hace falta para el caso **general**, donde no hay un periodo unico — exactamente el caso de AM con **tonos no armonicos entre si** (el primer final convertido en esta sesion, `F_Comu_2022-07-21`: "frecuencias provenientes de generadores independientes entre si, no hay relacion de armonica alguna entre ellas" — esa señal ni siquiera es periodica en sentido estricto). Ahi no existe "un periodo" para promediar, pero el limite sigue funcionando y la demostracion de ortogonalidad (Paso 1/Paso 2 mas arriba) sigue siendo valida sin cambiar nada. Esta misma formula ($P_x=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}|x(t)|^2dt$) ya habia aparecido sin derivar en [[../herramientas-matematicas/senales-energia-potencia|Señales de Energia vs Potencia]] — es el mismo cabo suelto de mas atras en la sesion, ahora cerrado. [analysis]
>
> **¿Como se diferencia, con la notacion $\langle\cdot\rangle$ misma, si una expresion lleva ese limite adentro o no? No se puede — el simbolo no lo dice, es notacion sobrecargada.** Comparar tres usos, los tres con los mismos corchetes angulares: (1) $\langle f,g\rangle=\int f(t)g^*(t)\,dt$ — producto interno binario, integral simple, sin normalizar, sin limite (tipico de señales de energia o espacios de Hilbert abstractos); (2) $\langle x,\phi_n\rangle_{[0,T_0]}=\int_0^{T_0}x(t)\phi_n^*(t)\,dt$ — mismo tipo de cosa pero acotado a un intervalo finito fijo, tampoco lleva limite (no hace falta, el intervalo ya es finito); (3) $\langle f(t)\rangle=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}f(t)\,dt$ — promedio temporal unario, con normalizacion y limite adentro. Las tres usan el mismo par de corchetes — viendo solo "$\langle f\rangle$" sin mas contexto, no hay forma de saber cual de las tres es. [analysis]
>
> Como se resuelve en la practica: **por cantidad de argumentos** (unario, una sola funcion, casi siempre es promedio/valor esperado; binario, dos funciones, casi siempre es producto interno sin normalizar); **por convencion del campo** (en mecanica cuantica $\langle\hat O\rangle$ nunca lleva limite, es un valor esperado sobre un estado ya normalizado; en señales de potencia se asume el limite $T\to\infty$ si no se dice lo contrario; para un periodo fijo de una señal periodica no hace falta limite porque el intervalo ya es finito y exacto); y sobre todo **por definicion explicita previa** — la unica forma realmente confiable. Ese fue el criterio usado aca: se definio $\langle f(t)\rangle$ una sola vez con el limite completo, y de ahi en mas todo el documento usa $\langle\cdot\rangle$ dando por sentada esa definicion — el simbolo no "recuerda" que tiene un limite adentro, es un atajo para lo que ya se dijo antes. Algunos textos usan $\langle\cdot\rangle_T$ (ventana finita, sin limite) versus $\langle\cdot\rangle$ o $\langle\cdot\rangle_\infty$ (el limite) para sacarse la ambiguedad de encima, aunque no es una convencion universal.

$$s_{AM}(t) = \underbrace{A_c\cos(\omega_1t)}_{x_1} + \underbrace{\frac{A_c\mu}{2}\cos(\omega_2t)}_{x_2} + \underbrace{\frac{A_c\mu}{2}\cos(\omega_3t)}_{x_3}, \quad \omega_1=2\pi f_c,\ \omega_2=2\pi(f_c-f_m),\ \omega_3=2\pi(f_c+f_m)$$

Elevando al cuadrado: $s_{AM}^2 = x_1^2+x_2^2+x_3^2 + 2x_1x_2+2x_1x_3+2x_2x_3$. Los terminos cruzados se anulan al promediar — el detalle de por que: [analysis]

**Por que $\langle\cos(\Omega t)\rangle=0$ si $\Omega\neq0$.** Con $\langle f(t)\rangle=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}f(t)\,dt$ (la misma definicion de promedio temporal usada para potencia de señales periodicas):

$$\langle\cos(\Omega t)\rangle = \lim_{T\to\infty}\frac{1}{T}\left[\frac{\sin(\Omega t)}{\Omega}\right]_{-T/2}^{T/2} = \lim_{T\to\infty}\frac{2\sin(\Omega T/2)}{\Omega T}$$

El numerador esta acotado ($|\sin(\cdot)|\leq1$, nunca crece) mientras el denominador $\Omega T\to\infty$ — el cociente tiende a 0. Intuicion mas simple: en cada periodo completo del coseno, el lobulo positivo y el negativo tienen la misma area (por simetria) y se cancelan; promediar sobre un tiempo cada vez mas largo diluye cualquier resto de periodo incompleto hasta cero.

**Por que el producto de dos cosenos de frecuencias distintas cae en ese caso.** Usando $\cos(\omega_it)\cos(\omega_jt)=\tfrac12[\cos((\omega_i-\omega_j)t)+\cos((\omega_i+\omega_j)t)]$: el producto se convierte en la suma de un coseno a la frecuencia *diferencia* y uno a la frecuencia *suma*. Si $\omega_i\neq\omega_j$, el primero ya tiene frecuencia no nula. El segundo, al ser suma de dos frecuencias positivas, **siempre** es no nulo (ni siquiera hace falta que sean distintas). Por el resultado de arriba, ambos promedian a cero, entonces $\langle\cos(\omega_it)\cos(\omega_jt)\rangle=0$.

**Chequeo concreto para los tres pares de $s_{AM}(t)$** (con $\omega_1,\omega_2,\omega_3$ definidos arriba, todas positivas y distintas si $f_m\neq0$):

| Par | Diferencia | Suma |
|---|---|---|
| $(1,2)$ | $2\pi f_m\neq0$ | $2\pi(2f_c-f_m)>0$ |
| $(1,3)$ | $-2\pi f_m\neq0$ | $2\pi(2f_c+f_m)>0$ |
| $(2,3)$ | $-4\pi f_m\neq0$ | $4\pi f_c>0$ |

> **¿Por que hace falta que sean positivas, y por que que sean distintas?** Son dos condiciones que protegen cada una un termino distinto de la identidad producto-a-suma. [analysis]
>
> **Distintas protege la diferencia.** Si $\omega_i=\omega_j$, la diferencia seria $\omega_i-\omega_j=0$, y $\cos(0\cdot t)=\cos(0)=1$ — una constante, no un coseno oscilante. El promedio de una constante es esa misma constante (1), no cero: ahi se rompe el argumento, dos componentes de la misma frecuencia no son ortogonales. Por eso se pide $f_m\neq0$: si $f_m=0$ (sin modulacion), $\omega_2=\omega_3=\omega_c$ y las tres frecuencias colapsan.
>
> **Positivas protege la suma** — con un matiz: el signo de $\Omega$ no afecta al lema en si ($\cos(\Omega t)=\cos(-\Omega t)$, el coseno es par, promedia a cero para cualquier $\Omega\neq0$ sea cual sea el signo). Lo que la positividad compra es una garantia barata sobre la *suma*: si $\omega_i,\omega_j>0$, la suma $\omega_i+\omega_j$ es automaticamente positiva, nunca puede dar cero, sin necesidad de calcularla caso por caso. Con frecuencias negativas permitidas, la suma si podria cancelarse por accidente (ej. $\omega_i=5$, $\omega_j=-5$, distintas mas la suma da cero igual) y el argumento se romperia.
>
> **La positividad no es gratis**: que $\omega_1,\omega_2,\omega_3$ sean todas positivas requiere $f_c>f_m$ (si no, $\omega_2=2\pi(f_c-f_m)$ seria negativa) — la misma condicion que ya se uso para el "cero exacto" de $\langle A^2(t)\cos^2(\omega_ct)\rangle$ en [[#^u9s3nm|el Paso B mas arriba]]. No es coincidencia: es la **misma condicion del teorema de la señal pasabanda de Hilbert** (ver [[../herramientas-matematicas/transformada-hilbert#Aplicaciones en Comunicaciones|Transformada de Hilbert — Aplicaciones]], con el diagrama de las dos islas espectrales) reapareciendo disfrazada por tercera vez en este documento: "la portadora suficientemente por encima del mensaje para que nada se solape con $f=0$" — ahi garantiza que $\mathcal H\{m(t)\cos(2\pi f_ct)\}=m(t)\sin(2\pi f_ct)$, en el Paso B garantiza el promedio cero exacto, y aca garantiza que $\omega_2>0$.

Los tres pares cumplen la condicion (ninguna diferencia ni suma es cero), asi que los tres terminos cruzados de $s_{AM}^2(t)$ promedian a cero — por eso los tres componentes son **ortogonales** entre si y sus potencias se suman sin terminos de interferencia. Queda:

$$\langle s_{AM}^2\rangle = \langle x_1^2\rangle+\langle x_2^2\rangle+\langle x_3^2\rangle = \frac{A_c^2}{2}+\frac{(A_c\mu/2)^2}{2}+\frac{(A_c\mu/2)^2}{2} = \frac{A_c^2}{2}+\frac{A_c^2\mu^2}{4}$$

usando que el valor cuadratico medio de un coseno de amplitud $A$ es $A^2/2$ (equivalente a $A_{rms}^2$, con $A_{rms}=A/\sqrt2$) — y esto si vale la pena mostrarlo, no solo asumirlo: por angulo doble, $\cos^2(\omega t)=\frac{1+\cos(2\omega t)}{2}=\frac12+\frac12\cos(2\omega t)$. Promediando, $\langle\cos^2(\omega t)\rangle=\frac12+\frac12\langle\cos(2\omega t)\rangle=\frac12+0=\frac12$, usando que el promedio temporal de un coseno de frecuencia no nula es cero (demostracion completa en [[#¿Cual metodo conviene usar en el examen?|¿Cual metodo conviene usar en el examen? — Paso A]], mas abajo). Entonces $\langle(A\cos\omega t)^2\rangle=A^2\langle\cos^2(\omega t)\rangle=A^2/2$. [analysis] Dividiendo por $R$:

$$P_{total} = \frac{A_c^2}{2R}+\frac{A_c^2\mu^2}{4R} = \frac{A_c^2}{2R}\left(1+\frac{\mu^2}{2}\right) \checkmark$$

Mismo resultado que por Parseval, como tiene que ser — es el mismo calculo de fondo (potencia de cada linea espectral vs. valor cuadratico medio de cada componente sinusoidal), solo que uno pasa por $S_{AM}(f)$ y el otro se queda en $s_{AM}(t)$.

#### ¿Cual metodo conviene usar en el examen?

**Dominio del tiempo, sin dudarlo** — es mas rapido y mas robusto que pasar por Parseval/$S_{AM}(f)$, sobre todo bajo presion de 30 min. [analysis]

Via Parseval hace falta escribir $S(f)$ con deltas y tener cuidado con el factor 2 entre amplitud real y altura de delta (el mismo error de factor 2 que es facil cometer, como paso en la autoevaluacion). Via tiempo hay un atajo directo que no pasa por ningun espectro, y que ademas es **exacto, no aproximado** — vale la pena mostrarlo bien: [analysis]

*Paso A*: por angulo doble, $\cos^2(\omega_ct)=\frac12+\frac12\cos(2\omega_ct)$ — es "$\tfrac12$ mas un coseno de frecuencia $2f_c$ (no nula)", que promedia a cero por el mismo lema ya demostrado arriba. Entonces $\langle\cos^2(\omega_ct)\rangle=\tfrac12$ exacto, para cualquier $f_c\neq0$.

*Paso B*: el problema real es el producto $A^2(t)\cos^2(\omega_ct)$, no $\cos^2(\omega_ct)$ solo, porque $A(t)$ tambien varia en el tiempo. Usando la misma identidad: $A^2(t)\cos^2(\omega_ct)=\frac12A^2(t)+\frac12A^2(t)\cos(2\omega_ct)$.

> **¿Por que se puede aplicar el angulo doble aca, si $A(t)$ no es necesariamente un coseno?** La identidad $\cos^2\theta=\frac{1+\cos2\theta}{2}$ se aplica **solo** al factor $\cos^2(\omega_ct)$ (que si es, literalmente, un coseno al cuadrado — es la portadora, por construccion de AM) — despues se **distribuye la multiplicacion** sobre la suma resultante: $A^2(t)\cdot\left[\frac12+\frac12\cos(2\omega_ct)\right]=\frac12A^2(t)+\frac12A^2(t)\cos(2\omega_ct)$. Ese ultimo paso es pura propiedad distributiva ($x\cdot(y+z)=xy+xz$), valida sea lo que sea $A^2(t)$ — no hace falta que $A(t)$ "contenga un coseno" ni que tenga ninguna forma particular. [analysis]
>
> Esto es la clave de la generalidad del metodo: $A(t)=A_c[1+\mu\,m_n(t)]$ con $m_n(t)$ arbitraria (un tono, varios tonos, o una señal no sinusoidal por factor de cresta) — en ningun momento de esta manipulacion se uso que $A(t)$ fuera un coseno, solo se toco el factor $\cos^2(\omega_ct)$, que es fijo (la portadora). Recien mas adelante, al calcular $\langle A^2(t)\rangle$ en si, hace falta la forma concreta de $m_n(t)$ (tono: $\langle m_n^2\rangle=\tfrac12$; factor de cresta: $1/CF^2$). Por eso el metodo sirve para moduladoras arbitrarias — nunca se apoyo en que $A(t)$ tuviera estructura sinusoidal.

El primer termino promedia a $\tfrac12\langle A^2(t)\rangle$ (lo que se busca). Falta el segundo: $A(t)$ tiene contenido de frecuencia hasta $f_m$ (viene de $m(t)$), asi que $A^2(t)$ (al cuadrado) tiene contenido hasta $2f_m$ — porque multiplicar en tiempo equivale a convolucionar en frecuencia ($x(t)^2\leftrightarrow X(f)*X(f)$), y convolucionar dos soportes $[-W,W]$ da soporte $[-2W,2W]$: elevar al cuadrado siempre duplica el ancho de banda. Es la misma regla que se usa mas abajo en [[#Generacion practica|Generación práctica]] para explicar donde caen $m^2(t)$ y $c^2(t)$ en el modulador de ley cuadratica. Multiplicar por $\cos(2\omega_ct)$ traslada ese contenido a quedar centrado en $2f_c$, ocupando de $2f_c-2f_m$ a $2f_c+2f_m$. **Mientras $f_c>f_m$**, esa banda completa queda lejos de $f=0$, y el promedio temporal (que extrae el valor en $f=0$) da **cero exacto** — no una aproximacion por "$A(t)$ casi constante", es el mismo argumento de separacion espectral del teorema pasabanda de Hilbert. ^u9s3nm

Entonces $\langle A^2(t)\cos^2(\omega_ct)\rangle=\tfrac12\langle A^2(t)\rangle$ exacto, y:

$$P_{total} = \frac{1}{2R}\langle A^2(t)\rangle$$

Con $A(t)=A_c[1+\mu\,m_n(t)]$ y $m_n(t)$ de media nula (tipico):

$$\boxed{P_{total} = \frac{A_c^2}{2R}\Big[1+\mu^2\langle m_n^2(t)\rangle\Big]}$$

Una sola formula general ($R$ = impedancia/resistencia de carga, la misma de toda la seccion de potencia). Verificacion de consistencia: para $m_n(t)=\cos(2\pi f_mt)$ (un tono), $\langle m_n^2\rangle=\tfrac12$, y da exactamente $\frac{A_c^2}{2R}(1+\mu^2/2)$ — lo de siempre, y coincide con el resultado de sumar las potencias de los tres cosenos por ortogonalidad mas arriba.

**Por que esto importa mas alla de la velocidad — señales no sinusoidales.** Si la moduladora no es un tono (ej. "2 Vpp, valor medio nulo, factor de cresta 3", el tipo de dato que aparece en `exercises/finales/md/F_Comu_2024-11-14_res.md`), no tiene un espectro de lineas limpio para meter en Parseval — inviable en 30 min. Pero con la formula de arriba no hace falta: si $m_n(t)$ esta normalizada a pico 1, $\langle m_n^2\rangle=m_{n,rms}^2=1/CF^2$ (factor de cresta $CF=$ pico/RMS), entonces:

$$P_{total} = \frac{A_c^2}{2R}\left[1+\frac{\mu^2}{CF^2}\right]$$

Sustitucion directa, sin necesidad de espectro. **Cuando si conviene frecuencia**: solo si el problema ya pide o da el espectro como paso previo (ej. "calcule $S(f)$") — ahi conviene seguir en ese dominio en vez de cambiar. Pero como metodo de arranque para calcular potencia, tiempo es mas rapido, mas general (sirve para moduladoras no sinusoidales), y tiene menos pasos donde cometer el error de factor 2.

### Eficiencia de potencia

Solo las bandas laterales transportan información. La eficiencia es:

$$\eta = \frac{P_{sidebands}}{P_{total}} = \frac{\mu^2}{2 + \mu^2}$$

Eficiencia máxima con $\mu = 1$:

$$\boxed{\eta_{max} = \frac{1}{3} = 33.33\%}$$

Esta baja eficiencia es la principal debilidad de AM [analysis]. La portadora consume el 67% de la potencia sin transportar información. Esto motivó el desarrollo de variantes como [[../modulacion-analogica/am-vs-dsb-sc|DSB-SC]] (supresión de portadora) y SSB (banda lateral única).

### Potencia Pico de Envolvente (PEP)

**Que es**: la potencia instantanea **maxima** que alcanza la envolvente de la señal modulada — a diferencia de $P_{total}$ (un promedio sobre todo el ciclo del mensaje), PEP es el valor en el peor instante (el pico). Importa para diseño de transmisores: el amplificador de salida tiene que soportar ese pico sin saturar, aunque en promedio maneje mucha menos potencia — es la misma logica del "headroom" en audio. [analysis]

**Deduccion**: la potencia instantanea de la envolvente (promediada sobre los ciclos rapidos de portadora, ya que $\cos^2(\omega_ct)$ promedia a $\tfrac12$ mucho mas rapido de lo que varia $A(t)$ — ver [[#¿Cual metodo conviene usar en el examen?|la deduccion de arriba]]) es $p(t)=\frac{A^2(t)}{2R}$. El pico ocurre cuando la envolvente es maxima, $A_{max}=A_c(1+\mu)$ (cuando $\cos(2\pi f_mt)=1$, el pico positivo de la moduladora):

$$PEP = \frac{A_{max}^2}{2R} = \frac{A_c^2(1+\mu)^2}{2R} = P_c(1+\mu)^2$$

usando $P_c=A_c^2/(2R)$. Para $\mu=1$ (maxima modulacion sin sobremodular): $PEP=4P_c$, mientras $P_{total}=1{,}5P_c$ — el pico es $4/1{,}5\approx2{,}67$ veces la potencia promedio total. El transmisor tiene que estar dimensionado para ese pico, no para el promedio.

**Multitono**: si la moduladora es una suma de tonos, el peor caso (worst-case PEP) ocurre cuando todos los tonos coinciden en fase simultaneamente, dando $A_{max}=A_c\left(1+\sum_i\mu_i\right)$ — aunque ese pico exacto puede ser un instante raro/momentaneo, el transmisor igual tiene que poder manejarlo sin distorsionar.

### Sobremodulación

Si $\mu > 1$, ocurre **sobremodulación**: la envolvente se vuelve negativa, causando distorsión en la demodulación por detector de envolvente. Nota: la $A_{max}=A_c(1+\mu)$ de PEP arriba es el mismo pico que aca — si $\mu>1$, el pico $A_{max}$ sigue siendo positivo y grande, el problema de la sobremodulacion esta del lado del **minimo** ($A_{min}=A_c(1-\mu)<0$), no del pico.

## Interpretación física

- **Dominio del tiempo:** La envolvente sigue la forma $A_c[1 + \mu m_n(t)]$ modulada a frecuencia $f_c$
- **Dominio de la frecuencia:** El espectro en banda base se traslada a $\pm f_c$, creando portadora + dos bandas laterales

## Generacion practica

**Modulador de ley cuadratica** (el metodo clasico de libro): se suma $m(t)+c(t)$ y se pasa por un dispositivo no lineal (diodo, o transistor en su zona no lineal) con caracteristica $v_{out}=a_1v_{in}+a_2v_{in}^2$. Con $v_{in}=m(t)+c(t)$: [analysis]

$$v_{out} = \underbrace{a_1m(t)}_{\text{banda base}} + \underbrace{a_1c(t)}_{f_c} + \underbrace{a_2m^2(t)}_{\text{banda base}} + \underbrace{2a_2m(t)c(t)}_{f_c\pm f_m} + \underbrace{a_2c^2(t)}_{\text{DC}+2f_c}$$

Los terminos al cuadrado ($m^2(t)$, $c^2(t)$) caen donde caen por la regla general "elevar al cuadrado duplica el ancho de banda" (ver [[#^u9s3nm|derivacion completa en la seccion de potencia]] mas arriba): multiplicar en tiempo convoluciona en frecuencia, y convolucionar dos soportes $[-W,W]$ da $[-2W,2W]$. $m(t)$ esta limitado a $f_m$ → $m^2(t)$ llega a $2f_m$ (sigue en banda base, mas ancho). $c(t)$ es un tono puro (deltas en $\pm f_c$) → autoconvolucionar deltas da $\delta(f-f_c)*\delta(f-f_c)=\delta(f-2f_c)$, entonces $c^2(t)$ cae en DC y $2f_c$, no en $f_c$.

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
