import pygame
import sys
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption('Apple Harvester : The Ultimate Fall Game')

resolution = (800, 600)
screen = pygame.display.set_mode(resolution)

# Preload assets to optimize performance
background = pygame.image.load('background 1.png')
background = pygame.transform.scale(background, (resolution))

basket = pygame.image.load('basket 2.png')
basket = pygame.transform.scale(basket, (120, 120))
blue_basket = pygame.image.load('blue basket.png')
blue_basket = pygame.transform.scale(blue_basket, (120, 120))
basket_rect = pygame.Rect(400, 480, 120, 120)

fruit = pygame.image.load('RedApple.png').convert_alpha()
fruit = pygame.transform.scale(fruit, (50, 50))
fruit_rect = pygame.Rect(0, 0, 50, 50)

# Load background music and sound effects
pygame.mixer.music.load('Output 1-2.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

catch_sound = pygame.mixer.Sound('bling.mp3')
catch_sound.set_volume(0.3)

clock = pygame.time.Clock()

# Game variables
run = False
falling = False
fall_speed = 0
score = 0
fruits_fallen = 0
blink_start_time = 0
blink_duration = 500
is_blinking = False

# Fonts
Title = pygame.font.Font('FONTS/Crang.ttf', 100)
Title2 = pygame.font.Font('FONTS/Crang.ttf', 40)

Subtitle = pygame.font.Font('FONTS/rainyhearts.ttf', 16)

# Render score function
def render_score():
    score_surface = Subtitle.render('Score: ' + str(score), True, (0, 0, 0))
    return score_surface

# Game start screen
def game_start():
    global run 
    screen.blit(background, (0, 0))  # Draw the background first

    # Draw title and subtitle over background
    Title_surface = Title2.render("Apple Harvester", True, (251,63,0))
    subtitle_surface = Subtitle.render("Press R to Play", True, (255, 255, 255))

    screen.blit(Title_surface, (resolution[0] // 4, resolution[1] // 4))
    screen.blit(subtitle_surface, (resolution[0] // 4, resolution[1] // 2))

    pygame.display.flip()
    clock.tick(60)
    

    while not run:
        # Handle events to start the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run = True
                    break
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Handle blinking effect
def handle_blinking():
    global is_blinking, blink_start_time, basket
    current_time = pygame.time.get_ticks()
    blink_elapsed = current_time - blink_start_time

    if (blink_elapsed // 60) % 2 == 0:
        basket = blue_basket  # Switch to blue basket
    else:
        basket = pygame.image.load('basket 2.png')
        basket = pygame.transform.scale(basket, (120, 120))

    if blink_elapsed >= blink_duration:
        is_blinking = False
        basket = pygame.image.load('basket 2.png')
        basket = pygame.transform.scale(basket, (120, 120))

# Game over screen
def game_end():
    Title_surface = Title.render("GAME OVER", True, (0, 0, 0))
    score_surface = Subtitle.render("Score: " + str(score), True, (255, 255, 255))
    play_again_surface = Subtitle.render("Play again? (Press R)", True, (255, 0, 0))

    title_x = (resolution[0] - Title_surface.get_width()) // 2
    title_y = 200
    screen.blit(Title_surface, (title_x, title_y))

    score_x = (resolution[0] - score_surface.get_width()) // 2
    score_y = title_y + Title_surface.get_height() + 20
    screen.blit(score_surface, (score_x, score_y))

    play_again_x = (resolution[0] - play_again_surface.get_width()) // 2
    play_again_y = score_y + score_surface.get_height() + 20
    screen.blit(play_again_surface, (play_again_x, play_again_y))

    pygame.display.flip()
    pygame.time.delay(1000)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    reset_game()
                    waiting = False

# Reset game state
def reset_game():
    global score, fruits_fallen, falling, fruit_rect
    score = 0
    fruits_fallen = 0
    falling = False
    fruit_rect.x = random.randint(0, 750 - fruit_rect.width)
    fruit_rect.y = random.randint(0, 100)

# Main game loop
while not run:
    game_start()

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

    if fruit_rect.y > 600:
        falling = False
        fruits_fallen += 1

    if is_blinking:
        handle_blinking()

    if not falling:
        fruit_rect.x = random.randint(0, 750 - fruit_rect.width)
        fruit_rect.y = random.randint(0, 100)
        fall_speed = random.randint(3, 10)
        falling = True

    if falling:
        fruit_rect.move_ip(0, fall_speed)

    if fruit_rect.colliderect(basket_rect):
        catch_sound.play()
        is_blinking = True
        score += 1
        fruits_fallen += 1
        falling = False
        blink_start_time = pygame.time.get_ticks()

    if fruits_fallen >= 20:
        game_end()

    screen.blit(background, (0, 0))
    screen.blit(basket, (basket_rect.x, basket_rect.y))
    screen.blit(fruit, fruit_rect.topleft)

    score_surface = render_score()
    screen.blit(score_surface, (10, 10))

    pygame.display.flip()
    clock.tick(60)
