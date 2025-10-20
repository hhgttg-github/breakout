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
        self.sp = sprite.Sprite(0,128,1,0,sprite.sp8Group)
        self.start_ball()
        self.count = 3

    def start_ball(self):
        self.sp.x = random.randint(0,screen.WIDTH)
        self.sp.y = 128
        self.sp.dx = random.choice([-1,1]) * BALL_SPEED
        self.sp.dy = 256
    
    def lost_ball(self):
        self.count -= 1
        
    def update(self):
        self.sp.update()

    def draw(self):
        self.sp.draw()