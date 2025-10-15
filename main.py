import pyxel
import sprite as sp
import ball

####====================================
#### CONSTANT

SCREEN_HEIGHT = 256
SCREEN_WIDTH = 256

####====================================
#### CLASS

class Game:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT,fps=60)
        pyxel.load("breakout.pyxres")
        self.ball = ball.Ball()
        self.ball.sp.dx = 32
        pyxel.run(self.update,self.draw)

    def update(self):
        self.ball.update()
        print(f"x={self.ball.sp.x}")
        print(f"tx={self.ball.sp.tx}")
        print(f"dx={self.ball.sp.dx}")

    def draw(self):
        pyxel.cls(0)
        self.ball.draw()
        pyxel.flip()
        
if __name__=="__main__":
    Game()
    