# Carta 32: Detección Coherente vs No Coherente

> **Unidad 6**: Modulación Digital

---

## 🎯 Pregunta

Compare detección coherente vs. no coherente en modulaciones digitales.

---

## 📝 Respuesta Breve (de la carta original)

**Detección Coherente**:
- Requiere **referencia de fase sincronizada** con portadora transmitida
- Usa correlación o multiplicación con portadora local
- **Ventaja**: mejor desempeño (menor BER para mismo SNR)
- **Desventaja**: circuito de recuperación de portadora necesario
- Usado en: PSK, QAM

**Detección No Coherente**:
- No requiere sincronización de fase
- Usa detección de envolvente o discriminador
- **Ventaja**: implementación más simple
- **Desventaja**: degradación de ~3 dB en SNR
- Usado en: FSK no coherente, ASK

**Penalidad típica**: no coherente requiere ~3 dB más de SNR para mismo BER

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La elección entre **detección coherente y no coherente** representa una de las decisiones de diseño más fundamentales en sistemas de comunicación digital, estableciendo un trade-off crítico entre complejidad del receptor y eficiencia de potencia. Esta decisión impacta directamente el costo, consumo de energía y desempeño del sistema completo. En esencia, la pregunta es: ¿vale la pena la complejidad adicional de sincronizar perfectamente con la fase de la portadora transmitida para obtener mejor sensibilidad?

¿Por qué es importante esta distinción? Considera un teléfono satelital en medio del océano versus un router WiFi en tu casa. El teléfono satelital opera con señales extremadamente débiles donde cada decibelio cuenta, justificando la complejidad de detección coherente. El router WiFi, con señales relativamente fuertes y requisitos de bajo costo, puede permitirse la simplicidad de detección no coherente en ciertos casos. Esta flexibilidad ha permitido que las comunicaciones digitales se adapten a una increíble variedad de aplicaciones.

Históricamente, los primeros sistemas de radio usaban detección no coherente por necesidad - la tecnología para mantener sincronización de fase precisa simplemente no existía. La detección de envolvente en receptores AM de los años 1920s es un ejemplo clásico. No fue hasta el desarrollo del Phase-Locked Loop (PLL) en los 1930s-40s y su perfeccionamiento en la era espacial de los 1960s que la detección coherente se volvió práctica. Hoy, con procesamiento digital de señales, podemos elegir dinámicamente entre ambos métodos según las condiciones del canal.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Fase de portadora** - concepto de fase absoluta vs relativa
- **Sincronización** - recuperación de portadora y temporización
- **Detección de envolvente** - demodulación basada en amplitud
- **Correlación** - producto interno entre señales

#### Desarrollo Paso a Paso

**Paso 1: Principio de Detección Coherente**

La detección coherente requiere que el receptor genere una réplica exacta de la portadora transmitida, incluyendo su fase:

1. Señal recibida: $r(t) = s(t)\cos(2\pi f_c t + \phi) + n(t)$
2. Oscilador local sincronizado: $\cos(2\pi f_c t + \phi)$
3. Multiplicación y filtrado paso-bajo recupera la señal banda base
4. La fase $\phi$ debe ser estimada y rastreada continuamente

Este proceso maximiza la energía de señal extraída, pero requiere circuitos de sincronización complejos.

**Paso 2: Principio de Detección No Coherente**

La detección no coherente evita la necesidad de conocer la fase absoluta:

1. Para amplitud: detecta la envolvente $|r(t)|$ independiente de fase
2. Para frecuencia: detecta cambios de frecuencia sin referencia de fase
3. Para fase diferencial: compara fase entre símbolos consecutivos

No requiere sincronización de portadora, pero desperdicia parte de la energía de señal al ignorar información de fase.

**Paso 3: Análisis de Penalidad en Desempeño**

La penalidad de usar detección no coherente se manifiesta como:
- Mayor Eb/N0 requerido para el mismo BER
- Típicamente 1-3 dB de penalidad
- La penalidad exacta depende de la modulación y condiciones del canal

#### Derivación Matemática

**Análisis para BPSK/DPSK:**

**BPSK Coherente:**
Señal recibida correlacionada con portadora sincronizada:
$$y = \int_0^T r(t)\cos(2\pi f_c t)dt = \pm\sqrt{E_b} + n$$

Probabilidad de error:
$$P_e^{coh} = Q\left(\sqrt{\frac{2E_b}{N_0}}\right)$$

**DPSK No Coherente:**
Decisión basada en fase diferencial entre símbolos:
$$\Delta\phi = \phi_k - \phi_{k-1}$$

Probabilidad de error:
$$P_e^{non-coh} = \frac{1}{2}e^{-E_b/N_0}$$

