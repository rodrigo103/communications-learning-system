# Solución — FM con multiplicador de frecuencia

**Origen del enunciado:** `exercises/finales/md/F_Comu_2023-02-16.md`, Ejercicio 1 (Modulación exponencial, 2,5 puntos)
**Resuelto:** 2026-07-26 (Día 2 del plan, bloque FM)
**Nota:** el PDF original es un examen **en blanco** — esta resolución es propia, no de un estudiante. Por eso vive acá y no dentro del archivo del final (ese corpus se mantiene con resoluciones reales únicamente, porque se usa como evidencia empírica para el plan de estudio).

---

## Formulario mínimo de FM

$$s_{FM}(t) = A_c\cos\big(2\pi f_ct + \beta\sin(2\pi f_mt)\big)$$

| Fórmula | Qué es |
|---|---|
| $f_i(t) = f_c + \Delta f\cos(2\pi f_mt)$ | Frecuencia instantánea (derivada de la fase $/2\pi$) |
| $\boxed{\Delta f = \beta f_m}$ | Desviación máxima de frecuencia |
| $\boxed{\beta = \Delta f/f_m}$ | Índice de modulación (adimensional) |
| $\boxed{B_T = 2(\Delta f + f_m) = 2f_m(\beta+1)}$ | **Regla de Carson** |
| $\boxed{P = \dfrac{A_c^2}{2R}}$ | Potencia — **constante, no depende de la modulación** |

### Las dos trampas a tener automatizadas

1. **La potencia en FM no cambia con la modulación.** Amplitud constante siempre → $P=A_c^2/2R$ pase lo que pase con $\beta$. Distinto de AM, donde modular sube la potencia total.
2. **Multiplicador de frecuencia $\times n$**: multiplica **la fase entera**, entonces $f_c\to nf_c$, $\Delta f\to n\Delta f$, $\beta\to n\beta$ — pero **$f_m$ NO cambia**, y la amplitud tampoco. Es el patrón que más se repite en los finales de FM. Justificación matemática completa (por qué $\beta$ escala y $f_m$ no, y en qué se diferencia de un mezclador) en [[../../wiki/derivaciones/modulacion-fm-carson#Multiplicadores y mezcladores de frecuencia (el patrón más testeado)|Derivación de FM — Multiplicadores y mezcladores]].

---

## Enunciado

Una portadora se modula en frecuencia con una onda senoidal resultando:

$$X_c(t) = 100\cos\big(2\pi f_ct + 6\,\text{sen}(4000\pi t)\big)$$

Siendo $f_c=100$ MHz. Determinar:

a) Máxima desviación de frecuencia instantánea. [0,5 pts]
b) Ancho de banda. [0,5 pts]
c) Si la amplitud de la modulante se triplica, evaluar el nuevo ancho de banda. [0,5 pts]
d) Si a la portadora modulada obtenida en c) se la pasa por un cuadruplicador de frecuencia (amplitud sin cambio), hallar la expresión matemática. [0,5 pts]
e) Potencia normalizada y ancho de banda de la expresión de d). [0,5 pts]

---

## Resolución

**Datos leídos del enunciado:** $\beta=6$; de $4000\pi t = 2\pi f_mt$ → $f_m = 2000$ Hz; $A_c = 100$ V.

**a) Desviación máxima de frecuencia**

$$\Delta f = \beta f_m = 6\times2000 = \boxed{12\text{ kHz}}$$

**b) Ancho de banda (Carson)**

$$B_T = 2(\Delta f+f_m) = 2(12+2) = \boxed{28\text{ kHz}}$$

**c) Amplitud de la modulante triplicada**

Como $\Delta f = k_fA_m$, triplicar $A_m$ triplica $\Delta f$ — pero **$f_m$ no cambia**:

$$\Delta f = 36\text{ kHz}, \qquad \beta = \frac{36}{2} = 18, \qquad B_T = 2(36+2) = \boxed{76\text{ kHz}}$$

**d) Cuadruplicador de frecuencia**

Multiplica la fase entera por 4: $4\times(2\pi f_ct + 18\sin(4000\pi t)) = 2\pi(4f_c)t + 72\sin(4000\pi t)$. Entonces $f_c\to400$ MHz, $\beta\to72$, amplitud sin cambio:

$$\boxed{X(t) = 100\cos\big(2\pi\cdot400\times10^6\,t + 72\,\text{sen}(4000\pi t)\big)}$$

**e) Potencia normalizada y ancho de banda de d)**

Potencia (normalizada, $R=1$) — no cambió en ningún momento del ejercicio, porque la amplitud nunca se tocó:

$$P = \frac{A_c^2}{2} = \frac{100^2}{2} = \boxed{5000\text{ W}}$$

Ancho de banda: $\Delta f = \beta f_m = 72\times2 = 144$ kHz →

$$B_T = 2(144+2) = \boxed{292\text{ kHz}}$$

---

## Patrón a reconocer

Todo el ejercicio es **la misma fórmula de Carson aplicada cuatro veces**, cambiando solo qué le pasó a $\Delta f$ y a $f_m$ en cada etapa:

| Etapa | $\Delta f$ | $f_m$ | $\beta$ | $B_T$ |
|---|---|---|---|---|
| Original | 12 kHz | 2 kHz | 6 | 28 kHz |
| Modulante $\times3$ | 36 kHz | 2 kHz | 18 | 76 kHz |
| $+$ cuadruplicador | 144 kHz | 2 kHz | 72 | 292 kHz |

$f_m$ constante en toda la tabla — ni triplicar la amplitud de la modulante ni multiplicar la frecuencia lo tocan. Ese es el error clásico a evitar.

## Ver también

- [[../../wiki/derivaciones/modulacion-fm-carson|Derivación de FM y Regla de Carson]]
- [[../../wiki/modulacion-analogica/fm-banda-angosta|FM Banda Angosta vs Banda Ancha]]
- [[../../wiki/modulacion-analogica/modulador-armstrong|Modulador Armstrong]] — moduladores indirectos con multiplicadores
- [[../../wiki/planificacion/formulario-imprimible|Formulario Imprimible]]
