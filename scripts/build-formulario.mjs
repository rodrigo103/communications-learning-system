#!/usr/bin/env node
/**
 * Genera wiki/planificacion/formulario-imprimible.html desde el .md homónimo.
 *
 * El .md es la fuente única: las fórmulas van en LaTeX y acá se convierten a
 * MathML nativo (ver lib/mdrender.mjs). El HTML resultante es autocontenido.
 *
 * Uso:  npm install && node scripts/build-formulario.mjs
 */

import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { convert, getWarnings, STYLE } from "./lib/mdrender.mjs";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const SRC = join(ROOT, "wiki/planificacion/formulario-imprimible.md");
const OUT = join(ROOT, "wiki/planificacion/formulario-imprimible.html");

// ─── main ────────────────────────────────────────────────────────────────────
const md = readFileSync(SRC, "utf8");
const content = convert(md);

// El charset va explícito: el archivo se abre como file:// desde el disco, donde
// no hay header HTTP que lo declare, y sin esto Chrome lo lee como Latin-1.
const html = `<meta charset="utf-8">
<title>Formulario — Sistemas de Comunicaciones</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>${STYLE}</style>

<div class="sheet">
  <header class="top">
    <h1>Formulario — Sistemas de Comunicaciones</h1>
    <span class="tag">Final 30/07/2026 · 19:00 hs</span>
  </header>

  <div class="legend">
    <span><b style="color:var(--mem)">●</b> de memoria</span>
    <span><b>°</b> cero apariciones en los 42 finales — baja prioridad</span>
    <span><b>%</b> frecuencia sobre 42 finales únicos</span>
    <button class="print-btn no-print" onclick="window.print()">Imprimir / Guardar PDF</button>
  </div>

${content}

  <footer class="end">
    <span>Fuente: wiki/planificacion/formulario-imprimible.md · generado con scripts/build-formulario.mjs</span>
    <span>Consolidado sobre 42 finales únicos (2019-2026) + los 7 formularios por tema</span>
  </footer>
</div>
`;

writeFileSync(OUT, html);
console.log(`✓ ${OUT}`);
console.log(`  ${(html.match(/<math/g)||[]).length} fórmulas convertidas a MathML · ${(html.length / 1024).toFixed(0)} KB`);
const warnings = getWarnings();
if (warnings) {
  console.error(`\n✗ ${warnings} problema(s) de tabla en el .md — el HTML salió igual, pero Obsidian los va a renderizar mal.`);
  process.exitCode = 1;
} else {
  console.log("  ✓ tablas consistentes · sin `|` literales dentro de fórmulas");
}
