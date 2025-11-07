
import pyxel

####====================================
#### CONSTANT

WIDTH = 256
HEIGHT = 256

GRID_SIZE = 8
GRID_MARGIN = GRID_SIZE -1
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
GRID_AREA = GRID_WIDTH * GRID_HEIGHT
grid_map = [-1 for _ in range(GRID_AREA)]

def sc_xy_to_pyxel(x,y):
    return(x * GRID_SIZE ,y * GRID_SIZE)

def pixel_to_sc_xy(px,py):
    return(px // GRID_SIZE,py // GRID_SIZE)

####====================================
####
#### TILE

TILE_NONE = 0
TILE_BLOCK_L = 32
TILE_BLOCK_R = 33
TILE_BLANK = 65
TILE_SIDE_BLOCK = 66
TILE_FLOOR_BLOCK = 67

TILE_DICT = {
    (0,3) : TILE_BLOCK_L,
    (1,3) : TILE_BLOCK_R,
    (1,4) : TILE_BLANK,
    (2,4) : TILE_SIDE_BLOCK,
    (3,4) : TILE_FLOOR_BLOCK}

BLOCK_L_PX = 0
BLOCK_L_PY = 24
BLOCK_WIDTH = 16
BLOCK_HEIGHT = 8

def get_tile_pxy(x,y):
    tile = pyxel.tilemaps[0].pget(x//GRID_SIZE, y//GRID_SIZE)
    return(TILE_DICT.get(tile,TILE_NONE))

def get_tile(x,y):
    tile = pyxel.tilemaps[0].pget(x, y)
    print(f"get_tile({x},{y})={tile}",end="/ ")
    return(TILE_DICT.get(tile,TILE_NONE))

def draw_block(x,y):
    px,py = sc_xy_to_pyxel(x,y)
    pyxel.blt(px,py,0,BLOCK_L_PX,BLOCK_L_PY,BLOCK_WIDTH,BLOCK_HEIGHT)

# def left_top_border(x):
#     if (x % GRID_SIZE) == 0:
#         return(True)
#     else:
#         return(False)

# def right_bottom_border(x):
#     if (x % GRID_SIZE) == GRID_SIZE - 1:
#         return(True)
#     else:
#         return(False)

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

def bresenham(x0, y0, x1, y1):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    Input coordinates should be integers.
    The result will contain both the start and the end point.
    
    >>> from bresenham import bresenham
    >>> list(bresenham(-1, -4, 3, 2))
    [(-1, -4), (0, -3), (0, -2), (1, -1), (2, 0), (2, 1), (3, 2)]
    """
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy

def clear_field():
    pyxel.cls(7)
    pyxel.bltm(0,0,0,0,0,256,256)

def draw_init_field():
    print("draw_init_field")
    pyxel.cls(7)
    pyxel.bltm(0,0,0,256,0,256,256)
    print("drow_init_field END")