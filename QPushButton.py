from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
import sys

class MyWin(QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        self.button = QPushButton("push button")
        self.label = QLabel()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

        self.button.setCheckable(True)

        self.button.clicked.connect(self.button_clicked)
        self.click_count = 0

    def button_clicked(self):
        self.click_count += 1
        self.label.setText(f"{self.click_count}번 클릭함")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec())