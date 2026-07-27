# Solución — PCM: audio digital en CD

**Origen del enunciado:** `exercises/finales/md/F_Comu_2023-12-07.md`, Ejercicio 2 (PCM, 2,5 puntos)
**Resuelto:** 2026-07-27, por Rodrigo — **primer ejercicio cronometrado del plan** (~30 min estimados, sin cronómetro real)
**Resultado: 6/6 correctos.**
**Nota:** el PDF original es un examen **en blanco** — no hay resolución de estudiante con la cual comparar. La verificación es independiente.

---

## Enunciado

Se desea grabar digitalmente señales de audio en un CD usando PCM. La señal de audio tiene un **ancho de banda de 15 kHz** y las muestras se cuantifican en **65536 niveles** distribuidos uniformemente. Determinar:

a) La frecuencia mínima ideal de muestreo (tasa de Nyquist). [0,25 pts]
b) La cantidad de dígitos binarios utilizados para codificar cada muestra. [0,5 pts]
c) La tasa de transmisión binaria para muestreo a tasa de Nyquist. [0,5 pts]
d) La tasa de bits para el caso de utilizar $f_s=44100$ Hz. [0,25 pts]
e) Con factor de cresta $\sqrt5$, la relación señal a ruido de cuantificación para amplitud máxima. [0,5 pts]
f) Con factor de cresta $\sqrt5$, la mínima amplitud relativa que asegure $SNR_Q$ de 50 dB. [0,5 pts]

---

## Resolución

**a) Tasa de Nyquist**

$$f_s = 2B = 2\times15\text{ kHz} = \boxed{30\text{ k muestras/s}}$$

**b) Bits por muestra**

$$n = \log_2 M = \log_2 65536 = \boxed{16\text{ bits/muestra}}$$

(chequeo: $2^{16}=65536$ ✓)

**c) Tasa binaria a tasa de Nyquist**

$$R_b = n\,f_s = 16\times30\text{k} = \boxed{480\text{ kbps}}$$

**d) Tasa binaria con $f_s = 44100$ Hz**

$$R_b = 16\times44100 = \boxed{705{,}6\text{ kbps}}$$

*(Este es el valor real del estándar CD-Audio: 44,1 kHz de muestreo, 16 bits, y $\times2$ canales estéreo da 1,41 Mbps.)*

**e) SNR de cuantificación a amplitud máxima**

$$SNR_Q = \frac{3M^2}{F_C^2} = \frac{3\,(65536)^2}{(\sqrt5)^2} = \frac{12{,}885\times10^9}{5} = 2{,}577\times10^9$$

$$SNR_Q\big|_{dB} = 10\log_{10}(2{,}577\times10^9) = \boxed{94{,}11\text{ dB}}$$

**f) Mínima amplitud relativa para $SNR_Q = 50$ dB**

Si la amplitud se reduce por un factor relativo $k$, la **potencia de señal escala por $k^2$** mientras el ruido de cuantificación $P_q=q^2/12$ **no cambia** (depende solo del paso $q$, fijado por el ADC). Entonces:

$$SNR_Q(k) = \frac{3M^2k^2}{F_C^2} \qquad\Longrightarrow\qquad SNR_Q\big|_{dB}(k) = 94{,}11 + 20\log_{10}k$$

Igualando a 50 dB:

$$20\log_{10}k = 50 - 94{,}11 = -44{,}11 \ \Rightarrow\ \log_{10}k = -2{,}2055$$

$$\boxed{k = 6{,}22\times10^{-3} \approx 0{,}62\%\text{ del fondo de escala}}$$

> **Chequeo mental rápido (sirve para validar en el examen):** hay $94{,}11-50 = 44{,}11$ dB de margen, y $10^{44{,}11/20}\approx160$. O sea se puede atenuar **160 veces** antes de caer a 50 dB → $k=1/160=6{,}25\times10^{-3}$ ✓. Coincide, y se hace sin calculadora.

### Método alternativo para f) — vía niveles efectivos (el que usé al resolver)

En vez de razonar sobre cómo escala la potencia, se puede razonar sobre **cuántos niveles abarca la señal**. Se pasa 50 dB a veces, se despeja $M$ de la misma fórmula, y se compara contra el total:

