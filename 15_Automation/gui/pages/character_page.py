from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QInputDialog,
    QMessageBox,
)

from controllers.character_controller import CharacterController


class CharacterPage(QWidget):

    def __init__(self):

        super().__init__()

        self.controller = CharacterController()

        layout = QVBoxLayout(self)

        # ------------------------
        # Table
        # ------------------------

        self.table = QTableWidget()

        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderLabels(
            ["Character", "Folder", "Status"]
        )

        layout.addWidget(self.table)

        # ------------------------
        # Buttons
        # ------------------------

        buttons = QHBoxLayout()

        self.addBtn = QPushButton("➕ Add")

        self.deleteBtn = QPushButton("🗑 Delete")

        self.refreshBtn = QPushButton("🔄 Refresh")

        buttons.addWidget(self.addBtn)

        buttons.addWidget(self.deleteBtn)

        buttons.addWidget(self.refreshBtn)

        layout.addLayout(buttons)

        self.addBtn.clicked.connect(self.add_character)

        self.deleteBtn.clicked.connect(self.delete_character)

        self.refreshBtn.clicked.connect(self.refresh)

        self.refresh()

    def refresh(self):

        characters = self.controller.get_all()

        self.table.setRowCount(len(characters))

        for row, item in enumerate(characters):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(item[0])
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem("Ready")
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem("Active")
            )

    def add_character(self):

        name, ok = QInputDialog.getText(
            self,
            "Character",
            "Character Name"
        )

        if ok and name:

            self.controller.add(name)

            self.refresh()

    def delete_character(self):

        row = self.table.currentRow()

        if row < 0:

            QMessageBox.information(
                self,
                "Info",
                "Select a character."
            )

            return

        name = self.table.item(row, 0).text()

        self.controller.delete(name)

        self.refresh()