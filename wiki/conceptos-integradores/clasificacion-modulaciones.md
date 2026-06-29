---
tags:
  - wiki/conceptos-integradores
curso: Sistemas de Comunicaciones
---

# Clasificacion de los Tipos de Modulacion

> **Last verified:** 2026-06-10 | **Verified by:** analysis

Todas las modulaciones del curso se organizan en una jerarquia con **dos ejes de clasificacion**: el tipo de portadora y la naturaleza de la informacion moduladora.

---

## Arbol Taxonomico

```
MODULACION
│
├─── ANALOGICA (portadora senoidal)
│    ├─── AM (DSB, SSB, VSB)
│    ├─── FM
│    └─── PM
│
└─── PULSOS (portadora = tren de pulsos)
     │
     ├─── ANALOGICA (muestras con valor continuo)
     │    ├─── PAM (Pulse Amplitude Modulation)
     │    ├─── PWM (Pulse Width Modulation)
     │    └─── PPM (Pulse Position Modulation)
     │
     └─── DIGITAL (muestras cuantificadas)
          │
          ├─── BANDA BASE (pulsos directos, sin portadora senoidal)
          │    └─── PCM (Pulse Code Modulation)
          │         └─── Variantes: Delta, DPCM, ADPCM
          │
          └─── PASO-BANDA (pulsos + portadora senoidal)
               ├─── ASK (Amplitude Shift Keying)
               ├─── FSK (Frequency Shift Keying)
               └─── PSK (Phase Shift Keying)
                    └─── Variantes: QPSK, QAM, etc.
```

## Matriz 2D de Clasificacion

La clasificacion se entiende mejor como una tabla de dos dimensiones:

```
                     Naturaleza de la informacion
                     Analoga           Digital
               ┌──────────────┬──────────────┐
Portadora      │              │              │
               │              │              │
Senoidal       │  AM, FM, PM  │ ASK, FSK,    │
               │              │ PSK, QAM     │
               ├──────────────┼──────────────┤
               │              │              │
Pulsos         │  PAM, PWM,   │    PCM       │
               │  PPM        │              │
               └──────────────┴──────────────┘
```

Las dos filas estan conectadas: PCM genera los bits que alimentan ASK/FSK/PSK. [analysis]

---

## Rama 1: Modulacion Analogica (Portadora Senoidal)

La informacion moduladora $m(t)$ es una señal **analogica continua**. La portadora es una senoidal $A_c \cos(2\pi f_c t + \phi)$.

### AM — Amplitude Modulation

La amplitud de la portadora varia proporcionalmente a $m(t)$:

$$\boxed{s_{AM}(t) = [A_c + m(t)] \cos(2\pi f_c t)}$$

Variantes:
- **DSB-FC**: AM convencional (portadora + dos bandas laterales). Robusta, simple, ineficiente (~33% de potencia util)
- **DSB-SC**: Portadora suprimida. 100% de eficiencia de potencia, pero requiere demodulacion coherente
- **SSB (BLU)**: Una sola banda lateral. Maxima eficiencia espectral analogica
- **VSB**: Banda lateral vestigial. Compromiso usado en TV analogica

→ [[../modulacion-analogica/am-vs-dsb-sc|AM vs DSB-SC]]
→ [[../modulacion-analogica/modulacion-ssb|Modulacion SSB]]
→ [[../modulacion-analogica/modulacion-vsb|Modulacion VSB]]

### FM — Frequency Modulation

La frecuencia instantanea de la portadora varia proporcionalmente a $m(t)$:

$$\boxed{f_i(t) = f_c + k_f m(t)}$$

$$\boxed{s_{FM}(t) = A_c \cos\left[2\pi f_c t + 2\pi k_f \int_0^t m(\tau) d\tau\right]}$$

Ancho de banda (regla de Carson): $B_T \approx 2(\Delta f + f_m)$. Alta inmunidad al ruido a cambio de mayor ancho de banda. [analysis]

→ [[../modulacion-analogica/fm-vs-pm|FM vs PM]]
→ [[../modulacion-analogica/ancho-banda-carson|Regla de Carson]]

### PM — Phase Modulation

La fase instantanea varia proporcionalmente a $m(t)$:

$$\boxed{\phi(t) = k_p m(t)}$$

$$\boxed{s_{PM}(t) = A_c \cos[2\pi f_c t + k_p m(t)]}$$

FM y PM estan matematicamente relacionadas: PM es FM con $m(t)$ derivada (o FM es PM con $m(t)$ integrada). PM es el precursor analogico de PSK. [analysis]

