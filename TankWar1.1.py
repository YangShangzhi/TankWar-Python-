'''
New Function: Load main window
Reference: www.pygame.org
'''

from pygame import *

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BGCOLOR = Color(0,0,0)

class MainGame():
    def __init__(self):
        pass

    def startGame(self):
        #init main window
        display.init()
        #set width and height
        MainGame.window = display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # set window title
        display.set_caption("TankWar")
        # show the window
        while True:
            # set bg color
            MainGame.window.fill(BGCOLOR)
            display.update()

    def quitGame(self):
        pass

class Tank():
    pass

class MyTank(Tank):
    pass

class EnemyTank(Tank):
    pass

class Bullet():
    pass

class Explode():
    pass

class Wall():
    pass

class Music():
    pass

if __name__ == '__main__':
    MainGame().startGame()