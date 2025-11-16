# Mazo Anki - Sistemas de Comunicaciones (UTN)
## Fundamentos y Bases Teóricas

---

## UNIDAD 1: INTRODUCCIÓN

### Carta 1
**Pregunta:** ¿Qué es un sistema de comunicaciones y cuáles son sus componentes fundamentales?

**Respuesta:** Un sistema de comunicaciones es un conjunto de elementos que permite la transferencia de información desde una fuente hasta un destino. Sus componentes fundamentales son:
- **Fuente de información**: genera el mensaje
- **Transmisor**: convierte el mensaje en señal adecuada para el canal
- **Canal**: medio físico de transmisión
- **Receptor**: recupera la señal y la convierte al formato original
- **Destino**: usuario final de la información

---

### Carta 2
**Pregunta:** ¿Por qué es necesaria la modulación en sistemas de comunicaciones?

**Respuesta:** La modulación es necesaria por varias razones:
1. **Adaptación al canal**: permite transmitir señales de baja frecuencia a través de medios que requieren altas frecuencias
2. **Multiplexación**: permite compartir un mismo canal entre múltiples usuarios
3. **Reducción de interferencias**: mejora la inmunidad al ruido
4. **Tamaño de antenas**: permite usar antenas de tamaño práctico (relacionado con λ)
5. **Uso eficiente del espectro**: optimiza el aprovechamiento de este recurso limitado

---

### Carta 3
**Pregunta:** ¿Qué es el espectro electromagnético y por qué requiere uso racional?

**Respuesta:** El espectro electromagnético es el rango de todas las frecuencias posibles de radiación electromagnética. Requiere uso racional porque:
- Es un **recurso natural limitado y no renovable**
- Diferentes servicios compiten por el mismo espectro
- Las interferencias entre servicios degradan la comunicación
- Su gestión está regulada por organismos nacionales e internacionales
- El uso eficiente permite maximizar la cantidad de servicios disponibles

---

## UNIDAD 2: ANÁLISIS DE SEÑALES

### Carta 4
**Pregunta:** Enuncie y explique el Teorema de Parseval. ¿Qué interpretación física tiene?

**Respuesta:** El Teorema de Parseval establece que:
$$\int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df$$

**Interpretación física**: La energía total de una señal en el dominio del tiempo es igual a la energía total en el dominio de la frecuencia. Esto demuestra que la Transformada de Fourier conserva la energía, y permite calcular la energía de una señal integrando su densidad espectral de energía.

---

### Carta 5
**Pregunta:** ¿Qué establece el Teorema del Muestreo (Nyquist-Shannon) y cuál es su importancia práctica?

**Respuesta:** El Teorema del Muestreo establece que una señal de banda limitada con frecuencia máxima $f_m$ puede ser completamente reconstruida a partir de sus muestras si la **frecuencia de muestreo $f_s ≥ 2f_m$**.

**Importancia práctica**:
- Fundamental para la conversión analógico-digital
- Define la mínima tasa de muestreo necesaria
- Si $f_s < 2f_m$ ocurre **aliasing** (solapamiento espectral) y pérdida de información
- Base de sistemas PCM, audio digital, video digital, etc.

---

### Carta 6
**Pregunta:** ¿Qué es la densidad espectral de potencia y cómo se relaciona con la autocorrelación?

**Respuesta:** La **densidad espectral de potencia (DEP)** $S_x(f)$ describe cómo se distribuye la potencia de una señal en el dominio de la frecuencia.

**Relación con autocorrelación** (Teorema de Wiener-Khinchin):
$$S_x(f) = \mathcal{F}\{R_x(\tau)\}$$

Donde $R_x(\tau)$ es la función de autocorrelación. Esto significa que la DEP y la autocorrelación forman un **par de transformadas de Fourier**.

**Implicación**: características temporales de correlación se traducen en características espectrales de distribución de potencia.

---

### Carta 7
**Pregunta:** Explique el Teorema de Convolución en el dominio del tiempo y su importancia en sistemas lineales.

**Respuesta:** El Teorema de Convolución establece que:
$$y(t) = x(t) * h(t) \quad \Leftrightarrow \quad Y(f) = X(f) \cdot H(f)$$

**Importancia**:
- La convolución en el tiempo equivale a multiplicación en frecuencia
- Permite analizar sistemas LTI más fácilmente en el dominio frecuencial
- La respuesta de un sistema es: entrada ⊗ respuesta al impulso
- Fundamental para entender filtrado, modulación y procesamiento de señales

---

### Carta 8
**Pregunta:** ¿Qué es la Transformada de Hilbert y cuál es su aplicación en comunicaciones?

**Respuesta:** La Transformada de Hilbert $\hat{x}(t)$ de una señal $x(t)$ produce un **desfasaje de -90° para todas las frecuencias**.

**Aplicaciones principales**:
1. **Señal analítica**: $x_a(t) = x(t) + j\hat{x}(t)$ permite representar señales reales como complejas
2. **Modulación BLU**: permite generar banda lateral única matemáticamente
3. **Demodulación**: facilita la detección de envolvente y fase
4. **Análisis de modulaciones**: separación de componentes en fase y cuadratura

---

### Carta 9
**Pregunta:** ¿Qué diferencia hay entre señales de energía y señales de potencia? Dé ejemplos.

**Respuesta:** 

**Señales de energía**:
- Duración finita
- Energía finita: $E = \int_{-\infty}^{\infty} |x(t)|^2 dt < \infty$
- Potencia promedio = 0
- Ejemplos: pulsos, ráfagas, transitorios

**Señales de potencia**:
- Duración infinita o periódicas
- Potencia promedio finita: $P = \lim_{T\to\infty} \frac{1}{T}\int_{-T/2}^{T/2} |x(t)|^2 dt < \infty$
- Energía infinita
- Ejemplos: senoidales, señales aleatorias estacionarias, portadoras

---

## UNIDAD 3: MODULACIÓN LINEAL

### Carta 10
**Pregunta:** Compare AM-DSB-FC (AM convencional) con DSB-SC en términos de eficiencia de potencia y espectro.

**Respuesta:** 

**AM-DSB-FC (AM convencional)**:
- Contiene portadora: $s(t) = A_c[1 + m(t)]\cos(2\pi f_c t)$
- Ancho de banda: $BW = 2f_m$
- Eficiencia de potencia: baja (máximo 33% con m=1)
- Ventaja: detección de envolvente simple (no requiere sincronismo)

**DSB-SC (Doble Banda Suprimida)**:
- Sin portadora: $s(t) = A_c m(t)\cos(2\pi f_c t)$
- Ancho de banda: $BW = 2f_m$
- Eficiencia: 100% (toda la potencia en información)
- Desventaja: requiere detección coherente (sincronismo)

