# Separación de canales FM y ancho de banda real

**Fecha:** 2025-11-19

**Rodrigo** (2025-11-19 05:07:42):

En mi país, al sintonizar FM tenemos la estación 99,9 MHz y la 100,1 MHz, es decir, tenemos 200 kHz de diferencia que entiendo que es el ancho de banda de cada estación. Por que tan grande si solo se necesitan 40kHz?

---

**Claude** (2025-11-19 05:08:16):

Excelente observación que toca un punto clave del diseño de sistemas reales. La diferencia entre lo que "necesitas teóricamente" y lo que "asignas en la práctica" tiene varias razones fundamentales:

## El ancho de banda real de FM estéreo

Primero, esos "40 kHz" que mencionás subestiман considerablemente el ancho de banda real. Para FM broadcasting estéreo:

**Por la regla de Carson:**
$$BW = 2(\Delta f + f_m)$$

Donde:
- Δf = 75 kHz (desviación máxima de frecuencia, norma internacional)
- f_m ≈ 53 kHz (señal multiplex estéreo completa: audio hasta 15 kHz + tono piloto 19 kHz + L-R en 38 kHz + subportadoras RDS/RDBS)

Esto da: **BW ≈ 2(75 + 53) = 256 kHz**

Incluso si considerás solo el audio principal (15 kHz):
$$BW = 2(75 + 15) = 180 \text{ kHz}$$

## ¿Por qué entonces 200 kHz de separación?

Acá viene la ingeniería del mundo real:

**1. Bandas de guarda**
Los 200 kHz asignados incluyen la señal (≈180 kHz) MÁS espacios de guarda a ambos lados para evitar interferencia entre canales adyacentes. Sin estas bandas de guarda, las estaciones se pisarían mutuamente.

**2. Imperfecciones de los transmisores**
Los osciladores reales no son perfectamente estables. Derivan en frecuencia por temperatura, envejecimiento de componentes, etc. Ese "colchón" extra absorbe estas variaciones.

**3. Imperfecciones de los receptores**
Los filtros de los receptores domésticos no tienen flancos infinitamente pronunciados. Necesitás ese espacio extra para que un filtro real pueda discriminar entre canales sin dejar pasar el canal adyacente.

**4. Compromiso económico-regulatorio**
200 kHz permite empaquetar aproximadamente 100 estaciones en la banda de FM (88-108 MHz). Es un balance entre:
- Cantidad de emisoras que podés licenciar (ingresos regulatorios, diversidad de contenidos)
- Calidad técnica suficiente (baja interferencia)
- Costo razonable de equipos tx/rx

## La decisión histórica

Esta separación de 200 kHz se estandarizó en los años 1940s-1960s cuando se definió FM broadcasting. Es otro ejemplo de cómo **las decisiones de ingeniería optimizan múltiples restricciones simultáneas**: espectro disponible, tecnología de la época, economía regulatoria, y márgenes de seguridad para operación confiable.

¿Querés que profundicemos en cómo se calculó ese ancho de banda de 256 kHz considerando toda la señal multiplex estéreo?

