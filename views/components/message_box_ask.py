from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox, QVBoxLayout, QLabel, QPushButton, QDialog
from styles.button_style import ButtonStyle


class MessageBoxAsk(QDialog):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Thông báo")
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.label = QLabel(title, self)
        self.layout.addWidget(self.label)

        self.ok_button = QPushButton("Ok", self)
        self.ok_button.setStyleSheet(ButtonStyle.BUTTON_SEARCH + ButtonStyle.HOVER_EFFECT_BUTTON)
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.setStyleSheet(ButtonStyle.BUTTON_SEARCH + ButtonStyle.HOVER_EFFECT_BUTTON)
        self.cancel_button.clicked.connect(self.reject)
        self.layout.addWidget(self.cancel_button)
        self.setStyleSheet("""
                            background-color: black; /* Màu nền */
                            color: white; /* Màu chữ */
                        """)
        self.setMinimumWidth(210)
        self.setMinimumHeight(100)