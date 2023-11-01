import sys

import pygame

import pygamebutton

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
playScreen = pygame.display.set_mode((width,height))
triviaScreen = pygame.display.set_mode((width,height))

# rendering a text written in this font
text = smallFont.render('quit', True, whiteColor)

# dice value
diceVal = 6
players = 2


def play():
    pygame.display.set_caption("Trivia")

    while True:
        playScreen.blit(background, (0,0))

        playMousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def options():
    pygame.display.set_caption("Options")

    while True:
        screen.fill(whiteColor)

        optionMousePos = pygame.mouse.get_pos()

        optionText = smallFont.render("OPTIONS", True, blackColor)
        optionRect = optionText.get_rect(center=(800, 100))
        diceText = smallFont.render("Dice Options", True, blackColor)
        diceRect = diceText.get_rect(center=(1000, 200))
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

        screen.blit(diceText, diceRect)
        screen.blit(optionText, optionRect)
        screen.blit(playerText, playerRect)

        for button in [diceFourButton, diceSixButton, diceTwelveButton, diceTwentyButton, backButton, playerOneButton,
                       playerTwoButton, playerThreeButton, playerFourButton]:
            button.changeColor(optionMousePos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if diceFourButton.checkForInput(optionMousePos):
                    diceVal = 4
                if diceSixButton.checkForInput(optionMousePos):
                    diceVal = 6
                if diceTwelveButton.checkForInput(optionMousePos):
                    diceVal = 12
                if diceTwentyButton.checkForInput(optionMousePos):
                    diceVal = 20
                if backButton.checkForInput(optionMousePos):
                    menu()
                if playerOneButton.checkForInput(optionMousePos):
                    players = 1
                if playerTwoButton.checkForInput(optionMousePos):
                    players = 2
                if playerThreeButton.checkForInput(optionMousePos):
                    players = 3
                if playerFourButton.checkForInput(optionMousePos):
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
                    play()
                if optionButton.checkForInput(menuMousePos):
                    options()
                if quitButton.checkForInput(menuMousePos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


menu()
