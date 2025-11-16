# Narrowband FM (NBFM) - Derivación Completa

**Fecha:** 2025-11-15
**Tema:** Modulación de Frecuencia de Banda Angosta

---

## 1. Punto de Partida: Modulación de Fase (PM)

### 1.1 Señal Modulada en Fase General

Una señal modulada en ángulo tiene la forma general:

$$s(t) = A_c \cos[\omega_c t + \phi(t)]$$

**Donde:**
- $A_c$ = amplitud constante de la portadora [V]
- $\omega_c = 2\pi f_c$ = frecuencia angular de la portadora [rad/s]
- $\phi(t)$ = fase instantánea variable [rad]

**Significado físico:** La información está codificada en la variación de la fase, NO en la amplitud (que permanece constante).

### 1.2 Modulación de Frecuencia (FM)

En FM, la frecuencia instantánea varía proporcionalmente al mensaje:

$$f_i(t) = f_c + k_f m(t)$$

**Donde:**
- $f_i(t)$ = frecuencia instantánea [Hz]
- $k_f$ = sensibilidad de frecuencia [Hz/V]
- $m(t)$ = señal de mensaje [V]

La frecuencia instantánea es la derivada de la fase:

$$f_i(t) = \frac{1}{2\pi}\frac{d\phi(t)}{dt}$$

Por lo tanto:

$$\frac{d\phi(t)}{dt} = 2\pi f_i(t) = 2\pi[f_c + k_f m(t)]$$

Integrando:

$$\phi(t) = 2\pi f_c t + 2\pi k_f \int_0^t m(\tau) d\tau$$

**Señal FM general:**

$$\boxed{s_{FM}(t) = A_c \cos\left[2\pi f_c t + 2\pi k_f \int_0^t m(\tau) d\tau\right]}$$

---

## 2. Señal de Mensaje Sinusoidal

Para análisis, consideramos mensaje sinusoidal:

$$m(t) = A_m \cos(2\pi f_m t)$$

### 2.1 Calcular la Integral

$$\int_0^t m(\tau) d\tau = \int_0^t A_m \cos(2\pi f_m \tau) d\tau$$

$$= A_m \frac{\sin(2\pi f_m t)}{2\pi f_m}$$

### 2.2 Índice de Modulación

Definimos el **índice de modulación de FM**:

$$\beta = \frac{\Delta f}{f_m} = \frac{k_f A_m}{f_m}$$

**Donde:**
- $\Delta f = k_f A_m$ = desviación máxima de frecuencia [Hz]
- $f_m$ = frecuencia del mensaje [Hz]

**Significado físico de $\beta$:**
- $\beta$ = relación entre desviación de frecuencia y frecuencia del mensaje
- $\beta \ll 1$: FM de banda angosta (NBFM)
- $\beta \gg 1$: FM de banda ancha (WBFM)

### 2.3 Sustituir en la Señal FM

$$s_{FM}(t) = A_c \cos\left[2\pi f_c t + 2\pi k_f \frac{A_m}{2\pi f_m}\sin(2\pi f_m t)\right]$$

$$s_{FM}(t) = A_c \cos\left[2\pi f_c t + \frac{k_f A_m}{f_m}\sin(2\pi f_m t)\right]$$

Usando $\beta = \frac{k_f A_m}{f_m}$:

$$\boxed{s_{FM}(t) = A_c \cos[2\pi f_c t + \beta \sin(2\pi f_m t)]}$$

Esta es la **forma general de FM con mensaje sinusoidal**.

---

## 3. Aproximación de Banda Angosta

### 3.1 Condición para NBFM

**Narrowband FM** ocurre cuando:

$$\boxed{\beta \ll 1}$$

Típicamente: $\beta < 0.3$ (o $\beta < 0.5$ según el criterio)

**¿Qué significa?** La desviación de frecuencia es mucho menor que la frecuencia del mensaje.

**Ejemplo:**
- FM comercial: $\beta = 5$ (banda ancha)
- NBFM: $\beta = 0.2$ (banda angosta)

### 3.2 Expansión usando Identidades Trigonométricas

Partimos de:

