import pygame

from utils import load_image

class Background(pygame.sprite.Sprite) :
    def __init__(self, startX, startY) :
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_image('MeetingRoom2.png', 'Background')

        self.currPosX, self.currPosY = startX, startY
        self.rect.topleft = self.currPosX, self.currPosY
