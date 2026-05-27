---
tags:
  - wiki/meta
---

# Changelog del Wiki

Registro cronologico de todas las actualizaciones al wiki de Sistemas de Comunicaciones.

---

## 2026-05-27

### Creacion inicial del vault

- **Infraestructura**: Creado `.opencode/wiki/` con config Obsidian, skills (`wiki`, `check-commit`), plugin `wiki-nudge` y `AGENTS.md`.
- **Estructura**: Definidas 14 categorias de conocimiento:
  - `introduccion/` — Fundamentos y modelo de Shannon
  - `herramientas-matematicas/` — Parseval, Fourier, Hilbert, muestreo
  - `modulacion-analogica/` — AM, DSB, SSB, FM, PM, Carson
  - `modulacion-pulsos/` — PCM, Delta, companding
  - `modulacion-digital/` — ASK, FSK, PSK, QAM
  - `ruido/` — Friis, SNR, intercomparacion
  - `teoria-informacion/` — Entropia, Shannon-Hartley, codigos
  - `espectro-expandido/` — CDMA, DSSS, FHSS, OFDM
  - `conceptos-integradores/` — Comparaciones globales
  - `derivaciones/` — Derivaciones matematicas completas
  - `resumenes/` — Mindmaps y overviews
  - `problemas/` — Soluciones de ejercicios
  - `planificacion/` — Programa, progreso, mazo
  - `sesiones/` — Logs de estudio

- **Paginas creadas** (total: ~70):
  - `index.md` — Tabla de contenidos con wikilinks a todas las paginas
  - `log.md` — Este changelog
  - Todas las paginas de contenido desde archivos fuente en `outputs/`, `explicaciones_anki/`, `ProgramaSistemasDeComunicaciones.md` y `Mazo_Anki_Sistemas_Comunicaciones.md`
  - Archivos originales preservados intactos en sus ubicaciones actuales

### Correccion de wikilinks rotos

- **20 paginas stub creadas** como alias/sinonimos (ej: `tdm` → `multiplex-tdm`, `pcm` → `pcm-cuantificacion`, `entropia` → `entropia-fuente`)
- **3 wikilinks corregidos** en paginas fuente (`modulacion-pulsos/teorema-muestreo` → `herramientas-matematicas/teorema-muestreo`)
- **Resultado final**: 95 paginas, 607 wikilinks totales, 146 wikilinks unicos, **0 links rotos**
