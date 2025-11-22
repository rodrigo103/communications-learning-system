# Informe de Revisión de Consistencia - Unidad 7: Ruido

**Fecha**: 2025-11-22
**Objetivo**: Verificar consistencia de fórmulas de ruido térmico en todas las cartas de la Unidad 7
**Revisión realizada por**: Claude Code (agente principal)

---

## 📋 Resumen Ejecutivo

✅ **Todas las cartas de la Unidad 7 ahora usan la convención moderna y consistente**:
- Densidad espectral: $N_0 = kT$ [W/Hz]
- Potencia total: $N = kTB$ [W]
- Valor estándar: $N_0 = -174$ dBm/Hz @ 290K

---

## 📚 Cartas Revisadas

### Carta 33: Ruido Blanco ✅ CORREGIDA

**Problemas encontrados**:
- ❌ Usaba $N_0 = 4kT$ (convención bilateral antigua)
- ❌ Cálculos numéricos con +6 dB de error

**Correcciones aplicadas**:
- ✓ Actualizada a $N_0 = kT$ (convención unilateral moderna)
- ✓ Recalculados todos los ejemplos numéricos
- ✓ Agregadas notas históricas explicando el factor 4 en voltaje
- ✓ Ejemplo FM: -115 dBm → -121 dBm (correcto)

**Cambios específicos**:
- Línea 106: $N_0 = 4kT$ → $N_0 = kT$
- Línea 145: Recalculado ejemplo FM (200 kHz @ 290K)
- Línea 168: Recalculado ejemplo WiFi
- Línea 255-261: Actualizadas fórmulas esenciales
- Línea 248-252: Nuevo error común sobre confusión 4kT

---

### Carta 34: Temperatura de Ruido ✅ YA CORRECTA + MEJORADA

**Estado original**: Correcta (usaba $N = kTB$)

**Mejoras aplicadas**:
- ✓ Agregada sección completa sobre relación $v_n^2 = 4kTRB$ ↔ $N = kTB$
- ✓ Derivación paso a paso desde voltaje a potencia disponible
- ✓ Explicación del factor 4R en adaptación de impedancias
- ✓ Ejemplo numérico verificando consistencia

---

### Carta 35: Figura de Ruido ✅ VERIFICADA CORRECTA

**Verificación**:
- ✓ Usa $N_{added} = kT_e B$ (correcto)
- ✓ Usa $N_0 = -174$ dBm/Hz @ 290K (correcto)
- ✓ Ejemplo 1 verificado: $N_{added} = 4.96 \times 10^{-14}$ W = -103.0 dBm ✓
- ✓ Fórmulas de conversión F ↔ NF ↔ Te clarificadas

**Mejoras aplicadas**:
- ✓ Aclaradas las "tres fórmulas de conversión" en línea 231-234

---

### Carta 36: Fórmula de Friis ✅ VERIFICADA CORRECTA

**Verificación**:
- ✓ No contiene cálculos directos de ruido térmico
- ✓ Usa figura de ruido F (adimensional)
- ✓ Fórmula de Friis aplicada correctamente
- ✓ No requiere correcciones

---

### Carta 37: Ruido de Banda Angosta ✅ VERIFICADA CORRECTA

**Verificación**:
- ✓ No contiene referencias a $N_0$ ni cálculos de potencia térmica
- ✓ Trata componentes I-Q del ruido (enfoque matemático/estadístico)
- ✓ No requiere correcciones

---

### Carta 38: Ruido en Receptor AM ✅ VERIFICADA CORRECTA

**Verificación**:
- ✓ Usa $N = kTB = -174 + 10\log(B)$ (correcto)
- ✓ Ejemplo verificado: B=6kHz → N=-136.2 dBm ✓
- ✓ Cálculo con convención moderna consistente
- ✓ No requiere correcciones

---

### Carta 39: Efecto Umbral en FM ✅ VERIFICADA CORRECTA

**Verificación**:
- ✓ No contiene cálculos directos de ruido térmico
- ✓ Trata el fenómeno del umbral (análisis cualitativo principalmente)
- ✓ No requiere correcciones

---

## 📄 Documentos Adicionales Creados

### aclaracion_densidad_espectral_ruido.md ✅ NUEVO

Documento completo que explica:
- La aparente contradicción entre Cartas 33 y 34
- Por qué $N_0 = 4kT$ vs $N_0 = kT$ vs $N = kTB$
- Convenciones bilateral vs unilateral
- Voltaje vs potencia disponible
- Ejemplos numéricos de verificación
- Recomendaciones de convención moderna

---

## 🔍 Verificaciones Numéricas Realizadas

