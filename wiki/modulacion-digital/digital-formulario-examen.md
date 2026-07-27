---
tags:
  - wiki/modulacion-digital
  - wiki/planificacion
curso: Sistemas de Comunicaciones
unidad: 6
---

# Modulación Digital — Formulario de examen (compacto)

> **Last verified:** 2026-07-27 | **Verified by:** analysis + patrón real de ejercicios en `exercises/finales/md/`

> **Para qué es esta nota**: versión operativa para resolver bajo reloj. Explicación conceptual completa en [[ask-fsk-psk|ASK, FSK, PSK]], [[modulacion-qam|Modulación QAM]] y [[probabilidad-error|Probabilidad de Error (BER)]].
>
> **Modulación Digital aparece en 40,5% de los 42 finales únicos.** Menos que PCM o AM/FM, pero sus fórmulas se reusan en Ruido/BER, así que rinde doble.

## Cadena de fórmulas

$$R_b\ [\text{bps}] \to \ell \to D\ [\text{baudios}] \to B\ [\text{Hz}] \to SNR \to BER$$

| # | Fórmula | Nota |
|---|---|---|
| 1 | $\boxed{\ell = \log_2 M}$ | bits/símbolo. 16-QAM → $\ell=4$; QPSK → $\ell=2$ |
| 2 | $\boxed{D = \dfrac{R_b}{\ell}}$ | Tasa de símbolos [baudios]. También se escribe $R_s$ |
| 3 | $\boxed{N = N_0\,B_N}$ | Potencia de ruido ($B_N$ = ancho de banda equivalente de ruido) |
| 4 | $\boxed{E_b = \dfrac{S}{R_b}}$ | Energía por bit (potencia $\times$ duración de bit) |
| 5 | $\boxed{\dfrac{E_b}{N_0} = SNR\cdot\dfrac{B}{R_b}}$ | **El puente** entre SNR y BER |

## Los tres anchos de banda — no confundirlos

Los finales piden los tres y son distintos. Confundirlos es el error más frecuente:

| Cuál | Fórmula | Cuándo se usa |
|---|---|---|
| **Nulo a nulo** | $B = 2D$ | Pulso rectangular, ancho del lóbulo principal. **Lo piden explícitamente 4 veces en el corpus** |
| **Mínimo (Nyquist ideal)** | $B = D$ | Cuando dice "ancho de banda mínimo ideal" ($\alpha=0$) |
| **Con roll-off** | $B = D(1+\alpha)$ | Coseno realzado real; el enunciado da $\alpha$ |

Ver la justificación del $B=D$ pasabanda en [[../modulacion-pulsos/pcm-formulario-examen#Justificación del paso $R_s \to B_{min}$ (criterio de Nyquist sin ISI)|criterio de Nyquist sin ISI]] — es la misma relación, con $D$ en lugar de $R_s$.

## BER — las fórmulas a tener

$$\boxed{P_e^{BPSK} = P_e^{QPSK} = Q\!\left(\sqrt{\frac{2E_b}{N_0}}\right)}, \qquad \boxed{P_e^{FSK\ coh} = Q\!\left(\sqrt{\frac{E_b}{N_0}}\right)}$$

**BPSK y QPSK dan lo mismo por bit** — QPSK transmite el doble de bits en el mismo ancho de banda **sin penalidad de BER**. Es la razón de que QPSK sea tan usada, y un punto conceptual que los finales preguntan.

Para $M$-QAM:

$$P_e \approx \frac{4}{\ell}\left(1-\frac{1}{\sqrt M}\right)Q\!\left(\sqrt{\frac{3\,\ell\,E_b}{(M-1)N_0}}\right)$$

**El trade-off central**: al subir $M$ se gana eficiencia espectral ($\ell$ bits por símbolo) pero **empeora la BER** para el mismo $E_b/N_0$ — los puntos de la constelación quedan más juntos. Ver [[constelaciones|Constelaciones]].

## Ejercicio resuelto — 16-QAM (`F_Comu_2026-02-26_res.md`)

> ⚠️ **Los dos estudiantes que rindieron este ejercicio lo reprobaron** (1,5/2,5 y 0,75/2,5). Vale la pena estudiar dónde fallaron.

**Enunciado**: señal digital pasabanda 16-QAM, $f_c=50$ MHz, amplitud máxima $3\sqrt2$ mV (pico), símbolos equiprobables, $R_b = 256$ kbps, $N_0 = 4\times10^{-14}$ W/Hz.

**a) Ancho de banda de nulo a nulo**

$$\ell = \log_2 16 = 4 \ \Rightarrow\ D = \frac{256\text{k}}{4} = 64\text{ kbaudios} \ \Rightarrow\ \boxed{B_{n\text{-}n} = 2D = 128\text{ kHz}}$$

**b) Densidad espectral de potencia**