> [!note]- Thinking
> El usuario está preguntando sobre las bandas de FM comercial. Veamos:
> 
> 1. Observa que las estaciones FM están separadas por 200 kHz (de 99.9 MHz a 100.1 MHz)
> 2. Pregunta por qué esta separación es tan grande si "solo se necesitan 40 kHz"
> 
> Esto es una excelente pregunta que refleja su enfoque característico de cuestionar decisiones de diseño de sistemas. Necesito explicar:
> 
> 1. El ancho de banda real de una señal FM
> 2. Por qué se asignan canales de 200 kHz
> 3. La diferencia entre ancho de banda necesario vs ancho de banda asignado
> 4. Las bandas de guarda
> 
> Primero, calculemos el ancho de banda de FM Broadcasting:
> - Para FM estéreo comercial típicamente:
>   - Frecuencia modulante máxima fm = 15 kHz (señal estéreo compleja con piloto en 19 kHz y L-R en 38 kHz, puede llegar hasta ~53 kHz considerando RDS)
>   - Desviación de frecuencia Δf = 75 kHz (norma para FM broadcasting)
>   - Por regla de Carson: BW = 2(Δf + fm) = 2(75 + 15) = 180 kHz
> 
> Pero considerando todo el contenido estéreo multiplex (hasta ~53 kHz), sería:
> BW = 2(75 + 53) = 256 kHz aproximadamente
> 
> Sin embargo, la norma asigna canales de 200 kHz.
> 
> El comentario del usuario de "40 kHz" probablemente viene de:
> - Si solo consideráramos señal mono de 15 kHz con desviación menor, o
> - Si estuviera pensando en el ancho de banda de la señal modulante (15 kHz × 2 = 30 kHz para audio estéreo)
> 
> 
> - O quizás confundiendo con otros estándares
> 
> Posiblemente hay diferentes estándares internacionales que explican esta variación en la percepción del ancho de banda necesario. La separación de 200 kHz permite márgenes de seguridad para evitar interferencias entre canales adyacentes, garantizando una recepción de señal más limpia y estable.

---

**Rodrigo** (2025-11-20 04:04:53):

Entonces en la práctica se usan 256 kHz o 180 kHz

---

**Claude** (2025-11-20 04:05:36):

Buena pregunta, necesito ser más preciso porque mezclé conceptos. Aquí está la realidad:

## En la práctica se usan aproximadamente **180 kHz**

La confusión viene de cómo aplico la regla de Carson. Dejame corregir:

**Para el cálculo estándar de FM broadcast se usa:**
- Δf = 75 kHz (desviación máxima)
- fm = **15 kHz** (frecuencia máxima del audio que modula)

$$BW_{Carson} = 2(\Delta f + f_m) = 2(75 + 15) = 180 \text{ kHz}$$

## ¿Y los 256 kHz que mencioné?

Eso fue un error de mi parte al usar fm = 53 kHz. Aunque la señal multiplex estéreo *contiene* componentes hasta ~53 kHz (con L-R modulada en 38 kHz), la **desviación de frecuencia** está dominada por el contenido de audio base (0-15 kHz), que es donde está la mayor energía de la señal modulante.

La regla de Carson pregunta: "¿qué frecuencia moduladora causa la mayor desviación?" Y esa es el audio de baja frecuencia/alta amplitud, no las subportadoras de estéreo que tienen menor amplitud.

## El esquema real entonces:

```
|←────────── 200 kHz asignados ──────────→|
|←── ~10 kHz ──→|← 180 kHz señal →|←~10 kHz→|
    (guarda)      (FM estéreo)     (guarda)
```

**180 kHz** es lo que la señal FM estéreo realmente ocupa, y los **200 kHz de separación** te dan ~20 kHz total (10 kHz a cada lado) de bandas de guarda para absorber las imperfecciones que mencioné antes.

Gracias por la pregunta que me hizo aclarar esto correctamente.

