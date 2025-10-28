import random
import pyxel
import sprite
import screen

####====================================
#### CONSTANT

SP_BRICK = 34
BRICK_WIDTH = 16
BRICK_HEIGHT = 8

####------------------------------------
#### ブロック配置用配列

C_WIDTH = 16
C_HEIGHT = 5
C_TABLE = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,34,35,34,35,34,35,34,35,34,35,34,35,34,35,34,35,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,34,35,34,35,34,35,34,35,34,35,34,35,34,35,34,35,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,34,35,34,35,34,35,34,35,34,35,34,35,34,35,34,35,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,34,35,34,35,34,35,34,35,34,35,34,35,34,35,34,35,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,34,35,34,35,34,35,34,35,34,35,34,35,34,35,34,35,-1,-1,-1,-1,-1,-1,-1,-1]]

####====================================
#### FUNCTION

def to_1d(x,y):
    return(x + y * screen.GRID_WIDTH)

def to_2d(i):
    y,x = divmod(i,screen.GRID_WIDTH)
    return(x,y)

####===========]=========================
#### CLASS

class Brick():
    def __init__(self,id,x,y):
        self.id = id
        self.sp = sprite.Sprite(x,y,SP_BRICK,0,sprite.sp8Group,area=(2,1))
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
        self.id_first = 1
        self.id_last = 1
        self.table = []
        brick_index = 0
        i = 0
        for l in C_TABLE:
            for b in l:
                if b==34:
                    screen.grid_map[i] = brick_index
                    sc_x,sc_y = to_2d(i)
                    x,y = screen.sc_xy_to_pyxel(sc_x,sc_y)
                    self.table.append(Brick(brick_index, x, y))
                elif b==35:
                    screen.grid_map[i] = brick_index
                    brick_index += 1
                    self.num_bricks += 1
                else:
                    screen.grid_map[i] = -1
                i += 1
        i = 0
        for _ in screen.grid_map:
            print(f"{i}:{screen.grid_map[i]}")
            i += 1


    def update(self,ball):
        sc_x,sc_y = screen.pixel_to_sc_xy(ball.sp.x,ball.sp.y)
        print(f"ball_x,ball_y = {ball.sp.x},{ball.sp.y}")
        print(f"sc_x,sc_y = {sc_x},{sc_y}")
        print(f"to_1d = {to_1d(sc_x,sc_y)}")
        if ball.left_border() and (ball.sp.vx < 0):
            check_x = sc_x - 1
            if screen.grid_map[to_1d(check_x,sc_y)] != -1:
                ball.reflect_horizontal()
        if ball.top_border() and (ball.sp.vy < 0):
            check_y = sc_y - 1
            if screen.grid_map[to_1d(sc_x,check_y)] != -1:
                ball.reflect_vertical()
        if ball.right_border() and (ball.sp.vx > 0):
            check_x = sc_x + 1
            if screen.grid_map[to_1d(check_x,sc_y)] != -1:
                ball.reflect_horizontal()
        if ball.bottom_border() and (ball.sp.vy > 0):
            check_y = sc_y + 1
            if screen.grid_map[to_1d(sc_x,check_y)] != -1:
                ball.reflect_horizontal()
    #     brck_list = []
    #     sp_list   = sprite.SpList()
    #     for brck in self.table:
    #         if brck.exist:
    #             if sprite.collision(brck.sp,ball.sp):
    #                 brck_list.append(brck)
    #                 sp_list.append(brck.sp)
    #     if brck_list != []:
    #         mbr = sp_list.mbr()
    #         overlap_x = sprite.overlap(mbr[0],mbr[2],ball.sp.x,ball.sp.w)
    #         overlap_y = sprite.overlap(mbr[1],mbr[3],ball.sp.y,ball.sp.h)
    #         x_mv,y_mv = sprite.pushback_rect(mbr[0],mbr[1],mbr[2],mbr[3],ball.sp.x,ball.sp.y,ball.sp.w,ball.sp.h)
    #         ball.sp.move_xy(x_mv,y_mv) #計算後、実際の押し戻しを行う。
        
    #         erase_brck = random.choice(brck_list)
    #         erase_brck.erase()
    #         if overlap_x < overlap_y:
    #             ball.reflect_horizontal()
    #         elif overlap_x > overlap_y:
    #             ball.reflect_vertical()
    #         else:
    #             ball.reflect_horizontal()
    #             ball.reflect_vertical()

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

