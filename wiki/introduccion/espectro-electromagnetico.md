---
tags:
  - wiki/introduccion
source_file: explicaciones_anki/unidad_01/carta_03_espectro_electromagnetico.md
curso: Sistemas de Comunicaciones
unidad: 1
---

# Espectro Electromagnetico

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_01/carta_03_espectro_electromagnetico]]]

## Definicion

El espectro electromagnetico es el rango completo de todas las frecuencias de ondas electromagneticas, gobernado por la ecuacion fundamental [source — [[../../explicaciones_anki/unidad_01/carta_03_espectro_electromagnetico]]]:

$$\boxed{c = \lambda \cdot f}$$

donde $c = 3 \times 10^8$ m/s, $\lambda$ = longitud de onda, $f$ = frecuencia.

## El Espectro como Recurso Limitado

El espectro electromagnetico es un **recurso natural limitado y no renovable** [source — [[../../explicaciones_anki/unidad_01/carta_03_espectro_electromagnetico]]]. A diferencia de recursos fisicos, no se "gasta" pero si puede "congestionarse" y degradarse por uso inadecuado. La capacidad esta limitada por el teorema de Shannon-Hartley:

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

**Limitaciones fisicas** [source — [[../../explicaciones_anki/unidad_01/carta_03_espectro_electromagnetico]]]:
- **Propagacion**: no todas las frecuencias se propagan igual. VLF-LF excelente propagacion pero baja capacidad; SHF-EHF alta capacidad pero alcance limitado
- **Tecnologia**: generacion y deteccion limitadas; costo aumenta con la frecuencia
- **Capacidad teorica**: $C = B \log_2(1 + S/N)$ — espectro limitado $\to$ capacidad limitada

> **¿Por que a mayor frecuencia hay mas capacidad, y por que el alcance se reduce?** $C=B\log_2(1+S/N)$ no tiene a la frecuencia portadora en ningun lado — la ventaja de las bandas altas no es "mas capacidad por Hz", es que hay disponible mucho mas **$B$ absoluto**, y $C$ crece aprox. linealmente con $B$ (mientras que con $S/N$ crece solo logaritmicamente). [analysis]
> - *Por que hay mas B a alta frecuencia*: limitacion practica de ancho de banda **fraccional** (osciladores, filtros y antenas reales manejan solo ~1-5% de $f_c$). Con el mismo porcentaje, a $f_c$ mas alta el $B$ absoluto es proporcionalmente mayor (AM: $f_c\approx1$MHz, $B\approx10$kHz, ~1%; 5G mmWave: $f_c\approx28$GHz, $B$ hasta 800MHz, ~2-3% — el $B$ absoluto es ~4 ordenes de magnitud mayor).
> - *Por que el alcance cae a alta frecuencia* — varios mecanismos independientes, todos empeoran con $f$:
>   1. Perdida de espacio libre con ganancia de antena fija: $L_{fs}(\text{dB}) = 20\log d + 20\log f + 32{,}44$ (Friis, ver [[../ruido/formula-friis]]) — crece con $f^2$ porque la apertura efectiva $A_e=\lambda^2G/4\pi$ se achica con la longitud de onda.
>   2. Absorcion atmosferica molecular (picos de O2 ~60GHz, vapor de agua ~22GHz y ~183GHz) — inexistente en VLF-HF.
>   3. Dispersion por lluvia/niebla, relevante quando $\lambda$ se acerca al tamaño de las gotas (mm, en EHF).
>   4. Se pierden los mecanismos de largo alcance de baja frecuencia: onda de superficie (sigue la curvatura terrestre) y onda de cielo (rebote ionosferico, miles de km) — desde VHF las ondas atraviesan la ionosfera en vez de rebotar, quedando limitadas a linea de vista.
> - *¿La SNR es constante con la frecuencia? No.* $N_0=kT$ (densidad de ruido termico) si es aprox. constante con $f$, pero $S$ llega mas debil (los 4 mecanismos de arriba) y $N=kTB$ es mayor porque los sistemas de alta frecuencia usan mas $B$ — el mismo $B$ que da la capacidad extra tambien mete mas ruido. La SNR por Hz tiende a empeorar con la frecuencia, no a mantenerse constante.
> - *No es una ley fisica inapelable, es un trade-off de antena*: con **apertura fija** en vez de ganancia fija, el termino $f^2$ de perdida se cancela con el $f^2$ de ganancia que da esa apertura a mayor frecuencia ($P_r \propto A_tA_r/(\lambda^2d^2) \propto f^2$ a apertura constante). Por eso radares y enlaces satelitales en banda Ku/Ka logran gran alcance en frecuencias altas: usan antenas grandes y muy directivas (o arrays de beamforming en 5G mmWave), no antenas isotropicas.

## Competencia por el Espectro

Principales categorias de usuarios [source — [[../../explicaciones_anki/unidad_01/carta_03_espectro_electromagnetico]]]:
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

La Conferencia Mundial de Radiocomunicaciones (WRC), cada 3-4 años, actualiza el tratado internacional de asignacion de bandas [source — [[../../explicaciones_anki/unidad_01/carta_03_espectro_electromagnetico]]].

### Metodos de Asignacion

- **Command and Control**: regulador asigna directamente (broadcasting, servicios publicos)
- **Subastas**: asigna a quien paga mas. Ej: subasta 5G en USA (2021): $81 mil millones
- **Commons**: acceso compartido. Bandas ISM (2.4 GHz, 5 GHz) para WiFi/Bluetooth

## Consecuencias del Mal Uso

- **Interferencia co-canal**: $SINR = S/(I + N)$ donde $I$ = interferencia [source — [[../../explicaciones_anki/unidad_01/carta_03_espectro_electromagnetico]]]
- **Interferencia de canal adyacente**: filtros imperfectos
- **Congestion**: degradacion en bandas saturadas
- **Ineficiencia economica**: espectro subutilizado ("spectrum holes")

## Estrategias de Uso Eficiente

- **Modulaciones eficientes**: QAM de alto orden (64-QAM, 256-QAM) [source — [[../../explicaciones_anki/unidad_01/carta_03_espectro_electromagnetico]]]
- **Acceso multiple**: FDMA, TDMA, CDMA, OFDMA (ver [[../espectro-expandido/cdma]] y [[../espectro-expandido/ofdm]])
- **Reutilizacion espacial**: celdas en redes celulares, MIMO masivo
- **Gestion dinamica**: radio cognitivo, carrier aggregation
- **Compresion**: codificacion de fuente (MP3, H.264, HEVC)

## Regla de Oro

> "El espectro es como el aire: parece infinito hasta que todos intentan usarlo simultaneamente" [analysis]

## Ver tambien

- [[../introduccion/modelo-shannon]]
- [[../introduccion/necesidad-modulacion]]
- [[../ruido/fuentes-ruido]]
- [[../espectro-expandido/cdma]]
- [[../espectro-expandido/ofdm]]
