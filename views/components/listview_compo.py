from PyQt6.QtWidgets import (QApplication, QListView, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QLabel, QPushButton)
from PyQt6.QtGui import QIcon, QPixmap, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from styles.main_style import MainStyle
from views.components.button_menu import ButtonMenu


class ListView(QHBoxLayout):
    def __init__(self, title):
        super().__init__()
        self.button_add = ButtonMenu("Add item")
        self.button_remove = ButtonMenu("Remove item")
        self.button_edit = ButtonMenu("Edit item")
        self.button_seen_image = ButtonMenu("Seen image")
        self.button_refresh = ButtonMenu("Refresh item")
        self.button_search = ButtonMenu("SEARCH")
        self.button_clear = ButtonMenu("CLEAR")
        self.title = title
        self.edit_text_search = QLineEdit()
        self.edit_text_search.setPlaceholderText("Nội dung tìm kiếm!!")
        self.initUI()
    def initUI(self):
        layout = QVBoxLayout()
        label = QLabel(self.title)
        label.setStyleSheet(MainStyle.QLABEL_TITLE)
        self.list_view = QListView()
        self.list_view.setStyleSheet("border:none")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addLayout(self.rows_search())
        layout.addWidget(self.list_view)
        if self.title == "CHAPTER" or self.title == "IMAGES" or self.title == "TYPE COMIC":
            layout.addLayout(self.list_button())
        self.model = QStandardItemModel()
        self.list_view.setModel(self.model)
        self.addLayout(layout)

    def rows_search(self):
        qh = QHBoxLayout()
        self.button_search.setFixedWidth(100)
        self.edit_text_search.setStyleSheet(MainStyle.QEDIT_CONTENT_SMALL)
        qh.addWidget(self.edit_text_search)
        qh.addWidget(self.button_clear)
        qh.addWidget(self.button_search)
        return qh
    def list_button(self):
        qh = QHBoxLayout()
        qh.addWidget(self.button_add)
        qh.addWidget(self.button_remove)

        if self.title != "IMAGES":
            qh.addWidget(self.button_refresh)
            qh.addWidget(self.button_edit)
        else:
            qh.addWidget(self.button_seen_image)

        return qh
    def show_data_search(self, data):
        self.model.clear()
        if data is None:
            return
        for item in data:
            standard_item = QStandardItem()
            standard_item.setText(f"id: {item['_id']}\nname: {item['name']}")
            standard_item.setIcon(QIcon(QPixmap("public/down.png")))
            standard_item.setData(item)
            self.model.appendRow(standard_item)
    def show_data_list_comic(self, value):
        self.model.clear()
        for item in value:
            standard_item = QStandardItem()
            standard_item.setText(f"id: {item['_id']}\nname: {item['name']}")
            standard_item.setIcon(QIcon(QPixmap("public/down.png")))
            standard_item.setData(item)
            self.model.appendRow(standard_item)
    def show_data_list(self, value):
        self.model.clear()
        for item in value:
            standard_item = QStandardItem()
            standard_item.setText(f"id: {item['_id']}\nname: {item['name']}")
            standard_item.setIcon(QIcon(QPixmap("public/down.png")))
            standard_item.setData(item)
            self.model.appendRow(standard_item)
    def show_data_list_image(self, value):
        self.model.clear()
        for item in value:
            standard_item = QStandardItem()
            standard_item.setText(f"name: {item.split("/")[1]}")
            standard_item.setIcon(QIcon(QPixmap("public/down.png")))
            standard_item.setData(item)
            self.model.appendRow(standard_item)
