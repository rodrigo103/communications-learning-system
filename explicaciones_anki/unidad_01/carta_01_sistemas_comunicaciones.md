# Carta 1: Sistemas de Comunicaciones - Componentes Fundamentales

## Pregunta
¿Qué es un sistema de comunicaciones y cuáles son sus componentes fundamentales?

## Respuesta Breve
Un sistema de comunicaciones es un conjunto de elementos que permite la transferencia de información desde una fuente hasta un destino. Sus componentes fundamentales son:
- **Fuente de información**: genera el mensaje
- **Transmisor**: convierte el mensaje en señal adecuada para el canal
- **Canal**: medio físico de transmisión
- **Receptor**: recupera la señal y la convierte al formato original
- **Destino**: usuario final de la información

## Explicación Detallada

### Introducción
Los sistemas de comunicaciones son la base de toda la tecnología moderna de información. Desde el teléfono hasta internet, desde la radio hasta las comunicaciones satelitales, todos estos sistemas comparten una arquitectura fundamental que fue formalizada por Claude Shannon en 1948. Comprender estos componentes es esencial para entender cómo funciona cualquier sistema de comunicación, ya sea analógico o digital, inalámbrico o por cable.

### Desarrollo Conceptual

#### 1. Fuente de Información
La fuente es el origen del mensaje que se desea transmitir. Puede ser:
- **Analógica**: como la voz humana, música, o señales de sensores
- **Digital**: como texto, datos de computadora, o información ya digitalizada

**Característica clave**: La fuente determina el ancho de banda y la tasa de información del sistema. Por ejemplo, la voz humana ocupa aproximadamente 300-3400 Hz, mientras que video de alta definición requiere varios MHz.

#### 2. Transmisor
El transmisor realiza varias funciones críticas:

a) **Acondicionamiento de señal**: filtra y amplifica la señal de la fuente
b) **Codificación**: puede incluir:
   - Codificación de fuente (compresión, reducción de redundancia)
   - Codificación de canal (agregar redundancia controlada para detección/corrección de errores)
c) **Modulación**: adapta la señal de información a las características del canal
   - Traslada la señal a una frecuencia apropiada
   - Permite multiplexación
   - Mejora inmunidad al ruido

**Ejemplo matemático**: En AM, el transmisor genera:
$$s(t) = [A_c + m(t)]\cos(2\pi f_c t)$$
donde $m(t)$ es la señal moduladora y $f_c$ la frecuencia de portadora.

#### 3. Canal
El canal es el medio físico que transporta la señal. Tipos principales:

**Canales guiados**:
- Cable coaxial
- Fibra óptica
- Par trenzado (twisted pair)

**Canales no guiados**:
- Espacio libre (radio, microondas)
- Ionosfera (comunicaciones HF)
- Guías de onda (frecuencias muy altas)

**Imperfecciones del canal**:
- **Atenuación**: pérdida de potencia con la distancia
- **Ruido**: señales no deseadas (térmico, impulsivo, etc.)
- **Distorsión**: no-linealidades y respuesta no plana en frecuencia
- **Interferencia**: otras señales, multitrayecto

La caracterización del canal incluye:
- **Ancho de banda**: rango de frecuencias que puede transmitir
- **Respuesta en frecuencia**: $H(f)$
- **Capacidad**: máxima tasa de información (Shannon)

#### 4. Receptor
El receptor invierte las operaciones del transmisor:

a) **Amplificación**: incrementa nivel de señal débil recibida
b) **Demodulación**: extrae la información de la portadora
c) **Decodificación**:
   - De canal: detecta/corrige errores
   - De fuente: descomprime información
d) **Filtrado**: elimina ruido fuera de banda

**Diseño crítico**: El receptor debe optimizar la relación señal-ruido (SNR) mientras mantiene la fidelidad de la señal. El teorema de igualación indica que la máxima SNR se obtiene con un filtro adaptado (matched filter).

#### 5. Destino
El usuario final o dispositivo que utiliza la información recibida. El destino define los requisitos de calidad del sistema:
- **Voz**: inteligibilidad, naturalidad
- **Datos**: tasa de error de bit (BER)
- **Video**: resolución, latencia

### Ejemplos Prácticos

#### Ejemplo 1: Sistema de Radio FM
- **Fuente**: Micrófono (voz/música) → señal de 50 Hz - 15 kHz
- **Transmisor**:
  - Preénfasis (realza altas frecuencias)
  - Modulación FM con $f_c$ = 88-108 MHz
  - Amplificación de potencia