**Comparación de Eb/N0 requerido:**
Para BER = 10⁻⁶:
- BPSK coherente: Eb/N0 = 10.5 dB
- DPSK no coherente: Eb/N0 = 11.3 dB
- **Penalidad: 0.8 dB**

**FSK Coherente vs No Coherente:**

**FSK Coherente (ortogonal):**
$$P_e^{coh} = Q\left(\sqrt{\frac{E_b}{N_0}}\right)$$

**FSK No Coherente:**
$$P_e^{non-coh} = \frac{1}{2}e^{-E_b/2N_0}$$

**Penalidad a BER = 10⁻⁶:**
- Coherente: 13.5 dB
- No coherente: 14.2 dB
- **Penalidad: 0.7 dB**

**Significado físico:**
- La detección coherente usa información completa (amplitud y fase)
- La no coherente descarta información de fase absoluta
- La pérdida de información se traduce en pérdida de sensibilidad

### 🔬 Intuición y Analogías

**Analogía principal:**

Imagina que estás tratando de entender a alguien hablando en una fiesta ruidosa. La detección coherente es como poder ver los labios de la persona además de escuchar - tienes información visual (fase) sincronizada perfectamente con el audio. La detección no coherente es como escuchar con los ojos cerrados - solo usas la intensidad y patrones del sonido, no la información visual adicional. Naturalmente, entenderás mejor con los ojos abiertos (coherente), pero requiere mantener contacto visual constante (sincronización).

**Intuición física:**

En detección coherente, el receptor "engancha" la onda exacta transmitida, cabalgando sus crestas y valles en perfecta sincronía. Es como dos bailarines perfectamente coordinados. En detección no coherente, el receptor solo observa cuánta energía hay o cómo cambia el ritmo, sin intentar seguir el baile exacto. Es más robusto pero menos preciso.

**Visualización:**

Piensa en la señal recibida como un vector rotando en el plano complejo. La detección coherente conoce el ángulo exacto y puede proyectar el vector completo sobre el eje correcto. La detección no coherente solo puede medir la longitud del vector (envolvente) o qué tan rápido gira (frecuencia), perdiendo información sobre su orientación absoluta.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Sistema GPS con Detección Coherente

**Situación:** Receptor GPS demodulando señal satelital extremadamente débil.

**Datos:**
| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Potencia recibida | -160 | dBW |
| Densidad de ruido | -204 | dBW/Hz |
| Chip rate | 1.023 | MHz |
| Ganancia de procesamiento | 43 | dB |
| Modulación | BPSK | - |

**Solución paso a paso:**

1. **C/N0 (Carrier to Noise density):**
   $$C/N_0 = -160 - (-204) = 44 \text{ dB-Hz}$$

2. **Eb/N0 después del despreading:**
   $$E_b/N_0 = C/N_0 + G_p - 10\log_{10}(R_b)$$
   $$= 44 + 43 - 10\log_{10}(50) = 44 + 43 - 17 = 70 \text{ dB}$$

3. **BER con detección coherente:**
   Con Eb/N0 = 70 dB (enormemente alto después del procesamiento):
   $$BER_{coherente} < 10^{-15}$$

4. **Si usáramos detección no coherente (hipotético):**
   Pérdida de 3 dB en sensibilidad significaría:
   - Reducción en alcance de adquisición
   - Mayor tiempo para primera posición
   - Pérdida de señales débiles en interiores

**Interpretación:** GPS usa detección coherente porque cada dB cuenta cuando las señales están 20 dB bajo el piso de ruido antes del despreading.

---

#### Ejemplo 2: Bluetooth con GFSK No Coherente

**Contexto:** Dispositivo Bluetooth Low Energy optimizado para bajo consumo.

Bluetooth Classic usa GFSK (Gaussian FSK) con detección no coherente:

**Ventajas de no coherente en este caso:**
- Receptor más simple → menor consumo (crítico para auriculares, wearables)
- Tolerante a offset de frecuencia entre dispositivos baratos
- Rápida sincronización para transmisiones cortas (publicidad BLE)

**Trade-offs aceptables:**
- Alcance limitado a ~10m (no crítico para aplicación)
- Sensibilidad de -70 dBm (suficiente para uso personal)
- BER objetivo de 10⁻³ (audio tolera errores ocasionales)

**Comparación de consumo:**
- Receptor coherente: ~30 mW
- Receptor no coherente: ~15 mW
- Ahorro del 50% en potencia justifica la penalidad de 3 dB en sensibilidad

---

#### Ejemplo 3: Transición Adaptativa en Modems Telefónicos

**Evolución histórica de los modems V.32/V.34:**

Los modems telefónicos evolucionaron de detección no coherente a coherente:

**V.21 (300 bps) - No coherente FSK:**
- Simple y robusto
- Funcionaba en líneas muy ruidosas
- No requería ecualización

