# Carta 43: Efecto del Énfasis en la Comparación FM vs AM

> **Unidad 8**: Intercomparación de Sistemas

---

## 🎯 Pregunta

¿Cómo afecta la pre-énfasis/de-énfasis a la comparación FM vs. AM?

---

## 📝 Respuesta Breve (de la carta original)

La **red de énfasis** mejora significativamente el desempeño de FM:

**Sin énfasis**:
- FM ya supera a AM en SNR (especialmente para β grande)
- Ventaja FM: proporcional a $\beta^2$

**Con énfasis**:
- **Mejora adicional**: 10-13 dB en componentes de alta frecuencia
- Compensa el énfasis del ruido en altas frecuencias en FM
- SNR efectivo mucho mayor que AM

**Comparación final**:
- **AM**: SNR salida ≈ SNR entrada (sin ganancia)
- **FM sin énfasis**: SNR salida = 3β²(SNR entrada) para tono único
- **FM con énfasis**: mejora adicional significativa

**Conclusión**: FM con énfasis es claramente superior a AM en ambiente ruidoso, justificando el mayor BW.

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El preénfasis y deénfasis representan una técnica ingeniosa que explota las características espectrales del ruido en FM para mejorar dramáticamente la calidad de audio, especialmente en radiodifusión FM comercial. Esta técnica, implementada universalmente en radio FM desde los 1940s, es la razón principal por la cual la radio FM suena tan superior a la AM, más allá de la ventaja inherente de la modulación de frecuencia.

**¿Por qué es importante?** Cada vez que escuchas radio FM en tu automóvil, el sistema de énfasis está trabajando silenciosamente para darte audio de alta fidelidad. Sin él, las frecuencias altas (platillos, consonantes en voz) serían ruidosas e inteligibles. La técnica es tan efectiva que se adoptó también en grabación de vinilo (curva RIAA), cassettes (Dolby), y broadcasting de TV analógica.

**Aplicaciones del mundo real:** La técnica se usa en FM broadcast (88-108 MHz), audio de TV analógica, comunicaciones satelitales de audio, y fue fundamental en sistemas de grabación analógica. Aunque los sistemas digitales no necesitan énfasis, el principio de "ecualización adaptada al ruido" persiste en técnicas modernas de procesamiento de señal.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Modulación FM y su espectro de ruido (Carta 16-17)
- Características del ruido en demodulación FM
- Respuesta en frecuencia y filtrado
- Concepto de densidad espectral de potencia del ruido

#### Desarrollo Paso a Paso

**Paso 1: El Problema del Ruido en FM**

En un demodulador FM, el ruido de salida tiene una característica peculiar:

$$S_{n,out}(f) = \left(\frac{2N_0 f^2}{A^2}\right) \quad \text{para } |f| < f_m$$

El ruido aumenta cuadráticamente con la frecuencia. Esto significa:
- Bajas frecuencias: poco ruido
- Altas frecuencias: mucho ruido
- Problema crítico para audio de alta fidelidad

**Paso 2: La Solución del Preénfasis**

En el transmisor, antes de modular:
1. Se pasa el audio por un filtro que amplifica altas frecuencias
2. Respuesta típica: $H_{pre}(f) = 1 + j(f/f_1)$
3. Constante de tiempo: τ = 75 μs (USA/Japón) o 50 μs (Europa)
4. Frecuencia de corte: $f_1 = 1/(2πτ) ≈ 2.12$ kHz

**Paso 3: El Deénfasis Complementario**

En el receptor, después de demodular:
1. Se aplica filtro inverso: $H_{de}(f) = 1/(1 + j(f/f_1))$
2. Restaura el balance espectral original del audio
3. Atenúa el ruido de alta frecuencia que fue amplificado

#### Derivación Matemática

**Análisis de la mejora en SNR:**

Para una señal de audio con densidad espectral plana, el SNR sin énfasis es:

$$SNR_{FM} = \frac{3A^2 f_m}{4N_0 f_m^3} \cdot P_{señal} = \frac{3\beta^2 \gamma}{2}$$

donde γ = SNR del canal.

**Con preénfasis/deénfasis:**

La mejora en SNR debido al énfasis es:

$$\text{Mejora} = \frac{(f_m/f_1)^2}{3[\arctan(f_m/f_1) - f_1/f_m + (f_1/f_m)^3/3]}$$