---

### Carta 11
**Pregunta:** ¿Qué es la modulación SSB (BLU) y cuáles son sus ventajas principales?

**Respuesta:** **SSB (Single Sideband - Banda Lateral Única)** transmite solo una banda lateral (superior o inferior), eliminando la portadora y la otra banda.

**Ventajas**:
1. **Ancho de banda mínimo**: $BW = f_m$ (mitad que AM o DSB)
2. **Eficiencia espectral**: máximo aprovechamiento del espectro
3. **Eficiencia de potencia**: toda la potencia transmite información
4. **Menor susceptibilidad al desvanecimiento selectivo**
5. **Aplicaciones**: radioaficionados, comunicaciones HF, telefonía

**Desventaja**: mayor complejidad en generación y detección, requiere sincronismo muy preciso.

---

### Carta 12
**Pregunta:** Explique el principio de funcionamiento del receptor superheterodino y sus ventajas.

**Respuesta:** El **superheterodino** convierte la señal de RF recibida a una frecuencia intermedia fija (FI) mediante un mezclador y oscilador local.

**Proceso**:
1. Señal RF → Amplificador RF
2. Mezclador: $f_{FI} = |f_{RF} - f_{LO}|$
3. Amplificación en FI (mayor ganancia y selectividad)
4. Detección

**Ventajas**:
- **Selectividad constante**: filtros FI optimizados para una frecuencia
- **Alta ganancia**: amplificación eficiente en FI
- **Rechazo de imagen**: con filtrado adecuado
- **Sintonización simple**: solo varía el oscilador local
- Estándar en radio AM/FM, TV, comunicaciones

---

### Carta 13
**Pregunta:** ¿Qué es el índice de modulación en AM y cómo afecta a la señal transmitida?

**Respuesta:** El **índice de modulación** $m$ en AM se define como:
$$m = \frac{A_m}{A_c}$$
donde $A_m$ es la amplitud de la moduladora y $A_c$ la amplitud de la portadora.

**Efectos**:
- **m < 1**: submodulación, transmisión normal
- **m = 1**: modulación 100%, máxima eficiencia sin distorsión
- **m > 1**: sobremodulación, **distorsión** (envolvente se invierte)

**Eficiencia de potencia**: $\eta = \frac{m^2}{2+m^2}$ (máximo 33% cuando m=1)

---

### Carta 14
**Pregunta:** Describa el funcionamiento del modulador balanceado y su importancia.

**Respuesta:** El **modulador balanceado** genera DSB-SC (suprime la portadora) mediante dispositivos no lineales (diodos, transistores) configurados simétricamente.

**Funcionamiento**:
- Usa simetría para cancelar la componente de portadora
- Entrada: señal moduladora + portadora
- Salida: solo productos de mezcla (bandas laterales)
- Configuraciones: anillo de diodos, puente balanceado, mezcladores de FETs

**Importancia**:
- Base para generar SSB (agregando filtros)
- Eficiencia energética (sin potencia desperdiciada en portadora)
- Fundamental en sistemas DBL y BLU

---

### Carta 15
**Pregunta:** ¿Qué es la banda lateral vestigial (VSB) y dónde se aplica principalmente?

**Respuesta:** **VSB (Vestigial Sideband)** es un compromiso entre DSB y SSB: transmite una banda lateral completa y un "vestigio" (parte) de la otra.

**Características**:
- Ancho de banda: $f_m < BW < 2f_m$
- Más fácil de generar que SSB (filtros menos críticos)
- Preserva componentes DC de la señal moduladora

**Aplicación principal**: **Televisión analógica**
- Video requiere preservar componente DC (nivel de brillo)
- SSB puro es muy difícil para video (BW grande)
- VSB permite transmisión eficiente manteniendo calidad

---

## UNIDAD 4: MODULACIÓN EXPONENCIAL

### Carta 16
**Pregunta:** Diferencie entre modulación en frecuencia (FM) y modulación en fase (PM) desde el punto de vista matemático.

**Respuesta:** 

**FM (Frequency Modulation)**:
$$s_{FM}(t) = A_c\cos[2\pi f_c t + 2\pi k_f \int m(t)dt]$$
- La frecuencia instantánea varía con $m(t)$
- $f_i(t) = f_c + k_f m(t)$

**PM (Phase Modulation)**:
$$s_{PM}(t) = A_c\cos[2\pi f_c t + k_p m(t)]$$
- La fase instantánea varía directamente con $m(t)$

**Relación**: FM de $m(t)$ ≡ PM de $\int m(t)dt$
- FM es derivador respecto a PM
- PM es integrador respecto a FM

---

### Carta 17
**Pregunta:** Defina el índice de modulación en FM y explique la diferencia entre FM de banda angosta y banda ancha.

**Respuesta:** **Índice de modulación en FM**:
$$\beta = \frac{\Delta f_{max}}{f_m} = \frac{k_f A_m}{f_m}$$
donde $\Delta f_{max}$ es la máxima desviación de frecuencia.

**FM Banda Angosta (NBFM)**: $\beta < 0.5$
- Ancho de banda ≈ 2$f_m$ (similar a AM)
- Pocas componentes espectrales significativas
- Aproximación lineal válida

**FM Banda Ancha (WBFM)**: $\beta > 1$
- Ancho de banda: Regla de Carson: $BW ≈ 2(\Delta f + f_m) = 2f_m(\beta + 1)$
- Múltiples componentes espectrales (funciones de Bessel)
- Mayor inmunidad al ruido
- Usado en FM broadcast ($\beta$ ≈ 5)

---

### Carta 18
**Pregunta:** ¿Qué establece la Regla de Carson para FM y cuál es su interpretación?

**Respuesta:** La **Regla de Carson** estima el ancho de banda de una señal FM:
$$BW ≈ 2(\Delta f + f_m) = 2f_m(\beta + 1)$$

**Interpretación**:
- Incluye el 98% de la potencia de la señal
- Considera la desviación de frecuencia más el ancho de banda de la moduladora
- Es una aproximación práctica (el espectro FM teóricamente es infinito)
- Útil para diseño de sistemas y asignación de espectro

**Ejemplo**: FM broadcast
- $f_m$ = 15 kHz, $\Delta f$ = 75 kHz
- $BW$ ≈ 2(75 + 15) = 180 kHz
- En práctica se asignan 200 kHz por canal

---

### Carta 19
**Pregunta:** Explique el funcionamiento del discriminador de frecuencia para demodular FM.

**Respuesta:** El **discriminador de frecuencia** convierte variaciones de frecuencia en variaciones de amplitud para recuperar la moduladora.

