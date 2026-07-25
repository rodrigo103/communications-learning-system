---
tags:
  - wiki/conceptos-integradores
curso: Sistemas de Comunicaciones
unidad: 2
---

# Joseph Fourier y sus Aportes a los Sistemas de Comunicaciones

> **Last verified:** 2026-06-10 | **Verified by:** analysis

Jean-Baptiste Joseph Fourier (1768–1830) fue un matematico y fisico frances cuyo trabajo sobre la descomposicion de funciones periodicas en series trigonometricas se convirtio en la **herramienta matematica fundamental** de las comunicaciones modernas. Todas las tecnicas de modulacion, filtrado y analisis espectral del curso dependen de sus ideas.

## La Transformada de Fourier

Toda señal $x(t)$ puede representarse como una superposicion de exponenciales complejas:

$$\boxed{X(f) = \int_{-\infty}^{\infty} x(t) e^{-j2\pi ft} dt}$$

$$\boxed{x(t) = \int_{-\infty}^{\infty} X(f) e^{j2\pi ft} df}$$

### ¿Por que es el pilar de TODO el curso?

El analisis en frecuencia permite: [analysis]
- Entender el **espectro** de cada modulacion (AM, DSB, SSB, FM, QAM, OFDM)
- Diseñar **filtros** que seleccionen bandas de frecuencia
- Calcular **ancho de banda** y verificar cumplimiento de regulaciones
- Analizar los efectos del **ruido** sobre señales moduladas

## Serie de Fourier (señales periodicas)

Para $x(t)$ periodica con periodo $T_0$:

$$\boxed{x(t) = \sum_{n=-\infty}^{\infty} c_n e^{j2\pi n f_0 t}}$$

Donde $f_0 = 1/T_0$ y los coeficientes $c_n$ representan el espectro discreto de la señal.

Esto es esencial para entender: señales de reloj digital, trenes de pulsos en PAM/PCM, y cualquier señal periodica en comunicaciones.

## Propiedades Fundamentales

| Propiedad       | Tiempo                 | Frecuencia                        |
| --------------- | ---------------------- | ---------------------------------- |
| **Linealidad**  | $a x_1 + b x_2$        | $a X_1 + b X_2$                    |
| **Convolucion** | $x_1 * x_2$            | $X_1 \cdot X_2$                    |
| **Modulacion**  | $x(t) e^{j2\pi f_c t}$ | $X(f - f_c)$                       |
| **Escalado**    | $x(at)$                | $\frac{1}{\lvert a\rvert} X(f/a)$  |
| **Parseval**    | $\int \lvert x\rvert^2 dt$ | $\int \lvert X\rvert^2 df$     |

La propiedad de **modulacion** (traslacion en frecuencia) es la que hace posible toda modulacion analogica y digital: multiplicar por una portadora desplaza el espectro de la señal a la frecuencia deseada. [analysis]

## Convencion $f$ vs $\omega$ — por que este curso usa $f$

Hay dos convenciones para escribir la Transformada de Fourier, y difieren en donde meten el $2\pi$. Vale la pena distinguirlas porque tablas/libros distintos pueden mostrar resultados que a primera vista parecen no coincidir. [analysis]

**Convencion en $f$ (la que usa toda esta materia — formulario, finales, todo lo derivado en la wiki):**

$$X(f) = \int x(t)e^{-j2\pi ft}\,dt, \qquad x(t) = \int X(f)e^{j2\pi ft}\,df$$

El $2\pi$ esta metido *adentro* del exponente, simetrico en ambas direcciones, sin factor extra afuera. Calculando $\mathcal F\{e^{j2\pi f_0t}\}$: $X(f)=\int e^{-j2\pi(f-f_0)t}dt=\delta(f-f_0)$ — sin $2\pi$ sobrante.

**Convencion en $\omega$ (comun en muchos libros/tablas, ej. Oppenheim):**

$$X(\omega) = \int x(t)e^{-j\omega t}\,dt, \qquad x(t) = \frac{1}{2\pi}\int X(\omega)e^{j\omega t}\,d\omega$$

El exponente no lleva $2\pi$ adentro, asi que el $\frac{1}{2\pi}$ aparece afuera, en la inversa, para compensar. Calculando $\mathcal F\{e^{j\omega_0t}\}$: $X(\omega)=\int e^{-j(\omega-\omega_0)t}dt=2\pi\delta(\omega-\omega_0)$ — de ahi sale el $2\pi$ que aparece en tablas escritas en $\omega$.

**Por que son exactamente lo mismo, no dos resultados distintos**: usando la propiedad de escala de la delta, $\delta(ax)=\frac{1}{|a|}\delta(x)$, con $\omega-\omega_0=2\pi(f-f_0)$:

