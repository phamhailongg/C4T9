import sys
import pygame 
from bullet import Bullet
def check_keydown_events(event, screen, ship, bullets) : 
    if event.key == pygame.K_SPACE : 
        new_bullet = Bullet(ai_settings, screen, ship)
        bullet.add(new_bullet)

def check_events(ai_settings, screen, ship, bullets) : 
    """Respond to keypresses and mouse events. """
    for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                sys.exit()  
            elif event.type == pygame.KEYDOWN : 
                check_keydown_events(ai_settings, screen, ship, bullets) 
                """ Respond to keypress """
                if event.key == pygame.K_RIGHT : 
                    ship.moving_right = True 
                elif event.key == pygame.K_LEFT : 
                    ship.moving_left = True
                check_keydown_events(event, ship)
            
            elif event.type == pygame.KEYUP : 
                def check_keyup_events(event, ship) :
                    """ Respond to key release """
                    if event.key == pygame.K_RIGHT : 
                        ship.moving_right = False
                    elif event.key == pygame.K_LEFT : 
                        ship.moving_left = False
                check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets) : 
    """ Update images on the screen and flip to the new screen. """ 
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
    for bullet in bullets.sprites() : 
        bullet.draw_bullet()