---
tags:
  - wiki/modulacion-analogica
  - wiki/planificacion
curso: Sistemas de Comunicaciones
unidad: 3
---

# Modulación Lineal (AM / DSB-SC / SSB / VSB) — Formulario de examen

> **Last verified:** 2026-07-29 | **Verified by:** analysis + patrón real de ejercicios en `exercises/finales/md/`

> **61,9% de los 42 finales únicos** — empatado con FM como el tema individual más frecuente después de PCM. Conceptual completo en [[../derivaciones/modulacion-am|Derivación de AM]] y [[am-vs-dsb-sc|AM vs DSB-SC]].

## Glosario

| Símbolo | Nombre | Unidad |
|---|---|---|
| $A_c$ | Amplitud de **portadora** | V |
| $f_c$ | Frecuencia de portadora | Hz |
| $f_m$ | Frecuencia de la **moduladora** (mensaje) | Hz |
| $m$ | **Índice de modulación** ⚠️ *sin argumento* | adimensional, $\leq1$ |
| $m(t)$ | Moduladora **cruda** (con su amplitud $A_m$ adentro) | V |
| $m_n(t)$ | Moduladora **normalizada a pico 1** | adimensional |
| $k$ | Sensibilidad del modulador | 1/V |
| $R$ | Impedancia de carga | Ω (normalizada: $R=1$) |
| $CF$ | Factor de cresta $=$ pico/RMS | adimensional |
| $A_{max}, A_{min}$ | Máximo y mínimo de la **envolvente** | V |

> ⚠️ **Notación de la cátedra** (verificado sobre los finales): el índice es **$m$**, no $\mu$ ni $k_a$. La sensibilidad cruda es **$k$**. Ver [[../derivaciones/modulacion-am|Derivación de AM]].

## Las fórmulas

### Señal y espectro

$$\boxed{s_{AM}(t) = A_c\big[1+m\,m_n(t)\big]\cos(2\pi f_ct)}$$

$$\boxed{S_{AM}(f) = \tfrac{A_c}{2}\big[\delta(f{\mp}f_c)\big] + \tfrac{A_cm}{4}\big[\delta(f{\mp}f_c{\mp}f_m)\big] + \tfrac{A_cm}{4}\big[\delta(f{\mp}f_c{\pm}f_m)\big]}$$

**6 deltas**: 2 de portadora de altura $A_c/2$, 4 de bandas laterales de altura $A_cm/4$.

> ⚠️ **La trampa del factor 2**: las alturas de las deltas son **la mitad** de las amplitudes de los cosenos reales ($A_c$ y $A_cm/2$). Cada coseno real se reparte en dos exponenciales complejas.

### Índice de modulación

$$\boxed{m = \frac{k\,A_m}{A_c}} \qquad\qquad \boxed{m = \frac{A_{max}-A_{min}}{A_{max}+A_{min}}}$$

La segunda es la que se usa cuando dan **medidas de envolvente en el osciloscopio** (patrón muy frecuente).

### Ancho de banda

$$\boxed{BW_{AM} = BW_{DSB} = 2f_m} \qquad \boxed{BW_{SSB} = f_m} \qquad \boxed{BW_{VSB} = f_m+f_v}$$

**Multitono**: $BW = 2f_{m,max}$ — manda el **tono más agudo**, no la suma.

### Potencias

| Cantidad | Fórmula |
|---|---|
| Portadora | $\boxed{P_c = \dfrac{A_c^2}{2R}}$ |
| **Cada** banda lateral | $P_{SB} = \dfrac{A_c^2m^2}{8R} = \dfrac{P_c\,m^2}{4}$ |
| Total (un tono) | $\boxed{P_{total} = P_c\left(1+\dfrac{m^2}{2}\right)}$ |
| **Total (general)** | $\boxed{P_{total} = P_c\left[1+m^2\langle m_n^2\rangle\right]}$ |
| Con factor de cresta | $P_{total} = P_c\left[1+\dfrac{m^2}{CF^2}\right]$ |
| **Multitono** | $P_{total} = P_c\left(1+\dfrac{\sum_i m_i^2}{2}\right)$ |

### PEP, eficiencia y sobremodulación

$$\boxed{PEP = \frac{A_{max}^2}{2R} = P_c(1+m)^2} \qquad \boxed{\eta_{AM} = \frac{m^2}{2+m^2}}$$

$\eta_{max} = 1/3 = 33{,}3\%$ (con $m=1$). Para **DSB-SC y SSB**: $\eta = 100\%$.

**Sobremodulación** — el criterio correcto en multitono es sobre la **suma**:

$$\boxed{\sum_i m_i \leq 1} \qquad (\text{no cada } m_i \text{ por separado})$$

## Tabla comparativa (pregunta conceptual frecuente)

| | AM | DSB-SC | SSB | VSB |
|---|---|---|---|---|
| **BW** | $2f_m$ | $2f_m$ | $f_m$ | $f_m+f_v$ |
| **Eficiencia** | $\leq33\%$ | 100% | 100% | ~100% |
| **Portadora** | Sí | Suprimida | Suprimida | Sí (reducida) |
| **Detección** | Envolvente (barata) | Coherente | Coherente | Envolvente |
| **Transmite DC** | Sí | Sí | **No** | **Sí** |
| **Uso típico** | Radio AM, aviación | Enlaces punto a punto | HF, telefonía | **TV analógica** |

> **Por qué DSB-SC no puede usar detector de envolvente**: la envolvente de $A_cm(t)\cos(\omega_ct)$ es $A_c|m(t)|$ — el **valor absoluto**, que pierde el signo en cada cruce por cero. Ver [[am-vs-dsb-sc|AM vs DSB-SC]].

> **Por qué TV usa VSB y no SSB**: el video tiene contenido hasta continua, así que las bandas laterales se tocan en $f_c$ y no hay hueco donde el filtro pueda caer. Ver [[modulacion-vsb|VSB]].

## Los errores que cuestan puntos

1. **El factor 2 en el espectro** — alturas de delta $A_c/2$ y $A_cm/4$, no $A_c$ y $A_cm/2$
2. **Olvidar el factor de cresta** al calcular potencia desde una amplitud máxima
3. **Sobremodulación multitono**: el criterio es $\sum m_i\leq1$, no cada uno por separado
4. **Confundir $m$ (índice) con $m(t)$ (moduladora)** — mismo símbolo, cosas distintas
5. **$BW$ multitono**: es $2f_{m,max}$, no $2\sum f_{m,i}$

## Ver también

- [[../derivaciones/modulacion-am|Derivación completa de AM]] — potencia por dos métodos, PEP, espectro
- [[am-vs-dsb-sc|AM vs DSB-SC]] · [[modulacion-ssb|SSB]] · [[modulacion-vsb|VSB]]
- [[indice-modulacion-am|Índice de Modulación]]
- [[../../exercises/ejercicio-am-multitono-dia2|Ejercicio de práctica — AM multitono]] · [[../../exercises/autoevaluacion-am|Autoevaluación AM]]
- [[exponencial-formulario-examen|Formulario de FM/PM]] — el otro 61,9%
