'''
Pygame Practice
8. Move a Block Left or Right
In Pygame, create a small square that can be moved left and right on the screen using the arrow keys.

The square should start at the center of the screen.
When the left arrow is pressed, the square should move left.
When the right arrow is pressed, the square should move right.
The square should stop at the screen boundaries.

'''

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display (width, height)
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Starter")

# Set up colors
WHITE = (255, 255, 255)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)

#variables
box = pygame.Surface((50,50))
box_rect = pygame.Rect(400,400,50,50)
box.fill(RED)
movespeed= 5

# Set the frames per second (FPS) for the game loop
clock = pygame.time.Clock()
FPS = 60

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            box_rect.x -= movespeed
        if event.key == pygame.K_RIGHT:
            box_rect.x += movespeed
        if event.key == pygame.K_UP:
            box_rect.y -= movespeed
        if event.key == pygame.K_DOWN:
            box_rect.y += movespeed
        

#movement

    # Fill the screen with white (or any other color)
    screen.fill(WHITE)

    screen.blit(box, box_rect.topleft)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
