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
        self.game = GameBoard(self)
        self.gameOn = True

        self.t1 = threading.Thread(target=self.game.step)
        self.t1.start()

    def paintEvent(self, e):
        qp = Painter(self)
        self.drawgrid(qp)
        self.game.render(qp)
        qp.end()
        self.update()
        time.sleep(0.01)
        if self.gameOn == False:
            while self.t1.is_alive() == True:
                print('unable to close window: thread is alive')
                time.sleep(0.5)
            self.close()
            self.deleteLater()

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

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('snake game')
        self.setFixedSize(self.rect().size())
        self.setStyleSheet('background-color:white')
        self.setAttribute(Qt.WA_DeleteOnClose)

    def keyPressEvent(self, QKeyEvent):
        key = QKeyEvent.key()
        if key == Qt.Key_Left:
            self.game.getInput('left')
        elif key == Qt.Key_Right:
            self.game.getInput('right')
        elif key == Qt.Key_Down:
            self.game.getInput('down')
        elif key == Qt.Key_Up:
            self.game.getInput('up')


    def closeEvent(self, QCloseEvent):
        self.game.close()

    def closeSignal(self):
        self.gameOn = False

    def goSign(self):
        time.sleep(0.5)
