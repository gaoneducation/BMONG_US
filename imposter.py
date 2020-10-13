import pygame as pg

from character import Character
from utils import *
from data import *
from _test import Customize

class Imposter(Character) :
    def __init__(self, startX, startY) :
        Character.__init__(self, startX, startY)

        customize = Customize()
        # red, green, blue, pink 가능
        customize.colorSwap("red")
        self.sabotage = False
        self.killCount = 0

    def update(self) :
        if self.currAnimation == IDLE :
            self.idleAnimation()

        elif self.currAnimation == WALK :
            self.walk()
            self.walkAnimation()
            self.setRectCenterPos()

    def addkillCounter(self) :
        self.killCount += 1

    def setSabotageState(self, state) :
        self.sabotage = state

    def idleAnimation(self) :
        self.count = 1

        imageFileName = 'idle.png'
        # self.image, self.rect = load_image(imageFileName, 'Imposter\\idle\\custom')
        self.image, self.rect = load_image(imageFileName, 'Imposter\\temp')

        if self.faceSide == FACE_LEFT :
            self.image = imageFlipLR(self.image)

        self.rect.center = self.currPosX, self.currPosY

    def walkAnimation(self) :
        if self.count == WALK_ANIMATION_FRAME :
            self.count = 1

        imageFileName = 'walk{}.png'.format(self.count)
        # self.image, self.rect = load_image(imageFileName, 'Imposter\\walk')
        self.image, self.rect = load_image(imageFileName, 'Imposter\\temp')

        if self.faceSide == FACE_LEFT :
            self.image = imageFlipLR(self.image)

        screen = pg.display.get_surface()
        self.area = screen.get_rect()

        self.count += 1

        if self.count == WALK_ANIMATION_FRAME + 1:
            self.count = 1

    def killMotion(self, display) :
        self.count = 1

        killBG, killBG_rect = load_image('killBg.png', 'Others')
        killBG_rect.center = KILL_BG_POS_X, KILL_BG_POS_Y

        while self.count <= KILL_ANIMATION_FRAME :
            pg.time.Clock().tick(30)

            imageFileName = 'kill{}.jpg'.format(self.count)
            self.image, self.rect = load_image(imageFileName, 'Imposter\\kill')

            screen = pg.display.get_surface()
            self.area = screen.get_rect()

            self.count += 1
            self.rect.topleft = KILL_ANIMATION_X, KILL_ANIMATION_Y

            display.blit(killBG, (KILL_BG_POS_X, KILL_BG_POS_Y))
            display.blit(self.image, (KILL_ANIMATION_X, KILL_ANIMATION_Y))
            pg.display.update()
            
        
