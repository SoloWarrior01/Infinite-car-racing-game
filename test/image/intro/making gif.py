import pygame
import time
pygame.init()

# SETTING THE SCREEN
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Space Invader")


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    for i in range(0,51):
        icon = pygame.image.load('frame_{}_delay-0.1s.png'.format(i))
        screen.blit(icon, (5,5))
        pygame.display.update()
        time.sleep(0.05)
    icon = screen.fill((0,0,0))
    pygame.display.update()
    
    
    
