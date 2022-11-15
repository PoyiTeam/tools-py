import sys
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QWidget, QApplication


class Foo1(QWidget):
    valueChanged = Signal(int)

    def __init__(self, parent=None):
        super(Foo1, self).__init__(parent)
        self._t = 0

    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, value):
        self._t = value
        self.valueChanged.emit(value)
        print('value emit!')


class Foo2(QWidget):
    valueChanged = Signal(int)

    def __init__(self, parent=None):
        super(Foo2, self).__init__(parent)
        self.t = 0

    def __setattr__(self, key, value):
        """
        ___setattr__ will be called while value
        """
        self.valueChanged.emit(value)
        print('value emit!')


app = QApplication(sys.argv)
foo_1 = Foo1()
foo_2 = Foo2()
# print(Foo.__getattr__())
for i in range(5):
    foo_1.t = i
    foo_2.t = i
    print(foo_1.t)

print(Foo2.__dict__)