**Principio**:
1. Circuito resonante con respuesta lineal en rango de $f_c ± \Delta f$
2. Convierte desviaciones de frecuencia en cambios de amplitud
3. Detector de envolvente extrae la señal moduladora

**Tipos principales**:
- **Discriminador Foster-Seeley**: usa transformador sintonizado
- **Detector de relación (ratio detector)**: más estable ante variaciones de amplitud
- **PLL (Phase-Locked Loop)**: moderno, más lineal y preciso

---

### Carta 20
**Pregunta:** ¿Qué es el preénfasis y deénfasis en FM y por qué se utiliza?

**Respuesta:** **Preénfasis** y **deénfasis** mejoran la relación señal-ruido en FM.

**Preénfasis** (transmisor):
- Filtro que amplifica componentes de alta frecuencia de la moduladora
- Respuesta típica: +6 dB/octava desde $f_1$ ≈ 2.1 kHz

**Deénfasis** (receptor):
- Filtro inverso que atenúa altas frecuencias
- Restaura balance espectral original

**Razón**: 
- El ruido en FM afecta más a altas frecuencias
- Preénfasis aumenta SNR de componentes agudos antes de transmisión
- Deénfasis reduce ruido sin afectar señal (ya que están pre-enfatizadas)
- Mejora típica: 10-13 dB en SNR para altas frecuencias

---

### Carta 21
**Pregunta:** Compare FM y PM en términos de ventajas, desventajas y aplicaciones.

**Respuesta:** 

**FM (Frequency Modulation)**:
- Ventajas: excelente rechazo al ruido, amplitud constante
- Desventajas: BW grande, circuitos más complejos
- Aplicaciones: radio broadcast, audio de TV, comunicaciones móviles

**PM (Phase Modulation)**:
- Ventajas: implementación más simple, no requiere integrador/derivador
- Desventajas: sensible a ruido de fase, menos común
- Aplicaciones: modulaciones digitales (PSK), transmisión de datos

**Comparación**:
- Ambas son modulaciones exponenciales (amplitud constante)
- FM más popular para aplicaciones analógicas
- PM base de modulaciones digitales modernas

---

## UNIDAD 5: MODULACIÓN DE PULSOS

### Carta 22
**Pregunta:** Explique los tipos de modulación analógica de pulsos: PAM, PWM y PPM.

**Respuesta:** 

**PAM (Pulse Amplitude Modulation)**:
- Amplitud del pulso varía según $m(t)$
- Más simple, base de PCM
- Susceptible a ruido

**PWM (Pulse Width Modulation)**:
- Ancho del pulso varía según $m(t)$
- Amplitud constante (mayor inmunidad al ruido)
- Usado en control de potencia

**PPM (Pulse Position Modulation)**:
- Posición temporal del pulso varía según $m(t)$
- Mayor inmunidad al ruido que PWM
- Requiere sincronización precisa
- Mejor eficiencia energética

Todas permiten multiplexación por división de tiempo (TDM).

---

### Carta 23
**Pregunta:** Describa el proceso de PCM (Pulse Code Modulation) y sus etapas principales.

**Respuesta:** **PCM** digitaliza señales analógicas en tres etapas:

**1. Muestreo**:
- Frecuencia: $f_s ≥ 2f_m$ (Nyquist)
- Genera PAM natural

**2. Cuantificación**:
- Divide rango en $L = 2^n$ niveles
- Error de cuantificación: $e_q ≤ \Delta/2$ donde $\Delta$ = paso de cuantificación
- SNR cuantificación: $SNR_q ≈ 6n + 1.76$ dB (n = bits)

**3. Codificación**:
- Asigna código binario de n bits a cada nivel
- Transmite secuencia de bits

**Ventajas**: inmunidad al ruido, regeneración, procesamiento digital
**Desventaja**: mayor ancho de banda

---

### Carta 24
**Pregunta:** ¿Qué es el companding en PCM y por qué se utiliza?

**Respuesta:** **Companding** = Compresión + Expansión

**Transmisor (compresor)**:
- Comprime el rango dinámico de la señal
- Señales débiles: mayor resolución
- Señales fuertes: menor resolución

**Receptor (expansor)**:
- Operación inversa, restaura rango original

**Por qué se usa**:
1. **SNR uniforme**: mejora SNR de señales débiles sin degradar las fuertes
2. **Rango dinámico efectivo**: mejor aprovechamiento de bits disponibles
3. **Percepción logarítmica**: se adapta a respuesta humana

**Leyes estándar**:
- **μ-law** (USA, Japón): μ = 255
- **A-law** (Europa): A = 87.6

---

### Carta 25
**Pregunta:** Compare PCM con Modulación Delta (DM) y Delta Adaptativa (ADM).

**Respuesta:** 

**PCM**:
- Transmite valor absoluto de cada muestra (n bits)
- Mayor tasa de bits pero mejor calidad
- Complejidad moderada

**Delta Modulation (DM)**:
- Transmite solo 1 bit por muestra (incremento/decremento)
- Tasa de bits muy baja
- Problemas: slope overload, granular noise
- Simple pero calidad limitada

**Adaptive Delta Modulation (ADM)**:
- Paso de cuantificación variable (adaptativo)
- Soluciona problemas de DM estándar
- Mejor balance complejidad/calidad
- Usado en aplicaciones de baja tasa (codecs de voz)

---

### Carta 26
**Pregunta:** ¿Qué es TDM (Time Division Multiplexing) y cómo se implementa en sistemas PCM?

**Respuesta:** **TDM** permite transmitir múltiples señales por un canal compartiendo el tiempo.

**Implementación en PCM**:
1. Cada canal se muestrea secuencialmente (muestreo entrelazado)
2. Muestras se cuantifican y codifican
3. Se forma una **trama** con:
   - Bits de cada canal
   - Bits de sincronización (frame alignment)
   - Posible señalización

**Ejemplo**: Sistema T1 (USA)
- 24 canales de voz
- 8 bits/muestra, 8000 muestras/s por canal
- Tasa: 1.544 Mbps (incluye overhead)

**Ventajas**: eficiente, flexible, regeneración digital
**Jerarquías**: E1, T1, PDH, SDH

---

## UNIDAD 6: MODULACIÓN DIGITAL

### Carta 27
**Pregunta:** Compare ASK, FSK y PSK en términos de eficiencia espectral y robustez ante ruido.

**Respuesta:** 

**ASK (Amplitude Shift Keying)**:
- Varía amplitud de portadora
- Eficiencia espectral: moderada
- Robustez: **baja** (muy sensible a ruido)
- Uso: limitado, fibra óptica (OOK)

