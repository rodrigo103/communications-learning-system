---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_07/carta_37_ruido-banda-angosta.md
curso: Sistemas de Comunicaciones
unidad: 7
---

# Ruido de Banda Angosta

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_07/carta_37_ruido-banda-angosta]]]

Cuando ruido blanco pasa a traves de un filtro pasabanda centrado en $f_c$ con ancho de banda $B \ll f_c$, el resultado es ruido de banda angosta. Este modelo es fundamental para analizar el comportamiento del ruido en receptores de comunicaciones.

## Condicion de banda angosta

La aproximacion es valida cuando:

$$B \ll f_c$$

El ruido resultante tiene una envolvente y fase que varian lentamente en comparacion con la portadora. [source — [[../../explicaciones_anki/unidad_07/carta_37_ruido-banda-angosta]]]

## Representacion en cuadratura (I-Q)

El ruido de banda angosta se expresa mediante componentes en fase y cuadratura:

$$\boxed{n(t) = x(t)\cos(2\pi f_c t) - y(t)\sin(2\pi f_c t)}$$

Donde:
- $x(t)$: componente en fase (in-phase)
- $y(t)$: componente en cuadratura (quadrature)

Ambas son procesos Gaussianos, independientes entre si, con igual varianza $\sigma^2 = N_0 B$. [source — [[../../explicaciones_anki/unidad_07/carta_37_ruido-banda-angosta]]]

## Representacion polar (envolvente y fase)

Alternativamente, en forma de envolvente $R(t)$ y fase $\phi(t)$:

$$\boxed{n(t) = R(t)\cos[2\pi f_c t + \phi(t)]}$$

donde:
$$R(t) = \sqrt{x^2(t) + y^2(t)}, \quad \phi(t) = \arctan\left(\frac{y(t)}{x(t)}\right)$$

## Distribuciones estadisticas

### Envolvente: Distribucion de Rayleigh

La envolvente $R$ sigue una distribucion de Rayleigh:

$$\boxed{p_R(r) = \frac{r}{\sigma^2}\exp\left(-\frac{r^2}{2\sigma^2}\right)}, \quad r \geq 0$$

### Fase: Distribucion uniforme

La fase $\phi$ es uniforme e independiente de la envolvente:

$$\boxed{p_\phi(\phi) = \frac{1}{2\pi}}, \quad 0 \leq \phi < 2\pi$$

## Importancia en sistemas de comunicaciones

El modelo de ruido de banda angosta es esencial para:

- **Analisis de deteccion de envolvente:** como el ruido afecta a demoduladores no coherentes
- **Efecto umbral en FM:** por que la deteccion de envolvente se degrada abruptamente a baja SNR
- **Analisis de BER en modulaciones digitales:** especialmente en canales con desvanecimiento Rayleigh
- **Relacion con senal analitica y transformada de Hilbert:** la representacion en cuadratura es la base del equivalente paso-bajo

[analysis]

## SNR alta vs baja

- **SNR alta:** la deteccion de envolvente se aproxima a la deteccion coherente, con degradacion despreciable
- **SNR baja:** aparece el **efecto umbral** — la deteccion de envolvente se degrada bruscamente; la senal es capturada por el ruido

Este comportamiento es clave para entender por que FM tiene efecto umbral y AM no (en deteccion coherente). [analysis]

## Ver también

- [[../ruido/ruido-blanco-banda-angosta]] — Ruido blanco
- [[../ruido/fuentes-ruido]] — Fuentes de ruido
- [[../ruido/efecto-umbral]] — Efecto umbral
- [[../herramientas-matematicas/densidad-espectral-potencia]] — Densidad espectral de potencia
- [[../herramientas-matematicas/transformada-hilbert]] — Transformada de Hilbert
- [[../modulacion-digital/probabilidad-error]] — Probabilidad de error (BER)
