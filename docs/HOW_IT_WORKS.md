# 🔧 How main.py Works - Technical Explanation

## ❌ What It's NOT

**It does NOT call Claude or any AI API**

This is a **pure Python CLI application** with hardcoded logic. The term "agents" is metaphorical - they're just Python classes, not AI agents.

---

## ✅ What It Actually Is

### Architecture

```
User Types Command
        ↓
    main.py (CLI using Click framework)
        ↓
    Python Class Methods
        ↓
    Hardcoded Logic + Data Structures
        ↓
    File I/O (JSON, PDF, .apkg)
```

---

## 📂 File Structure

```python
main.py                  # CLI interface (Click framework)
    ├── imports agents.coordinator.SessionCoordinator
    ├── imports agents.derivation_engine.DerivationEngine
    └── imports agents.problem_solver.ProblemSolver

agents/
    ├── coordinator.py         # Session management
    ├── derivation_engine.py   # Formula derivations (hardcoded)
    └── problem_solver.py      # Problem solving (regex + math)
```

---

## 🔍 Example: How `python main.py derive AM` Works

### Step 1: CLI Parsing (main.py)

```python
# main.py lines 191-277
@cli.command()
@click.argument('formula')
@click.option('--level', default='complete')
@click.option('--pdf', is_flag=True)
@click.option('--anki', is_flag=True)
def derive(formula: str, level: str, pdf: bool, anki: bool):
    """Derivar una fórmula desde primeros principios"""

    # 1. Create DerivationEngine instance
    engine = DerivationEngine()

    # 2. Call derive_formula method
    derivation = engine.derive_formula(formula, level=level)

    # 3. Display in terminal
    click.echo(derivation['title'])
    # ... format and display ...

    # 4. Generate PDF if --pdf flag
    if pdf:
        pdf_path = engine.generate_pdf(derivation)

    # 5. Generate Anki if --anki flag
    if anki:
        anki_path = engine.export_to_anki_deck(derivation)
```

### Step 2: DerivationEngine Class (agents/derivation_engine.py)

```python
class DerivationEngine:
    def __init__(self):
        # Knowledge base is HARDCODED in Python
        self.knowledge_base = {
            "AM": {
                "name": "Amplitude Modulation",
                "description": "...",
                # ... more metadata ...
            },
            "FM": {...},
            "Shannon-Hartley": {...},
            # etc.
        }

    def derive_formula(self, topic: str, level: str) -> Dict:
        """Route to specific derivation method"""
        if topic == "AM":
            return self._derive_am(level)
        elif topic == "FM":
            return self._derive_fm(level)
        # ... etc ...

    def _derive_am(self, level: str) -> Dict:
        """HARDCODED AM derivation - no AI here!"""
        steps = []

        # Step 1 - MANUALLY WRITTEN
        steps.append({
            "number": 1,
            "title": "Definition of Amplitude Modulation",
            "equation": r"s_{AM}(t) = A_c [1 + m(t)] \cos(2\pi f_c t)",
            "explanation": "Where A_c is carrier amplitude..."
        })

        # Step 2 - MANUALLY WRITTEN
        steps.append({
            "number": 2,
            "title": "Expand the AM Signal",
            "equation": r"s_{AM}(t) = A_c \cos(2\pi f_c t) + ...",
            "explanation": "This separates carrier from modulation..."
        })

        # ... more steps ...

        return {
            "topic": "AM",
            "title": "Amplitude Modulation (AM) Derivation",
            "steps": steps,
            "final_formula": "s_{AM}(t) = A_c [1 + m(t)] cos(2πf_c t)",
            "key_results": [
                "Bandwidth: BW = 2*f_m",
                "Power efficiency: η ≤ 33.3%",
                # ... etc ...
            ]
        }
```

### Step 3: Output Generation

```python
def generate_pdf(self, derivation: Dict) -> Path:
    """Generate PDF using ReportLab library"""
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate

    # Create PDF document
    pdf_file = self.outputs_dir / f"{derivation['topic']}_{timestamp}.pdf"
    doc = SimpleDocTemplate(str(pdf_file), pagesize=letter)

    # Add content (using derivation dict)
    story = []
    story.append(Paragraph(derivation['title'], title_style))
    for step in derivation['steps']:
        story.append(Paragraph(step['equation'], equation_style))
        story.append(Paragraph(step['explanation'], text_style))

    # Build PDF
    doc.build(story)
    return pdf_file
```

