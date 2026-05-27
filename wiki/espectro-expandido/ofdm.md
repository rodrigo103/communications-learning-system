---
tags:
  - wiki/espectro-expandido
source_file: explicaciones_anki/unidad_10/carta_53_ofdm-principio.md
curso: Sistemas de Comunicaciones
unidad: 10
---

# OFDM — Orthogonal Frequency Division Multiplexing

> **Last verified:** 2025-11-16 | **Verified by:** source

## Principio

**OFDM** divide un canal de banda ancha en $N$ subportadoras ortogonales de banda angosta, transmitiendo datos en paralelo a baja velocidad en cada una. Resuelve elegantemente el problema del multitrayecto sin ecualizadores complejos. [source]

Es la tecnologia de capa fisica dominante en comunicaciones modernas: WiFi (802.11a/g/n/ac/ax), 4G LTE, 5G NR, TV digital (DVB-T), DSL, y radio digital (DAB).

## Ortogonalidad

La clave de OFDM: las subportadoras estan espaciadas exactamente por:

$$\boxed{\Delta f = \frac{1}{T_s}}$$

donde $T_s$ es la duracion del simbolo OFDM util. Con este espaciado:

$$\int_0^{T_s} e^{j2\pi f_k t} \cdot e^{-j2\pi f_m t} dt = \begin{cases} T_s & \text{si } k = m \\ 0 & \text{si } k \neq m \end{cases}$$

Los espectros de las subportadoras (funciones sinc) se solapan, pero en el pico de cada una las demas tienen un cero. Esto permite **solapamiento sin interferencia**, logrando una eficiencia espectral $\sim 50\%$ mayor que FDM convencional. [analysis]

## Implementacion con FFT/IFFT

La genialidad practica de OFDM: la modulacion de todas las subportadoras se implementa con una sola IFFT/FFT: [source]

**Transmision**:
$$s[n] = \sum_{k=0}^{N-1} X_k \cdot e^{j2\pi kn/N} = \text{IFFT}\{X_k\}$$

**Recepcion**:
$$Y_k = \frac{1}{N}\sum_{n=0}^{N-1} r[n] \cdot e^{-j2\pi kn/N} = \text{FFT}\{r[n]\}$$

Esto reduce la complejidad de $O(N^2)$ a $O(N \log N)$.

## Modelo del Canal

Con **prefijo ciclico** para manejar el multitrayecto, el canal se convierte en una multiplicacion simple por subportadora:

$$\boxed{Y_k = H(f_k) \cdot X_k + N_k}$$

Donde $H(f_k)$ es la respuesta en frecuencia del canal en la subportadora $k$. La ecualizacion es trivial:

$$\boxed{\hat{X}_k = \frac{Y_k}{H(f_k)}}$$

El multitrayecto, que en sistemas single-carrier requiere ecualizadores complejos, se reduce aqui a una division compleja por subportadora. [analysis]

## Prefijo Ciclico (CP)

El **prefijo ciclico** copia los ultimos $T_g$ segundos del simbolo al inicio:

- **Proposito**: absorber el retardo del multitrayecto y convertir convolucion lineal en circular
- **Condicion**: $T_g > \tau_{max}$ (delay spread maximo)
- **Costo**: overhead que reduce throughput efectivo

Eficiencia por CP:

$$\eta = \frac{T_s}{T_s + T_g}$$

Para WiFi: $T_s = 3.2 \,\mu\text{s}$, $T_g = 0.8 \,\mu\text{s}$, $\eta = 80\%$. [source]

## Parametros de Diseno

| Parametro | Formula | Significado |
|-----------|---------|-------------|
| Espaciado subportadoras | $\Delta f = 1/T_s$ | Condicion de ortogonalidad |
| Numero subportadoras | $N = BW / \Delta f$ | Resolucion frecuencial |
| Duracion CP | $T_g > \tau_{max}$ | Absorber multitrayecto |
| Throughput | $R = N_{datos} \cdot \log_2(M) \cdot r \cdot \eta / T_{total}$ | Tasa efectiva |

## Ventajas de OFDM

1. **Resistencia a multitrayecto**: ecualizacion simple por subportadora
2. **Eficiencia espectral**: subportadoras solapadas ortogonalmente
3. **Flexibilidad**: modulacion adaptativa (AMC) por subportadora
4. **Escalabilidad**: facil variar BW (cambiar $N$)
5. **Implementacion digital eficiente**: FFT en hardware [analysis]

## Desventajas

- **Alto PAPR** (Peak-to-Average Power Ratio): requiere amplificadores lineales costosos
- **Sensible a offset de frecuencia**: efecto Doppler puede destruir ortogonalidad
- **Overhead por CP**: reduce throughput efectivo

## Parametros de Sistemas Reales

| Sistema | $N$ (FFT) | Datos | $\Delta f$ | $T_g$ |
|---------|-----------|-------|------------|-------|
| WiFi 802.11a/g | 64 | 48 | 312.5 kHz | 0.8 $\mu$s |
| WiFi 802.11ac | 256 | 234 | 78.125 kHz | 0.8 $\mu$s |
| LTE (20 MHz) | 2048 | 1200 | 15 kHz | 4.7 $\mu$s |
| 5G NR | Hasta 4096 | Variable | 15/30/60/120 kHz | Variable |
| DVB-T2 | 32768 | 27841 | Variable | Flexible |

## Errores Comunes

- Pensar que las subportadoras no se solapan: los espectros se solapan completamente; la ortogonalidad lo permite
- Ignorar la perdida por CP: overhead de 20-25% reduce el throughput proporcionalmente
- Confundir OFDM con FDM clasico: OFDM no necesita bandas de guarda

## Ver tambien

- [[espectro-expandido/cdma]]
- [[espectro-expandido/fhss]]
- [[herramientas-matematicas/teorema-convolucion]]
- [[modulacion-digital/modulacion-qam]]
- [[espectro-expandido/aplicaciones-spread-spectrum]]
- [[conceptos-integradores/evolucion-sistemas]]
