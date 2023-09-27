# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SubWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_SubWindow_Form(object):
    def setupUi(self, SubWindow_Form):
        if not SubWindow_Form.objectName():
            SubWindow_Form.setObjectName(u"SubWindow_Form")
        SubWindow_Form.resize(240, 100)
        self.Message_Label = QLabel(SubWindow_Form)
        self.Message_Label.setObjectName(u"Message_Label")
        self.Message_Label.setGeometry(QRect(10, 10, 220, 80))

        self.retranslateUi(SubWindow_Form)

        QMetaObject.connectSlotsByName(SubWindow_Form)
    # setupUi

    def retranslateUi(self, SubWindow_Form):
        SubWindow_Form.setWindowTitle(QCoreApplication.translate("SubWindow_Form", u"Sub Window", None))
        self.Message_Label.setText(QCoreApplication.translate("SubWindow_Form", u"<html><head/><body><p>This is sub window!!</p><p>Next step: limit window open if exist</p></body></html>", None))
    # retranslateUi

