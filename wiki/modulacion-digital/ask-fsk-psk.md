---
tags:
  - wiki/modulacion-digital
source_file: explicaciones_anki/unidad_06/carta_27_comparacion-ask-fsk-psk.md
curso: Sistemas de Comunicaciones
unidad: 6
---

# ASK, FSK y PSK: Modulaciones Digitales Básicas

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Principio

Las modulaciones digitales básicas modifican un parámetro de la portadora $s_c(t) = A_c\cos(2\pi f_c t + \phi_c)$ según los bits a transmitir. [source]

### ASK (Amplitude Shift Keying)

Varía la amplitud:

$$s_{ASK}(t) = A(t)\cos(2\pi f_c t), \quad A(t) = \begin{cases} A_1 & \text{bit } 1 \\ A_0 & \text{bit } 0 \end{cases}$$

En OOK (On-Off Keying): $A_0 = 0$, $A_1 = A_c$. [source]

### FSK (Frequency Shift Keying)

Varía la frecuencia:

$$s_{FSK}(t) = A_c\cos(2\pi f(t) t), \quad f(t) = \begin{cases} f_1 & \text{bit } 1 \\ f_0 & \text{bit } 0 \end{cases}$$

### PSK (Phase Shift Keying)

Varía la fase:

$$s_{PSK}(t) = A_c\cos(2\pi f_c t + \phi(t))$$

En BPSK: $\phi_0 = 0°$, $\phi_1 = 180°$. [source]

## Ancho de Banda

- **ASK/BPSK**: $BW = 2R_s$ (pulsos rectangulares)
- **FSK** (Carson): $\boxed{BW = 2(\Delta f + R_s)}$

donde $\Delta f = |f_1 - f_0|/2$ y $R_s$ es la velocidad de símbolo.

## Probabilidad de Error

Para canal AWGN con detección coherente: [source]

$$\boxed{P_e^{BPSK} = Q\left(\sqrt{\frac{2E_b}{N_0}}\right)}$$

$$\boxed{P_e^{FSK} = Q\left(\sqrt{\frac{E_b}{N_0}}\right)}$$

$$\boxed{P_e^{OOK} = Q\left(\sqrt{\frac{E_b}{2N_0}}\right)}$$

Para $E_b/N_0 = 10$ dB: $P_e^{BPSK} \approx 3.9 \times 10^{-6}$, $P_e^{FSK} \approx 7.9 \times 10^{-4}$, $P_e^{OOK} \approx 1.25 \times 10^{-2}$.

## Comparación

| Modulación | Robustez | Eficiencia espectral | Uso típico |
|------------|----------|---------------------|------------|
| ASK (OOK) | Baja | Moderada | Fibra óptica, RFID |
| FSK | Buena | Baja | Bluetooth, telemetría |
| PSK | Muy buena | Alta | WiFi, satélite, 5G |

Ranking general de desempeño: **PSK > FSK > ASK**. [analysis]

## Ver también

- [[modulacion-digital/modulacion-qam]] — Combinación de ASK y PSK
- [[modulacion-digital/constelaciones]] — Representación I-Q de estas modulaciones
- [[modulacion-digital/probabilidad-error]] — Análisis detallado de BER
