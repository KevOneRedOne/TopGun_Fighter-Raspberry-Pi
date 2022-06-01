import pygame as pg
import os

# ---------------------------------------------------------------------------                 
#          ----------- GAME SETTINGS -----------------  
# ---------------------------------------------------------------------------   
WIDTH = 1024 # 16 * 64 / 32 * 32 / 64 * 16
HEIGTH = 768 # 16 * 48 / 32 * 24 / 64 * 12
FPS = 60
GAME_NAME = "TopGun_Fighter"
SCREEN = pg.display.set_mode((WIDTH,HEIGTH))
TITLE =  pg.display.set_caption(GAME_NAME)

BACKGROUND_IMG = pg.transform.scale(pg.image.load(os.path.join('assets\images\wallpaper', 'bg55.png')), (WIDTH, HEIGTH))
# BACKGROUND_IMG = pg.transform.scale(pg.image.load(os.path.join('assets\images', 'bg6.png')), (WIDTH, HEIGTH))

#----------Font------------- 
pg.font.init()
# MENU_FONT = pg.font.Font('assets\\font\\TOP_GUN.ttf', 100)
HEALTH_FONT = pg.font.Font('assets\\font\\CarbonBlock.ttf',30)
WINNER_FONT = pg.font.Font('assets\\font\\CarbonBlock.ttf',100)


# -------Sound Effect------
pg.mixer.init()
# Game sound
GAME_SOUND =  pg.mixer.Sound(os.path.join('assets\sound', 'DangerZone.mp3'))
VICTORY_SOUND =  pg.mixer.Sound(os.path.join('assets\sound', 'greeting.mp3'))

# Missile and bullet
BULLET_FIRE_SOUND = pg.mixer.Sound(os.path.join('assets\sound', 'shoot.mp3'))
BULLET_HIT_SOUND = pg.mixer.Sound(os.path.join('assets\sound', 'shoothit.mp3'))
MISSILE_FIRE_SOUND = pg.mixer.Sound(os.path.join('assets\sound', 'missile.mp3'))
MISSILE_HIT_SOUND = pg.mixer.Sound(os.path.join('assets\sound', 'missilehit.wav'))


# ---------------------------------------------------------------------------                 
#          ----------- PLANES SETTINGS -----------------  
# ---------------------------------------------------------------------------   
# Import Assets Planes
AIR_FIGHTER_J1_IMG = pg.image.load(os.path.join('assets\images\planes', 'f-14.png'))
AIR_FIGHTER_J2_IMG = pg.image.load(os.path.join('assets\images\planes', 'SU-57.png'))

# Custom Width and heigth 
PLANE_WIDTH, PLANE_HEIGHT = 80, 90

# Rotation of the Image
ROTATION_J1 = 270
ROTATION_J2 = 90

# Custom size and rotation of the plane
AIR_FIGHTER_J1 = pg.transform.rotate(pg.transform.scale(AIR_FIGHTER_J1_IMG, (PLANE_WIDTH, PLANE_HEIGHT)), ROTATION_J1 )
AIR_FIGHTER_J2 = pg.transform.rotate(pg.transform.scale(AIR_FIGHTER_J2_IMG, (PLANE_WIDTH, PLANE_HEIGHT)), ROTATION_J2 )

# Planes speed
VELOCITY = 5
# Missiles and bullets speeds
BULLET_VELOCITY = 5
MISSILES_VELOCITY = 3
MAX_BULLETS = 6
MAX_MISSILES = 1


# ----------- Events priority-----------------
PLANE_J1_HIT_BY_BULLETS = pg.USEREVENT + 1
PLANE_J1_HIT_BY_MISSILES = pg.USEREVENT + 2
PLANE_J2_HIT_BY_BULLETS = pg.USEREVENT + 4
PLANE_J2_HIT_BY_MISSILES = pg.USEREVENT + 5



# ---------------------------------------------------------------------------                 
#          ----------- COLOR SETTINGS -----------------  
# ---------------------------------------------------------------------------   
# RGB
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
CYAN = (0,255,255)
RED = (255,0,0)
MAGENTA = (255,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