$$10^5 = \frac{3M_{ef}^2}{F_C^2} = \frac{3M_{ef}^2}{5} \ \Rightarrow\ M_{ef}^2 = \frac{5\times10^5}{3} \ \Rightarrow\ M_{ef} = 408{,}25\ \text{niveles}$$

$$k = \frac{M_{ef}}{M_{total}} = \frac{408{,}25}{65536} = \boxed{6{,}23\times10^{-3}}$$

**Por qué es exacto y no una aproximación**: en cuantificación uniforme el paso $q$ está fijo (lo define el rango del ADC), así que la cantidad de niveles que abarca una señal es **proporcional a su amplitud**:

$$\frac{M_{ef}}{M_{total}} = \frac{V/q}{V_{FS}/q} = \frac{V}{V_{FS}} = k$$

El $q$ se cancela — por eso "fracción de niveles usados" y "amplitud relativa" son literalmente el mismo número.

Conceptualmente esta ruta es **más directa**: en vez de "la potencia escala con $k^2$", dice "la señal solo abarca 408 de los 65536 niveles disponibles". Misma física vista desde el ADC en vez de desde la potencia.

> **Detalle**: que $M_{ef}=408{,}25$ no sea entero está bien — es un conteo *equivalente* en el umbral, no una cantidad física de niveles. Y ojo con la terminología: $M$ son **niveles**, no muestras (las muestras son lo que sale del muestreo, a razón de $f_s$ por segundo).

### Tercera ruta: en bits efectivos

$\log_2(408{,}25) = 8{,}67$ bits. O sea a 50 dB se están usando efectivamente **~8,7 bits de los 16** disponibles → sobran $16-8{,}67 = 7{,}33$ bits, y $7{,}33\times6{,}02 \approx 44$ dB de margen. Coincide con los 44,11 dB del primer método.

**Las tres rutas dan lo mismo** porque son la misma relación leída en tres escalas: amplitud ($k$), niveles ($M_{ef}$) y bits ($n_{ef}$), ligadas por $M_{ef}=k\,M_{total}$ y $n_{ef}=\log_2M_{ef}$.

---

## Lo que hay que sacar de este ejercicio

**Los puntos a–d son la cadena PCM directa** ([[../../wiki/modulacion-pulsos/pcm-formulario-examen|formulario PCM]]): Nyquist → $n=\log_2M$ → $R_b=n f_s$. Mecánicos, no deberían llevar más de 5 minutos entre los cuatro.

**El e) es aplicar la fórmula de factor de cresta**, que es la que usa esta cátedra ($3M^2/F_C^2$, no $6n+1{,}76$, aunque son la misma con $F_C=\sqrt2$).

**El f) es el único fuera del molde** y vale lo mismo que el e). Requiere entender que:
- El ruido de cuantificación **no depende de la amplitud de la señal** — está fijado por $q$, que sale del rango del ADC
- Por lo tanto bajar la señal **empeora la SNR proporcionalmente a $k^2$** (o $20\log k$ en dB)
- Y hay que **invertir** la fórmula en vez de evaluarla

Ese patrón — "qué pasa con la SNR si la señal no usa todo el rango del conversor" — es una idea física importante y reaparece en companding (ver [[../../wiki/modulacion-pulsos/companding|Companding]]): es exactamente el problema que la Ley A / Ley $\mu$ vienen a resolver, haciendo que la SNR sea aproximadamente **independiente del nivel** de la señal.

**Nota de presentación**: cuando el enunciado pide "amplitud relativa", conviene dar también el porcentaje (0,62%) además del número — en un examen donde se evalúa el desarrollo, la legibilidad suma.

## Ver también

- [[../../wiki/modulacion-pulsos/pcm-formulario-examen|PCM — Formulario de examen]] — las 6 fórmulas y la contabilidad de unidades
- [[../../wiki/modulacion-pulsos/companding|Companding]] — por qué existe, conectado con el punto f)
- [[../../wiki/herramientas-matematicas/teorema-muestreo|Teorema de Muestreo]]
