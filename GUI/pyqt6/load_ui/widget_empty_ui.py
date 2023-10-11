# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_empty.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_EmptyWidget(object):
    def setupUi(self, EmptyWidget):
        if not EmptyWidget.objectName():
            EmptyWidget.setObjectName(u"EmptyWidget")
        EmptyWidget.resize(400, 300)
        self.pushButton = QPushButton(EmptyWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 75, 24))

        self.retranslateUi(EmptyWidget)

        QMetaObject.connectSlotsByName(EmptyWidget)
    # setupUi

    def retranslateUi(self, EmptyWidget):
        EmptyWidget.setWindowTitle(QCoreApplication.translate("EmptyWidget", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("EmptyWidget", u"PushButton", None))
    # retranslateUi

