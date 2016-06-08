from PyQt4 import QtGui

class Paddle(QtGui.QGraphicsRectItem):
    'A pong paddle'

    def __init__(self, length, color, speed):
        super(Paddle, self).__init__()

        self.speed = speed
        self.length = length
        self.width = length/6
        self.color = color

    def setSpeed(speed):
        self.speed = speed
        
if __name__ == "__main__":
    main()