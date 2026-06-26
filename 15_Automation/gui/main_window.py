import sys

from PySide6.QtWidgets import (
    QApplication,
    QListWidget,
    QHBoxLayout,
    QMainWindow,
    QWidget,
)

from gui.pages.dashboard_page import DashboardPage


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("AI Studio Pro v3.0")

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

        self.dashboard = DashboardPage()

        layout.addWidget(self.dashboard)


app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()