"""-------------import statements--------------"""
import pygame
import random
from pygame import mixer
import time
import sys
import tkinter as tk
from tkinter import messagebox


"""-------------display screen set up--------------"""
# setting up window
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 570

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# giving name
pygame.display.set_caption("On The Run")
# setting icon
icon = pygame.image.load('test/image/sport-car.png')
pygame.display.set_icon(icon)

"""--------------variable declaration----------------"""

# PLAYER IMAGE
playerImage = pygame.image.load('test/image/car1.png')

# OPPONENT IMAGES
car2 = pygame.image.load('test/image/car2.png')
car3 = pygame.image.load('test/image/car3.png')
car4 = pygame.image.load('test/image/car4.png')
car5 = pygame.image.load('test/image/car5.png')
car6 = pygame.image.load('test/image/car6.png')
car7 = pygame.image.load('test/image/car7.png')

sample = [car2, car3, car4, car5, car6, car7]  # LIST OF IMAGES OF OPPONENTS
positions_for_opponents = [230, 330, 415, 500, 590, 690]  # X-COORDINATES w.r.t TRACK IMAGE

# FONTS
# game name font
name_font = pygame.font.Font('test/fonts/imminent-line.ttf', 72)
show_name = name_font.render("ON THE RUN", True, (255, 255, 255))

# game over font
over_font = pygame.font.Font('test/fonts/SwipeRaceDemo.ttf', 45)
over_textX = 185
over_textY = 300

# score font
score_font = pygame.font.Font('test/fonts/SwipeRaceDemo.ttf', 20)
score_textX = 5
score_textY = 5

# 'press any key to continue' font
continue_font = pygame.font.Font('test/fonts/EA_font.ttf', 50)
continue_textX = 80
continue_textY = 300

# TRACK IMAGES
# images of track components
wallLeft = pygame.image.load('test/image/left.png')
wallRight = pygame.image.load('test/image/right.png')
track = pygame.image.load('test/image/track.jpg')

# x-coordinate of track components
wallLeft_x = 0
wallRight_x = 800
track_x = 200

# y-coordinate of track components
wallLeft_y = 0
wallRight_y = 0
track_y = 0

# COLLECTING GIF IMAGES FOR GIF IN MAIN MENU
lst_images = []
for i in range(0, 62):
    image = pygame.image.load('test/image/intro/frame_{}_delay-0.1s.jpg'.format(i))
    image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    lst_images.append(image)


"""--------------BUTTON IMAGES OF BOTH EXTRA SCREENS----------------"""
# FRAME OF BUTTONS IN RESTART SCREEN
frame = pygame.image.load('test/image/frame.png')
frame = pygame.transform.scale(frame, (350, 450))
frame_x = SCREEN_WIDTH / 2 - frame.get_rect().width / 2
frame_y = SCREEN_HEIGHT / 2 - frame.get_rect().height / 2

# MENU SCREEN BUTTONS
start = pygame.image.load('test/image/GAME BUTTONS/start.png')
start = pygame.transform.scale(start, (250, 100))

settings = pygame.image.load('test/image/GAME BUTTONS/settings.png')
settings = pygame.transform.scale(settings, (250, 100))

profile = pygame.image.load('test/image/GAME BUTTONS/profile.png')
profile = pygame.transform.scale(profile, (250, 100))

# RESTART SCREEN BUTTONS
restart = pygame.image.load('test/image/GAME BUTTONS/restart.png')
restart = pygame.transform.scale(restart, (220, 100))

main_menu = pygame.image.load('test/image/GAME BUTTONS/main menu.png')
main_menu = pygame.transform.scale(main_menu, (220, 100))

how_to_play = pygame.image.load('test/image/GAME BUTTONS/how_to_play.png')
how_to_play = pygame.transform.scale(how_to_play, (220, 100))

"""----------------CLASS TO CREATE BUTTONS IN PYGAME WINDOW----------------"""


class Button:
    def __init__(self, image, position, callback):
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.callback = callback

    def on_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.callback(self)


