import pygame
import sys

# Initialize Pygame
pygame.init()

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Lab8A")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

#boxes
box1 = pygame.Surface((50,50))
box1.fill(BLUE)
box1_rect = pygame.Rect(50,50,50,50)

wall = pygame.Surface((70,400))
wall.fill(RED)
wall_rect = pygame.Rect(230,0,70,400)

movement_speed = 5

clock = pygame.time.Clock()
running = True

#Main Loop
while running:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    box1_rect.move_ip(movement_speed, 0)

    #collision handling
    if box1_rect.right >= resolution[0] or box1_rect.left <= 0:
        movement_speed = -movement_speed

    if box1_rect.colliderect(wall_rect):
        wall.fill(GREEN)
    else:
        wall.fill(RED)

    screen.fill(BLACK)

    screen.blit(box1, box1_rect.topleft)
    screen.blit(wall, wall_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()