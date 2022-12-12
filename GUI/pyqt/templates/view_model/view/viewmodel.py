from .ui_view import Ui_Form
from PySide6.QtWidgets import QWidget


class FooViewModel(QWidget):

    def __init__(self, model):
        super().__init__()
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        self._model = model
