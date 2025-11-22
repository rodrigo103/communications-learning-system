# Carta 35: Figura de Ruido y Factor de Ruido - Caracterización del Rendimiento de Componentes

> **Unidad 7**: Ruido en Sistemas de Comunicaciones

---

## 🎯 Pregunta

Defina la figura de ruido (F) y el factor de ruido (NF). ¿Cómo se relacionan?

---

## 📝 Respuesta Breve (de la carta original)

**Figura de Ruido (F)** (adimensional):
$$F = \frac{SNR_{entrada}}{SNR_{salida}} = \frac{S_i/N_i}{S_o/N_o}$$

Mide cuánto degrada un dispositivo la relación señal-ruido.

**Factor de Ruido (NF)** (en dB):
$$NF = 10\log_{10}(F)$$

**Interpretación**:
- F = 1 (NF = 0 dB): dispositivo ideal (sin ruido)
- F > 1 (NF > 0 dB): el dispositivo agrega ruido
- Típicos: LNA 0.5-2 dB, amplificador 5-10 dB

**Relación con temperatura**:
$$F = 1 + \frac{T_e}{T_0}$$

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La figura de ruido es uno de los **parámetros más importantes** en el diseño de sistemas de comunicaciones. Determina la sensibilidad de los receptores, el alcance de los enlaces y la calidad final de las comunicaciones. Todo dispositivo electrónico activo añade ruido a la señal que procesa, y la figura de ruido cuantifica precisamente esta degradación.

**¿Por qué es importante este concepto?**
- Define el **límite de sensibilidad** de un receptor
- Determina el **alcance máximo** de un sistema de comunicaciones
- Es crítico en el diseño de la **primera etapa** de amplificación
- Afecta directamente la **tasa de error** en sistemas digitales

**¿Dónde se aplica?**
- **Receptores satelitales**: donde las señales son extremadamente débiles
- **Estaciones base celulares**: para maximizar cobertura
- **Radioastronomía**: detectando señales cósmicas mínimas
- **GPS**: recibiendo señales de -160 dBW
- **WiFi y Bluetooth**: optimizando alcance y consumo

**Historia:** El concepto fue formalizado por Harald Friis en los laboratorios Bell en la década de 1940, como parte del desarrollo de sistemas de microondas para telecomunicaciones de larga distancia.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Relación señal-ruido (SNR)
- Ganancia de amplificadores
- Ruido térmico y temperatura de ruido
- Potencia de ruido en ancho de banda

#### Desarrollo Paso a Paso

**Paso 1: El problema fundamental**

Cuando una señal débil pasa por un amplificador, esperaríamos que tanto la señal como el ruido se amplifiquen por igual, manteniendo la SNR constante. Sin embargo, el amplificador mismo genera ruido adicional interno.

**Paso 2: Definición conceptual**

La figura de ruido cuantifica esta degradación comparando:
- La SNR disponible a la entrada
- La SNR resultante a la salida

**Paso 3: Formalización matemática**

Para un dispositivo con ganancia G:

$$F = \frac{SNR_{in}}{SNR_{out}} = \frac{S_i/N_i}{S_o/N_o}$$

#### Derivación Matemática

**Partiendo del modelo de ruido:**

Un amplificador real puede modelarse como uno ideal más una fuente de ruido equivalente a su entrada:

$$N_{out} = G \cdot N_{in} + N_{added}$$

donde $N_{added}$ es el ruido añadido referido a la entrada.

**Desarrollando la SNR de salida:**

$$SNR_{out} = \frac{S_{out}}{N_{out}} = \frac{G \cdot S_{in}}{G \cdot N_{in} + N_{added}}$$

**Dividiendo numerador y denominador por G:**

$$SNR_{out} = \frac{S_{in}}{N_{in} + N_{added}/G}$$

**Por lo tanto, la figura de ruido es:**

$$F = \frac{SNR_{in}}{SNR_{out}} = \frac{S_{in}/N_{in}}{S_{in}/(N_{in} + N_{added}/G)}$$

**Simplificando:**

$$\boxed{F = 1 + \frac{N_{added}}{G \cdot N_{in}}}$$

**Significado físico de cada término:**
- $F = 1$: corresponde al caso ideal sin ruido añadido
- $N_{added}/(G \cdot N_{in})$: representa la contribución del ruido del dispositivo
- $N_{in}$: ruido de entrada (típicamente térmico a temperatura ambiente)

### 🔬 Intuición y Analogías

**Analogía principal:**

