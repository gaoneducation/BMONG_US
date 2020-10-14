import pygame

from utils import load_image

class Table(pygame.sprite.Sprite) :
    def __init__(self, startX, startY):
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_image('MeetingTable.png', 'Background')

        self.centerX = startX
        self.centerY = startY

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = self.centerX, self.centerY
