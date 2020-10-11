import pygame, os
from pygame.compat import geterror

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
