import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.flag = False

    def initUI(self):
        self.pushButton.clicked.connect(self.drawf)

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setBrush(QColor(255, 255, 0))
            self.draw()
            self.qp.end()

    def drawf(self):
        self.flag = True
        self.update()

    def draw(self):
        krug = randint(1, 300)
        self.qp.drawEllipse(randint(0, 700), randint(30, 700), krug, krug)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
