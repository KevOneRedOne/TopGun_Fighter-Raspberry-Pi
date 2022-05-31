import pygame as pg
import os

# ------------Game settings -----------------
WIDTH = 1024 # 16 * 64 / 32 * 32 / 64 * 16
HEIGTH = 768 # 16 * 48 / 32 * 24 / 64 * 12
FPS = 60
GAME_NAME = "TopGun_Fighter"
SCREEN = pg.display.set_mode((WIDTH,HEIGTH))
TITLE =  pg.display.set_caption(GAME_NAME)

BACKGROUND_IMG = pg.transform.scale(pg.image.load(os.path.join('assets\images', 'bg55.png')), (WIDTH, HEIGTH))
# BACKGROUND_IMG = pg.transform.scale(pg.image.load(os.path.join('assets\images', 'bg6.png')), (WIDTH, HEIGTH))

# ------------Planes settings----------------
# Import Assets Planes
AIR_FIGHTER_J1_IMG = pg.image.load(os.path.join('assets\images', 'Plane1.png'))
AIR_FIGHTER_J2_IMG = pg.image.load(os.path.join('assets\images', 'Plane3.png'))

# Custom Width and heigth
PLANE_WIDTH, PLANE_HEIGHT = 50, 70

# Rotation of the Image
ROTATION_J1 = 270
ROTATION_J2 = 90

# Custom size and rotation of the plane
AIR_FIGHTER_J1 = pg.transform.rotate(pg.transform.scale(AIR_FIGHTER_J1_IMG, (PLANE_WIDTH, PLANE_HEIGHT)), ROTATION_J1 )
AIR_FIGHTER_J2 = pg.transform.rotate(pg.transform.scale(AIR_FIGHTER_J2_IMG, (PLANE_WIDTH, PLANE_HEIGHT)), ROTATION_J2 )

# Planes speed
VELOCITY = 5
# Missiles speed
BULLET_VELOCITY = 5
MISSILES_VELOCITY = 3
# Max missiles/shoot
MAX_BULLETS = 6
MAX_MISSILES = 1

PLANE_J1_HIT = pg.USEREVENT + 1
PLANE_J2_HIT = pg.USEREVENT + 2




#------------Some Colors---------------------
# RGB
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
CYAN = (0,255,255)
RED = (255,0,0)
MAGENTA = (255,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
