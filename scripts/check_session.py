#!/usr/bin/env python3
"""
Check if there's an active study session

Simple utility to see if a session is currently active.
"""

import json
from pathlib import Path
from datetime import datetime

def main():
    session_file = Path(__file__).parent.parent / "state" / "current_session.json"

    if not session_file.exists():
        print("\n❌ No active session")
        print("💡 Start one with: /start-session in Claude Code\n")
        return

    with open(session_file, 'r') as f:
        session = json.load(f)

    user = session.get('user', 'Unknown')
    start_time_str = session.get('start_time', '')

    try:
        start_time = datetime.fromisoformat(start_time_str)
        duration = datetime.now() - start_time
        hours = int(duration.total_seconds() // 3600)
        minutes = int((duration.total_seconds() % 3600) // 60)
    except:
        hours, minutes = 0, 0

    activities = session.get('activities', [])

    print("\n" + "="*60)
    print("✅ Active Session")
    print("="*60)
    print(f"\n👤 User: {user}")
    print(f"⏰ Started: {start_time_str}")
    print(f"⏱️  Duration: {hours}h {minutes}m")
    print(f"📊 Activities: {len(activities)}")

    if activities:
        print("\n📝 Work done this session:")
        for activity in activities[-5:]:  # Last 5 activities
            print(f"  • {activity.get('type', 'unknown')}: {activity.get('description', '')}")

    print("\n💡 Continue with: /derive [formula] or /solve [file]")
    print("💡 Finish with: /end-session\n")

if __name__ == "__main__":
    main()
