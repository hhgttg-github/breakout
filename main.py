import pyxel
import sprite as sp
import screen
import ball
import paddle
import brick

####====================================
#### CONSTANT

####====================================
#### CLASS

class Game:
    def __init__(self):
        pyxel.init(screen.WIDTH,screen.HEIGHT,fps=60)
        pyxel.load("breakout.pyxres")
        ball.init_line16()
        self.ball = ball.Ball()
        self.paddle = paddle.Paddle()
        self.score = 0
        self.bricks = brick.Bricks_Table()
        pyxel.run(self.update,self.draw)

    def update(self):
        if sp.collision(self.ball.sp,self.paddle.sp):
            if self.ball.sp.dy > 0:
                self.ball.sp.dy = (-1)*self.ball.sp.dy
        self.ball.reflect_around()
        self.ball.update()
        self.paddle.update()
        self.bricks.update(self.ball)

    def draw(self):
        pyxel.cls(0)
        self.ball.draw()
        self.paddle.draw()
        self.bricks.draw()
        screen.draw_score(self.score)
        pyxel.flip()
        
if __name__=="__main__":
    Game()
    