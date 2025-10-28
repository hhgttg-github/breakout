
import pyxel

####====================================
#### CONSTANT

WIDTH = 256
HEIGHT = 256

GRID_SIZE = 8
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
GRID_AREA = GRID_WIDTH * GRID_HEIGHT
grid_map = [-1 for _ in range(GRID_AREA)]

def sc_xy_to_pyxel(x,y):
    return(x * GRID_SIZE ,y * GRID_SIZE)

def pixel_to_sc_xy(px,py):
    return(px // GRID_SIZE,py // GRID_SIZE)

def left_top_border(x):
    if (x % GRID_SIZE) == 0:
        return(True)
    else:
        return(False)

def right_bottom_border(x):
    if (x % GRID_SIZE) == GRID_SIZE - 1:
        return(True)
    else:
        return(False)

####====================================
#### FONT

um10 = pyxel.Font("umplus_j10r.bdf")
um12 = pyxel.Font("umplus_j12r.bdf")

#  pyxel.text(x, y, "表示文字列", 色番号, um12)

####====================================
#### CLASS

####====================================
#### FUNCTION

def draw_score(score):
    pyxel.text(0,0,f"SCORE : {score}",7 , um12)

