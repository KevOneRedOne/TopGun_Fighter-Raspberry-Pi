import random
import pygame as pg
from settings import *

# --------------------------------------------------------------              
#        ----------- Drawing of the game -----------------  
# --------------------------------------------------------------  
# ------ Background ------
def draw_bg(SCREEN):
    SCREEN.blit(BACKGROUND_IMG, (0,0))

# ------ Health Bar ------
def draw_health_bar(health, x, y):
    ratio = health/100
    pg.draw.rect(SCREEN, WHITE, (x-2, y-2, 204, 24))
    pg.draw.rect(SCREEN, RED, (x, y, 200, 20))
    pg.draw.rect(SCREEN, GREEN, (x, y, 200*ratio, 20))

# ------ Draw text on the screen ------
def draw_text(text, font, text_col, x, y):
    texte_to_print = font.render(text, True, text_col)
    SCREEN.blit(texte_to_print, (x,y))

# ------ Draw winner text on the screen ------
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    SCREEN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGTH/2 - draw_text.get_height()/2))
    pg.display.update()
    pg.time.delay(3000)
    

# --------------------------------------------------------------               
#          -----------ROTATION IMG--------------  
# --------------------------------------------------------------
def blit_rotate_center(SCREEN, image, top_left, angle):
    rotated_image = pg.transform.rotate(image, angle)
    rotation_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    SCREEN.blit(rotated_image, rotation_rect)
    

# --------------------------------------------------------------               
#          ----------- J1 and J2 Movement ----------------  
# --------------------------------------------------------------
def J1_handle_movement(player1):
    keys_pressed = pg.key.get_pressed()
    player_moved = False
    #--------- rotation left ------------
    # Keyboard
    if keys_pressed[pg.K_q]:
        player1.rotate(left=True)         
    #--------- rotation right -----------    
    if keys_pressed[pg.K_d]:  
        player1.rotate(right=True)       
    #--------- PLAYER MOVE --------------
    if keys_pressed[pg.K_z]:
        player_moved=True
        # collsion with map
        if not player1.collide_map():
            player1.move_forward()
        elif player1.collide_map():
            player1.step_back()  
    #--------- PLAYER DOESN'T MOVE ---------- 
    if not player_moved:
        if not player1.collide_map():
            player1.reduce_speed()
        if player1.collide_map():
            player1.step_back()
        #--------IF PLAYER BLOCKED---------
        if player1.collide_map() and pg.time.delay(2000):
            player1.reset()
                        
def J2_handle_movement(player2):
    keys_pressed = pg.key.get_pressed()
    player_moved = False
    #--------- rotation left ------------
    if keys_pressed[pg.K_LEFT]: 
        player2.rotate(left=True)
    #--------- rotation right -----------    
    if keys_pressed[pg.K_RIGHT]:  
        player2.rotate(right=True)
        
    #--------- PLAYER MOVE --------------
    if keys_pressed[pg.K_UP]:
        player_moved=True
        # collsion with map
        if not player2.collide_map():
            player2.move_forward()
        elif player2.collide_map():
            player2.step_back()  
    #--------- PLAYER DOESN'T MOVE ---------- 
    if not player_moved:
        if not player2.collide_map():
            player2.reduce_speed()
        if player2.collide_map():
            player2.step_back()
        #--------IF PLAYER BLOCKED---------
        if player2.collide_map() and pg.time.delay(2000):
            player2.reset()
        
# --------------------------------------------------------------               
#          ----------- J1 and J2 JOYSTICK --------------  
# --------------------------------------------------------------
def J1_Joystick_movement(player1):
    axe_x_joy_left = round(CONTROLLER_J1.get_axis(0),2)
    axe_y_joy_right = round(CONTROLLER_J1.get_axis(3),2)
    #---------Left/Right------------
    if axe_x_joy_left < -0.1:
        player1.rotate(left=True)
    if axe_x_joy_left > 0.1:
        player1.rotate(right=True)

    #---------Move--------------
    if axe_y_joy_right < -0.1:
        player1.move_forward()
    if axe_y_joy_right > 0.1:
        player1.reduce_speed()
                          
def J2_Joystick_movement(player2):    
    axe_x_joy_left = round(CONTROLLER_J2.get_axis(0),2)
    axe_y_joy_right = round(CONTROLLER_J2.get_axis(3),2)
    #---------Left/Right------------
    if axe_x_joy_left < -0.1:
        player2.rotate(left=True)
    if axe_x_joy_left > 0.1:
        player2.rotate(right=True)
    #---------Move--------------
    if axe_y_joy_right < -0.1:
        player2.move_forward()
    if axe_y_joy_right > 0.1:
        player2.reduce_speed()


# ---------------------------------------------------------------------------                 
#          -----------Bullets/Missiles moves and collisions ------------  
# ---------------------------------------------------------------------------    
def handle_weapons(J1_bullets, J1_missiles, J2_bullets, J2_missiles, player1, player2):           
    # ------------------ Bullets J1 --------------------
    for bullet in J1_bullets:
        bullet.move_weapons()
        if bullet.rectangle.colliderect(player2.rect):
            J1_bullets.remove(bullet)
            #-------health and score--------
            player2.health -= bullet.damage
            player1.score += bullet.point * random.randint(1,5)
        elif bullet.collide_map():
            J1_bullets.remove(bullet)
            
    # ----------------- Missiles J1 --------------------
    for missile in J1_missiles:
        missile.move_weapons()
        if missile.rectangle.colliderect(player2.rect):
            J1_missiles.remove(missile)
            #-------health and score--------
            player2.health -= missile.damage
            player1.score += missile.point * random.randint(1,5)
        elif missile.collide_map():
            J1_missiles.remove(missile)

    # ------------------ Bullets J2 --------------------
    for bullet in J2_bullets:
        bullet.move_weapons()
        if bullet.rectangle.colliderect(player1.rect):
            J2_bullets.remove(bullet)
            #-------health and score--------
            player1.health -= bullet.damage
            player2.score += bullet.point * random.randint(1,5)
        elif bullet.collide_map():
            J2_bullets.remove(bullet)
            
    # ----------------- Missiles J2 --------------------
    for missile in J2_missiles:
        missile.move_weapons()
        if missile.rectangle.colliderect(player1.rect):
            J2_missiles.remove(missile)
            #-------health and score--------
            player1.health -= missile.damage
            player2.score += missile.point * random.randint(1,5)
        elif missile.collide_map():
            J2_missiles.remove(missile)
