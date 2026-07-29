---
tags:
  - wiki/planificacion
curso: Sistemas de Comunicaciones
---

# Diagramas en Bloques — los que hay que tener a mano

> **Last verified:** 2026-07-29 | **Verified by:** relevamiento sobre los 42 finales únicos de `exercises/finales/md/`

> **"Dibujar el diagrama en bloques" aparece ~20 veces en el corpus.** Casi siempre vale entre 0,5 y 0,75 puntos, y es de lo más rápido de resolver **si lo tenés memorizado** — y de lo más caro si no.

## Frecuencia real en los finales

| Diagrama | Apariciones |
|---|---|
| **Transmisor PAM/TDM** (y su receptor) | **10** |
| **Modulador SSB por desplazamiento de fase** | 3 |
| **Transmisor de FM / Armstrong** | 3+ |
| **Sección de repetición** (cable + repetidor) | 2 |
| **Transmisor OFDM** (S/P → IFFT → P/S → cuadratura) | 2 |
| **Generador PCM** | 1+ |
| **Demodulador FSK binaria** | 1 |

---

## 1. Generador PCM ⭐

$$\text{Analógica} \to \boxed{\text{Filtro anti-alias}} \to \boxed{\text{Muestreador S/H}} \to \boxed{\text{Cuantificador}} \to \boxed{\text{Codificador}} \to \text{PCM}$$

**Función de cada bloque** (lo piden explícitamente):

| Bloque | Qué hace |
|---|---|
| **Filtro anti-alias** (pasabajos) | Limita la señal a $B$ para que $f_s\geq2B$ sea suficiente. **Sin él hay aliasing** |
| **Muestreador (S/H)** | Toma muestras a $f_s$ y las **retiene** durante el tiempo de conversión |
| **Cuantificador** | Asigna cada muestra a uno de $M$ niveles. **Acá se pierde información** (error de cuantificación) |
| **Codificador** | Convierte cada nivel en $n=\log_2M$ binits |

*(Si el sistema usa companding, va un **compresor** entre muestreador y cuantificador, y el **expansor** en el receptor.)*

**Receptor**: $\text{PCM} \to \boxed{\text{Decodificador}} \to \boxed{\text{Retenedor}} \to \boxed{\text{Filtro pasabajos}} \to$ analógica

---

## 2. Transmisor PAM/TDM ⭐⭐ (el más pedido — 10 veces)

$$\begin{array}{c}
m_1(t) \to \boxed{\text{LPF}} \to \\
m_2(t) \to \boxed{\text{LPF}} \to \\
\vdots \\
m_N(t) \to \boxed{\text{LPF}} \to
\end{array}
\Bigg\} \to \boxed{\text{Conmutador rotativo}} \to \boxed{\text{LPF de salida}} \to \text{PAM/TDM}$$

**Puntos clave que evalúan:**
- Un **filtro pasabajos por canal** a la entrada (anti-alias, limita cada mensaje a $B_i$)
- El **conmutador** (o multiplexor) rota entre los $N$ canales a $f_s$ por canal → tasa total $Nf_s$
- **Filtro de salida** para que el ancho de banda sea mínimo (lo piden así: *"tal que el ancho de banda a la salida sea mínimo"*)

$$f_{s,total} = N f_s \geq 2NB \qquad B_{min} = \frac{Nf_s}{2}\ \text{(banda base)}$$

**Con sincronismo** (variante que piden 3 veces): se agrega un **canal extra** para la señal de trama/sincronismo, así que $N+1$ ranuras en vez de $N$.

**Receptor**: $\to \boxed{\text{Conmutador sincronizado}} \to$ cada canal $\to \boxed{\text{LPF}} \to m_i(t)$
El receptor necesita **sincronismo de trama** para saber qué ranura corresponde a qué canal.

---

## 3. Modulador SSB por desplazamiento de fase (Hartley) ⭐

$$\begin{array}{ccc}
m(t) &\to \boxed{\times}\ \leftarrow \cos(\omega_ct) & \searrow \\
&& \boxed{\pm} \to s_{SSB}(t) \\
m(t) \to \boxed{-90°} \to \hat m(t) &\to \boxed{\times}\ \leftarrow \sin(\omega_ct) & \nearrow
\end{array}$$

$$s_{SSB}(t) = m(t)\cos(\omega_ct) \mp \hat m(t)\sin(\omega_ct)$$

**$-$ para banda lateral superior (USB), $+$ para inferior (LSB).**

**Los dos bloques de $-90°$**: uno desplaza la **moduladora** (transformada de Hilbert, $\hat m(t)$) y otro desplaza la **portadora** ($\cos\to\sin$). Ver [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]].

*(Alternativa: **método del filtrado** — $\boxed{\text{Modulador balanceado}} \to \boxed{\text{Filtro lateral}}$. Más simple pero exige filtro muy abrupto.)*

---

