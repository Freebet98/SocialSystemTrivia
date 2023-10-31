import pygame
import sys
from pygame.locals import *

# initialize constructor
pygame.init()

# screen ize
width = 1600
height = 900

# open window
window = pygame.display.set_mode((width, height))

# language color
langColor = (111, 191, 87)

# Employment color
employColor = (171, 147, 197)

# Culture Color
cultColor = (226, 145, 190)

# Relationship Color
RelatColor = (61, 142, 204)

# Black Color
blackColor = (35, 31, 32)

# white Color
whiteColor = ()

# light shade of button
color_light = (170, 170, 170)

# dark shade of button
color_dark = (100, 100, 100)

# defining a font
smallFont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in this font
text = smallFont.render('quit', True, color)

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        # check if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the button the game is terminated
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()

    # fill screen with a color
    screen.fill((60, 25, 60))

    # stores the (x,y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

    # superimposing the text onto our button
    screen.blit(text, (width / 2 + 50, height / 2))

    # updates the frames of the game
    pygame.display.update()

bg_img = pygame.image.load('board-01.png')
bg_img = pygame.transform.scale(bg_img, (width, height))

running = True

while running:
    window.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()
pygame.quit()
