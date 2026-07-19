---
tags:
  - wiki/planificacion
curso: Sistemas de Comunicaciones
---

# Formulario Imprimible — Examen Final

> Chuleta de consulta rápida (no explicativa). Backup impreso por si la carpeta digital no se puede usar en el examen. Basado en el patrón real de 13 finales resueltos: Lineal (77%), TI (69%), PCM (69%), Espectro Expandido (62%), Exponencial (54%), Ruido (38%), Digital (31%).

---

## 1. Modulación Lineal (AM / DSB / SSB / VSB) — la más frecuente

| Fórmula | Qué es / cuándo usarla | Notas |
|---|---|---|
| $s_{AM}(t) = A_c[1+m\cos(\omega_m t)]\cos(\omega_c t)$ | Señal AM con tono único | $m=A_m/A_c$ |
| $m = \dfrac{A_{max}-A_{min}}{A_{max}+A_{min}}$ | Índice de modulación desde envolvente | $m\le1$ sin distorsión |
| $P_{AM} = \dfrac{A_c^2}{2Z}+\dfrac{m^2A_c^2}{4Z} = P_c\left(1+\dfrac{m^2}{2}\right)$ | **Potencia normalizada AM (tono único)** — de memoria | $Z$ = impedancia (1Ω si no dan dato) |
| $P = P_c + \sum_i P_{SB,i} = P_c\left(1+\dfrac{\sum m_i^2}{2}\right)$ | AM multitono (varias moduladoras) | Sumar $m_i^2/2$ de cada tono |
| $\eta_{AM}=\dfrac{m^2}{2+m^2}$ | Eficiencia de potencia AM | Máx 33.3% en $m=1$ |
| PEP $=P_c(1+m)^2$ | Potencia pico de envolvente | Pico instantáneo, no promedio; frecuente en finales |
| $s_{DSB-SC}(t)=A_c\,m(t)\cos(\omega_c t)$ | DSB-SC (sin portadora) | $\eta=100\%$, detección coherente |
| $BW_{AM}=BW_{DSB}=2f_m$ | Ancho de banda AM/DSB | Doble banda lateral |
| $s_{SSB}(t)=m(t)\cos\omega_ct \mp \hat m(t)\sin\omega_ct$ | SSB (Hilbert), $-$=USB, $+$=LSB | $\hat m$ = transf. de Hilbert |
| $BW_{SSB}=f_m$ | Ancho de banda SSB | Mitad de DSB |
| $BW_{VSB}=f_m+f_v$, $f_v\approx(0.1$–$0.25)f_m$ | Ancho de banda VSB | Compromiso DSB/SSB, preserva DC (video) |
| $H_{VSB}(f_c+f)+H_{VSB}(f_c-f)=1$, $\|f\|<f_v$ | Condición de simetría vestigial | Filtro VSB para recuperación perfecta |
| $SNR_{out}^{AM}=\dfrac{m^2}{2+m^2}SNR_{in}$ | SNR salida AM (envolvente) | Umbral $\approx10$ dB |
| $SNR_{out}^{DSB-SC}=SNR_{out}^{SSB}=SNR_{in}$ | SNR salida DSB-SC/SSB (síncrona) | Sin efecto umbral |
| $dBW = 10\log_{10}(P/1W)$, $dBm=10\log_{10}(P/1mW)$ | Conversión a dB | $0$ dBW = 30 dBm |

---

## 2. Modulación Exponencial (FM / PM) — segunda más frecuente

