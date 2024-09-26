from PyQt6.QtWidgets import QLineEdit
from styles.main_style import  MainStyle

class EditText(QLineEdit):
    def __init__(self, parent=None):
        super(EditText, self).__init__(parent)
        self.setup_ui()
    def setup_ui(self):
        self.setStyleSheet(MainStyle.QEDIT_CONTENT)
