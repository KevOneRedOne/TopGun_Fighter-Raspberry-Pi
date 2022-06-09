# --------------------------------------------
# Author : KevOneRedOne
# Game Development with Pygame - Using a Raspberry Pi as an arcade game
# Game Name : TOPGUN_Fighter
# Project Date : 16/05/2022 to 13/06/2022
# --------------------------------------------
import pygame as pg
from aircraft_fighter import *
from settings import *
from utils import *

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



# --------------------------------------------------------------               
#          ----------- J1 and J2 Movement ----------------  
# --------------------------------------------------------------
def J1_handle_movement(player1):
    keys_pressed = pg.key.get_pressed()
    player_moved = False
    #--------- rotation left ------------
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
            player1.score += bullet.point
        elif bullet.collide_map():
            J1_bullets.remove(bullet)
            
    # ----------------- Missiles J1 --------------------
    for missile in J1_missiles:
        missile.move_weapons()
        if missile.rectangle.colliderect(player2.rect):
            J1_missiles.remove(missile)
            #-------health and score--------
            player2.health -= missile.damage
            player1.score += missile.point
        elif missile.collide_map():
            J1_missiles.remove(missile)

    # ------------------ Bullets J2 --------------------
    for bullet in J2_bullets:
        bullet.move_weapons()
        if bullet.rectangle.colliderect(player1.rect):
            J2_bullets.remove(bullet)
            #-------health and score--------
            player1.health -= bullet.damage
            player2.score += bullet.point
        elif bullet.collide_map():
            J2_bullets.remove(bullet)
            
    # ----------------- Missiles J2 --------------------
    for missile in J2_missiles:
        missile.move_weapons()
        if missile.rectangle.colliderect(player1.rect):
            J2_missiles.remove(missile)
            #-------health and score--------
            player1.health -= missile.damage
            player2.score += missile.point
        elif missile.collide_map():
            J2_missiles.remove(missile)


# --------------------------------------------------------------             
#       -----------------Main function -------------------  
# -------------------------------------------------------------- 
def main(): 
    #------ Set framerate ----------
    clock = pg.time.Clock()
    playing = True
    # in_game = False
    
    # ---- Instantiation Player -----
    player1 = Player1(4,5)
    player2 = Player2(4,5)
    
    # ------ Bullet/Missile ---------
    J1_bullets, J1_missiles = [] , []
    J2_bullets, J2_missiles = [] , []
    winner_text = ""
    
    while playing:
        clock.tick(FPS)
        # while in_menu:
        #     clock.tick(FPS)
        # while in:
        #     clock.tick(FPS)
        # while in_game:
            # clock.tick(FPS)
        for event in pg.event.get():
            # Quit the game
            if event.type == pg.QUIT:
                playing = False
                pg.quit()
            # Keyboard Event
            if event.type == pg.KEYDOWN:
                #-----------PLAYER 1-------------
                if event.key == pg.K_LSHIFT and len(J1_bullets) < MAX_BULLET:
                    J1_bullets.append(player1.shoot_bullet())
                if event.key == pg.K_SPACE and len(J1_missiles) < MAX_MISSILE:
                    J1_missiles.append(player1.shoot_missile())
                #-----------PLAYER 2-------------- 
                if event.key == pg.K_RCTRL and len(J2_bullets) < MAX_BULLET:
                    J2_bullets.append(player2.shoot_bullet())
                if event.key == pg.K_RSHIFT and len(J2_missiles) < MAX_MISSILE:
                    J2_missiles.append(player2.shoot_missile())


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
            
        #---------Draw the Aircrafts-----------------
        Player1.draw(player1,SCREEN)
        Player2.draw(player2,SCREEN)
        
        #---------Setup the player's movement--------
        J1_handle_movement(player1)
        J2_handle_movement(player2)
     
        # --------Setup the weapon's movement and collision-----------
        handle_weapons(J1_bullets, J1_missiles, J2_bullets, J2_missiles, player1, player2)
        
        
        if player1.health <= 0 :
            winner_text = "Player 2 wins !"
            player1.set_explosion(AIRCRAFT_EXPLOSION)
            # GAME_SOUND.stop()
            # VICTORY_SOUND.play()
            # VICTORY_SOUND.set_volume(0.5)
            # break  
        elif player2.health <= 0 :
            winner_text = "Player 1 wins !"
            player2.set_explosion(AIRCRAFT_EXPLOSION)
            # draw_text(winner_text, WINNER_FONT, WHITE, (WIDTH/4), (HEIGTH/2 - 60))
            # GAME_SOUND.stop()
            # VICTORY_SOUND.play()
            # VICTORY_SOUND.set_volume(0.5)
        
        draw_text(winner_text, WINNER_FONT, WHITE, (WIDTH/4), (HEIGTH/2 - 60))
        # pg.time.delay(2000)
        
        # if winner_text != "":
            
        
        
        #---------Update the screen--------------
        pg.display.update()
        
    main()
        


if __name__ == '__main__':
    main()
    