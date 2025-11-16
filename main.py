#!/usr/bin/env python3
"""
Sistema de Aprendizaje para Sistemas de Comunicaciones
Simplified CLI for Session Management

This CLI handles ONLY session and state management.
All AI work (derivations, problem solving, progress analysis) is done by Claude Code subagents.

Usage:
    # Session management
    python main.py start-session --user <nombre>
    python main.py end-session
    python main.py progress

    # For actual learning work, use Claude Code with subagents:
    In Claude Code:
        - Derive formulas: Just ask "Can you derive [formula]?"
        - Solve problems: Just ask "Can you solve this problem?"
        - Check progress: Use the /progress command
        - Start/end sessions: Use /start-session and /end-session commands

Note: The subagent system is more powerful and flexible than this CLI.
      We recommend using Claude Code directly for most tasks.
"""

import click
from pathlib import Path
import sys

# Add agents directory to path
sys.path.insert(0, str(Path(__file__).parent))

from agents.coordinator import SessionCoordinator


@click.group()
@click.version_option(version='2.0.0')
def cli():
    """
    Sistema de Aprendizaje para Sistemas de Comunicaciones (UTN)

    SIMPLIFIED: This CLI now handles only session management.
    All AI work is done by Claude Code subagents:
      - formula-deriver: For derivations
      - exercise-solver: For problem solving
      - progress-analyzer: For progress analysis
      - study-session-manager: For session orchestration

    Use Claude Code commands for actual learning:
      /derive [formula] - Derive formulas
      /solve [file] - Solve problems
      /progress - Check learning progress
    """
    pass


# ============================================================================
# SESSION MANAGEMENT
# ============================================================================

@cli.command()
@click.option('--user', '-u', required=True, help='Username for this session')
def start_session(user: str):
    """Iniciar una nueva sesión de estudio"""
    click.echo(f"\n🎯 Starting session for {user}...")

    coordinator = SessionCoordinator()

    try:
        session_context = coordinator.start_session(user)

        click.echo("\n" + "="*60)
        click.echo("SESSION STARTED")
        click.echo("="*60)

        # Display session context
        click.echo(f"\n📊 Current Status:")
        click.echo(f"  - Overall progress: {session_context['progress']}%")
        click.echo(f"  - Active unit: Unit {session_context['active_unit']}")
        click.echo(f"  - Last studied: {session_context['last_topic']}")

        click.echo(f"\n💡 Recommendations:")
        for i, rec in enumerate(session_context['recommendations'], 1):
            click.echo(f"  {i}. {rec}")

        click.echo("\n✨ Ready to learn! In Claude Code, use:")
        click.echo("   - Ask to derive formulas")
        click.echo("   - Ask to solve problems")
        click.echo("   - Use /progress command")
        click.echo("\n   Or use the CLI slash commands:")
        click.echo("   /derive [formula]")
        click.echo("   /solve [file]")
        click.echo("   /progress")

    except Exception as e:
        click.echo(f"\n❌ Error starting session: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--summary', '-s', help='Brief summary of session work')
def end_session(summary: str = None):
    """Finalizar sesión actual y guardar estado"""
    click.echo("\n📊 Finalizing session...")

    coordinator = SessionCoordinator()

    try:
        report = coordinator.end_session(summary)

        click.echo("\n" + "="*60)
        click.echo("SESSION SUMMARY")
        click.echo("="*60)

        click.echo(f"\n⏱️  Duration: {report['duration']}")
        click.echo(f"\n✅ Completed:")
        for item in report['completed']:
            click.echo(f"   - {item}")

        click.echo(f"\n📈 Progress updates:")
        for update in report['updates']:
            click.echo(f"   - {update}")

        click.echo(f"\n💡 Next recommended focus:")
        click.echo(f"   {report['next_focus']}")

        click.echo(f"\n📁 Session log: {report['log_path']}")

        click.echo("\n✨ Don't forget to commit your work:")
        click.echo("   git add .")
        click.echo("   git commit -m 'Session: [description]'")
        click.echo("   git push origin main")

    except Exception as e:
        click.echo(f"\n❌ Error ending session: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--detailed', '-d', is_flag=True, help='Show detailed progress')
@click.option('--unit', '-u', type=int, help='Show progress for specific unit')
def progress(detailed: bool, unit: int):
    """Ver progreso actual del aprendizaje"""
    coordinator = SessionCoordinator()

    try:
        progress_data = coordinator.get_progress(detailed=detailed, unit=unit)

        click.echo("\n📊 Learning Progress")
        click.echo("="*60)

        click.echo(f"\nOverall: {progress_data['overall']}%")
        click.echo(f"Concepts mastered: {progress_data['concepts_mastered']}/{progress_data['total_concepts']}")
        click.echo(f"Problems solved: {progress_data['problems_solved']}")
        click.echo(f"Study time (7 days): {progress_data['study_hours']}h")

        click.echo("\n📚 Units:")
        for unit_data in progress_data['units']:
            status = "✅" if unit_data['complete'] else "📚" if unit_data['in_progress'] else "⏳"
            click.echo(f"  {status} Unit {unit_data['number']}: {unit_data['name']} ({unit_data['progress']}%)")

    except Exception as e:
        click.echo(f"\n❌ Error getting progress: {e}", err=True)
        sys.exit(1)


@cli.command()
def info():
    """Show system architecture information"""
    click.echo("\n" + "="*60)
    click.echo("SYSTEM ARCHITECTURE")
    click.echo("="*60)
    click.echo("\nThis system uses a SUBAGENT-FIRST architecture:")
    click.echo("\n📂 Python CLI (this file):")
    click.echo("   - Session management (start/end sessions)")
    click.echo("   - State persistence (learning_state.json)")
    click.echo("   - Progress tracking")
    click.echo("\n🤖 Claude Code Subagents (.claude/agents/):")
    click.echo("   - formula-deriver: Mathematical derivations")
    click.echo("   - comms-formula-deriver: Advanced comm systems")
    click.echo("   - exercise-solver: Problem solving")
    click.echo("   - progress-analyzer: Progress analysis")
    click.echo("   - study-session-manager: Session orchestration")
    click.echo("\n💡 Recommended workflow:")
    click.echo("   1. Start session: python main.py start-session --user <name>")
    click.echo("   2. Work in Claude Code (ask for derivations, problem solving)")
    click.echo("   3. Check progress: python main.py progress")
    click.echo("   4. End session: python main.py end-session")
    click.echo("\n📚 Documentation:")
    click.echo("   - README.md - System overview")
    click.echo("   - SYSTEM_ARCHITECTURE.md - Detailed architecture")
    click.echo("   - .claude/agents/ - Subagent definitions")
    click.echo("=" * 60)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    cli()
