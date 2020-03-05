import copy
import math
import random
import time
import sys

from PyQt5.QtCore import Qt


class GameBoard:
    def __init__(self, parent, w, h):
        self.WIDTH = w
        self.HEIGTH = h
        self.caller = parent

        self.board_size = 15
        self.board = [[0 * self.board_size] * self.board_size] # 30 x 30 game board
        sh = math.floor(self.board_size/2)
        f = math.floor(self.board_size/3)
        self.snake = [[sh, sh]]
        self.food = [f, f]
        self.direction = 'right'
        self.mode = 'IN GAME'


    def step(self):
        add = False
        while self.mode == 'IN GAME':
            if add == True:
                self.snake.append(self.snake[len(self.snake) - 1])
                add = False
            self.movesnake()
            if self.food == self.snake[0]:
                self.food = [random.randrange(0, self.board_size), random.randrange(0, self.board_size)]
                add = True

            time.sleep(0.3)
        if self.mode == 'TERMINATE APPLICATION':
            print('application terminated')
            pass

        elif self.mode == 'GAME OVER':
            print('game over')
            for i in reversed(range(1, 4)):
                print('exit in', i, 'seconds')
                time.sleep(1)
            self.caller.closesignal()


    def movesnake(self):
        index = len(self.snake) - 1
        while index > 0:  # move body except head(snake[0])
            self.snake[index] = copy.deepcopy(self.snake[index - 1])
            index -= 1
        if self.direction == 'up':
            self.snake[0][0] -= 1
        elif self.direction == 'right':
            self.snake[0][1] += 1
        elif self.direction == 'down':
            self.snake[0][0] += 1
        elif self.direction == 'left':
            self.snake[0][1] -= 1
        if self.snake[0][0] < 0 or self.snake[0][0] >= self.board_size:
            self.mode = 'GAME OVER'
        if self.snake[0][1] < 0 or self.snake[0][1] >= self.board_size:
            self.mode = 'GAME OVER'

        i = 1
        while i < len(self.snake):
            if self.snake[0] == self.snake[i]:
                self.mode = 'GAME OVER'
            i += 1


    def render(self, qp):  # qp: Painter
        if self.mode == 'IN GAME':
            qp.setcolor(Qt.blue)
        else:
            qp.setcolor(Qt.darkRed)
        len = self.WIDTH / self.board_size
        for i in self.snake:
            qp.fillrect(i[1]*len + 1, i[0]*len + 1, len, len)

        if self.mode == 'GAME OVER':
            qp.setcolor(Qt.darkYellow)
            qp.fillrect(self.snake[0][1]*len + 1, self.snake[0][0]*len + 1, len, len)

        qp.setcolor(Qt.red)
        qp.fillellipse(self.food[1]*len+1, self.food[0]*len+1, len, len)


    def drawBox(self, qp):
        pass

    def getinput(self, key):
        if key == 'left' and self.direction != 'right':
            self.direction = 'left'
        elif key == 'right' and self.direction != 'left':
            self.direction = 'right'
        elif key == 'down' and self.direction != 'up':
            self.direction = 'down'
        elif key == 'up' and self.direction != 'down':
            self.direction = 'up'

    def keyReleaseEvent(self, QKeyEvent):
        pass

    def close(self):
        self.mode = 'TERMINATE APPLICATION'



