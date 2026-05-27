---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia.md
curso: Sistemas de Comunicaciones
unidad: 4
---

# Moduladores y Demoduladores FM

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]

## Moduladores FM

### 1. VCO (Oscilador Controlado por Voltaje)

El metodo mas directo: la señal moduladora controla la frecuencia de un oscilador [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]].

```
m(t) → VCO → s_FM(t)
```

- Frecuencia instantanea: $f_i(t) = f_c + k_f m(t)$
- Ventaja: simplicidad, desviacion amplia posible
- Desventaja: requiere linealizacion del VCO, estabilidad de frecuencia central

### 2. Metodo de Armstrong (Indirecto)

Genera NBFM y luego multiplica frecuencia para obtener WBFM [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]:

```
m(t) → Integrador → Modulador PM (NBFM) → Multiplicador ×N → WBFM
```

- Primero genera PM (que es FM de la integral de $m(t)$)
- Multiplicacion de frecuencia aumenta la desviacion: $\Delta f_{out} = N \cdot \Delta f_{in}$
- Ventaja: excelente estabilidad de frecuencia (usa oscilador de cristal)
- Desventaja: requiere multiples etapas de multiplicacion

### 3. Modulador con PLL

Usa un PLL para linealizar el VCO [analysis]:

```
m(t) → VCO → s_FM(t)
         ↑
      Filtro PLL ← Detector de fase ← Referencia
```

El PLL corrige derivas del VCO manteniendo la modulacion.

## Demoduladores FM (Discriminadores)

### Principio General

Convierten variaciones de **frecuencia** en variaciones de **amplitud**, luego detectan la envolvente [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]. La respuesta lineal es:

$$v_{out}(t) = K_d[f_i(t) - f_c] = K_d \cdot k_f \cdot m(t)$$

donde $K_d$ [V/Hz] es la pendiente del discriminador.

### 1. Discriminador Foster-Seeley

Usa un transformador con circuito resonante sintonizado [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]:
- La respuesta en las "faldas" de la curva de resonancia es aproximadamente lineal
- Voltaje de salida proporcional a $\Delta f$
- **Requiere limitador** previo (sensible a variaciones de amplitud)
- THD tipica: 1-2% (con limitador)

### 2. Detector de Relacion (Ratio Detector)

Variante del Foster-Seeley con **auto-limitacion** [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]:
- Usa un capacitor grande para estabilizar amplitud total
- Rechaza automaticamente variaciones de AM
- **No requiere limitador** (ventaja en receptores economicos)
- THD tipica: 0.5-1%

### 3. PLL (Phase-Locked Loop)

El discriminador moderno mas lineal y preciso [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]:

```
s_FM(t) → Detector de fase → Filtro → VCO
              ↑________________________↓
                         
Salida demodulada: voltaje de control del VCO
```

- $V_{control} = \Delta f / K_{VCO}$
- Linealidad excelente: THD $< 0.1\%$
- Superior en ambientes de señal debil
- Ampliamente usado en receptores integrados

## Comparacion de Discriminadores

| Tipo | Limitador | Complejidad | THD tipica | Aplicacion |
|------|-----------|-------------|------------|------------|
| Foster-Seeley | Requerido | Media | 1-2% | Receptores discretos |
| Ratio Detector | Integrado | Media | 0.5-1% | Receptores economicos |
| PLL | No necesario | Alta (IC) | < 0.1% | Receptores modernos |

## Formulas Clave

Salida del discriminador [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]:

$$\boxed{v_{out}(t) = K_d \cdot \Delta f}$$

Constante de demodulacion total:

$$K_{dem} = K_d \cdot k_f$$

donde $k_f$ [Hz/V] es la sensibilidad del modulador original.

## Generacion FM desde PM (y viceversa)

Relacion fundamental [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]:

- **FM desde PM**: integrar $m(t)$ primero, luego aplicar PM
- **PM desde FM**: derivar $m(t)$ primero, luego aplicar FM

Muchos transmisores FM usan moduladores PM con integrador previo (Metodo de Armstrong) [analysis].

## Analogia

El discriminador de frecuencia es como un **tobogan con pendiente**: la señal FM "camina" horizontalmente (variaciones de frecuencia), y su posicion vertical (amplitud de salida) sigue las variaciones. La pendiente del tobogan es $K_d$, la caracteristica de conversion F-A [analysis].

## Puntos Clave

- ✓ Discriminador = conversion Frecuencia → Amplitud [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]
- ✓ VCO: modulador FM mas directo [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]
- ✓ Armstrong: NBFM con PM + multiplicacion de frecuencia [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]
- ✓ PLL: discriminador moderno mas preciso [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]
- ✓ Relacion integral/derivada permite conversion FM ↔ PM [source — [[../../explicaciones_anki/unidad_04/carta_19_discriminador_frecuencia]]]

## Ver tambien

- [[../modulacion-analogica/fm-vs-pm]]
- [[../modulacion-analogica/ancho-banda-carson]]
- [[../modulacion-analogica/receptor-superheterodino]]
- [[../modulacion-analogica/preenfasis-deenfasis]]
