import sys

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 40)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.VBoxLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.HBoxLayout = QtWidgets.QHBoxLayout()
        self.HBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.Label = QtWidgets.QLabel(self.centralwidget)
        self.Label.setText("LABEL")
        self.HBoxLayout.addWidget(self.Label)
        self.LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.HBoxLayout.addWidget(self.LineEdit)
        self.VBoxLayout.addLayout(self.HBoxLayout)
        SpacerItem = QtWidgets.QSpacerItem(
            20, 245,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum)
        self.VBoxLayout.addItem(SpacerItem)
        MainWindow.setCentralWidget(self.centralwidget)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
