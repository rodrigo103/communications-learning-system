---
tags:
  - wiki/espectro-expandido
source_file: explicaciones_anki/unidad_10/carta_54_aplicaciones-ofdm.md
curso: Sistemas de Comunicaciones
unidad: 10
---

# Aplicaciones de Spread Spectrum y OFDM

> **Last verified:** 2025-11-16 | **Verified by:** source

## Panorama General

Las tecnicas de espectro expandido y OFDM son la base de practicamente todos los sistemas de comunicacion inalambrica modernos. Esta pagina sintetiza las aplicaciones principales, desde GPS hasta 5G, pasando por WiFi, Bluetooth, y broadcasting digital. [source]

---

## Aplicaciones de Spread Spectrum

### GPS — Global Positioning System

**Tecnologia**: DSSS con codigos Gold.
- Frecuencia L1: 1575.42 MHz
- Chip rate: 1.023 Mchips/s, tasa de datos: 50 bps
- Ganancia de procesamiento: $G_p = 43$ dB
- Todos los satelites transmiten en la misma frecuencia, separados por codigos
- Senal recibida: $\sim 20$ dB por debajo del ruido termico
- La enorme $G_p$ permite recuperar la senal mediante correlacion sobre $20$ ms [analysis]

### Bluetooth

**Tecnologia**: FHSS con Adaptive Frequency Hopping (AFH).
- Banda ISM 2.4 GHz, 79 canales de 1 MHz
- 1600 saltos/segundo, slot de 625 $\mu$s
- AFH detecta canales ocupados por WiFi y los evita
- Aplicacion: redes personales (PAN), audio, perifericos

### Redes Celulares 3G

**WCDMA/UMTS**: CDMA de banda ancha (5 MHz).
- Chip rate: 3.84 Mcps
- Codigos OVSF para tasas variables
- Turbo codes para acercarse al limite de Shannon
- Soft handoff y diversidad de macrodiversidad

**CDMA2000**: evolucion de IS-95, hasta 3.1 Mbps con EV-DO.

### Comunicaciones Militares

- DSSS + FHSS hibrido para maxima robustez
- Baja probabilidad de deteccion/interceptacion (LPD/LPI)
- Resistencia a jamming: soportan interferencias 30-40 dB mas fuertes que la senal

---

## Aplicaciones de OFDM

### WiFi (IEEE 802.11)

| Estandar | FFT | $\Delta f$ | Modulacion max. | Throughput |
|----------|-----|------------|-----------------|------------|
| 802.11a/g | 64 | 312.5 kHz | 64-QAM | 54 Mbps |
| 802.11n | 64/128 | 312.5 kHz | 64-QAM + MIMO | 600 Mbps |
| 802.11ac | 256 | 78.125 kHz | 256-QAM + MU-MIMO | 6.9 Gbps |
| 802.11ax | 256 | 78.125 kHz | 1024-QAM + OFDMA | 9.6 Gbps |

WiFi 6 (802.11ax) introduce OFDMA para acceso multiple, reduciendo latencia en 75% para IoT.

### 4G LTE y 5G NR

**LTE**:
- OFDMA en downlink, SC-FDMA en uplink (mejor PAPR)
- $\Delta f = 15$ kHz, canales hasta 20 MHz (1200 subportadoras)
- MIMO hasta $8 \times 8$, modulacion hasta 256-QAM
- Carrier Aggregation: hasta 5 portadoras (100 MHz total)

**5G NR**:
- Numerologia flexible: $\Delta f = 15, 30, 60, 120, 240$ kHz
- mmWave (FR2): 24-52 GHz, canales de 100+ MHz
- Massive MIMO: 64-256 antenas en estacion base
- Codigos LDPC (datos) y Polar (control)
- Servicios: eMBB, URLLC, mMTC [source]

### TV Digital

- **DVB-T2**: OFDM con FFT de hasta 32K puntos, CP variable
- Single Frequency Networks: todos los transmisores en misma frecuencia
- 6-8 canales HD en el espectro de 1 canal analogico
- **ATSC 3.0** (USA): OFDM + LDPC + MIMO para broadcasting IP

### DSL

- DMT (Discrete Multitone): variante de OFDM para par de cobre
- ADSL: 256 subportadoras, adaptacion por tono
- VDSL2: hasta 4096 subportadoras, 100+ Mbps

---

## Tabla Resumen de Tecnologias por Aplicacion

| Aplicacion | Tecnologia | Banda | Caracteristica |
|------------|-----------|-------|----------------|
| Navegacion | DSSS (GPS) | L1/L2 | Correlacion precisa |
| PAN | FHSS (Bluetooth) | 2.4 GHz | Coexistencia |
| Celular 3G | CDMA | 850/1900 MHz | Soft capacity |
| Celular 4G | OFDMA | 0.7-3.5 GHz | Alta eficiencia |
| Celular 5G | OFDM + mmWave | 0.45-52 GHz | Flexibilidad |
| WiFi | OFDM | 2.4/5/6 GHz | WLAN alta velocidad |
| TV Digital | OFDM | VHF/UHF | SFN nacional |
| Militar | DS/FH hibrido | Variable | Maxima robustez |

## Tendencias

- **Convergencia**: WiFi y celular convergen en OFDM + MIMO
- **mmWave**: espectro abundante en frecuencias altas, compensado con Massive MIMO
- **IoT**: LoRa y NB-IoT usan variantes de spread spectrum para largo alcance y bajo consumo
- **6G**: investigacion en THz, AI-native networks, integracion sensing-comunicacion [analysis]

## Ver tambien

- [[espectro-expandido/cdma]]
- [[espectro-expandido/dsss]]
- [[espectro-expandido/fhss]]
- [[espectro-expandido/ofdm]]
- [[introduccion/espectro-electromagnetico]]
- [[conceptos-integradores/evolucion-sistemas]]