**V.32 (9600 bps) - Coherente QAM con entrenamiento:**
- Secuencia de entrenamiento para sincronización
- Ecualización adaptativa
- Recuperación de portadora con PLL

**Proceso de establecimiento de conexión:**
1. **Fase 1**: FSK no coherente para handshake inicial (robusto)
2. **Fase 2**: Entrenamiento para establecer sincronización
3. **Fase 3**: QAM coherente para datos de alta velocidad

Esta transición muestra cómo un sistema puede usar ambos tipos según la fase de operación.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **BER** (Carta 31): Penalidad directa en BER por detección no coherente
- **PSK/QAM** (Cartas 27, 29): Requieren detección coherente obligatoriamente
- **FSK** (Carta 27): Puede usar cualquier tipo de detección
- **Sincronización**: Tema crítico para implementar detección coherente

#### Dependencias (lo que necesitas saber primero)
1. **Phase-Locked Loop (PLL)** → Circuito clave para detección coherente
2. **Detección de envolvente** → Base de detección no coherente
3. **Ruido de fase** → Limita el desempeño de detección coherente

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Diseño de receptores**: Selección de arquitectura según requisitos
2. **Sistemas adaptativos**: Cambio dinámico de modo de detección
3. **Enlaces de potencia limitada**: Evaluación de trade-offs

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- No es simplemente "coherente = mejor": hay trade-offs válidos
- La penalidad típica de 3 dB, pero varía con modulación
- Cuándo la complejidad de coherente se justifica
- Imposibilidad de detección no coherente para ciertas modulaciones (QAM)

#### Tipos de problemas típicos
1. **Cálculo de penalidad**: Comparar Eb/N0 para mismo BER
   - Estrategia: Usar fórmulas o tablas para ambos casos

2. **Selección de detección**: Elegir tipo según requisitos del sistema
   - Estrategia: Evaluar trade-offs de complejidad, consumo y desempeño

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Asumir que coherente siempre es mejor**
- Por qué ocurre: Énfasis académico en desempeño óptimo
- Cómo evitarlo: Considerar requisitos completos del sistema
- Ejemplo: IoT prefiere no coherente por consumo de batería

❌ **Error #2: Confundir detección diferencial con no coherente**
- Por qué ocurre: DPSK a veces se llama "pseudo-coherente"
- Cómo evitarlo: DPSK es no coherente respecto a fase absoluta
- Pero mantiene coherencia entre símbolos consecutivos

❌ **Error #3: Ignorar tiempo de adquisición en coherente**
- Distinción importante: Coherente requiere tiempo de sincronización
- Para ráfagas cortas, puede ser prohibitivo

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Penalidad típica: 1-3 dB en Eb/N0
BPSK coherente: BER = Q(√(2Eb/N0))
DPSK no coherente: BER = 0.5×exp(-Eb/N0)
FSK coherente: BER = Q(√(Eb/N0))
FSK no coherente: BER = 0.5×exp(-Eb/2N0)
```

#### Conceptos Fundamentales
- ✓ **Trade-off fundamental**: Complejidad vs sensibilidad
- ✓ **Recuperación de portadora**: Requisito crítico para coherente
- ✓ **Modulaciones incompatibles**: QAM requiere coherente obligatoriamente
- ✓ **Aplicaciones mixtas**: Sistemas pueden usar ambos según fase

#### Reglas Mnemotécnicas
- 🧠 **"Coherente = Complejo pero Capaz"**: Las tres C
- 🧠 **"3 dB rule"**: Penalidad típica de no coherente

#### Valores Típicos (para referencias rápidas)
| Modulación | Penalidad No-Coh | Aplicación típica |
|------------|------------------|-------------------|
| BPSK/DPSK | 0.8-1 dB | Telemetría espacial |
| FSK | 0.7-1 dB | Bluetooth, LoRa |
| OOK/ASK | 0.5 dB | Control remoto IR |
| QAM | No aplicable | Solo coherente |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**: Simon & Alouini "Digital Communication over Fading Channels"
- **Material del curso**: Laboratorio de PLL y recuperación de portadora
- **Simulaciones**: GNU Radio - comparación de detectores coherente/no coherente

#### Temas Relacionados para Explorar
1. Sincronización de portadora en canales con desvanecimiento
2. Detección parcialmente coherente (piloto asistida)
3. Estimación ciega de canal para detección coherente

#### Preguntas para Reflexionar
- ¿Cómo afecta el Doppler a cada tipo de detección?
- ¿Por qué la fibra óptica prefiere detección coherente en sistemas modernos?
- ¿Podría diseñarse un receptor que cambie adaptativamente entre ambos modos?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 45 minutos
**Prerequisitos críticos**: Modulaciones digitales, sincronización, BER
**Tags**: `#deteccion` `#coherente` `#no-coherente` `#receptores` `#trade-offs`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*