import pygame

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 570

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("On The Run")
icon = pygame.image.load('image/sport-car.png')
pygame.display.set_icon(icon)

restart = pygame.image.load('image/GAME BUTTONS/restart.png')
restart = pygame.transform.scale(restart, (220, 100))

main_menu = pygame.image.load('image/GAME BUTTONS/main menu.png')
main_menu = pygame.transform.scale(main_menu, (220, 100))

how_to_play = pygame.image.load('image/GAME BUTTONS/how_to_play.png')
how_to_play = pygame.transform.scale(how_to_play, (220, 100))

frame = pygame.image.load('image/frame.png')
frame = pygame.transform.scale(frame, (350, 450))
frame_x = SCREEN_WIDTH / 2 - frame.get_rect().width / 2
frame_y = SCREEN_HEIGHT / 2 - frame.get_rect().height / 2

screen.fill((255, 255, 255))
while True:
    screen.blit(frame, (frame_x, frame_y))
    screen.blit(restart, (SCREEN_WIDTH/2 - restart.get_rect().width/2,
                          SCREEN_HEIGHT/2 - restart.get_rect().height/2 - 120))

    screen.blit(main_menu, (SCREEN_WIDTH/2 - restart.get_rect().width/2,
                SCREEN_HEIGHT/2 - restart.get_rect().height/2))
    screen.blit(how_to_play, (SCREEN_WIDTH/2 - restart.get_rect().width/2,
                SCREEN_HEIGHT/2 - restart.get_rect().height/2 + 120))

    pygame.display.update()
