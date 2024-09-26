from PyQt6.QtCore import QObject, pyqtSignal
class MainModel(QObject):
    value_list_connects = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self._ob_connections = []
    @property
    def ob_connections(self):
        return self._ob_connections
    @ob_connections.setter
    def ob_connections(self, value):
        self._ob_connections = value
        self.value_list_connects.emit(value)
