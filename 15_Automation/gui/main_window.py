import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QListWidget,
    QMainWindow,
    QStackedWidget,
    QWidget,
)

from gui.pages.dashboard_page import DashboardPage
from gui.pages.character_page import CharacterPage
from gui.pages.episode_page import EpisodePage


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("AI Studio Pro v3.2")

        self.resize(1500,900)

        central = QWidget()

        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        self.sidebar = QListWidget()

        self.sidebar.setFixedWidth(220)

        self.sidebar.addItems([
            "🏠 Dashboard",
            "🐵 Characters",
            "🎬 Episodes",
            "📝 Prompts",
            "🖼 Assets",
            "📊 Analytics",
            "⚙ Settings"
        ])

        layout.addWidget(self.sidebar)

        self.stack = QStackedWidget()

        self.dashboard = DashboardPage()

        self.characters = CharacterPage()

        self.episodes = EpisodePage()

        self.stack.addWidget(self.dashboard)

        self.stack.addWidget(self.characters)

        self.stack.addWidget(self.episodes)

        # Placeholder pages
        for _ in range(4):

            self.stack.addWidget(QWidget())

        layout.addWidget(self.stack)

        self.sidebar.currentRowChanged.connect(
            self.stack.setCurrentIndex
        )

        self.sidebar.setCurrentRow(0)


def main():

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":

    main()