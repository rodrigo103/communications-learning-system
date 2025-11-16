# Carta 11: Modulación SSB (Banda Lateral Única)

> **Unidad 3**: Modulación Lineal

---

## 🎯 Pregunta

¿Qué es la modulación SSB (BLU) y cuáles son sus ventajas principales?

---

## 📝 Respuesta Breve (de la carta original)

**SSB (Single Sideband - Banda Lateral Única)** transmite solo una banda lateral (superior o inferior), eliminando la portadora y la otra banda.

**Ventajas**:
1. **Ancho de banda mínimo**: $BW = f_m$ (mitad que AM o DSB)
2. **Eficiencia espectral**: máximo aprovechamiento del espectro
3. **Eficiencia de potencia**: toda la potencia transmite información
4. **Menor susceptibilidad al desvanecimiento selectivo**
5. **Aplicaciones**: radioaficionados, comunicaciones HF, telefonía

**Desventaja**: mayor complejidad en generación y detección, requiere sincronismo muy preciso.

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La modulación de Banda Lateral Única (SSB o BLU en español) representa el pináculo de la eficiencia en modulación analógica lineal. Desarrollada en 1915 por John Carson en AT&T, SSB surgió de la necesidad de maximizar la capacidad de los costosos cables telefónicos transatlánticos. Un solo cable podía llevar múltiples conversaciones telefónicas si se usaba el espectro eficientemente.

SSB es fundamental en comunicaciones HF (3-30 MHz), donde el espectro es extremadamente valioso y las condiciones de propagación ionosférica favorecen señales de banda estrecha. Los radioaficionados, servicios marítimos, aviación de largo alcance y comunicaciones militares dependen crucialmente de SSB para enlaces confiables a miles de kilómetros de distancia.

La importancia de SSB trasciende su uso directo - los principios matemáticos detrás de SSB (transformada de Hilbert, señales analíticas) son fundamentales para entender modulaciones modernas como QAM y OFDM. Además, SSB demuestra el límite teórico de eficiencia espectral para modulación analógica: es imposible transmitir una señal analógica en menos ancho de banda que SSB sin pérdida de información.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Análisis espectral y simetría de señales reales
- Transformada de Hilbert
- Filtrado ideal y realizabilidad
- Detección coherente y recuperación de portadora

#### Desarrollo Paso a Paso

**Paso 1: Origen de las Bandas Laterales**

Cuando modulamos una señal $m(t)$ con una portadora $\cos(2\pi f_c t)$:
$$s_{DSB}(t) = m(t)\cos(2\pi f_c t)$$

En el dominio de frecuencia:
$$S_{DSB}(f) = \frac{1}{2}[M(f-f_c) + M(f+f_c)]$$

Para frecuencias positivas, aparecen dos copias del espectro:
- **Banda lateral superior (USB)**: $f_c$ hasta $f_c + f_m$
- **Banda lateral inferior (LSB)**: $f_c - f_m$ hasta $f_c$

**Paso 2: Redundancia Espectral**

Las dos bandas laterales contienen exactamente la misma información (son imágenes especulares). Esto es redundante - podríamos reconstruir completamente $m(t)$ con solo una banda lateral.

**Paso 3: Generación de SSB**

Existen tres métodos principales:

1. **Método del filtro**: Generar DSB-SC y filtrar una banda
2. **Método de fase (Weaver)**: Usar transformada de Hilbert
3. **Método de Tercera**: Dos modulaciones sucesivas

#### Derivación Matemática del Método de Fase

**Señal SSB usando la Transformada de Hilbert:**

La señal analítica de $m(t)$ es:
$$m_a(t) = m(t) + j\hat{m}(t)$$

donde $\hat{m}(t)$ es la transformada de Hilbert de $m(t)$.

La señal SSB se obtiene como:
$$s_{SSB}(t) = \text{Re}[m_a(t)e^{j2\pi f_c t}]$$

Expandiendo:
$$s_{SSB}(t) = m(t)\cos(2\pi f_c t) \mp \hat{m}(t)\sin(2\pi f_c t)$$

donde:
- Signo (-): USB (Upper Sideband)
- Signo (+): LSB (Lower Sideband)

