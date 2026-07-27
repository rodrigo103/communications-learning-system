---
tags:
  - wiki/derivaciones
  - wiki/modulacion-analogica
source_file: outputs/derivations/FM_Carson_parallel_20251115.md
curso: Sistemas de Comunicaciones
unidad: 4
---

# Derivación de FM y Regla de Carson

> **Last verified:** 2025-11-15 | **Verified by:** source

## Fundamento: modulación angular

Una señal modulada en ángulo tiene la forma general:

$$s(t) = A_c \cos[2\pi f_c t + \phi(t)]$$

donde $\phi(t)$ es la desviación de fase variable en el tiempo.

### Frecuencia instantánea

La frecuencia instantánea se define como la derivada de la fase instantánea:

$$f_i(t) = f_c + \frac{1}{2\pi}\frac{d\phi(t)}{dt}$$

## FM: definición fundamental

En **Frequency Modulation (FM)**, la desviación de frecuencia instantánea es proporcional al mensaje:

$$f_i(t) = f_c + k_f m(t)$$

donde $k_f$ es la sensibilidad de frecuencia [Hz/V] [source — [[../../outputs/derivations/FM_Carson_parallel_20251115]]].

Integrando para obtener la fase:

$$\phi(t) = 2\pi k_f \int_{-\infty}^{t} m(\tau) d\tau$$

La señal FM completa es:

$$\boxed{s_{FM}(t) = A_c \cos\left[2\pi f_c t + 2\pi k_f \int_{-\infty}^{t} m(\tau) d\tau\right]}$$

## Modulación con tono único

Para $m(t) = A_m \cos(2\pi f_m t)$:

### Desviación de frecuencia

$$\boxed{\Delta f = k_f A_m}$$

Es la máxima excursión de frecuencia respecto a $f_c$.

### Índice de modulación

$$\boxed{\beta = \frac{\Delta f}{f_m}}$$

$\beta$ determina el ancho de banda y si la FM es de banda angosta o ancha [analysis].

### Señal FM con tono único

Sustituyendo:

$$\boxed{s_{FM}(t) = A_c \cos[2\pi f_c t + \beta \sin(2\pi f_m t)]}$$

## Espectro FM: funciones de Bessel

Usando la identidad de Jacobi-Anger:

$$s_{FM}(t) = A_c \sum_{n=-\infty}^{\infty} J_n(\beta) \cos[2\pi(f_c + n f_m)t]$$

donde $J_n(\beta)$ son las funciones de Bessel de primera especie [source — [[../../outputs/derivations/FM_Carson_parallel_20251115]]].

El espectro FM contiene **infinitas bandas laterales** (a diferencia de AM que tiene solo 2), pero las amplitudes $J_n(\beta)$ decaen con $n$.

### Propiedades de Bessel relevantes

- $J_0(0) = 1$, $J_n(0) = 0$ para $n \neq 0$
- $\sum_{n=-\infty}^{\infty} J_n^2(\beta) = 1$ (conservación de potencia)
- Para $\beta \ll 1$: $J_0(\beta) \approx 1$, $J_1(\beta) \approx \beta/2$, $J_n(\beta) \approx 0$ para $n > 1$
- Bandas significativas: aproximadamente $\beta + 1$ pares con $|J_n(\beta)| > 0.01$

## Regla de Carson

La regla de Carson estima el ancho de banda que contiene ~98% de la potencia:

$$\boxed{BW_{Carson} = 2(\Delta f + f_m) = 2f_m(\beta + 1)}$$

Para una señal general con ancho de banda $B$:

$$\boxed{BW_{Carson} = 2(\Delta f + B)}$$

### Precisión

Comparada con el ancho de banda exacto (corte al 1% por Bessel), Carson tiene un error de aproximadamente $\pm 10\%$ para valores prácticos de $\beta$ [analysis].

## Multiplicadores y mezcladores de frecuencia (el patrón más testeado)

Aparece constantemente en los finales ("se la pasa por un cuadruplicador", "por tres duplicadores en serie"). La regla operativa es: un multiplicador $\times n$ **multiplica la fase entera**, con lo cual $f_c\to nf_c$, $\Delta f\to n\Delta f$, $\beta\to n\beta$ — pero **$f_m$ no cambia**. Justificación: [analysis]

### Por qué el multiplicador multiplica la fase

Un multiplicador de frecuencia es un **dispositivo no lineal seguido de un filtro pasabanda**. El caso más simple, elevar al cuadrado, ya lo muestra todo. Con $s(t)=A\cos\phi(t)$:

$$s^2(t) = A^2\cos^2\phi(t) = \frac{A^2}{2}\big[1+\cos(2\phi(t))\big]$$

