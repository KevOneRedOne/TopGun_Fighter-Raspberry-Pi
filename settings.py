import pygame as pg
# --------------------------------------------------------------                
#          ----------- GAME SETTINGS -----------------  
# --------------------------------------------------------------   
WIDTH = 1024 # 16 * 64 / 32 * 32 / 64 * 16
HEIGHT = 768 # 16 * 48 / 32 * 24 / 64 * 12
GAME_NAME = "TopGun_Fighter"
SCREEN = pg.display.set_mode((WIDTH,HEIGHT))
TITLE =  pg.display.set_caption(GAME_NAME)
BACKGROUND_IMG = pg.transform.scale(pg.image.load('assets/images/wallpaper/bg55.png'), (WIDTH, HEIGHT))
BACKGROUND_MENU = pg.transform.scale(pg.image.load('assets/images/wallpaper/bg6.png'), (WIDTH, HEIGHT))
TOP_GUN_LOGO = pg.transform.scale(pg.image.load('assets/images/TOPGUN.png'), (100, 100))
FPS = 60

#======================== Font =========================
pg.font.init()
MENU_FONT = pg.font.Font('assets/font/TOP_GUN.ttf', 35)
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

#==================== Controllers =====================
pg.joystick.init()

# axis and buttons
AXIS_J1 = {}
AXIS_J2 = {}

# Labels for DS4 controller axes
# -------------AXIS--------------
AXIS_LEFT_STICK_X = 0
AXIS_LEFT_STICK_Y = 1
AXIS_RIGHT_STICK_X = 2
AXIS_RIGHT_STICK_Y = 3

# ------------Button-------------
BUTTON_CROSS = 0
BUTTON_CIRCULE = 1
BUTTON_SQUARE = 2
BUTTON_TRIANGLE = 3
BUTTON_L1 = 9
BUTTON_R1 = 10

# Count the number of Joystick
JOYSTICK_COUNT = pg.joystick.get_count()
print("Number of joysticks: " + str(JOYSTICK_COUNT))

CONTROLLER_J1 = None
CONTROLLER_J2 = None

if JOYSTICK_COUNT > 0:
    CONTROLLER_J1 = pg.joystick.Joystick(0)
    CONTROLLER_J1.init()
    print("Player 1 controller : " + str(CONTROLLER_J1))
    print("Player 1 controller ID : " + str(CONTROLLER_J1.get_id()))
    
if JOYSTICK_COUNT > 1:
    CONTROLLER_J2 = pg.joystick.Joystick(1)
    CONTROLLER_J2.init()
    print("Player 2 controller : " + str(CONTROLLER_J2))
    print("Player 2 controller ID : " + str(CONTROLLER_J2.get_id()))
    

# CONTROLLER_J1 = pg.joystick.Joystick(0)
# CONTROLLER_J2 = pg.joystick.Joystick(1)
# CONTROLLER_J1.init()    
# CONTROLLER_J2.init()
# print("Player 1 controller : " + str(CONTROLLER_J1))
# print("Player 1 controller ID : " + str(CONTROLLER_J1.get_id()))
# print("Player 2 controller : " + str(CONTROLLER_J2))
# print("Player 2 controller ID : " + str(CONTROLLER_J2.get_id()))
        
# ==================== Keyboard Controls =====================
# Define keys for player 1
PLAYER1_KEYS = {
    'left': pg.K_LEFT,
    'right': pg.K_RIGHT,
    'up': pg.K_UP,
    'down': pg.K_DOWN,
    'shoot_bullet': pg.K_SPACE,
    'shoot_missile': pg.K_LSHIFT
}

# Define keys for player 2
PLAYER2_KEYS = {
    'left': pg.K_a,
    'right': pg.K_d,
    'up': pg.K_w,
    'down': pg.K_s,
    'shoot_bullet': pg.K_LCTRL,
    'shoot_missile': pg.K_RSHIFT
}

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

AIRCRAFT_IMGS = [
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
#          ----------- MENU -----------------  
# -------------------------------------------------------------
HELP_TITLE = "DEROULEMENT D'UNE PARTIE :"
HELP_CONTENT = "\nIL S'AGIT D'UN JEU DE COMBAT AERIEN EN 1 CONTRE 1 (P1 VS P2). \nL'OBJECTIF POUR LES 2 JOUEURS SERA DE DETRUIRE L'ADVERSAIRE.\nCHAQUE JOUEUR PEUT TIRER : DES MISSILES (15 DEGATS/40 POINTS) OU DES BULLETS (5 DEGATS/20 POINTS).\n\n"
HELP_CONTROL_TITLE = "CONTROLE :"
HELP_CONTROL_J1 = "**JOUEUR 1** : LA MANETTE AVEC LE *JOYSTICK GAUCHE* POUR TOURNER, *JOYSTICK DROIT* POUR AVANCER\nAVEC *L1* (TIR BULLET) / et *R1* (TIR MISSILE)\n"\
    " ET/OU CLAVIERS : *Z-Q-D* POUR LA DIRECTION, *ESPACE* (BULLET) ET *SHIFT GAUCHE* (MISSILE)\n"\
    "**JOUEUR 2** : LA MANETTE AVEC LE *JOYSTICK GAUCHE* POUR TOURNER, *JOYSTICK DROIT* POUR AVANCER\nAVEC *L1* (TIR BULLET) / et *R1* (TIR MISSILE)\n"\
    "   ET/OU CLAVIERS : *FLECHES DIRECTIONS*, *CTRL DROIT* (BULLET) ET *SHIFT DROIT* (MISSILE)"



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