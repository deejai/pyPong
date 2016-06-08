from Display import MainMenu

from PyQt4 import QtGui

class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 480, 360)
        self.setWindowTitle("Davepong")
        # TODO: self.setWindowIcon(ICON_FILE_PATH)
        
        # self.scene = Display.MainMenu()

    def setView(self, qview):
        self.show()
    
if __name__ == "__main__":
    main()