"""-------------------------FUNCTIONS IN THE GAME-----------------------------"""


def terminate():  # TO END THE PROGRAM
    pygame.quit()
    sys.exit()


def player(x, y):  # TO CHANGE THE POSITION OF THE PLAYER
    screen.blit(playerImage, (x, y))


# TO DISPLAY 'GAME OVER' WHEN COUNT = 0 (LIVES)
def game_over_text(x, y):
    game_over = over_font.render('GAME OVER', True, (0, 0, 0))  # this statement uses the font stored in over_font
    screen.blit(game_over, (x, y))
    pygame.display.update()


# TO STOP THE EXECUTION OF LOOP
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                return True


def show_settings(class_variable):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("On The Run", "COMING SOON...")
    return


def show_profile(class_variable):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("On The Run", "COMING SOON...")
    return


# MAIN GAME EXECUTION
def play(class_variable):  # CLASS VARIABLE JUST TO FULFILL THE BUTTON CLASS CREATED (NO USAGE IN FUNCTION)
    global screen, SCREEN_WIDTH, SCREEN_HEIGHT
    global wallLeft_x, wallRight_x, track_x, wallLeft_y, wallRight_y, track_y
    global sample, positions_for_opponents

    # person's score
    score = 0

    player_X_change = 0  # CHANGE TO BE ADDED TO INSTANTANEOUS POSITION
    player_Y_change = 0
    player_X = 510  # INITIAL POSITION
    player_Y = 500
    playerRect = pygame.Rect(player_X, player_Y, 65, 120)  # CREATE A RECTANGLE AROUND PLAYER

    add_new_opponent_rate = 200  # --| - these statements are to release new enemy
    opponent = 0                 # --|   after the while loop has executed 120 times

    # motion check of the player (applying condition for executing the if-statements in loop)
    move_left = move_right = move_up = move_down = False

    count = 3  # NUMBER OF LIVES
    game_over = False
    while count > 0:
        running_main = True  # VARIABLE THAT KEEPS THE EXECUTION LOOP BELOW RUNNING
        opponents = []  # OPPONENTS PRESENT IN THE SCREENS AT THE MOMENT

        while running_main:
            score += 1  # EVERY LOOP ADDS A SCORE

            screen.fill((0, 0, 0))  # CLEARS THE WINDOW TO COMPLETE BLACK

            # ALGORITHM FOR INFINITE MOVEMENT OF THE TRACK COMPONENTS DOWNWARDS
            # left-side of track
            rel_y_left = wallLeft_y % wallLeft.get_rect().height
            screen.blit(wallLeft, (0, rel_y_left - wallLeft.get_rect().height))
            if rel_y_left < 800:
                screen.blit(wallLeft, (0, rel_y_left))
            wallLeft_y += 7  # sets the speed of left-side of track

            # right-side of track
            rel_y_right = wallRight_y % wallRight.get_rect().height
            screen.blit(wallRight, (800, rel_y_right - wallRight.get_rect().height))
            if rel_y_right < 800:
                screen.blit(wallRight, (800, rel_y_right))
            wallRight_y += 7  # sets the speed of right-side of track

            # track
            rel_y_track = track_y % track.get_rect().height
            screen.blit(track, (200, rel_y_track - track.get_rect().height))
            if rel_y_track < 800:
                screen.blit(track, (200, rel_y_track))
            track_y += 7  # sets the speed of the track

            # CHECKS IN EVERY LOOP ITERATION IF SOME EVENT IS PERFORMED OR NOT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # EVENT TO CHECK IF USER HAS QUITED
                    running_main = False
                    terminate()

                # TO CHECK IF THE USER HAS PRESSED THE ARROW KEYS
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_X_change -= 3  # TO BE ADDED TO player_x TO CHANGE THE POSITION OF PLAYER
                        move_left = True
                    elif event.key == pygame.K_RIGHT:
                        player_X_change += 3
                        move_right = True  # THESE CONDITIONS WILL HELP TO APPLY 'IF' CONDITION TO THE LOOP
                    elif event.key == pygame.K_UP:
                        player_Y_change -= 3
                        move_up = True
                    elif event.key == pygame.K_DOWN:
                        player_Y_change += 3
                        move_down = True

                # TO CHECK IF THE USER HAS REMOVED HIS FINGER FROM ARROW KEYS
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player_X_change = 0  # TO STOP THE CHANGE OF POSITION OF PLAYER or
                        move_left = move_right = False  # TO KEEP HIM AT REST
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_Y_change = 0
                        move_up = move_down = False

            opponent += 1  # TO EXECUTE THE BELOW 'IF' STATEMENT ONCE IN EVERY 120 TIMES
            if opponent == add_new_opponent_rate:
                opponent = 0  # RESET TO ZERO AFTER REACHING 120
                # THE BELOW STATEMENT CHOOSES NUMBER OF OPPONENTS (1 TO 4) TO BE ADDED TO SCREEN OUT OF 6
                number = random.choice([1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4])
                """2,3 WRITTEN MULTIPLE TIMES SO THAT MAJORITY TIMES ONLY 2,3 OPPONENTS
                    APPEAR TOGETHER ON THE SCREEN"""

                # SELECTS 'number'(say 3) DIFFERENT POSITIONS FROM 'positions_for_opponents'
                positions_X_different = random.sample(positions_for_opponents, number)

                for i in positions_X_different:
                    # CREATING DICTIONARY ABOUT INFORMATION OF ONE OPPONENT
                    new_opponent = {'position_X': i,
                                    'position_Y': -100,
                                    'rect': pygame.Rect(i + 5, -100, 70, 180),
                                    'colour': random.choice(sample),
                                    'speed': random.choice([2, 3, 4, 3, 4, 5])}
                    opponents.append(new_opponent)

            # LOOP FOR ALWAYS MOVING THE OPPONENT DOWNWARDS WITHOUT ANY STOP
            for enemy in opponents:
                enemy['position_Y'] = enemy['position_Y'] + enemy['speed']
                enemy['rect'].move_ip(0, enemy['speed'])  # move_ip moves the image

            # IF THE PLAYER CROSSES THE SCREEN_HEIGHT IT IS REMOVED FROM THE LIST OPPONENTS
            for enemy in opponents[:]:
                if enemy['position_Y'] > SCREEN_HEIGHT:
                    opponents.remove(enemy)

            # MOVEMENT OF PLAYER
            if move_left:
                player_X = player_X + player_X_change
                playerRect.move_ip(player_X_change, 0)
            elif move_right:
                player_X = player_X + player_X_change
                playerRect.move_ip(player_X_change, 0)
            elif move_up:
                player_Y = player_Y + player_Y_change
                playerRect.move_ip(0, player_Y_change)
            elif move_down:
                player_Y = player_Y + player_Y_change
                playerRect.move_ip(0, player_Y_change)

            # TO PLACE THE OPPONENTS ON THE SCREEN
            for enemy in opponents:
                screen.blit(enemy['colour'], (enemy['position_X'], enemy['position_Y']))

            """----TO CHECK FOR COLLISION----"""
            for enemy in opponents:
                if playerRect.colliderect(enemy['rect']):
                    # CHECKING THE COLLISION OF RECTANGLES OF PLAYER IMAGE AND OPPONENT IMAGES
                    running_main = False  # STOP THE EXECUTION OF INNER LOOP
                    count -= 1  # DECREASE THE NUMBER OF LIVES
                    if count > 0:
                        wait_to_continue1 = continue_font.render("Lost A Life! Don't worry {} More to go".format(count),
                                                                 True, (0, 100, 0, 255))
                        screen.blit(wait_to_continue1, (continue_textX, continue_textY))
                        wait_to_continue2 = continue_font.render('press any key to continue', True,
                                                                 (255, 0, 0))

                        screen.blit(wait_to_continue2, (continue_textX + 100, continue_textY + 50))
                        player(player_X, player_Y)
                        pygame.display.update()

                        waitForPlayerToPressKey()

                    else:  # GOING TO OUTER LOOP ELSE CLAUSE
                        pass

            # STOP THE PLAYER AT THE BOUNDARIES
            if player_X > 715:
                player_X = 715
            elif player_X < 205:
                player_X = 205
            if player_Y > 450:
                player_Y = 450
            elif player_Y < 5:
                player_Y = 5

            player(player_X, player_Y)

            # PRINT SCORE
            score_print = score_font.render('SCORE - ' + str(score), True,
                                            (0, 0, 139, 255))
            screen.blit(score_print, (score_textX, score_textY))

            # PRINT LIVES
            lifes_print = score_font.render('LIVES - ' + str(count), True,
                                            (0, 0, 139, 255))
            screen.blit(lifes_print, (score_textX, score_textY + 30))

            pygame.display.update()

    # STATEMENT FOR GAME OVER
    else:
        game_over_text(over_textX, over_textY)
        pygame.display.update()
        n = waitForPlayerToPressKey()
        if n:
            restart_menu()


