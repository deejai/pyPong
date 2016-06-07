from PyQt4 import QtGui

class Arena(QtGui.QGraphicsView):
    'A field for playing pong'

    black = QtGui.QColor.black()

    def __init__(self, width, height, bg_color=black, bg_image=0, fg_image=0):
        self.width = width
        self.height = height
        self.background = background
        self.gui = gui

    def render():
        pass
        #TODO: draw a thing
