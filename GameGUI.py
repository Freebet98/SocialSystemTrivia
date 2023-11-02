import sys
import pygame
import pygamebutton
import GameFunctions

# initialize constructor
pygame.init()
# Variables
# screen size
width = 1600
height = 900

# Colors
# language color
langColor = (111, 191, 87)
# Employment color
employColor = (171, 147, 197)
# Culture Color
cultColor = (226, 145, 190)
# Relationship Color
relaColor = (61, 142, 204)
# Black Color
blackColor = (35, 31, 32)
# white Color
whiteColor = (255, 255, 255)
# light shade of button
color_light = (170, 170, 170)
# dark shade of button
color_dark = (100, 100, 100)

# Fonts
# defining a font
smallFont = pygame.font.SysFont('Corbel', 35)
cardFont = pygame.font.SysFont('Corbel', 35)

# images
background = pygame.image.load('board-01.png')
background = pygame.transform.scale(background, (width, height))
langCard = pygame.image.load('Langauge2-01.jpg')
employCard = pygame.image.load('Employment2-01.jpg')
cultCard = pygame.image.load('Culture2-01.jpg')
relateCard = pygame.image.load('Relationship2-01.jpg')

# open window
screen = pygame.display.set_mode((width, height))
playScreen = pygame.display.set_mode((width, height))
triviaScreen = pygame.display.set_mode((width, height))

# rendering a text written in this font
text = smallFont.render('quit', True, whiteColor)

# dice value
diceVal = 6
players = 1
boardArr = [(150, 825), (250, 725), (400, 750), (550, 800), (650, 820), (800, 790), (950, 760), (1100, 800), (1250, 825),
            (1350, 850)]