## 4. Modulador Armstrong (FM indirecto) ⭐

$$\text{Oscilador} \to \boxed{\text{NBFM}} \to \boxed{\times n_1} \to \boxed{\text{Mezclador}} \to \boxed{\times n_2} \to \text{WBFM}$$
$$\uparrow \qquad\qquad\qquad\qquad \uparrow$$
$$m(t) \qquad\qquad\qquad \text{Oscilador local } f_{OL}$$

**Por qué esa estructura** (ver [[../derivaciones/modulacion-fm-carson#Multiplicador vs mezclador: una sola operación, dos segundas entradas|Derivación de FM]]):

| Bloque | $f_c$ | $\Delta f$ |
|---|---|---|
| **Multiplicador $\times n$** | $\times n$ | $\times n$ |
| **Mezclador** | $\pm f_{OL}$ | **sin cambio** |

Los multiplicadores **suben $\beta$** (que es lo que NBFM no puede dar directamente) y el mezclador **ubica la portadora final** sin arruinar la desviación conseguida.

---

## 5. Transmisor OFDM ⭐

$$\text{Datos serie} \to \boxed{S/P} \to \boxed{\text{Mapeo QAM}} \to \boxed{\text{IFFT}} \to \boxed{P/S} \to \boxed{+\text{CP}} \to \begin{array}{c}\boxed{\times}\leftarrow\cos\omega_ct \\ \boxed{\times}\leftarrow-\sin\omega_ct\end{array} \to \boxed{+} \to v(t)$$

$$v(t) = x(t)\cos(\omega_ct) - y(t)\,\text{sen}(\omega_ct)$$

con $x(t)=\text{Re}\{\tilde s(t)\}$, $y(t)=\text{Im}\{\tilde s(t)\}$.

**Receptor**: inverso exacto — cuadratura → quitar CP → S/P → **FFT** → demapeo → P/S.

Ver [[../espectro-expandido/ss-ofdm-formulario-examen|Formulario SS/OFDM]].

---

## 6. Sección de repetición (para ejercicios de Ruido) ⭐

$$\to \boxed{\text{Cable } g_c = 1/L_c,\ T_{amb}=T_0} \to \boxed{\triangleright\ \text{Repetidor } g_r = L_c,\ F_r} \to$$

**Se repite $n$ veces.** El repetidor compensa exactamente la atenuación del tramo previo. Ver [[../ruido/ruido-formulario-examen#El patrón estrella: cascada de repetidores|Formulario de Ruido]].

---

## 7. Demodulador FSK binaria

**Coherente** (dos filtros acoplados):

$$r(t) \to \begin{array}{c}\boxed{\text{BPF } f_1} \to \boxed{\text{Detector}} \\ \boxed{\text{BPF } f_2} \to \boxed{\text{Detector}}\end{array} \to \boxed{\text{Comparador}} \to \text{bits}$$

**No coherente**: los mismos dos brazos pero con **detector de envolvente** en vez de detector coherente. Más simple, ~3 dB de penalidad.

*(Y sí: un modulador FSK binaria **se puede armar con dos moduladores OOK** — uno en $f_1$ activado por los "1" y otro en $f_2$ por los "0", sumados a la salida. Es una pregunta del corpus.)*

---

## 8. Receptor superheterodino (por si aparece)

$$\text{Antena} \to \boxed{\text{RF}} \to \boxed{\text{Mezclador}} \to \boxed{\text{FI}} \to \boxed{\text{Detector}} \to \boxed{\text{Audio}}$$
$$\uparrow$$
$$\text{Oscilador local}$$

$f_{FI} = |f_{RF} - f_{OL}|$. La **frecuencia imagen** está a $2f_{FI}$ de la deseada y la rechaza el filtro de RF.

---

## Cómo dibujarlos en el examen

1. **Bloques rectangulares con el nombre adentro**, flechas indicando el sentido
2. **Rotular las señales** en los puntos clave (entrada, salida, frecuencias intermedias)
3. **Anotar los valores calculados** sobre cada bloque (ej. $\times500$, $f_{OL}=1{,}7$ MHz) — conecta el dibujo con la cuenta y muestra que entendés el sistema
4. Si piden "explicar la función de cada bloque", **una línea por bloque alcanza**

> Con la regla del **25% mínimo por punto**, un diagrama bien hecho puede salvar un ejercicio donde las cuentas no salieron.

## Ver también

- [[../modulacion-pulsos/pcm-formulario-examen|PCM]] · [[../modulacion-analogica/exponencial-formulario-examen|FM/PM]] · [[../espectro-expandido/ss-ofdm-formulario-examen|SS/OFDM]] · [[../ruido/ruido-formulario-examen|Ruido]]
- [[../modulacion-pulsos/multiplex-tdm|Multiplexación TDM]]
- [[../modulacion-analogica/modulador-armstrong|Modulador Armstrong]]
