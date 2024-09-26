from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton
from styles.button_style import ButtonStyle

class ButtonMenu(QPushButton):
    def __init__(self, title, parent=None):
        super(ButtonMenu, self).__init__(title, parent)
        if title == "CLEAR":
            self.setIcon(QIcon("./public/icons/clear.png"))
            self.setMinimumWidth(30)
        else:
            self.setText(title)
        self.setStyleSheet(ButtonStyle.BUTTON_MENU + ButtonStyle.HOVER_EFFECT_BUTTON)
