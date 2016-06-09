from Control.Player import Player

class Human(Player):
    'A human pong player'

    def __init__(self, name, paddle, color):
        super(Human, self).__init__(name, paddle, color)

    def getMove(self, upPressed, downPressed):
        if( upPressed ):
            return 1 if not downPressed else 0
        elif( downPressed ):
            return -1 if not upPressed else 0
        else:
            return 0