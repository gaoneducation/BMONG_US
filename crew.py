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

    def idleAnimation(self) :
        self.count = 1

        imageFileName = 'idle.png'
        self.image, self.rect = load_image(imageFileName, 'Crew\\idle')

        if self.faceSide == FACE_LEFT :
            self.image = imageFlipLR(self.image)

        self.rect.center = self.currPosX, self.currPosY