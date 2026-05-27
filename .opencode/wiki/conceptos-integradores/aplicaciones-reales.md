---
tags:
  - wiki/conceptos-integradores
source_file: explicaciones_anki/conceptos_integradores/carta_59_regeneracion_digital_vs_amplificacion_analogica.md
curso: Sistemas de Comunicaciones
unidad: 9-10
---

# Aplicaciones Reales de los Sistemas de Comunicaciones

> **Last verified:** 2025-11-16 | **Verified by:** source

## Mapeo de Tecnologias a Aplicaciones

Cada aplicacion real de comunicaciones impone restricciones unicas que determinan la eleccion de modulacion, codificacion y arquitectura. Esta pagina sintetiza el vinculo entre teoria y practica. [analysis]

---

## Broadcasting de Audio

### Radio AM
- **Modulacion**: AM-DSB-FC
- **Banda**: 530-1700 kHz (onda media)
- **Ventaja**: propagacion ionosferica (cientos de km de noche)
- **Desventaja**: baja fidelidad, susceptible a ruido atmosferico
- **Por que aun se usa**: receptores extremadamente simples y baratos; funciona con SNR muy bajo

### Radio FM
- **Modulacion**: FM banda ancha ($\Delta f = 75$ kHz)
- **Banda**: 88-108 MHz
- **Ventaja**: alta fidelidad (Hi-Fi), inmunidad al ruido (amplitud constante)
- **Regla de Carson**: $BW \approx 200$ kHz
- **Pre-enfasis/de-enfasis**: mejora SNR en $\sim 13$ dB adicionales

---

## Television Digital

### DVB-T2 (Europa)
- **Tecnologia**: OFDM con FFT de 1K a 32K puntos
- **CP variable**: permite Single Frequency Networks nacionales
- **LDPC + BCH**: codificacion cerca del limite de Shannon
- **Eficiencia**: 6-8 canales HD donde antes habia 1 analogico

### ATSC 3.0 (USA)
- OFDM + MIMO + LDPC
- Broadcasting IP nativo (servicios interactivos)
- Recepcion movil y fija

---

## Comunicaciones Moviles

### 2G — GSM
- **Modulacion**: GMSK (envolvente constante)
- **Acceso**: TDMA + FDMA, 8 usuarios por portadora de 200 kHz
- **Diseno**: prioriza duracion de bateria y simplicidad sobre tasa de datos
- Aun operativo como capa de cobertura basica (fallback) [analysis]

### 4G — LTE
- **Downlink**: OFDMA con $\Delta f = 15$ kHz
- **Uplink**: SC-FDMA (mejor PAPR para el movil)
- **Modulacion**: QPSK a 256-QAM adaptativa
- **MIMO**: hasta $8 \times 8$
- **Latencia**: $\sim 10$ ms

### 5G — NR
- **Tres casos de uso**:
  - **eMBB**: banda ancha mejorada (video 4K/8K, VR)
  - **URLLC**: ultra-confiable, baja latencia ($< 1$ ms)
  - **mMTC**: IoT masivo (1 millon de dispositivos/km${}^2$)
- mmWave (28, 39 GHz) para capacidad extrema en areas densas
- Massive MIMO con beamforming adaptativo

---

## Redes Inalambricas Locales (WiFi)

| Estandar | Tecnologia | Banda | Throughput max |
|----------|-----------|-------|---------------|
| 802.11b | DSSS | 2.4 GHz | 11 Mbps |
| 802.11a/g | OFDM 64-FFT | 5 / 2.4 GHz | 54 Mbps |
| 802.11n | OFDM + MIMO | 2.4/5 GHz | 600 Mbps |
| 802.11ac | OFDM + MU-MIMO | 5 GHz | 6.9 Gbps |
| 802.11ax | OFDMA | 2.4/5/6 GHz | 9.6 Gbps |

WiFi 6 introduce OFDMA (acceso multiple en frecuencia) y 1024-QAM, duplicando la eficiencia en entornos densos.

---

## Comunicaciones Satelitales

### Broadcast (DVB-S2)
- **Modulacion**: QPSK a 32-APSK
- **Codificacion**: LDPC + BCH
- **Eficiencia**: opera a $< 1$ dB del limite de Shannon

