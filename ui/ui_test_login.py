# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_logindmOrBv.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(623, 623)
        Login.setMinimumSize(QSize(623, 623))
        Login.setMaximumSize(QSize(623, 623))
        Login.setLayoutDirection(Qt.RightToLeft)
        Login.setStyleSheet(u"")
        self.login_btn = QPushButton(Login)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(92, 490, 443, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMinimumSize(QSize(443, 71))
        self.login_btn.setMaximumSize(QSize(443, 71))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.login_btn.setFont(font)
        self.login_btn.setLayoutDirection(Qt.LeftToRight)
        self.login_btn.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"background-color: rgb(66, 195, 255);")
        self.userid = QTextEdit(Login)
        self.userid.setObjectName(u"userid")
        self.userid.setGeometry(QRect(330, 285, 181, 31))
        sizePolicy.setHeightForWidth(self.userid.sizePolicy().hasHeightForWidth())
        self.userid.setSizePolicy(sizePolicy)
        self.userid.setMinimumSize(QSize(181, 31))
        self.userid.setMaximumSize(QSize(181, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.userid.setFont(font1)
        self.userid.setLayoutDirection(Qt.LeftToRight)
        self.combo_02 = QComboBox(Login)
        self.combo_02.addItem("")
        self.combo_02.addItem("")
        self.combo_02.setObjectName(u"combo_02")
        self.combo_02.setGeometry(QRect(330, 427, 181, 31))
        sizePolicy.setHeightForWidth(self.combo_02.sizePolicy().hasHeightForWidth())
        self.combo_02.setSizePolicy(sizePolicy)
        self.combo_02.setMinimumSize(QSize(181, 31))
        self.combo_02.setMaximumSize(QSize(181, 31))
        self.combo_02.setLayoutDirection(Qt.LeftToRight)
        self.psswd = QTextEdit(Login)
        self.psswd.setObjectName(u"psswd")
        self.psswd.setGeometry(QRect(330, 357, 181, 31))
        sizePolicy.setHeightForWidth(self.psswd.sizePolicy().hasHeightForWidth())
        self.psswd.setSizePolicy(sizePolicy)
        self.psswd.setMinimumSize(QSize(181, 31))
        self.psswd.setMaximumSize(QSize(181, 31))
        self.psswd.setFont(font1)
        self.psswd.setLayoutDirection(Qt.LeftToRight)
        self.combo_01 = QComboBox(Login)
        self.combo_01.addItem("")
        self.combo_01.addItem("")
        self.combo_01.setObjectName(u"combo_01")
        self.combo_01.setGeometry(QRect(330, 215, 181, 31))
        sizePolicy.setHeightForWidth(self.combo_01.sizePolicy().hasHeightForWidth())
        self.combo_01.setSizePolicy(sizePolicy)
        self.combo_01.setMinimumSize(QSize(181, 31))
        self.combo_01.setMaximumSize(QSize(181, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.combo_01.setFont(font2)
        self.combo_01.setLayoutDirection(Qt.LeftToRight)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"\ub85c\uadf8\uc778", None))
        self.login_btn.setText(QCoreApplication.translate("Login", u"LOGIN", None))
        self.userid.setPlaceholderText(QCoreApplication.translate("Login", u"USER ID", None))
        self.combo_02.setItemText(0, QCoreApplication.translate("Login", u"LANGUAGE", None))
        self.combo_02.setItemText(1, QCoreApplication.translate("Login", u"\ud55c\uad6d\uc5b4", None))

        self.psswd.setPlaceholderText(QCoreApplication.translate("Login", u"PASSWORD", None))
        self.combo_01.setItemText(0, QCoreApplication.translate("Login", u"COMPANY", None))
        self.combo_01.setItemText(1, QCoreApplication.translate("Login", u"\ubcf8\uc0ac", None))

    # retranslateUi

