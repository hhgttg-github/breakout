import pyxel
import sprite
import screen

####====================================
#### CONSTANT

PADDLE_SP = 32
PADDLE_WIDTH = 16
PADDLE_HEIGHT = 8

####====================================
#### CLASS

class Paddle():

    def __init__(self):
        self.sp = sprite.Sprite(120,240,32,0,sprite.sp8Group,area=(2,1))

    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.sp.dx = -512
        elif pyxel.btn(pyxel.KEY_D):
            self.sp.dx = 512
        elif (pyxel.btnr(pyxel.KEY_A)) or (pyxel.btnr(pyxel.KEY_D)):
            self.sp.dx = 0

        self.sp.update()

        print(f"x={self.sp.x}")
        if self.sp.x <=0:
            self.sp.x = 0
        if self.sp.x >= screen.WIDTH - PADDLE_WIDTH:
            self.sp.x = screen.WIDTH - PADDLE_WIDTH

    def draw(self):
        self.sp.draw()