---

## 🧮 How Problem Solving Works

### Example: `python main.py solve ejercicio_ruido.txt`

```python
# main.py calls:
solver = ProblemSolver()
solution = solver.solve_problem(Path("ejercicio_ruido.txt"))

# ProblemSolver does:
class ProblemSolver:
    def solve_problem(self, file_path: Path) -> Dict:
        # 1. READ THE FILE
        with open(file_path, 'r') as f:
            text = f.read()

        # 2. PARSE WITH REGEX (no AI!)
        problem = self.parse_problem(file_path)
        # Extracts variables using regex like:
        # r"(\w+)\s*=\s*([\d.×eE+-]+)\s*([a-zA-Zμ]+)"

        # 3. IDENTIFY PROBLEM TYPE (keyword matching)
        if 'ruido' in text or 'noise' in text:
            problem_type = 'noise'

        # 4. SOLVE USING HARDCODED FORMULAS
        if problem_type == 'noise':
            solution = self._solve_noise_problem(problem)

        return solution

    def _solve_noise_problem(self, problem: Dict) -> Dict:
        """Hardcoded noise problem solver"""
        G_linear = 10 ** (G_dB / 10)  # Convert dB to linear
        F = P_n_out / (G_linear * P_n_in)  # Noise figure formula
        T_e = T_0 * (F - 1)  # Temperature formula
        # ... etc ...

        # Return step-by-step solution
        return {
            "steps": [
                {"number": 1, "formula": "G = 10^(G_dB/10)", ...},
                {"number": 2, "formula": "F = P_n_out / (G * P_n_in)", ...},
                # ...
            ],
            "answer": f"F = {F:.2f} ({F_dB:.2f} dB)"
        }
```

---

## 📊 Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│  USER TYPES: python main.py derive AM                       │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│  main.py (Click CLI framework)                              │
│  - Parses command: derive                                   │
│  - Extracts argument: "AM"                                  │
│  - Extracts flags: --pdf, --anki                           │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│  DerivationEngine() instance created                        │
│  - Loads hardcoded knowledge_base from __init__           │
│  - knowledge_base["AM"] contains all AM info               │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│  engine.derive_formula("AM", level="complete")             │
│  - Routes to: _derive_am(level)                            │
│  - Calls method with hardcoded AM derivation               │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│  _derive_am() returns Dict:                                │
│  {                                                          │
│    "topic": "AM",                                           │
│    "steps": [                                               │
│      {"number": 1, "equation": "...", "explanation": "..."}, │
│      {"number": 2, "equation": "...", "explanation": "..."}, │
│      ...                                                    │
│    ],                                                       │
│    "final_formula": "...",                                  │
│    "key_results": [...]                                     │
│  }                                                          │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│  main.py displays dict contents using click.echo()         │
│  - Formats and prints to terminal                          │
│  - Uses Unicode box-drawing characters                     │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│  IF --pdf flag: engine.generate_pdf(derivation)            │
│  - Uses ReportLab library                                  │
│  - Creates PDF from dict data                              │
│  - Saves to: outputs/derivations/AM_timestamp.pdf          │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│  IF --anki flag: engine.export_to_anki_deck(derivation)    │
│  - Uses genanki library                                    │
│  - Creates .apkg file from dict data                       │
│  - Saves to: outputs/anki/AM_timestamp.apkg                │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│  DONE - User sees output in terminal                       │
│  Files saved to disk                                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔑 Key Technologies Used

### 1. **Click** (CLI Framework)
```python
import click

@click.command()
@click.argument('formula')
def derive(formula: str):
    # Click handles argument parsing
    pass
```

### 2. **ReportLab** (PDF Generation)
```python
from reportlab.platypus import SimpleDocTemplate, Paragraph

doc = SimpleDocTemplate("output.pdf")
doc.build([Paragraph("Hello World")])
```

### 3. **genanki** (Anki Deck Creation)
```python
import genanki

deck = genanki.Deck(deck_id=123, name="My Deck")
note = genanki.Note(
    model=model,
    fields=["Front text", "Back text"]
)
deck.add_note(note)
genanki.Package(deck).write_to_file("deck.apkg")
```

