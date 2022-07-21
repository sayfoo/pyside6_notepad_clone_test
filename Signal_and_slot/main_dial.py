# how to connect the relation from main widget to the dialog
from PySide6.QtGui import QPalette, QPixmap, QBrush
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QPushButton
from PySide6.QtCore import Qt
from ui.ui_test_main import Ui_Form
from ui.ui_test_dial import Ui_Dialog
from ui.ui_test_login import Ui_Login
import sys


class MyLogin(QDialog, Ui_Login):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.plt = QPalette()
        self.pmp = QPixmap("../img/login_screen.png")
        # pmp.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.plt.setBrush(QPalette.Window, QBrush(self.pmp))
        self.setPalette(self.plt)
        # self.login_btn.setGeometry(125, 479, 441, 71)


class MyDialog(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)


class MyApp(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.login = MyLogin()
        self.dial = MyDialog()

        self.btn_for_dial.clicked.connect(self.goto_the_dialog_window)
        self.btn_for_login.clicked.connect(self.goto_the_login_window)
        self.btn_for_end.clicked.connect(self.the_end_the_window)
        self.dial.back_to_the_main.clicked.connect(self.back_to_the_main_window)
        self.login.login_btn.clicked.connect(self.goto_the_main_window)

        self.goto_the_login_window()
        print("과연 여기를 지나갔을까...")
        # ---------------------------------------------------------------------------------------------------#
        #                       QPalette : set brush image with pixmap on the window
        # ---------------------------------------------------------------------------------------------------#
        self.plt = QPalette()
        self.pmp = QPixmap("../img/large_qfactory.png")
        # pmp.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.plt.setBrush(QPalette.Window, QBrush(self.pmp))
        self.groupBox.setPalette(self.plt)
        print("그런데 아무런 효과가 없넹...")
        # ---------------------------------------------------------------------------------------------------#
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        # ---------------------------------------------------------------------------------------------------#
        self.show()
        print("쇼가 끝났는데도...")

    def goto_the_login_window(self):
        self.login.exec()

    def goto_the_dialog_window(self):
        self.dial.exec()

    def goto_the_main_window(self):
        self.login.close()
        self.show()

    def back_to_the_main_window(self):
        self.dial.close()
        self.show()

    def the_end_the_window(self):
        self.close()


if __name__ == "__main__":
    if not QApplication.instance():
        print("QApplication(sys.argv) is executed...")
        app = QApplication(sys.argv)
    else:
        print("QApplication.instance() is executed...")
        app = QApplication.instance()
    exe = MyApp()

    plt = QPalette()
    pmp = QPixmap("../img/large_qfactory.png")
    # pmp.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    plt.setBrush(QPalette.Window, QBrush(pmp))
    exe.groupBox.setPalette(plt)
    try:
        sys.exit(app.exec())
    except SystemExit as e:
        print(f"정상적으로 마감했을까...[{e}]")
