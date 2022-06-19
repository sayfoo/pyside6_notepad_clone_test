from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel, QVBoxLayout, QWidget
from ui.ui_03_main_window import Ui_MainWindow
from ui.ui_03_form import Ui_Form
from pprint import pprint

from PySide6.QtGui import QIcon, Qt, QPixmap, QImage
from qt_material import apply_stylesheet
import os, sys


class SubWindow(QDialog, QWidget, Ui_Form):
    def __init__(self):
        super(SubWindow, self).__init__()
        self.initUI()
        self.setWindowIcon(QIcon("../img/icon_cat.png"))
        self.setWindowTitle("This is a Form test for Great Works")
        self.show()

    def initUI(self):
        self.setupUi(self) # class Ui_MainWindow(object)
        self.pushButton.clicked.connect(self.back_to_the_main_window)



    def back_to_the_main_window(self):
        self.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.sub_window = None
        self.text = None
        self.setupUi(self) # class Ui_MainWindow(object)
        self.setWindowIcon(QIcon("../img/icon_q.png"))
        self.setWindowTitle("This is a pushButton test for Great Works")

        self.pushButton_2.clicked.connect(self.left_pushButton_clicked)
        self.pushButton_3.clicked.connect(self.right_pushButton_clicked)
        self.pushButton_1.clicked.connect(self.subwindow_pushButton_clicked)

    def left_pushButton_clicked(self):
        self.pwd = os.getcwd()
        self.textEdit_1.append((f"버튼 누름\n {self.pwd}"))

    def right_pushButton_clicked(self):
        self.text = self.textEdit_1.toPlainText()
        self.textEdit_2.setText(self.text)

    def subwindow_pushButton_clicked(self):
        self.hide()
        self.text = self.textEdit_1.toPlainText()
        self.sub_window = SubWindow()
        self.sub_window.textEdit.setText(self.text)
        self.sub_window.exec() # 종료하면 돌아가도록 sys.exit()는 안한다.
        self.show()


if __name__ == "__main__":
    print(">>>>> 시작 <<<<<<")
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme='dark_yellow.xml')
    window.show()
    sys.exit(app.exec())