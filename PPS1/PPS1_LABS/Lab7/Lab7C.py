import pygame, sys
from pygame.locals import *

pygame.init()
resolution = (1000, 500)
screen = pygame.display.set_mode(resolution)
screen_rect = pygame.Rect(0,0,1000,500)
clock = pygame.time.Clock()

box1 = pygame.Surface((100,100))
box1.fill((0,255,0))
box1_rect = pygame.Rect(0,0,100,100)

box2 = pygame.Surface((100,100))
box2.fill((0,0,255))
box2_rect = pygame.Rect(0,400,100,100)
move_speed = 5


while True: # Main gameplay loop

    keys = pygame.key.get_pressed()    # Check which keys have been pressed
    for event in pygame.event.get():    # Checks what events happened, and act on them.
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    screen.fill(color=(0,0,0)) # Paint the whole screen black

#box 1
    box1_rect = box1_rect.move(move_speed,0)
    screen.blit(box1, box1_rect.topleft)

    if box1_rect.right > 1000 or box1_rect.left < 0:
        move_speed *= -1

#box 2
    box2_rect = box2_rect.move(move_speed, 0)
    screen.blit(box2, box2_rect.topleft)

    if box2_rect.right > 1000 or box2_rect.left < 0:
        move_speed *= -1



    pygame.display.flip() # Update the Display with the contents of the Display's surface
    clock.tick(60) #

