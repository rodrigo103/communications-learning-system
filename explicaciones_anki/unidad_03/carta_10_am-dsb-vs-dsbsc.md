# Carta 10: Comparación AM-DSB-FC vs DSB-SC

> **Unidad 3**: Modulación Lineal

---

## 🎯 Pregunta

Compare AM-DSB-FC (AM convencional) con DSB-SC en términos de eficiencia de potencia y espectro.

---

## 📝 Respuesta Breve (de la carta original)

**AM-DSB-FC (AM convencional)**:
- Contiene portadora: $s(t) = A_c[1 + m(t)]\cos(2\pi f_c t)$
- Ancho de banda: $BW = 2f_m$
- Eficiencia de potencia: baja (máximo 33% con m=1)
- Ventaja: detección de envolvente simple (no requiere sincronismo)

**DSB-SC (Doble Banda Suprimida)**:
- Sin portadora: $s(t) = A_c m(t)\cos(2\pi f_c t)$
- Ancho de banda: $BW = 2f_m$
- Eficiencia: 100% (toda la potencia en información)
- Desventaja: requiere detección coherente (sincronismo)

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La modulación de amplitud fue la primera forma práctica de transmitir información a largas distancias a través de ondas electromagnéticas. Sin embargo, no todas las implementaciones de AM son iguales en términos de eficiencia. La comparación entre AM-DSB-FC (AM convencional con portadora) y DSB-SC (Doble Banda Lateral con Portadora Suprimida) representa un dilema fundamental en el diseño de sistemas de comunicaciones: **simplicidad versus eficiencia**.

Este concepto es crucial porque aparece constantemente en decisiones de diseño de sistemas reales. Por ejemplo, la radio AM comercial usa AM-DSB-FC precisamente por su simplicidad de demodulación, permitiendo receptores muy económicos. En contraste, sistemas más sofisticados como comunicaciones satelitales o enlaces de microondas, donde la potencia es un recurso escaso y costoso, prefieren DSB-SC o técnicas aún más eficientes.

La comprensión profunda de estas diferencias permite al ingeniero tomar decisiones informadas sobre qué esquema de modulación usar según los recursos disponibles, las restricciones del sistema y los requisitos del usuario final.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Modulación de amplitud básica
- Análisis espectral mediante Transformada de Fourier
- Concepto de eficiencia de potencia
- Detección coherente vs no coherente

#### Desarrollo Paso a Paso

**Paso 1: AM-DSB-FC (AM Convencional con Portadora)**

La señal AM convencional se define matemáticamente como:

$$s_{AM}(t) = A_c[1 + k_a m(t)]\cos(2\pi f_c t)$$

donde:
- $A_c$ = amplitud de la portadora
- $k_a$ = sensibilidad del modulador
- $m(t)$ = señal moduladora normalizada ($|m(t)| \leq 1$)
- $f_c$ = frecuencia de la portadora

Expandiendo esta expresión:
$$s_{AM}(t) = A_c\cos(2\pi f_c t) + A_c k_a m(t)\cos(2\pi f_c t)$$

El primer término es la **portadora pura** que no contiene información, mientras que el segundo término contiene la información modulada.

**Paso 2: DSB-SC (Portadora Suprimida)**

La señal DSB-SC elimina completamente la portadora:

$$s_{DSB-SC}(t) = A_c m(t)\cos(2\pi f_c t)$$

Esta señal contiene solo el producto de la moduladora con la portadora, sin el término de portadora independiente.

**Paso 3: Análisis Espectral**

Para AM-DSB-FC, el espectro es:
$$S_{AM}(f) = \frac{A_c}{2}[\delta(f-f_c) + \delta(f+f_c)] + \frac{A_c k_a}{2}[M(f-f_c) + M(f+f_c)]$$

Para DSB-SC:
$$S_{DSB-SC}(f) = \frac{A_c}{2}[M(f-f_c) + M(f+f_c)]$$

La diferencia clave son los impulsos delta en $\pm f_c$ que representan la portadora en AM convencional.

#### Derivación Matemática de la Eficiencia

