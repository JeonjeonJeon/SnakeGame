import os
import threading
import sys
import time

from PyQt5.QtWidgets import QWidget

from board import GameBoard
from painter import Painter
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QColor
import random


class Frame(QWidget):
    def __init__(self):
        super().__init__()
        # self.pen = QPen(Qt.black)
        self.initUI()
        self.WIDTH = self.rect().width()
        self.HEIGHT = self.rect().height()
        self.game = GameBoard(self, self.WIDTH, self.HEIGHT)

        t1 = threading.Thread(target=self.game.step)
        t1.start()

    def paintEvent(self, e):
        qp = Painter(self)
        self.drawgrid(qp)
        self.game.render(qp)
        qp.end()
        self.update()
        time.sleep(0.01)

    def drawgrid(self, qp):
        qp.setcolor(Qt.gray)
        leng = self.WIDTH / self.game.board_size
        for i in range(self.game.board_size):
            qp.drawline(i*leng, 0, i*leng, self.WIDTH)
            qp.drawline(0, i * leng, self.WIDTH, i * leng)
        qp.setcolor(Qt.black)
        qp.drawstring(5, 5, 'location: '+str(self.game.snake[0]))
        qp.drawstring(5, 20, 'food: '+str(self.game.food))
        qp.drawstring(5, 35, 'len: '+str(len(self.game.snake)))


    def drawBox(self, qp):
        pass

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('snake game')
        self.setFixedSize(self.rect().size())
        self.setStyleSheet('background-color:white')
        self.setAttribute(Qt.WA_DeleteOnClose)

    def keyPressEvent(self, QKeyEvent):
        key = QKeyEvent.key()
        if key == Qt.Key_Left:
            self.game.getinput('left')
        elif key == Qt.Key_Right:
            self.game.getinput('right')
        elif key == Qt.Key_Down:
            self.game.getinput('down')
        elif key == Qt.Key_Up:
            self.game.getinput('up')

    def keyReleaseEvent(self, QKeyEvent):
        pass

    def closeEvent(self, QCloseEvent):
        self.game.close()

    def closesignal(self):
        self.close()
        self.deleteLater()
