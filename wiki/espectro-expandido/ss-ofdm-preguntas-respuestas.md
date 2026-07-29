---
tags:
  - wiki/espectro-expandido
curso: Sistemas de Comunicaciones
unidad: 10
---

# Espectro Expandido y OFDM — Preguntas y Respuestas

> **Last verified:** 2026-07-28 | **Verified by:** analysis + sesion de estudio

Dudas resueltas en sesion de estudio sobre OFDM y DSSS.

---

**¿OFDM paga por todo esto con ancho de banda extra?**

No. La cuenta lo demuestra:

$$B_T = N_p \cdot \Delta f = N_p \cdot \frac{1}{T_S} = N_p \cdot \frac{R_b}{N_p \cdot \ell} = \frac{R_b}{\ell}$$

$N_p$ se cancela. $B_T = R_b/\ell$, exactamente el mismo ancho de banda que una sola portadora usando la misma $\ell$-QAM. OFDM **empata** en ancho de banda. Lo que sí paga:

| Costo | Detalle |
|---|---|
| **PAPR altísimo** | Suma coherente de subportadoras — peor caso: PAPR = $N_p$ = 36 dB |
| **Sensibilidad a error de frecuencia** | $\Delta f$ es mínimo (~977 Hz); un desvío rompe ortogonalidad → ICI |
| **Overhead del CP** | Tiempo muerto (~1%), no es ancho de banda pero sí throughput |
| **Latencia** | Procesar bloques + IFFT/FFT introduce retardo |
| **Complejidad** | IFFT/FFT en hardware (hoy barato, pero es carga extra) |

La comparacion con 1024-QAM en el ejemplo del formulario es tramposa: usan modulaciones de distinto orden. Si ambas usaran 16-QAM, $B_T$ seria identico. [analysis]

**¿Por que el problema del eco/multitrayecto aparece recien en la unidad de OFDM? ¿A las otras tecnologias no les afecta?**

Afecta a todas. Pero el programa lo introduce recien aca por dos razones:

1. **El resto del curso asume canal AWGN ideal** (solo ruido blanco, sin distorsion, sin ecos). Es el modelo basico de Shannon, el punto de partida. La ISI que se estudia en digital viene del pulso mismo (sinc), no del canal.

2. **OFDM se invento especificamente para combatir el multitrayecto.** Si no hubiera ecos, nadie usaria OFDM — una sola portadora con QAM seria mas simple y tendria mejor PAPR. Tiene sentido que el eco aparezca como tema central justo aca: es el problema que motiva toda la arquitectura.

Cada tecnologia tiene su truco contra el eco: FM usa efecto captura (se engancha a la señal mas fuerte), DSSS usa RAKE receiver (trata cada eco como replica util), una sola portadora digital usa ecualizador adaptivo. La diferencia es que OFDM **pone el truco en el diseño de la forma de onda** en vez de en el receptor. [analysis]

**¿Cual es el problema de ISI por multitrayecto exactamente? Entender la seccion "La razon central" del formulario.**

La señal rebota en edificios y llega por varios caminos con retardos distintos. La **dispersion temporal** $\tau$ (eco tipico ~1 μs en ciudad) hace que el eco del simbolo anterior caiga encima del simbolo siguiente. La metrica clave es $\tau / T_S$: que fraccion de un simbolo tapa el eco.

Comparacion lado a lado, misma $R_b = 16$ Mbps:

| | Una portadora (1024-QAM) | OFDM (4096 × 16-QAM) |
|---|---|---|
| Bits/simbolo | 10 | 16384 |
| $T_S$ | $\mathbf{0{,}625\ \mu s}$ | $\mathbf{1024\ \mu s}$ |
| Eco de 1 μs tapa | **1,6 simbolos** → ISI severa | **0,1% del simbolo** → despreciable |

Con una portadora hace falta un ecualizador complejo que desenrede varios simbolos de arrastre. OFDM **no resuelve el multitrayecto: lo esquiva.** En vez de 16 Mbps rapido (simbolos cortos que el eco destroza), reparte el caudal entre 4096 enlaces lentisimos en paralelo. Cada subportadora transmite a solo 3,9 kbps → $T_S$ enorme → el eco es insignificante.

$$T_S = \frac{N_p \cdot \ell}{R_b}$$

Misma $R_b$, pero $N_p \cdot \ell$ bits empaquetados en un solo simbolo gigante en vez de $\ell$ bits en uno chiquito. [analysis]

**¿Cuales son los 4 beneficios adicionales de OFDM y como funciona cada uno?**

**1. Cada subportadora ve un canal plano** *(el mas importante)*. El canal inalambrico tiene fading selectivo en frecuencia — no responde igual en todas las frecuencias. Una portadora ancha atraviesa toda esa variacion y se distorsiona; corregirlo requiere un ecualizador temporal con muchos taps. Cada subportadora OFDM ocupa solo $\Delta f$ (~977 Hz), y en un ancho tan chico el canal es esencialmente constante. La distorsion se reduce a $Y_k = H_k \cdot X_k + N_k$: una simple multiplicacion compleja por subportadora, corregible con una division ($\hat{X}_k = Y_k / H_k$). Reemplaza un ecualizador complejo por $N_p$ divisiones triviales.

