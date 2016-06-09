from Display import MainMenu

from PyQt4 import QtGui, QtCore

class Window(QtGui.QGraphicsView, QtCore.QObject):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setFixedSize(480, 360)
        self.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setWindowTitle("Davepong")

        # TODO: self.setWindowIcon(ICON_FILE_PATH)
        
        # self.scene = Display.MainMenu()

    def setView(self, qview):
        self.show()