> [!note]- Thinking
> El usuario me pide aclarar qué ancho de banda se usa en la práctica para FM broadcasting. Debo ser preciso porque hay diferentes conceptos en juego:
> 
> 1. Ancho de banda OCUPADO por la señal transmitida
> 2. Ancho de banda ASIGNADO/CANALIZADO (channel spacing)
> 3. Lo que se calcula por Carson
> 
> Revisemos:
> 
> Para FM estéreo:
> - Δf = 75 kHz (desviación máxima)
> - La señal moduladora en estéreo es compleja:
>   - L+R (audio mono): 0-15 kHz
>   - Tono piloto: 19 kHz
>   - L-R (diferencia estéreo) modulada en DSB-SC: centrada en 38 kHz (2×19), con bandas laterales de ±15 kHz, por lo que ocupa de 23 a 53 kHz
>   - Opcionalmente RDS/RBDS en 57 kHz
> 
> Entonces fm máximo es aproximadamente 53 kHz (si no consideramos RDS) o incluso un poco más.
> 
> Por Carson:
> BW = 2(Δf + fm) = 2(75 + 53) = 256 kHz
> 
> PERO, en la PRÁCTICA regulatoria:
> - El channel spacing (separación entre canales) es 200 kHz
> - Esto significa que cada estación tiene "asignados" 200 kHz
> - La señal real ocupa aproximadamente 180-200 kHz del espectro
> 
> La aparente contradicción se resuelve así:
> - Carson da una aproximación que contiene ~98% de la potencia
> - La regla de Carson usa fm como la máxima frecuencia moduladora significativa
> - En la práctica, la señal se atenúa en los extremos y "cabe" dentro de los 200 kHz asignados
> 
> 
> - Las normas regulatorias establecen máscaras espectrales estrictas que limitan la emisión dentro del canal asignado
> - Esto garantiza que la señal se mantenga dentro de los 200 kHz, controlando las emisiones en los bordes del espectro
> - Usando fm=15 kHz para el audio principal, el ancho de banda calculado coincide precisamente con los 200 kHz reglamentarios

---

**Rodrigo** (2025-11-20 04:07:08):

Hablame mas de la señal multiplex fm completa

---

**Claude** (2025-11-20 04:07:54):

Perfecto, esto es fascinante porque es un ejemplo brillante de ingeniería que resuelve múltiples problemas simultáneamente.

## El problema original

En los años 1960s existía **FM mono** funcionando (con millones de receptores en uso). ¿Cómo agregar estéreo manteniendo compatibilidad hacia atrás? Es decir:
- Receptores viejos mono deben seguir funcionando
- Receptores nuevos estéreo deben recibir L y R separados

## La solución elegante: suma y diferencia

En lugar de transmitir L y R directamente, se transmite:
- **L+R**: señal de suma (mono compatible)
- **L-R**: señal de diferencia (info estéreo)

**¿Por qué funciona?** Matemáticamente:
$$L = \frac{(L+R) + (L-R)}{2}$$
$$R = \frac{(L+R) - (L-R)}{2}$$

Un receptor mono captura solo (L+R) y reproduce ambos canales mezclados. Un receptor estéreo captura ambas señales y recupera L y R separados.

## Estructura de la señal multiplex completa

La señal que **modula en frecuencia** a la portadora de FM (por ejemplo, 99.9 MHz) es:

```
Señal Multiplex = (L+R) + Piloto + (L-R)modulada + RDS

En frecuencia:
─────────────────────────────────────────────────
0        15 kHz   19    23      38      53 kHz
├─────────┤        │     ├───────┼───────┤
   L+R          Piloto      L-R en DSB-SC    RDS
 (mono)        (19 kHz)    (portadora 38kHz)
```

**Componentes:**

**1. L+R (0-15 kHz)**: Audio mono, banda base
- Compatible con receptores viejos
- Contiene toda la información si ignorás el resto

**2. Tono piloto (19 kHz)**: Señal sinusoidal pura
- Referencia de fase para demodular L-R
- Es exactamente **la mitad** de 38 kHz (crucial para la demodulación)

**3. L-R en DSB-SC (23-53 kHz)**: Información estéreo
- **DSB-SC**: Double Sideband Suppressed Carrier (portadora suprimida)
- Centrada en 38 kHz (= 2 × 19 kHz)
- Ocupa ±15 kHz alrededor de 38 kHz: [23, 53] kHz
- Modulación AM con portadora suprimida (recordá Unidad 3)

**4. RDS/RBDS (57 kHz)**: Data digital opcional
- Información de texto (nombre emisora, canción, etc.)
- Modulación PSK de baja velocidad

## ¿Por qué esta estructura?

