# --------------------------------------------
# Author : KevOneRedOne
# Game Development with Pygame - Using a Raspberry Pi as an arcade game
# Game Name : TOPGUN_Fighter
# Project Date : 16/05/2022 to 13/06/2022
# --------------------------------------------

import pygame as pg
import pygame_menu
from aircraft_fighter import *
from settings import *
from utils import *
from score import *

# --------------------------------------------------------------                
#          ----------- MAIN MENU -----------------  
# --------------------------------------------------------------  
def mainMenu():
    pg.init()
    # setup the theme of the menu
    mainMenuTheme = pygame_menu.themes.THEME_DARK.copy()
    mainMenuTheme.background_color = pygame_menu.BaseImage(
        'assets/images/wallpaper/bg6.png')
    mainMenuTheme.title_background_color = (0, 0, 0, 0)
    mainMenuTheme.title_font = MENU_FONT
    mainMenuTheme.title_offset = (WIDTH/3, ((HEIGHT-HEIGHT) + 30 ))
    mainMenuTheme.widget_font = MENU_FONT
    mainMenuTheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    # instantiation
    mainMenu = pygame_menu.Menu(
        'T O P G U N   F i g h t e r s', WIDTH, HEIGHT, theme=mainMenuTheme)
    # add widget
    mainMenu.add.image(image_path='assets/images/TOPGUN.png', scale=(0.5, 0.5), scale_smooth=True, float=False)
    mainMenu.add.button('P l a y', game, font_color=RED)
    mainMenu.add.button('I n s t r u c t i o n s',instructionMenu,font_color=BLUE)
    mainMenu.add.button('S c o r e', menuScore, font_color=RED)
    mainMenu.add.button('O p t i o n s',optionMenu, font_color=BLUE)
    mainMenu.add.button('Q u i t', pygame_menu.events.EXIT, font_color=RED)
    # loop Menu
    mainMenu.mainloop(SCREEN)
    
# --------------------------------------------------------------                
#          ----------- INSTRUCTION MENU -----------------  
# -------------------------------------------------------------- 
def instructionMenu():
    pg.init()
    # setup the theme of the menu
    instructionMenuTheme = pygame_menu.themes.THEME_DARK.copy()
    instructionMenuTheme.background_color = pygame_menu.BaseImage(
        'assets/images/wallpaper/bg6.png')
    instructionMenuTheme.title_background_color = (0, 0, 0, 0)
    instructionMenuTheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    instructionMenuTheme.title_font = MENU_FONT
    instructionMenuTheme.title_color = WHITE
    instructionMenuTheme.title_offset = (WIDTH/2.45, ((HEIGHT-HEIGHT) + 30 ))
    instructionMenuTheme.widget_font = SCORE_FONT
    instructionMenuTheme.button_font = MENU_FONT
    # instantiation of the menu
    instructionMenu = pygame_menu.Menu('Instruction', WIDTH, HEIGHT, theme=instructionMenuTheme)
    # add widget
    instructionMenu.add.vertical_margin(50)
    instructionMenu.add.label(HELP_TITLE, font_color=BLUE, align=pygame_menu.locals.ALIGN_CENTER)
    instructionMenu.add.label(HELP_CONTENT, font_color=WHITE, align=pygame_menu.locals.ALIGN_CENTER)
    instructionMenu.add.label(HELP_CONTROL_TITLE, font_color=RED, background_color=(0,0,0,100), align=pygame_menu.locals.ALIGN_CENTER)
    instructionMenu.add.label(HELP_CONTROL_J1, font_color=WHITE, background_color=(0,0,0,100), align=pygame_menu.locals.ALIGN_CENTER)
    instructionMenu.add.vertical_margin(50)
    instructionMenu.add.button('P L A Y', game, font_color=RED, padding=(20, 20, 20, 20))
    instructionMenu.add.button('R E T U R N', mainMenu, font_color=RED, padding=(20, 20, 20, 20), border_width=0)
    # loop Menu
    instructionMenu.mainloop(SCREEN)