→ [[../modulacion-analogica/fm-vs-pm|FM vs PM]]

---

## Rama 2: Modulacion de Pulsos

La portadora es un **tren de pulsos periodicos**. La señal de informacion se muestrea a $f_s$ y cada muestra modifica un parametro del pulso.

### Sub-rama 2A: Modulacion Analogica de Pulsos

Cada muestra representa el valor **exacto (continuo)** de $m(t)$ en ese instante. La informacion sigue siendo analogica, solo que existe en instantes discretos. [analysis]

| Tipo | Parametro modulado | Caracteristica |
|------|-------------------|----------------|
| **PAM** | Amplitud del pulso | Amplitud $\propto m(t)$ |
| **PWM** | Ancho del pulso | Duty cycle $\propto m(t)$ |
| **PPM** | Posicion del pulso | Desplazamiento temporal $\propto m(t)$ |

→ [[../modulacion-pulsos/pcm-cuantificacion|PCM y Cuantificacion]] (introduccion a PAM/PWM/PPM)

### Sub-rama 2B: Modulacion Digital de Pulsos

Las muestras se **cuantifican** a valores discretos → son **bits**. Este es el salto de analogico a digital. [analysis]

#### PCM — Pulse Code Modulation (Banda Base)

Digitalizacion completa en 3 etapas:

$$\boxed{\text{Muestrear} \rightarrow \text{Cuantificar} \rightarrow \text{Codificar}}$$

- $f_s = 8$ kHz para voz telefonica (Nyquist: $f_s \geq 2B$)
- Cuantificacion: 8 bits/muestra = 256 niveles
- Tasa resultante: 64 kbps por canal (base de T1/E1)

Variantes:
- **Delta (DM)**: 1 bit/muestra, transmite diferencias
- **DPCM**: Transmite diferencia con prediccion
- **ADPCM**: DPCM con paso y predictor adaptativos

→ [[../modulacion-pulsos/pcm-cuantificacion|PCM y Cuantificacion]]
→ [[../modulacion-pulsos/modulacion-delta|Modulacion Delta]]
→ [[../modulacion-pulsos/companding|Companding]]
→ [[../modulacion-pulsos/multiplex-tdm|TDM y Jerarquias T1/E1]]

#### Modulacion Digital Paso-Banda

Los bits generados por PCM se transmiten usando una **portadora senoidal**. Un parametro de la portadora toma valores discretos segun los bits. [analysis]

##### Por que se llama "paso-banda"

El espectro de los bits (banda base, centrado en $f = 0$) se **traslada** a la frecuencia de la portadora $f_c$ mediante la multiplicacion por $\cos(2\pi f_c t)$. La señal resultante ocupa una banda alrededor de $f_c$, no alrededor de $0$ → es una señal **paso-banda**. [analysis]

```
Espectro banda base           Espectro paso-banda
     |                              |
     |  ████                        |              ████         ████
     |  ████                        |              ████         ████
     |__████____f                   |______________████_________████____f
        0                                        -fc          +fc
```

##### De analogico a digital: el paralelo directo

ASK, FSK y PSK son las versiones **digitales** de AM, FM y PM. La diferencia es que el parametro modulado ya no varia continuamente segun $m(t)$, sino que solo toma **valores discretos** determinados por los bits:

| Analogica | Digital | Que cambia |
|-----------|---------|-------------|
| **AM**: amplitud varia con $m(t)$ continua | **ASK**: amplitud toma valores discretos (ej: 0 o $A_c$) |
| **FM**: frecuencia varia con $m(t)$ continua | **FSK**: frecuencia salta entre $f_0$ y $f_1$ |
| **PM**: fase varia con $m(t)$ continua | **PSK**: fase salta entre valores fijos (ej: $0^\circ$, $180^\circ$) |

##### El flujo completo

$$m(t) \xrightarrow{\text{Muestreo}} \text{muestras} \xrightarrow{\text{Cuantificacion}} \text{bits} \xrightarrow{\text{ASK/FSK/PSK}} \text{señal RF en } f_c$$

1. La voz $m(t)$ se muestrea y cuantifica → bits (PCM)
2. Los bits controlan un **commutador digital** que selecciona entre parametros discretos de portadora
3. La portadora senoidal modificada se transmite por la antena