$$s_{FM}(t) = A_c \cos[2\pi f_c t + \beta \sin(2\pi f_m t)]$$

Usamos la identidad:

$$\cos(\alpha + \theta) = \cos\alpha \cos\theta - \sin\alpha \sin\theta$$

**Donde:**
- $\alpha = 2\pi f_c t$
- $\theta = \beta \sin(2\pi f_m t)$

$$s_{FM}(t) = A_c[\cos(2\pi f_c t)\cos(\beta \sin(2\pi f_m t)) - \sin(2\pi f_c t)\sin(\beta \sin(2\pi f_m t))]$$

### 3.3 Aproximación de Ángulo Pequeño

**Para $\beta \ll 1$:**

$$\cos(\beta \sin(2\pi f_m t)) \approx 1$$

$$\sin(\beta \sin(2\pi f_m t)) \approx \beta \sin(2\pi f_m t)$$

**¿Por qué?** Expansiones de Taylor para ángulos pequeños:
- $\cos(x) \approx 1 - \frac{x^2}{2} \approx 1$ para $x \ll 1$
- $\sin(x) \approx x - \frac{x^3}{6} \approx x$ para $x \ll 1$

Como $|\beta \sin(2\pi f_m t)| \leq \beta \ll 1$, estas aproximaciones son válidas.

### 3.4 Sustituir las Aproximaciones

$$s_{NBFM}(t) = A_c[\cos(2\pi f_c t) \cdot 1 - \sin(2\pi f_c t) \cdot \beta \sin(2\pi f_m t)]$$

$$\boxed{s_{NBFM}(t) = A_c \cos(2\pi f_c t) - A_c \beta \sin(2\pi f_c t) \sin(2\pi f_m t)}$$

---

## 4. Análisis Espectral: Expansión a Componentes de Frecuencia

### 4.1 Aplicar Identidad Producto-a-Suma

Para el término $\sin(2\pi f_c t) \sin(2\pi f_m t)$, usamos:

$$\sin A \sin B = \frac{1}{2}[\cos(A-B) - \cos(A+B)]$$

$$\sin(2\pi f_c t) \sin(2\pi f_m t) = \frac{1}{2}[\cos(2\pi(f_c - f_m)t) - \cos(2\pi(f_c + f_m)t)]$$

### 4.2 Forma Final de NBFM

$$s_{NBFM}(t) = A_c \cos(2\pi f_c t) - A_c \beta \cdot \frac{1}{2}[\cos(2\pi(f_c - f_m)t) - \cos(2\pi(f_c + f_m)t)]$$

$$s_{NBFM}(t) = A_c \cos(2\pi f_c t) - \frac{A_c \beta}{2}\cos(2\pi(f_c - f_m)t) + \frac{A_c \beta}{2}\cos(2\pi(f_c + f_m)t)$$

**Reordenando:**

$$\boxed{s_{NBFM}(t) = A_c \cos(2\pi f_c t) + \frac{A_c \beta}{2}\cos(2\pi(f_c + f_m)t) - \frac{A_c \beta}{2}\cos(2\pi(f_c - f_m)t)}$$

---

## 5. Componentes de Frecuencia

### 5.1 Tres Componentes

**Portadora:**
- Frecuencia: $f_c$
- Amplitud: $A_c$
- Fase: $0°$

**Banda Lateral Superior (USB):**
- Frecuencia: $f_c + f_m$
- Amplitud: $\frac{A_c \beta}{2}$
- Fase: $0°$ (componente coseno positivo)

**Banda Lateral Inferior (LSB):**
- Frecuencia: $f_c - f_m$
- Amplitud: $\frac{A_c \beta}{2}$
- Fase: $180°$ (componente coseno negativo)

### 5.2 Comparación con AM

**AM:**
$$s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{A_c \mu}{2}\cos(2\pi(f_c - f_m)t) + \frac{A_c \mu}{2}\cos(2\pi(f_c + f_m)t)$$

**NBFM:**
$$s_{NBFM}(t) = A_c \cos(2\pi f_c t) + \frac{A_c \beta}{2}\cos(2\pi(f_c + f_m)t) - \frac{A_c \beta}{2}\cos(2\pi(f_c - f_m)t)$$

