# Solución — Teoría de la Información: entropía de una fuente de texto

**Origen del enunciado:** `exercises/finales/md/F_Comu_2024-11-14_res.md`, Ejercicio 4 (2,5 puntos)
**Verificado contra la resolución del estudiante** (examen resuelto del corpus).

> ⚠️ **El patrón de TI más frecuente del corpus: aparece en 7 de los 42 finales únicos** — `F_Comu_2019-07-17`, `F_Comu_2022-05-26`, `F_Comu_2022-12-01`, `F_Comu_2023-08-03_res`, `F_Comu_2024-11-14_res`, `F_Comu_2025-02-20_res`, `F_Comu_2026-02-26_res`.
>
> Es el caso **no equiprobable**, donde **no sirve** $H=\log_2M$ y hay que hacer la suma completa.

---

## Enunciado

Sobre un enlace asincrónico con tasa de transmisión binaria de **28.800 bps** se transmiten caracteres alfanuméricos codificados con **12 binits por carácter** (ASCII de 8 binits + 1 de paridad + 1 de comienzo + 2 de parada).

a) ¿Cuántos caracteres por segundo se pueden transmitir como máximo? [0,5 pts]
b) Si una página contiene 600 palabras de 6 caracteres promedio más un espacio entre palabras, ¿cuánto tarda en transmitirse una página? [0,75 pts]
c) Si el espacio tiene probabilidad $1/7$, cada una de las 10 vocales (may. y min.) $3/56$, y el resto son 72 caracteres equiprobables: determinar la información promedio **por palabra** ($H$, incluyendo el espacio). [0,75 pts]
d) Determinar la tasa de información transmitida en esas condiciones. [0,5 pts]

---

## Resolución

### a) Caracteres por segundo

$$r = \frac{r_b}{\bar N} = \frac{28\,800\ \text{binits/s}}{12\ \text{binits/carácter}} = \boxed{2400\ \text{caracteres/s}}$$

> Notar la contabilidad de unidades: binits/s ÷ binits/carácter = caracteres/s. Los 12 binits **no son 12 bits de información** — incluyen paridad, arranque y parada, que son *overhead* del protocolo asincrónico.

### b) Tiempo por página

$$\text{caracteres/página} = 600\ \tfrac{\text{palabras}}{\text{pág}} \times 7\ \tfrac{\text{caracteres}}{\text{palabra}} = 4200$$

(7 = 6 letras + 1 espacio, "todas las palabras terminan con espacio")

$$T = \frac{4200\ \text{caracteres}}{2400\ \text{caracteres/s}} = \boxed{1{,}75\ \text{s}}$$

### c) Entropía — el ítem clave

**Paso 1 — completar las probabilidades.** Las de los 72 caracteres restantes salen de que todo debe sumar 1:

$$p_{resto} = \frac{1 - \tfrac17 - 10\cdot\tfrac{3}{56}}{72} = \frac{1 - 0{,}1429 - 0{,}5357}{72} = \frac{0{,}3214}{72} = \frac{1}{224}$$

| Grupo | Cantidad | $p_i$ c/u | $\sum p$ |
|---|---|---|---|
| Espacio | 1 | $1/7 = 0{,}1429$ | $0{,}1429$ |
| Vocales | 10 | $3/56 = 0{,}0536$ | $0{,}5357$ |
| Resto | 72 | $1/224 = 0{,}00446$ | $0{,}3214$ |
| | **83** | | **1,0000** ✓ |

**Paso 2 — entropía por carácter**, con $H=\sum p_i\log_2\frac{1}{p_i}$:

$$H = \underbrace{\tfrac17\log_2 7}_{0{,}401} + \underbrace{10\cdot\tfrac{3}{56}\log_2\tfrac{56}{3}}_{2{,}262} + \underbrace{72\cdot\tfrac{1}{224}\log_2 224}_{2{,}510} = \boxed{5{,}17\ \text{bits/carácter}}$$

**Paso 3 — por palabra** (lo que pide el enunciado):

$$H_{palabra} = 5{,}17\ \tfrac{\text{bits}}{\text{carácter}} \times 7\ \tfrac{\text{caracteres}}{\text{palabra}} = \boxed{36{,}2\ \text{bits/palabra}}$$

> **Por qué se puede multiplicar por 7**: la entropía es **aditiva para símbolos independientes**, $H(S^s)=s\,H(S)$. Cada palabra son 7 caracteres, así que su información es 7 veces la de un carácter.

### d) Tasa de información

$$R = r\,H = 2400\ \tfrac{\text{caracteres}}{\text{s}} \times 5{,}17\ \tfrac{\text{bits}}{\text{carácter}} = \boxed{12\,408\ \text{bps}}$$

---

## Lo que este ejercicio enseña

**El contraste binit / bit, en números concretos:**

| Magnitud | Valor |
|---|---|
| Flujo binario en el canal | **28.800 binits/s** |
| Binits por carácter | 12 (8 ASCII + 1 paridad + 1 arranque + 2 parada) |
| **Información real** por carácter | **5,17 bits** |
| Tasa de **información** | **12.408 bps** |
| **Eficiencia** | $12\,408/28\,800 = \mathbf{43\%}$ |

**Menos de la mitad del flujo binario transporta información.** El resto se va en dos cosas distintas:

1. **Overhead de protocolo** (4 de los 12 binits: paridad, arranque, parada) → no es información del mensaje
2. **Redundancia estadística** (los caracteres no son equiprobables: $H=5{,}17$ contra $\log_2 83 = 6{,}38$ bits que tendría una fuente equiprobable de 83 símbolos) → es lo que la compresión eliminaría

> **El error a evitar**: usar $H=\log_2 M$. Acá daría $\log_2 83 = 6{,}38$ bits/carácter, un 23% más que el valor real. Esa fórmula **solo vale si todos los símbolos son equiprobables**, y el enunciado dice explícitamente que no lo son.

## Ver también

- [[../../wiki/teoria-informacion/ti-formulario-examen|TI — Formulario de examen]]
- [[../../wiki/teoria-informacion/entropia-fuente|Entropía de Fuente]]
- [[../../wiki/teoria-informacion/redundancia-compresion|Redundancia y Compresión]]
