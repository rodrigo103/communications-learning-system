#!/usr/bin/env node
/**
 * Genera wiki/planificacion/diagramas-en-bloques.html desde el .md homónimo.
 *
 * Los bloques ```diagram del .md se dibujan como SVG inline (ver lib/diagram.mjs);
 * el resto del markdown se renderiza igual que el formulario (lib/mdrender.mjs).
 *
 * Uso:  npm install && node scripts/build-diagramas.mjs
 */

import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { convert, getWarnings, STYLE } from "./lib/mdrender.mjs";
import { renderDiagram, DIAGRAM_CSS } from "./lib/diagram.mjs";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const SRC = join(ROOT, "wiki/planificacion/diagramas-en-bloques.md");
const OUT = join(ROOT, "wiki/planificacion/diagramas-en-bloques.html");

const md = readFileSync(SRC, "utf8");
const content = convert(md, { renderDiagram });

const html = `<meta charset="utf-8">
<title>Diagramas en Bloques — Sistemas de Comunicaciones</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>${STYLE}
${DIAGRAM_CSS}</style>

<div class="sheet">
  <header class="top">
    <h1>Diagramas en Bloques — Sistemas de Comunicaciones</h1>
    <span class="tag">Final 30/07/2026 · 19:00 hs</span>
  </header>

  <div class="legend">
    <span>Cadenas de bloques de los sistemas del programa</span>
    <button class="print-btn no-print" onclick="window.print()">Imprimir / Guardar PDF</button>
  </div>

${content}

  <footer class="end">
    <span>Fuente: wiki/planificacion/diagramas-en-bloques.md · generado con scripts/build-diagramas.mjs</span>
    <span>Material de elaboración propia</span>
  </footer>
</div>
`;

writeFileSync(OUT, html);
const nDia = (html.match(/<figure class="dia">/g) || []).length;
console.log(`✓ ${OUT}`);
console.log(
  `  ${nDia} diagramas en SVG · ${(html.match(/<math/g) || []).length} fórmulas en MathML · ${(html.length / 1024).toFixed(0)} KB`
);
const warnings = getWarnings();
if (warnings) {
  console.error(`\n✗ ${warnings} problema(s) de tabla en el .md.`);
  process.exitCode = 1;
} else {
  console.log("  ✓ tablas consistentes");
}
