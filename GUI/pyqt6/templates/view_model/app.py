import sys

from PySide6.QtWidgets import QApplication

from model.model import FooModel
from view.viewmodel import FooViewModel


class App(QApplication):
    def __init__(self, sys_argv=None):
        super(App, self).__init__()
        self.model = FooModel()
        self.view = FooViewModel(self.model)
        self.view.show()


app = App()
sys.exit(app.exec())
