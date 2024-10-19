import pygame
import sys

pygame.init()

# game window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)



on_button = pygame.image.load("media/on_button.png").convert_alpha()
on_button = pygame.transform.scale(on_button,(100,100))
on_button_rect = pygame.Rect(80,200,100,100)

off_button = pygame.image.load("media/off_button.png").convert_alpha()
off_button = pygame.transform.scale(off_button, (100,100))
off_button_rect = pygame.Rect(320,200,100,100)

laser = pygame.image.load("media/laser.png").convert_alpha()
laser = pygame.transform.scale(laser, (100,100))
laser_rect = pygame.Rect(200,200,100,100)

# window title
pygame.display.set_caption("Lab9")

#fonts
font = pygame.font.Font(None,32)
status_font = pygame.font.Font(None,64)

off_text = font.render("OFF", True, BLACK)
power_up_text = font.render("Power Up", True, BLACK)
shoot_text = font.render("Shoot", True, BLACK)
power_down_text = font.render("Power Down", True, BLACK)

#Flags
status_text = status_font.render("OFF", True, BLACK)

ready = False
charging = False
discharging = False
shooting = False

shoot_sound = pygame.mixer.Sound('media/shoot.mp3')
power_down_sound = pygame.mixer.Sound('media/power-down.mp3')
power_up_sound = pygame.mixer.Sound('media/power-up.mp3')


clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if on_button_rect.collidepoint(mouse_pos):
                    charging = True
                    pygame.mixer.Sound.play(power_up_sound) #play power up sound
                    status_text = status_font.render("CHARGING", True, BLACK)
                    charging = True
            elif laser_rect.collidepoint(mouse_pos) and ready and not shooting:
                shooting = True
                pygame.mixer.Sound.play(shoot_sound)
                status_text = status_font.render("Shooting", True, BLACK)
            elif off_button_rect.collidepoint(mouse_pos) and ready and not discharging:
                discharging = True
                pygame.mixer.Sound.play(power_down_sound)
                status_text = status_font.render("Discharging", True, BLACK)
    
    if charging and not pygame.mixer.get_busy():
        charging = False
        ready = True
        status_text = status_font.render("READY", True, BLACK)

    if shooting and not pygame.mixer.get_busy():
        shooting = False
        status_text = status_font.render("READY", True, BLACK)

    if discharging and not pygame.mixer.get_busy():
        discharging = False
        ready = False
        status_text = status_font.render("OFF", True, BLACK)

    
        
    # Fill the screen with a color (RGB)
    screen.fill(WHITE) # White background

    #Blitting
    screen.blit(laser, laser_rect.topleft)
    screen.blit(shoot_text, (220,320))

    screen.blit(off_button, off_button_rect.topleft)
    screen.blit(power_down_text, (310,320))

    screen.blit (on_button, on_button_rect.topleft)
    screen.blit(power_up_text, (80,320))
    screen.blit(status_text, (200,100)) #80 px would be (210, 170) but it looked ugly so I bumped it up tobe honest.
    
    # Update the display
    pygame.display.flip()

    clock.tick(60)  

pygame.quit()
sys.exit()
