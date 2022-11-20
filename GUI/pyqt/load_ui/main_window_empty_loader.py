# only for show MainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

ui_file = QFile("main_window_empty.ui")
ui_file.open(QFile.ReadOnly)

loader = QUiLoader()
window = loader.load(ui_file)
window.show()
