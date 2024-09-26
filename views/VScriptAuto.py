from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QListView, QComboBox, QVBoxLayout, QLineEdit, QTextEdit, \
    QPushButton, \
    QCheckBox, QRadioButton, QButtonGroup
import styles.main_style
from views.components.button_menu import ButtonMenu


class VHome(QWidget):
    def __init__(self, dark_mode):
        super().__init__()
        self.dark_mode = dark_mode
