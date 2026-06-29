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

### 5. La relacion entre PCM y ASK/FSK/PSK

Son etapas en cascada, no alternativas:
$$m(t) \xrightarrow{\text{PCM}} \text{bits} \xrightarrow{\text{ASK/FSK/PSK}} \text{señal RF}$$

PCM digitaliza la voz. ASK/FSK/PSK adaptan esos bits al canal inalambrico. [analysis]

### 6. OFDM y CDMA no son tipos de modulacion

Son tecnicas de **multiplexacion y acceso multiple**, no modulaciones en si mismas. OFDM usa QAM/PSK en cada subportadora. CDMA usa PSK + codigos de expansion. [analysis]

→ [[../espectro-expandido/ofdm|OFDM]]
→ [[../espectro-expandido/cdma|CDMA]]

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