**Análisis de Potencia para AM-DSB-FC:**

La potencia total transmitida es:
$$P_{total} = P_{portadora} + P_{bandas\_laterales}$$

Para una señal moduladora sinusoidal con índice de modulación $m$:

$$P_{portadora} = \frac{A_c^2}{2}$$

$$P_{bandas\_laterales} = \frac{m^2 A_c^2}{4}$$

La eficiencia se define como:
$$\eta = \frac{P_{información}}{P_{total}} = \frac{P_{bandas\_laterales}}{P_{portadora} + P_{bandas\_laterales}}$$

$$\boxed{\eta_{AM} = \frac{m^2}{2+m^2}}$$

Para modulación máxima sin distorsión ($m = 1$):
$$\eta_{max} = \frac{1}{3} = 33.33\%$$

**Análisis para DSB-SC:**

En DSB-SC, toda la potencia transmitida está en las bandas laterales:
$$\boxed{\eta_{DSB-SC} = 100\%}$$

### 🔬 Intuición y Analogías

**Analogía principal:**
Imagina que necesitas enviar un paquete por mensajería. AM-DSB-FC es como enviar un camión grande (la portadora) que siempre viaja, llevando o no paquetes. El camión consume combustible constantemente, incluso cuando está vacío. DSB-SC es como usar un servicio de mensajería que solo envía vehículos cuando hay paquetes que entregar - toda la energía se usa para transportar información útil.

**Intuición física:**
La portadora en AM convencional actúa como una "referencia" constante que facilita la detección pero desperdicia potencia. Es como mantener una luz piloto encendida permanentemente para poder encontrar el interruptor en la oscuridad - útil pero ineficiente.

**Visualización:**
En el dominio del tiempo, AM-DSB-FC siempre tiene una envolvente positiva que sigue la forma de la señal moduladora. DSB-SC tiene inversiones de fase (la envolvente cruza por cero) cuando la moduladora cambia de signo, lo que hace imposible la detección de envolvente simple.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Cálculo de Eficiencia para Radio AM

**Situación:** Una estación de radio AM transmite música con índice de modulación promedio de 0.3.

**Datos:**
| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Potencia de portadora | 50 | kW |
| Índice de modulación | 0.3 | - |

**Solución paso a paso:**

1. **Eficiencia del sistema AM:**
   $$\eta = \frac{m^2}{2+m^2} = \frac{0.09}{2.09} = 0.043$$

2. **Potencia útil transmitida:**
   $$P_{útil} = \eta \times P_{total} = 0.043 \times 50 = 2.15 \text{ kW}$$

3. **Potencia desperdiciada en portadora:**
   $$P_{desperdiciada} = 50 - 2.15 = 47.85 \text{ kW}$$

**Interpretación:** Solo el 4.3% de la potencia transmite información. Si usáramos DSB-SC, podríamos transmitir la misma información con solo 2.15 kW, pero necesitaríamos receptores más complejos.

---

#### Ejemplo 2: Comparación en Enlace Satelital

**Contexto:** Un satélite de comunicaciones tiene 100W de potencia disponible para el transmisor.

Con AM-DSB-FC (m=1, mejor caso):
- Potencia en información: 33.33W
- Potencia en portadora: 66.67W

Con DSB-SC:
- Potencia en información: 100W
- Mejora en SNR: $10\log_{10}(100/33.33) = 4.77$ dB

Esta mejora de casi 5 dB puede significar la diferencia entre un enlace confiable y uno que falla frecuentemente.

---

#### Ejemplo 3: Casos Límite

**¿Qué pasa cuando el índice de modulación varía?**

- Si $m \to 0$ (submodulación extrema):
  - AM: $\eta \to 0$ (casi toda la potencia en portadora)
  - DSB-SC: mantiene 100% eficiencia

- Si $m > 1$ (sobremodulación en AM):
  - AM: Distorsión severa, inversión de envolvente
  - DSB-SC: No existe concepto de sobremodulación

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados
- **SSB** (Carta 11): Evolución lógica de DSB-SC, elimina una banda lateral
- **Modulador balanceado** (Carta 14): Circuito para generar DSB-SC
- **Receptor superheterodino** (Carta 12): Necesario para detección coherente de DSB-SC
- **Índice de modulación** (Carta 13): Parámetro crítico en AM convencional

