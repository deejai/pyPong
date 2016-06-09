from PyQt4 import QtGui

class Arena():
    'A field for playing pong'

    black = QtGui.QColor(0,0,0)

    def __init__(self, view, bg_color=black):
        

    def setPlayers(self, player1, player2):
        self.player1 = player1
        self.player2 = player2