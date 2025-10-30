
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
