import sys

from PyQt4 import QtGui

from Core.GameLoop    import GameLoop
from Core.Paddle      import Paddle
from Display.Arena    import Arena
from Display.Window   import Window
from Display.MainMenu import MainMenu
from Control.Player   import Player
from Control.AI       import AI
from Control.Human    import Human

# Initialize things, run the game loop, clean up on exit

white = QtGui.QColor(255, 255, 255)

def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    # mainMenu = MainMenu()
    # window.setView(mainMenu)
    
    paddle1 = Paddle(10, white, 1)
    paddle2 = Paddle(10, white, 1)
    
    player1 = Human("Charlie", paddle1, white)
    player2 = AI("Doug", paddle2, white)
        
    testArena = Arena()
    testArena.setPlayers(player1, player2)
    window.setView(testArena)
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()