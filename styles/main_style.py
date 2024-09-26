class MainStyle:
    def __init__(self, dark):
        if dark:
            self.text_color_check = "white"
        else:
            self.text_color_check = "black"
    QLABEL_TITLE = "QLabel{font-size: 20px; color: black; border: none; padding-left:2px;font-weight:bold}"
    QLABEL_TITLE_DARK_MODE = "QLabel{font-size: 20px; color: white; border: none; padding-left:2px;font-weight:bold}"
    QWIDGET_PAGE = "QWidget{background-color: rgb(39, 39, 39); border-radius:8px}"
    QWIDGET_PAGE_COMPONENT = "QWidget{border:1px solid white; border-radius:8px}"
    QWIDGET_PAGE_NONE_BORDER = "QWidget{border:1px solid white; border-radius:8px;border:none}"
    QWIDGET_LIST_VIEW = "QWidget{background-color: rgb(39, 39, 39); border:1px solid white; border-radius:8px;padding:5px}"
    QLABEL_CONTENT = "QLabel{font-size: 12px;color:black;border:none; font-weight: bold;}"
    QLABEL_CONTENT_DARK_MODE = "QLabel{font-size: 12px;color:white;border:none; font-weight: bold;}"
    QEDIT_CONTENT = "QLineEdit{font-size:13px;padding:8px;border:none;}"
    QEDIT_CONTENT_SMALL = "QLineEdit{font-size:12px;padding:5px;border:none;}"
    QTEXTEDIT_CONTENT = "QTextEdit{font-size:13px;padding:0px;border:none;border-radius:8px}"
    QCOMBOBOX = "QComboBox{border:none; border-radius:5px;background-color: black; min-height:25px;color:black}"
    QLABEL_IMAGE = "QLabel{background-color: black;border:1px solid white; border-radius:8px; min-height:270px; min-width:200px; max-height:250px;}"