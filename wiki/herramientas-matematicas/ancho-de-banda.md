---
tags:
  - wiki/herramientas-matematicas
curso: Sistemas de Comunicaciones
unidad: 2
---

# Ancho de Banda

> **Last verified:** 2026-07-23 | **Verified by:** analysis

## Definicion

"Ancho de banda" no es un unico concepto — es una familia de medidas distintas que responden la misma pregunta ("¿cuanto espectro ocupa esta señal?") de formas diferentes, cada una util en un contexto distinto. No hay una pagina que las junte en la wiki hasta ahora; se usan en Nyquist, DEP, Carson, compromisos de diseño y en practicamente todas las formulas de ancho de banda del formulario, pero nunca se definen juntas. [analysis]

## Los distintos tipos de ancho de banda

### 1. Ancho de banda absoluto

El rango total de frecuencias donde la señal tiene contenido espectral estrictamente no nulo. Para la mayoria de las señales reales (ej. un pulso rectangular, cuyo espectro es un sinc que nunca llega exactamente a cero) esto es **infinito** — no es una medida practica para casi ninguna señal de interes.

### 2. Ancho de banda de -3dB (o de media potencia)

El rango de frecuencias donde la densidad espectral de potencia (o la respuesta de un filtro/sistema) cae a la mitad de su valor maximo — es decir, -3dB relativo al pico ($10\log_{10}(1/2)\approx-3$dB). Es la medida mas comun para caracterizar filtros y sistemas LTI.

### 3. Ancho de banda de nulo a nulo (null-to-null)

Para señales cuyo espectro tiene lobulos con nulos bien definidos (pulsos rectangulares, señales digitales moduladas), es la distancia entre el primer nulo espectral por debajo y por encima de la frecuencia central. Es la medida tipica en modulacion digital — ej. para una señal $M$-aria con tasa de simbolo $D$:

$$B_{null-null} = 2D$$

Ver ejemplo real en `exercises/finales/md/F_Comu_2026-02-26_res.md`, Ejercicio 3 (16-QAM).

### 4. Ancho de banda fraccional / porcentual

$$BW_{frac} = \frac{B}{f_c}$$

Expresado como porcentaje. Util para comparar sistemas a distinta frecuencia de portadora — es el concepto detras de por que a mayor $f_c$ hay mas $B$ absoluto disponible en la practica (sistemas de RF tipicamente manejan solo ~1-5% de $f_c$). Ver [[../introduccion/espectro-electromagnetico|Espectro Electromagnetico]].

### 5. Ancho de banda equivalente de ruido ($B_N$)

El ancho de un filtro **rectangular ideal** que dejaria pasar la misma potencia de ruido blanco que el filtro real (que tiene una respuesta mas gradual, no un corte abrupto). Formalmente, si $H(f)$ es la respuesta del filtro real con ganancia de pico $H_0$:

$$B_N = \frac{1}{H_0^2}\int_0^\infty |H(f)|^2\,df$$

Aparece explicito en varios finales como dato dado ("ancho de banda equivalente de ruido") en ejercicios de Ruido — no hace falta derivarlo, pero si entender que **no es lo mismo** que el ancho de banda de -3dB del mismo filtro (suelen ser parecidos pero no iguales).

## Conexion con la Densidad Espectral de Potencia

El area bajo la curva de DEP, integrada sobre una banda, da la potencia en esa banda:

$$P = \int_{BW} S_x(f)\,df$$

"Definir el ancho de banda" de una señal es, en el fondo, decidir donde cortar esa integral para capturar la parte relevante de la potencia — a -3dB, en el primer nulo, o al 99% de la energia total, segun el criterio que se use. Ver [[../herramientas-matematicas/densidad-espectral-potencia|Densidad Espectral de Potencia]].

## Conexion con Nyquist

El ancho de banda **minimo** para transmitir $R_s$ simbolos/segundo sin interferencia intersimbolica (ISI), con un filtro de Nyquist ideal, es:

$$B_{min} = \frac{R_s}{2}$$

Ver [[../conceptos-integradores/aportes-nyquist|Aportes de Nyquist]].

## Conexion con Carson (FM)

Caso particular de ancho de banda para modulacion angular (FM/PM), donde ni el ancho de banda absoluto ni el de -3dB son practicos (el espectro de FM tiene infinitas bandas laterales via Bessel) — se usa una aproximacion que captura ~98% de la potencia:

$$B_T \approx 2(\Delta f + f_m)$$

Ver [[../modulacion-analogica/ancho-banda-carson|Ancho de Banda de Carson]] (Dia 5 del plan, Unidad 3/4).

## Tabla resumen

| Tipo | Formula / criterio | Donde se usa |
|---|---|---|
| Absoluto | Rango total no nulo | Casi nunca practico (suele ser infinito) |
| -3dB (media potencia) | Caida a mitad de potencia del pico | Filtros, sistemas LTI en general |
| Nulo a nulo | Distancia entre primeros nulos | Modulacion digital (ASK/PSK/QAM) |
| Fraccional | $B/f_c$ | Comparar sistemas a distinta $f_c$ |
| Equivalente de ruido ($B_N$) | Filtro rectangular con misma potencia de ruido | Calculos de Ruido/SNR |
| Nyquist minimo | $R_s/2$ | Diseño sin ISI |
| Carson (FM) | $2(\Delta f+f_m)$ | Modulacion angular |

## Ver tambien

- [[../herramientas-matematicas/densidad-espectral-potencia|Densidad Espectral de Potencia]]
- [[../conceptos-integradores/aportes-nyquist|Aportes de Nyquist]]
- [[../modulacion-analogica/ancho-banda-carson|Ancho de Banda de Carson]]
- [[../conceptos-integradores/compromisos-diseno|Compromisos de Diseño]]
- [[../introduccion/espectro-electromagnetico|Espectro Electromagnetico]]
