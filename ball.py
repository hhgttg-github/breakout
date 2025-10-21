import random
import pyxel
import sprite
import screen

####====================================
#### CONSTANT

BALL_SP = 1
BALL_SIZE = 8
BALL_SPEED = 512

####====================================
#### CLASS

class Ball():
    def __init__(self):
        self.sp = sprite.Sprite(0,128,1,0,sprite.sp8Group,area=(1,1))
        self.start_ball()
        self.count = 3

    def start_ball(self):
        self.sp.x = random.randint(0,screen.WIDTH)
        self.sp.y = 128
        self.sp.dx = random.choice([-1,1]) * BALL_SPEED
        self.sp.dy = 256
    
    def lost_ball(self):
        self.count -= 1
        
    def reflect_around(self):
        if (self.sp.x<=0) and (self.sp.dx<0):
            self.sp.dx = abs(self.sp.dx)
        if (self.sp.x>=(screen.WIDTH-BALL_SIZE)) and (self.sp.dx>0):
            self.sp.dx *= -1
        if (self.sp.y<=0) and (self.sp.dy<0):
            self.sp.dy = abs(self.sp.dy)
    
    def reflect_horizontal(self):
        self.dx *= -1

    def reflect_vertical(self):
        self.dy *= -1

    def update(self):
        self.sp.update()

    def draw(self):
        self.sp.draw()