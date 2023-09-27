from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette, QGuiApplication


class DarkTheme(QWidget):

    def change_dark_theme(self):
        self.dark_palette = QPalette()
        self.dark_palette.setColor(QPalette.Window, QColor(41, 44, 51))
        self.dark_palette.setColor(QPalette.WindowText, Qt.white)
        self.dark_palette.setColor(QPalette.Base, QColor(15, 15, 15))
        self.dark_palette.setColor(QPalette.AlternateBase, QColor(41, 44, 51))
        self.dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        self.dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        self.dark_palette.setColor(QPalette.Text, Qt.white)
        self.dark_palette.setColor(QPalette.Button, QColor(41, 44, 51))
        self.dark_palette.setColor(QPalette.ButtonText, Qt.white)
        self.dark_palette.setColor(QPalette.BrightText, Qt.red)
        self.dark_palette.setColor(QPalette.Highlight, QColor(100, 100, 225))
        self.dark_palette.setColor(QPalette.HighlightedText, Qt.white)
        #self.dark_palette.setColor(QPalette.PlaceholderText, Qt.white)
        QGuiApplication.setPalette(self.dark_palette)
