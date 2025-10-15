import pyxel
import sprite as sp

####====================================
#### CONSTANT

BALL_SP = 1
BALL_SIZE = 8

####====================================
#### CLASS

class Ball():
    def __init__(self):
        sp = sp.Sprite(0,128,64,64,1,0,sp.sp8Group)
    def __update__(self):
        self.sp.update()

    def __draw__(self):
        self.sp.draw()