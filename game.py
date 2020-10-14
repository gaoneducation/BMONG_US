import os, sys

import pygame
import math

from data import *
from character import Character
from imposter import Imposter
from crew import Crew
from background import *
from button import KillButton, SbtgButton, ReviveButton
from table import Table
from utils import delTempImage, makeImagePaletteSwap, mouseOnButton

pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

clock = pygame.time.Clock()

def main() :
    bg = Background(0,0)

    makeImagePaletteSwap(PALETTE_DEFAULT)

    player = Imposter(250, 120)
    dummy = Crew(710, 600)

    table = Table(TABLE_POS_X, TABLE_POS_Y)

    killBt = KillButton(KILL_BUTTON_X, KILL_BUTTON_Y)
    sbtgBt = SbtgButton(SABOTAGE_BUTTON_X, SABOTAGE_BUTTON_Y)
    reviveBt = ReviveButton(REVIVE_BUTTON_X, REVIVE_BUTTON_Y)
    
    sbtgCounter = 0
    sbtgBG, sbtgBG_rect = load_image('SBTG_BG.png', 'Others')
    sbtgBG_rect.topleft = SBTG_BG_POS_X, SBTG_BG_POS_Y

    spriteGroup = pygame.sprite.LayeredUpdates((bg, table, dummy, player, killBt, sbtgBt, reviveBt))

    loop = True

    while loop :
        clock.tick(FPS)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                loop = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                loop = False

        keys = pygame.key.get_pressed()
        leftclick = pygame.mouse.get_pressed()[MOUSE_LEFT]

        if keys[pygame.K_a] :
            player.setLeftPressed(True)
        elif keys[pygame.K_a] == 0 :
            player.setLeftPressed(False)

        if keys[pygame.K_d] :
            player.setRightPressed(True)
        elif keys[pygame.K_d] == 0 :
            player.setRightPressed(False)

        if keys[pygame.K_w] :
            player.setUpPressed(True) 
        elif keys[pygame.K_w] == 0 :
            player.setUpPressed(False)
        
        if keys[pygame.K_s] :
            player.setDownPressed(True)
        elif keys[pygame.K_s] == 0 :
            player.setDownPressed(False)

        playerAction = player.checkAction()
        if playerAction == IDLE :
            player.updateAnimation(IDLE)
        elif playerAction == WALK :
            player.updateAnimation_NonReset(WALK)

        if leftclick : 
            if killBt.available == True and mouseOnButton(killBt) :
                player.addkillCounter()
                player.killMotion(screen)
                player.updateAnimation(IDLE)
                dummy.updateAnimation(DEAD)
                dummy.setDead(True)
            elif reviveBt.available == True and mouseOnButton(reviveBt) :
                dummy.updateAnimation(REVIVE)
                dummy.setDead(False)
            elif sbtgBt.available == True and mouseOnButton(sbtgBt) :
                player.setSabotageState(True)
                sbtgBt.setAvailable(False)

        if player.rect.colliderect(dummy) and dummy.dead == False :
            killBt.setAvailable(True)
        else :
            killBt.setAvailable(False)

        if dummy.dead == True :
            reviveBt.setAvailable(True)
        else :
            reviveBt.setAvailable(False)

        # 타원(테이블) 충돌
        a = 265
        b = 233
        dump = 10
        ay = math.pow(a, 2)*math.pow(player.currPosY-table.centery+dump, 2)
        bx = math.pow(b, 2)*math.pow(player.currPosX-table.centerx, 2)
        distance = math.sqrt(ay+bx)
        if distance <= a*b:
            if player.currPosX > table.centerx-265 & player.currPosX < table.centerx+265:
                if player.currPosY < table.centery:
                    player.setDownPressed(False)
                elif player.currPosY > table.centery:
                    player.setUpPressed(False)
            if player.currPosY > table.centery-233 & player.currPosY < table.centery+233:
                if player.currPosX > table.centerx:
                    player.setLeftPressed(False)
                elif player.currPosX < table.centerx:
                    player.setRightPressed(False)

        spriteGroup.remove(player)

        player.update()
        spriteGroup.update()

        spriteGroup.add(player)

        if player.currPosY >= dummy.currPosY :
            spriteGroup.move_to_back(player)
            spriteGroup.move_to_back(dummy)
        else :
            spriteGroup.move_to_back(dummy)
            spriteGroup.move_to_back(player)
        
        if player.currPosY >= table.centery :
            spriteGroup.move_to_back(table)
        else :
            spriteGroup.move_to_front(table)

        spriteGroup.move_to_back(bg)
        spriteGroup.move_to_front(killBt)
        spriteGroup.move_to_front(sbtgBt)
        spriteGroup.move_to_front(reviveBt)
        
        spriteGroup.draw(screen)
        
        if player.sabotage == True :
            sbtgTime = int(sbtgCounter / FPS)
            if (sbtgTime >= 0 and sbtgTime < 1) or \
                (sbtgTime >= 2 and sbtgTime < 3) or \
                (sbtgTime >= 4 and sbtgTime < 5) :

                screen.blit(sbtgBG, (SBTG_BG_POS_X, SBTG_BG_POS_Y))
            else :
                pass

            sbtgCounter += 1

            if sbtgCounter > SBTG_DURATION :
                sbtgCounter = 0
                player.setSabotageState(False)
                sbtgBt.setAvailable(True)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
    
    delTempImage()