Para valores típicos (fm = 15 kHz, f1 = 2.12 kHz):

$$\text{Mejora} \approx 4.7 \text{ (lineal)} = 6.7 \text{ dB}$$

**Considerando el espectro real del audio** (no plano), la mejora típica es:

$$\boxed{\text{Mejora total} \approx 10-13 \text{ dB}}$$

**Significado físico:**
- Las componentes de alta frecuencia del audio se transmiten con mayor desviación
- El ruido de alta frecuencia se atenúa en el receptor
- El resultado neto es una mejora sustancial en SNR perceptual

### 🔬 Intuición y Analogías

**Analogía principal:**
El preénfasis/deénfasis es como hablar más fuerte en frecuencias donde hay más ruido de fondo, y luego el oyente ajusta mentalmente el volumen. Imagina una conversación en un restaurante ruidoso: naturalmente enfatizas las consonantes (altas frecuencias) para ser entendido, y el oyente "normaliza" tu voz mentalmente.

**Intuición física:**
Piensa en el ruido FM como agua que se acumula más en las partes altas de un terreno inclinado (altas frecuencias). El preénfasis es como construir el terreno más alto aún en esas zonas, pero con canales de drenaje (deénfasis) que eliminan el agua extra al final, dejando el terreno nivelado pero seco.

**Visualización espectral:**
```
Frecuencia →
Sin énfasis:  [Señal: ————————] [Ruido: ↗↗↗↗]
Preénfasis:    [Señal: ————↗↗↗↗] [Ruido: ↗↗↗↗]
Post-deénfasis:[Señal: ————————] [Ruido: ————]
```

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Radio FM Comercial

**Situación:** Emisora FM transmitiendo música

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Desviación máxima (Δf) | 75 | kHz |
| Ancho de banda de audio | 15 | kHz |
| Constante de tiempo | 75 | μs |
| SNR del canal | 20 | dB |

**Análisis paso a paso:**

1. **Índice de modulación:**
   $$\beta = \frac{75 \text{ kHz}}{15 \text{ kHz}} = 5$$

2. **SNR sin énfasis (aproximado para audio):**
   $$SNR_{FM} = 3\beta^2 \gamma = 3 \times 25 \times 100 = 7500 = 38.8 \text{ dB}$$

3. **Mejora por énfasis:**
   $$\text{Mejora} \approx 12 \text{ dB}$$

4. **SNR final con énfasis:**
   $$SNR_{total} = 38.8 + 12 = 50.8 \text{ dB}$$

**Comparación con AM:**
- AM daría: SNR ≈ 20 dB (igual al canal)
- FM con énfasis: 50.8 dB
- **Ventaja FM: 30.8 dB** (factor de 1200)

---

#### Ejemplo 2: Comparación Detallada FM vs AM para Voz

**Contexto:** Transmisión de voz con ancho de banda limitado

**Sistema AM (DSB-FC):**
- BW = 6 kHz (±3 kHz)
- SNR salida ≈ SNR entrada = 15 dB (ambiente ruidoso)
- Calidad: marginal, ruido de fondo audible

**Sistema FM sin énfasis:**
- Δf = 15 kHz, fm = 3 kHz → β = 5
- BW = 2(15+3) = 36 kHz (Carson)
- SNR = 3 × 25 × 31.6 = 2370 = 33.7 dB
- Mejora sobre AM: 18.7 dB

**Sistema FM con énfasis:**
- Mismos parámetros
- Mejora adicional: ~10 dB (para voz)
- SNR total: 43.7 dB
- Mejora sobre AM: 28.7 dB

**Conclusión:** FM con énfasis ofrece calidad broadcast usando 6× más ancho de banda.

---

#### Ejemplo 3: Efecto en Diferentes Tipos de Audio

**¿Cómo varía la mejora según el contenido?**

| Tipo de Audio | Característica Espectral | Mejora por Énfasis |
|--------------|-------------------------|-------------------|
| Voz masculina | Energía en bajas freq. | 8-10 dB |
| Voz femenina | Más energía en altas | 10-12 dB |
| Música clásica | Espectro balanceado | 11-13 dB |
| Música rock | Rica en altas freq. | 12-14 dB |
| Podcast/narración | Principalmente medias | 9-11 dB |

