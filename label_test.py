import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel 예제")

        widget = QLabel("<= > <= >= == != 안녕하세요!")

        font = widget.font()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)

        font.setFamily("D2Coding Ligature")

        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())