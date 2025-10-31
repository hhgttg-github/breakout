import random
import pyxel
import sprite
import screen

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
        self.sp.x = random.randint(0,screen.WIDTH)
        self.sp.y = 128
        self.centerX = sp.x + 3
        self.centerY = sp.y + 3
        self.count = 3
        self.sp.set_dir()
    
    def lost_ball(self):
        self.count -= 1
        
    def reflect_around(self):
        pass

    def reflect_horizontal(self):
        self.sp.vx *= -1
        self.sp.dy += random.choice([-8,8,12])
        self.sp.dx += random.choice([-12,12])
        self.limit_speed()

    def reflect_vertical(self):
        self.sp.dir = random.choice(V_REFLECT[self.sp.dir])
        self.sp.set_dir()

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
        self.centerX = self.sp.x + 3
        self.centerY = self.sp.y + 3


    def draw(self):
        self.sp.draw()