Lóbulo principal centrado en $f_c$, con **nulos en $f_c\pm64$ kHz, $\pm128$ kHz, $\pm192$ kHz** (múltiplos de $D$). Forma $\text{sinc}^2$, típica de señalización pasabanda con pulso rectangular.

**c) Potencia normalizada** — ⚠️ **acá cayeron los dos**

Calcularon con la amplitud máxima y obtuvieron $10\ \mu$W. El corrector anotó a mano *"falta dividir por el factor de cresta"*:

$$\boxed{P_{norm} \approx 5\ \mu\text{W}}$$

> **Por qué**: en 16-QAM los símbolos **no tienen todos la misma amplitud** — hay tres niveles distintos ($\sqrt2$, $\sqrt{10}$, $3\sqrt2$ mV según la posición I/Q). La potencia es el **promedio sobre la constelación**, no el máximo. Es el mismo concepto de factor de cresta que aparece en [[../modulacion-pulsos/pcm-formulario-examen#SNR de cuantificación — esta cátedra usa factor de cresta|PCM]] y en [[../derivaciones/modulacion-am#¿Cual metodo conviene usar en el examen?|AM]] — esta cátedra lo usa sistemáticamente, conviene tenerlo como reflejo.

**d) Relación señal a ruido**

$$N = N_0 B_N = 4\times10^{-14}\times128\times10^3 = 5{,}12\text{ nW}$$

$$SNR = \frac{5\ \mu\text{W}}{5{,}12\ \text{nW}} = 976{,}6 \ \Rightarrow\ \boxed{SNR \approx 29{,}9\text{ dB}}$$

*(El estudiante había obtenido 32,99 dB arrastrando la potencia sin corregir; el corrector anotó "arrastra error" — igual descuenta.)*

**e) BER con filtro acoplado (QPSK)** — *ninguno de los dos llegó*

$$\frac{E_b}{N_0} = SNR\cdot\frac{B}{R_b} = 976{,}6\times\frac{128\text{k}}{256\text{k}} = 488$$

$$P_e = Q\!\left(\sqrt{2\times488}\right) = Q(31{,}2) \approx 0$$

BER prácticamente nula — el enlace tiene muchísimo margen.

## Los cuatro errores que cuestan el ejercicio

Del análisis de cómo fallaron los estudiantes reales:

1. **Confundir los tres anchos de banda** — nulo a nulo ($2D$) vs mínimo ideal ($D$) vs con roll-off ($D(1+\alpha)$)
2. **Olvidar el factor de cresta** al calcular potencia desde la amplitud máxima de la constelación
3. **Arrastrar el error** de un ítem al siguiente — el corrector lo marca ("arrastra error") pero **descuenta igual**
4. **No llegar al BER** por quedarse trabado antes. Recordar la regla del examen: **25% desarrollado por punto como mínimo**; conviene plantear la fórmula aunque no se termine la cuenta

## Ver también

- [[ask-fsk-psk|ASK, FSK, PSK]] — las tres modulaciones básicas
- [[modulacion-qam|Modulación QAM]]
- [[constelaciones|Constelaciones]] — diagramas I/Q, de donde sale el factor de cresta
- [[probabilidad-error|Probabilidad de Error (BER)]] — curvas BER vs $E_b/N_0$
- [[eficiencia-espectral|Eficiencia Espectral]]
- [[../modulacion-pulsos/pcm-formulario-examen|PCM — Formulario de examen]] — la cadena previa (PCM genera los bits que esto transmite)
- [[../conceptos-integradores/eb-n0-vs-snr|$E_b/N_0$ vs SNR]] — el puente de la fórmula 5, en detalle
- [[../planificacion/formulario-imprimible|Formulario Imprimible]]
