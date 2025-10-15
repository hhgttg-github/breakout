import pyxel
import sprite as sp

####====================================
#### CONSTANT

PADDLE_SP = 32
PADDLE_WIDTH = 16
PADDLE_HEIGHT = 8

####====================================
#### CLASS

class Paddle():
    def __init__(self):
        self.sp = sp.Sprite(0,128,64,64,1,0,sp.sp8Group)
    def __update__(self):
        self.sp.update()

    def __draw__(self):
        self.sp.draw()