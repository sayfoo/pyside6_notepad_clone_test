import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDialog, QToolTip
from PySide6.QtGui import QIcon, QPixmap, QFont
from PySide6.QtCore import QCoreApplication
import random


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.UI_init()

    def UI_init(self):
        self.image()
        self.button()
        self.tool_tip()
        self.first_look()

        self.setWindowTitle('Trials and errors!')
        self.setWindowIcon(QIcon('img/icon_q.png'))
        self.setGeometry(500, 500, 618, 400)
        self.show()

    def image(self):
        self.image = QLabel(self)
        # 이미지 원본 크기 : 175, 220
        # img_01.size = (69, 33)
        # img_02.size = (89, 94)
        # img_03.size = (618, 93)
        self.image.setPixmap(QPixmap('img/logo_qfactory.png').scaled(618, 93))
        self.image.move(0, 0)

    def button(self):
        self.vote_button = QPushButton('RandInt', self)
        self.vote_button.setFixedSize(340, 40)
        self.vote_button.move(130, 290)
        self.vote_button.clicked.connect(self.choice)

        self.quit_button = QPushButton('Quit', self)
        self.quit_button.setFixedSize(340, 40)
        self.quit_button.move(130, 340)
        self.quit_button.clicked.connect(self.close)

    def tool_tip(self):
        self.vote_button.setToolTip('이 버튼을 누르면 대표를 선출합니다. \n주의하세요. 되돌릴 수 없습니다.')
        self.quit_button.setToolTip('이 버튼을 누르면 프로그램을 종료합니다.')
        self.image.setToolTip('Q-factory 대표 로고')
        self.setToolTip('이곳은 QWidget!')

    def first_look(self):
        # https://doc.qt.io/qtforpython/PySide2/QtGui/QFont.html

        self.label = QLabel('QF', self)
        self.label.setFont(QFont("Helvetica", pointSize=75, weight=2))
        self.label.move(250, 150)

    def choice(self):
        s = f"{random.randint(1, 10):02d}"
        print(s)
        self.label.setText(s)
        self.label.setStyleSheet("font-weight: bold; color: red")  # 글자색 변환

    def close(self):
        return QCoreApplication.instance().quit()


app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec())