**2. El prefijo ciclico sale barato.** El CP es tiempo muerto — una copia del final del simbolo para absorber el eco. Su costo es $CP/T_S$. Con OFDM ($T_S = 1024\ \mu$s), 10 μs de CP cuesta ~1%. Con una sola portadora ($T_S = 0{,}625\ \mu$s), los mismos 10 μs son 1600% del simbolo — absurdo. Solo los simbolos largos hacen viable el CP.

**3. Bit loading adaptativo (water-filling).** Cada subportadora tiene su propia ganancia $H_k$: algunas ven +3 dB, otras -10 dB. En vez de usar la misma modulacion en todas, se asigna mas bits (256-QAM) a las buenas y menos (QPSK) o cero a las malas. Maximiza el throughput sin aumentar potencia ni ancho de banda. Es lo que hace ADSL: mide que frecuencias del cobre funcionan bien y carga mas bits ahi.

**4. Rechazo de interferencia de banda angosta.** Un interferente puntual ocupa pocas subportadoras; las otras sobreviven intactas. Con una portadora ancha, el mismo interferente corrompe todo el simbolo. Es diversidad en frecuencia: el daño se reparte en vez de concentrarse. El FEC puede recuperar los bits de las subportadoras afectadas. [analysis]

**¿5G usa OFDM? ¿OFDM es solo de 4G?**

OFDM es usado por **ambas** generaciones (y por WiFi desde 802.11a):

- **4G LTE:** OFDMA en downlink, SC-FDMA en uplink (mejor PAPR para el movil). Latencia ~10 ms.
- **5G NR:** CP-OFDM en ambas direcciones. Latencia <1 ms.
- **WiFi:** OFDM desde 802.11a hasta WiFi 6/7.

5G no reemplazo OFDM — lo **afino**. La mejora de latencia viene de la arquitectura, no de la modulacion:

| Cambio en 5G | Efecto |
|---|---|
| **Numerologia flexible** | 4G usa $\Delta f = 15$ kHz fijo. 5G permite 15, 30, 60, 120, 240 kHz. A mayor $\Delta f$, menor $T_S$ ($T_S = 1/\Delta f$) — con 240 kHz es 16× mas corto que LTE |
| **Mini-slots** | Transmite en 2, 4 o 7 simbolos en vez del slot completo de 14; no espera a llenar |
| **Slot auto-contenido** | DL y UL en el mismo slot, sin esperar cambio de direccion |
| **Acceso sin grant** | El dispositivo transmite sin pedir permiso previo |

OFDM no es el cuello de botella de la latencia — lo es la organizacion temporal de quien transmite cuando. [analysis]

**¿Que es PAPR y por que es un problema tan grave en OFDM?**

**Peak-to-Average Power Ratio** — la relacion entre la potencia de pico y la potencia media:

$$\boxed{PAPR = \frac{\max |s(t)|^2}{\langle |s|^2\rangle}}$$

El problema: un amplificador tiene un limite de saturacion. Si la señal tiene picos muy altos, hay dos opciones, ambas malas: (1) achicar la potencia media para no saturar → señal debil, poco alcance; (2) dejar que sature → distorsion no lineal, BER alta, interferencia en canales vecinos.

Hay dos fuentes de PAPR, y en OFDM el problema es la segunda:

| Fuente | Ejemplo | PAPR tipico |
|--------|---------|-------------|
| **Constelacion** | 16-QAM: esquinas tienen mas amplitud que interiores | ~1,8 (2,55 dB) |
| **Suma de subportadoras** | $N_p$ tonos en fase se suman coherentemente | $N_p$ (4096 = 36 dB en el ejemplo) |

La IFFT suma $N_p$ sinusoides. Si muchas se alinean en fase (por azar o por datos patologicos como todo ceros), el pico es $N_p$ veces la amplitud individual → PAPR = $N_p$. Con 4096 subportadoras: 36 dB, tres ordenes de magnitud peor que el PAPR de constelacion solo.

**Mitigaciones:** scrambler (aleatoriza bits para evitar patrones), clipping (recorta picos controladamente), reserva de tonos (sacrifica subportadoras para cancelar picos), SC-FDMA en uplink LTE (DFT-spreading, PAPR mucho menor para ahorrar bateria del movil). [analysis]

## Ver tambien

- [[ss-ofdm-formulario-examen|SS/OFDM — Formulario de examen]]
- [[ofdm|OFDM]]
- [[prefijo-ciclico|Prefijo Ciclico]]
- [[../modulacion-digital/digital-formulario-examen|Modulacion Digital]]
- [[../conceptos-integradores/aplicaciones-reales|Aplicaciones Reales (4G, 5G, WiFi)]]
