import sys
from PySide6.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PySide6.QtCore import QLocale, QTranslator
from PySide6.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'File System View'
        self.setLocale(QLocale(QLocale.English))
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)

        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.setColumnHidden(1, True)
        self.tree.setColumnHidden(2, True)
        self.tree.setColumnHidden(3, True)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)


app = QApplication(sys.argv)
file_treeview = App()
print(file_treeview.locale())
file_treeview.show()
sys.exit(app.exec())
