#buggy, but this was my draft, completed at 8 or 9ish PM in PYCHARM, before it got on my nerves
#To which I switched to VS Code.

import pygame
import sys
import random

pygame.init()
pygame.font.init()

resolution = (800, 600)
screen = pygame.display.set_mode(resolution)

basket = pygame.Surface((200, 100))
basket.fill((40, 155, 60))
basket_rect = pygame.Rect(300, 500, 200, 100)

fruit = pygame.Surface((25, 25))
fruit.fill((255, 0, 0))

clock = pygame.time.Clock()

run = True
falling = False
random_x = 0
random_y = 0
fruit_rect = pygame.Rect(random_x, random_y, 25, 25)
fall_speed = 0

score = 0
fruits_fallen = 0

Title = pygame.font.Font('FONTS/Crang.ttf', 36)
Subtitle = pygame.font.Font('FONTS/rainyhearts.ttf', 16)
Subtitle2 = pygame.font.Font('FONTS/rainyhearts.ttf', 10)

intensity = 0
opacity = 5


def game_end(intensity, opacity, subtitle2_grow):
    Title_surface = Title.render("GAME OVER", True, (0, 0, 0))
    score_surface = Subtitle.render("Score: " + str(score), True, (0, 255, 0))
    play_again_surface = Subtitle.render("Play again?", True, (intensity, intensity, intensity))

    screen.fill((255, 255, 255))
    screen.blit(Title_surface, (400 - Title_surface.get_width() // 2, 300))
    screen.blit(score_surface, (400 - score_surface.get_width() // 2, 350))
    screen.blit(play_again_surface, (400 - play_again_surface.get_width() // 2, 500))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        intensity += opacity
        if intensity >= 255:
            break


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_rect.x -= 10
    if keys[pygame.K_RIGHT]:
        basket_rect.x += 10

    if basket_rect.right > 800:
        basket_rect.right = 800
    if basket_rect.left < 0:
        basket_rect.left = 0

    if not falling:
        fruit_rect.x = random.randint(0, 750)
        fruit_rect.y = random.randint(0, 100)
        fall_speed = random.randint(3, 10)
        falling = True

    if falling:
        fruit_rect.move_ip(0, fall_speed)

    if fruit_rect.colliderect(basket_rect):
        score += 1
        fruits_fallen += 1
        falling = False

    elif fruit_rect.y >= 500:
        falling = False

    if fruits_fallen >= 3:
        game_end(intensity, opacity, 10)

    screen.fill((255, 255, 255))
    screen.blit(basket, (basket_rect.x, basket_rect.y))
    screen.blit(fruit, fruit_rect.topleft)

    pygame.display.flip()
    clock.tick(60)
