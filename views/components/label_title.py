from PyQt6.QtWidgets import QLabel
from styles.main_style import MainStyle
class LabelTitle(QLabel):
    def __init__(self, title, parent=None):
        super().__init__()
        self.title = title
        self.setupUi()
    def setupUi(self):
        self.setText(self.title)
        self.setStyleSheet(MainStyle.QLABEL_CONTENT)

