# set up game 
import sys 
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
     
def run_game() : 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")
    # Make a ship 
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in 
    bullets = Group()
    # set up bg 
    bg_color = (0, 0, 0)
    while True : 
        gf.check_events(ai_settings, screen, ship, bullets)
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        ship.update()
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                sys.exit()  
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip() 

run_game()



