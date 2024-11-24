import pygame, sys

pygame.init()
resolution = (600, 600)
screen_rect = pygame.Rect(0,0,600,600)
screen = pygame.display.set_mode(resolution)

clock = pygame.time.Clock()

box1 = pygame.Surface((60,60))
box1.fill((255,0,0))
box1_rect = pygame.Rect(0,0,60,60)

box2 = pygame.Surface((60,60))
box2.fill((255,0,0))
box2_rect = pygame.Rect(0,540,60,60)

box3 = pygame.Surface((60,60))
box3.fill((255,0,0))
box3_rect = pygame.Rect(300,300,60,60)

box4 = pygame.Surface((60,60))
box4.fill((255,0,0))
box4_rect = pygame.Rect(540,0,60,60)

box5 = pygame.Surface((60,60))
box5.fill((255,0,0))
box5_rect = pygame.Rect(540,540,60,60)

while True:

    screen.fill((0,0,0))
    screen.blit(box1, box1_rect)
    screen.blit(box2, box2_rect)
    screen.blit(box3, box3_rect)
    screen.blit(box4, box4_rect)
    screen.blit(box5, box5_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit(0)

    pygame.display.update()
    clock.tick(60)
