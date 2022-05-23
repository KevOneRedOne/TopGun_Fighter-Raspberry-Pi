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


# class Game:
#     def __init__(self):
#         pg.init()
#         self.screen = pg.display.set_mode((WITDH, HEIGTH))
#         pg.display.set_caption(TITLE)
#         self.clock = pg.time.Clock()
        
        
#     def play (self):
#         self.playing = True


    
                
def draw_windows(plane_J1, plane_J2, J1_bullets, J2_bullets):
    SCREEN.blit(BACKGROUND_IMG, (0,0))
    SCREEN.blit(AIR_FIGHTER_J1, (plane_J1.x, plane_J1.y))
    SCREEN.blit(AIR_FIGHTER_J2, (plane_J2.x, plane_J2.y))
    
    for bullet in J1_bullets:
        pg.draw.rect(SCREEN, RED, bullet )    
    
    for bullet in J2_bullets:
        pg.draw.rect(SCREEN, BLUE, bullet )    
        
    pg.display.update()
                
def J1_handle_movement(keys_pressed, plane_J1):
    if keys_pressed[pg.K_q] and plane_J1.x - VELOCITY > 0 : #left
        plane_J1.x -= VELOCITY   
    if keys_pressed[pg.K_d] and plane_J1.x + VELOCITY + plane_J1.height < WIDTH : #right
        plane_J1.x += VELOCITY   
    if keys_pressed[pg.K_z] and plane_J1.y - VELOCITY > 0 : #up
        plane_J1.y -= VELOCITY   
    if keys_pressed[pg.K_s] and plane_J1.y + VELOCITY + plane_J1.width < HEIGTH : #down
        plane_J1.y += VELOCITY  
    # --------Rotation------------
                
# TO DO :
# - Add the rotation left and right for planes   

def J2_handle_movement(keys_pressed, plane_J2):
    if keys_pressed[pg.K_LEFT] and plane_J2.x - VELOCITY > 0 : #left
        plane_J2.x -= VELOCITY   
    if keys_pressed[pg.K_RIGHT] and plane_J2.x + VELOCITY + plane_J2.height < WIDTH : #right
        plane_J2.x += VELOCITY   
    if keys_pressed[pg.K_UP] and plane_J2.y - VELOCITY > 0 : #up
        plane_J2.y -= VELOCITY   
    if keys_pressed[pg.K_DOWN] and plane_J2.y + VELOCITY + plane_J2.width < HEIGTH : #down
        plane_J2.y += VELOCITY    
    # --------Rotation------------
            
            
def handle_bullets(J1_bullets, J2_bullets, plane_J1, plane_J2):
    for bullet in J1_bullets:
        bullet.x += BULLET_VELOCITY
        if plane_J2.colliderect(bullet):
            pg.event.post(pg.event.Event(PLANE_J2_HIT))
            J1_bullets.remove(bullet)
            
    for bullet in J2_bullets:
        bullet.x -= BULLET_VELOCITY
        if plane_J1.colliderect(bullet):
            pg.event.post(pg.event.Event(PLANE_J1_HIT))
            J2_bullets.remove(bullet)
                
def main():
    plane_J1 = pg.Rect(100,350, PLANE_WIDTH, PLANE_HEIGHT)
    plane_J2 = pg.Rect(848,350, PLANE_WIDTH, PLANE_HEIGHT)
    
    J1_bullets = []
    J2_bullets = []
    
    clock = pg.time.Clock()
    playing = True
    while playing :
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT :
                playing = False
            
            if event.type == pg.KEYDOWN:    
                if event.key == pg.K_LCTRL and len(J1_bullets) < MAX_BULLETS:
                    bullet = pg.Rect(plane_J1.x + plane_J1.width, plane_J1.y + plane_J1.height//2 + 2, 20, 3)
                    J1_bullets.append(bullet)
                    
                if event.key == pg.K_RCTRL and len(J2_bullets) < MAX_BULLETS:
                    bullet = pg.Rect(plane_J2.x + plane_J2.width, plane_J2.y + plane_J2.height//2 + 2, 20, 3)
                    J2_bullets.append(bullet)
                              
        keys_pressed = pg.key.get_pressed()
        J1_handle_movement(keys_pressed, plane_J1)
        J2_handle_movement(keys_pressed, plane_J2)
        
        handle_bullets(J1_bullets, J2_bullets, plane_J1, plane_J2)
            
        draw_windows(plane_J1, plane_J2, J1_bullets, J2_bullets)  
       
        
    pg.quit()
    
    
    
if __name__ == "__main__":
    main()



# Game.play(self)

# ----------Start The Game -----------
# g = Game()
# g.show_start_screen()
# while True:
#     g.new()
#     g.play()
#     g.show_go_screen()