Ejemplo concreto con BPSK y el bit "1":
- Bit = 1 → commutador selecciona fase $0^\circ$ → $s(t) = A_c \cos(2\pi f_c t + 0^\circ)$
- Bit = 0 → commutador selecciona fase $180^\circ$ → $s(t) = A_c \cos(2\pi f_c t + 180^\circ) = -A_c \cos(2\pi f_c t)$

##### Simbolos, bits y tasa

Cada cambio de parametro de la portadora es un **simbolo**. Un simbolo puede representar 1 bit (BPSK), 2 bits (QPSK), 4 bits (16-QAM), etc.:

$$\boxed{R_b = R_s \cdot \log_2 M}$$

Donde $R_s$ = simbolos/segundo (baudios), $M$ = numero de simbolos distintos, $R_b$ = bits/segundo. [analysis]

No puede haber PCM sin ASK, FSK o PSK?

> [!note]- PCM sin modulacion paso-banda
> Si, PCM **no necesita** ASK/FSK/PSK para existir. PCM es una modulacion **banda base**: los bits se transmiten directamente como pulsos electricos sobre un cable, sin portadora senoidal. Ejemplos reales:
> - **T1/E1**: 24/30 canales PCM sobre par trenzado (1.5/2.0 Mbps) — sin portadora de RF
> - **Audio digital**: CD, S/PDIF, AES/EBU transmiten PCM por cable coaxial/optico
> - **USB, Ethernet**: los bits viajan en banda base como tensiones electricas sobre cobre
>
> ASK/FSK/PSK solo se necesitan cuando los bits deben transmitirse por un **canal inalambrico** (radio) o un canal paso-banda (fibra optica, cable coaxial de RF). Son dos etapas diferentes: PCM *digitaliza*, ASK/FSK/PSK *radioenlazan*:
> $$m(t) \xrightarrow{\text{PCM}} \text{bits} \xrightarrow{\text{ASK/FSK/PSK}} \text{señal RF}$$
> La primera etapa (PCM) es suficiente para comunicacion por cable. La segunda solo es necesaria si el canal es inalambrico.

| Tipo | Parametro modulado | Ejemplo binario |
|------|-------------------|-----------------|
| **ASK** | Amplitud | Bit 1 → $A \cos(2\pi f_c t)$, Bit 0 → 0 (OOK) |
| **FSK** | Frecuencia | Bit 1 → $f_1$, Bit 0 → $f_0$ |
| **PSK** | Fase | Bit 1 → fase $0^\circ$, Bit 0 → fase $180^\circ$ (BPSK) |

Extensiones M-arias (mas de 1 bit por simbolo):
- **QPSK**: 4 fases → 2 bits/simbolo
- **M-PSK**: M fases → $\log_2 M$ bits/simbolo
- **QAM**: Amplitud Y fase (constelacion 2D) → maxima eficiencia espectral

$$\boxed{R_b = R_s \cdot \log_2 M}$$

→ [[../modulacion-digital/ask-fsk-psk|ASK, FSK, PSK]]
→ [[../modulacion-digital/modulacion-qam|QAM]]
→ [[../modulacion-digital/constelaciones|Constelaciones]]
→ [[../modulacion-digital/probabilidad-error|Probabilidad de Error (BER)]]

---

## Aclaraciones de Conceptos que Suelen Confundirse

### 1. PAM/PWM/PPM NO son digitales

Son modulaciones **analogicas** de pulsos. La amplitud, ancho o posicion del pulso toma valores **continuos** proporcionales a $m(t)$. No hay cuantificacion. [analysis]

### 2. PCM es digital, pero es banda base (sin portadora senoidal)

PCM convierte la señal a bits, pero esos bits se transmiten como pulsos electricos directamente. Si queremos transmitirlos por radio, necesitamos una segunda etapa: modulacion digital paso-banda (ASK/FSK/PSK). [analysis]

### 3. PM y PSK no son lo mismo

PM es modulacion **analogica** de fase: $\phi(t)$ varia continuamente con $m(t)$.
PSK es modulacion **digital** de fase: $\phi(t)$ solo toma valores discretos (ej: $0^\circ$ o $180^\circ$).
PM es el precursor conceptual de PSK, pero con informacion de distinta naturaleza. [analysis]

### 4. QAM no es un tipo aparte de PSK

QAM es una generalizacion de PSK que modula **amplitud y fase simultaneamente**. La constelacion tiene puntos distribuidos en 2D en lugar de sobre un circulo. Es la modulacion digital de mayor eficiencia espectral. [analysis]

