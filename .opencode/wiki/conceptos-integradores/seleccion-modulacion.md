---
tags:
  - wiki/conceptos-integradores
source_file: explicaciones_anki/conceptos_integradores/carta_58_eficiencia_espectral_vs_potencia.md
curso: Sistemas de Comunicaciones
unidad: 9-10
---

# Criterios de Seleccion de Modulacion

> **Last verified:** 2025-11-16 | **Verified by:** source

## Marco de Decision

La seleccion de un esquema de modulacion es una decision de diseno que balancea recursos escasos y costosos: espectro, potencia y complejidad. Ningun esquema es optimo universalmente; la eleccion depende de las restricciones especificas de cada aplicacion. [source]

## Parametros de Comparacion

### Eficiencia Espectral

$$\boxed{\eta_B = \frac{R_b}{B} \quad \text{[bits/s/Hz]}}$$

Mide cuantos bits se transmiten por Hz de ancho de banda. Para modulacion M-aria ideal: $\eta_B = \log_2(M)$.

Valores tipicos: [analysis]
- BPSK: $\eta = 1$ (robuto, baja eficiencia)
- QPSK: $\eta = 2$ (balance)
- 64-QAM: $\eta = 6$ (alta eficiencia)
- 256-QAM: $\eta = 8$ (muy alta, requiere SNR alto)

### Eficiencia de Potencia

Medida por el $E_b/N_0$ requerido para cierto BER objetivo. Menor $E_b/N_0 \Rightarrow$ mayor eficiencia de potencia.

$$\boxed{\frac{E_b}{N_0} = SNR \cdot \frac{B}{R_b}}$$

### Complejidad de Implementacion

- Sincronizacion requerida (coherente vs no coherente)
- Linealidad del amplificador (PAPR)
- Procesamiento digital (FFT, decodificacion)
- Costo y consumo de potencia

## Arbol de Decision para Seleccion

### Por tipo de canal

| Condicion del Canal | Tecnologia Recomendada | Razon |
|--------------------|----------------------|-------|
| AWGN puro | QAM alto orden | Maxima eficiencia |
| Multitrayecto severo | OFDM | Ecualizacion simple |
| Desvanecimiento rapido | QPSK + diversidad | Robustez |
| Interferencia intencional | Spread spectrum | Anti-jamming |
| Doppler alto | BPSK/QPSK | Tolerancia a offset |

### Por recurso limitante

| Recurso Escaso | Estrategia | Ejemplo |
|---------------|-----------|---------|
| **Espectro** | Priorizar $\eta_B$: QAM alto orden, MIMO | Celular, cable, fibra |
| **Potencia** | Priorizar $\eta_P$: spread spectrum, codigos potentes | Satelite, espacio profundo, IoT |
| **Complejidad** | Esquemas simples: FSK, GMSK | Dispositivos de bajo costo |
| **Espectro + Potencia** | Modulacion adaptativa (AMC) | LTE, 5G, WiFi |

### Por aplicacion

| Aplicacion | Requisitos Clave | Modulacion Tipica |
|-----------|-----------------|-------------------|
| Radio AM/FM broadcast | Cobertura, simplicidad | AM, FM |
| Voz celular (2G) | Bateria, robustez | GMSK |
| Datos moviles (4G/5G) | Alta tasa, flexibilidad | OFDM + QAM adaptativo |
| WiFi indoor | Alta tasa, multitrayecto | OFDM + 256/1024-QAM |
| GPS | Precision temporal, anti-jamming | BPSK + DSSS |
| Espacio profundo | Maxima $\eta_P$ | BPSK + codigos potentes |
| TV digital | Broadcast, SFN | OFDM (DVB-T2) |
| IoT (bateria) | Bajo consumo, largo alcance | LoRa (CSS), NB-IoT |
| Bluetooth | Coexistencia, bajo costo | GFSK + FHSS |

## Relacion Fundamental de Shannon para Seleccion

El teorema de Shannon establece el limite del trade-off: [source]

$$\boxed{\frac{E_b}{N_0} = \frac{2^{\eta} - 1}{\eta}}$$

Interpretacion para la seleccion:
- Si $\eta$ deseada es baja ($< 1$): $E_b/N_0 \approx \ln(2) = -1.59$ dB como limite
- Si $\eta$ deseada es alta ($> 4$): $E_b/N_0$ crece exponencialmente
- **Cada bit/s/Hz adicional cuesta mas potencia que el anterior** (rendimientos decrecientes)

## Modulacion Adaptativa (AMC)

Los sistemas modernos no eligen un unico esquema sino que adaptan dinamicamente: [analysis]

| SNR disponible | Esquema | $\eta$ | Throughput (5 MHz) |
|---------------|---------|-------|-------------------|
| $< 5$ dB | QPSK 1/3 | 0.67 | Bajo |
| 5-10 dB | QPSK 1/2 | 1.0 | Medio |
| 10-15 dB | 16-QAM 2/3 | 2.67 | Alto |
| 15-20 dB | 64-QAM 3/4 | 4.5 | Muy alto |
| $> 20$ dB | 256-QAM 5/6 | 6.67 | Maximo |

Esto maximiza el throughput manteniendo BER objetivo, adaptandose a las condiciones variables del canal.

## Criterios Regulatorios

- **Bandas con licencia**: priorizar eficiencia espectral (el espectro es costoso)
- **Bandas ISM** (sin licencia): limitaciones de potencia, spread spectrum obligatorio en algunos casos
- **Estandares obligatorios**: GSM, LTE, 5G definen modulaciones especificas

## Errores Comunes en Seleccion

- Elegir la modulacion de mayor orden "porque es mejor": solo si hay SNR suficiente
- Ignorar el PAPR: QAM de alto orden requiere amplificadores lineales (costo y eficiencia)
- No considerar la latencia de procesamiento: OFDM + FEC introducen retardo
- Olvidar overhead: CP en OFDM, pilotos, preambulos reducen el throughput real

## Ver tambien

- [[conceptos-integradores/comparacion-global-modulaciones]]
- [[conceptos-integradores/compromisos-diseno]]
- [[conceptos-integradores/aplicaciones-reales]]
- [[conceptos-integradores/evolucion-sistemas]]
- [[teoria-informacion/teorema-shannon-hartley]]
- [[ruido/intercomparacion-sistemas]]
