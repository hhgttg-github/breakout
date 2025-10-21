import pyxel
import sprite

####====================================
#### CONSTANT

SP_BRICK = 34
BRICK_WIDTH = 16
BRICK_HEIGHT = 8

BRICKS_COLUM = 12
BRICKS_ROW = 5
NUM_BIRCKS = BRICKS_ROW * BRICKS_COLUM

BRICKS_TOP = 32
BRICKS_LEFT = 32

####====================================
#### CLASS

class Brick():
    def __init__(self):
        self.sp = sprite.Sprite(0,0,SP_BRICK,0,sprite.sp8Group,area=(2,1))
        self.exist = True

    def __update__(self):
        pass

    def __draw__(self):
        self.sp.draw()

####====================================

class Bricks_Table():
    def __init__(self):
        self.table = [Brick() for _ in range(NUM_BIRCKS)]
        i = 0
        for y in range(BRICKS_ROW):
            for x in range(BRICKS_COLUM):
                self.table[i].sp.x = BRICKS_LEFT + x*BRICK_WIDTH
                self.table[i].sp.y = BRICKS_TOP + y*BRICK_HEIGHT
                i += 1
    
    def update(self,ball):
        for brck in self.table:
            if sprite.collision(brck.sp,ball.sp):
                print(f"BRICK COLLISION = {brck}")

    def draw(self):
        for b in self.table:
            if b.exist:
                b.sp.draw()

####====================================
#### VARIABLES


####====================================
#### FUNCTION

def collision_ball(t,b):
    result = list(filter (lambda x:sprite.collision(b.sp,x.sp),t))