$$2\pi\delta(\omega-\omega_0) = 2\pi\cdot\delta\big(2\pi(f-f_0)\big) = 2\pi\cdot\frac{1}{2\pi}\delta(f-f_0) = \delta(f-f_0)$$

El $2\pi$ de la version en $\omega$ se cancela exacto contra el $\frac{1}{2\pi}$ que sale de la propiedad de escala al cambiar de variable — son el mismo objeto matematico.

**Recomendacion para el final: usar $f$, no $\omega$.** Motivos concretos: (1) es lo que usa el 100% del material real de este curso, nunca aparece $\omega$ con la convencion asimetrica; (2) con $f$ los pares de exponenciales/deltas salen "limpios", sin $2\pi$ sueltos que rastrear bajo presion de tiempo; (3) Parseval queda sin factores extra ($\int|x|^2dt=\int|X|^2df$), coincidiendo con lo derivado via Fubini en [[../herramientas-matematicas/teorema-parseval|Teorema de Parseval]]; (4) todo en el curso se mide en Hz, no en rad/s. Si aparece una tabla en $\omega$, el puente seguro es recordar la equivalencia de arriba en vez de mezclar las dos convenciones a mitad de una cuenta.

### ¿Cuando conviene usar $\omega$ en cambio?

No siempre gana $f$ — hay casos concretos donde $\omega$ es mas conveniente, y de hecho se uso $\omega$ como herramienta intermedia en varias derivaciones de esta misma wiki. [analysis]

1. **Impedancias y circuitos**: $Z_L=j\omega L$, $Z_C=\frac{1}{j\omega C}$ — asi se memorizan siempre, no como $j2\pi fL$. Cualquier derivada temporal se convierte limpio en $j\omega$ ($\frac{d}{dt}\leftrightarrow j\omega$), sin arrastrar un $2\pi$ en cada termino. Filtros, circuitos resonantes: $\omega$ es lo natural.
2. **Transformada de Laplace / dominio $s$**: $s=\sigma+j\omega$, Fourier es el caso particular $s=j\omega$. Diagramas de Bode, polos y ceros, $H(j\omega)$: viven en $\omega$.
3. **Compacidad algebraica en medio de una derivacion larga**: en [[../derivaciones/modulacion-am|Derivacion de Modulacion AM]] (seccion "Deduccion en el dominio del tiempo"), se define $\omega_1=2\pi f_c$, $\omega_2=2\pi(f_c-f_m)$, $\omega_3=2\pi(f_c+f_m)$ especificamente para escribir $\cos(\omega_1t)$ en vez de $\cos(2\pi f_1t)$ repetido en cada paso de la demostracion de ortogonalidad — mas compacto, aunque el resultado final ($BW=2f_m$, potencias) se reporta en $f$.
4. **Frecuencia instantanea sin factor de conversion**: $f_i(t)=\frac{1}{2\pi}\frac{d\phi(t)}{dt}$ (ver [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]]) — el $\frac{1}{2\pi}$ existe solo porque se quiere el resultado en Hz. La **frecuencia angular instantanea** $\omega_i(t):=\frac{d\phi(t)}{dt}$ no lleva factor de conversion — es la derivada de la fase, sin mas.

**La regla practica**: usar $\omega$ como herramienta algebraica intermedia (para no ensuciar una derivacion larga con $2\pi$ repetidos, o cuando aparecen derivadas/impedancias) esta perfecto. Pero el resultado final que se reporta (anchos de banda, frecuencias, en un final de esta materia) siempre va en $f$/Hz, porque es lo que se pide y lo que usa todo el material del curso.

## De Fourier a la Ingenieria Moderna

Sin la transformada de Fourier no existirian: [analysis]
- Ecualizadores y filtros
- Analizadores de espectro
- OFDM (basado enteramente en FFT/IFFT)
- Compresion de audio/video (JPEG, MP3 — via DCT, una variante de Fourier)
- Software Defined Radio (SDR)

→ [[../herramientas-matematicas/teorema-parseval|Teorema de Parseval]]
→ [[../herramientas-matematicas/teorema-convolucion|Teorema de Convolucion]]
→ [[../herramientas-matematicas/densidad-espectral-potencia|Densidad Espectral de Potencia]]

## Ver Tambien

- [[../herramientas-matematicas/teorema-parseval|Teorema de Parseval]]
- [[../herramientas-matematicas/teorema-convolucion|Teorema de Convolucion]]
- [[../herramientas-matematicas/densidad-espectral-potencia|Densidad Espectral de Potencia]]
- [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]]
- [[../conceptos-integradores/aportes-shannon|Aportes de Shannon]]
- [[../conceptos-integradores/aportes-nyquist|Aportes de Nyquist]]
