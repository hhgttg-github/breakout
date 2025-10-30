import random
import pyxel
import sprite
import screen

####====================================
#### CONSTANT

BALL_SP = 1
BALL_SIZE = 8
BALL_INIT_DIR = 6
BALL_INIT_SPEED = 10 # 1-25 の範囲。 x100でmax 256

### 16方向の座標・半径100の円で12時から時計回りに
DIR16 = [(0,-10),( 4,-9),( 7,-7),( 9,-4),
            (10, 0),( 9, 4),( 7, 7),( 4, 9),
            (0,10),(-4, 9),(-7, 7),(-9, 4),
            (-10,0),(-9,-4),(-7,-7),(-4,-9)]
LINE16 = {}
V_REFLECT = {0:[7,8,9],1:[6,7,8],2:[5,6,7],3:[4,5,6],
             4:[5,6],5:[2,3,4],6:[1,2,3],7:[0,1,2],
             8:[15,0,1],9:[0,15,14],10:[13,14,15],
             11:[12,13,14],12:[11,10],13:[10,11,12],
             14:[9,10,11],15:[8,9,10]}

def init_line16():
    """12次方向のインデックスが0, 以後、時計回りに1ずつ増加
        LINE16[DIR16[0]] で12次方向への座標軌跡が得られる"""
    id = 0 
    for d in DIR16:
        LINE16[id] = list(screen.bresenham(0,0,d[0],d[1]))
        print(f"DIR={d}, LINE={LINE16[id]}")
        id += 1

####====================================
#### CLASS

class Ball():
    def __init__(self):
        self.sp = sprite.Sprite(0,128,1,0,sprite.sp8Group,area=(1,1))
        self.dir = BALL_INIT_DIR
        self.speed = BALL_INIT_SPEED
        self.start_ball()
        self.count = 3

    def start_ball(self):
        self.sp.x = random.randint(0,screen.WIDTH)
        self.sp.y = 128
        self.set_dir_speed()

    def set_dir_speed(self):
        
        dx,dy = DIR16[self.dir]

        if dx < 0:
            self.vx = -1
        else:
            self.vx = 1
        self.sp.dx = abs(dx) * self.speed

        if dy < 0:
            self.vy = -1
        else:
            self.vy = 1
        self.sp.dy = abs(dy) * self.speed

    def course(self):
        l=LINE16[DIR16[self.dir]]
        return(list(map(lambda x:(self.sp.x + x[0], self.sp.y + x[1]), l)))
    
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