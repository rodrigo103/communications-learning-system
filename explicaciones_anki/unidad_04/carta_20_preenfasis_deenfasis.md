# Carta 20: Preénfasis y Deénfasis en FM

> **Unidad 4**: Modulación Exponencial

---

## 🎯 Pregunta

¿Qué es el preénfasis y deénfasis en FM y por qué se utiliza?

---

## 📝 Respuesta Breve (de la carta original)

**Preénfasis** y **deénfasis** mejoran la relación señal-ruido en FM.

**Preénfasis** (transmisor):
- Filtro que amplifica componentes de alta frecuencia de la moduladora
- Respuesta típica: +6 dB/octava desde $f_1$ ≈ 2.1 kHz

**Deénfasis** (receptor):
- Filtro inverso que atenúa altas frecuencias
- Restaura balance espectral original

**Razón**:
- El ruido en FM afecta más a altas frecuencias
- Preénfasis aumenta SNR de componentes agudos antes de transmisión
- Deénfasis reduce ruido sin afectar señal (ya que están pre-enfatizadas)
- Mejora típica: 10-13 dB en SNR para altas frecuencias

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El **preénfasis y deénfasis** constituyen una técnica ingeniosa de procesamiento de señal que mejora dramáticamente la calidad de audio en sistemas FM. Esta técnica es la razón principal por la cual la radio FM puede ofrecer audio de alta fidelidad con mucho menos ruido de fondo que AM, especialmente en las frecuencias agudas donde nuestro oído es más sensible a los detalles.

**¿Por qué es importante este concepto?** Sin preénfasis/deénfasis, la radio FM comercial tendría un siseo molesto en las frecuencias altas, similar al ruido de cinta en grabaciones analógicas antiguas. Esta técnica permite que disfrutes de música con platillos nítidos, voces claras y detalles sutiles en la transmisión FM. Es una de las innovaciones que hizo a FM superior a AM para transmisión de música de alta calidad.

**¿Dónde se aplica?** El preénfasis/deénfasis se utiliza en toda transmisión FM comercial (88-108 MHz), audio de TV analógica, grabación en cinta magnética, discos de vinilo (curva RIAA), transmisiones satelitales de audio, y comunicaciones de voz profesionales (radios de aviación, servicios de emergencia). Incluso algunos sistemas digitales modernos implementan técnicas similares.

**Historia relevante:** La técnica fue propuesta por Edwin Armstrong junto con FM en 1933, pero fue John R. Carson de Bell Labs quien formalizó el análisis matemático en 1939. La FCC adoptó la curva de 75 μs como estándar para FM broadcast en Estados Unidos en 1941, mientras que Europa adoptó 50 μs, reflejando diferencias en las características del audio y preferencias culturales.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Espectro de ruido en FM**: comprensión de la distribución triangular del ruido
- **Respuesta en frecuencia de filtros**: características de filtros pasa-altos y pasa-bajos
- **Demodulación FM** (Carta 19): el ruido aparece después del discriminador
- **Percepción auditiva humana**: sensibilidad vs. frecuencia

#### Desarrollo Paso a Paso

**Paso 1: El problema del ruido en FM**

Después de la demodulación FM, la densidad espectral de potencia del ruido no es uniforme, sino que aumenta con el cuadrado de la frecuencia:

$$S_n(f) = K \cdot f^2$$

Esto significa que el ruido es mucho más fuerte en frecuencias altas. Para audio de 15 kHz, el ruido a 15 kHz es 225 veces más fuerte que a 1 kHz. Este ruido de alta frecuencia se percibe como un siseo molesto.

**Paso 2: La solución - Preénfasis en el transmisor**

Antes de modular, amplificamos las componentes de alta frecuencia del audio con un filtro de preénfasis. Si el audio original tiene componentes débiles en altas frecuencias (común en voz y música), los amplificamos preventivamente:

$$H_p(f) = 1 + j\frac{f}{f_1}$$

donde $f_1 = \frac{1}{2\pi\tau}$ es la frecuencia de corte, con $\tau$ = constante de tiempo.

**Paso 3: Compensación - Deénfasis en el receptor**

Después de demodular, aplicamos el filtro inverso (deénfasis) que atenúa las altas frecuencias:

$$H_d(f) = \frac{1}{1 + j\frac{f}{f_1}}$$

Este filtro restaura el balance espectral original del audio, pero crucialmente, también atenúa el ruido de alta frecuencia que se sumó durante la transmisión.

#### Derivación Matemática

**Análisis de mejora en SNR:**

Partiendo del espectro de ruido post-demodulación:
$$N_0(f) = \frac{(2\pi f)^2 n_0}{3A_c^2}$$

donde $n_0$ es la densidad de ruido de entrada y $A_c$ es la amplitud de la portadora.

**Con preénfasis/deénfasis:**

La función de transferencia de preénfasis:
$$H_p(f) = \sqrt{1 + \left(\frac{f}{f_1}\right)^2}$$

La función de deénfasis:
$$H_d(f) = \frac{1}{\sqrt{1 + \left(\frac{f}{f_1}\right)^2}}$$

**SNR de salida con preénfasis/deénfasis:**