> [!note]- QPSK y 4-QAM son identicas
> En el diagrama de constelaciones, **QPSK = 4-QAM**. Ambas producen los mismos 4 puntos en las esquinas de un cuadrado, separados $90^\circ$:
> ```
>          Q
>          |
>    01 ●  |  ● 00
>          |
>    ------+------ I
>          |
>    11 ●  |  ● 10
>          |
> ```
> La diferencia es solo conceptual:
> - **QPSK** se piensa como modulacion de fase pura: 4 fases posibles ($\pi/4$, $3\pi/4$, $5\pi/4$, $7\pi/4$)
> - **4-QAM** se piensa como modulacion I/Q: $s(t) = \pm 1 \cdot \cos(2\pi f_c t) \pm 1 \cdot \sin(2\pi f_c t)$
>
> Ambas generan exactamente la misma señal matematica. La diferencia practica esta en como se implementa el modulador (desfasador vs mezclador I/Q), pero el resultado es identico.
>
> A partir de 16-QAM, los puntos ya **no** estan sobre un circulo (tienen distintas amplitudes), y ahi QAM y PSK si son familias distintas.

> [!note]- Jerarquia de ordenes: de BPSK a 1024-QAM
> El **orden** de una modulacion es el numero de puntos en la constelacion ($M$). A mayor orden, mas bits por simbolo, pero menor robustez (se necesita mas $E_b/N_0$ para la misma BER):
>
> | Orden | Modulacion | Bits/simbolo | $E_b/N_0$ tipico (BER $10^{-5}$) |
> |-------|-----------|-------------|-----------------------------------|
> | $M=2$ | **BPSK** (2-QAM) | 1 | ~9.6 dB — la mas robusta |
> | $M=4$ | **QPSK** (4-QAM) | 2 | ~9.6 dB — igual robustez por bit |
> | $M=8$ | 8-PSK | 3 | ~14 dB |
> | $M=16$ | 16-QAM | 4 | ~13 dB |
> | $M=64$ | 64-QAM | 6 | ~18 dB |
> | $M=256$ | 256-QAM | 8 | ~24 dB |
> | $M=1024$ | 1024-QAM | 10 | ~30 dB |
>
> BPSK y QPSK comparten el mismo $E_b/N_0$ requerido: son igual de eficientes energeticamente. Pero QPSK duplica los bits en el mismo ancho de banda, por eso es preferida cuando hay suficiente SNR. A partir de 8-PSK y 16-QAM, la eficiencia energetica empeora, pero la eficiencia espectral mejora.

### 5. La relacion entre PCM y ASK/FSK/PSK

Son etapas en cascada, no alternativas:
$$m(t) \xrightarrow{\text{PCM}} \text{bits} \xrightarrow{\text{ASK/FSK/PSK}} \text{señal RF}$$

PCM digitaliza la voz. ASK/FSK/PSK adaptan esos bits al canal inalambrico. [analysis]

### 6. OFDM y CDMA no son tipos de modulacion

Son tecnicas de **multiplexacion y acceso multiple**, no modulaciones en si mismas. OFDM usa QAM/PSK en cada subportadora. CDMA usa PSK + codigos de expansion. [analysis]

### 7. AM y ASK usan el mismo circuito (producto)

Ambos emplean un **modulador de producto** (multiplicador). La unica diferencia es la señal de entrada: [analysis]

- **AM**: $(A_c + m(t)) \times \cos(2\pi f_c t)$ — $m(t)$ analogica con offset DC para no suprimir la portadora
- **ASK (OOK)**: $\text{bit}(t) \times \cos(2\pi f_c t)$ — señal binaria ($0$ o $A_c$) sin offset
- **DSB-SC**: $m(t) \times \cos(2\pi f_c t)$ — $m(t)$ analogica sin offset (portadora suprimida)

El multiplicador es el mismo. Que sea AM, ASK o DSB-SC depende de que entra por la entrada de modulacion.

### 8. FM↔FSK y PM↔PSK comparten el mismo principio de circuito

La misma relacion se extiende a las otras familias: [analysis]

- **FM ↔ FSK**: un VCO recibe $m(t)$ continua → FM. El mismo VCO recibe bits (tension alta/baja) → FSK. En implementaciones baratas a veces se usan dos osciladores conmutados para FSK, pero el principio es identico.
- **PM ↔ PSK**: un desfasador controlado por $m(t)$ continua → PM. Con bits → PSK.

**El circuito que varia el parametro no sabe si la entrada es analogica o digital.** Lo que cambia es la naturaleza de la señal moduladora, no el modulador.

