---
name: wiki
description: "Manage the LLM Wiki for Communications Learning System — ingest, search, lint, status. Wiki lives at .opencode/wiki/ with knowledge about modulations, noise, information theory, and problem-solving patterns."
license: MIT
compatibility: opencode
metadata:
  workflow: knowledge-management
---

# Wiki Skill

Manage the **LLM Wiki** at `.opencode/wiki/` — a persistent, interlinked markdown knowledge base for the Communications Systems course.

## How the wiki works

The wiki is a **growing knowledge base compiled from study sessions**. It covers:
- Mathematical derivations (AM, FM, QAM, Parseval, Shannon-Hartley, Friis)
- Concept explanations (Anki flashcards organized by transversal themes)
- Mind maps and course overviews
- Problem solutions and exercise patterns
- Progress tracking and study planning

Three core operations:
- **Ingest** — Process new sources, compile/update wiki pages
- **Query** — Search wiki, synthesize answer with claim type annotations
- **Lint** — Check for contradictions, orphans, stale info

---

## Commands

### `/wiki ingest [topic]`

Processes new content into the wiki.

**What it does:**
1. If raw files exist in `.opencode/wiki/raw/`, processes them first: reads each, extracts key info, creates/updates wiki pages, **deletes** the processed raw files
2. If a topic is specified (`/wiki ingest modulacion`), searches relevant source files and compiles into wiki pages
3. Updates `.opencode/wiki/index.md` (table of contents) and `.opencode/wiki/log.md` (changelog)

**When to use:** After study sessions, after resolving non-trivial problems, after dropping files into `raw/`.

### `/wiki search <query>`

Searches all wiki pages and synthesizes an answer.

**What it does:**
1. Greps across all `.md` files in `.opencode/wiki/`
2. Reads matching pages
3. Synthesizes a concise answer with claim type annotations

### `/wiki lint`

Health-check the wiki for consistency.

**What it checks:**
- **Broken links** — `[[path]]` references to non-existent pages
- **Orphan pages** — Pages not linked from any other page
- **Empty stubs** — Pages with minimal/no content
- **Stale pages** — Pages with `Last verified:` older than 30 days
- **Unverified claims** — Pages with many `[unverified]` tags
- **Missing source files** — `source_file:` frontmatter pointing to deleted originals

**When to use:** Periodically (e.g., weekly) or before exams.

### `/wiki status`

Show wiki statistics.

**Output:**
- Page count per category
- Last 5 changelog entries
- Number of `[unverified]` and `[gap]` claims
- Stale pages
- Pending items in `raw/`

---

## Page format rules

Every wiki page follows this structure:

```markdown
---
tags:
  - wiki/categoria
source_file: path/to/original.md
curso: Sistemas de Comunicaciones
unidad: [1, 3]
---

# Page Title

> **Last verified:** YYYY-MM-DD | **Verified by:** [source|analysis|gap]

Content here...
```

### Claim types

Every factual statement should be tagged:

| Tag | Meaning |
|---|---|
| `[source]` | Verified from textbook or course program |
| `[analysis]` | Derived from evidence or pedagogical reasoning |
| `[unverified]` | Assumed, not yet checked against source |
| `[gap]` | Known unknown — topic to investigate |

### Cross-links

Use `[[relative/path/without-extension]]` to link between wiki pages. Example: `[[modulacion-analogica/am-vs-dsb-sc]]`.

### Math notation

Use `$$...$$` for display math and `$...$` for inline math. Box key formulas with `\boxed{...}`.

---

## Allowed tools

- Read, Write, Edit, Glob, Grep, Bash, Agent
