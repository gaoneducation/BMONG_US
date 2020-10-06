import pygame as pg

from utils import *
from data import *

class Character(pygame.sprite.Sprite) :
    def __init__(self, startX, startY):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('1.png', 'test')

        self.basePosX = 470
        self.basePosY = 260

        self.currPosX = startX
        self.currPosY = startY

        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = self.currPosX, self.currPosY

        self.currAnimation = IDLE
        self.faceSide = FACE_RIGHT

        self.leftPressed = False
        self.rightPressed = False
        self.upPressed = False
        self.downPressed = False

        self.count = 1

    def update(self) :
        if self.currAnimation == IDLE :
            self.count = 1

            imagePath = '{}.png'.format(self.count)
            self.image, self.rect = load_image(imagePath, 'test')

            if self.faceSide == FACE_LEFT :
                self.image = pg.transform.flip(self.image, 1, 0)

            self.rect.center = self.currPosX, self.currPosY

        elif self.currAnimation == WALK_LEFT :
            if self.leftPressed == False :
                self.currAnimation = IDLE

            if self.count == WALK_ANIMATION_FRAME :
                self.count = 1

            if self.currPosX > -10 :
                self.currPosX -= 5
            else :
                self.currPosX -= 0

            imagePath = '{}.png'.format(self.count)
            self.image, self.rect = load_image(imagePath, 'test')
            self.image = pg.transform.flip(self.image, 1, 0)

            screen = pg.display.get_surface()
            self.area = screen.get_rect()

            if self.currPosX > -10 :
                self.rect.center = self.currPosX, self.currPosY
            else :
                self.currPosX = -10
                self.rect.center = self.currPosX, self.currPosY

            self.faceSide = FACE_LEFT
            self.count += 1

            if self.count == WALK_ANIMATION_FRAME + 1 :
                self.count = 1

        elif self.currAnimation == WALK_RIGHT :
            if self.rightPressed == False :
                self.currAnimation == IDLE

            if self.count == WALK_ANIMATION_FRAME :
                self.count = 1

            if self.currPosX < 950 :
                self.currPosX += 5
            else :
                self.currPosX += 0

            imagePath = '{}.png'.format(self.count)
            self.image, self.rect = load_image(imagePath, 'test')

            screen = pg.display.get_surface()
            self.area = screen.get_rect()

            if self.currPosX < 950 :
                self.rect.center = self.currPosX, self.currPosY
            else :
                self.currPosX = 950
                self.rect.center = self.currPosX, self.currPosY

            self.faceSide = FACE_RIGHT
            self.count += 1

            if self.count == WALK_ANIMATION_FRAME + 1  :
                self.count = 1

        elif self.currAnimation == WALK_UP :
            if self.upPressed == False :
                self.currAnimation == IDLE

            if self.count == WALK_ANIMATION_FRAME :
                self.count = 1

            if self.currPosY > -10 :
                self.currPosY -= 5
            else :
                self.currPosY += 0

            imagePath = '{}.png'.format(self.count)
            self.image, self.rect = load_image(imagePath, 'test')
            if self.faceSide == FACE_LEFT :
                self.image = pg.transform.flip(self.image, 1, 0)

            screen = pg.display.get_surface()
            self.area = screen.get_rect()

            if self.currPosY > -10:
                self.rect.center = self.currPosX, self.currPosY
            else :
                self.currPosY = -10
                self.rect.center = self.currPosX, self.currPosY

            self.count += 1

            if self.count == WALK_ANIMATION_FRAME + 1  :
                self.count = 1

        elif self.currAnimation == WALK_DOWN :
            if self.downPressed == False :
                self.currAnimation == IDLE

            if self.count == WALK_ANIMATION_FRAME :
                self.count = 1

            if self.currPosY < 530 :
                self.currPosY += 5
            else :
                self.currPosY += 0

            imagePath = '{}.png'.format(self.count)
            self.image, self.rect = load_image(imagePath, 'test')
            if self.faceSide == FACE_LEFT :
                self.image = pg.transform.flip(self.image, 1, 0)
                
            screen = pg.display.get_surface()
            self.area = screen.get_rect()

            if self.currPosY < 530 :
                self.rect.center = self.currPosX, self.currPosY
            else :
                self.currPosY = 530
                self.rect.center = self.currPosX, self.currPosY

            self.count += 1

            if self.count == WALK_ANIMATION_FRAME + 1  :
                self.count = 1

    def updateAnimation(self, animate) :
        self.count = 0
        self.currAnimation = animate

    def updateAnimation_NonReset(self, animate) :
        self.currAnimation = animate

    def getCurrentPosition(self) :
        return self.currPosX, self.currPosY
    
    def setUpPressed(self, state) :
        self.upPressed = state
    
    def setDownPressed(self, state) :
        self.downPressed = state

    def setLeftPressed(self, state) :
        self.leftPressed = state

    def setRightPressed(self, state) :
        self.rightPressed = state

    def setIdlePressed(self) :
        self.setLeftPressed(False)
        self.setUpPressed(False)
        self.setDownPressed(False)
        self.setRightPressed(False)