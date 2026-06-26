from pathlib import Path

def count_directories(path: Path):
    if not path.exists():
        return 0
    return len([p for p in path.iterdir() if p.is_dir()])


def count_files(path: Path):
    if not path.exists():
        return 0
    return len([p for p in path.iterdir() if p.is_file()])
