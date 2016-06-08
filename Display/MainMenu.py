from Display.Arena import Arena
from PyQt4 import QtGui

class MainMenu(QtGui.QGraphicsView):
    'The place to customize or start a pong game'

    menuItems = []

    def __init__(self):
        spArenas = []
        spArenas.append(Arena())
        
if __name__ == "__main__":
    main()