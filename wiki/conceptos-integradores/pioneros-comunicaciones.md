---
tags:
  - wiki/conceptos-integradores
curso: Sistemas de Comunicaciones
---

# Pioneros de las Comunicaciones

> **Last verified:** 2026-06-10 | **Verified by:** analysis

Documento que recopila las contribuciones de figuras clave en la historia de las telecomunicaciones, organizadas por area de impacto. Las figuras con aportes multiples en el curso tienen pagina dedicada.

---

## Indice

1. [Precursores EM](#precursores-electromagneticos)
2. [Pioneros de la Radio](#pioneros-de-la-radio)
3. [Herramientas Matematicas](#herramientas-matematicas)
4. [Teoria de la Informacion y Codificacion](#teoria-de-la-informacion-y-codificacion)
5. [Sistemas Digitales y Redes](#sistemas-digitales-y-redes)
6. [Ruido](#ruido)

---

## Precursores Electromagneticos

### James Clerk Maxwell (1831–1879)

Formulo las **ecuaciones de Maxwell**, que unificaron electricidad y magnetismo y predijeron la existencia de ondas electromagneticas:

$$\nabla \cdot \mathbf{D} = \rho, \quad \nabla \cdot \mathbf{B} = 0, \quad \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}, \quad \nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$$

Sin estas ecuaciones, no existiria el concepto de propagacion de ondas electromagneticas ni, por tanto, las comunicaciones inalambricas. Su trabajo teorico es el punto de partida de todo el espectro electromagnetico que usamos. [analysis]

### Michael Faraday (1791–1867)

Descubrio la **induccion electromagnetica** (1831), el principio fisico detras de generadores, transformadores y antenas. Su concepto de "lineas de fuerza" fue la intuicion que Maxwell formalizo matematicamente. [analysis]

### Heinrich Hertz (1857–1894)

Demostro experimentalmente la existencia de ondas electromagneticas en 1886, confirmando las predicciones de Maxwell. Probo que se reflejan, refractan y polarizan igual que la luz. Su nombre perdura como la unidad de frecuencia:

$$\boxed{1 \text{ Hz} = 1 \text{ ciclo por segundo}}$$

[analysis]

### Andre-Marie Ampere (1775–1836)

Formulo las leyes del **electromagnetismo** que llevan su nombre (Ley de Ampere). Su trabajo sobre la interaccion entre corrientes electricas sento las bases para entender la propagacion guiada. La unidad de corriente electrica lleva su nombre. [analysis]

### Nikola Tesla (1856–1943)

Pionero de la **corriente alterna** y las comunicaciones inalambricas. Invento la **bobina de Tesla** y demostro la transmision de energia sin cables. Aunque su vision de energia inalambrica global no se materializo, sus patentes sentaron las bases de la radio. [analysis]

---

## Pioneros de la Radio

### Guglielmo Marconi (1874–1937)

Realizo la **primera transmision transatlantica** de radio (1901). Aunque uso tecnologia existente (como el detector de Branly), fue el primero en demostrar la viabilidad comercial de las comunicaciones inalambricas de larga distancia. Premio Nobel de Fisica (1909), compartido con Braun. [analysis]

### Karl Ferdinand Braun (1850–1918)

Invento el **detector de cristal** (rectificador de contacto puntual semiconductor), fundamental para los primeros receptores de radio. Co-creador de la telegrafia inalambrica. El diodo semiconductor moderno desciende directamente de su trabajo. Premio Nobel de Fisica (1909), compartido con Marconi. [analysis]

### Charles Wheatstone (1802–1875)

Invento el **puente de Wheatstone** para medir resistencias con precision. Contribuyo al desarrollo del **telegrafo electrico** y la telegrafia submarina. Su trabajo en circuitos electricos es fundamental para la electronica de comunicaciones. [analysis]

### Samuel Morse (1791–1872)

Invento el **telegrafo electrico** (1837) y desarrollo el **codigo Morse**, el primer esquema practico de codificacion digital: asignar patrones de pulsos cortos y largos a letras segun su frecuencia de uso (similar a como Huffman optimizaria codigos un siglo despues). La telegrafia fue la primera red de comunicacion digital global. [analysis]

### Alexander Graham Bell (1847–1922)

Invento el **telefono** (1876), el primer sistema de comunicacion de voz en tiempo real. Fundo los **Laboratorios Bell** (1925), donde trabajarian Shannon, Nyquist, Friis, Johnson y la mayoria de las figuras que construyeron la teoria de comunicaciones. La unidad logaritmica $dB$ (decibel) lleva su nombre. [analysis]

### Edwin Howard Armstrong

→ [[../conceptos-integradores/aportes-armstrong|Aportes de Armstrong]] — pagina dedicada

### John R. Carson (1886–1940)

→ [[../conceptos-integradores/aportes-carson|Aportes de Carson]] — pagina dedicada (regla de Carson para FM, modulador balanceado DSB-SC, pre-enfasis)

---

## Herramientas Matematicas

### Marc-Antoine Parseval (1755–1836)

→ [[../conceptos-integradores/aportes-parseval|Aportes de Parseval]] — pagina dedicada (conservacion de energia tiempo-frecuencia, base de Wiener-Khinchin)

### Joseph Fourier

→ [[../conceptos-integradores/aportes-fourier|Aportes de Fourier]] — pagina dedicada

### David Hilbert (1862–1943)

→ [[../conceptos-integradores/aportes-hilbert|Aportes de Hilbert]] — pagina dedicada (transformada de Hilbert, señal analitica, SSB por fase)

### Hendrik Bode (1905–1982)

Desarrollo los **diagramas de Bode**, la herramienta grafica estandar para analizar la respuesta en frecuencia de filtros y amplificadores. Su **integral de sensibilidad de Bode** establece limites fundamentales al diseño de sistemas realimentados: no se puede mejorar el desempeño en una banda sin empeorarlo en otra. Aunque su aplicacion directa es en teoria de control, sus conceptos son utiles para entender limitaciones de ecualizadores y filtros en comunicaciones. [analysis]

---

## Teoria de la Informacion y Codificacion

### Ralph Hartley (1888–1970)

Precursor de la teoria de la informacion. En 1928 propuso que la cantidad de informacion transmitida es proporcional a $\log m$, donde $m$ es el numero de mensajes posibles. Su formula $C = B \log_2(1 + S/N)$ sin el termino $(1 + S/N)$ fue la base que Shannon generalizo. [analysis]

→ [[../teoria-informacion/teorema-shannon-hartley|Teorema de Shannon-Hartley]]

### Claude Shannon

→ [[../conceptos-integradores/aportes-shannon|Aportes de Shannon]] — pagina dedicada

### David Huffman (1925–1999)

Creo el **algoritmo de Huffman** (1952), que construye un codigo prefijo optimo sin perdida minimizando la longitud promedio:

$$\boxed{\bar{L}_{opt} = \min \sum l_i p_i}$$

Usado universalmente en compresion de datos (ZIP, PNG, JPEG, MP3). El algoritmo demuestra que se puede alcanzar el limite teorico $H \leq \bar{L} < H + 1$ establecido por Shannon. [analysis]

→ [[../teoria-informacion/codigo-compacto|Codigos Compactos]]

### Richard Hamming (1915–1998)

Invento los **codigos de Hamming** (1950), los primeros codigos correctores de errores practicos. Un codigo Hamming(7,4) usa 7 bits para transmitir 4 bits de datos, pudiendo corregir 1 error:

$$\boxed{d_{min} = 3 \implies \text{corrige } \lfloor (d_{min}-1)/2 \rfloor = 1 \text{ error}}$$

La **distancia de Hamming** ($d_{min}$) es la metrica fundamental para determinar la capacidad de deteccion/correccion de cualquier codigo. [analysis]

→ [[../teoria-informacion/codigos-deteccion-error|Codigos Detectores y Correctores]]

### Robert Gallagher (n. 1931)

Invento los **codigos LDPC** (Low-Density Parity-Check) en 1960. En su momento fueron ignorados por requerir demasiado procesamiento, pero fueron "redescubiertos" en los 1990s y hoy son usados en WiFi (802.11n/ac/ax), 5G, y DVB-S2. Se acercan a **~0.004 dB** del limite de Shannon — lo mas cercano jamas logrado. [analysis]

### Claude Berrou (n. 1951)

Invento los **Turbo codes** (1993), que revolucionaron la correccion de errores al demostrar por primera vez que un codigo practico podia operar a solo **0.5 dB** del limite de Shannon. Usados en 3G y 4G LTE. [analysis]

→ [[../teoria-informacion/codigos-deteccion-error|Codigos Detectores y Correctores]]

---

## Sistemas Digitales y Redes

### Alec Reeves (1902–1971)

Invento el **PCM (Pulse Code Modulation)** en 1937, la tecnica fundamental de digitalizacion que sustenta toda la telefonia digital, audio digital, y comunicaciones modernas:

$$\boxed{\text{PCM: Muestrear} \rightarrow \text{Cuantificar} \rightarrow \text{Codificar}}$$

Su idea era adelantada a su epoca; no fue practica hasta la invencion del transistor. [analysis]

→ [[../modulacion-pulsos/pcm-cuantificacion|PCM y Cuantificacion]]

### Andrew Viterbi (1935–2023)

Invento el **algoritmo de Viterbi** (1967) para decodificar codigos convolucionales con maxima verosimilitud. Fundo Qualcomm con Irwin Jacobs y fue co-inventor del **CDMA**, la tecnologia base de 3G. El algoritmo se usa tambien en reconocimiento de voz, NLP, y bioinformatica. [analysis]

### Irwin Jacobs (n. 1933)

Co-fundador de **Qualcomm** y co-inventor del **CDMA** comercial. Su vision de que CDMA era superior a TDMA para sistemas moviles transformo la industria de las telecomunicaciones. [analysis]

→ [[../espectro-expandido/cdma|CDMA]]

### John R. Pierce (1910–2002)

Pionero de las **comunicaciones satelitales**. En los Laboratorios Bell, propuso y ayudo a desarrollar los primeros satelites de comunicacion (Echo 1, Telstar). Tambien acuno el termino "**transistor**" para el invento de Bardeen, Brattain y Shockley. [analysis]

### Leonard Kleinrock (n. 1934)

Desarrollo la teoria de **conmutacion de paquetes** (packet switching) en su tesis doctoral del MIT (1962), estableciendo las bases matematicas de Internet. Su trabajo sobre colas y teoria de trafico es fundamental para entender el comportamiento de redes de datos. [analysis]

### Vint Cerf (n. 1943) y Bob Kahn (n. 1938)

Co-inventores del protocolo **TCP/IP** (1974), la arquitectura fundamental de Internet. La separacion de responsabilidades entre TCP (transporte confiable) e IP (enrutamiento) es un ejemplo magistral de diseño de sistemas de comunicaciones en capas. [analysis]

---

## Ruido

### Harald Friis (1893–1976)

Dos contribuciones fundamentales para el diseño de radioenlaces:

**Formula de Friis para ruido en cascada** — si hay $N$ etapas en serie, el factor de ruido total es:

$$\boxed{F_{total} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots}$$

*La primera etapa (LNA) domina la figura de ruido del receptor completo.* [analysis]

**Formula de transmision de Friis** — potencia recibida en espacio libre:

$$\boxed{P_r = P_t G_t G_r \left(\frac{\lambda}{4\pi d}\right)^2}$$

[analysis]

→ [[../ruido/formula-friis|Formula de Friis]]
→ [[../ruido/intercomparacion-sistemas|Intercomparacion de Sistemas]]

### John B. Johnson (1887–1970)

Descubrio experimentalmente el **ruido termico** en conductores (1926), midiendo la tension fluctuante en resistencias. Nyquist lo explico teoricamente en 1927. El ruido termico se conoce como **ruido Johnson-Nyquist**:

$$\boxed{v_n^2 = 4kTRB}$$

Donde $k = 1.38 \times 10^{-23}$ J/K, $T$ en Kelvin, $R$ en $\Omega$, $B$ en Hz. A temperatura ambiente (290 K): $N_0 = kT \approx 4 \times 10^{-21}$ W/Hz $= -174$ dBm/Hz. [analysis]

→ [[../ruido/fuentes-ruido|Fuentes de Ruido]]

### Harry Nyquist

→ [[../conceptos-integradores/aportes-nyquist|Aportes de Nyquist]] — pagina dedicada

---

## Ver Tambien

- [[../conceptos-integradores/aportes-shannon|Aportes de Shannon]]
- [[../conceptos-integradores/aportes-nyquist|Aportes de Nyquist]]
- [[../conceptos-integradores/aportes-armstrong|Aportes de Armstrong]]
- [[../conceptos-integradores/aportes-fourier|Aportes de Fourier]]
- [[../conceptos-integradores/aportes-carson|Aportes de Carson]]
- [[../conceptos-integradores/aportes-parseval|Aportes de Parseval]]
- [[../conceptos-integradores/aportes-hilbert|Aportes de Hilbert]]
- [[../resumenes/overview-curso|Resumen General del Curso]]
