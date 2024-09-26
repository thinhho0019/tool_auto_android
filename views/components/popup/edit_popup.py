from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtGui import QIcon, QGuiApplication, QShortcut, QAction
from PyQt6.QtCore import Qt
import os
from styles.main_style import MainStyle
from views.components.button_menu import ButtonMenu
class EditPopup(QDialog):
        def __init__(self, title, qhs):
            super().__init__()
            self.setWindowModality(Qt.WindowModality.ApplicationModal)
            self.setWindowTitle(title)
            self.setWindowIcon(QIcon("public/main.ico"))
            self.setupUI(qhs)
        def setupUI(self, qhs):
            layout = QVBoxLayout()
            #label-input-checkbox-radio-button
            for i in qhs:
                qh = QHBoxLayout()
                if 'label' in i:
                    label = QLabel(i['label'])
                    label.setStyleSheet(MainStyle.QLABEL_CONTENT)
                    label.setMinimumWidth(150)
                    qh.addWidget(label)
                if 'lineedit' in i:
                    lineedit = QLineEdit()
                    if 'enable' in i['lineedit']:
                        if i['lineedit']['enable'] == "false":
                            lineedit.setEnabled(False)
                    if 'value' in i['lineedit']:
                        lineedit.setText(i['lineedit']['value'])
                    lineedit.setObjectName(i['lineedit']['name'])
                    lineedit.setStyleSheet(MainStyle.QEDIT_CONTENT_SMALL)
                    lineedit.setMinimumWidth(250)
                    qh.addWidget(lineedit)
                if 'button' in i:
                    button = ButtonMenu(i['button']['placeholder'])
                    button.setObjectName(i['button']['name'])
                    qh.addWidget(button)
                layout.addLayout(qh)
            self.setLayout(layout)