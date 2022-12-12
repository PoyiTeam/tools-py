import sys

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 40)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        FormLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        FormLayout.addRow("LABEL", self.LineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
