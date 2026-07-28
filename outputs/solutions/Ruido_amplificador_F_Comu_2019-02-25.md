# Solución — Ruido: amplificador y cambios en señal/ruido de entrada

**Origen del enunciado:** `exercises/finales/md/F_Comu_2019-02-25.md`, Ejercicio 3 (Ruido, 2,5 puntos)
**Resuelto:** 2026-07-28, por Rodrigo — tercer ejercicio cronometrado del plan.
**Tiempo: 30 min** (límite alcanzado) — resolvió a) y b); se trabó en c), pero **diagnosticó correctamente la causa**.
**Resultado: a) ✓ · b) ✓ · c) diagnóstico correcto, cuenta sin cerrar · d) no llegó**

---

## Enunciado

Dado un amplificador con ganancia $G=20$ dB, ancho de banda equivalente de ruido $B_{eq}=25$ kHz y **factor de ruido 4**. Se lo ensayó con $0{,}8\times10^{-12}$ W de potencia de señal a la entrada y se obtuvo **30 dB** de SNR a la salida.

a) Determinar la SNR a la entrada. [0,5 pts]
b) Si la **potencia de señal** a la entrada sube 3 dB y el ruido no cambia, determinar la SNR a la salida. [0,5 pts]
c) Si la **potencia de ruido** a la entrada sube 3 dB y la señal no cambia, determinar la SNR a la salida. [1 punto]
d) En un sistema WBFM optimizado para mensaje de 15 kHz y 10 mW se obtienen 35 dB de SNR a la salida. Si se aplica una modulante de sólo 5 kHz manteniendo 10 mW, ¿la SNR **mejora, empeora o queda invariable**? Justificar. [0,5 pts]

