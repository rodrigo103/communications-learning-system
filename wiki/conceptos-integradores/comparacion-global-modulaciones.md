---
tags:
  - wiki/conceptos-integradores
source_file: explicaciones_anki/conceptos_integradores/carta_56_tradeoff_bw_potencia_shannon.md
curso: Sistemas de Comunicaciones
unidad: 9-10
---

# Comparacion Global de Modulaciones

> **Last verified:** 2025-11-16 | **Verified by:** source

## Marco de Comparacion

La comparacion entre modulaciones se realiza sobre tres ejes fundamentales derivados del teorema de Shannon y de las metricas de desempeno practicas: [source — [[../../explicaciones_anki/conceptos_integradores/carta_56_tradeoff_bw_potencia_shannon]]]

$$\boxed{C = B \log_2\left(1 + \frac{S}{N}\right)}$$

De esta ecuacion se desprenden las relaciones entre **ancho de banda** ($B$), **potencia** ($S/N$), **eficiencia espectral** ($\eta = R_b/B$), y **complejidad de implementacion**.

## Tabla Comparativa Global

### Modulaciones Analogicas

| Modulacion | $\eta$ (aprox) | Eficiencia Potencia | Complejidad | Inmunidad Ruido | Aplicacion |
|-----------|----------------|---------------------|-------------|-----------------|------------|
| AM-DSB-FC | Baja | Pobre (33% max) | Baja | Mala | Radio AM |
| AM-DSB-SC | Media | 100% | Media | Mala | Baja |
| SSB | Alta | 100% | Alta | Mala | HF militar |
| FM banda angosta | Baja | Alta | Media | Buena | Radio movil |
| FM banda ancha | Muy baja | Alta | Media | Excelente | Radio FM broadcast |

### Modulaciones Digitales

| Modulacion | $\eta$ (bits/s/Hz) | $E_b/N_0$ @ BER $10^{-6}$ | PAPR | Aplicacion |
|-----------|--------------------|-----------------------------|------|------------|
| BPSK | 1 | 10.5 dB | 0 dB | Enlaces robustos, espacio profundo |
| QPSK | 2 | 10.5 dB | 0 dB | Satelite, 3G, LTE uplink |
| 8-PSK | 3 | 14 dB | 0 dB | Satelite DVB-S2 |
| 16-QAM | 4 | 14.5 dB | 2.6 dB | LTE, WiFi |
| 64-QAM | 6 | 18.5 dB | 3.7 dB | WiFi, cable |
| 256-QAM | 8 | 23 dB | 4.2 dB | DOCSIS, WiFi 6 |
| 1024-QAM | 10 | ~27 dB | 4.8 dB | WiFi 6 |

### Sistemas Multiacceso

| Sistema | Generacion | $\eta$ tipica | Tecnologia | Capacidad relativa |
|---------|-----------|---------------|------------|-------------------|
| GSM (TDMA) | 2G | 1.35 | GMSK | 1x |
| IS-95 (CDMA) | 2G/3G | 0.1-0.3 | QPSK + DSSS | 3-4x vs GSM |
| WCDMA | 3G | 0.5-2 | QPSK/16-QAM | 5-8 Mbps/sector |
| LTE | 4G | 1.5-5 | OFDMA + 64-QAM | 100+ Mbps |
| 5G NR | 5G | 2-8+ | OFDM + 256-QAM | 1+ Gbps |

## Trade-off Ancho de Banda vs Potencia

El teorema de Shannon revela que $B$ y $S/N$ son **intercambiables** pero con rendimientos diferentes: [analysis]

### Regimen de alto SNR (limitado por BW)

$$C \approx B \log_2(S/N)$$

- El BW es el recurso mas valioso: duplicar BW duplica $C$, duplicar potencia solo agrega $\sim 1$ bit/s/Hz.
- Estrategia: modulaciones de alto orden (QAM) y MIMO.
- Sistemas tipicos: fibra optica, cable, WiFi cercano.

### Regimen de bajo SNR (limitado por potencia)

$$C \approx 1.44 \cdot B \cdot \frac{S}{N}$$

- Ambos recursos son igualmente valiosos.
- Estrategia: spread spectrum, codigos de baja tasa.
- Sistemas tipicos: espacio profundo, GPS, satelite marginado.

### Punto de transicion

En $SNR = 0$ dB ($= 1$ lineal), ambos recursos tienen exactamente la misma efectividad marginal.

## Eficiencia Espectral vs Eficiencia de Potencia

El trade-off fundamental se expresa mediante la relacion de Shannon: [source — [[../../explicaciones_anki/conceptos_integradores/carta_56_tradeoff_bw_potencia_shannon]]]

$$\boxed{\frac{E_b}{N_0} = \frac{2^{\eta} - 1}{\eta}, \quad \eta = \frac{R_b}{B}}$$

Esto impone que **alta eficiencia espectral requiere alta $E_b/N_0$** (baja eficiencia de potencia), y viceversa.

| Prioridad | Estrategia | Ejemplo |
|-----------|-----------|---------|
| Maxima $\eta_B$ | QAM alto orden, MIMO | Fibra, cable |
| Maxima $\eta_P$ | Spread spectrum, codigos potentes | Espacio profundo, GPS |
| Balance | Modulacion adaptativa | LTE, 5G, WiFi |

## Criterios de Seleccion en Diseno

1. **Recurso limitante**: espectro (celular) $\to$ priorizar $\eta_B$; potencia (satelite) $\to$ priorizar $\eta_P$
2. **Condiciones del canal**: multitrayecto $\to$ OFDM; ruido continuo $\to$ DSSS; jamming parcial $\to$ FHSS
3. **Requisitos de la aplicacion**: latencia, tasa de datos, movilidad, costo
4. **Regulacion**: limites de emision, bandas asignadas, estandares obligatorios

## Errores Comunes

- Buscar un "mejor" esquema universal: no existe; depende de las restricciones
- Comparar sistemas en regimenes diferentes sin normalizar
- Ignorar que Shannon impone limites fisicos que la tecnologia no puede superar

## Ver tambien

- [[../ruido/intercomparacion-sistemas]]
- [[../modulacion-analogica/am-vs-dsb-sc]]
- [[../modulacion-digital/comparacion-digital-analogica]]
- [[../teoria-informacion/teorema-shannon-hartley]]
- [[../conceptos-integradores/seleccion-modulacion]]
- [[../conceptos-integradores/compromisos-diseno]]
