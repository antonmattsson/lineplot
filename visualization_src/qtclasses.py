from lineplot import *

from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QLabel


class GridLine(QWidget):

    def __init__(self,start,end,parent=None):
        super().__init__(parent)
        self.start = start
        self.end = end
        self.setGeometry(0,0, 1000,700)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        pen = QPen(Qt.lightGray)
        painter.setPen(pen)
        painter.drawLine(self.start.x,self.start.y,self.end.x,self.end.y)
        painter.end()


class Line(QWidget):

    def __init__(self, start, end, width=2, color=(0,0,0), parent=None):
        super().__init__(parent)
        self.start = start
        self.end = end
        self.width = width
        self.color = color
        self.setGeometry(0,0, parent.w, parent.h)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor(self.color[0],self.color[1],self.color[2]))
        pen.setWidth(self.width)
        painter.setPen(pen)
        painter.drawLine(self.start.x,self.start.y,self.end.x,self.end.y)


class PlotBackGround(QWidget):

    def __init__(self,x, y, w, h, parent = None):
        super().__init__(parent)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        self.setAutoFillBackground(True)
        self.setGeometry(x,y,w,h)
        self.show()


class VerticalLabel(QLabel):

    def __init__(self, *args):
        QLabel.__init__(self, *args)

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        painter = QPainter (self)
        painter.translate(0, self.height()-1)
        painter.rotate(-90)
        self.setGeometry(self.x(), self.y(), self.height(), self.width())
        QLabel.render(self, painter)

    def minimumSizeHint(self):
        size = QLabel.minimumSizeHint(self)
        return QSize(size.height(), size.width())

    def sizeHint(self):
        size = QLabel.sizeHint(self)
        return QSize(size.height(), size.width())
