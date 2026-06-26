from pathlib import Path

FOLDERS = [
    "images",
    "videos",
    "voice",
    "poses",
    "expressions",
    "prompts",
]


def create_character(base_path, character_name):

    character = base_path / character_name

    character.mkdir(parents=True, exist_ok=True)

    for folder in FOLDERS:
        (character / folder).mkdir(exist_ok=True)

    (character / "character.md").touch(exist_ok=True)

    print(f"✅ Character '{character_name}' created successfully!")