import sys

import pygame as pg

from data import *
from character import Character
from imposter import Imposter
from background import *

pg.init()
pg.display.set_caption(TITLE)
screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

clock = pg.time.Clock()

def main() :
    bg = Background(0,0)

    player = Imposter(250, 120)

    spriteGroup = pg.sprite.LayeredUpdates((bg, player))
    
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

        spriteGroup.remove(player)

        player.update()
        spriteGroup.update()

        spriteGroup.add(player)
        spriteGroup.move_to_back(player)
        spriteGroup.move_to_back(bg)

        spriteGroup.draw(screen)
        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()