from PyQt4 import QtGui

class Player:
    'Abstract class for pong player'
        
    def __init__(self, name, paddle, color):
    # string, Paddle, QColor
        self.name = name
        self.paddle = paddle
        self.color = color
        
    def setPaddle(self, paddle):
        self.paddle = paddle
        
    def getMove(self, args):
        raise NotImplementedError("getMove not implemented")
        
if __name__ == "__main__":
    main()