### 1. Valor estándar de industria
```
N₀ @ 290K:
  Esperado: -174.0 dBm/Hz (estándar IEEE)
  Con N₀=kT: -174.0 dBm/Hz ✓
  Con N₀=4kT: -168.0 dBm/Hz ❌ (error de 6 dB)
```

### 2. Consistencia con fórmula de Nyquist
```
Voltaje: v_n² = 4kTRB
Potencia disponible: P = v_n²/(4R) = kTB ✓
Factor 4 se cancela correctamente
```

### 3. Ejemplo FM (B=200 kHz, T=290K)
```
ANTES: N = -115 dBm (con N₀=4kT) ❌
AHORA: N = -121 dBm (con N₀=kT) ✓
Diferencia: 6.0 dB = 10log₁₀(4) ✓
```

### 4. Ejemplo WiFi (B=20 MHz, T=400K)
```
N₀ = kT = 5.52×10⁻²¹ W/Hz ✓
N = 1.1×10⁻¹³ W = -100 dBm ✓
```

### 5. Ejemplo Carta 35 (Te=119.8K, B=30MHz)
```
N_added = kTeB = 4.96×10⁻¹⁴ W ✓
N_added = -103.0 dBm ✓
```

### 6. Ejemplo Carta 38 (B=6 kHz, T=290K)
```
N = -174 + 10log(6000) = -136.2 dBm ✓
Verificación con kTB: -136.2 dBm ✓
```

---

## ✅ Convención Estandarizada en Toda la Unidad 7

### Fórmulas oficiales del curso:

```
DENSIDAD ESPECTRAL (unilateral):
  N₀ = kT [W/Hz]
  N₀ = -174 dBm/Hz @ T=290K

POTENCIA TOTAL:
  N = N₀ × B = kTB [W]
  N_dBm = -174 + 10log₁₀(B) [dBm, B en Hz]

VOLTAJE DE RUIDO (Nyquist):
  v_n² = 4kTRB [V²]

RELACIÓN VOLTAJE → POTENCIA:
  P_disponible = v_n²/(4R) = kTB [W]
```

### Constantes:
```
k = 1.38×10⁻²³ J/K (Boltzmann)
T₀ = 290 K (temperatura de referencia estándar)
N₀ @ 290K = -174.0 dBm/Hz (memorizar!)
```

---

## 🎯 Impacto de las Correcciones

### Antes (con N₀=4kT):
- ❌ Error sistemático de +6 dB en todos los cálculos
- ❌ Inconsistencia con estándar de industria (-174 dBm/Hz)
- ❌ Contradicción entre Cartas 33 y 34
- ❌ Confusión sobre el factor 4

### Ahora (con N₀=kT):
- ✅ Cálculos correctos y verificados
- ✅ Consistente con IEEE/industria
- ✅ Sin contradicciones entre cartas
- ✅ Explicación clara del factor 4 (voltaje vs potencia)

---

## 📊 Estadísticas de la Revisión

| Métrica | Valor |
|---------|-------|
| Cartas revisadas | 7/7 (100%) |
| Cartas corregidas | 1 (Carta 33) |
| Cartas mejoradas | 2 (Cartas 34, 35) |
| Cartas ya correctas | 4 (Cartas 36, 37, 38, 39) |
| Cálculos verificados | 6 ejemplos numéricos |
| Documentos nuevos | 2 (aclaración + este informe) |
| Errores detectados | 0 (después de correcciones) |

---

## 🔒 Garantía de Consistencia

**Estado final**: ✅ **UNIDAD 7 COMPLETAMENTE CONSISTENTE**

Todas las cartas ahora:
- ✓ Usan la misma convención ($N_0 = kT$)
- ✓ Tienen cálculos numéricos verificados
- ✓ Son consistentes con estándares de industria
- ✓ Explican correctamente el factor 4 de Nyquist
- ✓ No tienen contradicciones entre sí

---

## 📚 Referencias para Estudiantes

**Si tienes dudas sobre el factor 4**:
- Lee: `aclaracion_densidad_espectral_ruido.md`
- Ver: Carta 34, sección "Relación entre ambas fórmulas"
- Ver: Carta 33, sección "Errores Comunes"

**Valores para memorizar**:
- $N_0 = -174$ dBm/Hz @ 290K
- $k = 1.38 \times 10^{-23}$ J/K
- Umbral AM ≈ 10 dB SNR

**Fórmulas clave**:
- Potencia de ruido: $N = kTB$
- Voltaje de Nyquist: $v_n^2 = 4kTRB$
- Temperatura equivalente: $T_e = T_0(F-1)$
- Fórmula de Friis: $F_{total} = F_1 + \frac{F_2-1}{G_1} + ...$

---

**Fin del informe**
**Próxima revisión recomendada**: Antes del examen final (verificar que no se hayan introducido inconsistencias nuevas)
