# --------------------------------------------
# Author : KevOneRedOne
# Game Development with Pygame - Using a Raspberry Pi as an arcade game
#  
# Project Date : 16/05/2022 to 13/06/2022
# --------------------------------------------

import pygame as pg
import os
import sys
from settings import *


    
# ---------------------------------------------------------------------------                 
#          ----------- Drawing of the game -----------------  
# ---------------------------------------------------------------------------                 
                         
def draw_windows(plane_J1, plane_J2, J1_bullets, J1_missiles, J2_bullets,J2_missiles, J1_health, J2_health):
    # Draw Background
    SCREEN.blit(BACKGROUND_IMG, (0,0))
    # Draw Health 
    J1_health_text = HEALTH_FONT.render("HEALTH : " + str(J1_health), 1, WHITE)
    J2_health_text = HEALTH_FONT.render("HEALTH : " + str(J2_health), 1, WHITE)
    SCREEN.blit(J1_health_text, (10, 10))
    SCREEN.blit(J2_health_text, (WIDTH - J1_health_text.get_width()- 10, 10))
    # Draw planes
    SCREEN.blit(AIR_FIGHTER_J1, (plane_J1.x, plane_J1.y))
    SCREEN.blit(AIR_FIGHTER_J2, (plane_J2.x, plane_J2.y))
     
    # Draw bullets
    for bullet in J1_bullets:
        pg.draw.rect(SCREEN, RED, bullet )     
    for bullet in J2_bullets:
        pg.draw.rect(SCREEN, BLUE, bullet )  
          
    # Draw missiles
    for missile in J1_missiles:
        pg.draw.rect(SCREEN, MAGENTA, missile)
    for missile in J2_missiles:
        pg.draw.rect(SCREEN, CYAN, missile)
 
    # Update the screen  
    pg.display.update()
    
    
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    SCREEN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGTH/2 - draw_text.get_height()/2))
    pg.display.update()
    pg.time.delay(13000)
    
# ---------------------------------------------------------------------------                 
#          ----------- J1 and J2 Movement -----------------  
# ---------------------------------------------------------------------------                 
                
def J1_handle_movement(keys_pressed, plane_J1):
    if keys_pressed[pg.K_q] and plane_J1.x - VELOCITY > 0 : #left
        plane_J1.x -= VELOCITY   
    if keys_pressed[pg.K_d] and plane_J1.x + VELOCITY + plane_J1.height < WIDTH : #right
        plane_J1.x += VELOCITY   
    if keys_pressed[pg.K_z] and plane_J1.y - VELOCITY > 0 : #up
        plane_J1.y -= VELOCITY   
    if keys_pressed[pg.K_s] and plane_J1.y + VELOCITY + plane_J1.width < HEIGTH : #down
        plane_J1.y += VELOCITY  
        
def J2_handle_movement(keys_pressed, plane_J2):
    if keys_pressed[pg.K_LEFT] and plane_J2.x - VELOCITY > 0 : #left
        plane_J2.x -= VELOCITY   
    if keys_pressed[pg.K_RIGHT] and plane_J2.x + VELOCITY + plane_J2.height < WIDTH : #right
        plane_J2.x += VELOCITY   
    if keys_pressed[pg.K_UP] and plane_J2.y - VELOCITY > 0 : #up
        plane_J2.y -= VELOCITY   
    if keys_pressed[pg.K_DOWN] and plane_J2.y + VELOCITY + plane_J2.width < HEIGTH : #down
        plane_J2.y += VELOCITY    

# TO DO :
# - Add the rotation left and right for planes   


        
# ---------------------------------------------------------------------------                 
#          -----------Bullets and Missiles collisions -----------------  
# ---------------------------------------------------------------------------                 
def handle_bullets(J1_bullets, J2_bullets, plane_J1, plane_J2):
    for bullet in J1_bullets:
        bullet.x += BULLET_VELOCITY
        if plane_J2.colliderect(bullet):
            pg.event.post(pg.event.Event(PLANE_J2_HIT_BY_BULLETS))
            J1_bullets.remove(bullet)
        elif bullet.x > WIDTH :
            J1_bullets.remove(bullet)
            
    for bullet in J2_bullets:
        bullet.x -= BULLET_VELOCITY
        if plane_J1.colliderect(bullet):
            pg.event.post(pg.event.Event(PLANE_J1_HIT_BY_BULLETS))
            J2_bullets.remove(bullet)
        elif bullet.x < 0 :
            J2_bullets.remove(bullet)
            
def handle_missiles(J1_missiles, J2_missiles, plane_J1, plane_J2):
    for missile in J1_missiles:
        missile.x += MISSILES_VELOCITY
        if plane_J2.colliderect(missile):
            pg.event.post(pg.event.Event(PLANE_J2_HIT_BY_MISSILES))
            J1_missiles.remove(missile)
        elif missile.x > WIDTH :
            J1_missiles.remove(missile)
            
    for missile in J2_missiles:
        missile.x -= MISSILES_VELOCITY
        if plane_J1.colliderect(missile):
            pg.event.post(pg.event.Event(PLANE_J1_HIT_BY_MISSILES))
            J2_missiles.remove(missile)
        elif missile.x < 0 :
            J2_missiles.remove(missile)
            
            
