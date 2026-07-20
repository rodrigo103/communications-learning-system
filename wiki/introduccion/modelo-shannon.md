---
tags:
  - wiki/introduccion
source_file: explicaciones_anki/unidad_01/carta_01_sistema-comunicaciones.md
curso: Sistemas de Comunicaciones
unidad: 1
---

# Modelo de Shannon: Componentes del Sistema de Comunicaciones

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_01/carta_01_sistema-comunicaciones]]]

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
- **Naturaleza**: analogica (voz, musica) o digital (datos, texto) [source — [[../../explicaciones_anki/unidad_01/carta_01_sistema-comunicaciones]]]
- **Ancho de banda**: rango de frecuencias que ocupa la informacion (ej: voz 300-3400 Hz) [source — [[../../explicaciones_anki/unidad_01/carta_01_sistema-comunicaciones]]]
- **Tasa de informacion**: cantidad de informacion generada por unidad de tiempo

### 2. Transmisor

Convierte el mensaje en una señal adecuada para el canal. Funciones:

$$\text{Informacion} \rightarrow \text{Codificacion} \rightarrow \text{Modulacion} \rightarrow \text{Amplificacion} \rightarrow \text{Antena/Medio}$$

> Nota: la lista de abajo enumera las funciones del transmisor, no repite el orden secuencial de la linea de arriba. Ese orden (codificar antes de modular) es el que importa: se protege la informacion con redundancia *antes* de subirla a la portadora. [analysis]
>
> "Conversion de formato" no es una caja aparte de la cadena de arriba: es el sub-paso inicial de **Codificacion** (ADC, si la fuente es analogica y hay que digitalizarla antes de poder codificar/modular) — y su espejo, el DAC, aparece al final del Receptor, justo antes del Destino (ver seccion 4 abajo, donde ya esta bien ordenado). Si la fuente ya es digital, se salta el ADC. [analysis]

- **Conversion de formato (ADC)**: digitaliza la fuente si es analogica — primer sub-paso de la codificacion [source — [[../../explicaciones_anki/unidad_01/carta_01_sistema-comunicaciones]]]
- **Codificacion**: agrega redundancia para proteccion contra errores (va antes de modular)
- **Modulacion**: traslada la informacion a una frecuencia portadora adecuada [source — [[../../explicaciones_anki/unidad_01/carta_01_sistema-comunicaciones]]]
- **Filtrado**: limita el ancho de banda (va despues de Modulacion, antes de Amplificacion — ver nota abajo)
- **Amplificacion**: proporciona potencia suficiente para transmision

> **¿Por que Filtrado va justo ahi (despues de Modulacion, antes de Amplificacion)?** [analysis]
> - *Despues de Modulacion, no antes*: recien cuando la señal esta sobre la portadora tiene sentido este filtrado — elimina componentes espectrales no deseadas que aparecen al modular/mezclar (bandas laterales no deseadas, productos de mezcla, imagenes).
> - *Antes de Amplificacion, no despues*: no tiene sentido gastar potencia del amplificador en amplificar contenido espectral que despues se va a descartar. Se filtra primero para quedarse solo con la señal util, y recien ahi se sube la potencia. Por eso Amplificacion queda como la ultima etapa activa antes de la antena.
> - Ejemplo real de esto en un final: `exercises/finales/md/F_Comu_2024-02-22_res.md`, Ejercicio 2 — transmisor de FM indirecto con la cadena **Modulador de FM → Filtro Pasabanda → Multiplicadores de frecuencia (×8) → Amplificador → Salida**. El filtro va pegado a la salida del modulador, y el amplificador queda al final.
> - En sistemas reales a veces hay un *segundo* filtro despues del amplificador (para limpiar armonicos que genera el propio amplificador de potencia), pero el modelo simplificado de este curso usa un unico bloque de Filtrado entre Modulacion y Amplificacion.

### 3. Canal de Comunicacion

Medio fisico por el cual viaja la señal. Tipos:
- **Guiados**: cable coaxial, fibra optica, par trenzado
- **No guiados**: espacio libre (radio) [source — [[../../explicaciones_anki/unidad_01/carta_01_sistema-comunicaciones]]]

Caracteristicas del canal:

