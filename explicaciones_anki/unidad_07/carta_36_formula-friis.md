# Carta 36: Fórmula de Friis para Sistemas en Cascada - La Importancia de la Primera Etapa

> **Unidad 7**: Ruido en Sistemas de Comunicaciones

---

## 🎯 Pregunta

Enuncie y explique la fórmula de Friis para figura de ruido en sistemas en cascada.

---

## 📝 Respuesta Breve (de la carta original)

La **fórmula de Friis** calcula la figura de ruido total de una cascada de dispositivos:

$$F_{total} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \frac{F_4 - 1}{G_1 G_2 G_3} + ...$$

donde:
- $F_i$ = figura de ruido del i-ésimo dispositivo
- $G_i$ = ganancia de potencia (lineal) del i-ésimo dispositivo

**Implicaciones**:
1. **Primera etapa domina**: $F_1$ tiene mayor impacto
2. **Alta ganancia inicial**: reduce contribución de etapas posteriores
3. **LNA crítico**: amplificador de bajo ruido al inicio es fundamental
4. **Diseño**: maximizar $G_1$ y minimizar $F_1$

**Ejemplo**: en receptor, LNA determina sensibilidad del sistema.

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La fórmula de Friis es uno de los **resultados más fundamentales** en el diseño de receptores de radiofrecuencia. Desarrollada por Harald Friis en Bell Labs en 1944, revolucionó la forma en que diseñamos las cadenas de recepción, estableciendo matemáticamente por qué la primera etapa de amplificación es crítica para el rendimiento del sistema completo.

**¿Por qué es importante este concepto?**
- Determina la **arquitectura óptima** de receptores
- Justifica el uso de **LNAs costosos** en la primera etapa
- Define la **sensibilidad máxima** alcanzable del sistema
- Guía las decisiones de **trade-off** entre componentes

**¿Dónde se aplica?**
- **Receptores GPS**: con señales de -160 dBW requieren NF < 2 dB total
- **Estaciones base 5G**: optimizando para máxima cobertura
- **Radiotelescopios**: detectando señales cósmicas de femtowatts
- **Receptores satelitales**: maximizando la calidad de señal
- **Sistemas de radar**: mejorando el alcance de detección

**Historia y contexto:** Durante la Segunda Guerra Mundial, Friis trabajaba en sistemas de radar cuando formalizó esta relación. Su descubrimiento mostró que invertir en un excelente primer amplificador era más efectivo que mejorar todas las etapas por igual.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Figura de ruido individual (Carta 35)
- Ganancia de amplificadores en cascada
- Adición de potencias de ruido no correlacionadas
- Conversión entre unidades lineales y dB

#### Desarrollo Paso a Paso

**Paso 1: El problema de la cascada**

En un receptor real, la señal pasa por múltiples componentes: LNA, mezclador, filtros, amplificadores IF, etc. Cada uno añade ruido y tiene una ganancia específica. ¿Cómo se combina el efecto total?

**Paso 2: Principio de superposición de ruido**

El ruido de cada etapa se suma en potencia (no en voltaje) porque son procesos aleatorios independientes. Pero el ruido de etapas posteriores se ve "atenuado" por la ganancia de las etapas anteriores cuando lo referimos a la entrada.

**Paso 3: Construcción de la fórmula**

Cada etapa contribuye ruido, pero esa contribución se divide por la ganancia acumulada de todas las etapas anteriores.

#### Derivación Matemática

**Modelo de cascada de dos etapas:**

Consideremos primero dos dispositivos en cascada:

**Etapa 1:**
- Figura de ruido: $F_1$
- Ganancia: $G_1$
- Ruido añadido (referido a entrada): $N_{a1} = (F_1 - 1)N_{in}$

**Etapa 2:**
- Figura de ruido: $F_2$
- Ganancia: $G_2$
- Ruido añadido (referido a su entrada): $N_{a2} = (F_2 - 1)N_{in}G_1$

