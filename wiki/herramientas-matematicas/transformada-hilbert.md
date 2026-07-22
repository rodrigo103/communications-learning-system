---
tags:
  - wiki/herramientas-matematicas
source_file: explicaciones_anki/unidad_02/carta_08_transformada_hilbert.md
curso: Sistemas de Comunicaciones
unidad: 2
---

# Transformada de Hilbert

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert]]]

## Definicion

La Transformada de Hilbert $\hat{x}(t)$ de una señal $x(t)$ produce un **desfasaje de -90° para todas las frecuencias positivas** [source — [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert]]]:

$$\hat{x}(t) = \mathcal{H}\{x(t)\} = \frac{1}{\pi} \text{P.V.} \int_{-\infty}^{\infty} \frac{x(\tau)}{t-\tau} d\tau$$

P.V. denota el **valor principal de Cauchy** para manejar la singularidad en $\tau = t$.

## Respuesta en Frecuencia

La Transformada de Hilbert es un sistema LTI con funcion de transferencia [source — [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert]]]:

$$\boxed{H(f) = -j \cdot \text{sgn}(f) = \begin{cases} -j & f > 0 \\ 0 & f = 0 \\ +j & f < 0 \end{cases}}$$

Caracteristicas:
- $|H(f)| = 1$ para $f \neq 0$: **conserva la energia/amplitud**
- Fase = $-90°$ para $f > 0$, $+90°$ para $f < 0$
- Elimina la componente DC ($f = 0$)
- Es una convolucion con $\frac{1}{\pi t}$: $\hat{x}(t) = x(t) * \frac{1}{\pi t}$

## Pares Fundamentales

$$\boxed{\mathcal{H}\{A\cos(2\pi f_0 t + \phi)\} = A\sin(2\pi f_0 t + \phi)}$$

$$\boxed{\mathcal{H}\{A\sin(2\pi f_0 t + \phi)\} = -A\cos(2\pi f_0 t + \phi)}$$

| Señal $x(t)$ | Transformada $\hat{x}(t)$ |
|--------------|---------------------------|
| $\cos(\omega t)$ | $\sin(\omega t)$ |
| $\sin(\omega t)$ | $-\cos(\omega t)$ |
| $\delta(t)$ | $1/(\pi t)$ |
| $1/(\pi t)$ | $-\delta(t)$ |

## Señal Analitica

La señal analitica se construye combinando la señal original con su transformada [source — [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert]]]:

$$x_a(t) = x(t) + j\hat{x}(t)$$

Propiedad clave: su espectro solo contiene **frecuencias positivas**:

$$X_a(f) = \begin{cases} 2X(f) & f > 0 \\ X(0) & f = 0 \\ 0 & f < 0 \end{cases}$$

Esto elimina la redundancia de frecuencias negativas en señales reales.

> **¿Que significa esto y por que se llama "analitica"?** [analysis]
> - *La redundancia que elimina*: toda señal real tiene espectro con simetria hermitica, $X(-f)=X^*(f)$ — la mitad de frecuencias negativas no aporta informacion nueva, es el espejo conjugado de la positiva. La señal analitica empaqueta toda la informacion en un espectro de un solo lado, sin perder nada (siempre se recupera $x(t)=\text{Re}\{x_a(t)\}$).
> - *Por que hace falta para tener amplitud/fase instantanea bien definidas*: por Euler, $\cos(\omega t)=\tfrac12 e^{j\omega t}+\tfrac12 e^{-j\omega t}$ — un coseno real es la suma de dos fasores girando en direcciones opuestas, y por si solo es ambiguo (no se le puede asignar una unica direccion de giro). La Transformada de Hilbert cancela uno de los dos fasores y deja solo el que gira en sentido positivo, dando $x_a(t)=a(t)e^{j\phi(t)}$ con amplitud $a(t)=|x_a(t)|$ y fase $\phi(t)=\angle x_a(t)$ instantaneas bien definidas — de ahi sale su uso para envolvente en AM y frecuencia instantanea en FM.
> - *De donde sale el nombre*: si se extiende $t$ a un plano complejo, $x_a(t)$ es el valor de borde de una funcion **analitica/holomorfa** (derivable en sentido complejo, cumple Cauchy-Riemann) en el semiplano superior — condicion que se cumple *solo* cuando no hay frecuencias negativas, que es justo lo que garantiza la Transformada de Hilbert. Conecta con las relaciones de Kramers-Kronig (fuera del alcance del final, pero es el origen del nombre).

## Aplicaciones en Comunicaciones

### 1. Generacion de SSB (Banda Lateral Unica)

La señal SSB se genera usando la transformada de Hilbert [source — [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert]]]:

$$s_{SSB}(t) = m(t)\cos(2\pi f_c t) \mp \hat{m}(t)\sin(2\pi f_c t)$$

- Signo $(-)$: USB (Upper Sideband)
- Signo $(+)$: LSB (Lower Sideband)

Ver [[../modulacion-analogica/modulacion-ssb]] para detalles.

### 2. Deteccion de Envolvente en AM