### 4. **Regular Expressions** (Problem Parsing)
```python
import re

# Extract variables like "G = 50 dB"
pattern = r"(\w+)\s*=\s*([\d.×eE+-]+)\s*([a-zA-Zμ]+)"
matches = re.findall(pattern, text)
# Result: [('G', '50', 'dB'), ...]
```

### 5. **JSON** (State Management)
```python
import json

# Save state
with open('learning_state.json', 'w') as f:
    json.dump(state_dict, f, indent=2)

# Load state
with open('learning_state.json', 'r') as f:
    state = json.load(f)
```

---

## 🧠 Why Call Them "Agents"?

The term "agent" is used **metaphorically** to represent specialized components:

- **Coordinator** = Session manager
- **DerivationEngine** = Formula derivation generator
- **ProblemSolver** = Exercise solver

They're NOT:
- ❌ AI models
- ❌ LLM API calls
- ❌ Claude instances
- ❌ Autonomous agents

They ARE:
- ✅ Python classes
- ✅ Methods with hardcoded logic
- ✅ Data structures and algorithms
- ✅ File I/O operations

---

## 🎯 Where's the Intelligence?

### The "intelligence" comes from:

1. **Hardcoded Knowledge Base**
   - All derivations are manually written in Python
   - All formulas are predefined
   - All solution steps are scripted

2. **Pattern Matching**
   - Regex to parse problem statements
   - Keyword matching to identify problem types
   - Unit conversion dictionaries

3. **Algorithmic Logic**
   - Mathematical calculations (numpy)
   - Formula evaluation
   - Step-by-step generation following templates

### What Claude Code (me) did:

I **wrote the Python code** that contains all this hardcoded logic. The system runs independently without any AI calls.

---

## 📝 Example: Complete Flow

**Command:**
```bash
python main.py derive AM --pdf
```

**What happens:**

1. **Python interpreter** starts
2. **Click** parses command line: `derive`, `"AM"`, `--pdf=True`
3. **main.py** calls: `DerivationEngine().derive_formula("AM")`
4. **DerivationEngine.__init__()** loads hardcoded `knowledge_base`
5. **derive_formula()** routes to `_derive_am()`
6. **_derive_am()** returns a **Python dict** with steps (hardcoded)
7. **main.py** prints dict contents with `click.echo()`
8. **generate_pdf()** uses **ReportLab** to create PDF
9. **File saved** to `outputs/derivations/AM_timestamp.pdf`
10. **Terminal displays** file path and success message

**No AI calls. No API requests. Pure Python.**

---

## 🤔 So Who Created the Derivations?

**I did (Claude Code)** - by writing Python code with hardcoded strings.

For example, the AM derivation at `agents/derivation_engine.py:120-180` was written by me during our conversation. It's now **static code** that runs the same way every time.

Think of it like a textbook: the author (me) wrote the content once, and now anyone can read it (run the code) without the author being present.

---

## 🔮 Future Enhancement Ideas

To make it use AI (if desired):

```python
# Instead of this (current):
def _derive_am(self, level: str) -> Dict:
    steps = [
        {"equation": "s_AM(t) = ...", ...},  # Hardcoded
        {"equation": "...", ...},             # Hardcoded
    ]
    return {"steps": steps}

# Could do this (AI-powered):
def _derive_am(self, level: str) -> Dict:
    import anthropic

    client = anthropic.Client(api_key="...")
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        messages=[{
            "role": "user",
            "content": f"Derive AM formula with {level} detail"
        }]
    )

    # Parse response into steps
    return parse_ai_response(response.content)
```

But that's **not implemented**. Current version is pure Python with hardcoded logic.

---

## ✅ Summary

| Component | What It Is | What It's NOT |
|-----------|------------|---------------|
| `main.py` | Click CLI framework | AI orchestrator |
| "Agents" | Python classes | AI models |
| Derivations | Hardcoded text in Python | Generated by AI at runtime |
| Problem solving | Regex + math algorithms | NLP or ML |
| Knowledge base | Python dict with strings | Vector database |
| Intelligence | Predefined rules and data | Machine learning |

**Bottom line:** It's a well-structured Python CLI app with hardcoded educational content, wrapped in a clean interface. No AI calls during execution.
