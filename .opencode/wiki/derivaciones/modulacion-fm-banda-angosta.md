---
tags:
  - wiki/derivaciones
  - wiki/modulacion-analogica
source_file: outputs/derivations/FM_Narrowband_20251115.md
curso: Sistemas de Comunicaciones
unidad: 4
---

# Derivación de FM de Banda Angosta (NBFM)

> **Last verified:** 2025-11-15 | **Verified by:** source

## Condición de banda angosta

**Narrowband FM (NBFM)** ocurre cuando el índice de modulación es muy pequeño:

$$\boxed{\beta \ll 1}$$

Típicamente $\beta < 0.3$ (criterio estricto). Esto significa que la desviación de frecuencia es mucho menor que la frecuencia del mensaje: $\Delta f \ll f_m$ [source].

## Punto de partida

Señal FM con mensaje sinusoidal $m(t) = A_m \cos(2\pi f_m t)$:

$$s_{FM}(t) = A_c \cos[2\pi f_c t + \beta \sin(2\pi f_m t)]$$

donde $\beta = \frac{\Delta f}{f_m} = \frac{k_f A_m}{f_m}$.

## Aproximación de ángulo pequeño

Usando la identidad $\cos(\alpha + \theta) = \cos\alpha\cos\theta - \sin\alpha\sin\theta$:

$$s_{FM}(t) = A_c[\cos(2\pi f_c t)\cos(\beta \sin(2\pi f_m t)) - \sin(2\pi f_c t)\sin(\beta \sin(2\pi f_m t))]$$

Para $\beta \ll 1$, aplicamos las aproximaciones de Taylor [analysis]:

$$\cos(\beta \sin(2\pi f_m t)) \approx 1$$
$$\sin(\beta \sin(2\pi f_m t)) \approx \beta \sin(2\pi f_m t)$$

Sustituyendo:

$$\boxed{s_{NBFM}(t) = A_c \cos(2\pi f_c t) - A_c \beta \sin(2\pi f_c t) \sin(2\pi f_m t)}$$

## Expansión espectral

Usando $\sin A \sin B = \frac{1}{2}[\cos(A-B) - \cos(A+B)]$:

$$\boxed{s_{NBFM}(t) = A_c \cos(2\pi f_c t) + \frac{A_c \beta}{2}\cos(2\pi(f_c + f_m)t) - \frac{A_c \beta}{2}\cos(2\pi(f_c - f_m)t)}$$

### Tres componentes espectrales

1. **Portadora:** $f_c$, amplitud $A_c$, fase $0°$
2. **USB:** $f_c + f_m$, amplitud $\frac{A_c \beta}{2}$, fase $0°$
3. **LSB:** $f_c - f_m$, amplitud $\frac{A_c \beta}{2}$, fase $180°$ (signo negativo)

## Comparación con AM

| Característica | AM | NBFM |
|---|---|---|
| USB | $+\frac{A_c \mu}{2}$ | $+\frac{A_c \beta}{2}$ |
| LSB | $+\frac{A_c \mu}{2}$ | $-\frac{A_c \beta}{2}$ |

**Diferencia crucial:** En NBFM, la LSB está desfasada 180° respecto a la portadora, mientras que en AM ambas bandas están en fase [analysis]. Este desfasaje produce:

- **Amplitud constante** en FM (las variaciones de amplitud se cancelan)
- La información está codificada en la fase, no en la amplitud

## Ancho de banda

$$\boxed{BW_{NBFM} = 2f_m}$$

Idéntico al ancho de banda de AM. Esto hace que NBFM sea espectralmente eficiente, pero sacrifica la principal ventaja de FM (gran mejora de SNR) que solo se obtiene con banda ancha ($\beta \gg 1$) [analysis].

## Distribución de potencia

- $P_c = \frac{A_c^2}{2R}$
- $P_{SB} = \frac{A_c^2 \beta^2}{8R}$
- $P_{total} \approx \frac{A_c^2}{2R}$ (aproximadamente toda en la portadora)

Eficiencia: $\eta \approx \frac{\beta^2}{2}$ — para $\beta = 0.2$, solo 2% (peor que AM) [analysis].

## Resumen de fórmulas

**Forma compacta:**
$$\boxed{s_{NBFM}(t) = A_c \cos(2\pi f_c t) - A_c \beta \sin(2\pi f_c t) \sin(2\pi f_m t)}$$

**Forma expandida:**
$$\boxed{s_{NBFM}(t) = A_c \cos(2\pi f_c t) + \frac{A_c \beta}{2}\cos(2\pi(f_c + f_m)t) - \frac{A_c \beta}{2}\cos(2\pi(f_c - f_m)t)}$$

## Generación y aplicaciones

- **Método de Armstrong:** generar NBFM con modulador de fase + integrador
- **Multiplicadores de frecuencia:** NBFM puede expandirse a WBFM mediante multiplicación ($\beta_{out} = N \cdot \beta_{in}$)
- Aplicaciones: comunicaciones móviles de banda estrecha, radio amateur, etapa inicial de transmisores WBFM

## Ver también

- [[modulacion-analogica/fm-banda-angosta]]
- [[modulacion-analogica/fm-vs-pm]]
- [[derivaciones/modulacion-fm-carson]]
- [[modulacion-analogica/modulador-armstrong]]
- [[modulacion-analogica/fm-banda-ancha]]
