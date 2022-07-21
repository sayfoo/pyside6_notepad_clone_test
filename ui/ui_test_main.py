# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_mainzXxFou.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(626, 508)
        Form.setStyleSheet(u"font: 700 20pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);")
        self.btn_for_dial = QPushButton(self.groupBox)
        self.btn_for_dial.setObjectName(u"btn_for_dial")
        self.btn_for_dial.setGeometry(QRect(40, 90, 531, 81))
        self.btn_for_dial.setStyleSheet(u"color: rgb(85, 255, 255);")
        self.btn_for_end = QPushButton(self.groupBox)
        self.btn_for_end.setObjectName(u"btn_for_end")
        self.btn_for_end.setGeometry(QRect(230, 380, 191, 91))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_for_end.sizePolicy().hasHeightForWidth())
        self.btn_for_end.setSizePolicy(sizePolicy1)
        self.btn_for_end.setStyleSheet(u"color: rgb(170, 255, 0);")
        self.btn_for_login = QPushButton(self.groupBox)
        self.btn_for_login.setObjectName(u"btn_for_login")
        self.btn_for_login.setGeometry(QRect(40, 210, 531, 81))
        self.btn_for_login.setStyleSheet(u"color: rgb(255, 255, 0);")

        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\uba54\uc778 \ud654\uba74", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.btn_for_dial.setText(QCoreApplication.translate("Form", u"Go to Dialog", None))
        self.btn_for_end.setText(QCoreApplication.translate("Form", u"The end", None))
        self.btn_for_login.setText(QCoreApplication.translate("Form", u"Go to Login", None))
    # retranslateUi