El filtro pasabanda centrado en $2f_c$ elimina el término de continua y deja $\propto\cos(2\phi(t))$: **la fase se duplicó**, $\phi\to2\phi$. Para $\times n$ se usa una no linealidad de orden superior (o duplicadores en cascada) y se filtra el armónico $n$-ésimo, dando $\phi\to n\phi$.

### Por qué eso escala $f_c$ y $\Delta f$ pero no $f_m$

Sustituyendo la fase de FM con tono único, $\phi(t)=2\pi f_ct+\beta\sin(2\pi f_mt)$:

$$n\phi(t) = 2\pi (nf_c)\,t + n\beta\sin(2\pi f_mt)$$

Leyendo término a término está todo:

- $2\pi f_ct \to 2\pi(nf_c)t$ → **portadora $\times n$**
- $\beta \to n\beta$ → **índice $\times n$**, porque $\beta$ es un **coeficiente afuera** del seno
- $\sin(2\pi f_mt)$ → **intacto**, porque $f_m$ vive **adentro del argumento** del seno, y multiplicar la fase por $n$ no toca argumentos internos

Y de $\Delta f=\beta f_m$: como $\beta$ se multiplica por $n$ y $f_m$ queda igual, $\Delta f\to n\Delta f$. **Ese es el punto entero**: $\beta$ está afuera (escala), $f_m$ está adentro (no escala).

**Vía frecuencia instantánea (más directo aún)**: si $\phi\to n\phi$, entonces $f_i=\frac{1}{2\pi}\frac{d\phi}{dt}\to n\,f_i$, o sea la función completa se multiplica por $n$:

$$f_i(t) = f_c+\Delta f\cos(2\pi f_mt) \quad\longrightarrow\quad n f_i(t) = nf_c + n\Delta f\cos(2\pi f_mt)$$

El centro y la excursión se escalan por $n$, pero **la velocidad a la que oscila** (que es $f_m$) no cambia — solo se agrandó el vaivén, no se aceleró.

### Cómo se implementa físicamente

No se construye literalmente un "elevador al cuadrado". Se usa un dispositivo **naturalmente no lineal**, que genera *todos* los armónicos a la vez, y un circuito sintonizado que selecciona el deseado: [analysis]

| Implementación | Cómo genera armónicos |
|---|---|
| **Amplificador clase C con tanque sintonizado** (el clásico en transmisores) | Conduce solo una fracción chica del ciclo → tren de pulsos angostos → espectro rico en armónicos. El tanque LC de salida se sintoniza en $nf_c$ y filtra el resto. |
| **Diodo varactor** | Capacidad que varía con la tensión = reactancia no lineal. Excitado fuerte genera armónicos, y al ser reactivo (no resistivo) casi no disipa → alta eficiencia. Típico en microondas. |
| **Step-recovery diode (snap diode)** | Produce pulsos extremadamente abruptos, muy ricos en armónicos. Sirve para factores altos ($\times10$ o más). |
| **PLL con divisor $\div N$ en el lazo** | Mecanismo distinto (realimentación, no generación de armónicos): al enganchar, la fase del VCO queda $N$ veces la de la referencia. Es como se hace hoy en sintetizadores. |

**El argumento general que cubre todos los casos**: si $x=A\cos\phi$ entra a cualquier no linealidad $y=f(x)$, la salida es periódica en $\phi$, así que admite serie de Fourier en $\phi$:

$$y = \sum_n c_n\cos(n\phi)$$

**Todos los armónicos están presentes** — la no linealidad concreta solo determina los pesos $c_n$. El filtro elige el término $n$-ésimo y queda $\cos(n\phi)$. Por eso da igual si es un diodo, un transistor en clase C o un varactor: el mecanismo matemático es el mismo, y el $\phi\to n\phi$ vale en todos.

### Triplicador (y por qué en la práctica se cascadean duplicadores)

Elevar al cubo, usando $\cos^3\theta=\tfrac34\cos\theta+\tfrac14\cos3\theta$ (sale de $\cos^3=\cos\cdot\cos^2$ más producto-a-suma):

$$s^3(t) = A^3\cos^3\phi(t) = A^3\Big[\underbrace{\tfrac34\cos\phi(t)}_{\text{en } f_c} + \underbrace{\tfrac14\cos3\phi(t)}_{\text{en } 3f_c}\Big]$$

El pasabanda en $3f_c$ deja $\propto\cos(3\phi(t))$, o sea $\phi\to3\phi$, y de ahí $3\phi(t)=2\pi(3f_c)t+3\beta\sin(2\pi f_mt)$ — misma estructura que el duplicador.

**Dos consecuencias prácticas que salen de la propia cuenta:**

