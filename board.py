try:
    import copy
    import math
    import random
    import time
    import sys
    from PyQt5.QtCore import Qt
except ModuleNotFoundError:
    print('Module Not Found')


class GameBoard:
    def __init__(self, parent):
        self.caller = parent
        try:
            self.WIDTH = self.caller.rect().width()
            self.HEIGTH = self.caller.rect().height()
        except AttributeError:
            pass

        self.board_size = 15
        sh = math.floor(self.board_size/2)
        f = math.floor(self.board_size/3)
        self.snake = [[sh, sh]]
        self.food = [f, f]
        self.direction = 'right'
        self.mode = 'IN GAME'


    def step(self):
        add = False
        while self.mode == 'IN GAME':
            bs = self.board_size
            if add == True:
                self.snake.append(self.snake[len(self.snake) - 1])
                add = False
            self.movesnake()
            if self.food == self.snake[0]:
                self.food = [self.r(0, bs), self.r(0, bs)]
                add = True

            self.caller.goSign()

        # check if application ended
        if self.mode == 'TERMINATE APPLICATION':
            print('application terminated')
            pass

        elif self.mode == 'GAME OVER':
            print('game over')
            for i in reversed(range(1, 4)):
                print('exit in', i, 'seconds')
                time.sleep(1)
            print('send close signal')
            self.caller.closeSignal()
            print('close signal complete')
        print('end of step func')


    def movesnake(self):
        bs = self.board_size
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
        if self.snake[0][0] < 0 or self.snake[0][0] >= bs:
            self.mode = 'GAME OVER'
        if self.snake[0][1] < 0 or self.snake[0][1] >= bs:
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


    def printMap(self):
        if self.mode != 'IN GAME':
            print('game over: unable to draw map')
            return
        bs = self.board_size
        board = [[0 for i in range(bs)]for j in range(bs)]
        for i in self.snake:
            board[i[0]][i[1]] = 1
        board[self.food[0]][self.food[1]] = 2

        print()
        for i in range(bs):
            print((i+1)%10, end='')
        print()
        for i in range(bs):
            print('-', end='')
        print()

        cnt = 1
        for i in board:
            for j in i:
                if j == 0:
                    print(' ', end='')
                elif j == 1:
                    print('o', end='')
                elif j == 2:
                    print('x', end='')
            print('|', cnt)
            cnt += 1
        for i in range(bs):
            print('-', end='')
        print() 


    def drawBox(self, qp):
        pass

    def getInput(self, key):
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

    def r(self, x, y):
        return random.randrange(x, y)


