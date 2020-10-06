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
            player.updateAnimation_NonReset(WALK_LEFT)

        if keys[pg.K_d] :
            player.setRightPressed(True)
            player.updateAnimation_NonReset(WALK_RIGHT)

        if keys[pg.K_w] :
            player.setUpPressed(True) 
            player.updateAnimation_NonReset(WALK_UP)
        
        if keys[pg.K_s] :
            player.setDownPressed(True)
            player.updateAnimation_NonReset(WALK_DOWN)

        if list(keys).count(1) == 0 :
            player.setIdlePressed()
            player.updateAnimation(IDLE)

        player.update()

        screen.fill(WHITE)
        screen.blit(player.image, player.getCurrentPosition())

        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()