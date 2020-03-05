try:
    import sys
    from PyQt5.QtWidgets import QApplication
    from frame import Frame
    from board import GameBoard
except ModuleNotFoundError:
    print('Module not found')

from player import AIPlayer


if __name__ == '__main__':
    print('input key [gui(g) / cui(c)]:', end=' ')
    display = input()
    if display == 'g':
        app = QApplication(sys.argv)
        game = Frame()
        game.show()
        sys.exit(app.exec_())
    elif display == 'c':
        player = AIPlayer()
    else:
        print('invalid input:', display)
        print('only g, c are available')
        sys.exit()


    