**FSK (Frequency Shift Keying)**:
- Varía frecuencia de portadora
- Eficiencia espectral: baja (mayor BW)
- Robustez: **buena** (amplitud constante)
- Uso: modems, comunicaciones HF

**PSK (Phase Shift Keying)**:
- Varía fase de portadora
- Eficiencia espectral: **alta** (especialmente M-PSK)
- Robustez: muy buena con detección coherente
- Uso: **preferida** en comunicaciones modernas

**Ranking general**: PSK > FSK > ASK

---

### Carta 28
**Pregunta:** Explique qué es una constelación en modulación digital y su importancia.

**Respuesta:** Una **constelación** es la representación gráfica de todos los símbolos posibles de una modulación digital en el plano complejo (I-Q).

**Componentes**:
- Eje I (In-phase): componente en fase
- Eje Q (Quadrature): componente en cuadratura
- Cada punto representa un símbolo único

**Importancia**:
1. **Visualización**: permite ver la estructura de la modulación
2. **Distancia entre símbolos**: determina robustez ante ruido
3. **Diseño**: optimización de esquemas de modulación
4. **Diagnóstico**: identificar problemas (ruido, offset, errores IQ)

**Ejemplos**:
- BPSK: 2 puntos en eje I
- QPSK: 4 puntos en esquinas de cuadrado
- QAM: red rectangular de puntos

---

### Carta 29
**Pregunta:** ¿Qué es QAM y por qué es ampliamente utilizada en comunicaciones modernas?

**Respuesta:** **QAM (Quadrature Amplitude Modulation)** modula independientemente amplitud y fase de dos portadoras en cuadratura.

**Señal QAM**:
$$s(t) = A_I(t)\cos(2\pi f_c t) - A_Q(t)\sin(2\pi f_c t)$$

**Ventajas**:
1. **Alta eficiencia espectral**: M-QAM transmite $\log_2(M)$ bits/símbolo
2. **Flexibilidad**: múltiples configuraciones (16-QAM, 64-QAM, 256-QAM, etc.)
3. **Adaptabilidad**: puede ajustar orden según condiciones del canal

**Desventaja**: sensible a ruido y no-linealidades (amplitud variable)

**Aplicaciones**: 
- Cable modems, DSL
- WiFi (802.11), 4G/5G
- TV digital, comunicaciones satelitales

---

### Carta 30
**Pregunta:** Defina velocidad de señalización (baud rate) y tasa de bits (bit rate). ¿Son siempre iguales?

**Respuesta:** 

**Velocidad de señalización (Rs)**: 
- Símbolos transmitidos por segundo
- Unidad: baudios (símbolos/s)
- Relacionada con ancho de banda

**Tasa de bits (Rb)**:
- Bits transmitidos por segundo
- Unidad: bits/s (bps)

**Relación**:
$$R_b = R_s \cdot \log_2(M)$$
donde M = número de símbolos posibles

**NO son iguales** excepto en modulaciones binarias (M=2).

**Ejemplos**:
- BPSK: Rs = Rb (1 bit/símbolo)
- QPSK: Rb = 2Rs (2 bits/símbolo)
- 16-QAM: Rb = 4Rs (4 bits/símbolo)

---

### Carta 31
**Pregunta:** ¿Qué es la probabilidad de error de bit (BER) y de qué factores depende?

**Respuesta:** **BER (Bit Error Rate)** es la probabilidad de que un bit transmitido se reciba erróneamente.

**Definición**:
$$BER = \frac{\text{bits erróneos}}{\text{total de bits transmitidos}}$$

**Depende de**:
1. **SNR o Eb/N0**: relación señal-ruido por bit
2. **Tipo de modulación**: diferentes curvas BER vs Eb/N0
3. **Tipo de detección**: coherente vs no coherente
4. **Características del canal**: desvanecimiento, interferencia
5. **Codificación**: códigos correctores mejoran BER

**Objetivo típico**: BER < 10⁻⁶ (telefonía), < 10⁻⁹ (datos)

**Curvas BER**: herramienta fundamental para comparar modulaciones

---

### Carta 32
**Pregunta:** Compare detección coherente vs. no coherente en modulaciones digitales.

**Respuesta:** 

**Detección Coherente**:
- Requiere **referencia de fase sincronizada** con portadora transmitida
- Usa correlación o multiplicación con portadora local
- **Ventaja**: mejor desempeño (menor BER para mismo SNR)
- **Desventaja**: circuito de recuperación de portadora necesario
- Usado en: PSK, QAM

**Detección No Coherente**:
- No requiere sincronización de fase
- Usa detección de envolvente o discriminador
- **Ventaja**: implementación más simple
- **Desventaja**: degradación de ~3 dB en SNR
- Usado en: FSK no coherente, ASK

**Penalidad típica**: no coherente requiere ~3 dB más de SNR para mismo BER

---

## UNIDAD 7: RUIDO

### Carta 33
**Pregunta:** Defina ruido blanco y explique por qué es un modelo útil en comunicaciones.

**Respuesta:** **Ruido blanco** es ruido aleatorio con densidad espectral de potencia constante para todas las frecuencias.

**Características**:
- DEP: $N_0$ (W/Hz) constante
- Potencia infinita (en ancho de banda infinito)
- Proceso estacionario, gaussiano
- Autocorrelación: función delta $R_n(\tau) = (N_0/2)\delta(\tau)$

**Por qué es útil**:
1. **Modelo simplificado**: aproxima bien el ruido térmico
2. **Análisis matemático simple**: independencia espectral
3. **Peor caso razonable**: conservador pero realista
4. **Banda limitada**: en sistemas reales se filtra a BW finito

**Realidad**: ruido "blanco filtrado" con potencia $N = N_0 \cdot BW$

---

### Carta 34
**Pregunta:** Explique el concepto de temperatura de ruido de un dispositivo.

**Respuesta:** La **temperatura de ruido** $T_e$ es una forma de caracterizar el ruido que un dispositivo agrega a la señal.

**Definición**: temperatura equivalente de una resistencia que produciría la misma potencia de ruido que el dispositivo.

**Relación con potencia de ruido**:
$$N = kT_e B$$
donde:
- k = constante de Boltzmann (1.38×10⁻²³ J/K)
- B = ancho de banda (Hz)

**Relación con figura de ruido**:
$$T_e = T_0(F - 1)$$
donde $T_0$ = 290 K (temperatura de referencia)

**Ventaja**: útil para sistemas en cascada, componentes criogénicos, antenas

---

### Carta 35
**Pregunta:** Defina la figura de ruido (F) y el factor de ruido (NF). ¿Cómo se relacionan?

**Respuesta:** 

