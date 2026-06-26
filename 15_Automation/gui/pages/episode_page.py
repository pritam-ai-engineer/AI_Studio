from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QListWidget,
    QMessageBox,
)

BASE = Path(
    "20_Projects/Chimpanzee_Crazy/Episodes"
)

FILES = [
    "Script.md",
    "Scenes.md",
    "Prompt.md",
    "Thumbnail.md",
    "Metadata.md",
]


class EpisodePage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        self.list = QListWidget()

        layout.addWidget(self.list)

        self.newButton = QPushButton(
            "➕ Create Episode"
        )

        layout.addWidget(self.newButton)

        self.newButton.clicked.connect(
            self.create_episode
        )

        BASE.mkdir(
            parents=True,
            exist_ok=True
        )

        self.refresh()

    def refresh(self):

        self.list.clear()

        for folder in sorted(BASE.glob("Episode_*")):

            self.list.addItem(folder.name)

    def create_episode(self):

        count = len(
            list(BASE.glob("Episode_*"))
        ) + 1

        episode = BASE / f"Episode_{count:03d}"

        episode.mkdir()

        for file in FILES:

            (episode / file).touch()

        QMessageBox.information(
            self,
            "Success",
            f"{episode.name} created."
        )

        self.refresh()