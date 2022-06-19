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
        self.show()

    def initUI(self):
        self.setupUi(self) # class Ui_MainWindow(object)
        self.pushButton.clicked.connect(self.back_to_the_main_window)


    def back_to_the_main_window(self):
        self.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self) # class Ui_MainWindow(object)
        self.setWindowIcon(QIcon("../img/icon_q.png"))
        self.setWindowTitle("This is a pushButton test for Great Works")

        self.pushButton_2.clicked.connect(self.pushButton_2_button_clicked)
        self.pushButton_3.clicked.connect(self.pushButton_3_button_clicked)
        self.pushButton_1.clicked.connect(self.pushButton_1_button_clicked)

    def pushButton_2_button_clicked(self):
        self.pwd = os.getcwd()
        self.textEdit_1.append((f"버튼 누름\n {self.pwd}"))

    def pushButton_3_button_clicked(self):
        self.text = self.textEdit_1.toPlainText()
        self.textEdit_2.setText(self.text)

    def pushButton_1_button_clicked(self):
        self.hide()
        self.sub_window = SubWindow()
        self.sub_window.exec()
        self.show()


if __name__ == "__main__":
    print(">>>>> 시작 <<<<<<")
    app = QApplication(sys.argv)
    window = MainWindow()
    # apply_stylesheet(app, theme='dark_yellow.xml', extra=extra)
    window.show()
    sys.exit(app.exec())