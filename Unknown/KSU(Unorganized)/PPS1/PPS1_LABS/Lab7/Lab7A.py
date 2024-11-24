import pygame, sys

pygame.init()
resolution = (400, 400)
screen = pygame.display.set_mode(resolution)

screen_box = pygame.Surface(resolution)

clock = pygame.time.Clock()

intensity = 0
direction = 1 #1 for increasing, -1 for decrease

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)
                pygame.quit()


    screen_box.fill((intensity, intensity, intensity))


    if intensity >= 255:
        direction = -1
    elif intensity <= 0:
        direction = 1

    intensity += direction


    screen.blit(screen_box, (0, 0))

    pygame.display.update()
    clock.tick(250)
