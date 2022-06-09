import pygame as pg
# --------------------------------------------------------------                
#          ----------- GAME SETTINGS -----------------  
# --------------------------------------------------------------   
WIDTH = 1024 # 16 * 64 / 32 * 32 / 64 * 16
HEIGTH = 768 # 16 * 48 / 32 * 24 / 64 * 12
GAME_NAME = "TopGun_Fighter"
SCREEN = pg.display.set_mode((WIDTH,HEIGTH))
TITLE =  pg.display.set_caption(GAME_NAME)
BACKGROUND_IMG = pg.transform.scale(pg.image.load('assets/images/wallpaper/bg55.png'), (WIDTH, HEIGTH))
# BACKGROUND_MENU = pg.transform.scale(pg.image.load('assets/images/wallpaper/bg55.png'), (WIDTH, HEIGTH))
# BACKGROUND_IMG = pg.transform.scale(pg.image.load('assets/images/wallpaper/bg6.png'), (WIDTH, HEIGTH))
# BACKGROUND_MENU = pg.transform.scale(pg.image.load('assets/images/wallpaper/bg6.png'), (WIDTH, HEIGTH))
FPS = 60

# score P1 et P2
# SCORE = [0, 0]


#======================== Font =========================
pg.font.init()
# MENU_FONT = pg.font.Font('assets/font/TOP_GUN.ttf', 50)
SCORE_FONT = pg.font.Font('assets/font/CarbonBlock.ttf', 25)
PLAYER_FONT = pg.font.Font('assets/font/CarbonBlock.ttf', 15)
WINNER_FONT = pg.font.Font('assets/font/CarbonBlock.ttf', 100)


#==================== Sound Effect =====================
pg.mixer.init()
# Game sound
GAME_SOUND =  pg.mixer.Sound('assets/sound/DangerZone.mp3')
VICTORY_SOUND =  pg.mixer.Sound('assets/sound/greeting.mp3')

# Missile and bullet
BULLET_FIRE_SOUND = pg.mixer.Sound('assets/sound/shoot.mp3')
BULLET_HIT_SOUND = pg.mixer.Sound('assets/sound/shoothit.mp3')
MISSILE_FIRE_SOUND = pg.mixer.Sound('assets/sound/missile.mp3')
MISSILE_HIT_SOUND = pg.mixer.Sound('assets/sound/missilehit.wav')



# --------------------------------------------------------------               
#          ----------- PLANES SETTINGS -----------------  
# --------------------------------------------------------------   
#-------Size of the planes--------
PLANE_WIDTH, PLANE_HEIGHT = 70, 80
EXPLOSION_WIDTH, EXPLOSION_HEIGHT = 100, 100

#-----Load Images of planes-------
AIRCRAFT_F2_IMG = pg.transform.scale(pg.image.load('assets/images/planes/f-2.png'), (PLANE_WIDTH, PLANE_HEIGHT))
AIRCRAFT_F14_IMG = pg.transform.scale(pg.image.load('assets/images/planes/f-14.png'), (PLANE_WIDTH, PLANE_HEIGHT))
AIRCRAFT_F18_IMG = pg.transform.scale(pg.image.load('assets/images/planes/f-18.png'), (PLANE_WIDTH, PLANE_HEIGHT))
AIRCRAFT_F22_IMG = pg.transform.scale(pg.image.load('assets/images/planes/f-22.png'), (PLANE_WIDTH, PLANE_HEIGHT))
AIRCRAFT_RAFALE_IMG = pg.transform.scale(pg.image.load('assets/images/planes/rafale.png'), (PLANE_WIDTH, PLANE_HEIGHT))
AIRCRAFT_SU28_IMG = pg.transform.scale(pg.image.load('assets/images/planes/SU-28.png'), (PLANE_WIDTH, PLANE_HEIGHT))
AIRCRAFT_SU47_IMG = pg.transform.scale(pg.image.load('assets/images/planes/SU-47.png'), (PLANE_WIDTH, PLANE_HEIGHT))
AIRCRAFT_SU57_IMG = pg.transform.scale(pg.image.load('assets/images/planes/SU-57.png'), (PLANE_WIDTH, PLANE_HEIGHT))

AIRCRAFTS_IMGS = [
    AIRCRAFT_F2_IMG,
    AIRCRAFT_F14_IMG,
    AIRCRAFT_F18_IMG,
    AIRCRAFT_F22_IMG,
    AIRCRAFT_RAFALE_IMG,
    AIRCRAFT_SU28_IMG,
    AIRCRAFT_SU47_IMG,
    AIRCRAFT_SU57_IMG
]

AIRCRAFT_EXPLOSION = pg.transform.scale(pg.image.load('assets/images/missiles_bullets/explosion2.png'), (EXPLOSION_WIDTH,EXPLOSION_HEIGHT))

# --------------------------------------------------------------               
#          ------- Bullets and Missiles SETTINGS ------  
# --------------------------------------------------------------  
#-------Size of the weapons--------
BULLET_WIDTH, BULLET_HEIGHT = 25, 5
MISSILE_WIDTH, MISSILE_HEIGHT = 50, 10

#-----Load Images of weapons-------
BULLET1_IMG = pg.transform.scale(pg.image.load('assets/images/missiles_bullets/bullets.png'), (BULLET_WIDTH, BULLET_HEIGHT))
MISSILE1_IMG = pg.transform.scale(pg.image.load('assets/images/missiles_bullets/missile1.png'), (MISSILE_WIDTH, MISSILE_HEIGHT))
MISSILE2_IMG = pg.transform.scale(pg.image.load('assets/images/missiles_bullets/missile2.png'), (MISSILE_WIDTH, MISSILE_HEIGHT))
MISSILES_IMG = [
    MISSILE1_IMG, 
    MISSILE2_IMG
]
# --------Stats of weapons--------
MAX_BULLET = 7
MAX_MISSILE = 2
VELOCITY_BULLET = 6
VELOCITY_MISSILE = 7
BULLET_DAMAGE = 5
MISSILE_DAMAGE = 15
BULLET_POINT =  20
MISSILE_POINT = 40


# -------------------------------------------------------------           
#          ----------- COLOR SETTINGS -----------------  
# -------------------------------------------------------------
# RGB
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
CYAN = (0,255,255)
RED = (255,0,0)
MAGENTA = (255,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
ORANGE = pg.Color('orange')