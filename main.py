import pyxel
import sprite as sp
import ball
import paddle

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
        self.paddle = paddle.Paddle()
        pyxel.run(self.update,self.draw)

    def update(self):
        if sp.collision(self.ball.sp,self.paddle.sp):
            self.ball.sp.dy = (-1)*self.ball.sp.dy
        self.ball.update()
        self.paddle.update()

    def draw(self):
        pyxel.cls(0)
        self.ball.draw()
        self.paddle.draw()
        pyxel.flip()
        
if __name__=="__main__":
    Game()
    