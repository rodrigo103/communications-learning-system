---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_07/carta_35_figura-factor-ruido.md
curso: Sistemas de Comunicaciones
unidad: 7
---

# Factor de Ruido y Temperatura Equivalente

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_07/carta_35_figura-factor-ruido]]]

## Figura de Ruido ($F$)

La figura de ruido mide cuánto degrada un dispositivo la relación señal-ruido:

$$\boxed{F = \frac{SNR_{entrada}}{SNR_{salida}} = \frac{S_i/N_i}{S_o/N_o}}$$

- $F = 1$: dispositivo ideal, sin ruido agregado
- $F > 1$: el dispositivo agrega ruido
- $F$ es adimensional (lineal) [source — [[../../explicaciones_anki/unidad_07/carta_35_figura-factor-ruido]]]

### Factor de Ruido ($NF$)

Es la misma magnitud expresada en dB:

$$\boxed{NF = 10\log_{10}(F) \text{ dB}}$$

**Valores típicos:**
| Dispositivo | NF típico | Aplicación |
|-------------|-----------|------------|
| LNA GaAs | 0.5–1.5 dB | Satélite, radar |
| LNA Silicon | 2–4 dB | WiFi, celular |
| Mezclador | 6–10 dB | Conversión de frecuencia |
| Cable coaxial | 0.2 dB/m @ 1 GHz | Interconexión |

## Temperatura Equivalente de Ruido ($T_e$)

Cualquier fuente de ruido puede caracterizarse por una temperatura equivalente $T_e$: [source — [[../../explicaciones_anki/unidad_07/carta_35_figura-factor-ruido]]]

$$\boxed{T_e = T_0(F - 1)}$$

donde $T_0 = 290$ K (temperatura de referencia estándar).

Recíprocamente:

$$\boxed{F = 1 + \frac{T_e}{T_0}}$$

La potencia de ruido agregada (referida a la entrada) es:

$$N_{agregado} = kT_e B$$

## Relación con la Potencia de Ruido

**Modelo de amplificador real:**

$$N_{out} = G \cdot N_{in} + G \cdot kT_e B$$

La figura de ruido se relaciona directamente con el ruido agregado:

$$F = 1 + \frac{N_{agregado}}{G \cdot N_{in}}$$

### De Voltaje a Potencia

La fórmula de Nyquist para voltaje de ruido es $v_n^2 = 4kTRB$. La potencia **disponible** (con carga adaptada) es $N = kTB$. El factor 4 se cancela al dividir por $4R$ en la adaptación de impedancias. [source — [[../../explicaciones_anki/unidad_07/carta_35_figura-factor-ruido]]]

## Temperatura del Sistema

Para un sistema completo:

$$\boxed{T_{sys} = T_{antena} + T_{receptor}}$$

Donde $T_{antena}$ incluye ruido cósmico, atmosférico y terrestre. Minimizar $T_{sys}$ maximiza la sensibilidad.

## Ver también

- [[../ruido/formula-friis]] — Cálculo de ruido en cascada
- [[../ruido/relacion-snr]] — Relación señal-ruido
- [[../ruido/ruido-blanco-banda-angosta]] — $N_0 = kT$ como referencia
