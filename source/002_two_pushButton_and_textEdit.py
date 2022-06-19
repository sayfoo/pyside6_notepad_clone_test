from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QVBoxLayout, QWidget
from ui.ui_02_two_pushButton_and_textEdit import Ui_MainWindow

from PySide6.QtGui import QIcon, Qt, QPixmap, QImage
from qt_material import apply_stylesheet
import os, sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self) # class Ui_MainWindow(object)
        self.setWindowIcon(QIcon("../img/icon_q.png"))
        self.setWindowTitle("This is a pushButton test for Great Works")

        self.orig_pushButton.clicked.connect(self.orig_button_clicked)
        self.dest_pushButton.clicked.connect(self.dest_button_clicked)

    def orig_button_clicked(self):
        self.pwd = os.getcwd()
        self.textEdit.append((f"버튼 누름\n {self.pwd}"))

    def dest_button_clicked(self):
        self.text = self.textEdit.toPlainText()
        self.textEdit_2.setText(self.text)

if __name__ == "__main__":
    print(">>>>> 시작 <<<<<<")
    app = QApplication(sys.argv)
    window = MainWindow()
    # apply_stylesheet(app, theme='dark_yellow.xml', extra=extra)
    window.show()
    sys.exit(app.exec())