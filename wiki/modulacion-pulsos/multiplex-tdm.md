---
tags:
  - wiki/modulacion-pulsos
source_file: explicaciones_anki/unidad_05/carta_26_tdm-sistemas-pcm.md
curso: Sistemas de Comunicaciones
unidad: 5
---

# Multiplexación por División de Tiempo (TDM)

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Principio de TDM

TDM permite que múltiples señales compartan un mismo canal de transmisión asignando **ranuras temporales** (time slots) exclusivas a cada una. A diferencia de [[modulacion-analogica/multiplex-fdm|FDM]] que divide en frecuencia, TDM divide en tiempo. [source]

### Estructura de Trama

Cada canal se muestrea secuencialmente y sus muestras se agrupan en una **trama**:

$$\text{Trama} = [Sync][Ch_1][Ch_2]\dots[Ch_N][Se\tilde{n}alizaci\acute{o}n]$$

Período de trama para telefonía (voz a 8 kHz):

$$\boxed{T_{frame} = \frac{1}{f_s} = 125 \text{ μs}}$$

## Jerarquías PCM-TDM

### Sistema T1 (Norteamérica)

- 24 canales de voz × 8 bits/muestra × 8000 Hz + 1 bit de sync × 8000 Hz

$$\boxed{R_{T1} = 1.544 \text{ Mbps}}$$

### Sistema E1 (Europa)

- 32 time slots (30 voz + 1 sync + 1 señalización) × 8 bits × 8000 Hz

$$\boxed{R_{E1} = 2.048 \text{ Mbps}}$$

| Parámetro | T1 | E1 |
|-----------|----|----|
| Región | América/Japón | Europa/Mundo |
| Canales de voz | 24 | 30 |
| Companding | μ-law | A-law |
| Codificación línea | AMI, B8ZS | HDB3 |

## Sincronización

La sincronización es **crítica** para TDM. Sin ella, el sistema colapsa. Se requieren tres niveles: [analysis]

1. **Sincronización de bit**: identificar límites de bits
2. **Sincronización de trama**: patrón único (FAW) para detectar inicio
3. **Sincronización de multitrama**: para señalización

La pérdida de sincronismo (Loss of Frame) produce alarma y requiere re-sincronización en 2-10 tramas (250 μs – 1.25 ms).

## Jerarquías Digitales

Los sistemas TDM se escalan en jerarquías:
- **PDH**: E1 → E2 (4×E1) → E3 (4×E2) → E4
- **SDH/SONET**: STM-1 (155 Mbps) → STM-4 → STM-16 → STM-64

## Ver también

- [[modulacion-pulsos/pcm-cuantificacion]] — Digitalización PCM que alimenta los canales TDM
- [[modulacion-analogica/multiplex-fdm]] — Multiplexación en frecuencia como alternativa
- [[introduccion/espectro-electromagnetico]] — El espectro como recurso compartido
