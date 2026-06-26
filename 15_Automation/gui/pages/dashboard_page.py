from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)


class StatCard(QFrame):

    def __init__(self, title, value):

        super().__init__()

        self.setFrameShape(QFrame.StyledPanel)

        self.setStyleSheet("""
            QFrame{
                background:#ffffff;
                border:1px solid #dddddd;
                border-radius:10px;
            }
        """)

        layout = QVBoxLayout(self)

        titleLabel = QLabel(title)

        titleLabel.setAlignment(Qt.AlignCenter)

        titleLabel.setStyleSheet("""
            font-size:14px;
            color:gray;
        """)

        valueLabel = QLabel(str(value))

        valueLabel.setAlignment(Qt.AlignCenter)

        valueLabel.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(titleLabel)
        layout.addWidget(valueLabel)


class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()

        main = QVBoxLayout(self)

        title = QLabel("Dashboard")

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            padding:10px;
        """)

        main.addWidget(title)

        cards = QGridLayout()

        cards.addWidget(StatCard("Characters",11),0,0)
        cards.addWidget(StatCard("Episodes",6),0,1)
        cards.addWidget(StatCard("Prompts",12),0,2)
        cards.addWidget(StatCard("Assets",150),0,3)

        main.addLayout(cards)

        recent = QLabel("""

Recent Activity

✓ Episode_007 Created

✓ JungleKing Created

✓ Prompt Saved

✓ AI Studio Started

""")

        recent.setStyleSheet("""
            font-size:16px;
            padding:20px;
        """)

        main.addWidget(recent)

        main.addStretch()