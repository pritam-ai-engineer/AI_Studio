from pathlib import Path

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QGridLayout,
    QVBoxLayout,
    QFrame,
)

from services.database_service import DatabaseService


EPISODES = Path(
    "20_Projects/Chimpanzee_Crazy/Episodes"
)


class Card(QFrame):

    def __init__(self, title, value):

        super().__init__()

        self.setFrameShape(QFrame.StyledPanel)

        layout = QVBoxLayout(self)

        label = QLabel(title)

        label.setAlignment(Qt.AlignCenter)

        valueLabel = QLabel(str(value))

        valueLabel.setAlignment(Qt.AlignCenter)

        valueLabel.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
        """)

        layout.addWidget(label)

        layout.addWidget(valueLabel)


class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()

        db = DatabaseService()

        characters = db.count_characters()

        prompts = db.count_prompts()

        episodes = len(
            list(
                EPISODES.glob("Episode_*")
            )
        )

        db.close()

        layout = QVBoxLayout(self)

        title = QLabel("Dashboard")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        cards = QGridLayout()

        cards.addWidget(
            Card("Characters", characters),
            0,
            0,
        )

        cards.addWidget(
            Card("Episodes", episodes),
            0,
            1,
        )

        cards.addWidget(
            Card("Prompts", prompts),
            0,
            2,
        )

        cards.addWidget(
            Card("Assets", 0),
            0,
            3,
        )

        layout.addLayout(cards)

        recent = QLabel("""

Recent Activity

✓ AI Studio Started

✓ Dashboard Loaded

""")

        recent.setStyleSheet("""
            font-size:16px;
            padding:20px;
        """)

        layout.addWidget(recent)

        layout.addStretch()