| Fórmula | Qué es / cuándo usarla | Notas |
|---|---|---|
| $s_{FM}(t)=A_c\cos\left[2\pi f_ct+2\pi k_f\int m(\tau)d\tau\right]$ | Señal FM | $f_i=f_c+k_fm(t)$ |
| $s_{PM}(t)=A_c\cos[2\pi f_ct+k_pm(t)]$ | Señal PM | $\phi_i=2\pi f_ct+k_pm(t)$ |
| $\beta_{FM}=\dfrac{\Delta f}{f_m}=\dfrac{k_fA_m}{f_m}$ | Índice de modulación FM | $\Delta f$=desviación máx. |
| $\beta_{PM}=k_pA_m$ | Índice de modulación PM | Independiente de $f_m$ |
| $BW\approx2(\Delta f+f_m)=2f_m(\beta+1)$ | **Regla de Carson** — de memoria | ~98% de la potencia; NBFM→$2f_m$, WBFM→$2\Delta f$ |
| FM$[m(t)]\equiv$PM$[\int m\,dt]$ | Dualidad FM↔PM | Clave para moduladores indirectos |
| Multiplicador de frec. ×$n$: $\Delta f\to n\Delta f$, $f_c\to nf_c$, $\beta\to n\beta$ | Modulador indirecto (Armstrong) | Escala todo por $n$ |
| Mezclador: $f_{IF}=|f_{RF}-f_{LO}|$ | Traslación de frecuencia (no cambia $\beta$ ni $\Delta f$) | Solo desplaza portadora |
| $SNR_{out}^{FM}=3\beta^2(\beta+1)\cdot SNR_{in}$ | Ganancia SNR en FM (sobre umbral) | Tono único: $3\beta^2\cdot SNR_{in}$ |
| $SNR_{umbral}\approx10$ dB | Umbral FM (discriminador convencional) | PLL: ~7dB, FMFB: ~4-5dB |
| Mejora por énfasis $\approx10$–$13$ dB | Pre-énfasis/de-énfasis | $\tau=75\mu s$ (USA), $50\mu s$ (Europa) |
| $f_{IF}=|f_{RF}-f_{LO}|$ | Receptor superheterodino | Frecuencia imagen: $f_{RF}\pm2f_{IF}$ |

---

## 3. Muestreo / PCM / Cuantificación — tercer/cuarto ejercicio frecuente

| Fórmula | Qué es / cuándo usarla | Notas |
|---|---|---|
| $f_s\geq2B$ (o $2f_{max}$) | **Nyquist** — de memoria | Evita aliasing |
| $\Delta=\dfrac{2V_{max}}{L}=\dfrac{2V_{max}}{2^n}$ | Paso de cuantificación | $L=2^n$ niveles |
| $\sigma_q^2=\Delta^2/12$ | Potencia de ruido de cuantificación | Error uniforme $\pm\Delta/2$ |
| $SQNR\approx6.02n+1.76$ dB | **SNR de cuantificación PCM** — de memoria | +1 bit = +6dB (senoidal amplitud completa) |
| $R_b=n\cdot f_s$ | Tasa de bits PCM | Telefonía: $n=8$, $f_s=8$kHz → 64kbps |
| $BW_{PCM}\approx R_b/2$ | Ancho de banda banda base PCM | $BW_{PCM}/BW_{analog}\geq n$ |
| $BW_{min}=1/\tau$ | Ancho de banda de pulso (PAM) | $\tau$=ancho del pulso |
| $C_\mu(x)=\text{sgn}(x)\dfrac{\ln(1+\mu\|x/V_{max}\|)}{\ln(1+\mu)}$ | Companding μ-law ($\mu=255$, USA/Japón) | Cuantif. no uniforme |
| $C_A(x)$: lineal cerca de 0, log lejos | Companding A-law ($A=87.6$, Europa) | μ-law y A-law NO compatibles entre sí |
| Mejora rango dinámico $\approx20\log_{10}(\mu)$ dB | Ganancia por companding | $\mu=255$→~48dB |
| Slope overload: $\delta\cdot f_s\geq\max\|dx/dt\|$ | Condición modulación Delta (DM) | 1 bit/muestra; $R_{DM}=f_s$ |
| $\delta[n]=\delta[n-1]\cdot K$ (misma dir.) o $/K$ (cambio) | Delta Adaptativa (ADM) | $K\approx1.5$ |

---

## 4. Ruido / Friis / SNR

| Fórmula | Qué es / cuándo usarla | Notas |
|---|---|---|
| $N=kTB$ | **Ruido térmico** — de memoria | $k=1.38\times10^{-23}$ J/K |
| $v_n^2=4kTRB$ | Ruido térmico (voltaje, Johnson-Nyquist) | Potencia disponible = $kTB$ |
| $F=\dfrac{SNR_{in}}{SNR_{out}}$; $NF=10\log_{10}F$ dB | Figura de ruido | $F=1$ ideal (sin ruido agregado) |
| $T_e=T_0(F-1)$; $F=1+T_e/T_0$ | Temperatura equivalente de ruido | $T_0=290$K referencia |
| $T_{sys}=T_{antena}+T_{receptor}$ | Temperatura de sistema | Aditiva |
| $F_{total}=F_1+\dfrac{F_2-1}{G_1}+\dfrac{F_3-1}{G_1G_2}+\cdots$ | **Fórmula de Friis (cascada)** — de memoria | Valores LINEALES, no dB; $F_i-1$ en numerador |
| $T_{e,total}=T_{e,1}+\dfrac{T_{e,2}}{G_1}+\cdots$ | Friis en temperaturas | Equivalente, más intuitivo |
| $SNR_{out}=SNR_{in}/F$ | Degradación de SNR por dispositivo | Primera etapa domina (LNA crítico) |
| $E_b/N_0 = SNR\cdot B/R_b$ | Relación SNR ↔ Eb/N0 | Puente entre ambas métricas |
| $E_s/N_0=(E_b/N_0)\log_2 M$ | Energía por símbolo | $M$-aria |
| $SNR_{umbral}\approx10$dB (AM y FM discrim.) | Umbral de detección | Bajo umbral: colapso de SNR |