### 9. ASK no es solo OOK

Aunque OOK (bit 0 = sin señal) es la forma mas comun de ASK, existen variantes: [analysis]

- **ASK binaria con dos amplitudes no nulas**: bit 1 = $A_1$, bit 0 = $A_0$, ambas > 0. Poco usada porque OOK da mas distancia entre simbolos.
- **M-ASK**: mas de 2 amplitudes discretas (ej: 4-ASK = 4 niveles = 2 bits/simbolo). Rara vez se usa sola; se prefiere QAM.

En la practica, "ASK" casi siempre significa OOK.

> [!note]- M-ASK y M-PAM: el mismo mapeo en banda base y paso-banda
> **M-PAM** y **M-ASK** usan el mismo conjunto de $M$ amplitudes discretas. La diferencia es si hay portadora:
>
> | | M-PAM | M-ASK |
> |--|-------|-------|
> | **Tipo** | Digital banda base | Digital paso-banda |
> | **Señal** | $A_m \cdot p(t)$ | $A_m \cdot \cos(2\pi f_c t)$ |
> | **Espectro** | Centrado en $f = 0$ | Centrado en $\pm f_c$ |
> | **Bits/simbolo** | $\log_2 M$ | $\log_2 M$ |
>
> M-ASK **es** M-PAM trasladado a $f_c$. Los niveles de amplitud y el mapeo de bits son identicos. La unica diferencia es la multiplicacion por la portadora senoidal.
>
> Ejemplo 4-PAM / 4-ASK con $M=4$ niveles: $\{-3d, -d, +d, +3d\}$, 2 bits por simbolo, mapeo Gray:
> ```
> Bits   Nivel   4-PAM (banda base)       4-ASK (paso-banda)
> 00     -3d     pulso de altura -3d      -3d · cos(2π fc t)
> 01     -d      pulso de altura -d       -d  · cos(2π fc t)
> 11     +d      pulso de altura +d       +d  · cos(2π fc t)
> 10     +3d     pulso de altura +3d      +3d · cos(2π fc t)
> ```
>
> En la practica, M-PAM se usa en banda base (Ethernet 1000BASE-T usa 5-PAM). M-ASK solo casi nunca se usa porque QAM aprovecha mejor las dos dimensiones (I/Q) para la misma energia.

→ [[../espectro-expandido/ofdm|OFDM]]
→ [[../espectro-expandido/cdma|CDMA]]

---

## Tabla de Referencia Rapida: Modulacion, Multiplexacion y Acceso Multiple

### Modulacion de Pulsos

| Sigla | Nombre | Tipo | Descripcion |
|-------|--------|------|-------------|
| **PAM** | Pulse Amplitude Modulation | Analogica | Amplitud del pulso $\propto m(t)$ continua |
| **PWM** | Pulse Width Modulation | Analogica | Ancho del pulso $\propto m(t)$ continua |
| **PPM** | Pulse Position Modulation | Analogica | Posicion del pulso $\propto m(t)$ continua |
| **PCM** | Pulse Code Modulation | Digital banda base | Muestreo + cuantificacion + codificacion binaria |
| **M-PAM** | M-ary PAM | Digital banda base | PAM con $M$ niveles discretos de amplitud ($\log_2 M$ bits/simbolo) |
| **Delta (DM)** | Delta Modulation | Digital banda base | 1 bit/muestra: transmite si la señal sube o baja |
| **DPCM** | Differential PCM | Digital banda base | Transmite diferencia cuantificada entre muestras |
| **ADPCM** | Adaptive DPCM | Digital banda base | DPCM con paso de cuantificacion y predictor adaptativos |

### Modulacion Digital Paso-Banda

