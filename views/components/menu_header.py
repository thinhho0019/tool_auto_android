from PyQt6.QtWidgets import (QApplication, QListView, QVBoxLayout, QWidget, QHBoxLayout, QComboBox, QLineEdit)
from views.components.button_menu import ButtonMenu
from styles.main_style import MainStyle
from PyQt6.QtWidgets import (QApplication, QListView, QVBoxLayout, QWidget, QHBoxLayout)
from PyQt6.QtGui import QIcon, QPixmap, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from styles.main_style import MainStyle
from views.components.message_box import MessageBox


class MenuHeader(QHBoxLayout):
    def __init__(self):
        super().__init__()
        # self.combobox_location = QLineEdit()
        # self.combobox_location.setStyleSheet(MainStyle.QCOMBOBOX)
        # self.edit_text_search = QLineEdit()
        # self.button_search = ButtonMenu("SEARCH")
        self.button_load_server = ButtonMenu("LOAD SERVER")
        # self.button_load_all_server = ButtonMenu("LOAD ALL SERVER")
        self.init_ui()
    def init_ui(self):
        # self.addWidget(self.combobox_location)
        self.addWidget(self.button_load_server)
        # self.addWidget(self.button_load_all_server)
        # self.addWidget(self.edit_text_search)
        # self.addWidget(self.button_search)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # self.config_cb()
        self.config_button()
        self.config_edittext()


    def config_button(self):
        self.button_load_server.setFixedWidth(200)
        # self.button_load_all_server.setFixedWidth(200)
        # self.button_search.setFixedWidth(100)
    def config_edittext(self):
        # self.edit_text_search.setStyleSheet(MainStyle.QEDIT_CONTENT_SMALL)
        return