Para una señal AM $r(t)$, la envolvente se extrae via:

$$|r_a(t)| = |r(t) + j\hat{r}(t)|$$

### 3. Frecuencia Instantanea en FM

Para una señal FM $s(t)$, la frecuencia instantanea se calcula como:

$$f_i(t) = \frac{1}{2\pi}\frac{d}{dt}\angle s_a(t)$$

## Analogia

La Transformada de Hilbert es como ver una onda desde una posicion rotada 90°. Ambas vistas describen la misma onda pero desde perspectivas ortogonales. La señal analitica combina ambas vistas para una descripcion completa [analysis].

## Puntos Clave

- ✓ NO cambia el contenido de frecuencias, solo las fases [source — [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert]]]
- ✓ $|H(f)| = 1$ para $f \neq 0$: conserva energia
- ✓ Solo definida para señales reales
- ✓ La señal analitica elimina frecuencias negativas

## Preguntas y Respuestas (dudas resueltas en sesion de estudio)

**¿A fines practicos, la Transformada de Hilbert se usa siempre solo sobre senos/cosenos?**

En la practica de este curso, casi seguro que si. En los 13 finales resueltos revisados (`exercises/finales/md/`) la palabra "Hilbert" no aparece ni una vez como parte de un calculo — los "$P_{SSB}$" que aparecen en varios ejercicios son la potencia de una banda lateral dentro de una señal AM/DSB, no señales SSB generadas via Hilbert. Todas las señales moduladoras de los finales son sumas de tonos senoidales. Como la Transformada de Hilbert es lineal, para $m(t)=\sum_i A_i\cos(\omega_i t+\phi_i)$ alcanza con aplicar el par fundamental termino a termino: $\hat m(t)=\sum_i A_i\sin(\omega_i t+\phi_i)$ — no hace falta la integral general (valor principal de Cauchy) para resolver un problema, esa forma es para la definicion/demostracion. Ojo: si algun dia dan una $m(t)$ que no sea suma de senos/cosenos, ahi si hace falta ir a $H(f)=-j\,\text{sgn}(f)$. [analysis]

**¿Cual es el espectro del seno y del coseno? ¿Uno de los dos es impar y por eso no tiene simetria hermitica?**

$$\cos(2\pi f_0 t) \leftrightarrow \frac{1}{2}\big[\delta(f-f_0)+\delta(f+f_0)\big] \quad\text{— real y par}$$
$$\sin(2\pi f_0 t) \leftrightarrow -\frac{j}{2}\delta(f-f_0)+\frac{j}{2}\delta(f+f_0) \quad\text{— imaginario puro e impar}$$

Correccion importante: la **simetria hermitica** ($X(-f)=X^*(f)$) se cumple para **toda** señal real, sin excepcion — no depende de que la señal sea par o impar en el tiempo. Demostracion corta: $X^*(f) = \left(\int x(t)e^{-j2\pi ft}dt\right)^* = \int x^*(t)e^{j2\pi ft}dt \overset{x\text{ real}}{=} \int x(t)e^{j2\pi ft}dt = X(-f)$ — el argumento solo usa que $x^*(t)=x(t)$ (real), nunca paridad. El seno tambien cumple $X(-f)=X^*(f)$ (se puede verificar directo con la formula de arriba). Lo que si depende de la paridad es una propiedad *distinta*, mas especifica: real+par$\to$espectro real y par (coseno); real+impar$\to$espectro imaginario puro e impar (seno); real sin paridad definida$\to$espectro complejo con parte real par + parte imaginaria impar. Las tres son casos particulares de simetria hermitica, no excepciones a ella. [analysis]

**¿El concepto de señal analitica se relaciona con las funciones FRP (Funcion Real Positiva, de Teoria de Circuitos)? ¿Son conceptos fisicos o matematicos?**

*(Asumiendo que FRP = Funcion Real Positiva — no confirmado, no aparece en el material del curso.)* La conexion es real: una FRP caracteriza que funciones $Z(s)$ son fisicamente realizables como impedancia de una red pasiva (R, L, C), via el teorema de Brune. La condicion matematica de fondo es la misma familia que la señal analitica: ambas dependen de que una funcion sea analitica/holomorfa en un semiplano (la señal analitica en el semiplano superior del tiempo complejo; la FRP en el semiplano derecho de $s$). En ambos casos esa analiticidad fuerza una relacion tipo Hilbert entre parte real e imaginaria en el eje de frecuencias — en fisica son las relaciones de Kramers-Kronig, en teoria de circuitos las relaciones de Bode ganancia-fase. Son conceptos **matematicos** (analisis complejo) que se usan porque capturan una restriccion **fisica**: causalidad (señal analitica) o realizabilidad pasiva (FRP). El hilo comun: un sistema fisico causal/realizable impone automaticamente una relacion de Hilbert entre las partes real e imaginaria de su respuesta en frecuencia. [analysis]

## Ver tambien

- [[../herramientas-matematicas/teorema-convolucion]]
- [[../modulacion-analogica/modulacion-ssb]]
- [[../introduccion/modelo-shannon]]
