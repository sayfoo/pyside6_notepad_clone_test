# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '03_sub_windowlOuDaG.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_SubWindow(object):
    def setupUi(self, SubWindow):
        if not SubWindow.objectName():
            SubWindow.setObjectName(u"SubWindow")
        SubWindow.resize(640, 480)
        self.centralwidget = QWidget(SubWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.verticalLayout.addWidget(self.textEdit_3)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        SubWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SubWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 22))
        SubWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SubWindow)
        self.statusbar.setObjectName(u"statusbar")
        SubWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubWindow)

        QMetaObject.connectSlotsByName(SubWindow)
    # setupUi

    def retranslateUi(self, SubWindow):
        SubWindow.setWindowTitle(QCoreApplication.translate("SubWindow", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("SubWindow", u"conform button", None))
        self.pushButton_5.setText(QCoreApplication.translate("SubWindow", u"Back tothe main window", None))
    # retranslateUi

