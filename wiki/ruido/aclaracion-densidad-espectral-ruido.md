---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_07/aclaracion_densidad_espectral_ruido.md
curso: Sistemas de Comunicaciones
unidad: 7
---

# Aclaracion: Densidad Espectral de Ruido Termico

> **Last verified:** 2025-11-22 | **Verified by:** [source — [[../../explicaciones_anki/unidad_07/aclaracion_densidad_espectral_ruido]]]

## La aparente contradiccion

La carta 33 dice $N_0 = 4kT$ y la carta 34 dice $N = kTB$. **Ambas son correctas.** La confusion surge de la diferencia entre densidad espectral vs potencia total, representacion bilateral vs unilateral, y potencia disponible vs densidad de voltaje [source — [[../../explicaciones_anki/unidad_07/aclaracion_densidad_espectral_ruido]]].

## Tres formas de describir el ruido termico

### 1. Densidad Espectral de Voltaje (Bilateral)

$$\boxed{\overline{v_n^2} = 4kTRB}$$

La formula de Nyquist (1928) para el voltaje cuadratico medio en terminales de una resistencia R:
- El 4 aparece en la formula original
- Densidad por unidad de ancho de banda: $4kTR$ V²/Hz
- Valida para todo el espectro (frecuencias positivas y negativas)

Representacion bilateral: $S_v(f) = 2kTR$ para $-\infty < f < \infty$.

### 2. Potencia Disponible (lo que importa en comunicaciones)

$$\boxed{N_{disponible} = kTB}$$

Maxima potencia transferible a una carga adaptada ($R_L = R$). Derivacion:

$$P_{carga} = \frac{\overline{v_n^2}}{(R + R_L)^2} \times R_L = \frac{4kTRB}{(2R)^2} \times R = \frac{4kTRB}{4R} = kTB$$

**Clave**: El factor 4 en el numerador y $(2R)^2$ en el denominador se cancelan, dando el factor 1 en $kTB$ [source — [[../../explicaciones_anki/unidad_07/aclaracion_densidad_espectral_ruido]]].

### 3. Densidad Espectral Unilateral (convencion moderna)

$$\boxed{N_0 = kT \quad \text{[W/Hz]}}$$

**Dos convenciones:**
- **Convencion A (moderna, IEEE)**: $N_0 = kT$, solo frecuencias positivas, $N = N_0 B = kTB$
- **Convencion B (algunos textos clasicos)**: $N_0 = 2kT$, requiere factor 1/2 al integrar

## Convencion recomendada (estandar IEEE)

| Concepto | Formula | Unidades |
|----------|---------|----------|
| Voltaje de ruido (RMS²) | $\overline{v_n^2} = 4kTRB$ | V² |
| Densidad de voltaje | $4kTR$ | V²/Hz |
| Potencia disponible | $N = kTB$ | W |
| Densidad de potencia (unilateral) | $N_0 = kT$ | W/Hz |

## Ejemplo numerico (T = 290 K, B = 1 MHz, R = 50 Ω)

Desde voltaje: $\overline{v_n^2} = 4 \times 1.38\times10^{-23} \times 290 \times 50 \times 10^6 = 8.03\times10^{-13}$ V²
$$P_{disponible} = \frac{\overline{v_n^2}}{4R} = 4.0\times10^{-15} \text{ W}$$

Desde potencia: $N = kTB = 1.38\times10^{-23} \times 290 \times 10^6 = 4.0\times10^{-15}$ W ✅

Ambos metodos dan **-114 dBm**.

## Conclusion

No hay contradiccion entre las cartas 33 y 34:
- Carta 33 usa notacion de densidad espectral $N_0 = 4kT$
- Carta 34 usa potencia disponible directa $N = kTB$

La convencion moderna y recomendada es: $N_0 = kT$ y $N = kTB$ [analysis].

## Ver tambien

- [[../ruido/fuentes-ruido]] — Fuentes de ruido (carta 33)
- [[../ruido/temperatura-ruido]] — Temperatura equivalente de ruido (carta 34)
- [[../ruido/ruido-blanco-banda-angosta]] — Ruido blanco
- [[../ruido/ruido-termico]] — Ruido termico (stub)
- [[../ruido/factor-ruido-temperatura]] — Factor de ruido y temperatura
- [[../ruido/relacion-snr]] — Relacion Senal a Ruido