Imagina un amplificador de audio conectado a un micrófono en una sala silenciosa. El micrófono capta un susurro (señal) y algo de ruido ambiente (ruido de entrada). El amplificador aumenta el volumen del susurro, pero también añade su propio "siseo" electrónico. La figura de ruido mide cuánto "siseo extra" añade el amplificador en comparación con simplemente amplificar lo que ya estaba presente.

**Intuición física:**

La figura de ruido responde a la pregunta: "¿Cuánto ruido extra genera este dispositivo comparado con un dispositivo ideal que solo amplifica?"

**Visualización:**

Imagina dos tubos de agua:
- Tubo ideal: el agua (señal) y las burbujas (ruido) fluyen proporcionalmente
- Tubo real: además de amplificar el flujo, inyecta burbujas adicionales
- La figura de ruido mide la proporción de burbujas extra añadidas

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Amplificador de Bajo Ruido (LNA) para Receptor Satelital

**Situación:** Diseñando el front-end de un receptor de TV satelital en banda Ku (12 GHz)

**Datos:**
| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Ganancia del LNA | 20 | dB |
| Figura de ruido | 1.5 | dB |
| Temperatura ambiente | 290 | K |
| Ancho de banda | 30 | MHz |

**Solución paso a paso:**

1. **Convertir NF a figura lineal:**
   $$F = 10^{1.5/10} = 1.413$$

2. **Calcular temperatura equivalente de ruido:**
   $$T_e = T_0(F - 1) = 290 \times 0.413 = 119.8 \text{ K}$$

3. **Potencia de ruido añadida:**
   $$N_{added} = kT_e B = 1.38 \times 10^{-23} \times 119.8 \times 30 \times 10^6$$
   $$N_{added} = 4.96 \times 10^{-14} \text{ W} = -103.0 \text{ dBm}$$

**Interpretación:** El LNA añade solo 119.8 K de temperatura de ruido, permitiendo recibir señales muy débiles del satélite.

---

#### Ejemplo 2: Comparación de Tecnologías de Amplificadores

**Contexto:** Selección de tecnología para estación base 5G en 3.5 GHz

| Tecnología | NF (dB) | Ganancia (dB) | Costo Relativo | Consumo (W) |
|------------|---------|---------------|----------------|-------------|
| GaAs pHEMT | 0.5 | 15 | Alto (3x) | 2 |
| GaN HEMT | 1.2 | 18 | Muy Alto (5x) | 5 |
| Si CMOS | 2.5 | 12 | Bajo (1x) | 1 |
| SiGe BiCMOS | 1.0 | 16 | Medio (2x) | 1.5 |

**Análisis de sensibilidad del sistema:**

Para una SNR mínima requerida de 10 dB y ruido térmico de -174 dBm/Hz:

- **Con GaAs pHEMT:** Sensibilidad = -174 + 10log(BW) + 0.5 + 10 = -163.5 + 10log(BW) dBm
- **Con Si CMOS:** Sensibilidad = -174 + 10log(BW) + 2.5 + 10 = -161.5 + 10log(BW) dBm

**Diferencia:** 2 dB de mejor sensibilidad con GaAs, equivalente a ~26% más de alcance.

---

#### Ejemplo 3: Efecto de la Temperatura en la Figura de Ruido

**¿Qué pasa cuando enfriamos un amplificador?**

**Caso: LNA criogénico para radioastronomía**

- **A temperatura ambiente (290 K):**
  - NF = 1.0 dB → F = 1.259
  - Te = 75 K

- **Enfriado a nitrógeno líquido (77 K):**
  - Te se reduce ~proporcionalmente: Te_cold ≈ 75 × (77/290) = 20 K
  - F_cold = 1 + 20/77 = 1.26 (referido a 77 K)
  - NF_cold = 0.26 dB

- **Enfriado a helio líquido (4 K):**
  - Te_cold ≈ 75 × (4/290) = 1 K
  - F_cold = 1 + 1/4 = 1.25 (referido a 4 K)
  - NF_cold = 0.1 dB

**Conclusión:** El enfriamiento criogénico puede reducir dramáticamente la figura de ruido.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Temperatura de ruido** (Carta 34): Forma alternativa de expresar el ruido añadido
- **Fórmula de Friis** (Carta 36): Cálculo de NF en cascada
- **Ruido blanco** (Carta 33): Modelo base del ruido térmico
- **SNR y BER**: La figura de ruido afecta directamente el rendimiento del sistema

