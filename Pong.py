import sys

from PyQt4 import QtGui

import Core.GameLoop
import GUI.Window

# Initialize things, run the game loop, clean up on exit

def main():
	app = QtGui.QApplication(sys.argv)
	mainWindow = GUI.Window.Window()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()