# --------------------------------------------------------------                
#          ----------- SCORE MENU -----------------  
# -------------------------------------------------------------- 
def menuScore():
    pg.init()
    
    # setup the theme of the menu
    ScoreMenuTheme = pygame_menu.themes.THEME_DARK.copy()
    ScoreMenuTheme.background_color = pygame_menu.BaseImage(
    'assets/images/wallpaper/bg55.png')
    ScoreMenuTheme.title_background_color = (0, 0, 0, 0)
    ScoreMenuTheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    ScoreMenuTheme.title_font = MENU_FONT
    ScoreMenuTheme.title_offset = (WIDTH/2.25, ((HEIGHT-HEIGHT) + 30 ))
    ScoreMenuTheme.widget_font = SCORE_FONT
    
    # instantiation of the menu
    ScoreMenu = pygame_menu.Menu('S C O R E', WIDTH, HEIGHT, theme=ScoreMenuTheme)
    
    # add widget
    ScoreMenu.add.label(getScores())  #ingrogress
    ScoreMenu.add.vertical_margin(100)
    ScoreMenu.add.button('R E T U R N', mainMenu, font_color=RED, padding=(20, 20, 20, 20), border_width=0)
    
    ScoreMenu.mainloop(SCREEN)

# --------------------------------------------------------------                
#          ----------- OPTION MENU -----------------  
# -------------------------------------------------------------- 
def optionMenu():
    pg.init()
    # setup the theme of the menu
    optionTheme = pygame_menu.themes.THEME_DARK.copy()
    optionTheme.background_color = pygame_menu.BaseImage(
    'assets/images/wallpaper/bg6.png')
    optionTheme.title_background_color = (0, 0, 0, 0)
    optionTheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    optionTheme.title_font = MENU_FONT
    optionTheme.title_offset = (WIDTH/2.3, ((HEIGHT-HEIGHT) + 30 ))
    optionTheme.widget_font = MENU_FONT

    Option_Menu = pygame_menu.Menu('O P T I O N', WIDTH, HEIGHT, theme=optionTheme)
    
    # in progress
    Option_Menu.add.button('R E T U R N', mainMenu, font_color=RED, padding=(20, 20, 20, 20), border_width=0)
    Option_Menu.mainloop(SCREEN)

# --------------------------------------------------------------             
#       -----------------Main function -------------------  
# -------------------------------------------------------------- 
def main(): 
    mainMenu()

