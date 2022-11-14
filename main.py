import random
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.f(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def f(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        t = random.randint(0, 200)
        qp.drawEllipse(random.randint(0, 300), random.randint(0, 300), t, t)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
