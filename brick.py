import pyxel
import sprite
import screen

####====================================
#### CONSTANT

SP_BRICK = 34
BRICK_WIDTH = 16
BRICK_HEIGHT = 8

BRICKS_COLUM = 16
BRICKS_ROW = 5

BRICKS_TOP = 24

####------------------------------------
#### ブロック配置用配列

C_WIDTH = 16
C_HEIGHT = 5
C_TABLE = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
           [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
           [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
           [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
           [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0]]

# C_TABLE = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
#            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
#            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
#            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
#            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
####====================================
#### FUNCTION

def to_1d(x,y):
    return(x + y * screen.SC_WIDTH)

def to_2d(i):
    y,x = divmod(i,screen.SC_WIDTH)
    return(x,y)

####===========]=========================
#### CLASS

class Brick():
    def __init__(self):
        self.id = 0
        self.sp = sprite.Sprite(0,0,SP_BRICK,0,sprite.sp8Group,area=(2,1))
        self.exist = True

    def erase(self):
        self.exist = False

    def update(self):
        pass

    def draw(self):
        self.sp.draw()

####====================================

class Bricks_Table():

    def __init__(self):
        self.num_bricks =0
        for l in C_TABLE:
            self.num_bricks += l.count(1)
        self.table = [Brick() for _ in range(self.num_bricks)]

        x = 0
        y = 0
        i = 0
        for l in C_TABLE:
            for c in l:
                print(f"x,y={x},{y}")
                print(f"c = {c}")
                if c == 1:
                    self.table[i].sp.x = x * BRICK_WIDTH
                    self.table[i].sp.y = y * BRICK_HEIGHT
                    i += 1
                x += 1
            x = 0
            y += 1
            

####        ???????????????????????/

        # i = 0
        # for y in range(BRICKS_ROW):
        #     for x in range(BRICKS_COLUM):
        #         self.table[i].sp.x = BRICKS_LEFT + x*BRICK_WIDTH
        #         self.table[i].sp.y = BRICKS_TOP + y*BRICK_HEIGHT
        #         i += 1
    
    def update(self,ball):
        mbr_list = []
        for brck in self.table:
            if brck.exist:
                if sprite.collision(brck.sp,ball.sp):
                    list.append((brck.sp.x,brck.sp.y,brck.sp.w,brck.sp.h))
        mbr = sprite.mbr(mbr_list)
        overlap_x = sprite.overlap(mbr[0],mbr[2],ball.sp.x,ball.sp.w)
        overlap_y = sprite.overlap(mbr[1],mbr[3],ball.sp.y,ball.sp.h)
        x_mv,y_mv = sprite.pushback_rect(mbr[0],mbr[1],mbr[2],mbr[3],ball.sp.x,ball.sp.y,ball.sp.w,ball.sp.h)
        ball.move_xy(x_mv,y_mv) #計算後、実際の押し戻しを行う。
        
        for brck in mbr_list:
            brck.erase()
        if overlap_x < overlap_y:
            ball.reflect_horizontal()
        elif overlap_x > overlap_y:
            ball.reflect_vertical()

        else:
            ball.reflect_horizontal()
            ball.reflect_vertical()

                    # overlap_x = sprite.overlap(brck.sp.x,brck.sp.w,ball.sp.x,ball.sp.w)
                    # overlap_y = sprite.overlap(brck.sp.y,brck.sp.h,ball.sp.y,ball.sp.h)
                    # sprite.pushback(brck.sp,ball.sp)

                    # if overlap_x < overlap_y:
                    #     brck.erase()
                    #     ball.reflect_horizontal()
                    #     break
                    # elif overlap_x > overlap_y:
                    #     brck.erase()
                    #     ball.reflect_vertical()
                    #     break
                    # else:
                    #     brck.erase()
                    #     ball.reflect_horizontal()
                    #     ball.reflect_vertical()
                    #     break

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

