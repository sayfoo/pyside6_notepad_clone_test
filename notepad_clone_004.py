from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QVBoxLayout, QWidget
from ui.ui_notepad_clone_01 import Ui_MainWindow
from PySide6.QtGui import QIcon, Qt, QPixmap, QImage
from qt_material import apply_stylesheet
import os, sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self) # class Ui_MainWindow(object)
        self.setWindowIcon(QIcon("img/icon_q.png"))
        self.setWindowTitle("This is a clone test for Great Works")

        print(f"{os.getcwd() = }")

        pixmap = QPixmap(QImage('img/large_qfactory.png'))
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        # layout = QVBoxLayout()
        # layout.addWidget(self.label)
        # container = QWidget()
        # container.setLayout(layout)
        # self.setCentralWidget(container)

        self.action_W.triggered.connect(self.add_window)  # 새창 QAction name is action_W
        self.action_O.triggered.connect(self.open_file)   # 열기(O)
        self.action_S.triggered.connect(self.save_file)   # 저장(S)
        self.windows = []

    def add_window(self):
        new_window = MainWindow()
        self.windows.append(new_window)                   #
        new_window.show()

    def open_file(self):  # 열기(O)
        file_name = QFileDialog.getOpenFileName(self)
        if file_name[0]:
            with open(file_name[0], encoding='UTF-8') as f:
                text = f.read()
            self.plainTextEdit.setPlainText(text)

    def save_file(self):  # 저장(S)
        file_name = QFileDialog.getSaveFileName(self)
        if file_name[0]:
            text = self.plainTextEdit.toPlainText()
            with open(file_name[0], 'w', encoding='UTF-8') as f:
                f.write(text)


if __name__ == "__main__":
    print(">>>>> 시작 <<<<<<")
    app = QApplication(sys.argv)
    window = MainWindow()
    # apply_stylesheet(app, theme='dark_yellow.xml')
    extra = {

        # Density Scale
        'density_scale': '-2',
    }
    apply_stylesheet(app, theme='dark_yellow.xml', extra=extra)
    window.show()
    sys.exit(app.exec())
