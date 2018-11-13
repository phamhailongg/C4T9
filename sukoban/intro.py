import pygame
pygame.init()

win = pygame.display.set_mode( (500, 500) )

pygame.display.set_caption("Sukoban")

x = 50
y = 50
width = 50
length = 50
vel = 5 

run = True
while run : 
    pygame.time.delay(360)

    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
        x -= vel
    if keys[pygame.K_RIGHT] :
        x += vel
    if keys[pygame.K_UP] :
        y -= vel
    if keys[pygame.K_DOWN] :
        y += vel
    
   
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, length))
    pygame.display.update()
pygame.quit()




