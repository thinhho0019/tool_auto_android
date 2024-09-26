import os
import subprocess
import time

from PyQt6.QtCore import Qt
from concurrent.futures import ThreadPoolExecutor

from services.exec_image import detect_image
from views.components.message_box import MessageBox


class HomeController:
    def __init__(self, ui_home, main_model):
        self.main_model = main_model
        self.ui_home = ui_home
        self.connect_button()
        self.listening_ob()
        self.main_model.ob_connections = self.get_adb_devices()
        self.ui_home.model_list_view_connection.itemChanged.connect(self.on_item_changed)

    def listening_ob(self):
        self.main_model.value_list_connects.connect(self.ui_home.show_data_list_connection)

    def connect_button(self):
        self.ui_home.button_reload_adb.clicked.connect(self.reload_adb_devices)
        self.ui_home.button_check_all.clicked.connect(self.check_all)
        self.ui_home.button_proxy.clicked.connect(self.start_proxy)
        self.ui_home.button_kill_app.clicked.connect(self.kill_all_app)
        self.ui_home.button_auto_tap_banana.clicked.connect(
            lambda: self.open_telegram("BANANA", self.main_model.ob_connections, "auto-click-banana"))

    def reload_adb_devices(self):
        try:
            self.main_model.ob_connections = self.get_adb_devices()
            MessageBox("Succes reload connection!")
        except Exception as ex:
            MessageBox("Reload " + str(ex))

    def get_list_connect_choose(self):
        temp = []
        for i in self.main_model.ob_connections:
            if i['checked']:
                temp.append(i['name'])
        return temp

    def thread_turnon_socket_proxy(self, name_divice):
        subprocess.run(
            f'adb -s {name_divice} shell monkey -p net.typeblog.socks -c android.intent.category.LAUNCHER 1')
        time.sleep(1.5)
        subprocess.run(f'adb -s {name_divice} shell input tap 270 35')

    def start_proxy(self):
        with ThreadPoolExecutor(max_workers=len(self.main_model.ob_connections)) as ex:
            for i in self.get_list_connect_choose():
                ex.submit(self.thread_turnon_socket_proxy, i)

    def get_list_app_started(self, devices):
        list_app = []
        result = subprocess.run(['adb', '-s', devices, 'shell', 'pm', 'list', 'packages', '-3'],
                                capture_output=True, text=True)
        devices_output = result.stdout.splitlines()
        list_app = [app.replace("package:", "") for app in devices_output[1:]]
        return list_app

    def kill_all_app(self):
        with ThreadPoolExecutor(max_workers=len(self.main_model.ob_connections)) as ex:
            for i in self.get_list_connect_choose():
                subprocess.run(f"adb -s {i} shell input keyevent 3")
                data = ex.submit(self.get_list_app_started, i)
                for app in data.result():
                    subprocess.run(f'adb -s {i} shell am force-stop {app}')

    def on_item_changed(self, item):
        # Kiểm tra trạng thái của checkbox
        for index, i in enumerate(self.main_model.ob_connections):
            if i['name'] == item.text():
                if item.checkState() == Qt.CheckState.Checked:
                    self.main_model.ob_connections[index]['checked'] = True
                else:
                    self.main_model.ob_connections[index]['checked'] = False
        self.main_model.ob_connections = self.main_model.ob_connections

    def open_application(self, name_device, name_package):
        subprocess.run(
            f'adb -s {name_device} shell monkey -p {name_package} -c android.intent.category.LAUNCHER 1')

    def open_telegram(self, name_game, data, task):
        def countdown_execimage(direc_image, name_device):
            max_count = 0
            while max_count < 500:
                result = detect_image(direc_image, name_device)
                if result['result'] == 'error':
                    continue
                if len(result['result']) > 0:
                    a, b = result['result'][0]
                    subprocess.run(f'adb -s {name_device} shell input tap {a} {b}')
                    return
                max_count += 1
        def menu_task(name_device, task):
            if task == "auto-click-banana":
                numbers_click_banana = 0
                while numbers_click_banana < 1200:
                    subprocess.run(f'adb -s {name_device} shell input tap 168 237')
                    time.sleep(0.2)
                    numbers_click_banana += 1
        def thread_open_telegram_search(name_device, name_game, task):
            name_device = name_device['name']
            self.kill_all_app()
            time.sleep(1)
            self.open_application(name_device, "org.telegram.messenger.web")
            time.sleep(1)
            countdown_execimage(["./public/image_sys/search.png"], name_device)
            time.sleep(1)
            subprocess.run(f"adb -s {name_device} shell input text {name_game}")
            countdown_execimage(["./public/image_sys/banana/banana.png"], name_device)
            time.sleep(1)
            countdown_execimage(["./public/image_sys/play.png"], name_device)
            time.sleep(3)
            ##auto_click
            # menu_task(name_device, task)
        with ThreadPoolExecutor(max_workers=len(data)) as ex:
            for i in data:
                if i['checked']:
                    ex.submit(thread_open_telegram_search, i, name_game, task)
    def check_all(self):
        try:
            for index, i in enumerate(self.main_model.ob_connections):
                self.main_model.ob_connections[index]['checked'] = True
            self.main_model.ob_connections = self.main_model.ob_connections
        except Exception as ex:
            MessageBox("Fail check all connections!")

    def get_adb_devices(self):
        # Chạy lệnh adb devices để lấy danh sách thiết bị
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        # Phân tích kết quả trả về
        devices_output = result.stdout.splitlines()
        # Bỏ qua dòng đầu tiên vì nó chứa thông tin tiêu đề "List of devices attached"
        devices = [{"name": line.split()[0], "checked": False} for line in devices_output[1:] if line.strip()]
        return devices
