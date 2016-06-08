from Control.Player import Player

class AI(Player):
    'A virtual pong player'

    def __init__(self, name, paddle, color):
        super(AI, self).__init__(name, paddle, color)

    def getMove(self, oppPos, opptVel, ballPos, ballVel):
        # TODO: implement AI
        return 1 #up
        # return -1 #down
        # return 0 #stay
        
if __name__ == "__main__":
    main()