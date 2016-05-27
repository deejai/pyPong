import Core.Paddle

class Player:
	'A human pong player'

	def __init__(name, color):
		this.paddle = Core.Paddle.Paddle()

		this.name = name
		this.color = color