**Ruido total a la salida:**
$$N_{out} = G_1G_2[N_{in} + N_{a1}/G_1 + N_{a2}/(G_1G_2)]$$

**Simplificando y refiriendo a la entrada:**
$$N_{out,ref} = N_{in} + (F_1 - 1)N_{in} + \frac{(F_2 - 1)N_{in}}{G_1}$$

**Figura de ruido total:**
$$F_{total} = \frac{N_{out,ref}}{N_{in}} = 1 + (F_1 - 1) + \frac{F_2 - 1}{G_1}$$

**Generalizando para n etapas:**

$$\boxed{F_{total} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + ... + \frac{F_n - 1}{\prod_{i=1}^{n-1} G_i}}$$

**Significado físico de cada término:**
- $F_1$: Contribución completa de la primera etapa
- $(F_i - 1)/\prod G_j$: Contribución de la i-ésima etapa, reducida por ganancia previa
- La división por $G_1G_2...$ representa la "dilución" del ruido por amplificación previa

### 🔬 Intuición y Analogías

**Analogía del megáfono en cadena:**

Imagina una cadena de personas con megáfonos pasándose un mensaje susurrado:
- La primera persona (LNA) escucha el susurro original más el ruido ambiente
- Si esta persona tiene un megáfono ruidoso, ese ruido se amplifica en toda la cadena
- Las personas siguientes también añaden ruido, pero como el mensaje ya viene amplificado, su ruido relativo es menor
- Por eso, es crucial que la primera persona tenga el megáfono más silencioso

**Intuición física:**

El ruido de las etapas posteriores se ve "pequeño" comparado con la señal ya amplificada. Es como añadir una gota de tinta a un vaso de agua (primera etapa) versus añadirla a una piscina (etapas posteriores).

**Visualización del dominio:**

```
Entrada → [LNA] → [Mixer] → [IF Amp] → Salida
  ↓         ↓        ↓          ↓
Ruido₁   Ruido₂/G₁  Ruido₃/G₁G₂  (contribuciones)
```

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Diseño de Front-End de Receptor GPS

**Situación:** Diseñar la cadena de RF para un receptor GPS de alta sensibilidad

**Datos de componentes disponibles:**

| Componente | NF (dB) | Ganancia (dB) | F (lineal) | G (lineal) |
|------------|---------|---------------|------------|------------|
| LNA opción A | 0.8 | 18 | 1.20 | 63.1 |
| LNA opción B | 1.5 | 25 | 1.41 | 316.2 |
| Filtro SAW | 2.0 | -2 | 1.58 | 0.63 |
| Mezclador | 7.0 | -6 | 5.01 | 0.25 |
| Amp IF | 4.0 | 30 | 2.51 | 1000 |

**Configuración 1: LNA A → Filtro → Mezclador → Amp IF**

1. **Aplicar Friis:**
   $$F_{total} = 1.20 + \frac{1.58 - 1}{63.1} + \frac{5.01 - 1}{63.1 \times 0.63} + \frac{2.51 - 1}{63.1 \times 0.63 \times 0.25}$$

2. **Calcular término por término:**
   - Término 1: 1.20
   - Término 2: 0.58/63.1 = 0.0092
   - Término 3: 4.01/39.75 = 0.101
   - Término 4: 1.51/9.94 = 0.152

3. **Resultado:**
   $$F_{total} = 1.20 + 0.009 + 0.101 + 0.152 = 1.462$$
   $$NF_{total} = 10\log(1.462) = 1.65 \text{ dB}$$

**Configuración 2: LNA B → Filtro → Mezclador → Amp IF**

Siguiendo el mismo proceso:
$$F_{total} = 1.41 + \frac{0.58}{316.2} + \frac{4.01}{199.2} + \frac{1.51}{49.8} = 1.464$$
$$NF_{total} = 1.66 \text{ dB}$$

