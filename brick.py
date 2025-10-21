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
                if (ball.sp.dx < 0) and (ball.sp.dy < 0):
# ちょっともう少し考えてから
                    # if Bricks_Table.touch_top(ball,brck):
                    #     ball.reflect_vertical()
                    # elif Bricks_Table.touch_left(ball.brck):
                    #     ball.reflect_horizontal()

    def draw(self):
        for b in self.table:
            if b.exist:
                b.sp.draw()

####====================================

    @staticmethod

    def touch_top(ball,brick):
        x,y   = ball.sp.x, ball.sp.y
        bx,by = brick.sp.x, brick.sp.y
        w,h   = brick.sp.w, brick.sp.h
        if sprite.check_pt_in_rect(x,y,bx,by,w,h):
            if sprite.check_pt_in_rect(x+3,y,bx,by,w,h):
                return(True)
        return(False)
    
    def touch_bottom(ball,brick):
        x,y   = ball.sp.x, ball.sp.y
        bx,by = brick.sp.x, brick.sp.y
        w,h   = brick.sp.w, brick.sp.h
        if sprite.check_pt_in_rect(x,y,bx,by,w,h):
            if sprite.check_pt_in_rect(x+3,y,bx,by,w,h):
                return(True)
        return(False)


####====================================
#### VARIABLES


####====================================
#### FUNCTION

