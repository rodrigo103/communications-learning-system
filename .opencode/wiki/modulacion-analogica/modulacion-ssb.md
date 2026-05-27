---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_03/carta_11_ssb-blu.md
curso: Sistemas de Comunicaciones
unidad: 3
---

# Modulacion SSB (Banda Lateral Unica / BLU)

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Definicion

SSB (Single Sideband) transmite **solo una banda lateral** (superior o inferior), eliminando la portadora y la banda lateral redundante de DSB [source]. Es la modulacion analogica lineal mas eficiente espectralmente.

## Caracteristicas Fundamentales

$$\boxed{BW_{SSB} = f_m}$$

- **Mitad del ancho de banda** que AM o DSB-SC [source]
- Eficiencia de potencia: **100%** (toda la potencia transmite informacion) [source]
- Eficiencia espectral: **maxima** para modulacion analogica [analysis]

## Generacion: Metodo de Fase (Weaver)

Usando la Transformada de Hilbert $\hat{m}(t)$ de la señal moduladora [source]:

$$\boxed{s_{SSB}(t) = m(t)\cos(2\pi f_c t) \mp \hat{m}(t)\sin(2\pi f_c t)}$$

donde:
- Signo $(-)$: **USB** (Upper Sideband, banda lateral superior)
- Signo $(+)$: **LSB** (Lower Sideband, banda lateral inferior)

## Metodos de Generacion

| Metodo | Principio | Ventaja | Desventaja |
|--------|-----------|---------|------------|
| **Filtro** | Generar DSB-SC, filtrar una banda | Simple conceptualmente | Filtros muy selectivos |
| **Fase (Weaver)** | Transformada de Hilbert | No requiere filtros criticos | Requiere desfasadores precisos |
| **Tercera** | Dos modulaciones sucesivas | Balancea complejidad | Mas etapas |

## Espectro

Para USB, el espectro contiene solo frecuencias $> f_c$:

$$S_{USB}(f) = \begin{cases} M(f-f_c) & f > f_c \\ 0 & f < f_c \end{cases}$$

No hay simetria hermitiana como en señales reales normales — el espectro es **asimétrico** alrededor de $f_c$.

## Ventajas

1. **Ancho de banda minimo**: $BW = f_m$, la mitad que DSB [source]
2. **Eficiencia de potencia**: similar a DSB-SC, toda potencia en informacion [source]
3. **Menor susceptibilidad al desvanecimiento selectivo** [analysis]
4. **Maximo aprovechamiento del espectro** en bandas congestionadas (HF)

## Desventajas

- **Mayor complejidad** en generacion y deteccion
- Requiere **sincronismo de frecuencia muy preciso** (errores causan distorsion audible)
- **No puede transmitir DC**: las bajas frecuencias requieren filtros impracticos [source]

## Ejemplo: Sistema Multicanal Telefonico

12 canales de voz de 4 kHz cada uno:

| Esquema | BW por canal | BW total | Canales en 100 kHz |
|---------|-------------|----------|-------------------|
| DSB-SC | 8 kHz | 96 kHz | 12 |
| SSB | 4 kHz | 48 kHz | 25 |

SSB permite **duplicar** la cantidad de canales en el mismo espectro.

## SNR en SSB

A pesar de usar la mitad del ancho de banda, SSB mantiene el mismo SNR que DSB-SC con deteccion coherente [source]:
- Menos ancho de banda = menos ruido admitido
- Mayor densidad espectral de señal
- Los efectos se **compensan exactamente**

## Aplicaciones

- Radioaficionados (bandas HF: 3-30 MHz)
- Comunicaciones maritimas y aeronauticas de largo alcance
- Sistemas telefonicos multiplexados (FDM)
- Comunicaciones militares HF

## Puntos Clave

- ✓ $BW_{SSB} = f_m$: mitad del ancho de banda de DSB [source]
- ✓ Se elimina redundancia espectral sin perdida de informacion [source]
- ✓ Deteccion coherente absolutamente necesaria [source]
- ✓ Estabilidad de frecuencia critica: $< \pm 50$ Hz para voz

## Ver tambien

- [[modulacion-analogica/am-vs-dsb-sc]]
- [[herramientas-matematicas/transformada-hilbert]]
- [[modulacion-analogica/modulacion-vsb]]
- [[modulacion-analogica/receptor-superheterodino]]