**Figura de Ruido (F)** (adimensional):
$$F = \frac{SNR_{entrada}}{SNR_{salida}} = \frac{S_i/N_i}{S_o/N_o}$$

Mide cuánto degrada un dispositivo la relación señal-ruido.

**Factor de Ruido (NF)** (en dB):
$$NF = 10\log_{10}(F)$$

**Interpretación**:
- F = 1 (NF = 0 dB): dispositivo ideal (sin ruido)
- F > 1 (NF > 0 dB): el dispositivo agrega ruido
- Típicos: LNA 0.5-2 dB, amplificador 5-10 dB

**Relación con temperatura**:
$$F = 1 + \frac{T_e}{T_0}$$

---

### Carta 36
**Pregunta:** Enuncie y explique la fórmula de Friis para figura de ruido en sistemas en cascada.

**Respuesta:** La **fórmula de Friis** calcula la figura de ruido total de una cascada de dispositivos:

$$F_{total} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \frac{F_4 - 1}{G_1 G_2 G_3} + ...$$

donde:
- $F_i$ = figura de ruido del i-ésimo dispositivo
- $G_i$ = ganancia de potencia (lineal) del i-ésimo dispositivo

**Implicaciones**:
1. **Primera etapa domina**: $F_1$ tiene mayor impacto
2. **Alta ganancia inicial**: reduce contribución de etapas posteriores
3. **LNA crítico**: amplificador de bajo ruido al inicio es fundamental
4. **Diseño**: maximizar $G_1$ y minimizar $F_1$

**Ejemplo**: en receptor, LNA determina sensibilidad del sistema.

---

### Carta 37
**Pregunta:** ¿Qué es el ruido de banda angosta y cómo se representa matemáticamente?

**Respuesta:** El **ruido de banda angosta** es ruido blanco filtrado a un ancho de banda pequeño centrado en una frecuencia.

**Representación**:
$$n(t) = x(t)\cos(2\pi f_c t) - y(t)\sin(2\pi f_c t)$$

donde:
- $x(t)$ = componente en fase (in-phase)
- $y(t)$ = componente en cuadratura
- Ambas son procesos gaussianos, media cero, idéntica varianza

**Representación alternativa** (envolvente-fase):
$$n(t) = R(t)\cos[2\pi f_c t + \phi(t)]$$

donde:
- $R(t)$ = envolvente (distribución de Rayleigh)
- $\phi(t)$ = fase (distribución uniforme)

**Uso**: analizar efectos del ruido en receptores AM, FM, etc.

---

### Carta 38
**Pregunta:** Explique el efecto del ruido sobre un receptor AM con detección de envolvente.

**Respuesta:** En **AM con detección de envolvente**, señal + ruido:
$$r(t) = [A_c + m(t) + x(t)]\cos(2\pi f_c t) - y(t)\sin(2\pi f_c t)$$

**Casos**:

**Alto SNR** (señal >> ruido):
- Envolvente ≈ $A_c + m(t) + x(t)$
- Componente en fase del ruido interfiere
- SNR salida ≈ SNR entrada (detección lineal)

**Bajo SNR** (señal ≪ ruido):
- **Efecto umbral**: degradación súbita
- Ruido domina, envolvente sigue al ruido
- Pérdida completa de señal debajo del umbral
- Umbral típico: SNR ≈ 10 dB

**Conclusión**: AM requiere SNR mínimo para operación útil.

---

### Carta 39
**Pregunta:** ¿Qué es el efecto umbral en FM y cómo se manifiesta?

**Respuesta:** El **efecto umbral en FM** es una degradación súbita del desempeño cuando SNR cae por debajo de un valor crítico.

**Manifestación**:
- **Sobre umbral**: FM mejora SNR (intercambio BW por SNR)
  - SNR salida $\propto \beta^2$ (ventaja de FM)
- **Cerca/bajo umbral**: clicks de ruido
  - Saltos de fase de 2π generan pulsos impulsivos
  - Degradación rápida
  
**Umbral típico**: SNR entrada ≈ 10 dB (depende de β)

**Soluciones**:
- Aumentar potencia transmitida
- Usar PLL (baja umbral ~3 dB)
- Feedback demodulator
- No operar cerca del umbral en diseño

---

## UNIDAD 8: INTERCOMPARACIÓN DE SISTEMAS

### Carta 40
**Pregunta:** ¿Qué parámetros se utilizan para comparar diferentes sistemas de modulación?

**Respuesta:** **Parámetros principales de comparación**:

1. **Eficiencia espectral**: bits/s/Hz
2. **Eficiencia de potencia**: Eb/N0 requerido para cierto BER
3. **Ancho de banda requerido**: vs. tasa de información
4. **SNR de salida**: vs. SNR de entrada
5. **Complejidad**: de implementación
6. **Robustez**: ante ruido, interferencia, desvanecimiento
7. **Inmunidad a no-linealidades**: amplificadores
8. **Sincronización**: requerimientos
9. **Costo**: económico y energético

**Trade-offs clave**:
- Ancho de banda ↔ Potencia (Shannon)
- Complejidad ↔ Desempeño
- Eficiencia espectral ↔ Robustez

---

### Carta 41
**Pregunta:** Compare la eficiencia espectral de diferentes esquemas de modulación.

**Respuesta:** **Eficiencia espectral** = Rb/BW (bits/s/Hz)

**Analógicas** (referencia):
- AM-DSB: ~1 bit/s/Hz (pobre)
- SSB: ~2 bits/s/Hz (mejor)
- FM: muy pobre (BW grande), pero buena en SNR

**Digitales**:
- **ASK, FSK**: 0.5-1 bit/s/Hz (baja)
- **BPSK**: ~1 bit/s/Hz
- **QPSK**: ~2 bits/s/Hz
- **8-PSK**: ~3 bits/s/Hz
- **16-QAM**: ~4 bits/s/Hz
- **64-QAM**: ~6 bits/s/Hz
- **256-QAM**: ~8 bits/s/Hz

**Tendencia**: QAM de alto orden tiene máxima eficiencia espectral, pero requiere mayor SNR.

**Conclusión**: existe trade-off entre eficiencia espectral y robustez (BER).

---

### Carta 42
**Pregunta:** Explique el concepto de ganancia de procesamiento en modulación de pulsos.

**Respuesta:** La **ganancia de procesamiento** es la mejora en SNR que se obtiene al usar modulación de pulsos vs. transmisión analógica directa en banda base.

**En PCM**:
$$G_p = \frac{SNR_{salida}}{SNR_{banda\_base}}$$

**Fuentes de ganancia**:
1. **Cuantificación uniforme**: SNR depende de número de bits
   - SNR ≈ 6n + 1.76 dB (n = bits/muestra)
