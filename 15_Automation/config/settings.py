from pathlib import Path

PROJECT_NAME = "Chimpanzee_Crazy"

ROOT = Path(__file__).resolve().parent.parent

DATABASE = ROOT / "database" / "studio.db"

EPISODES = ROOT / "20_Projects" / PROJECT_NAME / "Episodes"

CHARACTERS = ROOT / "02_Characters"

ASSETS = ROOT / "21_Assets"