**Observación:** La mejora es mayor cuando hay más contenido de alta frecuencia, justo donde más se necesita.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados
- **Modulación FM** (Cartas 16-21): Base para entender el problema del ruido
- **Ruido de banda angosta** (Carta 37): Naturaleza del ruido en FM
- **Efecto umbral FM** (Carta 39): Límite donde el énfasis deja de ayudar
- **Companding** (Carta 24): Otra técnica de procesamiento no lineal

#### Dependencias
1. Demodulación FM → Entender cómo surge el ruido triangular
2. Filtrado → Comprender respuesta en frecuencia
3. SNR y su medición → Para cuantificar mejoras

#### Aplicaciones Posteriores
1. **Dolby NR**: Extensión del concepto a grabación magnética
2. **Ecualización adaptativa**: En comunicaciones digitales modernas
3. **Perceptual coding**: MP3, AAC usan principios similares

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- El ruido en FM no es plano, aumenta con f²
- Preénfasis/deénfasis es un sistema complementario (no altera la señal final)
- La mejora es adicional a la ventaja inherente de FM
- Esto justifica técnicamente por qué FM broadcast usa 200 kHz por canal

#### Tipos de problemas típicos
1. **Cálculo de mejora total**: FM con y sin énfasis vs AM
   - Estrategia: Calcular SNR base de FM, añadir mejora por énfasis

2. **Diseño de red de énfasis**: Dada τ, determinar respuesta
   - Estrategia: Usar funciones de transferencia estándar

3. **Comparación de sistemas**: Justificar elección FM vs AM
   - Estrategia: Considerar SNR, BW, complejidad, aplicación

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Pensar que el énfasis distorsiona permanentemente el audio**
- Por qué ocurre: No entender la naturaleza complementaria
- Cómo evitarlo: Recordar que preénfasis × deénfasis = 1
- Clave: El audio final es idéntico al original

❌ **Error #2: Aplicar la mejora de 13 dB a todos los casos**
- Por qué ocurre: Memorización sin contexto
- Cómo evitarlo: La mejora depende del contenido espectral
- Realidad: 10-13 dB es un rango, no un valor fijo

❌ **Error #3: Ignorar que AM también podría usar énfasis**
- Por qué ocurre: Asociación exclusiva con FM
- Cómo evitarlo: AM podría usarlo, pero la mejora sería menor
- Diferencia: En FM funciona mejor porque el ruido tiene característica f²

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Constante de tiempo: τ = 75 μs (USA) o 50 μs (Europa)
Frecuencia de corte: f₁ = 1/(2πτ) ≈ 2.12 kHz
Mejora típica: 10-13 dB
SNR_FM_total = 3β²γ + Mejora_énfasis (dB)
```

#### Conceptos Fundamentales
- ✓ **Ruido triangular**: En FM, el ruido aumenta con f²
- ✓ **Sistema complementario**: Pre×De = 1 (no hay distorsión neta)
- ✓ **Mejora perceptual**: Mayor donde más importa (altas frecuencias)
- ✓ **Justificación del BW**: FM+énfasis justifica 200 kHz/canal

#### Comparación Final

| Sistema | SNR (para γ=20dB, audio) | BW Requerido | Complejidad |
|---------|--------------------------|--------------|-------------|
| AM | 20 dB | 30 kHz | Baja |
| FM sin énfasis | 39 dB | 180 kHz | Media |
| FM con énfasis | 51 dB | 180 kHz | Media |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**: Carlson Cap. 8 (FM noise and emphasis)
- **Standards**: ITU-R BS.450 (Pre-emphasis characteristics)
- **Historia**: "FM Broadcasting" - Major Armstrong papers

#### Temas Relacionados para Explorar
1. Curva RIAA en discos de vinilo (mismo principio)
2. Dolby noise reduction systems
3. Companding en FM (compresión/expansión adicional)

#### Preguntas para Reflexionar
- ¿Por qué USA eligió 75 μs y Europa 50 μs?
- ¿Podría aplicarse énfasis múltiple (cascada)?
- ¿Cómo afecta el énfasis a la potencia transmitida?
- En la era digital, ¿sigue siendo relevante este concepto?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 30 minutos
**Prerequisitos críticos**: Modulación FM, características del ruido, filtrado
**Tags**: `#FM` `#preenfasis` `#deenfasis` `#comparacion-sistemas` `#mejora-SNR`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*