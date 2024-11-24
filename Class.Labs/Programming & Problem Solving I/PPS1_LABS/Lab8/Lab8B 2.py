import pygame
import sys

# Initialize Pygame
pygame.init()

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Lab8B")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

#boxes
box1 = pygame.Surface((50,50))
box1.fill(BLUE)
box1_rect = pygame.Rect(0,0,50,50)

box2 = pygame.Surface((50,50))
box2.fill(BLUE)
box2_rect = pygame.Rect(345,100,50,50)

box3 = pygame.Surface((50,50))
box3.fill(BLUE)
box3_rect = pygame.Rect(0,350,50,50)

wall = pygame.Surface((70,400))
wall.fill(RED)
wall_rect = pygame.Rect(230,0,70,400)

boxes = [box1_rect,box2_rect,box3_rect]
movement_speed1 = 10
movement_speed2 = 5
movement_speed3 = 20

clock = pygame.time.Clock()
running = True

#Main Loop
while running:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    box1_rect.move_ip(movement_speed1, 0)
    box2_rect.move_ip(movement_speed2, 0)
    box3_rect.move_ip(movement_speed3, 0)


    #collision handling
    if box1_rect.right >= resolution[0] or box1_rect.left <= 0:
        movement_speed1 = -movement_speed1

    if box2_rect.right >= resolution[0] or box2_rect.left <= 0:
            movement_speed2 = -movement_speed2

    if box3_rect.right >= resolution[0] or box3_rect.left <= 0:
        movement_speed3 = -movement_speed3


    if wall_rect.collidelist(boxes):
        wall.fill(GREEN)
    else:
        wall.fill(RED)

    screen.fill(BLACK)


    screen.blit(box1, box1_rect.topleft)
    screen.blit(box2, box2_rect.topleft)
    screen.blit(box3, box3_rect.topleft)

    screen.blit(wall, wall_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()