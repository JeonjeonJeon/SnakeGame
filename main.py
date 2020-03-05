import sys
from PyQt5.QtWidgets import QApplication
from frame import Frame

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Frame()
    game.show()
    sys.exit(app.exec_())