import pygame as pg
import math
import random
from settings import *
from utils import blit_rotate_center

# --------------------------------------------------------------               
#                 ------- CLASS AIRCRAFT --------  
# --------------------------------------------------------------  
class AircraftFighter(pg.sprite.Sprite):
    def __init__(self, max_velocity,rotation_velocity):
        self.image = AIRCRAFTS_IMGS[random.randint(0,7)]
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = self.START_POSITION 
        self.max_velocity = max_velocity
        self.health = 100
        self.vel = 0
        self.rotation_velocity = rotation_velocity
        self.angle = self.START_ANGLE
        self.x , self.y = self.START_POSITION
        self.acceleration = 0.1
        self.score = 0
        
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_velocity
        elif right:
            self.angle -= self.rotation_velocity
            
    def draw(self, SCREEN):
        blit_rotate_center(SCREEN, self.image, (self.x, self.y), self.angle)
        
    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_velocity)
        self.move()
        
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel 
        
        self.x -= horizontal  
        self.y -= vertical
        self.rect.x = self.x
        self.rect.y = self.y
    
    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration/2, 0)
        self.move()
        
    def step_back(self):
        self.vel = -self.vel
        self.move()     
                 
    def reset(self):
        self.x, self.y = self.START_POSITION
        self.rect.x, self.rect.y = self.START_POSITION
        self.angle = self.START_ANGLE
        self.vel = 0
        
    def get_angle(self):
        return self.angle
    
    def set_explosion(self,image):
        self.image = image
    
    def get_rect_image(self):
        return self.image.get_rect()
    
    def collide_map(self):
        if self.x - self.vel <= 0: # collide left
            return True 
        if self.x + self.vel + PLANE_HEIGHT >= WIDTH: # collide right
            return True 
        if self.y - self.vel <= 0 : # collide top  
            return True 
        if self.y + self.vel + PLANE_WIDTH >= HEIGTH: # collide down
            return True 
        
    
# --------------------------------------------------------------               
#                  ------- CLASS WEAPONS ------  
# --------------------------------------------------------------          
class Weapons():
    def __init__(self,x, y, image, angle, vel, damage, point):
        self.image = image
        self.rectangle = self.image.get_rect()
        self.rectangle.x = x
        self.rectangle.y = y
        self.angle = angle
        self.x, self.y = x, y 
        self.vel = vel
        self.damage = damage
        self.point = point
    
    def get_rect_image(self):
        return self.image.get_rect()
    
    def move_weapons(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel 
        self.x -= horizontal  
        self.y -= vertical
        self.rect = blit_rotate_center(SCREEN, self.image, (self.x, self.y), self.angle-90)
        self.rectangle.x = self.x
        self.rectangle.y = self.y 
        
    def collide_map(self):
        if self.x - self.vel <= 0: # collide left
            return True 
        if self.x + self.vel + BULLET_HEIGHT >= WIDTH: # collide right
            return True 
        if self.y - self.vel <= 0 : # collide top  
            return True 
        if self.y + self.vel + BULLET_WIDTH >= HEIGTH: # collide down
            return True 




# --------------------------------------------------------------               
#               ------- CLASS PLAYER ------  
# --------------------------------------------------------------  
class Player1(AircraftFighter) :
    START_POSITION = (100, 350)
    START_ANGLE = 270

    def shoot_bullet(self):
        bullet = Weapons(self.x + PLANE_WIDTH-10, self.y + PLANE_HEIGHT-43, BULLET1_IMG , self.angle, VELOCITY_BULLET, BULLET_DAMAGE, BULLET_POINT)
        return bullet
        
    def shoot_missile(self):
        missile = Weapons(self.x + PLANE_WIDTH-50, self.y + PLANE_HEIGHT-60, MISSILES_IMG[random.randint(0,1)], self.angle, VELOCITY_MISSILE, MISSILE_DAMAGE, MISSILE_POINT)
        return missile


class Player2(AircraftFighter) :
    START_POSITION = (848, 350)
    START_ANGLE = 90
    
    def shoot_bullet(self):
        bullet = Weapons(self.x + PLANE_WIDTH-80, self.y + PLANE_HEIGHT-43, BULLET1_IMG, self.angle, VELOCITY_BULLET, BULLET_DAMAGE, BULLET_POINT)
        return bullet
    
    def shoot_missile(self):
        missile = Weapons(self.x + PLANE_WIDTH-80, self.y + PLANE_HEIGHT-60,  MISSILES_IMG[random.randint(0,1)], self.angle, VELOCITY_MISSILE, MISSILE_DAMAGE, MISSILE_POINT)
        return missile




    
    
    