- **El armónico útil es débil**: el término de $3f_c$ tiene coeficiente $\tfrac14$ contra $\tfrac34$ del fundamental, y empeora con el orden $n$. Por eso los multiplicadores reales se limitan a $n$ chico por etapa ($\times2$, $\times3$) y se **cascadean con amplificación entre etapas**.
- **Por eso los finales dicen "tres duplicadores en serie"** en vez de "un multiplicador $\times8$" — refleja cómo se hace en serio. Matemáticamente es lo mismo: $\phi\to2\phi\to4\phi\to8\phi$, o sea $\beta\to8\beta$, $\Delta f\to8\Delta f$, $f_c\to8f_c$.

### La amplitud

En el $s^2(t)$ de arriba la amplitud sí cambia ($A\to A^2/2$). En la práctica el multiplicador va seguido de un **limitador/amplificador** que normaliza la amplitud, y por eso los enunciados aclaran "la amplitud de la señal permanece sin cambio". Como en FM la potencia es $P=A_c^2/2R$ independiente de la modulación, si la amplitud no cambia **la potencia tampoco** — pase lo que pase con $\beta$.

### Multiplicador vs mezclador: una sola operación, dos segundas entradas

Distinción que los finales testean, y es la razón de ser del [[../modulacion-analogica/modulador-armstrong|modulador Armstrong]]. Lo importante es que **no son dos operaciones distintas**: ambos multiplican dos señales y filtran un término, y multiplicar **suma las fases**: [analysis]

$$\cos\phi_1\cos\phi_2 = \tfrac12\big[\underbrace{\cos(\phi_1-\phi_2)}_{\text{diferencia}} + \underbrace{\cos(\phi_1+\phi_2)}_{\text{suma}}\big]$$

Todo lo demás depende de **qué se pone en $\phi_2$**:

| Caso                 | $\phi_2$                            | Fase de salida (término suma)                 | Efecto                              |
| -------------------- | ----------------------------------- | --------------------------------------------- | ----------------------------------- |
| **Mezclador** con OL | $2\pi f_{OL}t$ (**sin modulación**) | $2\pi(f_c{+}f_{OL})t+\beta\sin(2\pi f_mt)$    | traslada $f_c$, $\beta$ **intacto** |
| **Duplicador**       | $\phi_1$ (**la señal misma**)       | $2\phi_1 = 2\pi(2f_c)t+2\beta\sin(2\pi f_mt)$ | escala $f_c$ **y** $\beta$          |

#### De dónde sale cada fila de la tabla

**Deducción general.** Escribiendo cada fase separada en su **parte de portadora** (lineal en $t$) y su **parte de modulación**:

$$\phi_1(t) = 2\pi f_1 t + \psi_1(t), \qquad \phi_2(t) = 2\pi f_2 t + \psi_2(t)$$

El término suma, agrupando:

$$\phi_1+\phi_2 = \underbrace{2\pi f_1t + 2\pi f_2t}_{\text{lineales en }t} + \underbrace{\psi_1(t)+\psi_2(t)}_{\text{modulaciones}} = \boxed{2\pi(f_1{+}f_2)\,t + \big[\psi_1(t)+\psi_2(t)\big]}$$

El paso clave es **sacar $2\pi t$ como factor común** de los dos términos lineales — de ahí sale que las portadoras se suman. Las partes de modulación, al no ser lineales en $t$, no se pueden agrupar con esas: quedan sumándose aparte. O sea: **las portadoras se suman entre sí, y las modulaciones entre sí**, sin mezclarse. Las dos filas de la tabla son especializaciones de esto.

**Fila 1 — mezclador** ($f_2=f_{OL}$, $\psi_2=0$):

$$A\cos\phi_1(t)\cdot\cos(2\pi f_{OL}t) = \frac{A}{2}\big[\cos(\phi_1-\phi_2)+\cos(\phi_1+\phi_2)\big]$$

Desarrollando el término suma paso a paso:

$$\phi_1+\phi_2 = \big[2\pi f_ct + \beta\sin(2\pi f_mt)\big] + 2\pi f_{OL}t = 2\pi f_ct + 2\pi f_{OL}t + \beta\sin(2\pi f_mt)$$
$$= 2\pi(f_c{+}f_{OL})\,t + \beta\sin(2\pi f_mt)$$

**El OL no tiene con qué modificar la modulación**: su fase es puramente lineal en $t$ ($\psi_2=0$), así que $\beta\sin(2\pi f_mt)$ **atraviesa sin tocarse** y solo se movió la portadora. (El término diferencia da lo mismo pero con $f_c-f_{OL}$; el filtro elige cuál queda.)

**Fila 2 — duplicador** ($f_2=f_c$, $\psi_2=\psi_1=\beta\sin(2\pi f_mt)$):

$$A\cos\phi_1(t)\cdot A\cos\phi_1(t) = A^2\cos^2\phi_1 = \frac{A^2}{2}\big[\cos(\phi_1-\phi_1)+\cos(\phi_1+\phi_1)\big]$$