La mejora en SNR es:
$$\text{Mejora} = 10\log_{10}\left[\frac{3\left(\frac{f_m}{f_1}\right)^2}{\left(\frac{f_m}{f_1}\right) - \arctan\left(\frac{f_m}{f_1}\right)}\right]$$

Para FM broadcast ($f_m = 15$ kHz, $f_1 = 2.1$ kHz):

$$\boxed{\text{Mejora SNR} \approx 13.5 \text{ dB}}$$

**Significado físico de cada término:**
- $f_1$ [Hz]: frecuencia de transición, determina dónde empieza el énfasis
- $f_m$ [Hz]: frecuencia máxima de audio, límite del sistema
- $\tau$ [μs]: constante de tiempo RC del filtro (75 μs en USA, 50 μs en Europa)

### 🔬 Intuición y Analogías

**Analogía principal:**
Imagina que vas a una fiesta ruidosa y necesitas hablar con alguien. Instintivamente elevas más la voz en los tonos agudos (preénfasis) porque sabes que estos se perderán más fácilmente en el ruido ambiente. Tu amigo mentalmente "filtra" (deénfasis) tu voz exagerada para entender el mensaje normal, pero el ruido de fondo queda atenuado en el proceso.

**Intuición física:**
Es como usar gafas de sol con diferente oscuridad según el color. El preénfasis es como hacer más transparente la parte del espectro que se va a contaminar más con ruido (altas frecuencias), y el deénfasis es como poner las gafas oscuras después para ver normal, pero bloqueando el ruido que se coló.

**Visualización:**
Piensa en el espectro de audio como un paisaje montañoso. El preénfasis "levanta" las montañas altas (frecuencias agudas) aún más. Durante la transmisión, la niebla (ruido) se acumula más en las alturas. El deénfasis "aplana" todo de vuelta, pero la niebla también baja, quedando menos visible.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Diseño de red de preénfasis para FM broadcast

**Situación:** Diseñar filtros de preénfasis/deénfasis para una estación FM comercial.

**Datos:**
| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Constante de tiempo (USA) | 75 | μs |
| Frecuencia máxima de audio | 15 | kHz |
| Impedancia del circuito | 600 | Ω |

**Solución paso a paso:**

1. **Frecuencia de corte del filtro:**
   $$f_1 = \frac{1}{2\pi\tau} = \frac{1}{2\pi \times 75 \times 10^{-6}} = 2122 \text{ Hz}$$

2. **Ganancia de preénfasis a 15 kHz:**
   $$|H_p(15\text{kHz})| = \sqrt{1 + \left(\frac{15000}{2122}\right)^2} = \sqrt{1 + 49.9} = 7.14$$

   En dB: $20\log_{10}(7.14) = 17.1$ dB

3. **Componentes del circuito RC:**
   $$R = 600 \text{ Ω}$$
   $$C = \frac{\tau}{R} = \frac{75 \times 10^{-6}}{600} = 125 \text{ nF}$$

4. **Resultado:**
   $$\boxed{\text{Preénfasis: }R = 600\text{ Ω}, C = 125\text{ nF, Ganancia a 15 kHz = 17.1 dB}}$$

**Interpretación:** El circuito amplifica las frecuencias altas hasta 17 dB, preparándolas para sobrevivir al proceso de transmisión con mejor SNR.

---

#### Ejemplo 2: Comparación USA vs Europa

**Contexto:** Análisis comparativo de estándares de preénfasis.

**Parámetros:**
| Región | τ | f₁ | Mejora SNR @ 15kHz |
|--------|---|----|--------------------|
| USA/Japón | 75 μs | 2.12 kHz | 13.5 dB |
| Europa/Australia | 50 μs | 3.18 kHz | 11.3 dB |

**Análisis de compatibilidad:**
Si se recibe una transmisión USA en un receptor europeo:
- Exceso de agudos: $(75-50)/50 = 50\%$ más énfasis en altas frecuencias
- Sonido brillante y estridente
- Necesita ecualización correctiva

Si se recibe transmisión europea en receptor USA:
- Déficit de agudos: sonido opaco y apagado
- Pérdida de presencia y claridad

**Solución práctica:** Receptores multinorma con preénfasis conmutable.

---

#### Ejemplo 3: Impacto en música vs. voz

**¿Qué pasa con diferentes tipos de contenido?**

**Contenido musical (espectro completo):**
- Energía significativa hasta 15 kHz (platillos, armónicos)
- Sin preénfasis: SNR pobre > 5 kHz, pérdida de "aire" y presencia
- Con preénfasis: SNR uniforme, preservación de detalles sutiles
- Mejora percibida: dramática, especialmente en música clásica y jazz

**Contenido de voz (banda limitada):**
- Energía principal < 4 kHz
- Componentes de fricativas ('s', 'f') en 4-8 kHz se benefician enormemente
- Inteligibilidad mejora significativamente
- Reduce fatiga auditiva en comunicaciones prolongadas