2. **Regeneración**: elimina ruido acumulado
3. **Codificación de canal**: corrección de errores

**Costo**: mayor ancho de banda
- Banda base: BW = $f_m$
- PCM: BW ≈ $nf_m$ (sin considerar codificación de línea)

**Trade-off Shannon**: intercambio BW por SNR

---

### Carta 43
**Pregunta:** ¿Cómo afecta la pre-énfasis/de-énfasis a la comparación FM vs. AM?

**Respuesta:** La **red de énfasis** mejora significativamente el desempeño de FM:

**Sin énfasis**:
- FM ya supera a AM en SNR (especialmente para β grande)
- Ventaja FM: proporcional a $\beta^2$

**Con énfasis**:
- **Mejora adicional**: 10-13 dB en componentes de alta frecuencia
- Compensa el énfasis del ruido en altas frecuencias en FM
- SNR efectivo mucho mayor que AM

**Comparación final**:
- **AM**: SNR salida ≈ SNR entrada (sin ganancia)
- **FM sin énfasis**: SNR salida = 3β²(SNR entrada) para tono único
- **FM con énfasis**: mejora adicional significativa

**Conclusión**: FM con énfasis es claramente superior a AM en ambiente ruidoso, justificando el mayor BW.

---

## UNIDAD 9: TEORÍA DE LA INFORMACIÓN

### Carta 44
**Pregunta:** Defina entropía de una fuente de información y explique su significado.

**Respuesta:** La **entropía** H mide la información promedio (incertidumbre) de una fuente discreta.

**Definición**:
$$H = -\sum_{i=1}^{n} p_i \log_2(p_i) \text{ bits/símbolo}$$

donde $p_i$ = probabilidad del símbolo i

**Interpretación**:
- Cantidad promedio de bits necesarios para representar cada símbolo
- Máxima cuando todos los símbolos son equiprobables: $H_{max} = \log_2(n)$
- Mínima (= 0) cuando un símbolo tiene probabilidad 1

**Propiedades**:
- Siempre: $0 ≤ H ≤ \log_2(n)$
- Mide eficiencia potencial de compresión
- Base de teoría de codificación

**Ejemplo**: lanzar moneda justa: H = 1 bit

---

### Carta 45
**Pregunta:** Enuncie y explique el Teorema de Shannon-Hartley.

**Respuesta:** El **Teorema de Shannon-Hartley** establece la **capacidad máxima** de un canal con ruido gaussiano blanco:

$$C = B \log_2\left(1 + \frac{S}{N}\right) \text{ bits/s}$$

donde:
- C = capacidad del canal (bits/s)
- B = ancho de banda (Hz)
- S/N = relación señal a ruido (lineal)

**Implicaciones fundamentales**:
1. **Límite teórico**: tasa máxima para comunicación libre de errores
2. **Trade-off BW-SNR**: se puede intercambiar ancho de banda por potencia y viceversa
3. **Inalcanzable en práctica**: pero indica dirección de diseño
4. **Base de comparación**: eficiencia de sistemas reales vs. límite de Shannon

**Conclusión**: fija límite fundamental de lo que es posible en comunicaciones.

---

### Carta 46
**Pregunta:** ¿Qué es la redundancia en una fuente de información y cómo se relaciona con la compresión?

**Respuesta:** **Redundancia** mide cuánta información "extra" contiene una fuente vs. su mínimo teórico.

**Definición**:
$$\text{Redundancia} = 1 - \frac{H}{H_{max}} = 1 - \frac{H}{\log_2(n)}$$

donde:
- H = entropía de la fuente
- $H_{max}$ = entropía máxima posible

**Interpretación**:
- Redundancia = 0: fuente óptima (equiprobable, sin memoria)
- Redundancia > 0: existe información predecible/repetitiva

**Relación con compresión**:
- **Compresión sin pérdida**: puede eliminar redundancia hasta alcanzar H
- **Factor de compresión máximo**: $H_{max}/H$
- Ejemplos: texto español ~50% redundancia, permite compresión efectiva

**Aplicaciones**: ZIP, Huffman coding, códigos aritméticos

---

### Carta 47
**Pregunta:** Explique qué es un código óptimo o compacto según el criterema de Kraft-McMillan.

**Respuesta:** Un **código óptimo** (o compacto) minimiza la longitud promedio de palabra código.

**Criterio de Kraft-McMillan** (para código instantáneo):
$$\sum_{i=1}^{n} 2^{-l_i} ≤ 1$$

donde $l_i$ = longitud del código i

**Código óptimo**:
- Satisface desigualdad de Kraft (es instantáneo/únicamente decodificable)
- Longitud promedio $\bar{L}$ satisface: $H ≤ \bar{L} < H + 1$
- Asigna códigos más cortos a símbolos más probables

**Ejemplos**:
- **Huffman coding**: construye código óptimo
- **Shannon-Fano**: aproximación

**Límite**: ningún código puede tener $\bar{L} < H$ (entropía es límite inferior)

---

### Carta 48
**Pregunta:** ¿Qué son los códigos detectores y correctores de errores? Dé ejemplos.

**Respuesta:** **Códigos de canal** agregan redundancia controlada para detectar/corregir errores de transmisión.

**Códigos Detectores**:
- Detectan errores pero no pueden corregirlos
- Ejemplo simple: **bit de paridad**
- Requieren retransmisión (ARQ)

**Códigos Correctores (FEC)**:
- Detectan Y corrigen errores sin retransmisión
- Requieren más redundancia

**Ejemplos**:

*Códigos de bloque*:
- **Hamming (7,4)**: 4 bits datos, 3 bits paridad, corrige 1 error
- **Reed-Solomon**: muy usado (CD, DVD, QR, espacio)
- **BCH**: flexible, potente

*Códigos convolucionales*:
- **Viterbi decoding**: usado en telefonía móvil
- **Turbo codes**: cerca del límite de Shannon

**Parámetro clave**: distancia de Hamming → capacidad de detección/corrección

---

### Carta 49
**Pregunta:** Compare comunicación analógica vs. digital desde la perspectiva de la Teoría de la Información.

**Respuesta:** 

**Analógica**:
- No hay límite claro error vs. no-error
- Degradación gradual con ruido
- SNR disminuye monotónicamente
- No alcanza capacidad del canal
- Difícil regenerar sin pérdida

**Digital**:
- **Operación libre de errores posible** si R < C (Shannon)
- Degradación abrupta en umbral
- Regeneración sin pérdida (repetidores)
- Puede acercarse a capacidad con codificación
- BER puede hacerse arbitrariamente pequeña (a costa de complejidad)

