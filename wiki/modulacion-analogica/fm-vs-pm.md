---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_04/carta_16_fm_vs_pm.md
curso: Sistemas de Comunicaciones
unidad: 4
---

# FM vs PM: Modulacion en Frecuencia y Fase

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_04/carta_16_fm_vs_pm]]]

## Definiciones

Ambas son modulaciones angulares (exponenciales) con **amplitud constante** [source — [[../../explicaciones_anki/unidad_04/carta_16_fm_vs_pm]]]:

### FM (Frequency Modulation)

La frecuencia instantanea varia directamente con $m(t)$:

$$\boxed{s_{FM}(t) = A_c\cos\left[2\pi f_c t + 2\pi k_f \int_{-\infty}^{t} m(\tau) d\tau\right]}$$

$$f_i(t) = f_c + k_f m(t)$$

donde $k_f$ = sensibilidad de frecuencia [Hz/V].

### PM (Phase Modulation)

La fase instantanea varia directamente con $m(t)$:

$$\boxed{s_{PM}(t) = A_c\cos[2\pi f_c t + k_p m(t)]}$$

$$\phi_i(t) = 2\pi f_c t + k_p m(t)$$

donde $k_p$ = sensibilidad de fase [rad/V].

## Relacion Fundamental

FM y PM estan intimamente relacionadas [source — [[../../explicaciones_anki/unidad_04/carta_16_fm_vs_pm]]]:

$$\boxed{\text{FM}[m(t)] \equiv \text{PM}\left[\int m(t) dt\right]}$$

$$\boxed{\text{PM}[m(t)] \equiv \text{FM}\left[\frac{dm(t)}{dt}\right]}$$

FM de $m(t)$ es equivalente a PM de la integral de $m(t)$ (y viceversa).

## Indice de Modulacion

Para moduladora sinusoidal $m(t) = A_m\cos(2\pi f_m t)$:

| Parametro | FM | PM |
|-----------|-----|-----|
| Indice | $\beta_{FM} = \frac{k_f A_m}{f_m} = \frac{\Delta f}{f_m}$ | $\beta_{PM} = k_p A_m$ |
| Dependencia de $f_m$ | Inversamente proporcional | **Independiente** |
| Unidades | Adimensional (radianes) | Radianes |

## Comportamiento Espectral

**FM**: $\beta_{FM}$ decrece con la frecuencia → las bajas frecuencias tienen mayor indice y ocupan mas espectro. FM naturalmente "comprime" el espectro de audio [source — [[../../explicaciones_anki/unidad_04/carta_16_fm_vs_pm]]].

**PM**: $\beta_{PM}$ constante → todas las frecuencias contribuyen igualmente al espectro. Esto hace que PM requiera pre-ecualizacion para señales de audio [analysis].

## Respuesta al Ruido

| Aspecto | FM | PM |
|---------|-----|-----|
| Ruido post-demodulacion | Crece con $f^2$ | Uniforme en frecuencia |
| Preenfasis/deenfasis | Muy efectivo | Menos necesario |
| Sensibilidad a ruido de fase | Moderada | Alta |

## Analogia del Automovil

- **FM es como controlar el velocimetro**: la señal controla la velocidad (frecuencia). La distancia recorrida (fase) es la integral de la velocidad [analysis].
- **PM es como controlar el odometro**: la señal controla la posicion (fase). La velocidad (frecuencia) es la derivada de la posicion [analysis].

## Aplicaciones

| Aplicacion | Modulacion | Razon |
|------------|-----------|--------|
| Radio FM broadcast | FM | Audio analogico, alta fidelidad |
| Walkie-talkies | FM (NBFM) | Robusto, simple |
| GPS | BPSK (PM digital) | Transiciones de fase precisas |
| WiFi | QAM (basado en PM) | Datos digitales, eficiencia espectral |
| Satelite TV | QPSK (PM) | Datos digitales, robusto |

## Ventajas y Desventajas

**FM**:
- ✓ Excelente rechazo al ruido (amplitud constante) [source — [[../../explicaciones_anki/unidad_04/carta_16_fm_vs_pm]]]
- ✓ Natural para audio analogico (favorece bajas frecuencias)
- ✗ Mayor ancho de banda (WBFM) [source — [[../../explicaciones_anki/unidad_04/carta_16_fm_vs_pm]]]
- ✗ Circuitos mas complejos (VCO lineal)

**PM**:
- ✓ Implementacion mas simple conceptualmente
- ✓ Transiciones precisas → ideal para datos digitales [source — [[../../explicaciones_anki/unidad_04/carta_16_fm_vs_pm]]]
- ✓ Base de PSK, QPSK, QAM [analysis]
- ✗ Sensible a ruido de fase y jitter

## Puntos Clave

- ✓ FM y PM son **matematicamente duales** (relacion integral/derivada) [source — [[../../explicaciones_anki/unidad_04/carta_16_fm_vs_pm]]]
- ✓ FM para audio analogico, PM para datos digitales [analysis]
- ✓ $\beta_{FM} \propto 1/f_m$, $\beta_{PM}$ = constante [source — [[../../explicaciones_anki/unidad_04/carta_16_fm_vs_pm]]]
- ✓ Amplitud constante en ambas (ventaja sobre AM) [source — [[../../explicaciones_anki/unidad_04/carta_16_fm_vs_pm]]]

## Ver tambien

- [[../modulacion-analogica/ancho-banda-carson]]
- [[../modulacion-analogica/fm-banda-angosta]]
- [[../modulacion-analogica/modulador-fm]]
- [[../derivaciones/modulacion-fm-carson]]
- [[../ruido/snr-modulacion-exponencial]]
- [[../../claude-conversations/2025-11-19_separaci-n-de-canales-fm-y-ancho-de-banda-real|Conversación: canales FM y ancho de banda real]]
- [[../../claude-conversations/2025-11-20_modulaci-n-bpsk-sobre-fm-en-telemetr-a-espacial|Conversación: BPSK sobre FM en telemetría]]
