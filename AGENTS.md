# Communications Learning System

Plataforma de aprendizaje para Sistemas de Comunicaciones (UTN). Ayuda a preparar examenes mediante estudio de teoria y practica de problemas.

## Quick Reference

- `python main.py` — CLI principal
- `python -m pytest tests/ -v` — Tests
- Agentes disponibles: `formula-deriver`, `exercise-solver`, `progress-analyzer`, `study-session-manager`, `anki-explainer`, `mindmap-generator`

## Arquitectura

- Coordinador central en `agents/coordinator.py`
- Agentes definidos en `.claude/agents/`
- Estado de aprendizaje en `state/`
- Sesiones en `sessions/`

---

# LLM Wiki

El proyecto tiene un wiki persistente en `wiki/` que compila y conecta todo el conocimiento del curso.

## Cuando leer el wiki — OBLIGATORIO

**Siempre, sin excepcion, lee la wiki ANTES de responder cualquier consulta del curso.**

Categorias cubiertas:
- Introduccion y fundamentos
- Herramientas matematicas (Fourier, Parseval, Hilbert, muestreo)
- Modulacion analogica (AM, DSB, SSB, FM, PM)
- Modulacion de pulsos (PCM, Delta, companding)
- Modulacion digital (ASK, FSK, PSK, QAM, constelaciones)
- Ruido e intercomparacion (Friis, SNR, efecto umbral)
- Teoria de la informacion (entropia, Shannon-Hartley, codigos)
- Espectro expandido (CDMA, DSSS, FHSS, OFDM)
- Derivaciones matematicas completas
- Resumenes y mapas mentales
- Problemas resueltos
- Planificacion y progreso

Hacer `/wiki search <tema>` o leer directamente en `wiki/`.

## Cuando escribir al wiki

Despues de finalizar una sesion de estudio, compilar conocimiento al wiki si se trata de:
- Una derivacion matematica nueva
- Una solucion de problema con patrones reusables
- Una explicacion de concepto que conecta multiples temas
- Un mapa mental o resumen integrador
- Un descubrimiento sobre estrategias de examen

**IMPORTANTE**: Despues de cambios significativos en archivos fuente (`outputs/`, `explicaciones_anki/`), **revisa si las paginas del wiki necesitan actualizarse**. Busca archivos mencionados en el wiki (`grep` de `source_file:` en `wiki/`). Si encontras referencias a contenido que cambio, actualiza la pagina y agrega entrada en `log.md`.

El skill `check-commit` incluye un paso de wiki review antes del commit.

Hacer `/wiki ingest` para procesar archivos en `raw/` o `/wiki ingest <topic>` para compilar conocimiento desde archivos fuente.

## Formato de paginas

Toda pagina debe tener:

```markdown
---
tags:
  - wiki/categoria
source_file: path/to/original.md
---

# Titulo

> **Last verified:** YYYY-MM-DD | **Verified by:** [source|analysis|gap]

Contenido con claim types...
```

### Claim types

| Tag | Uso |
|-----|-----|
| `[source]` | Verificado del programa oficial o bibliografia |
| `[analysis]` | Conclusion derivada de evidencia |
| `[unverified]` | Suposicion sin chequear contra fuente |
| `[gap]` | Tema conocido como pendiente de estudio |

### Cross-links

Usar `[[ruta/sin-extension]]` para enlazar paginas. Ej: `[[modulacion-analogica/am-vs-dsb-sc]]`.

### Notacion matematica

Usar `$$...$$` para ecuaciones en bloque y `$...$` para inline. Encerrar formulas clave con `\boxed{...}`.

### Lint

`/wiki lint` chequea: links rotos, paginas huerfanas, info stale (>30 dias), `[unverified]` abundantes.

## Estructura del wiki

```
wiki/
├── raw/                         # Inbox — drop files aqui
├── index.md                     # TOC auto-mantenido
├── log.md                       # Changelog cronologico
├── introduccion/                # Conceptos fundamentales (U1)
├── herramientas-matematicas/    # Fourier, Parseval, Hilbert, muestreo
├── modulacion-analogica/        # AM, DSB, SSB, FM, PM
├── modulacion-pulsos/           # PCM, Delta, companding
├── modulacion-digital/          # ASK, FSK, PSK, QAM
├── ruido/                       # Ruido, Friis, SNR, intercomparacion
├── teoria-informacion/          # Entropia, Shannon-Hartley, codigos
├── espectro-expandido/          # CDMA, DSSS, FHSS, OFDM
├── conceptos-integradores/      # Comparaciones globales
├── derivaciones/                # Derivaciones matematicas completas
├── resumenes/                   # Mapas mentales y overviews
├── problemas/                   # Soluciones de ejercicios
├── planificacion/               # Programa, progreso, mazo Anki
└── sesiones/                    # Logs de sesiones de estudio
```
