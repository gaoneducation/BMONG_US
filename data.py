from pygame.locals import *

# Window Setting Values
TITLE = 'BMONG US'
DISPLAY_WIDTH = 960
DISPLAY_HEIGHT = 720
FPS = 30

LIMIT_LEFT = -10
LIMIT_RIGHT = DISPLAY_WIDTH - 10
LIMIT_TOP = -10
LIMIT_BOTTOM = DISPLAY_HEIGHT - 10

# Color Values
WHITE = (255,255,255)
BLACK = (0,0,0)

# Action Values
IDLE = 5
WALK_LEFT = 4 
WALK_RIGHT = 6
WALK_UP = 8
WALK_DOWN = 2
WALK = 11

MOVE_SPEED = 7

WALK_ANIMATION_FRAME = 12

# Background Values
BG_IDLE = 5
BG_MOVE_LEFT = 4
BG_MOVE_RIGHT = 6
BG_MOVE_UP = 8
BG_MOVE_DOWN = 2
BG_MOVE_SPEED = 5

# Face Side Value
FACE_LEFT = 4
FACE_RIGHT = 6

# Key Value
AVAILABLE_KEY = []