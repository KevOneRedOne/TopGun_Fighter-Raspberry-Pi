import pygame as pg
import pygame_menu
from aircraft_fighter import Player1, Player2
from score import getScores, saveScore
from settings import AIRCRAFT_EXPLOSION, BULLET_FIRE_SOUND, BUTTON_L1, BUTTON_R1, CONTROLLER_J1, CONTROLLER_J2, FPS, GAME_SOUND, MAX_BULLET, MAX_MISSILE, MISSILE_FIRE_SOUND, PLAYER_FONT, VICTORY_SOUND, WIDTH, HEIGHT, MENU_FONT, RED, BLUE, WHITE, HELP_TITLE, HELP_CONTENT, HELP_CONTROL_TITLE, HELP_CONTROL_J1, SCORE_FONT, SCREEN
from utils import j1_joystick_movement, j1_handle_movement, j2_joystick_movement, j2_handle_movement, draw_bg, draw_health_bar, draw_text, draw_winner, handle_weapons

# --------------------------------------------------------------                
#          ----------- MAIN MENU -----------------  
# --------------------------------------------------------------  
def main_menu():
    pg.init()
    
    # setup the theme of the menu
    main_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    main_menu_theme.background_color = pygame_menu.BaseImage('assets/images/wallpaper/bg6.png')
    main_menu_theme.title_background_color = (0, 0, 0, 0)
    main_menu_theme.title_font = MENU_FONT
    main_menu_theme.title_offset = (WIDTH/3, (30))
    main_menu_theme.widget_font = MENU_FONT
    main_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    
    # instantiation
    main_menu = pygame_menu.Menu('T O P G U N   F i g h t e r s', WIDTH, HEIGHT, theme=main_menu_theme)
    
    # add widget
    main_menu.add.image(image_path='assets/images/TOPGUN.png', scale=(0.5, 0.5), scale_smooth=True, float=False)
    main_menu.add.button('P l a y', game, font_color=RED)
    main_menu.add.button('I n s t r u c t i o n s',instruction_menu,font_color=BLUE)
    main_menu.add.button('S c o r e', menu_score, font_color=RED)
    main_menu.add.button('O p t i o n s',option_menu, font_color=BLUE)
    main_menu.add.button('Q u i t', pygame_menu.events.EXIT, font_color=RED)
    
    # loop Menu
    main_menu.mainloop(SCREEN)
    
# --------------------------------------------------------------                
#          ----------- INSTRUCTION MENU -----------------  
# -------------------------------------------------------------- 
def instruction_menu():
    pg.init()
    
    # setup the theme of the menu
    instruction_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    instruction_menu_theme.background_color = pygame_menu.BaseImage('assets/images/wallpaper/bg6.png')
    instruction_menu_theme.title_background_color = (0, 0, 0, 0)
    instruction_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    instruction_menu_theme.title_font = MENU_FONT
    instruction_menu_theme.title_color = WHITE
    instruction_menu_theme.title_offset = (WIDTH/2.45, (30))
    instruction_menu_theme.widget_font = SCORE_FONT
    instruction_menu_theme.button_font = MENU_FONT
    
    # instantiation of the menu
    instruction_menu = pygame_menu.Menu('Instruction', WIDTH, HEIGHT, theme=instruction_menu_theme)
    
    # add widget
    instruction_menu.add.vertical_margin(50)
    instruction_menu.add.label(HELP_TITLE, font_color=BLUE, align=pygame_menu.locals.ALIGN_CENTER)
    instruction_menu.add.label(HELP_CONTENT, font_color=WHITE, align=pygame_menu.locals.ALIGN_CENTER)
    instruction_menu.add.label(HELP_CONTROL_TITLE, font_color=RED, background_color=(0,0,0,100), align=pygame_menu.locals.ALIGN_CENTER)
    instruction_menu.add.label(HELP_CONTROL_J1, font_color=WHITE, background_color=(0,0,0,100), align=pygame_menu.locals.ALIGN_CENTER)
    instruction_menu.add.vertical_margin(50)
    instruction_menu.add.button('P L A Y', game, font_color=RED, padding=(20, 20, 20, 20))
    instruction_menu.add.button('R E T U R N', main_menu, font_color=RED, padding=(20, 20, 20, 20), border_width=0)
    
    # loop Menu
    instruction_menu.mainloop(SCREEN)

