---
tags:
  - wiki/introduccion
source_file: explicaciones_anki/unidad_01/carta_01_sistema-comunicaciones.md
curso: Sistemas de Comunicaciones
unidad: 1
---

# Modelo de Shannon: Componentes del Sistema de Comunicaciones

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Definicion

Un sistema de comunicaciones es un conjunto de elementos que permite la transferencia de informacion desde una fuente hasta un destino. El modelo formalizado por Claude Shannon en 1948 establece la arquitectura fundamental de todo sistema de comunicacion moderno.

## Componentes Fundamentales

El diagrama de bloques del modelo de Shannon es:

```
[Fuente] → [Transmisor] → [Canal] → [Receptor] → [Destino]
                              ↑
                           [Ruido]
```

### 1. Fuente de Informacion

La fuente genera el mensaje original. Caracteristicas:
- **Naturaleza**: analogica (voz, musica) o digital (datos, texto) [source]
- **Ancho de banda**: rango de frecuencias que ocupa la informacion (ej: voz 300-3400 Hz) [source]
- **Tasa de informacion**: cantidad de informacion generada por unidad de tiempo

### 2. Transmisor

Convierte el mensaje en una señal adecuada para el canal. Funciones:

$$\text{Informacion} \rightarrow \text{Codificacion} \rightarrow \text{Modulacion} \rightarrow \text{Amplificacion} \rightarrow \text{Antena/Medio}$$

- **Conversion de formato**: ADC/DAC [source]
- **Modulacion**: traslada la informacion a una frecuencia portadora adecuada [source]
- **Codificacion**: agrega redundancia para proteccion contra errores
- **Amplificacion**: proporciona potencia suficiente para transmision
- **Filtrado**: limita el ancho de banda

### 3. Canal de Comunicacion

Medio fisico por el cual viaja la señal. Tipos:
- **Guiados**: cable coaxial, fibra optica, par trenzado
- **No guiados**: espacio libre (radio) [source]

Caracteristicas del canal:
- **Atenuacion**: perdida de potencia con la distancia
- **Distorsion**: alteracion de la forma de la señal
- **Ruido**: señales no deseadas que se suman (ver [[ruido/fuentes-ruido]])
- **Ancho de banda**: rango de frecuencias que puede transmitir

### 4. Receptor

Realiza las operaciones inversas al transmisor:
- Amplificacion de bajo ruido
- **Demodulacion**: recupera la informacion de la portadora
- Decodificacion: detecta y corrige errores
- Conversion de formato y filtrado

### 5. Destino

Usuario final de la informacion: persona (altavoz, pantalla), computadora, actuador.

### 6. Ruido (Elemento Inevitable)

El ruido es inevitable en todo sistema real [source]:
- **Ruido termico**: presente en todos los dispositivos electronicos
- **Interferencia**: señales de otros sistemas
- **Distorsion**: no-linealidades del sistema

## Principios Clave

- **Universalidad**: este modelo aplica a TODOS los sistemas de comunicacion [source]
- **Procesamiento dual**: transmisor y receptor realizan operaciones inversas [analysis]
- **Ruido inevitable**: siempre presente, debe diseñarse considerandolo [source]

## Analogia: El Sistema Postal

| Componente | Analogia Postal |
|------------|-----------------|
| Fuente | Persona escribiendo carta |
| Transmisor | Oficina postal que empaqueta |
| Canal | Sistema de transporte |
| Receptor | Oficina postal destino |
| Destino | Persona recibiendo |
| Ruido | Cartas perdidas/dañadas |

## Ejemplo: Llamada Telefonica Movil

| Componente | Implementacion Real |
|------------|-------------------|
| Fuente | Voz (300-3400 Hz) |
| Transmisor | Telefono: digitaliza, codifica, modula a ~1.9 GHz |
| Canal | Aire + torres celulares |
| Receptor | Telefono receptor: demodula, decodifica, convierte a audio |
| Destino | Oido del receptor |
| Ruido | Interferencia, multitrayecto |

## Ver tambien

- [[introduccion/espectro-electromagnetico]]
- [[introduccion/necesidad-modulacion]]
- [[ruido/fuentes-ruido]]
- [[herramientas-matematicas/transformada-hilbert]]
