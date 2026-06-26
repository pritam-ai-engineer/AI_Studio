from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

import sys


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("AI Studio Pro v2.0")

        self.resize(1200, 700)

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout()

        central.setLayout(layout)

        title = QLabel("🚀 AI Studio Pro")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            padding:20px;
        """)

        layout.addWidget(title)

        layout.addWidget(
            QLabel("Welcome to AI Studio Pro Desktop")
        )


app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()