
import pyxel

####====================================
#### CONSTANT

WIDTH = 256
HEIGHT = 256

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