| Sigla | Nombre | Bits/simbolo | Descripcion |
|-------|--------|-------------|-------------|
| **ASK (OOK)** | Amplitude Shift Keying | 1 | Amplitud toma 2 valores discretos |
| **FSK** | Frequency Shift Keying | 1 | Frecuencia salta entre $f_0$ y $f_1$ |
| **BPSK** | Binary Phase Shift Keying | 1 | Dos fases: $0^\circ$ y $180^\circ$. La mas robusta |
| **QPSK** | Quadrature PSK | 2 | 4 fases: $0^\circ, 90^\circ, 180^\circ, 270^\circ$ |
| **OQPSK** | Offset QPSK | 2 | QPSK con rama Q retrasada medio simbolo → evita cruces por cero |
| **M-PSK** | M-ary PSK | $\log_2 M$ | M fases equidistantes sobre un circulo |
| **8-PSK** | 8-ary PSK | 3 | 8 fases a $45^\circ$ |
| **QAM** | Quadrature Amplitude Modulation | $\log_2 M$ | Amplitud + fase (constelacion 2D). 16/64/256/1024-QAM |
| **DBPSK** | Differential BPSK | 1 | BPSK con codificacion diferencial (no necesita referencia de fase) |
| **DQPSK** | Differential QPSK | 2 | QPSK con codificacion diferencial |
| **8-DPSK** | 8-ary DPSK | 3 | 8-PSK con codificacion diferencial |
| **GMSK** | Gaussian Minimum Shift Keying | 1 | FSK de fase continua con filtro gaussiano (GSM) |
| **GFSK** | Gaussian FSK | 1 | FSK con filtro gaussiano (Bluetooth) |
| **CPM** | Continuous Phase Modulation | variable | Familia de modulaciones con fase continua (sin saltos bruscos) |

### Multiplexacion y Acceso Multiple

| Sigla | Nombre | Dominio | Descripcion |
|-------|--------|--------|-------------|
| **FDM** | Frequency Division Multiplexing | Frecuencia | Señales en distintas bandas de frecuencia (analogico) |
| **FDMA** | Frequency Division Multiple Access | Frecuencia | Acceso multiple por FDM (1G) |
| **TDM** | Time Division Multiplexing | Tiempo | Señales en distintos slots de tiempo |
| **TDMA** | Time Division Multiple Access | Tiempo | Acceso multiple por TDM (2G GSM) |
| **CDM** | Code Division Multiplexing | Codigo | Señales separadas por codigos ortogonales |
| **CDMA** | Code Division Multiple Access | Codigo | Acceso multiple por CDM (3G) |
| **OFDM** | Orthogonal Frequency Div. Multiplexing | Frecuencia | Multiportadora con subportadoras ortogonales |
| **OFDMA** | Orthogonal Frequency Div. Multiple Access | Frecuencia | Acceso multiple por OFDM (4G/5G) |
| **WDM** | Wavelength Division Multiplexing | Longitud de onda | Multiplexacion optica en fibra |

### Combinaciones y Tecnicas Hibridas

| Combinacion | Descripcion | Ejemplo |
|-------------|-------------|---------|
| **PAM-TDM** | PAM analogica multiplexada en tiempo | Sistema telefonico analogico multiplexado |
| **PCM-TDM** | PCM + TDM: canales digitales en slots temporales | T1 (24 canales), E1 (30 canales) |
| **TDM + FDM** | Jerarquia: señales TDM moduladas en distintas portadoras FDM | Radioenlaces PDH |
| **WDM + TDM** | Longitudes de onda con slots temporales en cada una | OTN (Optical Transport Network) |
| **DSSS (CDMA)** | Datos × secuencia PN de alta velocidad | GPS, IS-95, WCDMA |
| **FHSS** | Portadora salta entre frecuencias segun secuencia PN | Bluetooth, militar |
| **OFDM + QAM** | Cada subportadora OFDM modulada con QAM/PSK | WiFi, LTE, 5G, DVB-T |
| **SC-FDMA** | OFDM con precodificacion DFT para reducir PAPR | LTE uplink |
| **TCM** | Trellis Coded Modulation: modulacion + FEC conjunta | Modems de banda vocal |

---

## Ver Tambien

- [[../modulacion-analogica/am-vs-dsb-sc|AM vs DSB-SC]]
- [[../modulacion-analogica/modulacion-ssb|Modulacion SSB]]
- [[../modulacion-analogica/fm-vs-pm|FM vs PM]]
- [[../modulacion-analogica/ancho-banda-carson|Regla de Carson]]
- [[../modulacion-pulsos/pcm-cuantificacion|PCM y Cuantificacion]]
- [[../modulacion-pulsos/modulacion-delta|Modulacion Delta]]
- [[../modulacion-digital/ask-fsk-psk|ASK, FSK, PSK]]
- [[../modulacion-digital/modulacion-qam|QAM]]
- [[../modulacion-digital/constelaciones|Constelaciones]]
- [[../espectro-expandido/ofdm|OFDM]]
- [[../espectro-expandido/cdma|CDMA]]
- [[comparacion-global-modulaciones|Comparacion Global de Modulaciones]]
- [[../resumenes/overview-curso|Resumen General del Curso]]