def play_one():
    pygame.display.set_caption("Trivia")
    pos = boardArr[9]
    counter = 0
    dice_roll = 0

    while True:
        playScreen.blit(background, (0, 0))

        playMousePos = pygame.mouse.get_pos()

        rollDiceButton = pygamebutton.Button(image=None, pos=(300, 100), text_input="Roll",
                                             font=smallFont, base_color=blackColor, hovering_color=langColor)
        for button in [rollDiceButton]:
            button.changeColor(playMousePos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rollDiceButton.checkForInput(playMousePos):
                    dice_roll = GameFunctions.roll_dice(diceVal)

        counter += dice_roll
        if counter > 0:
            category = GameFunctions.check_spot(dice_roll, counter)
            qa_rlst = GameFunctions.switch_dict(category)
            lst_qa = qa_rlst[0]
            ran_lst = qa_rlst[1]
        if players == 1:
            draw_circle(pos, blackColor, playScreen)

        pygame.display.update()


def play_two():
    pygame.display.set_caption("Trivia")
    pos1 = (80, 800)
    draw_circle(pos1, blackColor, playScreen)
    pos2 = (70, 800)
    draw_circle(pos2, blackColor, playScreen)

    while True:
        playScreen.blit(background, (0, 0))

        playMousePos = pygame.mouse.get_pos()

        rollDiceButton = pygamebutton.Button(image=None, pos=(300, 100), text_input="Roll",
                                             font=smallFont, base_color=blackColor, hovering_color=langColor)
        for button in [rollDiceButton]:
            button.changeColor(playMousePos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rollDiceButton.checkForInput(playMousePos):
                    diceRoll = GameFunctions.roll_dice(diceVal)

        pygame.display.update()


def play_three():
    pygame.display.set_caption("Trivia")
    pos1 = (80, 800)
    pos2 = (70, 800)
    pos3 = (90, 800)
    draw_circle(pos1, blackColor, playScreen)
    draw_circle(pos2, blackColor, playScreen)
    draw_circle(pos3, blackColor, playScreen)

    while True:
        playScreen.blit(background, (0, 0))

        play_mouse_pos = pygame.mouse.get_pos()

        diceRoll = pygamebutton.Button(image=None, pos=(300, 100), text_input="Roll",
                                       font=smallFont, base_color=blackColor, hovering_color=langColor)
        for button in [diceRoll]:
            button.changeColor(play_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if diceRoll.checkForInput(play_mouse_pos):
                    diceRoll = GameFunctions.roll_dice(diceVal)

        pygame.display.update()


def play_four():
    pygame.display.set_caption("Trivia")
    pos1 = (80, 800)
    pos2 = (70, 800)
    pos3 = (90, 800)
    pos4 = (100, 800)
    draw_circle(pos1, blackColor, playScreen)
    draw_circle(pos2, blackColor, playScreen)
    draw_circle(pos3, blackColor, playScreen)
    draw_circle(pos4, blackColor, playScreen)

    while True:
        playScreen.blit(background, (0, 0))

        playMousePos = pygame.mouse.get_pos()

        roll_dice_button = pygamebutton.Button(image=None, pos=(300, 100), text_input="Roll",
                                               font=smallFont, base_color=blackColor, hovering_color=langColor)
        for button in [roll_dice_button]:
            button.changeColor(playMousePos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if roll_dice_button.checkForInput(playMousePos):
                    diceRoll = GameFunctions.roll_dice(diceVal)

        pygame.display.update()


def options():
    pygame.display.set_caption("Options")

    while True:
        screen.fill(whiteColor)

        option_mouse_pos = pygame.mouse.get_pos()

        option_text = smallFont.render("OPTIONS", True, blackColor)
        optionRect = option_text.get_rect(center=(800, 100))
        dice_text = smallFont.render("Dice Options", True, blackColor)
        dice_rect = dice_text.get_rect(center=(1000, 200))
        playerText = smallFont.render("Player Options", True, blackColor)
        playerRect = playerText.get_rect(center=(600, 200))

        diceFourButton = pygamebutton.Button(image=None, pos=(1000, 300), text_input="Four",
                                             font=smallFont, base_color=blackColor, hovering_color=langColor)
        diceSixButton = pygamebutton.Button(image=None, pos=(1000, 450), text_input="Six",
                                            font=smallFont, base_color=blackColor, hovering_color=langColor)
        diceTwelveButton = pygamebutton.Button(image=None, pos=(1000, 600), text_input='Twelve',
                                               font=smallFont, base_color=blackColor, hovering_color=langColor)
        diceTwentyButton = pygamebutton.Button(image=None, pos=(1000, 750), text_input='Twenty',
                                               font=smallFont, base_color=blackColor, hovering_color=langColor)
        backButton = pygamebutton.Button(image=None, pos=(100, 100), text_input='BACK',
                                         font=smallFont, base_color=blackColor, hovering_color=langColor)
        playerOneButton = pygamebutton.Button(image=None, pos=(600, 300), text_input='One',
                                              font=smallFont, base_color=blackColor, hovering_color=langColor)
        playerTwoButton = pygamebutton.Button(image=None, pos=(600, 450), text_input='Two',
                                              font=smallFont, base_color=blackColor, hovering_color=langColor)
        playerThreeButton = pygamebutton.Button(image=None, pos=(600, 600), text_input='Three',
                                                font=smallFont, base_color=blackColor, hovering_color=langColor)
        playerFourButton = pygamebutton.Button(image=None, pos=(600, 750), text_input='Four',
                                               font=smallFont, base_color=blackColor, hovering_color=langColor)

        screen.blit(dice_text, dice_rect)
        screen.blit(option_text, optionRect)
        screen.blit(playerText, playerRect)

        for button in [diceFourButton, diceSixButton, diceTwelveButton, diceTwentyButton, backButton, playerOneButton,
                       playerTwoButton, playerThreeButton, playerFourButton]:
            button.changeColor(option_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if diceFourButton.checkForInput(option_mouse_pos):
                    diceVal = 4
                if diceSixButton.checkForInput(option_mouse_pos):
                    diceVal = 6
                if diceTwelveButton.checkForInput(option_mouse_pos):
                    diceVal = 12
                if diceTwentyButton.checkForInput(option_mouse_pos):
                    diceVal = 20
                if backButton.checkForInput(option_mouse_pos):
                    menu()
                if playerOneButton.checkForInput(option_mouse_pos):
                    players = 1
                if playerTwoButton.checkForInput(option_mouse_pos):
                    players = 2
                if playerThreeButton.checkForInput(option_mouse_pos):
                    players = 3
                if playerFourButton.checkForInput(option_mouse_pos):
                    players = 4

        pygame.display.update()


def menu():
    pygame.display.set_caption("Menu")

    while True:

        screen.fill(whiteColor)

        menuMousePos = pygame.mouse.get_pos()

        menuText = smallFont.render("MAIN MENU", True, blackColor)
        menuRect = menuText.get_rect(center=(800, 100))

        playButton = pygamebutton.Button(image=None, pos=(800, 250), text_input="PLAY",
                                         font=smallFont, base_color=blackColor, hovering_color=langColor)
        optionButton = pygamebutton.Button(image=None, pos=(800, 400), text_input="Dice Options",
                                           font=smallFont, base_color=blackColor, hovering_color=langColor)
        quitButton = pygamebutton.Button(image=None, pos=(800, 550), text_input="Quit",
                                         font=smallFont, base_color=blackColor, hovering_color=langColor)

        screen.blit(menuText, menuRect)

        for button in [playButton, optionButton, quitButton]:
            button.changeColor(menuMousePos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(menuMousePos):
                    if players == 1:
                        play_one()
                    if players == 2:
                        play_two()
                    if players == 3:
                        play_three()
                    if players == 4:
                        play_four()
                if optionButton.checkForInput(menuMousePos):
                    options()
                if quitButton.checkForInput(menuMousePos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def draw_circle(pos, color, display):
    pygame.draw.circle(display, color, pos, 10)

def trivia(lst_qa, ran_lst):
    questions = lst_qa[0]
    answer = lst_qa[1]

    choice_one = ran_lst[0]
    choice_two = ran_lst[1]
    choice_three = ran_lst[2]
    choice_four = ran_lst[3]

    #create new screen
    #show question with choices below
    #make choices button
    #answer check true


menu()
#play_one()