# ---------------------------------------------------------------------------                 
#           -----------------Main function --------------------------  
# ---------------------------------------------------------------------------                 
                     
def main():
    GAME_SOUND.play()
    GAME_SOUND.set_volume(0.3)
    
    plane_J1 = pg.Rect(100,350, PLANE_WIDTH, PLANE_HEIGHT)
    plane_J2 = pg.Rect(848,350, PLANE_WIDTH, PLANE_HEIGHT)
    
    J1_health = 100
    J2_health = 100

    J1_bullets = []
    J1_missiles= []
    J2_bullets = []
    J2_missiles = []
    
    clock = pg.time.Clock()
    playing = True
    while playing :
        clock.tick(FPS)
        for event in pg.event.get():
            # Quit the Game
            if event.type == pg.QUIT :
                playing = False
                pg.quit()
            # Keyboard Event
            if event.type == pg.KEYDOWN:    
                if event.key == pg.K_LCTRL and len(J1_bullets) < MAX_BULLETS:
                    bullet = pg.Rect(plane_J1.x + plane_J1.width, plane_J1.y + plane_J1.height//2 - 10, 10, 2)
                    J1_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    BULLET_FIRE_SOUND.set_volume(0.3)
                if event.key == pg.K_LALT and len(J1_missiles) < MAX_MISSILES:
                    missile = pg.Rect(plane_J1.x-25 + plane_J1.width, plane_J1.y + plane_J1.height//2 - 30, 25, 4)
                    J1_missiles.append(missile)
                    MISSILE_FIRE_SOUND.play()
                    MISSILE_FIRE_SOUND.set_volume(0.3)
                    
                if event.key == pg.K_RCTRL and len(J2_bullets) < MAX_BULLETS:
                    bullet = pg.Rect(plane_J2.x-40 + plane_J2.width, plane_J2.y + plane_J2.height//2 - 10, 10, 2)
                    J2_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    BULLET_FIRE_SOUND.set_volume(0.3)
                if event.key == pg.K_RSHIFT and len(J2_missiles) < MAX_MISSILES:
                    missile = pg.Rect(plane_J2.x-25 + plane_J2.width, plane_J2.y + plane_J2.height//2 - 30, 25, 4)
                    J2_missiles.append(missile)
                    MISSILE_FIRE_SOUND.play()
                    MISSILE_FIRE_SOUND.set_volume(0.3)
                           
            if event.type == PLANE_J1_HIT_BY_BULLETS:
                J1_health -= 5
                BULLET_HIT_SOUND.play()
                BULLET_HIT_SOUND.set_volume(0.3)
                
            if event.type == PLANE_J1_HIT_BY_MISSILES:
                J1_health -= 15
                MISSILE_HIT_SOUND.play()
                MISSILE_HIT_SOUND.set_volume(0.3)
                               
            if event.type == PLANE_J2_HIT_BY_BULLETS:               
                J2_health -= 5
                BULLET_HIT_SOUND.play()
                BULLET_HIT_SOUND.set_volume(0.3)
                
            if event.type == PLANE_J2_HIT_BY_MISSILES:               
                J2_health -= 15
                MISSILE_HIT_SOUND.play()
                MISSILE_HIT_SOUND.set_volume(0.3)
                
                              
        winner_text =""                 
        if J1_health <= 0 :
            winner_text = "Player 2 wins !"
            GAME_SOUND.stop()
            VICTORY_SOUND.play()
            VICTORY_SOUND.set_volume(0.5)
            
        if J2_health <= 0 :
            winner_text = "Player 1 wins !"
            GAME_SOUND.stop()
            VICTORY_SOUND.play()
            VICTORY_SOUND.set_volume(0.5)
        
        if winner_text != "":
            draw_winner(winner_text)
            break
            
            
        keys_pressed = pg.key.get_pressed()
        J1_handle_movement(keys_pressed, plane_J1)
        J2_handle_movement(keys_pressed, plane_J2)
        
        handle_bullets(J1_bullets, J2_bullets, plane_J1, plane_J2)
        handle_missiles(J1_missiles, J2_missiles, plane_J1, plane_J2)
                  
        draw_windows(plane_J1, plane_J2, J1_bullets,J1_missiles, J2_bullets, J2_missiles, J1_health, J2_health)  
    
    # Restart the game 
    main()
       
        
    
if __name__ == "__main__":
    main()



# class Game:
#     def __init__(self):
#         pg.init()
#         self.screen = pg.display.set_mode((WITDH, HEIGTH))
#         pg.display.set_caption(TITLE)
#         self.clock = pg.time.Clock()
        
        
#     def play (self):
#         self.playing = True
    


# Game.play(self)

# ----------Start The Game -----------
# g = Game()
# g.show_start_screen()
# while True:
#     g.new()
#     g.play()
#     g.show_go_screen()