**Interpretación:** Aunque LNA B tiene peor NF individual, su mayor ganancia compensa, resultando en NF total similar.

---

#### Ejemplo 2: Optimización de Receptor de Estación Base 5G

**Contexto:** Receptor de estación base con arquitectura heterodina en 3.5 GHz

**Cadena de recepción propuesta:**
1. Filtro de antena: Pérdida = 0.5 dB
2. LNA: NF = 0.6 dB, G = 15 dB
3. Filtro imagen: Pérdida = 1 dB
4. Mezclador: NF = 8 dB, G = -7 dB
5. Amplificador IF: NF = 3 dB, G = 40 dB

**Análisis detallado:**

| Etapa | NF (dB) | G (dB) | F | G | F acumulada |
|-------|---------|--------|---|---|-------------|
| Filtro antena | 0.5 | -0.5 | 1.12 | 0.891 | 1.12 |
| LNA | 0.6 | 15 | 1.15 | 31.62 | 1.122 + 0.168 = 1.29 |
| Filtro imagen | 1.0 | -1.0 | 1.26 | 0.794 | 1.29 + 0.009 = 1.30 |
| Mezclador | 8.0 | -7 | 6.31 | 0.20 | 1.30 + 0.212 = 1.51 |
| Amp IF | 3.0 | 40 | 2.0 | 10000 | 1.51 + 0.0002 = 1.51 |

**NF total del sistema = 1.79 dB**

**Impacto de cambiar el LNA:**
- Con LNA de 1.5 dB: NF total = 2.62 dB
- Diferencia: 0.83 dB (pérdida de ~10% en alcance)

---

#### Ejemplo 3: Efecto de Reordenar Componentes

**¿Qué pasa si ponemos el mezclador antes del LNA?**

**Configuración incorrecta:** Mezclador → LNA → Amp IF

Usando los mismos componentes del ejemplo anterior:

$$F_{total} = 6.31 + \frac{1.15 - 1}{0.20} + \frac{2.0 - 1}{0.20 \times 31.62}$$
$$F_{total} = 6.31 + 0.75 + 0.16 = 7.22$$
$$NF_{total} = 8.59 \text{ dB}$$

**Comparación:**
- Configuración correcta (LNA primero): 1.79 dB
- Configuración incorrecta (Mezclador primero): 8.59 dB
- **Degradación: 6.8 dB** (pérdida de 75% del alcance)

Esto demuestra dramáticamente por qué el LNA debe ir primero.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Figura de ruido individual** (Carta 35): Base para entender cada término
- **Temperatura de ruido** (Carta 34): Forma alternativa de expresar Friis
- **Sensibilidad del receptor**: Determinada por NF total
- **Análisis de enlace**: NF total entra en el cálculo del margen

#### Dependencias (lo que necesitas saber primero)
1. Figura de ruido de dispositivos individuales
2. Ganancia en cascada: $G_{total} = \prod G_i$
3. Conversión dB ↔ lineal
4. Modelo de ruido aditivo

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Diseño de receptores**: Optimización de arquitectura
2. **Análisis de presupuesto de ruido**: Trade-offs costo/rendimiento
3. **Especificación de componentes**: Requisitos mínimos por etapa

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- Por qué la primera etapa es **dominante** en el ruido total
- Cómo una alta ganancia inicial **suprime** el ruido de etapas posteriores
- La importancia de usar valores **lineales** (no dB) en la fórmula
- Que dispositivos pasivos (pérdidas) tienen F = 1/G = L
- El concepto de **ruido referido a la entrada**

#### Tipos de problemas típicos
1. **Cálculo de NF en cascada**: Dados componentes, hallar NF total
   - Estrategia: Convertir todo a lineal, aplicar Friis, volver a dB

2. **Optimización de orden**: Determinar mejor secuencia de componentes
   - Estrategia: Poner menor NF y mayor G al principio

