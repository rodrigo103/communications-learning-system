---
tags:
  - wiki/resumen
  - wiki/modulacion-digital
source_file: outputs/mindmaps/unit_6_digital_modulation_detailed_20251116.md
curso: Sistemas de Comunicaciones
unidad: 6
---

# Resumen Unidad 6: Modulación Digital

> **Last verified:** 2025-11-16 | **Verified by:** source

## Fundamentos teóricos

### Representación en espacio de señales
Cada símbolo se representa como combinación lineal de bases ortonormales:
$$s(t) = \sum_n a_n \phi_n(t), \quad \langle \phi_i, \phi_j \rangle = \delta_{ij}$$

### Constelaciones
Diagrama I-Q donde cada punto representa un símbolo. La distancia euclidiana entre puntos determina la inmunidad al ruido. [[../modulacion-digital/constelaciones]]

**Codificación Gray:** símbolos adyacentes difieren en 1 bit → minimiza BER por errores de símbolo [source — [[../../outputs/mindmaps/unit_6_digital_modulation_detailed_20251116]]].

### Criterio de Nyquist
Condición de ISI cero: pulsos con cruces por cero en $t = nT$. El filtro de coseno realzado (roll-off $\alpha$) cumple esta condición.

## Esquemas de modulación

### ASK — Amplitude Shift Keying
Varía la amplitud de la portadora. OOK (On-Off Keying): $s_0(t) = 0$, $s_1(t) = A\cos(2\pi f_c t)$.
- Simple, susceptible a ruido
- Usado en fibra óptica
- M-ASK: $M$ niveles de amplitud

### FSK — Frequency Shift Keying
Varía la frecuencia: $s_0(t) = A\cos(2\pi f_0 t)$, $s_1(t) = A\cos(2\pi f_1 t)$.
- Ortogonalidad: $\Delta f = n/(2T_b)$
- Envolvente constante (apto para amplificadores no lineales)
- MSK: $\Delta f = 1/(4T_b)$, fase continua
- GMSK: filtro gaussiano, usado en GSM ($BT = 0.3$)

### PSK — Phase Shift Keying
Varía la fase de la portadora:
- **BPSK:** 2 fases (0°, 180°), $P_e = Q(\sqrt{2E_b/N_0})$
- **QPSK:** 4 fases, 2 bits/símbolo, $\eta \approx 2$ bits/s/Hz
- **OQPSK:** I-Q desfasados $T_b/2$, reduce variación de envolvente
- **$\pi/4$-QPSK:** codificación diferencial, usado en TDMA
- **8-PSK:** 3 bits/símbolo, $\eta \approx 3$ bits/s/Hz
- **DPSK:** detección sin referencia de fase, ~3 dB de penalización

### QAM — Quadrature Amplitude Modulation
Modula amplitud y fase simultáneamente en dos portadoras en cuadratura:
$$s(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)$$

| QAM | Grid | bits/símbolo | $\eta$ (bits/s/Hz) |
|-----|------|-------------|---------------------|
| 16-QAM | 4×4 | 4 | 4 |
| 64-QAM | 8×8 | 6 | 6 |
| 256-QAM | 16×16 | 8 | 8 |
| 1024-QAM | 32×32 | 10 | 10 |

Ver [[../derivaciones/modulacion-qam]].

## Análisis de desempeño

### Probabilidad de error (BER)

| Modulación | $P_e$ (coherente) |
|------------|-------------------|
| BPSK | $Q(\sqrt{2E_b/N_0})$ |
| QPSK | $\approx Q(\sqrt{2E_b/N_0})$ |
| M-PSK | $\approx Q(\sqrt{2E_b/N_0}\sin(\pi/M))$ |
| M-QAM | $\approx 4Q(\sqrt{3E_b/[(M-1)N_0]})$ |
| FSK coherente | $Q(\sqrt{E_b/N_0})$ |
| FSK no coherente | $\frac{1}{2}e^{-E_b/2N_0}$ |

### Eficiencia espectral
$$\eta = \frac{R_b}{B} \text{ bits/s/Hz}$$

| Esquema | $\eta$ típica |
|---------|---------------|
| BPSK | 1 |
| QPSK | 2 |
| 8-PSK | 3 |
| 16-QAM | 4 |
| 64-QAM | 6 |
| 256-QAM | 8 |

### Eficiencia de potencia ($E_b/N_0$ para BER = $10^{-5}$)

| Modulación | $E_b/N_0$ requerido |
|------------|---------------------|
| BPSK/QPSK | ~10.5 dB |
| 8-PSK | ~14 dB |
| 16-QAM | ~14.5 dB |
| 64-QAM | ~18.5 dB |

**Trade-off fundamental:** mayor orden M → mejor $\eta$, pero peor $P_e$ para el mismo $E_b/N_0$ [analysis].

### Relaciones clave
$$R_b = R_s \cdot \log_2(M), \quad \frac{E_b}{N_0} = \frac{S}{N} \cdot \frac{B}{R_b}$$

[[../modulacion-digital/probabilidad-error]]

## Filtrado de pulsos e ISI

### Coseno realzado (Raised Cosine)
$$H(f) = \begin{cases} T & |f| \leq \frac{1-\alpha}{2T} \\ \frac{T}{2}[1+\cos(\frac{\pi(|f|-\beta)}{\alpha})] & \beta < |f| < \frac{1}{2T} \end{cases}$$

- $\alpha \in [0,1]$: roll-off factor
- $\alpha = 0$: Nyquist ideal (sinc), $\alpha = 1$: 100% exceso de BW
- Ancho de banda: $B = (1+\alpha)/(2T)$
- Root Raised Cosine: TX y RX usan $\sqrt{H(f)}$, combinados = RC

### Diagrama de ojo
Herramienta de visualización: apertura indica margen de ruido, cierre indica ISI.

[[../modulacion-digital/codificacion-linea]]

## Aplicaciones

| Sistema | Modulación |
|---------|-----------|
| GSM (2G) | GMSK |
| 3G UMTS | QPSK, 16-QAM |
| 4G LTE | hasta 256-QAM |
| 5G NR | hasta 256-QAM |
| WiFi 802.11b | BPSK, QPSK |
| WiFi 802.11ac | hasta 256-QAM |
| WiFi 6 (802.11ax) | 1024-QAM |
| DVB-S2 (satélite) | QPSK, 8PSK, 16/32APSK |
| DOCSIS 3.1 (cable) | hasta 4096-QAM |
| Bluetooth | GFSK, $\pi/4$-DQPSK |

## Ver también

- [[../modulacion-digital/ask-fsk-psk]]
- [[../modulacion-digital/constelaciones]]
- [[../modulacion-digital/modulacion-qam]]
- [[../modulacion-digital/probabilidad-error]]
- [[../modulacion-digital/comparacion-digital-analogica]]
- [[../modulacion-digital/codificacion-linea]]
- [[../derivaciones/modulacion-qam]]
- [[../conceptos-integradores/trade-off-bw-potencia]]
