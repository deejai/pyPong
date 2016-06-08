from PyQt4 import QtGui

class Arena(QtGui.QGraphicsView):
    'A field for playing pong'

    black = QtGui.QColor(0,0,0)

    def __init__(self, width, height, bg_color=black):
        self.width = width
        self.height = height
        self.background = background
        self.gui = gui

    def setPaddles(paddle1, paddle2):
        self.paddle1 = paddle1
        self.paddle2 = paddle2

if __name__ == "__main__":
    main()