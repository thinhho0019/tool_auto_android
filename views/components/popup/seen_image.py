from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QScrollArea, QVBoxLayout
from PyQt6.QtGui import QPixmap, QIcon

from threads.ImageLoaderThread import ImageLoaderThread


class SeenImage(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("public/main.ico"))
        # Thiết lập tiêu đề và kích thước của dialog
        self.setWindowTitle("Image Viewer")
        self.resize(640, 800)

        # Tạo layout
        layout = QVBoxLayout(self)
        # Tạo QLabel để chứa ảnh
        self.image_label = QLabel()
        # Tạo QScrollArea và thiết lập QLabel là widget con
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.image_label)

        # Thêm QScrollArea vào layout
        layout.addWidget(self.scroll_area)

    def update_state_image_loaded(self, noti, pixmap):
        if noti == 'fail' or noti == 'error':
            self.image_label.setText("Không thể hiện hình!!")
            return
        width_pixmap = pixmap.width()
        height_pixmap = pixmap.height()
        scale = 600 / width_pixmap
        new_height = int(height_pixmap * scale)
        scaled_pixmap = pixmap.scaled(600, new_height, Qt.AspectRatioMode.KeepAspectRatio)
        self.image_label.setPixmap(scaled_pixmap)

    def load_pixmap(self, url_image):
        self.thread_loadimage = ImageLoaderThread(url_image)
        self.thread_loadimage.imageLoaded.connect(self.update_state_image_loaded)
        self.thread_loadimage.start()