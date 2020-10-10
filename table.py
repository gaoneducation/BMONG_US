import pygame as pg

from utils import *
from data import *

class Table(pygame.sprite.Sprite) :
    def __init__(self, startX, startY):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('MeetingTable.png', 'Background')

        self.centerx = startX
        self.centery = startY

        self.currPosX = startX
        self.currPosY = startY

        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = (self.centerx, self.centery)
