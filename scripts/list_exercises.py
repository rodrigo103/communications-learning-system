#!/usr/bin/env python3
"""
List available exercises to solve

Shows all exercise files in the docs/ directory
"""

from pathlib import Path

def main():
    exercises_dir = Path(__file__).parent.parent / "exercises"

    # Find all .txt files that look like exercises
    exercises = []
    if exercises_dir.exists():
        for file in exercises_dir.glob("**/*.txt"):
            # Skip non-exercise files
            if 'ejercicio' in file.name.lower() or 'exercise' in file.name.lower():
                exercises.append(file)

    if not exercises:
        print("\n❌ No exercises found in exercises/")
        print("💡 Create exercise files with problems to solve\n")
        return

    print("\n" + "="*60)
    print("📝 Available Exercises")
    print("="*60 + "\n")

    for i, ex_file in enumerate(sorted(exercises), 1):
        rel_path = ex_file.relative_to(Path(__file__).parent.parent)

        # Try to read first line for title
        try:
            with open(ex_file, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
        except:
            first_line = "Unknown"

        print(f"{i}. {rel_path}")
        print(f"   {first_line[:70]}")
        print()

    print("="*60)
    print("💡 To solve an exercise:")
    print("   /solve [filename]")
    print("\n   Example: /solve exercises/ejercicio_ruido.txt")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
