from pathlib import Path

def list_characters(base_path):

    print("\n===== CHARACTER LIST =====")

    characters = sorted([p for p in base_path.iterdir() if p.is_dir()])

    if not characters:
        print("No characters found.")
        return

    for i, character in enumerate(characters, start=1):
        print(f"{i}. {character.name}")

    print("==========================")
