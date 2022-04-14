import pygame
import time

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 570

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("On The Run")

name_font = pygame.font.Font('fonts/imminent-line.ttf', 72)
show_name = name_font.render("ON THE RUN", True, (255, 255, 255))

start = pygame.image.load('image/GAME BUTTONS/start.png')
start = pygame.transform.scale(start, (250, 100))

start_x = 100
start_y = 100

settings = pygame.image.load('image/GAME BUTTONS/settings.png')
settings = pygame.transform.scale(settings, (250, 100))
settings_x = 100
settings_y = 400

profile = pygame.image.load('image/GAME BUTTONS/profile.png')
profile = pygame.transform.scale(profile, (250, 100))
profile_x = 400
profile_y = 100


class Button:
    def __init__(self, image, position, callback):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.callback = callback

    def on_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.callback(self)


def play(class_variable):
    print('play')
    return


def show_settings(class_variable):
    print('settings')
    return


def show_profile(class_variable):
    print('profile')
    return


def menu():
    for i in range(0, 62):
        image = pygame.image.load('image/intro/frame_{}_delay-0.1s.jpg'.format(i))
        image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        sprite = pygame.sprite.Sprite()
        sprite.image = image
        sprite.rect = image.get_rect()
        sprite.image.blit(show_name, (sprite.rect.width / 2 - (show_name.get_rect().width / 2), 5))
        group = pygame.sprite.Group()
        group.add(sprite)
        group.draw(screen)
        pygame.display.update()
        time.sleep(0.08)

    button1 = Button(start, (350, 150), play)
    button2 = Button(settings, (350, 300), show_settings)
    button3 = Button(profile, (350, 450), show_profile)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            button1.on_click(event)
            button2.on_click(event)
            button3.on_click(event)

        screen.blit(button1.image, button1.rect)
        screen.blit(button2.image, button2.rect)
        screen.blit(button3.image, button3.rect)
        pygame.display.update()


menu()