- **Atenuacion**: perdida de potencia de la señal a medida que se propaga. [analysis]
  - *Medios guiados*: crece con la distancia expresada en dB (constante de atenuacion $\alpha$ en dB/km) y tambien con la frecuencia (efecto pelicular en cables de cobre, absorcion en fibra).
  - *Medios no guiados (espacio libre)*: perdida de trayecto en espacio libre, $L_{fs}(\text{dB}) = 20\log_{10}d + 20\log_{10}f + 32{,}44$ ($d$ en km, $f$ en MHz) — la potencia cae con $1/d^2$ en espacio libre puro (mas rapido en entornos reales con reflexiones, ej. terrestre $\approx 1/d^4$).
  - Idealmente es un efecto **lineal** e independiente de la frecuencia dentro de la banda de la señal: escala la amplitud pero no cambia la forma de onda. En la practica suele depender de la frecuencia, lo cual la conecta con la distorsion (ver abajo).
  - Consecuencia directa: al llegar mas debil al receptor empeora la SNR (el ruido del receptor no cambia, la potencia de señal si) — de ahi la necesidad de amplificadores/repetidores y el vinculo con la Unidad 7 (Ruido, ver [[../ruido/formula-friis]]).

- **Distorsion**: cambio en la **forma** de la señal, no solo en su amplitud — el canal deja de comportarse como un simple atenuador con retardo. [analysis]
  - *Condicion de canal sin distorsion*: $y(t) = K \cdot x(t-t_0)$, equivalente en frecuencia a $H(f) = K\,e^{-j2\pi f t_0}$ — modulo constante ($|H(f)|=K$) y fase lineal en toda la banda de la señal.
  - *Distorsion de amplitud*: $|H(f)|$ no es constante dentro de la banda — atenua distinto cada componente de frecuencia (no agrega frecuencias nuevas, pero cambia el peso relativo entre las que ya estaban).
  - *Distorsion de fase / retardo de grupo*: la fase de $H(f)$ no es lineal con $f$ — cada componente de frecuencia llega con un retardo distinto y la señal se "esparce" en el tiempo (causa interferencia intersimbolica, ISI, en sistemas digitales).
  - *Distorsion no lineal*: producida por elementos no lineales del sistema (ej. amplificadores saturados). A diferencia de las dos anteriores (que son lineales), esta **si genera componentes de frecuencia nuevas** — armonicos y productos de intermodulacion que no estaban en la señal original.
  - *Diferencia clave con el ruido*: la distorsion es **deterministica** (depende de la respuesta del canal/sistema, se puede caracterizar y en principio corregir con un ecualizador); el ruido es **aleatorio** y no se puede deshacer una vez sumado.

- **Ruido**: señales no deseadas que se suman (ver [[../ruido/fuentes-ruido]])
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

El ruido es inevitable en todo sistema real [source — [[../../explicaciones_anki/unidad_01/carta_01_sistema-comunicaciones]]]:
- **Ruido termico**: presente en todos los dispositivos electronicos
- **Interferencia**: señales de otros sistemas
- **Distorsion**: no-linealidades del sistema

> El diagrama dibuja la flecha de ruido solo sobre el canal como simplificacion (modelo AWGN). En la practica el ruido se origina en cada etapa — transmisor, canal y receptor — y suele dominar el ruido termico de la **primera etapa del receptor** (por eso existe el LNA). La Unidad 7 desagrega esto etapa por etapa con la formula de Friis en cascada: ver [[../ruido/formula-friis]]. [analysis]

## Principios Clave

- **Universalidad**: este modelo aplica a TODOS los sistemas de comunicacion [source — [[../../explicaciones_anki/unidad_01/carta_01_sistema-comunicaciones]]]
- **Procesamiento dual**: transmisor y receptor realizan operaciones inversas [analysis]
- **Ruido inevitable**: siempre presente, debe diseñarse considerandolo [source — [[../../explicaciones_anki/unidad_01/carta_01_sistema-comunicaciones]]]

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

- [[../introduccion/espectro-electromagnetico]]
- [[../introduccion/necesidad-modulacion]]
- [[../ruido/fuentes-ruido]]
- [[../herramientas-matematicas/transformada-hilbert]]
- [[../../outputs/mindmaps/communications_systems_course_overview_20251116|Mapa mental del curso]] — Vista general de todos los temas
