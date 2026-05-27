---
tags:
  - wiki/modulacion-digital
source_file: explicaciones_anki/unidad_06/carta_32_deteccion_coherente_no_coherente.md
curso: Sistemas de Comunicaciones
unidad: 6
---

# Codificación de Línea y Detección

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_06/carta_32_deteccion_coherente_no_coherente]]]

## Detección Coherente vs. No Coherente

La elección del tipo de detección representa un trade-off fundamental entre complejidad del receptor y eficiencia de potencia. [source — [[../../explicaciones_anki/unidad_06/carta_32_deteccion_coherente_no_coherente]]]

### Detección Coherente

Requiere una réplica exacta de la portadora transmitida (fase sincronizada):

$$y = \int_0^T r(t)\cos(2\pi f_c t) \, dt$$

**Ventaja**: mejor desempeño (menor BER para mismo SNR)
**Desventaja**: requiere circuito de recuperación de portadora (PLL)
**Usado en**: [[../modulacion-digital/ask-fsk-psk|PSK]], [[../modulacion-digital/modulacion-qam|QAM]]

### Detección No Coherente

No requiere sincronización de fase. Usa detección de envolvente o discriminador:

$$y = |r(t)| \quad \text{(envolvente)}$$

**Ventaja**: implementación más simple, menor consumo
**Desventaja**: penalidad de ~3 dB en SNR
**Usado en**: FSK, ASK/OOK, DPSK

## Penalidad en Desempeño

| Modulación | BER coherente | BER no coherente | Penalidad @ $10^{-6}$ |
|------------|---------------|-------------------|------------------------|
| BPSK/DPSK | $Q(\sqrt{2E_b/N_0})$ | $\frac{1}{2}e^{-E_b/N_0}$ | 0.8 dB |
| FSK | $Q(\sqrt{E_b/N_0})$ | $\frac{1}{2}e^{-E_b/2N_0}$ | 0.7 dB |

## Principios de Codificación de Línea

La codificación de línea adapta los bits para transmisión en banda base, proporcionando: [analysis]

- **Sincronización de reloj**: transiciones suficientes para recuperar el clock
- **Supresión de DC**: evitar componentes de corriente continua
- **Densidad espectral controlada**: ajustar el espectro al canal

### Códigos Principales

| Código | Transiciones | Componente DC | Ancho de banda |
|--------|-------------|---------------|----------------|
| NRZ-L | Pocas | Alta | $R_b/2$ |
| RZ | Garantizadas | Alta | $R_b$ |
| Manchester | Cada bit | Nula | $R_b$ |
| AMI | Suficientes | Nula | $R_b/2$ |
| HDB3 | Garantizadas | Nula | $R_b/2$ |

**Manchester** (usado en Ethernet 10 Mbps): cada bit tiene transición en el centro — "1" = alto→bajo, "0" = bajo→alto. Excelente sincronización pero duplica el ancho de banda.

**HDB3** (usado en E1): sustituye secuencias de 4 ceros con patrones de violación para garantizar transiciones. [source — [[../../explicaciones_anki/unidad_06/carta_32_deteccion_coherente_no_coherente]]]

## Ver también

- [[../modulacion-digital/ask-fsk-psk]] — Modulaciones que requieren detección coherente/no coherente
- [[../modulacion-pulsos/pcm-cuantificacion]] — Origen de los bits que se codifican en línea
- [[../modulacion-digital/probabilidad-error]] — BER como métrica afectada por el tipo de detección