**Caso especial - Transmisión de datos (subportadoras):**
- RDS a 57 kHz sufriría excesivo énfasis
- Se transmite con pre-deénfasis para compensar
- Técnica crítica para servicios auxiliares

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Discriminador FM** (Carta 19): El ruido parabólico aparece después del discriminador
- **Regla de Carson** (Carta 18): El ancho de banda no cambia con preénfasis
- **Comparación FM vs AM** (Carta 43): Preénfasis es ventaja exclusiva de FM
- **Ruido blanco** (Carta 33): Base teórica del análisis de ruido

#### Dependencias (lo que necesitas saber primero)
1. Respuesta en frecuencia de filtros RC → Para entender las redes de énfasis
2. Espectro del ruido FM → Para comprender por qué el ruido crece con f²
3. Decibelios y ganancia → Para cuantificar las mejoras

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Grabación magnética**: Curvas NAB, IEC para cinta
2. **Discos de vinilo**: Curva RIAA (similar concepto)
3. **Dolby Noise Reduction**: Evolución del concepto para cassettes
4. **Procesamiento de audio digital**: Companding espectral

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- El ruido en FM no es uniforme en frecuencia (crece con f²)
- Preénfasis/deénfasis es un "truco" que no cuesta ancho de banda extra
- La mejora en SNR es significativa y medible (~10-13 dB)
- Diferentes regiones usan diferentes estándares (75 vs 50 μs)

#### Tipos de problemas típicos
1. **Diseño de circuitos**: Calcular R y C para una constante de tiempo dada
   - Estrategia: Usar $\tau = RC$ y la impedancia del sistema

2. **Cálculo de mejora SNR**: Determinar ganancia en dB para frecuencia específica
   - Estrategia: Aplicar fórmula de mejora con límites de integración

3. **Análisis de compatibilidad**: Efectos de usar τ incorrecto
   - Estrategia: Comparar respuestas en frecuencia, calcular error en dB

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir preénfasis con aumento de desviación**
- Por qué ocurre: Ambos afectan la modulación
- Cómo evitarlo: Preénfasis cambia forma espectral, no desviación máxima total
- Clarificación: La potencia total de la señal moduladora permanece constante

❌ **Error #2: Aplicar preénfasis después de modular**
- Por qué ocurre: Malentender la cadena de procesamiento
- Cómo evitarlo: Preénfasis SIEMPRE antes del modulador FM
- Consecuencia del error: No habría mejora en SNR

❌ **Error #3: Ignorar la limitación de desviación**
- Por qué ocurre: Preénfasis puede causar sobredesviación en altas frecuencias
- Cómo evitarlo: Usar limitadores o compresores antes del preénfasis
- Práctica: Estaciones FM usan procesadores de audio sofisticados

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Frecuencia de corte: f₁ = 1/(2πτ)
Función preénfasis: Hp(f) = 1 + jf/f₁
Función deénfasis: Hd(f) = 1/(1 + jf/f₁)
Mejora SNR típica: 10-13 dB @ 15 kHz
```

#### Conceptos Fundamentales
- ✓ **Ruido triangular**: En FM, el ruido crece con f² después del discriminador
- ✓ **Compensación exacta**: Hp(f) × Hd(f) = 1 (respuesta plana total)
- ✓ **Sin costo de BW**: La técnica no requiere ancho de banda adicional

#### Reglas Mnemotécnicas
- 🧠 **"PET"**: Preénfasis Eleva Tonos, Deénfasis Destruye Disturbios
- 🧠 **75-50**: USA 75 μs (más énfasis), Europa 50 μs (menos énfasis)
- 🧠 **2-3-15**: 2 kHz corte, 3× mejora, 15 kHz máximo

#### Valores Típicos (para referencias rápidas)
| Parámetro | Valor Típico | Aplicación |
|-----------|--------------|------------|
| τ (USA/Japón) | 75 μs | FM broadcast |
| τ (Europa) | 50 μs | FM broadcast |
| f₁ (USA) | 2.12 kHz | Frecuencia de transición |
| Mejora SNR | 10-13 dB | A 15 kHz |
| Ganancia máx | 17 dB | Preénfasis a 15 kHz |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**:
  - "FM Theory & Applications" de John F. Rider - análisis clásico completo
  - "Communication Systems" de Carlson - Cap. 6.5 sobre mejora de SNR
- **Normas técnicas**: ITU-R BS.450-3 (especificaciones de preénfasis mundial)
- **Simulaciones**: GNU Radio - bloques de preénfasis/deénfasis incluidos

#### Temas Relacionados para Explorar
1. Curva RIAA en discos de vinilo (concepto similar)
2. Dolby A, B, C, S - evolución del concepto
3. Preénfasis en transmisiones satelitales
4. Companding espectral en códecs modernos

#### Preguntas para Reflexionar
- ¿Por qué no usar preénfasis más agresivo (τ menor) para más mejora?
- ¿Cómo interactúa el preénfasis con la compresión de audio moderna?
- ¿Sería útil preénfasis adaptativo que cambie según el contenido?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 50 minutos
**Prerequisitos críticos**: Modulación FM, ruido en FM, filtros RC, análisis espectral
**Tags**: `#FM` `#preenfasis` `#deenfasis` `#mejora-SNR` `#procesamiento-audio`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*