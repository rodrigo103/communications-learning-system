---
tags:
  - wiki/meta
---

# Changelog del Wiki

Registro cronologico de todas las actualizaciones al wiki de Sistemas de Comunicaciones.

---

## 2026-06-02

### Wikilinks desde conversaciones Claude

- **Conversaciones**: Incorporados 13 archivos historicos de conversaciones con Claude (`claude-conversations/`) como vault de Obsidian.
- **Pagina indice**: Creada `sesiones/conversaciones-claude.md` con mapeo de 11 conversaciones de contenido del curso a paginas del wiki.
- **Links reciprocos**: Agregados enlaces desde 26 paginas del wiki (`Ver tambien`) hacia las conversaciones relevantes:
  - `ruido/` (7 paginas): formula-friis, factor-ruido-temperatura, relacion-snr, lna-diseno-receptor, intercomparacion-sistemas, temperatura-ruido, problemas/ejercicio-ruido
  - `modulacion-analogica/` (3): ancho-banda-carson, fm-estereo, fm-vs-pm
  - `modulacion-digital/` (3): comparacion-digital-analogica, ask-fsk-psk, constelaciones
  - `herramientas-matematicas/` (3): teorema-parseval, senales-energia-potencia, teorema-muestreo, transformada-fourier
  - `teoria-informacion/` (3): teorema-shannon-hartley, capacidad-canal-shannon, sistema-ideal-comunicaciones
  - `planificacion/` (3): mazo-anki, progreso-actual, programa-oficial
  - `conceptos-integradores/` (1): evolucion-sistemas
  - `sesiones/` (1): 2025-11-15-sesion
  - `modulacion-pulsos/` (1): muestreo-ideal-natural
- **Index**: Actualizado `wiki/index.md` con link a la nueva pagina.

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

### Unificacion de duplicados y archivos huerfanos

- **3 pares duplicados unificados** en `explicaciones_anki/`:
  - `carta_01_sistemas_comunicaciones` → mergeado en `carta_01_sistema-comunicaciones`
  - `carta_02_modulacion` → mergeado en `carta_02_necesidad-modulacion`
  - `carta_04_teorema_parseval` → mergeado en `carta_04_teorema-parseval`
  - Archivos sobrantes eliminados
- **Nueva pagina wiki**: `ruido/aclaracion-densidad-espectral-ruido.md` desde archivo fuente previamente huerfano
- **Nueva pagina wiki**: `resumenes/resumen-modulacion-digital.md` desde `outputs/unidad_6_modulacion_digital_resumen.md`
- **Conexiones fortalecidas**: wikilinks agregados a `fuentes-ruido`, `temperatura-ruido`, `formula-friis`, `modelo-shannon`, `programa-oficial`, `comparacion-digital-analogica`, `necesidad-modulacion`
- Resultado: 0 archivos fuente huerfanos, 1058 wikilinks, 0 rotos
