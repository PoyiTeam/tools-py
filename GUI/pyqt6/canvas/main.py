import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from canvas import Canvas


class App(QApplication):
    def __init__(self, sys_argv=None):

        super(App, self).__init__()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.view = QGraphicsView(self)
        self.scene = Canvas(640, 480)
        self.view.setScene(self.scene)

        self.setCentralWidget(self.view)

        self.setWindowTitle("Custom Graphics Item Example")
        self.setGeometry(100, 100, 800, 600)


def main():

    app = App(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
