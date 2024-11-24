import pygame
import sys

# Initialize Pygame
pygame.init()

resolution = (500, 500)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Lab8C")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

#boxes
box = pygame.Surface((50,50))
box.fill(BLUE)
box_rect = pygame.Rect(50,50,50,50)

movement_speed = 5

clock = pygame.time.Clock()
running = True

#Main Loop
while running:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False            
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        box_rect.y -= movement_speed
    if keys[pygame.K_s]:
        box_rect.y += movement_speed
    if keys[pygame.K_a]:
        box_rect.x -= movement_speed
    if keys[pygame.K_d]:
        box_rect.x += movement_speed

    #collision handling
    if box_rect.right >= resolution[0] :
        box_rect.right = resolution[0]
    if box_rect.left <= 0:
        box_rect.left = 0
    if box_rect.bottom >= resolution[1]:
        box_rect.bottom = resolution[1]
    if box_rect.top <= 0:
        box_rect.top = 0

    screen.fill(BLACK)

    screen.blit(box, box_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()