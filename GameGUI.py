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
langCard = pygame.image.load('Langauge2-01.jpg')
employCard = pygame.image.load('Employment2-01.jpg')
cultCard = pygame.image.load('Culture2-01.jpg')
relateCard = pygame.image.load('Relationship2-01.jpg')

# open window
screen = pygame.display.set_mode((width, height))

# rendering a text written in this font
text = smallFont.render('quit', True, whiteColor)

def play():
    pass


def options():
    pass


def menu():
    pygame.display.set_caption("Menu")

    while True:

        screen.fill(whiteColor)

        menuMousePos = pygame.mouse.get_pos()

        menuText = smallFont.render("MAIN MENU", True, blackColor)
        menuRect = menuText.get_rect(center=(1400, 600))

        playButton = pygamebutton.Button(image = None, pos = (640, 250), text_input="PLAY",
                                         font = smallFont, base_color = blackColor, hovering_color= langColor)
        optionButton = pygamebutton.Button(image= None, pos=(640, 400), text_input="Option",
                                         font=smallFont, base_color=blackColor, hovering_color=langColor)
        quitButton = pygamebutton.Button(image=None, pos=(640, 550), text_input="Quit",
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