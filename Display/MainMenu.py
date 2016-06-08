from Display.Arena import Arena
from PyQt4 import QtGui

class MainMenu(QtGui.QGraphicsView):
    'The place to customize or start a pong game'

    menuItems = []

    def __init__(self):
        singlePlayerArenas[1] = Arena()
        createItem("Single Player", )

    def createItem(text, qview):
        # TODO: if text is duplicate, replace qview of that
        #       item instead of creating a new item
        menuItems.append(text, qview)