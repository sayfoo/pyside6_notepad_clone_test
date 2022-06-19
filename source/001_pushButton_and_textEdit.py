from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QVBoxLayout, QWidget
from ui.ui_01_pushButton_and_textEdit import Ui_MainWindow

from PySide6.QtGui import QIcon, Qt, QPixmap, QImage
from qt_material import apply_stylesheet
import os, sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self) # class Ui_MainWindow(object)
        self.setWindowIcon(QIcon("../img/icon_q.png"))
        self.setWindowTitle("This is a pushButton test for Great Works")

        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        pwd = os.getcwd()
        # self.textEdit.setText("버튼 누름")
        self.textEdit.append((f"버튼 누름\n {pwd}"))
        # self.textEdit.insertPlainText("버튼 누름")

if __name__ == "__main__":
    print(">>>>> 시작 <<<<<<")
    app = QApplication(sys.argv)
    window = MainWindow()
    # apply_stylesheet(app, theme='dark_yellow.xml', extra=extra)
    window.show()
    sys.exit(app.exec())