**Diferencia clave:**
- AM: Ambas bandas laterales están **en fase** con la portadora
- NBFM: USB en fase, LSB **desfasada 180°**

Este desfasamiento de 180° es crucial y produce:
- Amplitud constante en FM (las variaciones se cancelan)
- La información está en la fase, no en la amplitud

---

## 6. Ancho de Banda de NBFM

### 6.1 Cálculo del Ancho de Banda

Desde el análisis espectral:
- Componente más baja: $f_c - f_m$
- Componente más alta: $f_c + f_m$

$$\boxed{BW_{NBFM} = 2f_m}$$

**¡Igual que AM!**

### 6.2 Comparación de Anchos de Banda

| Modulación | Ancho de Banda | Comentario |
|------------|----------------|------------|
| AM | $2f_m$ | Referencia |
| NBFM | $2f_m$ | Igual que AM |
| WBFM | $2(\Delta f + f_m)$ | Regla de Carson |

**Ejemplo numérico:**

Para audio: $f_m = 5$ kHz, $\Delta f = 1$ kHz ($\beta = 0.2$)

- NBFM: $BW = 2 \times 5 = 10$ kHz
- Si fuera WBFM con mismo $\Delta f$: $BW = 2(1 + 5) = 12$ kHz

---

## 7. Distribución de Potencia

### 7.1 Potencia de Cada Componente

**Potencia de portadora:**
$$P_c = \frac{A_c^2}{2R}$$

**Potencia de cada banda lateral:**
$$P_{SB} = \frac{(A_c \beta / 2)^2}{2R} = \frac{A_c^2 \beta^2}{8R}$$

**Potencia total:**
$$P_{total} = P_c + 2P_{SB} = \frac{A_c^2}{2R}\left(1 + \frac{\beta^2}{2}\right)$$

### 7.2 Aproximación para NBFM

Como $\beta \ll 1$, entonces $\beta^2 \ll \beta \ll 1$:

$$P_{total} \approx \frac{A_c^2}{2R}$$

**Conclusión:** Casi toda la potencia está en la portadora cuando $\beta$ es pequeño.

### 7.3 Eficiencia de Potencia

$$\eta = \frac{P_{sidebands}}{P_{total}} = \frac{\beta^2/2}{1 + \beta^2/2} \approx \frac{\beta^2}{2}$$

**Para $\beta = 0.2$:**
$$\eta = \frac{(0.2)^2}{2} = \frac{0.04}{2} = 0.02 = 2\%$$

**¡Eficiencia terrible!** Aún peor que AM (33% máximo).

**Pero:** En FM, la ventaja no es eficiencia de potencia, sino **inmunidad al ruido**.

---

## 8. Características de NBFM

### 8.1 Ventajas

1. **Ancho de banda limitado:** $BW = 2f_m$ (igual que AM)
2. **Amplitud constante:** Permite amplificadores clase C (más eficientes)
3. **Base para WBFM:** Se puede expandir usando multiplicadores de frecuencia
4. **Algo de inmunidad al ruido:** Mejor que AM (aunque no tanto como WBFM)

### 8.2 Desventajas

1. **Eficiencia de potencia baja:** Peor que AM
2. **Poca mejora de SNR:** No aprovecha la principal ventaja de FM
3. **Distorsión si $\beta$ no es suficientemente pequeño**

### 8.3 Aplicaciones

- **Comunicaciones móviles antiguas** (antes de digital)
- **Radio amateur de banda estrecha**
- **Sistemas de telemetría**
- **Etapa inicial en transmisores WBFM** (antes de multiplicación)

---

## 9. Generación de NBFM

### 9.1 Método de Modulador de Fase

```
m(t) ──→ [Integrador] ──→ [Modulador PM] ──→ NBFM
                            ↑
                        Portadora
```

**Razón:** FM = integral del mensaje aplicada a PM

### 9.2 Método de Desfasador

Se puede generar directamente sumando:
- Portadora
- Mensaje modulado en cuadratura (desfasado 90°)

Este es el **método de Armstrong** para NBFM.

---

