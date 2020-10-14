import os
import PIL.Image as Image
import glob
from pathlib import Path

import pygame
from pygame.compat import geterror

import data

mainDIR = os.path.split(os.path.abspath(__file__))[0]
dataDIR = os.path.join(mainDIR, 'data')

def load_image(name, folderName) :
    fullname_Folder = os.path.join(dataDIR, folderName)
    fullname = os.path.join(fullname_Folder, name)

    PNG = True if fullname.endswith('png') or fullname.endswith('PNG') else False

    try :
        image = pygame.image.load(fullname)
    except pygame.error :
        print('Cannot load image : ' + fullname)
        raise SystemExit(str(geterror()))

    if PNG :
        image = image.convert_alpha()
    else :
        image = image.convert()

    return image, image.get_rect()

def load_sprite_image(name, f1, f2, f3, f4):
    fullname_Folder = os.path.join(dataDIR, f1, f2, f3, f4)
    fullname = os.path.join(fullname_Folder, name)

    try :
        image = pygame.image.load(fullname)
        image.set_colorkey((0,0,0))
    except pygame.error:
        print ('Cannot load image :', fullname)
        raise SystemExit(str(geterror()))

    return image, image.get_rect()

def imageFlipLR(image) :
    return pygame.transform.flip(image, 1, 0)

def imageScalePercent(image, scalePercent) :
    width = int(image.get_width() * scalePercent / 100)
    height = int(image.get_height() * scalePercent / 100)

    return pygame.transform.scale(image, (width, height))

def imageScaleAbsolute(image, width, height) :
    return pygame.transform.scale(image, (width, height))

def createModifiedSprites(path, palatteColor):
    src = Image.open(path)
    px = src.load()
    width, height = src.size

    for i in range(width):
        for j in range(height):
            pixel = px[i, j]
            r, g, b = pixel[0], pixel[1], pixel[2]
            
            if pixel == data.PALETTE_BLUE[0] or (70 < b < 255) and not (g > 220 and b > 80):
                px[i, j] = palatteColor[1]
                
            if pixel == data.PALETTE_RED[0] or (70 < r < 255) and not (g > 220 and r > 80):
                px[i, j] = palatteColor[0]

    src.save('data/Imposter/temp/' + Path(path).name)

def makeImagePaletteSwap(paletteColor=data.PALETTE_DEFAULT) :
    for path in glob.glob('data/Imposter/defaults/*.png') :
        createModifiedSprites(path, paletteColor)

def delTempImage() :
    for path in glob.glob('data/Imposter/temp/*.png') :
        os.remove(path)

def mouseOnButton(button) :
    mouseX, mouseY = pygame.mouse.get_pos()

    if mouseX > button.rect.left and mouseX < button.rect.right and \
        mouseY > button.rect.top and mouseY < button.rect.bottom :
        return True
    else :
        return False

def getMask(image) :
    return pygame.mask.from_surface(image)

def isRedScreenTime(counter) :
    sbtgTime = int(counter / FPS)

    if (sbtgTime >= 0 and sbtgTime < 1) or \
        (sbtgTime >= 2 and sbtgTime < 3) or \
        (sbtgTime >= 4 and sbtgTime < 5) :

        return True
    else :
        return False
