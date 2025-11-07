import random
import pyxel
import sprite
import screen as sc

####====================================
#### CONSTANT

BALL_SP = 1
BALL_SIZE = 8
BALL_INIT_DIR = 6
BALL_INIT_SPEED = 256 # 1-25 の範囲。 x100でmax 256

LINE16 = {}
#### 反射テーブルでは、0,4,8,12(水平・垂直方向)が2方向。
#### ランダムに選んだら、壁などにめり込む方向となる。
#### CourseSpとしては0,4,8,11は必須だが、今回のボールの反射
#### については、水平・垂直移動は存在しないことにする？

V_REFLECT = {0:[7,8,9],1:[6,7,8],2:[5,6,7],3:[4,5,6],
             4:[3,5],5:[2,3,4],6:[1,2,3],7:[0,1,2],
             8:[15,0,1],9:[0,15,14],10:[13,14,15],
             11:[12,13,14],12:[11,13],13:[10,11,12],
             14:[9,10,11],15:[8,9,10]}
H_REFLECT = {0:[1,15],1:[14,15,0],2:[13,14,15],3:[12,13,14],
             4:[11,12,13],5:[10,11,12],6:[9,10,11],7:[8,9,10],
             8:[7,9],9:[6,7,8],10:[5,6,7],
             11:[4,5,6],12:[10,11],13:[2,3,4],
             14:[1,2,3],15:[0,1,2]}

####====================================
#### CLASS

class Ball():
    def __init__(self):
        self.sp = sprite.CourseSp(0,128,1,0,sprite.sp8Group,BALL_INIT_DIR,BALL_INIT_SPEED,area=(1,1))
        self.sp.x = random.randint(0,sc.WIDTH)
        self.sp.y = 128
        self.centerX = self.sp.x + 3
        self.centerY = self.sp.y + 3
        self.lt = (self.sp.x,self.sp.y)
        self.rt = (self.sp.x+sc.GRID_MARGIN,self.sp.y)
        self.lb = (self.sp.x,self.sp.y+sc.GRID_MARGIN)
        self.rb = (self.sp.x+sc.GRID_MARGIN,self.sp.y+sc.GRID_MARGIN)
        self.count = 3
    
    def lost_ball(self):
        self.count -= 1
        
    def reflect_around(self):
        pass

    def reflect_horizontal(self):
        reflect = random.choice(H_REFLECT[self.sp.dir])
        self.sp.set_dir(reflect)
        self.sp.speed += 100
        self.limit_speed()

    def reflect_vertical(self):
        reflect = random.choice(V_REFLECT[self.sp.dir])
        self.sp.set_dir(reflect)
        self.sp.speed += 100
        self.limit_speed()

####====================================

    def check_pushback(self):

        right_top    = sc.get_tile_pxy(self.rt[0],self.rt[1])
        right_bottom = sc.get_tile_pxy(self.rb[0],self.rb[1])
        left_top     = sc.get_tile_pxy(self.lt[0],self.lt[1])
        left_bottom  = sc.get_tile_pxy(self.lb[0],self.lb[1])
        rt = (right_top    == sc.TILE_BLOCK_L) or (right_top    == sc.TILE_BLOCK_R)
        rb = (right_bottom == sc.TILE_BLOCK_L) or (right_bottom == sc.TILE_BLOCK_R)
        lt = (left_top     == sc.TILE_BLOCK_L) or (left_top     == sc.TILE_BLOCK_R)
        lb = (left_bottom  == sc.TILE_BLOCK_L) or (left_bottom  == sc.TILE_BLOCK_R)
        
        # 3方向のうち1方向のみブロックでなければ、その方向にプッシュバック
        if not(rt) and rb and lt and lb:
            self.move_to_rt()
            return()
        elif rt and not(rb) and lt and lb:
            self.move_to_rb()
            return()
        elif rt and rb and not(lt) and lb:
            self.move_to_lt()
            return()
        elif rt and rb and lt and not(lb):
            self.move_to_lb()
            return()
        
        # 2方向のみブロックなら、水平か垂直にプッシュバック
        if not(rt) and not(rb) and lt and lb:
            self.move_to_left_edge()
            return()
        elif rt and rb and not(lt) and not(lb):
            self.move_to_right_edge()
            return()
        elif not(rt) and rb and not(lt) and lb:
            self.move_to_top_edge()
            return()
        elif rt and not(rb) and lt and not(lb):
            self.move_to_bottom_edge()
            return()

####====================================

    def move_to_rt(self):
        pass
    def move_to_rb(self):
        pass
    def move_to_lt(self):
        pass
    def move_to_lb(self):
        pass
 
    def move_to_right_edge(self):
        pass
    def move_to_left_edge(self):
        pass
    def move_to_top_edge(self):
        pass
    def move_to_bottom_edge(self):
        pass
####====================================

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
        self.centerX = self.sp.x + 3
        self.centerY = self.sp.y + 3
        self.lt = (self.sp.x,self.sp.y)
        self.rt = (self.sp.x+sc.GRID_MARGIN,self.sp.y)
        self.lb = (self.sp.x,self.sp.y+sc.GRID_MARGIN)
        self.rb = (self.sp.x+sc.GRID_MARGIN,self.sp.y+sc.GRID_MARGIN)

    def draw(self):
        self.sp.draw()