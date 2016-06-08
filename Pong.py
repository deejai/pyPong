import sys

from PyQt4 import QtGui

from Core.GameLoop import GameLoop
from Display.Window import Window

# Initialize things, run the game loop, clean up on exit

def main():
	app = QtGui.QApplication(sys.argv)
	mainWindow = Window()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()