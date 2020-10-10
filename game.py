import sys

import pygame as pg
import math

from data import *
from character import Character
from background import *
from table import *

pg.init()
pg.display.set_caption(TITLE)
screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

clock = pg.time.Clock()

def main() :
    bg = Background(0,0)

    table = Table(485, 370)

    player = Character(200, 260)

    
    
    spriteGroup = pg.sprite.LayeredUpdates((bg, table, player))
    
    loop = True

    while loop :
        clock.tick(FPS)

        for event in pg.event.get() :
            if event.type == pg.QUIT :
                loop = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                loop = False

        keys = pg.key.get_pressed()

        if keys[pg.K_a] :
            player.setLeftPressed(True)
        elif keys[pg.K_a] == 0 :
            player.setLeftPressed(False)

        if keys[pg.K_d] :
            player.setRightPressed(True)
        elif keys[pg.K_d] == 0 :
            player.setRightPressed(False)

        if keys[pg.K_w] :
            player.setUpPressed(True) 
        elif keys[pg.K_w] == 0 :
            player.setUpPressed(False)
        
        if keys[pg.K_s] :
            player.setDownPressed(True)
        elif keys[pg.K_s] == 0 :
            player.setDownPressed(False)

        playerAction = player.checkAction()
        if playerAction == IDLE :
            player.updateAnimation(IDLE)
        elif playerAction == WALK :
            player.updateAnimation_NonReset(WALK)

        '''
        #test 원 충돌
        if(pygame.sprite.collide_rect(b1,player)):
            if player.currPosY == b1.centery-100:
                player.setDownPressed(False)
            elif player.currPosY == b1.centery+100:
                player.setUpPressed(False)
            elif player.currPosX == b1.centerx-100:
                player.setLeftPressed(False)
            elif player.currPosX == b1.centerx+100:
                player.setRightPressed(False)
        '''

        a = 265
        b = 233
        dump = 10
        ay = math.pow(a, 2)*math.pow(player.currPosY-table.centery+dump, 2)
        bx = math.pow(b, 2)*math.pow(player.currPosX-table.centerx, 2)
        distance = math.sqrt(ay+bx)
        if distance <= a*b:
            if player.currPosX > table.centerx-200 & player.currPosX < table.centerx+200:
                if player.currPosY < table.centery:
                    player.setDownPressed(False)
                elif player.currPosY > table.centery:
                    player.setUpPressed(False)
            if player.currPosY > table.centery-200 & player.currPosY < table.centery+200:
                if player.currPosX > table.centerx:
                    player.setLeftPressed(False)
                elif player.currPosX < table.centerx:
                    player.setRightPressed(False)


        spriteGroup.remove(player)

        player.update()
        spriteGroup.update()

        spriteGroup.add(player)
        spriteGroup.move_to_back(player)
        spriteGroup.move_to_back(bg)

        #screen.fill(WHITE)
        #screen.blit(player.image, player.getCurrentPosition())

        spriteGroup.draw(screen)
        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()