"""------------RESTART MENU------------"""


def restart_menu():
    # USING THE BUTTON FUNCTION CREATED THROUGH THE CLASS
    button4 = Button(restart, (390, 115), play)
    button5 = Button(how_to_play, (390, 235), show_settings)
    button6 = Button(main_menu, (390, 355), menu)

    running_restart = True
    while running_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_restart = False
                terminate()

            # CALLING THE EVENT FUNCTION FOR THESE BUTTONS FROM CLASS
            button4.on_click(event)
            button5.on_click(event)
            button6.on_click(event)

        screen.blit(frame, (frame_x, frame_y))
        screen.blit(button4.image, (SCREEN_WIDTH / 2 - restart.get_rect().width / 2,
                                    SCREEN_HEIGHT / 2 - restart.get_rect().height / 2 - 120))
        screen.blit(button5.image, (SCREEN_WIDTH / 2 - restart.get_rect().width / 2,
                                    SCREEN_HEIGHT / 2 - restart.get_rect().height / 2))
        screen.blit(button6.image, (SCREEN_WIDTH / 2 - restart.get_rect().width / 2,
                                    SCREEN_HEIGHT / 2 - restart.get_rect().height / 2 + 120))
        pygame.display.update()
    waitForPlayerToPressKey()


"""------------OPENING MENU------------"""