# --------------------------------------------------------------             
#       -----------------Game function -------------------  
# -------------------------------------------------------------- 
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
    J1_bullets, J1_missiles = [] , []
    J2_bullets, J2_missiles = [] , []
    winner_text = ""
    
    while playing:
        clock.tick(FPS)
        for event in pg.event.get():
            # Quit the game
            if event.type == pg.QUIT:
                playing = False
                pg.joystick.quit()
                pg.quit()

            # Keyboard Event
            if event.type == pg.KEYDOWN:
                #-----------PLAYER 1-------------
                if event.key == pg.K_LSHIFT and len(J1_bullets) < MAX_BULLET:
                    J1_bullets.append(player1.shoot_bullet())
                    BULLET_FIRE_SOUND.play()
                    BULLET_FIRE_SOUND.set_volume(0.3)
                if event.key == pg.K_SPACE and len(J1_missiles) < MAX_MISSILE:
                    J1_missiles.append(player1.shoot_missile())
                    MISSILE_FIRE_SOUND.play()
                    MISSILE_FIRE_SOUND.set_volume(0.3)
                #-----------PLAYER 2-------------- 
                if event.key == pg.K_RCTRL and len(J2_bullets) < MAX_BULLET:
                    J2_bullets.append(player2.shoot_bullet())
                    BULLET_FIRE_SOUND.play()
                    BULLET_FIRE_SOUND.set_volume(0.3)
                if event.key == pg.K_RSHIFT and len(J2_missiles) < MAX_MISSILE:
                    J2_missiles.append(player2.shoot_missile())
                    MISSILE_FIRE_SOUND.play()
                    MISSILE_FIRE_SOUND.set_volume(0.3)
                # Go back to the menu
                if event.key == pg.K_ESCAPE:
                    mainMenu()
                
            # Joystick
            if event.type == pg.JOYBUTTONDOWN:
                #-----------PLAYER 1-------------
                if CONTROLLER_J1.get_button(BUTTON_L1) and len(J1_bullets) < MAX_BULLET:
                    J1_bullets.append(player1.shoot_bullet())
                    BULLET_FIRE_SOUND.play()
                    BULLET_FIRE_SOUND.set_volume(0.3)
                elif CONTROLLER_J1.get_button(BUTTON_R1) and len(J1_missiles) < MAX_MISSILE:
                    J1_missiles.append(player1.shoot_missile())
                #-----------PLAYER 2-------------- 
                if CONTROLLER_J2.get_button(BUTTON_L1) and len(J2_bullets) < MAX_BULLET:
                    J2_bullets.append(player2.shoot_bullet())
                    BULLET_FIRE_SOUND.play()
                    BULLET_FIRE_SOUND.set_volume(0.3)
                elif CONTROLLER_J2.get_button(BUTTON_R1) and len(J2_missiles) < MAX_MISSILE:
                    J2_missiles.append(player2.shoot_missile())
                    MISSILE_FIRE_SOUND.play()
                    MISSILE_FIRE_SOUND.set_volume(0.3)
                    
                    
        #---------Draw the background---------------- 
        draw_bg(SCREEN)
        
        #---------Draw the health Bar----------------
        draw_health_bar(player1.health,10, 10)
        draw_health_bar(player2.health,815, 10)
        
        #---------Draw Score and Player --------------------
        draw_text("Score P1 : " + str(player1.score), SCORE_FONT, RED, 8, 40)
        draw_text("Score P2 : " + str(player2.score), SCORE_FONT, BLUE, 813, 40)
        
        draw_text("P.1", PLAYER_FONT, RED, player1.x, player1.y)
        draw_text("P.2", PLAYER_FONT, BLUE, player2.x, player2.y)
            
        #---------Draw the Aircraft-----------------
        Player1.draw(player1,SCREEN)
        Player2.draw(player2,SCREEN)
        
        #---------Setup the player's movement--------
        J1_handle_movement(player1)
        J2_handle_movement(player2)
        
        if pg.joystick.get_count() > 0:
            J1_Joystick_movement(player1)
            
        if pg.joystick.get_count() > 1:
            J1_Joystick_movement(player1)
            J2_Joystick_movement(player2)
        
        # --------Setup the weapon's movement and collision-----------
        handle_weapons(J1_bullets, J1_missiles, J2_bullets, J2_missiles, player1, player2)
        
        
        if player1.health <= 0 :
            winner_text = "Player 2 wins !"
            player1.set_explosion(AIRCRAFT_EXPLOSION) 
            Player1.draw(player1,SCREEN)   
            saveScore("Player 2", player2.score)
            GAME_SOUND.stop()
            VICTORY_SOUND.play()
            VICTORY_SOUND.set_volume(0.5)
        elif player2.health <= 0 :
            winner_text = "Player 1 wins !"
            player2.set_explosion(AIRCRAFT_EXPLOSION) 
            Player2.draw(player2,SCREEN)     
            saveScore("Player 1", player1.score)
            GAME_SOUND.stop()
            VICTORY_SOUND.play()
            VICTORY_SOUND.set_volume(0.5)
        
        if winner_text != "":
            draw_winner(winner_text)
            menuScore()
        
        
        #---------Update the screen--------------
        pg.display.update()
    
        

if __name__ == '__main__':
    main()
    