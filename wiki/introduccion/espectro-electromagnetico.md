---
tags:
  - wiki/introduccion
source_file: explicaciones_anki/unidad_01/carta_03_espectro_electromagnetico.md
curso: Sistemas de Comunicaciones
unidad: 1
---

# Espectro Electromagnetico

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Definicion

El espectro electromagnetico es el rango completo de todas las frecuencias de ondas electromagneticas, gobernado por la ecuacion fundamental [source]:

$$\boxed{c = \lambda \cdot f}$$

donde $c = 3 \times 10^8$ m/s, $\lambda$ = longitud de onda, $f$ = frecuencia.

## El Espectro como Recurso Limitado

El espectro electromagnetico es un **recurso natural limitado y no renovable** [source]. A diferencia de recursos fisicos, no se "gasta" pero si puede "congestionarse" y degradarse por uso inadecuado. La capacidad esta limitada por el teorema de Shannon-Hartley:

$$C = B \log_2(1 + S/N)$$

Rango util para comunicaciones: aproximadamente 3 kHz - 300 GHz.

## Bandas de Frecuencia y Aplicaciones

| Banda | Frecuencia | Longitud de onda | Aplicaciones |
|-------|-----------|------------------|--------------|
| ELF | 3-30 Hz | 100,000-10,000 km | Comunicacion submarina |
| VLF | 3-30 kHz | 100-10 km | Navegacion |
| LF | 30-300 kHz | 10-1 km | Radiofaros |
| MF | 300-3000 kHz | 1000-100 m | AM broadcast (530-1700 kHz) |
| HF | 3-30 MHz | 100-10 m | Onda corta, radioaficionados |
| VHF | 30-300 MHz | 10-1 m | FM, TV, aviacion |
| UHF | 300-3000 MHz | 100-10 cm | TV digital, celular, WiFi, GPS |
| SHF | 3-30 GHz | 10-1 cm | Satelites, radar, 5G |
| EHF | 30-300 GHz | 10-1 mm | mmWave 5G, radioastronomia |

## Por que es Limitado

**Limitaciones fisicas** [source]:
- **Propagacion**: no todas las frecuencias se propagan igual. VLF-LF excelente propagacion pero baja capacidad; SHF-EHF alta capacidad pero alcance limitado
- **Tecnologia**: generacion y deteccion limitadas; costo aumenta con la frecuencia
- **Capacidad teorica**: $C = B \log_2(1 + S/N)$ — espectro limitado $\to$ capacidad limitada

## Competencia por el Espectro

Principales categorias de usuarios [source]:
1. **Broadcasting**: radio AM/FM, TV
2. **Telecomunicaciones**: telefonia movil, enlaces de microondas, satelites
3. **Gobierno y Defensa**: comunicaciones militares, radar
4. **Servicios de Emergencia**: policia, bomberos
5. **Cientificos**: radioastronomia, meteorologia
6. **Navegacion**: GPS, GLONASS, Galileo
7. **Industrial**: WiFi, Bluetooth (bandas ISM), RFID

## Gestion y Regulacion

### Nivel Internacional - ITU

La UIT-R divide el mundo en 3 regiones:
- **Region 1**: Europa, Africa, Medio Oriente
- **Region 2**: Americas
- **Region 3**: Asia-Pacifico

La Conferencia Mundial de Radiocomunicaciones (WRC), cada 3-4 años, actualiza el tratado internacional de asignacion de bandas [source].

### Metodos de Asignacion

- **Command and Control**: regulador asigna directamente (broadcasting, servicios publicos)
- **Subastas**: asigna a quien paga mas. Ej: subasta 5G en USA (2021): $81 mil millones
- **Commons**: acceso compartido. Bandas ISM (2.4 GHz, 5 GHz) para WiFi/Bluetooth

## Consecuencias del Mal Uso

- **Interferencia co-canal**: $SINR = S/(I + N)$ donde $I$ = interferencia [source]
- **Interferencia de canal adyacente**: filtros imperfectos
- **Congestion**: degradacion en bandas saturadas
- **Ineficiencia economica**: espectro subutilizado ("spectrum holes")

## Estrategias de Uso Eficiente

- **Modulaciones eficientes**: QAM de alto orden (64-QAM, 256-QAM) [source]
- **Acceso multiple**: FDMA, TDMA, CDMA, OFDMA (ver [[espectro-expandido/cdma]] y [[espectro-expandido/ofdm]])
- **Reutilizacion espacial**: celdas en redes celulares, MIMO masivo
- **Gestion dinamica**: radio cognitivo, carrier aggregation
- **Compresion**: codificacion de fuente (MP3, H.264, HEVC)

## Regla de Oro

> "El espectro es como el aire: parece infinito hasta que todos intentan usarlo simultaneamente" [analysis]

## Ver tambien

- [[introduccion/modelo-shannon]]
- [[introduccion/necesidad-modulacion]]
- [[ruido/fuentes-ruido]]
- [[espectro-expandido/cdma]]
- [[espectro-expandido/ofdm]]