---

## 5. Modulación Digital (ASK/FSK/PSK/QAM/BER)

| Fórmula | Qué es / cuándo usarla | Notas |
|---|---|---|
| $BW_{ASK,BPSK}=2R_s$ | Ancho de banda ASK/BPSK (pulso rectangular) | $R_s$=tasa de símbolo |
| $BW_{FSK}=2(\Delta f+R_s)$ | Ancho de banda FSK (Carson) | $\Delta f=\|f_1-f_0\|/2$ |
| $R_b=R_s\cdot\log_2M$ | **Bits vs símbolos** — de memoria | $M$=orden de modulación |
| $s_{QAM}(t)=I(t)\cos(\omega_ct)-Q(t)\sin(\omega_ct)$ | Señal QAM | I/Q ortogonales |
| $\eta=R_b/B=\log_2M$ bits/s/Hz | Eficiencia espectral (Nyquist, $B=R_s$) | Con roll-off $\alpha$: $\eta=2\log_2M/(1+\alpha)$ |
| $P_e^{BPSK}=Q\!\left(\sqrt{2E_b/N_0}\right)$ | **BER BPSK/QPSK** — de memoria | $=\frac12\text{erfc}(\sqrt{E_b/N_0})$ |
| $P_e^{FSK}=Q\!\left(\sqrt{E_b/N_0}\right)$ | BER FSK ortogonal coherente | Peor que BPSK |
| $P_e^{OOK}=Q\!\left(\sqrt{E_b/2N_0}\right)$ | BER OOK (ASK on-off) | La más débil de las 3 básicas |
| $BER_{M\text{-}QAM}\approx\dfrac{2(\sqrt M-1)}{\sqrt M\log_2M}Q\!\left(\sqrt{\dfrac{3\log_2M\,E_b}{(M-1)N_0}}\right)$ | BER M-QAM rectangular (aprox.) | Mayor $M$ → mejor $\eta$, peor BER |
| $d_{min}=\min_{i\ne j}\|s_i-s_j\|$ | Distancia mínima constelación | Mayor $d_{min}$ → menor $P_e$ |
| $P_e\approx Q(d_{min}/2\sigma_n)$ | BER aproximado vía distancia | Válido AWGN |
| $BER\approx SER/\log_2M$ | Relación BER-SER con mapeo Gray | 1 error símbolo ≈ 1 bit |

---

## 6. Espectro Expandido / OFDM

| Fórmula | Qué es / cuándo usarla | Notas |
|---|---|---|
| $G_p=\dfrac{BW_{SS}}{BW_{info}}=\dfrac{R_{chip}}{R_{bit}}$ | **Ganancia de procesamiento DSSS/CDMA** — de memoria | $SNR_{out}=G_p\cdot SNR_{in}$ |
| $N=2^L-1$ | **Longitud secuencia LFSR** de $L$ etapas — de memoria | Código PN máximo |
| $G_{p,FHSS}\approx M/k$ | Ganancia procesamiento FHSS | $M$=canales, $k$=interferidos |
| $P_{hit}=k/M$ | Prob. de colisión con jammer (FHSS) | Slow-hop: varios bits/salto |
| $\Delta f=1/T_s$ | Espaciado subportadoras OFDM (ortogonalidad) | $T_s$=duración símbolo útil |
| $Y_k=H(f_k)X_k+N_k$; $\hat X_k=Y_k/H(f_k)$ | Ecualización OFDM por subportadora | División compleja, trivial con CP |
| $T_{CP}>\tau_{max}$ | Condición de diseño prefijo cíclico | $\tau_{max}$=delay spread máx. |
| $\eta_{CP}=\dfrac{T_s}{T_s+T_{CP}}$ | Eficiencia por overhead de CP | WiFi: ~80%, LTE normal: ~93% |
| $N_{subport}=BW/\Delta f$ | Número de subportadoras | Resolución frecuencial |
| $s_k(t)=A_kd_k(t)c_k(t)\cos(\omega_ct+\phi_k)$ | Señal CDMA usuario $k$ | Multiplicación por código PN |

---

