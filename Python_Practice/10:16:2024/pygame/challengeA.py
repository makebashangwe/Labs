import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 800  # Window size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame Window")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Game variables
box = pygame.Surface(50,50)
box.fill(RED)
box_rect = pygame.Rect(0,0,50,50)

wall = pygame.Surface(40,800)
wall_rect = pygame.Rect(360,0)
wall.fill(BLUE)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the loop


    # Fill the screen with white
    screen.fill(WHITE)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
