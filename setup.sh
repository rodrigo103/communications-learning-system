#!/bin/bash
# Setup Script para Communications Learning System
# Usage: bash setup.sh

set -e  # Exit on error

echo "🚀 Setting up Communications Learning System..."
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if we're in the right directory
if [ ! -f "QUICK_START.md" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    echo "   (where QUICK_START.md is located)"
    exit 1
fi

echo -e "${BLUE}Step 1: Creating directory structure...${NC}"
mkdir -p agents
mkdir -p state
mkdir -p progress/{units,concepts,problems/{solved,pending}}
mkdir -p knowledge/{formulas,derivations}
mkdir -p outputs/{anki,derivations,solutions,simulations,reports}
mkdir -p sessions
mkdir -p docs
mkdir -p config
mkdir -p tests
mkdir -p scripts
echo -e "${GREEN}✓ Directories created${NC}"
echo ""

echo -e "${BLUE}Step 2: Copying files to correct locations...${NC}"

# Move files from /tmp/ to correct locations
if [ -f "/tmp/SYSTEM_ARCHITECTURE.md" ]; then
    cp /tmp/SYSTEM_ARCHITECTURE.md docs/
    echo "✓ SYSTEM_ARCHITECTURE.md → docs/"
fi

if [ -f "/tmp/README.md" ]; then
    cp /tmp/README.md .
    echo "✓ README.md → root"
fi

if [ -f "/tmp/main.py" ]; then
    cp /tmp/main.py .
    chmod +x main.py
    echo "✓ main.py → root (executable)"
fi

if [ -f "/tmp/coordinator.py" ]; then
    cp /tmp/coordinator.py agents/
    echo "✓ coordinator.py → agents/"
fi

if [ -f "/tmp/learning_state_schema.json" ]; then
    cp /tmp/learning_state_schema.json state/learning_state.json
    echo "✓ learning_state.json → state/"
fi

if [ -f "/tmp/.gitignore" ]; then
    cp /tmp/.gitignore .
    echo "✓ .gitignore → root"
fi

if [ -f "/tmp/QUICK_START.md" ]; then
    cp /tmp/QUICK_START.md docs/
    echo "✓ QUICK_START.md → docs/"
fi

echo -e "${GREEN}✓ Files copied${NC}"
echo ""

echo -e "${BLUE}Step 3: Copying course materials...${NC}"
if [ -f "/mnt/project/Programa_de_la_materia" ]; then
    cp "/mnt/project/Programa_de_la_materia" docs/programa_materia.md
    echo "✓ Programa de la materia → docs/"
fi

if [ -f "/mnt/project/Examen_final__24_04_2025___Ejercicio_3. Ruido [2,5 puntos]" ]; then
    cp "/mnt/project/Examen_final__24_04_2025___Ejercicio_3. Ruido [2,5 puntos]" docs/ejercicio_ruido.txt
    echo "✓ Ejercicio de ruido → docs/"
fi
echo -e "${GREEN}✓ Course materials copied${NC}"
echo ""

echo -e "${BLUE}Step 4: Creating requirements.txt...${NC}"
cat > requirements.txt << 'EOF'
# Core
numpy>=1.24.0
scipy>=1.10.0
sympy>=1.12

# CLI
click>=8.1.0
rich>=13.0.0

# Visualización
matplotlib>=3.7.0
seaborn>=0.12.0

# Anki
genanki>=0.13.0
requests>=2.31.0

# Concept mapping
graphviz>=0.20.0
networkx>=3.1

# Utilidades
pyyaml>=6.0
python-dateutil>=2.8.0

# PDF generation
reportlab>=4.0.0

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0
EOF
echo -e "${GREEN}✓ requirements.txt created${NC}"
echo ""

echo -e "${BLUE}Step 5: Creating Python virtual environment...${NC}"
if command -v python3 &> /dev/null; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
    echo ""
    
    echo -e "${BLUE}Step 6: Installing dependencies...${NC}"
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    echo -e "${GREEN}✓ Dependencies installed${NC}"
else
    echo -e "${YELLOW}⚠ Python3 not found. Please install dependencies manually:${NC}"
    echo "  python -m venv venv"
    echo "  source venv/bin/activate"
    echo "  pip install -r requirements.txt"
fi
echo ""

echo -e "${BLUE}Step 7: Creating __init__.py files...${NC}"
touch agents/__init__.py
touch tests/__init__.py
echo -e "${GREEN}✓ __init__.py files created${NC}"
echo ""

echo -e "${BLUE}Step 8: Initializing Git repository...${NC}"
if [ ! -d ".git" ]; then
    git init
    git add .
    git commit -m "Initial commit: System architecture and foundation"
    echo -e "${GREEN}✓ Git repository initialized${NC}"
else
    echo -e "${YELLOW}⚠ Git repository already exists${NC}"
fi
echo ""

echo "═══════════════════════════════════════════════════════"
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "📁 Project structure created"
echo "📦 Dependencies installed"
echo "📝 Documentation ready"
echo "🎯 Git repository initialized"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo ""
echo "1. Activate virtual environment:"
echo -e "   ${YELLOW}source venv/bin/activate${NC}"
echo ""
echo "2. Test the CLI:"
echo -e "   ${YELLOW}python main.py --help${NC}"
echo ""
echo "3. Start your first session:"
echo -e "   ${YELLOW}python main.py start-session --user rodrigo${NC}"
echo ""
echo "4. Open in Claude Code:"
echo -e "   ${YELLOW}claude-code${NC}"
echo ""
echo "5. Give Claude Code this prompt:"
echo -e "${YELLOW}"
cat << 'PROMPT'
Hi! I need you to implement Phase 1 of the communications learning system.

Please:
1. Read /docs/SYSTEM_ARCHITECTURE.md (complete architecture)
2. Read /docs/programa_materia.md (course curriculum)  
3. Complete the implementation of agents/coordinator.py
4. Make the CLI in main.py fully functional
5. Create tests in tests/test_coordinator.py

The goal is to have working session management. Let's start!
PROMPT
echo -e "${NC}"
echo ""
echo "📖 Full documentation: docs/SYSTEM_ARCHITECTURE.md"
echo "🚀 Quick start guide: docs/QUICK_START.md"
echo ""
echo "Good luck with your studies! 🎓✨"