# --------------------------------------------------------------                
#          ----------- SCORE MENU -----------------  
# -------------------------------------------------------------- 
def menu_score():
    pg.init()
    
    # setup the theme of the menu
    score_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    score_menu_theme.background_color = pygame_menu.BaseImage('assets/images/wallpaper/bg55.png')
    score_menu_theme.title_background_color = (0, 0, 0, 0)
    score_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    score_menu_theme.title_font = MENU_FONT
    score_menu_theme.title_offset = (WIDTH/2.25, (30))
    score_menu_theme.widget_font = SCORE_FONT
    
    # instantiation of the menu
    score_menu = pygame_menu.Menu('S C O R E', WIDTH, HEIGHT, theme=score_menu_theme)
    
    # add widget
    score_menu.add.label(getScores())
    score_menu.add.vertical_margin(100)
    score_menu.add.button('R E T U R N', main_menu, font_color=RED, padding=(20, 20, 20, 20), border_width=0)
    
    score_menu.mainloop(SCREEN)

# --------------------------------------------------------------                
#          ----------- OPTION MENU -----------------  
# -------------------------------------------------------------- 
def option_menu():
    pg.init()
    
    # setup the theme of the menu
    option_theme = pygame_menu.themes.THEME_DARK.copy()
    option_theme.background_color = pygame_menu.BaseImage('assets/images/wallpaper/bg6.png')
    option_theme.title_background_color = (0, 0, 0, 0)
    option_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    option_theme.title_font = MENU_FONT
    option_theme.title_offset = (WIDTH/2.3, (30))
    option_theme.widget_font = MENU_FONT

    menu_option = pygame_menu.Menu('O P T I O N', WIDTH, HEIGHT, theme=option_theme)
    
    # in progress
    menu_option.add.button('R E T U R N', main_menu, font_color=RED, padding=(20, 20, 20, 20), border_width=0)
    menu_option.mainloop(SCREEN)

# --------------------------------------------------------------             
#       -----------------Main function -------------------  
# -------------------------------------------------------------- 
def main(): 
    main_menu()

# --------------------------------------------------------------             
#       -----------------Game function -------------------  
# -------------------------------------------------------------- 
def handle_keyboard_event(event, player1, player2, j1_bullets, j1_missiles, j2_bullets, j2_missiles):
    if event.key == pg.K_LSHIFT and len(j1_bullets) < MAX_BULLET:
        j1_bullets.append(player1.shoot_bullet())
        BULLET_FIRE_SOUND.play()
        BULLET_FIRE_SOUND.set_volume(0.3)
    if event.key == pg.K_SPACE and len(j1_missiles) < MAX_MISSILE:
        j1_missiles.append(player1.shoot_missile())
        MISSILE_FIRE_SOUND.play()
        MISSILE_FIRE_SOUND.set_volume(0.3)
    if event.key == pg.K_RCTRL and len(j2_bullets) < MAX_BULLET:
        j2_bullets.append(player2.shoot_bullet())
        BULLET_FIRE_SOUND.play()
        BULLET_FIRE_SOUND.set_volume(0.3)
    if event.key == pg.K_RSHIFT and len(j2_missiles) < MAX_MISSILE:
        j2_missiles.append(player2.shoot_missile())
        MISSILE_FIRE_SOUND.play()
        MISSILE_FIRE_SOUND.set_volume(0.3)
    if event.key == pg.K_ESCAPE:
        main_menu()

