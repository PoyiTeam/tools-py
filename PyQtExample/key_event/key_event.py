import sys
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCharts import QChart, QChartView
from PySide6.QtGui import QKeyEvent


class Chart(QChart):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        print(f'key num: {event.key()} / key text: {event.text()}')


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        print(f'key num: {event.key()} / key text: {event.text()}')


app = QApplication(sys.argv)
chart = Chart()
chart_view = QChartView(chart)
window = MainWindow().
window.show()
chart_view.show()


sys.exit(app.exec_())