> **Dato de vocabulario**: dice "**factor** de ruido 4" → es **lineal** ($F=4$, equivalente a 6,02 dB de *cifra* de ruido). Ver [[../../wiki/ruido/ruido-formulario-examen#Glosario de símbolos|la distinción factor/cifra]].

---

## Resolución

### a) SNR a la entrada

$$F = 4 \equiv 6{,}02\text{ dB}$$

$$\left(\frac{S}{N}\right)_{in}\bigg|_{dB} = \left(\frac{S}{N}\right)_{out}\bigg|_{dB} + F\big|_{dB} = 30 + 6{,}02 = \boxed{36{,}0\text{ dB}}$$

### b) Señal de entrada +3 dB, ruido igual

Sube la señal y el ruido queda igual → la SNR de entrada sube los mismos 3 dB. **$F$ no cambia** (es una propiedad del amplificador, y el ruido de entrada no se tocó):

$$\left(\frac{S}{N}\right)_{in}' = 36{,}02+3 = 39{,}02\text{ dB} \ \Rightarrow\ \left(\frac{S}{N}\right)_{out}' = 39{,}02-6{,}02 = \boxed{33{,}0\text{ dB}}$$

### c) Ruido de entrada +3 dB, señal igual — ⚠️ **cambia la degradación real, no el $F$ del dispositivo**

**El punto clave**: el ruido propio del amplificador, $N_a$ (referido a la entrada), es **una propiedad del dispositivo** — no cambia porque le entre más ruido. Lo que sí cambia es **cuánto pesa relativamente** frente al ruido que entra.

**Distinción importante para justificar bien por escrito:**

| Concepto | Definición | ¿Cambia en c)? |
|---|---|---|
| **$F$ del amplificador** (spec de catálogo) | $F = 1+\dfrac{T_{eq}}{T_0}$, **siempre** referido a $T_0=290$ K | ❌ **No** — sigue siendo 4 |
| **Degradación real de SNR** | $\dfrac{(S/N)_{in}}{(S/N)_{out}} = 1+\dfrac{T_{eq}}{T_{fuente}} = 1+\dfrac{N_a}{N_i}$ | ✅ **Sí** — baja a 2,5 |

Las dos coinciden **solo cuando la fuente está a $T_0$**. Al duplicarse el ruido de entrada (fuente a $2T_0$), se separan:

$$\text{Degradación} = 1+\frac{N_a}{N_i'} = 1+\frac{3N_i}{2N_i} = 1+1{,}5 = \mathbf{2{,}5} \equiv 3{,}98\text{ dB}$$

> **De dónde sale $1+\frac{N_a}{N_i}$**: es la misma fórmula $F = 1+\frac{T_{eq}}{T_0}$ escrita en potencias, sustituyendo $N_a = kT_{eq}B$ (ruido propio del ampli referido a la entrada) y $N_i = kT_0B$ (ruido de la fuente) — el $kB$ se cancela y queda $\frac{N_a}{N_i}=\frac{T_{eq}}{T_0}$. Ver [[../../wiki/ruido/ruido-formulario-examen#De dónde sale $T_e = (F-1)T_0$ (deducción de la fórmula 3)|la deducción completa]].

| | Original | Después ($N_i'=2N_i$) |
|---|---|---|
| $N_a/N_i$ | $F-1 = 3$ | $3N_i/2N_i = 1{,}5$ |
| Degradación de SNR | $4$ (6,02 dB) | $\mathbf{2{,}5}$ (**3,98 dB**) |

$$\left(\frac{S}{N}\right)_{in}' = 36{,}02-3 = 33{,}02\text{ dB}$$

$$\left(\frac{S}{N}\right)_{out}' = 33{,}02 - 3{,}98 = \boxed{29{,}0\text{ dB}}$$

**Verificación con potencias absolutas:**

| Cantidad | Valor |
|---|---|
| $N_i = S_i/4000$ | $2\times10^{-16}$ W |
| $N_a = 3N_i$ | $6\times10^{-16}$ W |
| $N_i' = 2N_i$ | $4\times10^{-16}$ W |
| $N_{total}' = N_i'+N_a$ | $10^{-15}$ W |
| $(S/N)_{out}' = 0{,}8\times10^{-12}/10^{-15}$ | $800 \equiv 29{,}0$ dB ✓ |

> **La trampa**: la respuesta ingenua (mantener $F=4$) da $33{,}02-6{,}02 = 27$ dB. Los **2 dB de diferencia** son exactamente lo que evalúa el medio punto extra de este ítem. Que valga el doble que a) y b) es la señal de que hay una vuelta de tuerca.
>
> **En temperaturas es la misma cuenta**: con $F=1+T_{eq}/T_0$ y $F=4$ sale $T_{eq}=3T_0$; si la fuente pasa a $2T_0$, entonces $F'=1+\frac{3T_0}{2T_0}=2{,}5$ ✓ (ver [[../../wiki/ruido/ruido-formulario-examen#De dónde sale $T_e = (F-1)T_0$ (deducción de la fórmula 3)|la deducción de $T_e=(F-1)T_0$]])

### d) WBFM con menor ancho de banda de mensaje

**Mejora, y bastante.** Con $W$ de 15 → 5 kHz y $\Delta f$ **fijo** (lo determina el diseño del transmisor, no la modulante), actúan **dos efectos en la misma dirección**:

| Efecto                                    | Cambio                                              |
| ----------------------------------------- | --------------------------------------------------- |
| Índice de modulación $\beta = \Delta f/W$ | se **triplica** → $\beta^2$ se multiplica por **9** |
| $\gamma = S_R/(N_0W)$ (SNR en banda base) | se **triplica** (entra menos ruido al bajar $W$)    |

$$\left(\frac{S}{N}\right)_D \propto 3\beta^2\gamma \ \Rightarrow\ \text{mejora } 9\times3 = 27\times \approx +14{,}3\text{ dB}$$

De 35 dB pasaría a **~49 dB**.

---

## Qué aprender de este ejercicio

1. **La degradación real de SNR es constante frente a cambios en la señal, pero NO frente a cambios en el ruido de entrada.** Es la diferencia entre b) y c), y es todo el contenido del ítem que vale doble. Ojo con la redacción: el **$F$ del amplificador no cambia** (es spec a $T_0$); lo que cambia es cuánto degrada realmente, porque su ruido propio pesa menos frente a un ruido de entrada mayor.
2. **El puntaje delata la dificultad**: si un ítem vale el doble que sus vecinos, tiene una vuelta de tuerca. Desconfiar de la respuesta simétrica obvia.
3. **$B_{eq}$ y $G$ no se usaron en ningún ítem** — el enunciado los da como datos para una ruta alternativa (o distractores). Ver [[../../wiki/ruido/ruido-formulario-examen#¿Cuándo hace falta $B_N$ en las cuentas?|cuándo hace falta $B_N$]]: solo para potencias absolutas, no para cocientes.
4. **Regla de examen**: si a los 5 minutos de un ítem no aparece el camino, **escribir el planteo y pasar al siguiente**. Acá dejar asentado *"$F$ cambia porque $N_a$ es fijo y $N_i$ subió"* ya habría sumado, sin necesidad de cerrar la cuenta.

## Ver también

- [[../../wiki/ruido/ruido-formulario-examen|Ruido — Formulario de examen]]
- [[../../wiki/ruido/factor-ruido-temperatura|Factor de Ruido y Temperatura Equivalente]]
- [[../../wiki/ruido/snr-modulacion-exponencial|SNR en Modulaciones Exponenciales]] — para el ítem d)
- [[../../wiki/derivaciones/modulacion-fm-carson|Derivación de FM y Regla de Carson]] — de dónde sale $\beta=\Delta f/W$
