# Aclaración: Densidad Espectral de Ruido Térmico

## La Aparente Contradicción entre Carta 33 y 34

### ¿Cuál es correcta?

**Carta 33** dice: $N_0 = 4kT$
**Carta 34** dice: $N = kTB$

**Respuesta: ¡Ambas son correctas!** La confusión surge de la diferencia entre:
1. **Densidad espectral** vs **Potencia total**
2. **Representación bilateral** vs **unilateral**
3. **Potencia disponible** vs **densidad de voltaje**

---

## Tres Formas de Describir el Ruido Térmico

### 1. Densidad Espectral de Voltaje (Bilateral)

$$\overline{v_n^2} = 4kTRB$$

**Contexto**: Voltaje de ruido medido en circuito abierto a través de resistencia R
- El **4** aparece en la fórmula de Nyquist original
- Es densidad por unidad de ancho de banda: $4kTR$ V²/Hz
- Válida para todo el espectro (frecuencias positivas y negativas)

**Representación bilateral**: $S_v(f) = 2kTR$ para $-\infty < f < \infty$

Integrando en ancho de banda B (de -B/2 a B/2):
$$\int_{-B/2}^{B/2} 2kTR \, df = 2kTR \times B$$

Potencia en resistencia R:
$$P = \frac{\overline{v_n^2}}{R} = \frac{2kTRB}{R} = 2kTB$$

Pero esta NO es la potencia disponible...

---

### 2. Potencia Disponible (lo que realmente importa)

$$N_{disponible} = kTB$$

**Contexto**: Máxima potencia transferible a una carga adaptada (RL = R)

**Derivación desde el voltaje:**

Circuito equivalente de Thévenin:
- Fuente de voltaje: $v_n$ (con $\overline{v_n^2} = 4kTRB$)
- Impedancia interna: R
- Carga: RL = R (adaptada)

Potencia transferida:
$$P_{carga} = \frac{\overline{v_n^2}}{(R + R_L)^2} \times R_L = \frac{4kTRB}{(2R)^2} \times R = \frac{4kTRB}{4R} = kTB$$

**Clave**: El factor 4 en el numerador y el (2R)² en el denominador se cancelan, dando el factor 1 en kTB.

---

### 3. Densidad Espectral Unilateral (Convención en Comunicaciones)

$$N_0 = 2kT \text{ o } N_0 = kT$$

**Dos convenciones comunes:**

#### Convención A (más común en libros modernos):
$$N_0 = \frac{kT}{1} = kT \quad \text{[W/Hz, solo freq. positivas]}$$

Potencia en ancho de banda B:
$$N = N_0 \times B = kTB$$

Esta convención es **directa y consistente** con la potencia disponible.

#### Convención B (usada en algunos textos clásicos):
$$N_0 = 2kT \quad \text{[W/Hz, solo freq. positivas]}$$

Potencia en ancho de banda B:
$$N = \frac{N_0}{2} \times B = \frac{2kT}{2} \times B = kTB$$

Aquí el factor 1/2 aparece al integrar.

---

## ¿Por qué la confusión con 4kT?

La fórmula histórica de **Nyquist (1928)** es:

$$\overline{v_n^2} = 4kTRB$$

Esta describe el **voltaje cuadrático medio** en los terminales de una resistencia.

Pero cuando hablamos de **densidad espectral de potencia disponible**, usamos:

$$N_0 = kT \quad \text{[W/Hz]}$$

**Relación entre ambas:**

Partiendo de $\overline{v_n^2} = 4kTRB$:

1. Densidad espectral de voltaje: $\frac{\overline{v_n^2}}{B} = 4kTR$ [V²/Hz]

2. Potencia disponible por Hz: $\frac{(4kTR)/4R}{1} = kT$ [W/Hz]

   (El factor 4R en denominador viene de la adaptación de impedancias)

---

## Resolución de la "Contradicción"

### Carta 33 (Ruido Blanco)

Cuando dice:
$$N_0 = 4kT$$

Se refiere a la densidad espectral **bilateral** donde:
- $S_n(f) = \frac{N_0}{2} = 2kT$ para $-\infty < f < \infty$
- Integrando solo frecuencias positivas (0 a B): $N = 2kT \times B$
- Integrando frecuencias positivas Y negativas (-B/2 a B/2): $N = 2kT \times B$

