#!/usr/bin/env python3
"""
Quick Progress Checker - Simple script to view learning progress

This is a lightweight script that reads state and shows basic progress.
For detailed analysis, use: /progress in Claude Code
"""

import json
from pathlib import Path
from datetime import datetime, date

def main():
    # Load learning state
    state_file = Path(__file__).parent.parent / "state" / "learning_state.json"

    if not state_file.exists():
        print("❌ No learning state found. Start a session first!")
        return

    with open(state_file, 'r') as f:
        state = json.load(f)

    # Extract key metrics
    metadata = state.get('metadata', {})
    progress = state.get('progress_summary', {})
    velocity = state.get('learning_velocity', {}).get('total', {})

    # Calculate days to exam
    exam_date_str = metadata.get('exam_date', '2025-12-15')
    exam_date = date.fromisoformat(exam_date_str)
    days_remaining = (exam_date - date.today()).days

    # Display
    print("\n" + "="*60)
    print("📊 Quick Progress Check")
    print("="*60)

    print(f"\n📅 Exam: {exam_date_str} ({days_remaining} days remaining)")
    print(f"📈 Overall Progress: {progress.get('overall_percentage', 0):.1f}%")
    print(f"🎯 Concepts Mastered: {progress.get('concepts_mastered', 0)}/87")
    print(f"📝 Problems Solved: {progress.get('problems_solved', 0)}")
    print(f"⏱️  Study Sessions: {velocity.get('sessions', 0)}")
    print(f"📚 Study Hours: {velocity.get('study_hours', 0):.1f}h")

    # Show unit progress
    units = state.get('units', {})
    print(f"\n📚 Units Progress:")
    for unit_id in sorted(units.keys(), key=lambda x: int(x)):
        unit = units[unit_id]
        status = unit.get('status', 'pending')
        progress_pct = unit.get('progress', 0)

        if status == 'completed':
            icon = "✅"
        elif status == 'in_progress':
            icon = "📚"
        else:
            icon = "⏳"

        bar = "━" * int(progress_pct / 10) + "░" * (10 - int(progress_pct / 10))
        print(f"  {icon} Unit {unit_id}: {unit.get('name', 'Unknown')[:30]:<30} {bar} {progress_pct}%")

    print("\n" + "="*60)
    print("💡 For detailed analysis, use: /progress in Claude Code")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