**Análisis Espectral:**

Para USB:
$$S_{USB}(f) = \begin{cases}
M(f-f_c) & f > f_c \\
0 & f < f_c
\end{cases}$$

El ancho de banda resultante:
$$\boxed{BW_{SSB} = f_m}$$

Comparado con DSB: $BW_{DSB} = 2f_m$, SSB usa exactamente la mitad del espectro.

### 🔬 Intuición y Analogías

**Analogía principal:**
SSB es como comprimir un archivo eliminando información redundante. Imagina que tienes una fotografía y su negativo - ambos contienen la misma información pero en forma complementaria. Transmitir ambos sería redundante; con uno puedes reconstruir el otro. Las bandas laterales en DSB son como la foto y su reflejo en un espejo - SSB transmite solo una de ellas.

**Intuición física:**
Cada componente de frecuencia de la señal moduladora crea dos componentes en la señal modulada: una arriba y otra abajo de la portadora. SSB reconoce que estas son redundantes y elimina una mitad completa del espectro, como si cortáramos verticalmente el espectro por la frecuencia de la portadora.

**Visualización:**
En el espectro, SSB aparece como un "espectro asimétrico" alrededor de donde estaría la portadora. No hay simetría hermitiana como en señales reales normales. En el dominio del tiempo, la envolvente de SSB no sigue directamente la señal moduladora - tiene una envolvente compleja que varía tanto en amplitud como en fase.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Cálculo de Ancho de Banda para Transmisión de Voz

**Situación:** Un sistema de comunicación HF necesita transmitir canales de voz con calidad telefónica.

**Datos:**
| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Frecuencia mínima de voz | 300 | Hz |
| Frecuencia máxima de voz | 3400 | Hz |
| Frecuencia de portadora | 14.2 | MHz |

**Solución paso a paso:**

1. **Ancho de banda de la señal de voz:**
   $$BW_{voz} = 3400 - 300 = 3100 \text{ Hz}$$

2. **Ancho de banda con diferentes modulaciones:**
   - AM convencional: $BW_{AM} = 2 \times 3100 = 6200$ Hz
   - DSB-SC: $BW_{DSB} = 2 \times 3100 = 6200$ Hz
   - SSB: $BW_{SSB} = 3100$ Hz

3. **Ubicación espectral de USB:**
   - Límite inferior: 14.2003 MHz
   - Límite superior: 14.2034 MHz

**Interpretación:** SSB permite duplicar el número de canales en el mismo espectro comparado con AM o DSB.

---

#### Ejemplo 2: Sistema Multicanal Telefónico

**Contexto:** Un enlace de microondas debe transportar 12 canales telefónicos simultáneos.

**Comparación de esquemas:**

Con DSB-SC:
- BW por canal: 2 × 4 kHz = 8 kHz
- BW total: 12 × 8 = 96 kHz
- Separación entre canales: 1 kHz guardband
- BW total con guardbands: 107 kHz

Con SSB:
- BW por canal: 4 kHz
- BW total: 12 × 4 = 48 kHz
- Separación entre canales: 0.5 kHz guardband
- BW total con guardbands: 53.5 kHz

**Ahorro espectral:** 50% del ancho de banda

---

#### Ejemplo 3: Análisis de Potencia y SNR

**¿Qué pasa con la relación señal-ruido?**

Consideremos 100W de potencia transmitida:

DSB-SC:
- Potencia por banda lateral: 50W cada una
- En recepción, ambas bandas contribuyen al SNR

SSB:
- Toda la potencia (100W) en una sola banda
- Densidad espectral de potencia: doble que DSB

**Resultado sorprendente:** A pesar de usar la mitad del ancho de banda, SSB mantiene el mismo SNR que DSB-SC en detección coherente, porque:
- Menos ancho de banda = menos ruido admitido
- Mayor densidad espectral de señal
- Los efectos se compensan exactamente

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados
- **DSB-SC** (Carta 10): SSB es evolución de DSB-SC eliminando redundancia
- **Transformada de Hilbert** (Carta 8): Fundamental para generar SSB por método de fase
- **VSB** (Carta 15): Compromiso entre DSB y SSB
- **Receptor superheterodino** (Carta 12): Esencial para demodular SSB

