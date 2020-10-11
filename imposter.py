import pygame as pg

from character import Character
from utils import *
from data import *

class Imposter(Character) :
    def __init__(self, startX, startY) :
        Character.__init__(self, startX, startY)

        self.sabotage = False
        self.kill = False

    def update(self) :
        if self.currAnimation == IDLE :
            self.idleAnimation()

        elif self.currAnimation == WALK :
            self.walk()
            self.walkAnimation()
            self.setRectCenterPos()

    def idleAnimation(self) :
        self.count = 1

        imageFileName = 'idle.png'
        self.image, self.rect = load_image(imageFileName, 'Imposter\\idle')

        if self.faceSide == FACE_LEFT :
            self.image = imageFlipLR(self.image)

        self.rect.center = self.currPosX, self.currPosY

    def walkAnimation(self) :
        if self.count == WALK_ANIMATION_FRAME :
            self.count = 1

        imageFileName = 'walk{}.png'.format(self.count)
        self.image, self.rect = load_image(imageFileName, 'Imposter\\walk')

        if self.faceSide == FACE_LEFT :
            self.image = imageFlipLR(self.image)

        screen = pg.display.get_surface()
        self.area = screen.get_rect()

        self.count += 1

        if self.count == WALK_ANIMATION_FRAME + 1:
            self.count = 1