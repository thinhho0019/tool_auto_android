from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QGuiApplication, QShortcut, QAction, QPalette
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QStackedWidget
from controllers.home_controller import HomeController
from models.main_model import MainModel
from styles.button_style import ButtonStyle
from views.VHome import VHome
from views.components.button_menu import ButtonMenu
class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #check dark mode
        if self.is_dark_mode():
            self.dark_mode = True
        else:
            self.dark_mode = False
        self.ob_connections = MainModel()
        self.setWindowTitle("Tool Auto Add Script")
        self.setWindowIcon(QIcon("public/main.png"))
        self.setGeometry(100, 100, 1000, 700)  # Set window size
        self.container = QWidget()
        self.main_layout = QVBoxLayout()
        self.init_ui()
        self.ui_stacked_menu()
        self.home_controller = HomeController(self.page_home, self.ob_connections)
        self.setCentralWidget(self.container)
    def init_ui(self):
        self.ui_menu()
    def ui_menu(self):
        QhMenu = QHBoxLayout()
        QhMenu.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.button_home = ButtonMenu("Home")
        self.button_create_script = ButtonMenu("Create Scripts")
        self.button_home.setStyleSheet(ButtonStyle.BUTTON_CLICKED + ButtonStyle.HOVER_EFFECT_BUTTON)
        QhMenu.addWidget(self.button_home)
        QhMenu.addWidget(self.button_create_script)
        self.main_layout.addLayout(QhMenu)
        self.container.setLayout(self.main_layout)
    def ui_stacked_menu(self):
        self.stack = QStackedWidget(self)
        self.page_home = VHome(self.dark_mode)
        self.stack.addWidget(self.page_home)
        self.main_layout.addWidget(self.stack)
        self.setLayout(self.main_layout)
    def button_click_home(self):
        self.stack.setCurrentIndex(0)
        self.button_home.setStyleSheet(ButtonStyle.BUTTON_CLICKED + ButtonStyle.HOVER_EFFECT_BUTTON)
    def is_dark_mode(self):
        palette = QApplication.instance().palette()
        background_color = palette.color(QPalette.ColorRole.Window)
        text_color = palette.color(QPalette.ColorRole.WindowText)
        # So sánh màu nền với một ngưỡng tối (dark threshold)
        # Nếu màu nền tối hơn, ta cho rằng đang ở chế độ Dark Mode
        # Màu background thường sáng hơn ở Light Mode và tối hơn ở Dark Mode
        brightness = background_color.red() * 0.299 + background_color.green() * 0.587 + background_color.blue() * 0.114
        return brightness < 128  # ngưỡng để xác định "tối"
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MenuWindow()
    ui.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()