**Ventaja fundamental digital**:
- La Teoría de Shannon garantiza que **existe** un esquema de codificación que permite transmitir a tasa R < C con error arbitrariamente pequeño
- La práctica moderna (Turbo, LDPC) se acerca al límite

**Conclusión**: digital puede alcanzar el límite teórico, analógica no.

---

## UNIDAD 10: ESPECTRO EXPANDIDO Y OFDM

### Carta 50
**Pregunta:** ¿Qué es la modulación de espectro expandido (Spread Spectrum) y cuáles son sus ventajas principales?

**Respuesta:** **Spread Spectrum** expande deliberadamente el ancho de banda de la señal mucho más allá del mínimo necesario.

**Características**:
- BW transmitida >> BW de información
- Usa secuencia pseudoaleatoria (código)
- Densidad espectral de potencia baja

**Ventajas principales**:
1. **Resistencia a interferencias**: señal parece ruido para no-autorizados
2. **Múltiple acceso** (CDMA): usuarios comparten frecuencia
3. **Inmunidad a jamming**: aplicaciones militares
4. **Privacidad**: difícil interceptar sin conocer código
5. **Resistencia a multitrayecto**: diversidad temporal
6. **Baja probabilidad de detección** (LPD/LPI)

**Costo**: requiere mayor BW y sincronización precisa

---

### Carta 51
**Pregunta:** Compare las técnicas DSSS (Direct Sequence) y FHSS (Frequency Hopping) de espectro expandido.

**Respuesta:** 

**DSSS (Direct Sequence Spread Spectrum)**:
- Multiplica datos por secuencia PN de alta velocidad (chip rate >> bit rate)
- Ocupa todo el BW todo el tiempo
- Ganancia de procesamiento: $G_p = BW_{RF}/BW_{info}$
- Mejor para ambientes con ruido continuo
- Ejemplo: GPS, CDMA (IS-95), WiFi 802.11b

**FHSS (Frequency Hopping Spread Spectrum)**:
- Cambia rápidamente la frecuencia de portadora según patrón PN
- Usa una frecuencia a la vez, pero muchas frecuencias en el tiempo
- Dos tipos: Fast hopping (varios hops/bit) y Slow hopping (varios bits/hop)
- Mejor contra interferencia de banda angosta y jamming
- Ejemplo: Bluetooth, 802.11 (original)

**Comparación**:
- DSSS: mejor ganancia de procesamiento, más complejo
- FHSS: implementación más simple, mejor contra jamming pulsado

---

### Carta 52
**Pregunta:** Explique el principio de CDMA (Code Division Multiple Access).

**Respuesta:** **CDMA** permite que múltiples usuarios compartan simultáneamente la misma banda de frecuencia usando códigos ortogonales únicos.

**Principio**:
1. Cada usuario tiene código PN único
2. Transmisor: datos × código → señal expandida
3. Todos transmiten en misma frecuencia simultáneamente
4. Receptor: señal recibida × mismo código → recupera datos
   - Señales con códigos diferentes aparecen como ruido
   - **Correlación**: alta con código correcto, baja con otros

**Requisitos clave**:
- Códigos **ortogonales** o casi-ortogonales (baja correlación cruzada)
- Sincronización precisa
- Control de potencia (problema near-far)

**Ventajas**:
- Capacidad flexible (soft capacity)
- Inmunidad a interferencias
- Handoff suave en celular

**Aplicaciones**: 3G (IS-95, CDMA2000, WCDMA)

---

### Carta 53
**Pregunta:** ¿Qué es OFDM y cuál es su principio de funcionamiento?

**Respuesta:** **OFDM (Orthogonal Frequency Division Multiplexing)** divide el canal en múltiples subportadoras ortogonales de banda angosta.

**Principio**:
1. Flujo de datos serial → paralelo en N subcanales
2. Cada subcanal modula una subportadora (típicamente QAM)
3. Subportadoras son ortogonales: $\Delta f = 1/T_{symbol}$
4. Implementación eficiente: **IFFT** (transmisor) y **FFT** (receptor)

**Características clave**:
- Espectros de subportadoras se solapan, pero son ortogonales
- Cada subportadora transmite a baja tasa → símbolo largo
- **Prefijo cíclico (CP)**: guarda contra multitrayecto

**Ventajas**:
1. **Resistencia a multitrayecto**: ecualización simple
2. **Uso eficiente del espectro**: ortogonalidad
3. **Adaptabilidad**: puede variar modulación por subportadora
4. **Implementación digital eficiente**: FFT/IFFT

---

### Carta 54
**Pregunta:** ¿Cuáles son las principales aplicaciones de OFDM y por qué es tan popular?

**Respuesta:** **Aplicaciones principales de OFDM**:

1. **WiFi**: 802.11a/g/n/ac/ax
2. **4G LTE / 5G**: downlink usa OFDMA
3. **TV Digital**: DVB-T, ISDB-T, ATSC 3.0
4. **Radio Digital**: DAB, HD Radio
5. **DSL**: ADSL, VDSL (DMT - variante de OFDM)
6. **WiMAX**: 802.16

**Por qué es popular**:
1. **Multitrayecto**: maneja canales difíciles sin ecualizador complejo
2. **Eficiencia espectral**: alta capacidad
3. **Flexibilidad**: adaptive modulation and coding (AMC)
4. **Escalabilidad**: fácil variar BW
5. **Implementación práctica**: DSP eficiente con FFT

**Desventaja principal**: alto PAPR (Peak-to-Average Power Ratio) → requiere amplificadores lineales costosos

---

### Carta 55
**Pregunta:** Explique qué es el prefijo cíclico en OFDM y por qué es necesario.

**Respuesta:** El **prefijo cíclico (CP)** es una copia de la parte final del símbolo OFDM que se añade al principio.

**Funcionamiento**:
1. Símbolo OFDM de duración $T_s$
2. Se copian últimos $T_g$ segundos
3. Se añaden al inicio → símbolo total: $T_s + T_g$

**Por qué es necesario**:

**Problema sin CP**: 
- Multitrayecto causa **ISI** (interferencia entre símbolos)
- Destruye ortogonalidad entre subportadoras → **ICI** (interferencia entre portadoras)

**Solución con CP**:
- Si $T_g >$ delay spread del canal:
  - Convierte convolución lineal en circular
  - Preserva ortogonalidad
  - Elimina ISI e ICI
  - Ecualización simple: solo un coeficiente complejo por subportadora

**Costo**: overhead típico 10-25% (reduce tasa efectiva)

---

## CONCEPTOS INTEGRADORES Y TRANSVERSALES

### Carta 56
**Pregunta:** Explique el trade-off fundamental entre ancho de banda y potencia (relación de Shannon).

**Respuesta:** El Teorema de Shannon establece el **trade-off fundamental BW-Potencia**:

