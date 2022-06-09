import pygame as pg

def blit_rotate_center(SCREEN, image, top_left, angle):
    rotated_image = pg.transform.rotate(image, angle)
    rotation_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    SCREEN.blit(rotated_image, rotation_rect)
    
def chrono():
    pass

def score():
    pass