def handle_joystick_event(event, player1, player2, j1_bullets, j1_missiles, j2_bullets, j2_missiles):
    if CONTROLLER_J1.get_button(BUTTON_L1) and len(j1_bullets) < MAX_BULLET:
        j1_bullets.append(player1.shoot_bullet())
        BULLET_FIRE_SOUND.play()
        BULLET_FIRE_SOUND.set_volume(0.3)
    elif CONTROLLER_J1.get_button(BUTTON_R1) and len(j1_missiles) < MAX_MISSILE:
        j1_missiles.append(player1.shoot_missile())
    if CONTROLLER_J2.get_button(BUTTON_L1) and len(j2_bullets) < MAX_BULLET:
        j2_bullets.append(player2.shoot_bullet())
        BULLET_FIRE_SOUND.play()
        BULLET_FIRE_SOUND.set_volume(0.3)
    elif CONTROLLER_J2.get_button(BUTTON_R1) and len(j2_missiles) < MAX_MISSILE:
        j2_missiles.append(player2.shoot_missile())
        MISSILE_FIRE_SOUND.play()
        MISSILE_FIRE_SOUND.set_volume(0.3)
        
        
def handle_quit_game(event):
    if event.type == pg.QUIT:
        pg.joystick.quit()
        pg.quit()


def check_and_handle_winner(player1, player2):
    winner_text = ""
    
    if player1.health <= 0:
        winner_text = "Player 2 wins !"
        player1.set_explosion(AIRCRAFT_EXPLOSION) 
        Player1.draw(player1)   
        saveScore("Player 2", player2.score)
        GAME_SOUND.stop()
        VICTORY_SOUND.play()
        VICTORY_SOUND.set_volume(0.5)

    elif player2.health <= 0:
        winner_text = "Player 1 wins !"
        player2.set_explosion(AIRCRAFT_EXPLOSION) 
        Player2.draw(player2)     
        saveScore("Player 1", player1.score)
        GAME_SOUND.stop()
        VICTORY_SOUND.play()
        VICTORY_SOUND.set_volume(0.5)

    if winner_text != "":
        draw_winner(winner_text)
        menu_score()



def game():
    #-----Music of the Game
    GAME_SOUND.play(-1)
    GAME_SOUND.set_volume(0.3)
    #------ Set framerate ----------
    clock = pg.time.Clock()
    playing = True
    
    # ---- Instantiation Player -----
    player1 = Player1(3,3.5)
    player2 = Player2(3,3.5)
    
    # ------ Bullet/Missile ---------
    j1_bullets, j1_missiles = [] , []
    j2_bullets, j2_missiles = [] , []
    
    event_handlers = {
        pg.KEYDOWN: handle_keyboard_event,
        pg.JOYBUTTONDOWN: handle_joystick_event
    }
    
    while playing:
        clock.tick(FPS)
        
        for event in pg.event.get():
            handle_quit_game(event)
            
            
            event_handler = event_handlers.get(event.type)
            if event_handler:
                event_handler(event, player1, player2, j1_bullets, j1_missiles, j2_bullets, j2_missiles)
                    
        #---------Draw the background---------------- 
        draw_bg()
        
        #---------Draw the health Bar----------------
        draw_health_bar(player1.health,10, 10)
        draw_health_bar(player2.health,815, 10)
        
        #---------Draw Score and Player --------------------
        draw_text("Score P1 : " + str(player1.score), SCORE_FONT, RED, 8, 40)
        draw_text("Score P2 : " + str(player2.score), SCORE_FONT, BLUE, 813, 40)
        
        draw_text("P.1", PLAYER_FONT, RED, player1.x, player1.y)
        draw_text("P.2", PLAYER_FONT, BLUE, player2.x, player2.y)
            
        #---------Draw the Aircraft-----------------
        Player1.draw(player1)
        Player2.draw(player2)
        
        #---------Setup the player's movement--------
        j1_handle_movement(player1)
        j2_handle_movement(player2)
        
        if pg.joystick.get_count() > 0:
            j1_joystick_movement(player1)
            
        if pg.joystick.get_count() > 1:
            j1_joystick_movement(player1)
            j2_joystick_movement(player2)
        
        # --------Setup the weapon's movement and collision-----------
        handle_weapons(j1_bullets, j1_missiles, j2_bullets, j2_missiles, player1, player2)
        
        check_and_handle_winner(player1, player2)
        
        #---------Update the screen--------------
        pg.display.update()
    
        

if __name__ == '__main__':
    main()
    