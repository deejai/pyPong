from PyQt4 import QtGui

class Ball(QtGui.QGraphicsEllipseItem):
	'A bouncy pong ball'

	def __init__(self, radius, xpos=0, ypos=0):
		super(Ball, self).__init__()

		self.radius = radius
		self.vel = [0, 0]
		self.pos = [xpos, ypos]

	def jumpTo(xpos, ypos):
		self.position = [xpos, ypos]

	def setVelocity(xvel, yvel):
		self.vel = [xvel, yvel]

	def render():
		#TODO draw a thing