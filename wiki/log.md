---
tags:
  - wiki/meta
---

# Changelog del Wiki

Registro cronologico de todas las actualizaciones al wiki de Sistemas de Comunicaciones.

---

## 2026-05-27

### Creacion inicial del vault

- **Infraestructura**: Creado `wiki/` con config Obsidian, skills (`wiki`, `check-commit`), plugin `wiki-nudge` y `AGENTS.md`.
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

### Contenido faltante: cartas Anki huerfanas y derivaciones paralelas

- **8 cartas Anki sin wiki** ahora tienen pagina:
  - `ruido/temperatura-ruido.md` — Temperatura equivalente de ruido Te (carta_34)
  - `ruido/ruido-banda-angosta.md` — Ruido banda angosta, I-Q, Rayleigh (carta_37)
  - `ruido/eficiencia-espectral-comparada.md` — Eficiencia espectral por sistema (carta_41)
  - `ruido/ganancia-procesamiento-pulsos.md` — Ganancia de procesamiento PCM (carta_42)
  - `ruido/efecto-enfasis-fm-am.md` — Enfasis en FM/AM, mejora 10-13 dB (carta_43)
  - `teoria-informacion/redundancia-compresion.md` — Redundancia y compresion (carta_46)
  - `espectro-expandido/prefijo-ciclico.md` — Prefijo ciclico en OFDM (carta_55)
  - `conceptos-integradores/eb-n0-vs-snr.md` — Eb/N0 vs SNR (carta_57)
- **3 derivaciones paralelas** ahora tienen pagina:
  - `derivaciones/modulacion-am-extendida.md` — AM extendida (424 lineas)
  - `derivaciones/modulacion-am-alternativa.md` — AM subagente (361 lineas)
  - `derivaciones/ecuacion-friis-extendida.md` — Friis extendida (621 lineas)
- Links bidireccionales agregados desde las paginas canonicas a las extendidas
- `index.md` actualizado con las 11 nuevas paginas
