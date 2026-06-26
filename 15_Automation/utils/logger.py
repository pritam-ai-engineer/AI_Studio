"""
AI Studio Logger
"""

from pathlib import Path
from datetime import datetime

LOG_FILE = Path("D:/AI_Studio/15_Automation/logs/studio.log")


def log(message):

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as file:

        file.write(
            f"{datetime.now():%Y-%m-%d %H:%M:%S} | {message}\n"
        )