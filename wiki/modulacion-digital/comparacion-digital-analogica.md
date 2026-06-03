---
tags:
  - wiki/modulacion-digital
source_file: explicaciones_anki/unidad_06/carta_30_velocidad_tasa_bits.md
curso: Sistemas de Comunicaciones
unidad: 6
---

# Comparación Digital vs. Analógica

> **Last verified:** 2025-11-16 | **Verified by:** [analysis]

## Ventajas de la Modulación Digital

### Inmunidad al Ruido

Los sistemas digitales pueden **regenerar** la señal en repetidores intermedios, eliminando la acumulación de ruido. Un sistema analógico acumula ruido en cada etapa; un sistema digital con regeneración mantiene la SNR constante. [source — [[../../explicaciones_anki/unidad_06/carta_30_velocidad_tasa_bits]]]

### Corrección de Errores

La codificación de canal (FEC) permite detectar y corregir errores, algo imposible en sistemas analógicos puros. Ver [[../ruido/relacion-snr|SNR y calidad]].

### Procesamiento Digital

- Compresión de datos sin pérdida de calidad
- Encriptación para seguridad
- Multiplexación estadística eficiente
- Almacenamiento y procesamiento flexibles

### Flexibilidad

La modulación adaptativa permite ajustar el esquema de modulación según las condiciones del canal, maximizando throughput. [analysis]

## Desventajas de la Modulación Digital

### Mayor Ancho de Banda

La digitalización expande el ancho de banda. Para telefonía PCM:

$$\frac{BW_{PCM}}{BW_{anal\acute{o}gico}} \geq n$$

donde $n$ es el número de bits por muestra. [[../modulacion-pulsos/pcm-cuantificacion|PCM]] intercambia BW por inmunidad al ruido. [source — [[../../explicaciones_anki/unidad_06/carta_30_velocidad_tasa_bits]]]

### Mayor Complejidad

- Requiere conversión A/D y D/A
- Sincronización de símbolo, trama y portadora
- Procesamiento digital de señal (DSP)
- Circuitos más complejos y costosos

### Latencia

El procesamiento digital introduce retardo por buffering, codificación, y entrelazado. Crítico en aplicaciones de tiempo real.

## Cuantificación: Ventaja Digital Clave

La tasa de bits $R_b$ se relaciona con la velocidad de símbolo $R_s$:

$$\boxed{R_b = R_s \cdot \log_2(M)}$$

donde $M$ es el número de símbolos. Solo en modulaciones binarias ($M = 2$) coinciden baudios y bits/s. [source — [[../../explicaciones_anki/unidad_06/carta_30_velocidad_tasa_bits]]]

En modulaciones multinivel como [[../modulacion-digital/modulacion-qam|QAM]], cada símbolo transporta múltiples bits, aumentando la eficiencia espectral.

## Tabla Comparativa

| Aspecto | Analógico | Digital |
|---------|-----------|---------|
| Ruido acumulado | Sí | No (regeneración) |
| Corrección errores | No | Sí (FEC) |
| Ancho de banda | Menor | Mayor (expansión) |
| Complejidad | Baja | Media-Alta |
| Flexibilidad | Limitada | Alta (adaptativa) |
| Seguridad | Baja | Alta (encriptación) |
| Degradación | Gradual | Umbral (más abrupta) |

## Ver también

- [[../modulacion-digital/ask-fsk-psk]] — Modulaciones digitales básicas
- [[../modulacion-analogica/am-vs-dsb-sc]] — Modulaciones analógicas de referencia
- [[../ruido/intercomparacion-sistemas]] — Comparación sistemática de todos los esquemas
- [[../conceptos-integradores/comparacion-global-modulaciones]] — Visión integradora
- [[../../explicaciones_anki/conceptos_integradores/carta_59_regeneracion_digital_vs_amplificacion_analogica|Regeneracion digital]] — Amplificacion analogica vs regeneracion
- [[../../claude-conversations/2025-11-16_digital-modulation-history-and-bandpass-concepts|Conversación: historia mod. digital y conceptos bandpass]]