#### Dependencias (lo que necesitas saber primero)
1. Concepto de SNR → Base para entender la degradación
2. Ganancia de amplificadores → Relación señal entrada/salida
3. Potencia de ruido térmico → Referencia para el ruido añadido

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Diseño de receptores**: Selección de componentes de RF
2. **Análisis de enlace**: Cálculo de sensibilidad y alcance
3. **Optimización de sistemas**: Trade-off entre NF, ganancia y linealidad

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La figura de ruido **siempre es ≥ 1** (NF ≥ 0 dB)
- Un dispositivo pasivo (atenuador) tiene F = L (sus pérdidas)
- La diferencia entre figura (lineal) y factor (dB) de ruido
- La relación con temperatura equivalente de ruido
- Por qué la primera etapa es crítica (ver Friis)

#### Tipos de problemas típicos
1. **Conversión entre F, NF y Te**: Dados unos, calcular los otros
   - Estrategia: Memorizar las tres fórmulas de conversión:
     1. **F ↔ NF**: $NF = 10\log_{10}(F)$ y $F = 10^{NF/10}$
     2. **F ↔ Te**: $F = 1 + \frac{T_e}{T_0}$ y $T_e = T_0(F - 1)$
     3. **NF ↔ Te**: Combinando las dos anteriores con $T_0 = 290$ K

2. **Comparación de dispositivos**: Seleccionar el mejor para una aplicación
   - Estrategia: Considerar NF, ganancia, costo y consumo

3. **Cálculo de sensibilidad**: Determinar señal mínima detectable
   - Estrategia: Sensibilidad = kTB × F × SNR_min

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir figura (F) con factor (NF)**
- Por qué ocurre: Nombres similares, ambos describen ruido
- Cómo evitarlo: F es lineal (adimensional), NF está en dB
- Ejemplo: F = 2 corresponde a NF = 3 dB, no 2 dB

❌ **Error #2: Pensar que NF negativo es posible**
- Por qué ocurre: Confusión con ganancia negativa (pérdida)
- Cómo evitarlo: NF siempre ≥ 0 dB (F ≥ 1)
- Dispositivo ideal: NF = 0 dB, no negativo

❌ **Error #3: Ignorar la temperatura de referencia**
- Por qué ocurre: Fórmulas simplificadas asumen T₀ = 290 K
- Cómo evitarlo: Verificar siempre la temperatura de referencia
- En criogenia: las fórmulas estándar no aplican directamente

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
F = SNR_in / SNR_out          [Figura de ruido]
NF = 10 log₁₀(F)              [Factor en dB]
F = 1 + Te/T₀                 [Relación con temperatura]
Te = T₀(F - 1)                [Temperatura equivalente]
```

#### Conceptos Fundamentales
- ✓ **Degradación inevitable**: Todo dispositivo activo añade ruido (F > 1)
- ✓ **Primera etapa crítica**: Define la NF del sistema completo
- ✓ **Trade-off fundamental**: Menor NF generalmente significa mayor costo
- ✓ **Límite físico**: Relacionado con la temperatura física del dispositivo

#### Reglas Mnemotécnicas
- 🧠 **"FANTA"**: Figure Always Not less Than one Always (F ≥ 1 siempre)
- 🧠 **"3 dB = doble"**: NF de 3 dB significa F = 2 (doble ruido)
- 🧠 **"Frío es silencioso"**: Menor temperatura → menor ruido

#### Valores Típicos (para referencias rápidas)
| Dispositivo | NF Típico | Aplicación |
|-------------|-----------|------------|
| LNA GaAs | 0.5-1.5 dB | Satélite, radar |
| LNA Silicon | 2-4 dB | WiFi, celular |
| Mezclador | 6-10 dB | Conversión de frecuencia |
| Cable coaxial | 0.2 dB/m @ 1GHz | Interconexión |
| Amplificador IF | 5-8 dB | Etapa intermedia |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**:
  - Pozar, "Microwave Engineering", Cap. 10
  - Razavi, "RF Microelectronics", Cap. 2
- **Material del curso**: Notas sobre diseño de receptores de bajo ruido
- **Simulaciones**: ADS, CST para análisis de ruido en circuitos RF

#### Temas Relacionados para Explorar
1. Círculos de ruido constante en carta de Smith
2. Optimización simultánea de ruido y adaptación
3. Medición de figura de ruido con analizador

#### Preguntas para Reflexionar
- ¿Por qué no podemos tener F < 1 incluso con enfriamiento extremo?
- ¿Cómo afecta la no-linealidad a la figura de ruido efectiva?
- ¿Existe un límite cuántico fundamental para la figura de ruido?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 20 minutos
**Prerequisitos críticos**: SNR, ganancia, ruido térmico
**Tags**: `#ruido` `#figura-de-ruido` `#receptores` `#LNA` `#sensibilidad`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*