from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox

class MessageBox(QMessageBox):
    def __init__(self, title):
        super().__init__()
        self.setWindowIcon(QIcon("./public/main.png"))
        self.setWindowTitle("Notification")
        self.setText(title)
        self.setIcon(QMessageBox.Icon.Information)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.setStyleSheet("""
                    background-color: black; /* Màu nền */
                    color: white; /* Màu chữ */
                """)
        self.exec()