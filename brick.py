import random
import pyxel
import sprite
import screen as sc

import time

####====================================
#### CONSTANT

####====================================
#### FUNCTION

def pt_in_rect(x,y,r): # r=(x,y,w,h)
    if (x>=r[0]) and (x<=r[0]+r[2]) and (y>=r[1]) and (y<=r[1]+r[3]):
        return(True)
    else:
        return(False)
    
# def to_1d(x,y):
#     return(x + y * sc.GRID_WIDTH)

# def to_2d(i):
#     y,x = divmod(i,sc.GRID_WIDTH)
#     return(x,y)

####===========]=========================
#### CLASS

class Bricks_Table():

    def __init__(self):
        self.num_bricks =0
        self.table = []
        self.rect = []
        self.tm_x = 32
        self.tm_y = 0
        self.setup()

    def setup(self):
        sc.draw_init_field()
        print("sart setup")
        for y in range(sc.GRID_HEIGHT):
            for x in range(sc.GRID_WIDTH):
                if sc.get_tile(x+self.tm_x,y+self.tm_y) == sc.TILE_BLOCK_L:
                    self.table.append((x,y))
                    self.rect.append((x*sc.GRID_WIDTH,y*sc.GRID_HEIGHT,sc.GRID_SIZE*2,sc.GRID_HEIGHT))
                    self.num_bricks += 1
        print(f"number = {self.num_bricks}")
    
    def find_hit(self,x,y):
        """点(x,y)を含むブロックがあればindexを返す。
           なければFalse"""
        for r in self.rect:
            if pt_in_rect(x,y,r):
                return(self.rect.index(r))
            else:
                return(False)

    def erase_brick(self,i):
        x,y = self.table[i]
        del(self.table[i])
        del(self.rect[i])


    def update(self,ball):
        pass

    def draw(self):
        pass
#        sc.clear_field()
#        for i in self.table:
#           sc.draw_block(i.x,i.y)


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

