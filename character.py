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
            self.idleAnimation()

        elif self.currAnimation == WALK :
            self.walk()
            self.walkAnimation()
            self.setRectCenterPos()

    def idleAnimation(self) :
        self.count = 1

        imagePath = 'idle.png'
        self.image, self.rect = load_image(imagePath, 'Imposter\\idle')

        if self.faceSide == FACE_LEFT :
            self.image = imageFlipLR(self.image)

        self.rect.center = self.currPosX, self.currPosY
    
    def walkAnimation(self) :
        if self.count == WALK_ANIMATION_FRAME :
            self.count = 1

        imagePath = 'walk{}.png'.format(self.count)
        self.image, self.rect = load_image(imagePath, 'Imposter\\walk')

        if self.faceSide == FACE_LEFT :
            self.image = imageFlipLR(self.image)

        screen = pg.display.get_surface()
        self.area = screen.get_rect()

        self.count += 1

        if self.count == WALK_ANIMATION_FRAME + 1:
            self.count = 1

    def walk(self) :
        if self.leftPressed :
            self.faceSide = FACE_LEFT
            if self.currPosX > LIMIT_LEFT :
                self.currPosX -= MOVE_SPEED
            else :
                self.currPosX = LIMIT_LEFT

        if self.rightPressed :
            self.faceSide = FACE_RIGHT
            if self.currPosX < LIMIT_RIGHT :
                self.currPosX += MOVE_SPEED
            else :
                self.currPosX = LIMIT_RIGHT

        if self.upPressed :
            if self.currPosY > LIMIT_TOP :
                self.currPosY -= MOVE_SPEED
            else :
                self.currPosY = LIMIT_TOP

        if self.downPressed :
            if self.currPosY < LIMIT_BOTTOM :
                self.currPosY += MOVE_SPEED
            else :
                self.currPosY = LIMIT_BOTTOM

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

    def checkAction(self) :
        if self.upPressed or self.downPressed or self.leftPressed or self.rightPressed :
            return WALK
        else :
            return IDLE

    def setRectCenterPos(self) :
        self.rect.center = self.currPosX, self.currPosY