### GPS
- **Tecnologia**: DSSS, codigos Gold, chip rate 1.023 Mcps
- **Ganancia de procesamiento**: 43 dB — opera con senales bajo el ruido termico
- **CDMA**: 32 satelites comparten $f = 1575.42$ MHz
- Critico para: navegacion, sincronizacion de redes, operaciones financieras

### Espacio Profundo (Voyager, Mars Rovers)
- **Modulacion**: BPSK (maxima robustez)
- **Codigos**: Reed-Solomon + convolucional concatenados
- **Tasa**: $\sim 160$ bps desde 23 mil millones de km
- **$E_b/N_0$**: operando a $\sim 2$ dB, cerca del limite de Shannon

---

## Comunicaciones por Cable y Fibra

### DSL (ADSL, VDSL)
- **Tecnologia**: DMT (variante de OFDM)
- **Adaptacion**: water-filling por tono (mas bits en frecuencias con mejor SNR)
- **Limitacion**: atenuacion creciente con frecuencia y distancia

### Fibra Optica Submarina
- **Modulacion**: DP-QPSK, DP-16QAM (deteccion coherente)
- **Regeneracion**: cada 50-100 km (digital O-E-O)
- **Capacidad**: decenas de Tbps por fibra
- **Codificacion**: FEC con ganancia de $\sim 10$ dB permite espaciamiento amplio

---

## Bluetooth y Redes Personales

- **Modulacion**: GFSK (Gaussian Frequency Shift Keying)
- **Acceso**: FHSS con 79 canales de 1 MHz
- **AFH** (Adaptive Frequency Hopping): evita canales con interferencia WiFi
- **Eficiencia energetica**: disenado para dispositivos con bateria (bajo consumo)
- **Aplicaciones**: audio, perifericos, IoT, beacons

---

## Sistemas Militares y Seguros

- **Spread spectrum hibrido**: DSSS + FHSS para maxima robustez anti-jamming
- **Baja probabilidad de deteccion** (LPD): PSD bajo el ruido termico
- **Cifrado**: la secuencia PN agrega una capa adicional de seguridad
- **Costo**: complejidad y ancho de banda elevados, justificados por el requisito de supervivencia

---

## Tabla Resumen: Aplicacion $\to$ Tecnologia

| Aplicacion | Modulacion | Acceso / Tecnica | Clave de diseno |
|-----------|-----------|------------------|-----------------|
| Radio AM | AM-DSB-FC | SISO | Simplicidad, cobertura |
| Radio FM | FM WB | SISO | Calidad de audio |
| TV Digital | OFDM | DVB-T2 / ATSC 3.0 | SFN, compresion |
| 2G GSM | GMSK | TDMA + FDMA | Bateria, robustez |
| 4G LTE | QAM + OFDM | OFDMA + MIMO | Tasa de datos |
| 5G NR | QAM + OFDM | OFDMA + mMIMO | Flexibilidad |
| WiFi 6 | OFDM + 1024-QAM | OFDMA | Alta densidad |
| GPS | BPSK + DSSS | CDMA | Precision, anti-jam |
| Bluetooth | GFSK + FHSS | AFH | Bajo costo, coexistencia |
| Satelite | QPSK/APSK | DVB-S2 | Max $\eta_P$ |
| Fibra optica | DP-QAM | DWDM | Max $\eta_B$ |
| Espacio profundo | BPSK + FEC | SISO | Max $\eta_P$ extrema |

## Errores Comunes

- Asumir que la tecnologia mas avanzada (5G, WiFi 6) es siempre la mejor opcion: el contexto manda
- Ignorar que las generaciones coexisten como capas complementarias (cobertura + capacidad)
- No considerar el costo y consumo energetico en el diseno

## Ver tambien

- [[conceptos-integradores/comparacion-global-modulaciones]]
- [[conceptos-integradores/seleccion-modulacion]]
- [[conceptos-integradores/compromisos-diseno]]
- [[conceptos-integradores/evolucion-sistemas]]
- [[introduccion/espectro-electromagnetico]]
- [[introduccion/necesidad-modulacion]]
