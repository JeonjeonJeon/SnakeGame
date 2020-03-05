try:
    import random
    import threading
    import time
    from board import GameBoard
except ModuleNotFoundError:
    print('Module not found')

class AIPlayer:
    def __init__(self):
        self.game = GameBoard(self)
        
        self.gameOn = True

        while self.gameOn == True:
            self.game.step()


    def goSign(self):
        direction = ['up', 'right', 'down', 'left', 'none']
        rand = random.randrange(0, 5)
        if direction[rand] != 'none':
            self.game.getInput(direction[rand])
        self.game.printMap()
        print(direction[rand], 'head:', self.game.snake[0])
        time.sleep(1)

    def closeSignal(self):
        self.gameOn = False