3. **Especificación de componentes**: Dado NF objetivo, especificar componentes
   - Estrategia: Trabajar hacia atrás desde el requisito total

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Aplicar Friis directamente en dB**
- Por qué ocurre: Tentación de sumar dBs directamente
- Cómo evitarlo: SIEMPRE convertir a valores lineales primero
- Ejemplo: NF₁ = 3 dB + NF₂ = 6 dB ≠ NF_total = 9 dB (¡INCORRECTO!)

❌ **Error #2: Olvidar restar 1 en los términos**
- Por qué ocurre: La fórmula tiene (F - 1) en numeradores
- Cómo evitarlo: Memorizar la forma correcta, entender que F₁ ya incluye el 1
- Consecuencia: Sin el -1, el resultado es muy pesimista

❌ **Error #3: Usar ganancia de voltaje en lugar de potencia**
- Por qué ocurre: Confusión entre tipos de ganancia
- Cómo evitarlo: Friis usa ganancia de POTENCIA (G = V²)
- Verificación: G_dB = 10 log(G), no 20 log(G)

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
F_total = F₁ + (F₂-1)/G₁ + (F₃-1)/(G₁G₂) + ...  [Friis - valores lineales]
NF_total ≠ NF₁ + NF₂ + ...                       [¡INCORRECTO en dB!]
F_pasivo = L (pérdida)                           [Dispositivo pasivo]
G_total = G₁ × G₂ × G₃ × ...                     [Ganancia en cascada]
```

#### Conceptos Fundamentales
- ✓ **Primera etapa manda**: Su NF contribuye completamente al total
- ✓ **Ganancia suprime ruido**: Alta G₁ minimiza contribución de etapas posteriores
- ✓ **LNA justificado**: Vale la pena invertir en excelente primera etapa
- ✓ **Orden importa**: La secuencia de componentes es crítica

#### Reglas Mnemotécnicas
- 🧠 **"FLAP"**: First (stage) Leads All Performance
- 🧠 **"Dividir por ganancia previa"**: Cada término se divide por G acumulada
- 🧠 **"Linear para Friis"**: Siempre trabajar en valores lineales

#### Valores Típicos de Cascadas Completas

| Sistema | NF Total Típico | Dominado por |
|---------|-----------------|--------------|
| Receptor GPS | 2-3 dB | LNA + pérdidas de antena |
| Receptor celular | 3-5 dB | Duplexor + LNA |
| Receptor satelital | 1-2 dB | LNA + alimentador |
| WiFi doméstico | 5-7 dB | Switch + LNA integrado |
| Radioastronomía | < 0.5 dB | LNA criogénico |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**:
  - Pozar, "Microwave Engineering", Cap. 10.3
  - Razavi, "RF Microelectronics", Cap. 2.5
  - Egan, "Practical RF System Design", Cap. 3
- **Papers históricos**: H.T. Friis, "Noise Figures of Radio Receivers", Proc. IRE, 1944
- **Simulaciones**: Keysight SystemVue, Cadence VSS para análisis de cascada

#### Temas Relacionados para Explorar
1. Fórmula de Friis para temperatura de ruido en cascada
2. Análisis de ruido en sistemas con retroalimentación
3. Efecto de desadaptación de impedancia en la figura de ruido
4. Medición de figura de ruido usando método Y-factor

#### Preguntas para Reflexionar
- ¿Qué pasa con Friis si hay ganancia negativa (atenuación) en la primera etapa?
- ¿Cómo se modifica Friis para mezcladores con ganancia de conversión?
- ¿Por qué los radiotelescopios ponen el LNA en el foco de la antena?
- Si el dinero no fuera problema, ¿cuál sería el diseño óptimo?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 30 minutos
**Prerequisitos críticos**: Figura de ruido individual, ganancia en cascada, conversión dB-lineal
**Tags**: `#friis` `#cascada` `#ruido` `#receptores` `#LNA` `#diseño-RF`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*