'''
New Function: opimize the function of my bullet:
    1.the movement of my bullet
    2.the bullet should disappear while hitting the wall
    3.my tank can shoot 3 bullets at most
Reference: www.pygame.org
'''

import pygame, time, nprandom

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BGCOLOR = pygame.Color(0,0,0)
FONT_COLOR = pygame.Color(255,0,0)
TANK_SPEED = 3
ENEMY_TANK_SPEED = [1,2,3,4,5]
ENEMY_TANK_COUNT = 4
ENEMY_TANK_STEP = 50
BULLET_SPEED = 6
MAX_BULLET_NUM = 3

class MainGame():
    window = None
    myTank = None
    enemyTanksList = []
    myBulletsList = []

    def __init__(self):
        pass

    def startGame(self):
        #init main window
        pygame.display.init()
        #set width and height
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # set window title
        pygame.display.set_caption("TankWar")
        # init my tank
        MainGame.myTank = MyTank(350, 250)
        # init enemy tanks
        self.initEnemyTanks()
        # init my bullets has been done in KEY_DOWN
        # self.initMyBullets()
        # show the window
        while True:
            # set the update time
            time.sleep(0.02)
            # set bg color
            MainGame.window.fill(BGCOLOR)
            # draw new surface to window surface
            MainGame.window.blit(self.getFontSurface("Remain Enemies:{0}".format(len(MainGame.enemyTanksList))), (10,10))
            # display the tank
            MainGame.myTank.displayTank()
            self.displayEnemyTank()
            # display the my bullets
            self.displayMyBullets()
            # record the events
            self.getEvent()
            # control the movement of my tank
            if MainGame.myTank.movement:
                MainGame.myTank.move()
            # update the screen
            pygame.display.update()

    def displayMyBullets(self):
        for bullet in MainGame.myBulletsList:
            if bullet.alive:
                bullet.displayBullet()
                bullet.move()
            else:
                MainGame.myBulletsList.remove(bullet)

    def displayEnemyTank(self):
        for enemyTank in MainGame.enemyTanksList:
            enemyTank.displayTank()
            enemyTank.randMove()

    def initEnemyTanks(self):
        top = 100
        # loop to create enemy tanks
        for i in range(ENEMY_TANK_COUNT):
            left = nprandom.randint(0, 600)
            speed = nprandom.randint(1, 4)
            enemyTank = EnemyTank(top, left, speed)
            MainGame.enemyTanksList.append(enemyTank)

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
                if event.key == pygame.K_LEFT:
                    MainGame.myTank.direction = 'L'
                    # MainGame.myTank.move()
                    MainGame.myTank.movement = True
                elif event.key == pygame.K_RIGHT:
                    MainGame.myTank.direction = 'R'
                    # MainGame.myTank.move()
                    MainGame.myTank.movement = True
                elif event.key == pygame.K_UP:
                    MainGame.myTank.direction = 'U'
                    # MainGame.myTank.move()
                    MainGame.myTank.movement = True
                elif event.key == pygame.K_DOWN:
                    MainGame.myTank.direction = 'D'
                    # MainGame.myTank.move()
                    MainGame.myTank.movement = True
                elif event.key == pygame.K_SPACE:
                    # init a bullet while push K_SPACE
                    if len(MainGame.myBulletsList) < MAX_BULLET_NUM:
                        myBullet = Bullet(MainGame.myTank)
                        MainGame.myBulletsList.append(myBullet)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    MainGame.myTank.movement = False

class Tank():
    def __init__(self):
        super().__init__()
        self.direction = 'U'
        self.speed = TANK_SPEED
        self.myTanksImgs = {
            'U': pygame.image.load('img/mytankU.gif'),
            'R': pygame.image.load('img/mytankR.gif'),
            'D': pygame.image.load('img/mytankD.gif'),
            'L': pygame.image.load('img/mytankL.gif')
        }
        self.enemyTanksImgs = {
            'U': pygame.image.load('img/enemyU.gif'),
            'R': pygame.image.load('img/enemyR.gif'),
            'D': pygame.image.load('img/enemyD.gif'),
            'L': pygame.image.load('img/enemyL.gif')
        }

class MyTank(Tank):
    # init my tank and set the position of the tank
    def __init__(self, left, top):
        super().__init__()
        # get my tank surface according to the direction
        self.myTank = self.myTanksImgs.get(self.direction)
        # get the rectangle of my tank
        self.rect = self.myTank.get_rect()
        self.rect.left = left
        self.rect.top = top
        # set a flag to control the continue movement
        self.movement = False

    # display the tank in the game window
    def displayTank(self):
        # get my tank surface
        self.myTank = self.myTanksImgs.get(self.direction)
        # display it
        MainGame.window.blit(self.myTank, self.rect)

    def move(self):
        # judging direction
        if self.direction == "L":
            self.rect.left -= self.speed
            if self.rect.left <= 0:
                self.rect.left = 0
        elif self.direction == "R":
            self.rect.left += self.speed
            if self.rect.left + self.rect.height >= SCREEN_WIDTH:
                self.rect.left = SCREEN_WIDTH - self.rect.height
        elif self.direction == "U":
            self.rect.top -= self.speed
            if self.rect.top <= 0:
                self.rect.top = 0
        elif self.direction == "D":
            self.rect.top += self.speed
            if self.rect.top + self.rect.height >= SCREEN_HEIGHT:
                self.rect.top = SCREEN_HEIGHT - self.rect.height

class EnemyTank(Tank):
    def __init__(self, top, left, speed):
        super().__init__()
        self.enemyTank = self.enemyTanksImgs.get(self.direction)
        self.direction = self.randDirection()
        self.rect = self.enemyTank.get_rect()
        self.speed = ENEMY_TANK_SPEED[nprandom.randint(0, 4)]
        self.rect.left = left
        self.rect.top = top
        self.movement = True
        self.step = ENEMY_TANK_STEP

    def randMove(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = ENEMY_TANK_STEP
        else:
            self.step -= 1
            self.move()

    def move(self):
        # judging direction
        if self.direction == "L":
            self.rect.left -= self.speed
            if self.rect.left <= 0:
                self.rect.left = 0
        elif self.direction == "R":
            self.rect.left += self.speed
            if self.rect.left + self.rect.height >= SCREEN_WIDTH:
                self.rect.left = SCREEN_WIDTH - self.rect.height
        elif self.direction == "U":
            self.rect.top -= self.speed
            if self.rect.top <= 0:
                self.rect.top = 0
        elif self.direction == "D":
            self.rect.top += self.speed
            if self.rect.top + self.rect.height >= SCREEN_HEIGHT:
                self.rect.top = SCREEN_HEIGHT - self.rect.height

    def randDirection(self):
        num = nprandom.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'

    def displayTank(self):
        # get my tank surface
        self.enemyTank = self.enemyTanksImgs.get(self.direction)
        # display it
        MainGame.window.blit(self.enemyTank, self.rect)

class Bullet():
    def __init__(self, tank):
        self.myBulletImg = pygame.image.load('img/bullet.gif')
        self.rect = self.myBulletImg.get_rect()
        self.direction = tank.direction
        self.speed = 6
        self.alive = True
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2

    def displayBullet(self):
        MainGame.window.blit(self.myBulletImg, self.rect)

    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.alive = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < SCREEN_WIDTH:
                self.rect.left += self.speed
            else:
                self.alive = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed
            else:
                self.alive = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.alive = False

class Explode():
    pass

class Wall():
    pass

class Music():
    pass

if __name__ == '__main__':
    MainGame().startGame()
    # MainGame().getFontSurface()