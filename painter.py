from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QRect


class Painter(QPainter):
    def __init__(self, qwidget):
        super().__init__()
        self.begin(qwidget)
        self.color = Qt.black

    # draw rect
    def drawrect(self, *args):
        if len(args) == 1:
            self.drawrect_RECT_TYPE(args[0])
        else:
            self.drawrect_INT_TYPE(args[0], args[1], args[2], args[3])
    def drawrect_RECT_TYPE(self, rect):
        self.setPen(self.color)
        self.drawRect(rect)
    def drawrect_INT_TYPE(self, x, y, width, height):
        self.setPen(self.color)
        self.drawRect(QRect(x, y, width, height))
    # fill rect
    def fillrect(self, *args):
        if len(args) == 1:
            self.fillrect_RECT_TYPE(args[0])
        else:
            self.fillrect_INT_TYPE(args[0], args[1], args[2], args[3])
    def fillrect_RECT_TYPE(self, rect):
        self.fillRect(rect, self.color)
    def fillrect_INT_TYPE(self, x, y, width, height):
        self.fillRect(QRect(x, y, width, height), self.color)


    # draw line
    def drawline(self, *args):
        if len(args) == 1:
            self.drawline_LINE_TYPE(args[0])
        else:
            self.drawline_INT_TYPE(args[0], args[1], args[2], args[3])
    def drawline_LINE_TYPE(self, line):
        self.setPen(self.color)
        self.drawLine(line)
    def drawline_INT_TYPE(self, x1, y1, x2, y2):
        self.setPen(self.color)
        self.drawLine(x1, y1, x2, y2)


    # draw string
    def drawstring(self, x, y, str):
        self.setPen(self.color)
        self.drawText(QRect(x, y, 7*len(str), 7*len(str)), Qt.AlignLeft | Qt.AlignTop, str)


    # draw ellipse
    def drawellipse(self, *args):
        self.setPen(self.color)
        if len(args) == 1:
            self.drawellipse_ELLIPSE_TYPE(args[0])
        else:
            self.drawellipse_INT_TYPE(args[0], args[1], args[2], args[3])
    def drawellipse_ELLIPSE_TYPE(self, el):
        self.drawEllipse(el)
    def drawellipse_INT_TYPE(self, x, y, width, height):
        self.drawEllipse(QRect(x, y, width, height))
    # fill ellipse
    def fillellipse(self, *args):
        self.setPen(self.color)
        if len(args) == 1:
            self.fillellipse_ELLIPSE_TYPE(args[0])
        else:
            self.fillellipse_INT_TYPE(args[0], args[1], args[2], args[3])
    def fillellipse_ELLIPSE_TYPE(self, el):
        self.setBrush(self.color)
        self.drawEllipse(el)
    def fillellipse_INT_TYPE(self, x, y, width, height):
        self.setBrush(self.color)
        self.drawEllipse(QRect(x, y, width, height))



    def setcolor(self, c):
        self.color = c
