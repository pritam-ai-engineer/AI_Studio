import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QListWidget,
    QMainWindow,
    QStackedWidget,
    QWidget,
)

# Pages
from gui.pages.dashboard_page import DashboardPage
from gui.pages.character_page import CharacterPage
from gui.pages.episode_page import EpisodePage
from gui.pages.prompt_page import PromptPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Studio Pro v3.3")

        self.resize(1500, 900)

        # -----------------------------
        # Central Widget
        # -----------------------------

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout()
        central.setLayout(layout)

        # -----------------------------
        # Sidebar
        # -----------------------------

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

        # -----------------------------
        # Stack Widget
        # -----------------------------

        self.stack = QStackedWidget()

        # Dashboard
        self.dashboardPage = DashboardPage()
        self.stack.addWidget(self.dashboardPage)

        # Characters
        self.characterPage = CharacterPage()
        self.stack.addWidget(self.characterPage)

        # Episodes
        self.episodePage = EpisodePage()
        self.stack.addWidget(self.episodePage)

        # Prompts
        self.promptPage = PromptPage()
        self.stack.addWidget(self.promptPage)

        # Assets (Placeholder)
        self.assetsPage = QWidget()
        self.stack.addWidget(self.assetsPage)

        # Analytics (Placeholder)
        self.analyticsPage = QWidget()
        self.stack.addWidget(self.analyticsPage)

        # Settings (Placeholder)
        self.settingsPage = QWidget()
        self.stack.addWidget(self.settingsPage)

        layout.addWidget(self.stack)

        # -----------------------------
        # Events
        # -----------------------------

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