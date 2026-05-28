---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_07/carta_36_formula-friis.md
curso: Sistemas de Comunicaciones
unidad: 7
---

# Fórmula de Friis para Sistemas en Cascada

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_07/carta_36_formula-friis]]]

## Enunciado

La fórmula de Friis calcula la figura de ruido total de $n$ dispositivos en cascada:

$$\boxed{F_{total} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots + \frac{F_n - 1}{\prod_{i=1}^{n-1} G_i}}$$

donde:
- $F_i$ = figura de ruido del $i$-ésimo dispositivo (lineal)
- $G_i$ = ganancia de potencia del $i$-ésimo dispositivo (lineal) [source — [[../../explicaciones_anki/unidad_07/carta_36_formula-friis]]]

## Implicaciones de Diseño

### La Primera Etapa Domina

$F_1$ contribuye directamente y completamente al ruido total. Las etapas posteriores se atenúan por la ganancia acumulada previa.

**Estrategia de diseño:**
1. Minimizar $F_1$ (LNA de bajo ruido)
2. Maximizar $G_1$ (suprime ruido de etapas posteriores)
3. Colocar dispositivos con peor $F$ después de suficiente ganancia

### Ejemplo Numérico

Cadena: LNA ($F_1 = 1.20$, $G_1 = 63.1$) → Filtro ($F_2 = 1.58$, $G_2 = 0.63$) → Mezclador ($F_3 = 5.01$)

$$F_{total} = 1.20 + \frac{0.58}{63.1} + \frac{4.01}{63.1 \times 0.63} = 1.462$$

$$NF_{total} = 1.65 \text{ dB}$$

### Orden Incorrecto

Si se coloca el mezclador primero: $NF_{total} = 8.59$ dB → **degradación de 6.8 dB**. Esto demuestra por qué el LNA debe ir siempre primero. [analysis]

## Errores Comunes

- **NUNCA sumar directamente en dB**: $NF_1 + NF_2 \neq NF_{total}$
- **Usar valores lineales** (no dB) en la fórmula
- **Restar 1** en los numeradores ($F_i - 1$)
- **Usar ganancia de potencia** ($G_{dB} = 10\log G$), no de voltaje

## Forma Alternativa con Temperaturas

$$T_{total} = T_1 + \frac{T_2}{G_1} + \frac{T_3}{G_1 G_2} + \cdots$$

## Ver también

- [[../ruido/factor-ruido-temperatura]] — Figura de ruido y temperatura equivalente
- [[../derivaciones/ecuacion-friis]] — Derivación completa de la fórmula
- [[../ruido/relacion-snr]] — Impacto de $F_{total}$ en la SNR del sistema
- [[../modulacion-analogica/receptor-superheterodino]] — Arquitectura típica donde se aplica Friis
- [[../../outputs/solutions/ejercicio_ruido_complete_20251115|Ejercicio de ruido resuelto]] — Aplicacion practica de Friis
