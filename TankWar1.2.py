'''
New Function: add close function to quit the game window
Reference: www.pygame.org
'''

import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BGCOLOR = pygame.Color(0,0,0)

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
            # record the events
            self.getEvent()
            # update the screen
            pygame.display.update()

    def quitGame(self):
        print("successful quit!")
        exit()

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