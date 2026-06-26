from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QInputDialog,
)

from controllers.prompt_controller import PromptController


class PromptPage(QWidget):

    def __init__(self):

        super().__init__()

        self.controller = PromptController()

        layout = QVBoxLayout(self)

        self.table = QTableWidget()

        self.table.setColumnCount(2)

        self.table.setHorizontalHeaderLabels([
            "Title",
            "Category"
        ])

        layout.addWidget(self.table)

        self.addButton = QPushButton("➕ Add Prompt")

        layout.addWidget(self.addButton)

        self.addButton.clicked.connect(self.add_prompt)

        self.refresh()

    def refresh(self):

        rows = self.controller.get_all()

        self.table.setRowCount(len(rows))

        for r,row in enumerate(rows):

            self.table.setItem(
                r,0,QTableWidgetItem(row[0])
            )

            self.table.setItem(
                r,1,QTableWidgetItem(row[1])
            )

    def add_prompt(self):

        title,ok = QInputDialog.getText(
            self,
            "Title",
            "Prompt Title"
        )

        if not ok:

            return

        category,ok = QInputDialog.getText(
            self,
            "Category",
            "Category"
        )

        if not ok:

            return

        prompt,ok = QInputDialog.getMultiLineText(
            self,
            "Prompt",
            "Prompt"
        )

        if not ok:

            return

        self.controller.add(
            title,
            category,
            prompt
        )

        self.refresh()