## 10. Demodulación de NBFM

### 10.1 Discriminador de Frecuencia

Un discriminador convierte variaciones de frecuencia en variaciones de amplitud:

$$v_{out}(t) \propto \frac{df_i(t)}{dt} \propto m(t)$$

### 10.2 Detector de Fase (PLL)

Un Phase-Locked Loop puede demodular NBFM:
- Más robusto que discriminador
- Mejor rechazo de ruido
- Usado en sistemas modernos

---

## 11. Transición de NBFM a WBFM

### 11.1 Multiplicadores de Frecuencia

Para crear WBFM desde NBFM:

1. Generar NBFM con $\beta = 0.2$
2. Pasar por multiplicador ×N (N = 25 típico)
3. Resultado: $\beta_{out} = N \times \beta_{in} = 25 \times 0.2 = 5$

**También se multiplica $f_c$**, así que se usa mezclado posterior para bajar a frecuencia deseada.

### 11.2 Ventaja

Más fácil generar NBFM con buena linealidad y precisión, luego multiplicar.

---

## 12. Resumen de Fórmulas Clave

### Forma Compacta
$$\boxed{s_{NBFM}(t) = A_c \cos(2\pi f_c t) - A_c \beta \sin(2\pi f_c t) \sin(2\pi f_m t)}$$

### Forma Expandida (Componentes de Frecuencia)
$$\boxed{s_{NBFM}(t) = A_c \cos(2\pi f_c t) + \frac{A_c \beta}{2}\cos(2\pi(f_c + f_m)t) - \frac{A_c \beta}{2}\cos(2\pi(f_c - f_m)t)}$$

### Índice de Modulación
$$\boxed{\beta = \frac{\Delta f}{f_m} = \frac{k_f A_m}{f_m} \ll 1}$$

### Ancho de Banda
$$\boxed{BW_{NBFM} = 2f_m}$$

### Condición de Validez
$$\boxed{\beta < 0.3 \text{ (criterio estricto)}}$$

---

## 13. Comparación: NBFM vs AM vs WBFM

| Característica | AM | NBFM | WBFM |
|----------------|----|----|------|
| **Ancho de banda** | $2f_m$ | $2f_m$ | $2(\Delta f + f_m)$ |
| **Índice** | $\mu \leq 1$ | $\beta \ll 1$ | $\beta \gg 1$ |
| **Amplitud** | Variable | Constante | Constante |
| **Eficiencia** | 33% máx | ~2% | Baja |
| **Inmunidad ruido** | Pobre | Moderada | Excelente |
| **Complejidad** | Simple | Moderada | Alta |

---

## 14. Interpretación Física

### ¿Por qué las bandas laterales tienen signos opuestos?

En FM, la información está en las **variaciones de fase**, no de amplitud:

- Cuando la frecuencia aumenta ($f > f_c$): fase avanza más rápido
- Cuando la frecuencia disminuye ($f < f_c$): fase avanza más lento

Las bandas laterales con signos opuestos se combinan para:
- **Mantener amplitud constante** (se cancelan las variaciones de amplitud)
- **Crear variaciones de fase** (se suman las variaciones de fase)

**Esto es lo opuesto a AM**, donde ambas bandas suman en amplitud.

---

## 15. Conclusiones

1. **NBFM es una aproximación válida** cuando $\beta \ll 1$
2. **Espectro similar a AM** pero con LSB desfasada 180°
3. **Ancho de banda igual a AM**: $2f_m$
4. **Amplitud constante** (ventaja de FM conservada)
5. **Eficiencia de potencia peor que AM** (pero no es el objetivo)
6. **Útil como etapa intermedia** para generar WBFM
7. **Aplicaciones limitadas** hoy en día (reemplazado por digital)

**La principal lección:** NBFM muestra que FM puede ser compacta en espectro, pero pierde la principal ventaja de FM (gran mejora de SNR), que solo se obtiene con banda ancha ($\beta \gg 1$).

---

**Referencias para continuar:**
- Wideband FM (WBFM) y regla de Carson
- Funciones de Bessel en FM
- Pre-énfasis y de-énfasis
- Teorema de captura en FM
