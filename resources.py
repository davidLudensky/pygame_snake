import pygame

BG_IMAGE = 'images/hodaya/padam.jpeg'

ICON_PATH = "images/snake/snake-icon-32x32.png"

EASY = 2
MEDIUM = 4
HARD = 6
IMPOSSIBLE = 8

DIRECTION_TO_MOVEMENT = {
    'left': [-1, 0],
    'right': [1, 0],
    'up': [0, -1],
    'down': [0, 1]
}

KEY_STROKE_TO_DIRECTION = {
    pygame.K_LEFT: 'left',
    pygame.K_RIGHT: 'right',
    pygame.K_UP: 'up',
    pygame.K_DOWN: 'down'
}

IMAGES_DICT = {
    'apple': "images/snake/50percent/apple.png",
    'head right': "images/snake/50percent/snake-head-right.png",
    'head left': "images/snake/50percent/snake-head-left.png",
    'head up': "images/snake/50percent/snake-head-up.png",
    'head down': "images/snake/50percent/snake-head-down.png",
    'body horizontal': "images/snake/50percent/snake-body-horizontal.png",
    'body vertical': "images/snake/50percent/snake-body-vertical.png",
    'body right to up': "images/snake/50percent/right2up-or-down2left.png",
    'body right to down': "images/snake/50percent/right2down-or-up2left.png",
    'body left to up': "images/snake/50percent/left2up-or-down2right.png",
    'body left to down': "images/snake/50percent/left2down-or-up2right.png",
    'body up to right': "images/snake/50percent/left2down-or-up2right.png",
    'body up to left': "images/snake/50percent/right2down-or-up2left.png",
    'body down to right': "images/snake/50percent/left2up-or-down2right.png",
    'body down to left': "images/snake/50percent/right2up-or-down2left.png",
    'tail right': "images/snake/50percent/snake-tail-right.png",
    'tail left': "images/snake/50percent/snake-tail-left.png",
    'tail up': "images/snake/50percent/snake-tail-up.png",
    'tail down': "images/snake/50percent/snake-tail-down.png",
}

HEAD_PART_INDEX = 0
REGULAR_PART_INDEX = 1
TAIL_PART_INDEX = 2

DIRECTIONS_TO_SURFACE_NAMES = {
    'right->right': ['head right', 'body horizontal', 'tail right'],
    'right->up': ['head up', 'body right to up', 'tail up'],
    'right->down': ['head down', 'body right to down', 'tail down'],
    'left->left': ['head left', 'body horizontal', 'tail left'],
    'left->up': ['head up', 'body left to up', 'tail up'],
    'left->down': ['head down', 'body left to down', 'tail down'],
    'up->up': ['head up', 'body vertical', 'tail up'],
    'up->left': ['head left', 'body up to left', 'tail left'],
    'up->right': ['head right', 'body up to right', 'tail right'],
    'down->down': ['head down', 'body vertical', 'tail down'],
    'down->left': ['head left', 'body down to left', 'tail left'],
    'down->right': ['head right', 'body down to right', 'tail right'],
}
