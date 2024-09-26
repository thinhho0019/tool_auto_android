from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QListView, QComboBox, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, \
    QCheckBox, QRadioButton, QButtonGroup
import styles.main_style
from views.components.button_menu import ButtonMenu
class VHome(QWidget):
    def __init__(self, dark_mode):
        super().__init__()
        self.dark_mode = dark_mode
        self.main_vertical_layout = QVBoxLayout()
        self.main_vertical_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        ## instance button-label-text-connection
        self.title_connection = QLabel("List Connection Android")
        self.title_template = QLabel("Template AirDrop")
        self.button_reload_adb = ButtonMenu("Reload")
        self.button_check_all = ButtonMenu("Check all")
        self.button_proxy = ButtonMenu("Start proxy")
        self.button_kill_app = ButtonMenu("Kill all app")
        self.button_auto_tap_banana = ButtonMenu("Banana(Tap)")
        self.listview_connection = QListView()
        self.model_list_view_connection = QStandardItemModel()
        self.ui_rows_connection_android()
        self.setLayout(self.main_vertical_layout)
    def ui_rows_template_run(self):
        rows_layout = QHBoxLayout()
        self.title_template.setStyleSheet(styles.main_style.MainStyle.QLABEL_TITLE_DARK_MODE)
        rows_layout.addWidget(self.title_template, stretch=1)
        rows_layout.addWidget(self.button_auto_tap_banana, stretch=1)
        rows_layout.addStretch(8)
        return rows_layout
    def ui_rows_connection_android(self):
        columns_layout = QVBoxLayout()
        rows_layout = QHBoxLayout()
        self.title_connection.setStyleSheet(styles.main_style.MainStyle.QLABEL_TITLE_DARK_MODE)
        rows_layout.addWidget(self.title_connection, stretch=1)
        rows_layout.addWidget(self.button_reload_adb, stretch=1)
        rows_layout.addWidget(self.button_check_all, stretch=1)
        rows_layout.addWidget(self.button_proxy, stretch=1)
        rows_layout.addWidget(self.button_kill_app, stretch=1)
        rows_layout.addStretch(8)
        columns_layout.addLayout(rows_layout)
        # set listview connection
        # self.listview_connection.setMaximumHeight(200)
        columns_layout.addWidget(self.listview_connection)
        columns_layout.addLayout(self.ui_rows_template_run())
        self.main_vertical_layout.addLayout(columns_layout)
    def show_data_list_connection(self, value):
        self.model_list_view_connection.clear()
        print(value)
        try:
            for i in value:
                item = QStandardItem(f"{i['name']}")
                item.setCheckable(True)
                if i['checked']:
                    item.setCheckState(Qt.CheckState.Checked) # Đặt trạng thái ban đầu là chưa được chọn
                else:
                    item.setCheckState(Qt.CheckState.Unchecked)
                self.model_list_view_connection.appendRow(item)
            self.listview_connection.setModel(self.model_list_view_connection)
        except Exception as ex:
            print(ex)