$$C = B\log_2(1 + S/N)$$

**Implicaciones**:

**Régimen limitado por BW** (S/N alto):
- Aumentar S/N mejora C logarítmicamente (rendimiento decreciente)
- Aumentar BW mejora C linealmente
- Solución: usar más BW → modulaciones eficientes espectralmente

**Régimen limitado por Potencia** (S/N bajo):
- Aumentar BW permite mantener C con menos potencia
- Límite cuando S/N → 0: $C/B → (S/N) \cdot 1.44$
- Solución: spread spectrum, codificación

**Conclusión práctica**:
- Sistemas con potencia limitada (satélite, móvil): usar más BW
- Sistemas con BW limitado (cable, terrestre): usar más potencia
- Codificación permite acercarse al límite de Shannon

---

### Carta 57
**Pregunta:** ¿Cuál es la relación entre Eb/N0 y SNR, y por qué Eb/N0 es más útil para comparar sistemas digitales?

**Respuesta:** 

**Definiciones**:
- **SNR**: $S/N$ = potencia de señal / potencia de ruido
- **Eb/N0**: energía por bit / densidad espectral de ruido

**Relación**:
$$\frac{E_b}{N_0} = \frac{S}{N} \cdot \frac{B}{R_b}$$

donde $R_b$ = tasa de bits, B = ancho de banda

**Por qué Eb/N0 es mejor**:
1. **Normalizado por tasa**: permite comparar sistemas con diferentes tasas
2. **Independiente del BW**: separa eficiencia de modulación del ancho de banda
3. **Comparación justa**: sistemas con mismo BER requieren mismo Eb/N0 (idealmente)
4. **Límite de Shannon**: $E_b/N_0 ≥ \ln(2) \approx -1.59$ dB

**Uso**: curvas BER vs Eb/N0 son estándar para comparar modulaciones

---

### Carta 58
**Pregunta:** Explique el concepto de eficiencia espectral y eficiencia de potencia, y el trade-off entre ambas.

**Respuesta:** 

**Eficiencia Espectral** (η_B):
$$\eta_B = \frac{R_b}{B} \text{ bits/s/Hz}$$
Mide cuánta información se transmite por unidad de ancho de banda.

**Eficiencia de Potencia** (η_P):
Medida por Eb/N0 requerido para cierto BER.
- Menor Eb/N0 → más eficiente en potencia

**Trade-off fundamental**:
- **Alta η_B** (QAM alto orden): requiere alta SNR → baja η_P
  - Ejemplo: 256-QAM: 8 bits/s/Hz, pero requiere Eb/N0 alto
- **Alta η_P** (spread spectrum, codificación): usa más BW → baja η_B
  - Ejemplo: GPS: robusta pero poca capacidad

**Aplicaciones**:
- Satélite (potencia limitada): priorizar η_P
- Fibra óptica (potencia abundante): priorizar η_B
- Sistemas adaptativos (LTE, 5G): varían según condiciones

---

### Carta 59
**Pregunta:** ¿Cómo permite la digitalización la regeneración de señales sin pérdida, a diferencia de los sistemas analógicos?

**Respuesta:** La **regeneración** es una ventaja fundamental de sistemas digitales.

**Sistema Analógico**:
- Amplificador repite señal + ruido acumulado
- Cada etapa degrada SNR
- Ruido se acumula irreversiblemente
- SNR empeora con distancia

**Sistema Digital**:
1. **Decisión binaria**: regenerador decide 0 o 1 basado en umbral
2. **Regeneración limpia**: si BER suficientemente bajo, genera pulso nuevo
3. **Ruido no acumulativo**: cada regenerador "resetea" el ruido
4. **Distancia ilimitada**: con suficientes regeneradores

**Requisito crítico**:
- SNR en cada sección debe estar sobre umbral
- Diseño: espaciamiento de regeneradores según atenuación y ruido

**Resultado**: comunicaciones de larga distancia (fibra óptica transcontinental, enlaces satelitales) son digitales.

---

### Carta 60
**Pregunta:** Resuma la evolución histórica y lógica de los sistemas de modulación desde AM hasta 5G.

**Respuesta:** **Evolución de sistemas de modulación**:

**1ª Gen - Analógica (1920s-1980s)**:
- **AM**: primera, simple pero ineficiente
- **FM**: mejor calidad, más espectro (1930s+)
- SSB: eficiente, voz HF

**2ª Gen - Digital básica (1990s)**:
- Digitalización de voz (PCM)
- FSK, GMSK (GSM): robustas pero baja tasa
- CDMA (IS-95): espectro expandido

**3ª Gen - CDMA avanzada (2000s)**:
- WCDMA, CDMA2000
- Mayor capacidad, datos
- Turbo códigos

**4ª Gen - OFDM (2010s)**:
- **LTE**: OFDMA, alta eficiencia espectral
- QAM adaptativo (hasta 256-QAM)
- MIMO: múltiples antenas

**5ª Gen - Flexible (2020+)**:
- **NR**: OFDM mejorado
- mmWave, Massive MIMO
- Ultra-flexible (eMBB, URLLC, mMTC)

**Tendencia**: mayor eficiencia espectral, complejidad, adaptabilidad

---

## FIN DEL MAZO

**Total de cartas**: 60 cartas fundamentales

**Distribución por unidad**:
- Unidad 1 (Introducción): 3 cartas
- Unidad 2 (Análisis de señales): 6 cartas
- Unidad 3 (Modulación Lineal): 6 cartas
- Unidad 4 (Modulación Exponencial): 6 cartas
- Unidad 5 (Modulación de Pulsos): 5 cartas
- Unidad 6 (Modulación Digital): 6 cartas
- Unidad 7 (Ruido): 7 cartas
- Unidad 8 (Intercomparación): 4 cartas
- Unidad 9 (Teoría Información): 6 cartas
- Unidad 10 (Spread Spectrum/OFDM): 6 cartas
- Conceptos Integradores: 5 cartas

---

## INSTRUCCIONES DE USO

**Para importar a Anki**:
1. Las cartas están en formato pregunta-respuesta clara
2. Puede copiar directamente o usar addon de importación markdown
3. Recomendación: crear mazos separados por unidad
4. Usar tags para clasificar por tema y dificultad

**Estrategia de estudio**:
1. Estudiar en orden (respeta dependencias conceptuales)
2. No memorizar mecánicamente - entender derivaciones
3. Complementar con resolución de problemas
4. Relacionar conceptos entre unidades

**Formato matemático**:
- Las ecuaciones usan LaTeX ($$...$$)
- Anki soporta LaTeX con MathJax
- Instalar addon "MathJax" si es necesario