#### Dependencias
1. Análisis de Fourier → Necesario para entender espectros
2. Teoría de potencia en señales → Base para cálculos de eficiencia
3. Multiplicación de señales → Operación fundamental en ambos esquemas

#### Aplicaciones Posteriores
1. **Modulación QAM**: Usa principios de DSB-SC en canales I y Q
2. **Sistemas digitales**: PSK es esencialmente DSB-SC con moduladora digital
3. **OFDM**: Cada subportadora puede verse como DSB-SC

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La portadora no transmite información pero facilita la demodulación
- El trade-off fundamental entre simplicidad y eficiencia
- Cómo calcular y comparar eficiencias de potencia
- Por qué diferentes aplicaciones eligen diferentes esquemas

#### Tipos de problemas típicos
1. **Cálculo de eficiencia**: Dado un índice de modulación, calcular η
2. **Comparación de potencias**: Cuánta potencia se ahorra con DSB-SC
3. **Diseño de sistema**: Justificar elección de esquema según aplicación

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir ancho de banda con eficiencia de potencia**
- Por qué ocurre: Ambos esquemas tienen mismo BW (2fm)
- Cómo evitarlo: Recordar que eficiencia se refiere a distribución de potencia, no espectro
- Ejemplo de error: "DSB-SC es más eficiente porque usa menos ancho de banda" (FALSO)

❌ **Error #2: Asumir que DSB-SC siempre es mejor**
- Por qué ocurre: Foco excesivo en eficiencia de potencia
- Cómo evitarlo: Considerar complejidad del receptor y costo
- Distinción importante: "Mejor" depende del contexto y restricciones

❌ **Error #3: Olvidar que m ≤ 1 en AM convencional**
- Por qué ocurre: No considerar limitaciones físicas
- Cómo evitarlo: Recordar que m > 1 causa distorsión de envolvente

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
AM-DSB-FC: s(t) = Ac[1 + m·m(t)]cos(2πfct)
DSB-SC: s(t) = Ac·m(t)cos(2πfct)
Eficiencia AM: η = m²/(2+m²)
Eficiencia DSB-SC: η = 100%
```

#### Conceptos Fundamentales
- ✓ **Trade-off central**: Simplicidad (AM) vs Eficiencia (DSB-SC)
- ✓ **Detección**: AM permite envolvente simple, DSB-SC requiere coherente
- ✓ **Portadora**: Desperdicia potencia pero sirve de referencia
- ✓ **Aplicabilidad**: AM para broadcast, DSB-SC para enlaces punto a punto

#### Valores Típicos
| Parámetro | AM-DSB-FC | DSB-SC |
|-----------|-----------|---------|
| Eficiencia máxima | 33.33% | 100% |
| Ancho de banda | 2fm | 2fm |
| Complejidad receptor | Baja | Alta |
| Sincronización | No necesaria | Crítica |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Haykin**: Capítulo 3, secciones 3.2-3.3 para análisis matemático detallado
- **Carlson**: Comparación práctica de esquemas AM
- **Simulación MATLAB**: `ammod()` vs modulación DSB-SC manual

#### Temas Relacionados para Explorar
1. VSB como compromiso entre AM y SSB
2. Detección síncrona con PLL
3. Efectos del desvanecimiento selectivo en cada esquema

#### Preguntas para Reflexionar
- ¿Por qué la radio AM comercial nunca migró a DSB-SC a pesar de su ineficiencia?
- ¿Cómo afectaría el ruido de fase del oscilador local a la detección de DSB-SC?
- ¿Qué pasaría si intentamos detectar DSB-SC con un detector de envolvente?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 20 minutos
**Prerequisitos críticos**: Modulación AM básica, análisis de Fourier
**Tags**: `#modulacion-lineal` `#am` `#dsb-sc` `#eficiencia-potencia` `#trade-offs`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*