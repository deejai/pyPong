from PyQt4 import QtGui

class Arena(QtGui.QGraphicsView):
    'A field for playing pong'

    black = QtGui.QColor(0,0,0)

    def __init__(self, width=480, height=360, bg_color=black):
        self.width = width
        self.height = height
        self.bg_color = bg_color

    def setPlayers(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

if __name__ == "__main__":
    main()