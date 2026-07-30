---
tags:
  - wiki/planificacion
curso: Sistemas de Comunicaciones
---

# Diagramas en Bloques — los que hay que tener a mano

> 🖨️ **Para imprimir**: abrir `diagramas-en-bloques.html` en Chrome o Safari. **Ese HTML se genera de este archivo** con `node scripts/build-diagramas.mjs` — los bloques ```` ```diagram ```` se dibujan como SVG. Todo cambio va acá, no en el HTML.

> Diagramas de referencia: la cadena de bloques de cada sistema, con la función de cada etapa.

## 1. Generador PCM

```diagram
<Analógica> > [Filtro anti-alias;pasabajos a B] > [Muestreador S/H;a f_s ≥ 2B] > [Cuantificador;M niveles] > [Codificador;n = log_2 M] > <PCM>
caption: Transmisor. La información se pierde en el cuantificador, no antes.
```

**Función de cada bloque**:

| Bloque | Qué hace |
|---|---|
| **Filtro anti-alias** (pasabajos) | Limita la señal a $B$ para que $f_s\geq2B$ sea suficiente. **Sin él hay aliasing** |
| **Muestreador (S/H)** | Toma muestras a $f_s$ y las **retiene** durante el tiempo de conversión |
| **Cuantificador** | Asigna cada muestra a uno de $M$ niveles. **Acá se pierde información** (error de cuantificación) |
| **Codificador** | Convierte cada nivel en $n=\log_2M$ binits |

*(Si el sistema usa companding, va un **compresor** entre muestreador y cuantificador, y el **expansor** en el receptor.)*

**Receptor** — el inverso exacto:

```diagram
<PCM> > [Decodificador] > [Retenedor] > [Filtro pasabajos;reconstruye] > <Analógica>
```

---

## 2. Transmisor PAM/TDM

```diagram
{<m_1(t)> | <m_2(t)> | <⋮> | <m_N(t)>} > {[LPF] | [LPF] | . | [LPF]} > [Conmutador rotativo;f_s por canal] > [LPF de salida;BW mínimo] > <PAM/TDM>
caption: Un pasabajos por canal (anti-alias), el conmutador rota a f_s, y el filtro de salida acota el ancho de banda.
```

**Puntos clave:**
- Un **filtro pasabajos por canal** a la entrada (anti-alias, limita cada mensaje a $B_i$)
- El **conmutador** (o multiplexor) rota entre los $N$ canales a $f_s$ por canal → tasa total $Nf_s$
- **Filtro de salida** para que el ancho de banda sea mínimo

$$f_{s,total} = N f_s \geq 2NB \qquad B_{min} = \frac{Nf_s}{2}\ \text{(banda base)}$$

**Con sincronismo** (variante con canal de sincronismo): se agrega un **canal extra** para la señal de trama/sincronismo, así que $N+1$ ranuras en vez de $N$.

**Receptor**:

```diagram
<PAM/TDM> > [Conmutador sincronizado;misma f_s] > {[LPF] | [LPF] | . | [LPF]} > {<m_1(t)> | <m_2(t)> | <⋮> | <m_N(t)>}
caption: Necesita sincronismo de trama para saber qué ranura corresponde a qué canal.
```

---

## 3. Modulador SSB por desplazamiento de fase (Hartley)

```diagram
<m(t)> > {~ | [−90°;Hilbert]} > {(×)v{cos(2πf_c t)} | "m̂(t)"(×)^{sen(2πf_c t)}} > (∓) > <s_{SSB}(t)>
caption: Dos desfasajes de 90°: uno a la moduladora (Hilbert) y otro a la portadora (cos → sen).
```

$$s_{SSB}(t) = m(t)\cos(\omega_ct) \mp \hat m(t)\sin(\omega_ct)$$

**$-$ para banda lateral superior (USB), $+$ para inferior (LSB).**

**Los dos bloques de $-90°$**: uno desplaza la **moduladora** (transformada de Hilbert, $\hat m(t)$) y otro desplaza la **portadora** ($\cos\to\sin$). Ver [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]].

*(Alternativa: **método del filtrado** — $\boxed{\text{Modulador balanceado}} \to \boxed{\text{Filtro lateral}}$. Más simple pero exige filtro muy abrupto.)*

---

## 4. Modulador Armstrong (FM indirecto)

```diagram
<Osc. de cristal> > [NBFM;β ≪ 1]^{m(t)} > [× n_1;sube β] > (×)^{Osc. local f_{OL}} > [× n_2;sube β] > <WBFM>
caption: Los multiplicadores suben β; el mezclador ubica la portadora sin tocar Δf.
```

**Por qué esa estructura** (ver [[../derivaciones/modulacion-fm-carson#Multiplicador vs mezclador: una sola operación, dos segundas entradas|Derivación de FM]]):

| Bloque | $f_c$ | $\Delta f$ |
|---|---|---|
| **Multiplicador $\times n$** | $\times n$ | $\times n$ |
| **Mezclador** | $\pm f_{OL}$ | **sin cambio** |

Los multiplicadores **suben $\beta$** (que es lo que NBFM no puede dar directamente) y el mezclador **ubica la portadora final** sin arruinar la desviación conseguida.

---

## 5. Transmisor OFDM

```diagram
<Datos serie> > [S/P] > [Mapeo QAM] > [IFFT] > [P/S] > [+ CP] > {"x(t)"(×)v{cos(2πf_c t)} | "y(t)"(×)^{−sen(2πf_c t)}} > (+) > <v(t)>
caption: x(t) = Re{s̃(t)}, y(t) = Im{s̃(t)}. El receptor es el inverso exacto, con FFT en vez de IFFT.
```

$$v(t) = x(t)\cos(\omega_ct) - y(t)\,\text{sen}(\omega_ct)$$

con $x(t)=\text{Re}\{\tilde s(t)\}$, $y(t)=\text{Im}\{\tilde s(t)\}$.

**Receptor**: inverso exacto — cuadratura → quitar CP → S/P → **FFT** → demapeo → P/S.

Ver [[../espectro-expandido/ss-ofdm-formulario-examen|Formulario SS/OFDM]].

---

## 6. Sección de repetición

```diagram
<⋯> > [Cable;g_c = 1/L_c,  T_{amb} = T_0] > [Repetidor;g_r = L_c,  F_r] > <⋯ × n secciones>
caption: El repetidor compensa exactamente la atenuación del tramo previo.
```

**Se repite $n$ veces.** El repetidor compensa exactamente la atenuación del tramo previo. Ver [[../ruido/ruido-formulario-examen#El patrón estrella: cascada de repetidores|Formulario de Ruido]].

---

## 7. Demodulador FSK binaria

**Coherente** (dos filtros acoplados):

```diagram
<r(t)> > {[BPF f_1] | [BPF f_0]} > {[Detector] | [Detector]} > [Comparador;decide 1 / 0] > <bits>
caption: No coherente: los mismos dos brazos con detector de envolvente. Más simple, ~3 dB de penalidad.
```

**No coherente**: los mismos dos brazos pero con **detector de envolvente** en vez de detector coherente. Más simple, ~3 dB de penalidad.

*(Y sí: un modulador FSK binaria **se puede armar con dos moduladores OOK** — uno en $f_1$ activado por los "1" y otro en $f_2$ por los "0", sumados a la salida.)*

---

## 8. Receptor superheterodino

```diagram
<Antena> > [Ampl. RF;rechaza la imagen] > (×)^{Osc. local f_{OL}} > [Ampl. FI;f_{FI} = f_{RF} − f_{OL}] > [Detector] > [Ampl. audio] > <Parlante>
caption: El filtro de RF es el que rechaza la frecuencia imagen, a 2·f_{FI} de la deseada.
```

$f_{FI} = |f_{RF} - f_{OL}|$. La **frecuencia imagen** está a $2f_{FI}$ de la deseada y la rechaza el filtro de RF.

---

## Cómo dibujarlos

1. **Bloques rectangulares con el nombre adentro**, flechas indicando el sentido
2. **Rotular las señales** en los puntos clave (entrada, salida, frecuencias intermedias)
3. **Anotar los valores calculados** sobre cada bloque (ej. $\times500$, $f_{OL}=1{,}7$ MHz) — conecta el dibujo con la cuenta y muestra que entendés el sistema
4. Para explicar la función de cada bloque, **una línea por bloque alcanza**


## Ver también

- [[../modulacion-pulsos/pcm-formulario-examen|PCM]] · [[../modulacion-analogica/exponencial-formulario-examen|FM/PM]] · [[../espectro-expandido/ss-ofdm-formulario-examen|SS/OFDM]] · [[../ruido/ruido-formulario-examen|Ruido]]
- [[../modulacion-pulsos/multiplex-tdm|Multiplexación TDM]]
- [[../modulacion-analogica/modulador-armstrong|Modulador Armstrong]]
