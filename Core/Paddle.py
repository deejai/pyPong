class Paddle:
    'A pong paddle'

    def __init__(xstart, ystart, length, thickness, color):
        # Place the paddle and set the speed
        this.xposition = xstart
        this.yposition = ystart
        this.xspeed = 0
        this.yspeed = 0

        # Give the paddle its shape and color
        this.length = length
        this.thickness = thickness
        this.color = color

    def jumpTo(xposition, yposition):
        this.xposition = xposition
        this.yposition = yposition

    def setSpeed(xspeed, yspeed):
        this.xspeed = xspeed
        this.yspeed = yspeed

    def render():
        # TODO: paint a thing