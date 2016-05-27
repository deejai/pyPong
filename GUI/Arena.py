def test():
	print("Arena!")

class Arena:
	'A field for playing pong'

	def __init__(self, width, height, background, gui):
		self.width = width
		self.height = height
		self.background = background
		self.gui = gui
