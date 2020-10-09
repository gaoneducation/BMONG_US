import pygame as pg

from data import *
from utils import *

class Background(pygame.sprite.Sprite) :
    def __init__(self, startX, startY) :
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_image('MeetingRoom2.png', 'Background')

        self.currPosX, self.currPosY = startX, startY
        self.rect.topleft = self.currPosX, self.currPosY

        self.currAnimation = BG_IDLE

    def update(self) :
        if self.currAnimation == BG_IDLE :
            return None

class Collision_Line(pygame.sprite.Sprite) :
    def __init__(self, startX, startY, width, height) :
        pygame.sprite.Sprite.__init(self)

        self.image = pg.Surface([width, height])

        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.y = startY
        self.rect.x = startX