**Separación en frecuencia (FDM)**
Es **Frequency Division Multiplex** - cada componente ocupa su propia banda sin superponerse:
- Mono: 0-15 kHz
- Piloto: 19 kHz (línea espectral pura)
- Estéreo: 23-53 kHz
- RDS: 57 kHz

**Ortogonalidad**
Las frecuencias están relacionadas armónicamente (19, 38, 57 kHz = n×19 kHz), lo que facilita la generación y demodulación con PLLs.

**Uso eficiente del espectro**
DSB-SC para L-R es eficiente: no desperdicias potencia en portadora (que no lleva información), solo transmitís las bandas laterales.

## En el transmisor FM

```
Audio L ─┐
         ├─→ [Σ] ──→ L+R ──┐
Audio R ─┘                  │
                            ├─→ [Sumador] ──→ Señal Multiplex ──→ [Modulador FM]
Audio L ─┐                  │                                            ↓
         ├─→ [-] ──→ L-R ──→ [Modulador balanceado 38kHz] ────────────────→ RF out
Audio R ─┘                        ↑                         │
                                  │                         │
                     [Oscilador 19 kHz] ──→ [×2] ──────────┤
                            │                               │
                            └───────────────────────────────┘
                                    (piloto)
```

## En el receptor FM estéreo

Después del discriminador FM obtenés la señal multiplex:

```
Señal Multiplex ─┬─→ [Filtro pasa-bajos 0-15kHz] ──→ L+R
                 │
                 ├─→ [Filtro pasabanda 23-53kHz] ──→ [Demod. síncrona] ──→ L-R
                 │                                          ↑
                 └─→ [PLL en 19 kHz] ──→ [×2] ──→ 38 kHz ──┘
```

El PLL (Phase-Locked Loop) **engancha** con el piloto de 19 kHz, lo duplica a 38 kHz, y usa esa referencia coherente para demodular síncronamente L-R (que recordá, es DSB-SC).

Finalmente:
```
L = (L+R) + (L-R)
        2

R = (L+R) - (L-R)
        2
```

## El detalle crucial de la desviación

Cuando mencioné antes Δf = 75 kHz, ese es el **total** de desviación permitida. Pero está **distribuido** entre componentes:

- L+R causa ~90% de la desviación (tiene la mayor amplitud)
- L-R causa menor desviación (se transmite con ~50% de amplitud de L+R)
- Piloto: solo ~10% de desviación

Por eso en Carson usamos fm = 15 kHz (el audio base), porque es quien más desvía la portadora.

## ¿Por qué todo este trabajo?

Esta arquitectura logra:
✓ **Compatibilidad**: receptores mono siguen funcionando
✓ **Separación estéreo**: L y R independientes en receptores nuevos
✓ **Eficiencia espectral**: todo cabe en ~180 kHz
✓ **Referencia de fase**: el piloto permite demodulación coherente
✓ **Escalabilidad**: se pudo agregar RDS después sin romper nada

Es un diseño que equilibra restricciones técnicas, económicas (no obsoletizar receptores existentes) y regulatorias (caber en 200 kHz asignados).

¿Querés que profundicemos en la demodulación síncrona de DSB-SC, o en cómo el PLL recupera la portadora suprimida?

> [!note]- Thinking
> Rodrigo quiere entender en profundidad la señal multiplex de FM estéreo. Esto es perfecto para su estilo de aprendizaje - quiere entender desde los fundamentos cómo funciona realmente el sistema.
> 
> Déjame explicar la señal multiplex FM estéreo desde los principios fundamentales:
> 
> 1. El problema original: cómo transmitir dos canales (L y R) siendo compatible con receptores mono
> 2. La solución elegante usando suma y diferencia
> 3. La estructura completa de la señal multiplex
> 4. Por qué está diseñada así (compatibilidad, ortogonalidad, uso eficiente del espectro)
> 
> Necesito ser preciso con las frecuencias y la estructura, y conectarlo con los conceptos que ya vimos de modulación.

---

