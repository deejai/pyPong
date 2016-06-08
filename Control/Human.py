from Control.Player import Player

class Human(Player):
    'A human pong player'

    def __init__(self):
        super(AI, self).__init__()

    def getMove(self, upPressed, downPressed):
        if( upPressed ):
            return 1 if !downPressed else 0
        else if( downPressed ):
            return -1 if !upPressed else 0
        else:
            return 0
            
if __name__ == "__main__":
    main()