def menu(class_variable):  # CLASS VARIABLE JUST TO FULFILL THE BUTTON CLASS CREATED (NO USAGE IN FUNCTION)
    global screen
    screen.fill((0, 0, 0))
    pygame.display.update()
    for i in lst_images:
        # THE FOLLOWING COMMANDS ARE FOR PRINTING TEXT OVER THE IMAGE
        sprite = pygame.sprite.Sprite()
        sprite.image = i
        sprite.rect = image.get_rect()
        sprite.image.blit(show_name, (sprite.rect.width / 2 - (show_name.get_rect().width / 2), 5))
        group = pygame.sprite.Group()
        group.add(sprite)
        group.draw(screen)
        pygame.display.update()
        time.sleep(0.08)

    # USING THE BUTTON FUNCTION CREATED THROUGH THE CLASS
    button1 = Button(start, (350, 150), play)
    button2 = Button(settings, (350, 300), show_settings)
    button3 = Button(profile, (350, 450), show_profile)

    running_menu = True
    while running_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_menu = False
                terminate()

            # CALLING THE EVENT FUNCTION FOR THESE BUTTONS FROM CLASS
            button1.on_click(event)
            button2.on_click(event)
            button3.on_click(event)

        screen.blit(button1.image, button1.rect)
        screen.blit(button2.image, button2.rect)
        screen.blit(button3.image, button3.rect)
        pygame.display.update()


if __name__ == '__main__':
    var = 'class_variable'
    menu(var)