**Nota**: Esta convención es menos común y puede causar confusión.

### Carta 34 (Temperatura de Ruido)

Cuando dice:
$$N = kT_e B$$

Se refiere a la **potencia disponible** (convención unilateral moderna):
- $N_0 = kT$ [W/Hz] solo frecuencias positivas
- Potencia total en ancho de banda B: $N = N_0 \times B = kTB$

---

## Convención Recomendada (Estándar IEEE)

Para **evitar confusiones**, usa la convención moderna:

### Densidad espectral unilateral:
$$N_0 = kT \quad \text{[W/Hz]}$$

### Potencia total:
$$N = N_0 B = kTB \quad \text{[W]}$$

### Voltaje de ruido:
$$\overline{v_n^2} = 4kTRB \quad \text{[V²]}$$

### Potencia disponible (desde voltaje):
$$P_{disponible} = \frac{\overline{v_n^2}}{4R} = \frac{4kTRB}{4R} = kTB$$

---

## Tabla Comparativa

| Concepto | Fórmula | Unidades | Contexto |
|----------|---------|----------|----------|
| Voltaje de ruido (RMS²) | $\overline{v_n^2} = 4kTRB$ | V² | Circuito abierto |
| Densidad de voltaje | $4kTR$ | V²/Hz | Por unidad de BW |
| Potencia disponible | $N = kTB$ | W | Con carga adaptada |
| Densidad de potencia (unilateral) | $N_0 = kT$ | W/Hz | Convención moderna |
| Densidad bilateral | $S_n(f) = \frac{kT}{1} = kT$ | W/Hz | Frecuencias ± |

---

## Ejemplos Numéricos de Consistencia

### Caso: T = 290 K, B = 1 MHz, R = 50 Ω

#### Método 1: Desde voltaje
$$\overline{v_n^2} = 4 \times 1.38 \times 10^{-23} \times 290 \times 50 \times 10^6 = 8.03 \times 10^{-13} \text{ V}^2$$
$$v_{n,rms} = 0.896 \text{ μV}$$
$$P_{disponible} = \frac{\overline{v_n^2}}{4R} = \frac{8.03 \times 10^{-13}}{200} = 4.0 \times 10^{-15} \text{ W}$$

#### Método 2: Desde potencia disponible directa
$$N = kTB = 1.38 \times 10^{-23} \times 290 \times 10^6 = 4.0 \times 10^{-15} \text{ W}$$

✅ **Ambos métodos dan el mismo resultado: 4.0 × 10⁻¹⁵ W = -114 dBm**

---

## Puntos Clave para Recordar

### ✅ Reglas Claras:

1. **Voltaje de ruido**: Usa $\overline{v_n^2} = 4kTRB$ (el 4 viene de Nyquist)

2. **Potencia disponible**: Usa $N = kTB$ (independiente de R)

3. **Densidad espectral moderna**: Usa $N_0 = kT$ (unilateral, solo f > 0)

4. **Relación**: $N = \frac{\overline{v_n^2}}{4R} = \frac{4kTRB}{4R} = kTB$

### ⚠️ Cuidado con:

- **Convenciones antiguas**: Algunos textos usan $N_0 = 2kT$ o $N_0 = 4kT$ (bilateral)
- **Factor 2 vs 4**: Depende de si es densidad bilateral/unilateral y de voltaje/potencia
- **Temperatura de referencia**: Siempre verificar si se usa T₀ = 290 K o T₀ = 300 K

---

## Conclusión

**No hay contradicción entre las cartas 33 y 34:**

- Carta 33 usa notación de densidad espectral (posiblemente bilateral): $N_0 = 4kT$
- Carta 34 usa potencia disponible directa: $N = kTB$

Ambas son correctas si se interpretan en su contexto apropiado. La convención **moderna y recomendada** es:

$$\boxed{N_0 = kT \quad \text{y} \quad N = kTB}$$

Esta convención es más simple, directa y evita los factores de 2 o 4 que causan confusión.

---

**Generado**: 2025-11-22
**Propósito**: Aclarar confusiones comunes sobre densidad espectral de ruido térmico
