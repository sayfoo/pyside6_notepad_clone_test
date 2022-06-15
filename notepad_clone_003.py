import sys

from PySide6.QtGui import QPixmap, QImage, Qt
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QVBoxLayout, QWidget, QLabel
import os

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        print(f"{os.getcwd() = }")
        self.btn = QPushButton("push button")
        self.lab = QLabel()
        self.lab.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(QImage('img/mk.png'))
        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(pixmap)
        self.lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        self.lbl_size.setAlignment(Qt.AlignCenter)
        self.lbl_img.setScaledContents(True)
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.lab)
        layout.addWidget(self.lbl_img)
        layout.addWidget(self.lbl_size)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.label_count = 0

        self.btn.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.label_count += 1
        self.lab.setText(f"{self.label_count}가 말씀하셨나요")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = MyApp()
    exe.show()
    sys.exit(app.exec())