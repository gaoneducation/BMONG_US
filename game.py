import sys

import pygame as pg

from data import *
from character import Character

pg.init()
pg.display.set_caption(TITLE)
screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

clock = pg.time.Clock()

def main() :
    player = Character(470, 260)
    
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

        player.update()

        screen.fill(WHITE)
        screen.blit(player.image, player.getCurrentPosition())

        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()