import pyxel
import sprite as sp

####====================================
#### CONSTANT

####====================================
#### CLASS

class Game:
    def __init__(self):
        pyxel.init(256,256,fps=60)
        pyxel.load("breakout.pyxres")

        pyxel.run(self.update,self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,128,128)
        
if __name__=="__main__":
    Game()
    