El término suma es $2\phi_1$, y **el factor 2 se distribuye sobre los dos términos**:

$$2\phi_1 = 2\big[2\pi f_ct + \beta\sin(2\pi f_mt)\big] = 2\cdot2\pi f_ct + 2\beta\sin(2\pi f_mt) = 2\pi(2f_c)\,t + 2\beta\sin(2\pi f_mt)$$

Notar **dónde entra cada 2**: en el primer término se absorbe dentro de la frecuencia ($2\cdot2\pi f_ct = 2\pi(2f_c)t$ → portadora al doble); en el segundo queda como **coeficiente del seno** ($\beta\to2\beta$), sin poder entrar al argumento — y por eso $f_m$ no se toca.

**Regla unificada** (que ahora es consecuencia, no afirmación): el término de modulación de la salida es **la suma de los términos de modulación de las dos entradas**. El oscilador local tiene $\psi_2=0$, así que $\beta$ ni se entera. La señal misma tiene $\psi_2=\psi_1$, así que la modulación se duplica junto con la portadora.

> **Confirmación de que es literalmente el mismo mecanismo**: en el duplicador, ¿dónde esta el término *diferencia*? Es $\cos(\phi_1-\phi_1)=\cos 0=1$ — **la continua**. Y efectivamente $\cos^2\phi=\tfrac12[1+\cos2\phi]$: ese "$1$" que arriba se describió como "el término de continua que el filtro elimina" **es** la salida de frecuencia-diferencia del mezclador con las dos entradas iguales. No hay dos fenómenos, hay uno. [analysis]
>
> Consecuencia: un **triplicador** también se puede armar mezclando la señal con su propia versión duplicada ($2\phi+\phi=3\phi$), sin necesidad de una no linealidad cúbica.

### ¿Son entonces el mismo dispositivo físico? No — y por qué

Matemáticamente es una sola operación, pero **los circuitos son distintos**, elegidos por eficiencia y nivel de potencia (no por la matemática): [analysis]

| | Mezclador | Multiplicador de transmisor |
|---|---|---|
| **Puertos de entrada** | **Dos** (RF y OL) | **Uno solo** — no hay dónde meter una segunda señal |
| **Circuitos típicos** | Anillo de diodos (doble balanceado), celda de Gilbert | Clase C con tanque sintonizado, varactor, SRD |
| **Nivel de potencia** | Bajo (procesamiento de señal) | Alto (etapa de transmisor, watts a kW) |
| **Eficiencia** | Tiene **pérdida** de conversión (−6 a −8 dB en diodos) | Clase C llega a 70–80% |

Un multiplicador clase C **no es** un mezclador con las entradas unidas: es una topología de un solo puerto que genera armónicos a partir de una forma de onda pulsada. **Pero los conjuntos se superponen**: un mezclador con las dos entradas unidas *sí* funciona como duplicador, y se hace — típicamente a bajo nivel, dentro de un chip. Lo que no se hace es usarlo en la etapa de potencia de un transmisor, donde la pérdida de conversión es inaceptable.

### Por qué esto importa para Armstrong

Como el mezclador traslada la portadora **sin tocar la desviación**, y el multiplicador escala **ambas**, el [[../modulacion-analogica/modulador-armstrong|modulador Armstrong]] usa cada uno para lo suyo: **multiplicadores para subir $\beta$** (de NBFM a WBFM) y **mezcladores para ubicar la portadora final** en la frecuencia deseada sin arruinar el $\beta$ ya conseguido. Si se usara un multiplicador para corregir la frecuencia final, se volvería a cambiar $\Delta f$ y habría que rehacer todo.

## Clasificación: NBFM vs WBFM

| Tipo | Condición | Ancho de banda |
|------|-----------|----------------|
| **NBFM** | $\beta < 0.3$ | $BW \approx 2f_m$ |
| **WBFM** | $\beta > 1$ | $BW \approx 2\Delta f$ |

## Ejemplo: FM broadcast

- $\Delta f = 75$ kHz, $f_m = 15$ kHz, $\beta = 5$
- $BW = 2(75 + 15) = 180$ kHz
- Asignación práctica: 200 kHz (con bandas de guarda)

## Ganancia SNR en FM

Para WBFM, la mejora de SNR respecto a AM es:

$$\frac{SNR_{FM}}{SNR_{AM}} \approx \frac{3\beta^3}{2}$$

FM intercambia ancho de banda por SNR: $SNR_{FM} \propto \beta^2 \propto BW^2$ [analysis].

## Ver también

- [[../modulacion-analogica/ancho-banda-carson]]
- [[../modulacion-analogica/fm-vs-pm]]
- [[../derivaciones/modulacion-fm-banda-angosta]]
- [[../modulacion-analogica/funciones-bessel]]
- [[../ruido/efecto-umbral-fm]]
