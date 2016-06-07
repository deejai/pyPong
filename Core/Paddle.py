from PyQt4 import QtGui

class Paddle(QtGui.QGraphicsRectItem):
    'A pong paddle'

    def __init__(self, length, color):
        super(Paddle, self).__init__()

        this.speed = 1
        this.length = length
        this.width = length/6
        this.color = color

    def setSpeed(speed):
        this.speed = speed

    def render(display):
        # TODO: draw a thing