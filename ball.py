import random
import pyxel
import sprite
import screen

####====================================
#### CONSTANT

BALL_SP = 1
BALL_SIZE = 8
BALL_SPEED = 128

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
        self.sp.dx = BALL_SPEED
        self.sp.dy = BALL_SPEED
        self.vx = random.choice([-1,1])
        self.vy = 1
    
    def lost_ball(self):
        self.count -= 1
        
    def reflect_around(self):
        if (self.sp.x<=0) and (self.sp.vx<0):
            self.reflect_horizontal()
        if (self.sp.x>=(screen.WIDTH-BALL_SIZE)) and (self.sp.vx>0):
            self.reflect_horizontal()
        if (self.sp.y<=0) and (self.sp.vy<0):
            self.reflect_vertical()
        if (self.sp.y>220) and (self.sp.vy>0):
            self.reflect_vertical()

    def reflect_horizontal(self):
        self.sp.vx *= -1
        self.sp.dy += random.choice([-8,8,12])
        self.sp.dx += random.choice([-12,12])
        self.limit_speed()

    def reflect_vertical(self):
        self.sp.vy *= -1
        self.sp.dx += random.choice([-8,8,12])
        self.sp.dy += random.choice([-12,12])
        self.limit_speed()

####====================================

    def left_border(self):
        if screen.left_top_border(self.sp.x):
            return(True)
        else:
            return(False)

    def left_border(self):
        if screen.left_top_border(self.sp.x):
            return(True)
        else:
            return(False)

    def top_border(self):
        if screen.left_top_border(self.sp.y):
            return(True)
        else:
            return(False)

    def right_border(self):
        if screen.left_top_border(self.sp.x + 7):
            return(True)
        else:
            return(False)

    def bottom_border(self):
        if screen.left_top_border(self.sp.y + 7):
            return(True)
        else:
            return(False)
####====================================

    def limit_speed(self):
        if self.sp.dx < 512:
            self.sp.dx = 512
        if self.sp.dx > 2048:
            self.sp.dx = 2048
        if self.sp.dy < 512:
            self.sp.dy = 512
        if self.sp.dy > 2048:
            self.sp.dy = 2048
####====================================

    def update(self):
        self.sp.update()
        self.limit_speed()

    def draw(self):
        self.sp.draw()