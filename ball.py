import pyxel
import sprite

####====================================
#### CONSTANT

BALL_SP = 1
BALL_SIZE = 8

####====================================
#### CLASS

class Ball():
    def __init__(self):
        self.sp = sprite.Sprite(0,128,512,512,64,1,0,sprite.sp8Group)

    def update(self):
        self.sp.update()

    def draw(self):
        self.sp.draw()