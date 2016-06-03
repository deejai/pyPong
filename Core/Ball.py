class Ball:
	'A bouncy pong ball'

	def __init__(self):
		self.xposition = 0
		self.yposition = 0
		self.xvelocity = 0
		self.yvelocity = 0

	def jumpTo(xposition, yposition):
		self.xposition = xposition
		self.yposition = yposition

	def setVelocity(xvelocity, yvelocity):
		self.xvelocity = xvelocity
		self.yvelocity = yvelocity

	def render():
		#TODO draw a thing