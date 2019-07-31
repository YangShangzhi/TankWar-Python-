'''
New Function: Create font on the left corner
Reference: www.pygame.org
'''

import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BGCOLOR = pygame.Color(0,0,0)
FONT_COLOR = pygame.Color(255,0,0)

class MainGame():
    def __init__(self):
        pass

    def startGame(self):
        #init main window
        pygame.display.init()
        #set width and height
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # set window title
        pygame.display.set_caption("TankWar")
        # show the window
        while True:
            # set bg color
            MainGame.window.fill(BGCOLOR)
            #draw new surface to window surface
            MainGame.window.blit(self.getFontSurface("Remain Enemies:{0}".format(6)), (10,10))
            # record the events
            self.getEvent()
            # update the screen
            pygame.display.update()

    def quitGame(self):
        print("successful quit!")
        exit()

    def getFontSurface(self,text):
        # init the font module
        pygame.font.init()
        # show the fonts' names
        # print(pygame.font.get_fonts())
        # get a font object
        font = pygame.font.SysFont("consolas", 18)
        # draw text on a new surface
        textSurface = font.render(text, True, FONT_COLOR)
        # return textsurface
        return textSurface

    def getEvent(self):
        # record the events
        eventList = pygame.event.get()
        # loop the events and do reaction
        for event in eventList:
            # if click "close" button
            if event.type == pygame.QUIT:
                self.quitGame()
            # if click keyboard
            if event.type == pygame.KEYDOWN:
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
    # MainGame().getFontSurface()