## 7. Teoría de la Información — muy frecuente (69%)

| Fórmula | Qué es / cuándo usarla | Notas |
|---|---|---|
| $H(X)=-\sum_i p_i\log_2 p_i$ | **Entropía** — de memoria | bits/símbolo |
| $I(p)=-\log_2p$ | Información de un evento | $p=1\Rightarrow I=0$ |
| $0\leq H\leq\log_2n$ | Cota de entropía | Máx si equiprobables |
| $R=1-H/H_{max}=1-H/\log_2n$ | Redundancia de fuente | $\eta=H/H_{max}$ = eficiencia |
| $H\leq\bar L<H+1$ | Límite Shannon codificación de fuente | $\bar L=\sum p_il_i$ long. media |
| $\sum_i2^{-l_i}\leq1$ | Criterio de Kraft-McMillan | Código unívocamente decodificable |
| $C=B\log_2(1+S/N)$ | **Shannon-Hartley (capacidad)** — de memoria | $S/N$ LINEAL, no dB |
| $C\approx B\log_2(SNR)$ | Régimen limitado por banda ($S/N\gg1$) | Crecimiento logarítmico |
| $C\approx1.44\,B\,S/N$ | Régimen limitado por potencia ($S/N\ll1$) | Crecimiento lineal |
| $C_\infty=\dfrac{S}{N_0\ln2}=1.44\dfrac{S}{N_0}$ | Capacidad con $B\to\infty$ | Límite finito aún con banda infinita |
| $E_b/N_0>\ln2\approx-1.59$ dB | **Límite absoluto de Shannon** — de memoria | Ningún sistema opera por debajo |
| $e_d=d_{min}-1$ | Máx errores detectables (código) | $d_{min}$=distancia de Hamming |
| $e_c=\lfloor(d_{min}-1)/2\rfloor$ | Máx errores corregibles | Hamming(7,4): $d_{min}=3$→corrige 1 |
| $R_{codigo}=k/n$ | Tasa de código (bloque $k\to n$) | $d_{min}\leq n-k+1$ (Singleton) |
| $B_{min}=R_s/2$ | BW mínimo sin ISI (Nyquist) | Filtro raised-cosine |

---

## Herramientas Matemáticas de Base (transversal)

| Fórmula | Qué es / cuándo usarla |
|---|---|
| $X(f)=\int x(t)e^{-j2\pi ft}dt$ | Transformada de Fourier |
| $x(t)=\sum_n c_n e^{j2\pi nf_0t}$, $f_0=1/T_0$ | Serie de Fourier (señal periódica) |
| $\int\|x(t)\|^2dt=\int\|X(f)\|^2df$ | Teorema de Parseval (conservación de energía) |
| $\hat x(t)=\mathcal H\{x(t)\}$; $\hat X(f)=-j\,\text{sgn}(f)X(f)$ | Transformada de Hilbert (desfasaje 90°) |
| $x_a(t)=x(t)+j\hat x(t)$; $a(t)=\sqrt{x^2+\hat x^2}$ | Señal analítica → envolvente/fase instantánea |
| $x_1(t)*x_2(t)\leftrightarrow X_1(f)X_2(f)$ | Teorema de convolución |

---

## Constantes y valores típicos

| Constante / valor | Significado |
|---|---|
| $k=1.38\times10^{-23}$ J/K | Constante de Boltzmann |
| $T_0=290$ K | Temperatura de referencia estándar (ruido) |
| $\mu=255$ | Companding μ-law (Norteamérica/Japón) |
| $A=87.6$ | Companding A-law (Europa) |
| $\tau=75\,\mu s$ / $50\,\mu s$ | Pre-énfasis FM (USA/Japón vs Europa) |
| $SNR_{umbral}\approx10$ dB | Umbral AM/FM (discriminador convencional) |
| $\ln2\approx-1.59$ dB | Límite absoluto $E_b/N_0$ |
| $0$ dBW $=30$ dBm | Conversión dBW↔dBm |
| $N=-174+10\log_{10}(B)$ dBm | Piso de ruido térmico a $T_0=290$K |
| FM broadcast: $\Delta f=75$kHz, $f_m=15$kHz, $\beta=5$, $BW=200$kHz | Valores estándar radio FM |
| Telefonía PCM: $f_s=8$kHz, $n=8$bit, $R_b=64$kbps | G.711 estándar |

---

## Ver También

- [[../planificacion/plan-11-dias-final|Plan Intensivo 11 Días]]
- [[../conceptos-integradores/clasificacion-modulaciones|Clasificación de Modulaciones]]
- [[../glosario|Glosario]]
