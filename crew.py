import pygame as pg

from data import *
from utils import *
from character import Character

class Crew(Character) :
    def __init__(self, startX, startY) :
        Character.__init__(self, startX, startY)

        self.dead = False

    def update(self) :
        if self.currAnimation == IDLE :
            self.idleAnimation()
        if self.currAnimation == DEAD :
            self.deadAnimation()
            self.setRectCenterPos()

    def idleAnimation(self) :
        self.count = 1

        imageFileName = 'idle.png'
        self.image, self.rect = load_image(imageFileName, 'Crew\\idle')

        if self.faceSide == FACE_LEFT :
            self.image = imageFlipLR(self.image)

        self.rect.center = self.currPosX, self.currPosY

    def walkAnimation(self) :
        if self.count == WALK_ANIMATION_FRAME :
            self.count = 1

        imageFileName = 'walk{}.png'.format(self.count)
        self.image, self.rect = load_image(imageFileName, 'Crew\\walk')

        if self.faceSide == FACE_LEFT :
            self.image = imageFlipLR(self.image)

        screen = pg.display.get_surface()
        self.area = screen.get_rect()

        self.count += 1

        if self.count == WALK_ANIMATION_FRAME + 1:
            self.count = 1

    def deadAnimation(self) :
        if self.count == DEAD_ANIMATION_FRAME :
            self.count = 33

        imageFileName = 'Dead{}.png'.format(self.count)
        self.image, self.rect = load_image(imageFileName, 'Crew\\dead')

        screen = pg.display.get_surface()
        self.area = screen.get_rect()

        self.count += 1

        if self.count == DEAD_ANIMATION_FRAME + 1 :
            self.count = 33
    
    def setDead(self, state) :
        self.dead = state