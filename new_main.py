import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush

from random import randint
from UI import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.draw_circles)
        self.do_paint = False

    def draw_circles(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def draw(self, qp):
        for i in range(randint(1, 5)):
            qp.setBrush(QBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255))))
            x, y, size = randint(10, 440), randint(10, 350), randint(10, 100)
            qp.drawEllipse(x - size // 2, y - size // 2, x + size // 2, y + size // 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