- **Canal**: Espacio libre (propagación electromagnética)
- **Receptor**:
  - Antena capta señal
  - Superheterodino convierte a FI (10.7 MHz)
  - Discriminador demodula FM
  - Deénfasis restaura balance espectral
- **Destino**: Altavoces

#### Ejemplo 2: Enlace de Datos WiFi
- **Fuente**: Paquetes de datos TCP/IP
- **Transmisor**:
  - Codificación convolucional
  - Modulación OFDM con QAM
  - Frecuencias 2.4 o 5 GHz
- **Canal**: Aire (multitrayecto, desvanecimiento)
- **Receptor**:
  - Demodulación OFDM (FFT)
  - Ecualización
  - Decodificación Viterbi
- **Destino**: Computadora, smartphone

#### Ejemplo 3: Sistema Telefónico Digital (T1/E1)
- **Fuente**: Voz analógica (300-3400 Hz)
- **Transmisor**:
  - Muestreo: 8000 muestras/s (Nyquist)
  - Cuantificación: 8 bits con companding (μ-law/A-law)
  - PCM: 64 kbps por canal
  - TDM: 24 canales multiplexados
- **Canal**: Cable de cobre, fibra óptica
- **Receptor**:
  - Demultiplexación
  - Decodificación PCM
  - Expansor (descompresión)
  - Filtro pasa-bajos de reconstrucción
- **Destino**: Auricular telefónico

### Relación con Otros Conceptos

**Prerequisites necesarios**:
- Análisis de señales (dominio tiempo y frecuencia)
- Transformada de Fourier
- Conceptos de probabilidad (para ruido)

**Conexiones con temas posteriores**:
- **Modulación**: el "cómo" del transmisor (Unidades 3, 4, 5, 6)
- **Ruido**: limitación fundamental del canal (Unidad 7)
- **Capacidad del canal**: límite teórico (Shannon - Unidad 9)
- **Codificación**: mejora de confiabilidad y eficiencia (Unidad 9)

**Modelo de Shannon**: Este modelo de 5 componentes es la base conceptual para:
- Teoría de la Información
- Diseño de sistemas
- Análisis de desempeño
- Optimización de recursos

### Puntos Clave para Recordar

1. **Flujo de información**: Fuente → Transmisor → Canal → Receptor → Destino
2. **Transmisor y receptor son inversos**: operaciones complementarias
3. **El canal es imperfecto**: introduce ruido, atenuación, distorsión
4. **Modulación es esencial**: adapta señal al canal y permite compartir recursos
5. **Trade-off fundamental**: Ancho de banda ↔ SNR ↔ Tasa de información (Shannon)

**Fórmulas importantes**:
- Capacidad de Shannon: $C = B\log_2(1 + S/N)$ bits/s
- SNR en dB: $SNR_{dB} = 10\log_{10}(S/N)$
- Potencia recibida: $P_r = P_t G_t G_r (\lambda/4\pi d)^2$ (Friis)

### Errores Comunes

1. **Confundir fuente con transmisor**: La fuente genera información, el transmisor la prepara para transmisión
2. **Ignorar el ruido del canal**: Ningún canal real es perfecto; el ruido es inevitable
3. **Pensar que más potencia siempre es mejor**: Existe un límite teórico (Shannon) independiente de la potencia
4. **Olvidar la sincronización**: Los receptores coherentes necesitan sincronismo con el transmisor
5. **No considerar ancho de banda**: Es un recurso limitado y valioso, regulado internacionalmente

### Referencias y Profundización

**Conceptos fundamentales relacionados**:
- Modelo de Shannon-Weaver (teoría de información)
- Ecuación de Friis (comunicaciones inalámbricas)
- Teorema de muestreo de Nyquist
- Criterio de Nyquist para ISI

**Temas para estudiar más**:
- Arquitecturas de receptores (superheterodino, conversión directa, SDR)
- Efectos de propagación (desvanecimiento, multitrayecto, Doppler)
- Estándares de comunicaciones (IEEE 802.x, 3GPP, ITU)
- Medidas de calidad (SNR, BER, SINAD, EVM)

**Libros de referencia**:
- Haykin, "Communication Systems"
- Proakis & Salehi, "Fundamentals of Communication Systems"
- Taub & Schilling, "Principles of Communication Systems"

**Aplicaciones para explorar**:
- Sistemas celulares (2G/3G/4G/5G)
- Comunicaciones satelitales (GEO, LEO)
- Radar y sensores remotos
- Sistemas ópticos (fibra, free-space optics)
