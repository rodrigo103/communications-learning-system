---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_03/carta_14_modulador_balanceado.md
curso: Sistemas de Comunicaciones
unidad: 3
---

# Multiplexacion por Division de Frecuencia (FDM)

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Definicion

FDM (Frequency Division Multiplexing) permite que **multiples señales compartan simultaneamente el mismo medio fisico** modulando cada una a una frecuencia portadora diferente, con bandas de guarda entre ellas [source].

## Principio de Operacion

Cada señal moduladora $m_i(t)$ se modula a una portadora $f_{ci}$ distinta:

$$s_{FDM}(t) = \sum_{i=1}^{N} s_i(t) = \sum_{i=1}^{N} m_i(t) \cdot \cos(2\pi f_{ci} t)$$

Espectro resultante:

```
|--Canal 1--|  guarda  |--Canal 2--|  guarda  |--Canal 3--|
f_{c1}               f_{c2}                  f_{c3}
```

## Parametros de Diseño

| Parametro | Definicion | Valor tipico |
|-----------|------------|--------------|
| Ancho de banda por canal | $BW_{canal}$ | Depende de modulacion |
| Banda de guarda | Separacion entre canales | 10-25% del BW |
| Espaciado entre portadoras | $\Delta f_c = BW_{canal} + BW_{guarda}$ | |
| Ancho de banda total | $BW_{total} = N \cdot \Delta f_c$ | |

## Sistema Telefonico FDM Clasico

Ejemplo: 12 canales de voz SSB (grupo basico) [source]:

- Cada canal de voz: 300-3400 Hz, BW = 4 kHz
- Modulacion: SSB (banda lateral inferior) con moduladores balanceados
- Portadoras: 64, 68, 72, ..., 108 kHz
- Espaciado: 4 kHz entre portadoras
- Banda de guarda: minima
- BW total del grupo: 60-108 kHz = 48 kHz

El modulador balanceado es fundamental en FDM: suprime la portadora de cada canal, evitando que 12 portadoras consuman potencia y causen batidos entre canales [source].

## Ventajas de FDM

- **Uso eficiente del espectro**: multiples usuarios comparten el medio [source]
- **Transmision simultanea**: todos los canales activos al mismo tiempo
- **Independencia**: cada canal puede usar diferente modulacion y ancho de banda
- **Simplicidad en recepcion**: filtros pasa-banda separan los canales

## Desventajas

- **Interferencia entre canales**: filtros no ideales causan crosstalk
- **Bandas de guarda**: desperdicio de espectro
- **Productos de intermodulacion**: no linealidades del canal generan señales espurias
- **Complejidad**: moduladores y filtros por cada canal

## Comparacion con TDM

| Aspecto | FDM | TDM |
|---------|-----|-----|
| Division | Frecuencia | Tiempo |
| Sincronizacion | Menos critica | Muy critica |
| Apto para | Señales analogicas | Señales digitales |
| Vulnerabilidad | Interferencia frecuencial | Jitter temporal |

Ver [[modulacion-pulsos/multiplex-tdm]] para TDM.

## Aplicaciones

- **Telefonia analogica**: sistemas de larga distancia historicos (Bell L1, L3, L5)
- **Radio FM estereo**: L+R en banda base, L-R en subportadora 38 kHz (ver [[modulacion-analogica/fm-estereo]])
- **Cable TV**: multiples canales en diferentes frecuencias
- **DSL**: DMT (Discrete Multi-Tone) = FDM digital
- **OFDM**: version digital moderna de FDM (ver [[espectro-expandido/ofdm]])

## Puntos Clave

- ✓ FDM comparte el medio modulando a diferentes portadoras [source]
- ✓ Bandas de guarda necesarias para evitar interferencia [source]
- ✓ Moduladores balanceados suprimen portadoras y evitan batidos [analysis]
- ✓ OFDM es la evolucion digital de FDM

## Ver tambien

- [[introduccion/necesidad-modulacion]]
- [[introduccion/espectro-electromagnetico]]
- [[modulacion-pulsos/multiplex-tdm]]
- [[modulacion-analogica/fm-estereo]]
- [[espectro-expandido/ofdm]]
