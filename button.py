import pygame

from data import *
from utils import load_image, imageScalePercent

class Button(pygame.sprite.Sprite) :
    def __init__(self, startX, startY) :
        pygame.sprite.Sprite.__init__(self)

        self.currPosX, self.currPosY = startX, startY
        self.available = False
    
    def setAvailable(self, state) :
        self.available = state

class KillButton(Button) :
    def __init__(self, startX, startY) :
        Button.__init__(self, startX, startY)

        self.imageAFull, _ = load_image('killBt.png', 'Others')
        self.imageAHalf, _ = load_image('killBtTP.png', 'Others')

        self.image, self.rect = self.imageAFull, self.imageAFull.get_rect()
        self.image = imageScalePercent(self.image, 80)

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.midbottom = self.currPosX, self.currPosY

        self.setAvailable(False)

    def update(self) :
        if self.available == False :
            self.image = imageScalePercent(self.imageAHalf, 80)
        else :
            self.image = imageScalePercent(self.imageAFull, 80)

class SbtgButton(Button) :
    def __init__(self, startX, startY) :
        Button.__init__(self, startX, startY)

        self.imageAFull, _ = load_image('saboBt.png', 'Others')
        self.imageAHalf, _ = load_image('saboBtTP.png', 'Others')

        self.image, self.rect = self.imageAFull, self.imageAFull.get_rect()
        self.image = imageScalePercent(self.image, 80)

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.midbottom = self.currPosX, self.currPosY

        self.setAvailable(True)

    def update(self) :
        if self.available == False :
            self.image = imageScalePercent(self.imageAHalf, 80)
        else :
            self.image = imageScalePercent(self.imageAFull, 80)

class ReviveButton(Button) :
    def __init__(self, startX, startY) :
        Button.__init__(self, startX, startY)

        self.imageAFull, _ = load_image('AgainBt.png', 'Others')
        self.imageAHalf, _ = load_image('AgainBtTP.png', 'Others')

        self.image, self.rect = self.imageAFull, self.imageAFull.get_rect()
        self.image = imageScalePercent(self.image, 80)

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topright = self.currPosX, self.currPosY

        self.setAvailable(False)

    def update(self) :
        if self.available == False :
            self.image = imageScalePercent(self.imageAHalf, 80)
        else :
            self.image = imageScalePercent(self.imageAFull, 80)