#### Dependencias
1. Teoría de filtros → Necesario para método de filtrado
2. Señales analíticas → Base matemática del método de fase
3. Detección coherente → Único método viable de demodulación

#### Aplicaciones Posteriores
1. **QAM**: Usa principios similares en canales I/Q
2. **OFDM**: Cada subportadora puede modularse independientemente
3. **Radio definida por software**: SSB implementado digitalmente

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- SSB elimina redundancia espectral sin pérdida de información
- El trade-off entre eficiencia espectral y complejidad
- Por qué la detección coherente es absolutamente necesaria
- La importancia de la estabilidad de frecuencia en SSB

#### Tipos de problemas típicos
1. **Cálculo de ancho de banda**: Comparar BW de diferentes esquemas
2. **Diseño de sistemas multicanal**: Cuántos canales SSB caben en un BW dado
3. **Análisis espectral**: Dibujar espectros de USB y LSB
4. **Generación**: Explicar métodos de generación de SSB

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Pensar que SSB tiene mejor SNR que DSB**
- Por qué ocurre: Confusión con la eficiencia espectral
- Cómo evitarlo: Recordar que SNR depende de potencia total y BW de ruido
- Verdad: SSB y DSB-SC tienen mismo SNR con detección coherente ideal

❌ **Error #2: Creer que se puede detectar SSB con envolvente**
- Por qué ocurre: Analogía incorrecta con AM
- Cómo evitarlo: La envolvente de SSB no sigue la moduladora
- Excepción: SSB + portadora piloto permite detección cuasi-envolvente

❌ **Error #3: Ignorar requisitos de estabilidad de frecuencia**
- Por qué ocurre: No considerar efectos prácticos
- Cómo evitarlo: Un error de 100 Hz en el oscilador local causa distorsión audible
- Solución práctica: Osciladores de cristal, sintetizadores PLL

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
SSB: s(t) = m(t)cos(2πfct) ∓ m̂(t)sin(2πfct)
BW_SSB = fm (mitad de DSB)
USB: usa signo negativo
LSB: usa signo positivo
```

#### Conceptos Fundamentales
- ✓ **Eficiencia máxima**: Mejor uso posible del espectro para señales analógicas
- ✓ **Redundancia eliminada**: Una banda lateral contiene toda la información
- ✓ **Complejidad necesaria**: Precio a pagar por la eficiencia
- ✓ **Sincronización crítica**: Errores de frecuencia causan distorsión

#### Reglas Mnemotécnicas
- 🧠 **"USB resta, LSB suma"**: Para recordar signos en la fórmula
- 🧠 **"SSB = Mitad de todo"**: Mitad del BW, misma información

#### Valores Típicos
| Parámetro | Valor Típico | Aplicación |
|-----------|--------------|------------|
| BW canal voz SSB | 2.4-3 kHz | Radio HF |
| Estabilidad requerida | < ±50 Hz | Comunicaciones de voz |
| Supresión de portadora | > 40 dB | Transmisores comerciales |
| Supresión banda no deseada | > 60 dB | Especificación típica |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Haykin**: Capítulo 3.5 - Análisis matemático completo de SSB
- **ARRL Handbook**: Implementación práctica en equipos de radioaficionado
- **GNU Radio**: Bloques para experimentar con SSB en software

#### Temas Relacionados para Explorar
1. ISB (Independent Sideband): Dos canales SSB independientes
2. Compandores en SSB para mejorar SNR
3. Procesadores de voz para SSB
4. ALC (Control Automático de Nivel) en transmisores SSB

#### Preguntas para Reflexionar
- ¿Por qué SSB domina en HF pero no en VHF/UHF?
- ¿Cómo afecta el efecto Doppler a las comunicaciones SSB?
- ¿Sería posible hacer SSB para señales de video?
- ¿Qué pasaría si intentamos transmitir música de alta fidelidad por SSB?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 25 minutos
**Prerequisitos críticos**: DSB-SC, Transformada de Hilbert, filtrado
**Tags**: `#modulacion-lineal` `#ssb` `#blu` `#eficiencia-espectral` `#hf-communications`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*