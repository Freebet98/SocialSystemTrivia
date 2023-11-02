import sys
import pygame
import pygamebutton
import GameFunctions

# initialize constructor
pygame.init()
# Variables
# screen size
width = 1500
height = 800

# button size
bWidth = 150
bheight = 75

bAWidth = 75
bAHeight = 75

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
smallFont = pygame.font.SysFont('Rockwell', 20)
largeFont = pygame.font.SysFont('Rockwell', 40)
mediumFont = pygame.font.SysFont('Rockwell', 30)
cardFont = pygame.font.SysFont('Rockwell', 50)

# images
background = pygame.image.load('board-01.png')
background = pygame.transform.scale(background, (width, height))
langCard = pygame.image.load('Langauge2-01.jpg')
langCard = pygame.transform.scale(langCard, (width, height))
employCard = pygame.image.load('Employment2-01.jpg')
employCard = pygame.transform.scale(employCard, (width, height))
cultCard = pygame.image.load('Culture2-01.jpg')
cultCard = pygame.transform.scale(cultCard, (width, height))
relateCard = pygame.image.load('Relationship2-01.jpg')
relateCard = pygame.transform.scale(relateCard, (width, height))
purpleButton = pygame.image.load('free button purple.png')
purpleButton = pygame.transform.scale(purpleButton, (bWidth, bheight))
pinkButton = pygame.image.load('free button pink.png')
pinkButton = pygame.transform.scale(pinkButton, (bWidth, bheight))
greenButton = pygame.image.load('free button green.png')
greenButton = pygame.transform.scale(greenButton, (bWidth, bheight))
blueButton = pygame.image.load('free button blue.png')
blueButton = pygame.transform.scale(blueButton, (bWidth, bheight))
menuOption01 = pygame.image.load('card menuu-01.png')
menuOption01 = pygame.transform.scale(menuOption01, (width, height))
menuOption02 = pygame.image.load('card menu again-01.png')
menuOption02 = pygame.transform.scale(menuOption02, (width, height))

# Button photos Trivia
purpleButtonA = pygame.transform.scale(purpleButton, (bAWidth, bAHeight))
pinkButtonA = pygame.transform.scale(pinkButton, (bAWidth, bAHeight))
greenButtonA = pygame.transform.scale(greenButton, (bAWidth, bAHeight))
blueButtonA = pygame.transform.scale(blueButton, (bAWidth, bAHeight))

# open window
screen = pygame.display.set_mode((width, height))
playScreen = pygame.display.set_mode((width, height))
triviaScreen = pygame.display.set_mode((width, height))

# rendering a text written in this font
text = smallFont.render('quit', True, whiteColor)

# dice value
diceVal = 6
players = 1
answer = False
boardArr = [(125, 700), (250, 650), (350, 675), (450, 725), (650, 700), (800, 700), (900, 700), (1050, 725),
            (1150, 750),(1250, 750), (1400, 700), (1350, 600), (1250, 600), (1050, 600), (1100, 525), (1250, 525),
            (1250, 450), (1150, 400), (1050, 425), (900, 450),(800, 500), (650, 550), (500, 550),(350, 550), (250, 550),
            (100, 500), (100, 400), (150, 350), (300, 375), (400, 425), (500, 300), (650, 250), (750, 275), (900, 300),
            (975, 275), (1125, 275), (1250, 275), (1350, 275), (1400, 175), (1350, 50), (1175, 75), (1075, 100),
            (975, 150), (825, 155),(650,100), (600,100), (450,150),]


def play_one():
    pygame.display.set_caption("Trivia")
    pos = boardArr[0]
    counter = 0
    dice_roll = 0

    while True:
        playScreen.blit(background, (0, 0))

        playMousePos = pygame.mouse.get_pos()

        rollDiceButton = pygamebutton.Button(image=pinkButton, pos=(300, 100), text_input="Roll",
                                             font=smallFont, base_color=blackColor, hovering_color=cultColor)
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
                        if trivia(lst_qa, ran_lst, category):
                            pos += counter

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

        option_text = largeFont.render("OPTIONS", True, blackColor)
        optionRect = option_text.get_rect(center=(750, 100))
        dice_text = mediumFont.render("Dice Options", True, blackColor)
        dice_rect = dice_text.get_rect(center=(950, 200))
        playerText = mediumFont.render("Player Options", True, blackColor)
        playerRect = playerText.get_rect(center=(550, 200))

        diceFourButton = pygamebutton.Button(image=pinkButton, pos=(950, 300), text_input="Four",
                                             font=smallFont, base_color=blackColor, hovering_color=cultColor)
        diceSixButton = pygamebutton.Button(image=purpleButton, pos=(950, 450), text_input="Six",
                                            font=smallFont, base_color=blackColor, hovering_color=employColor)
        diceTwelveButton = pygamebutton.Button(image=greenButton, pos=(950, 600), text_input='Twelve',
                                               font=smallFont, base_color=blackColor, hovering_color=langColor)
        diceTwentyButton = pygamebutton.Button(image=blueButton, pos=(950, 750), text_input='Twenty',
                                               font=smallFont, base_color=blackColor, hovering_color=relaColor)
        backButton = pygamebutton.Button(image=pinkButton, pos=(100, 100), text_input='BACK',
                                         font=smallFont, base_color=blackColor, hovering_color=cultColor)
        playerOneButton = pygamebutton.Button(image=pinkButton, pos=(550, 300), text_input='One',
                                              font=smallFont, base_color=blackColor, hovering_color=cultColor)
        playerTwoButton = pygamebutton.Button(image=purpleButton, pos=(550, 450), text_input='Two',
                                              font=smallFont, base_color=blackColor, hovering_color=employColor)
        playerThreeButton = pygamebutton.Button(image=greenButton, pos=(550, 600), text_input='Three',
                                                font=smallFont, base_color=blackColor, hovering_color=langColor)
        playerFourButton = pygamebutton.Button(image=blueButton, pos=(550, 750), text_input='Four',
                                               font=smallFont, base_color=blackColor, hovering_color=relaColor)

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
        screen.fill(blackColor)
        screen.blit(menuOption02, (0, 0))

        menuMousePos = pygame.mouse.get_pos()

        menuText = largeFont.render("MAIN MENU", True, whiteColor)
        menuRect = menuText.get_rect(center=(750, 100))

        playButton = pygamebutton.Button(image=purpleButton, pos=(750, 250), text_input="PLAY",
                                         font=smallFont, base_color=blackColor, hovering_color=employColor)
        optionButton = pygamebutton.Button(image=greenButton, pos=(750, 400), text_input="Dice Options",
                                           font=smallFont, base_color=blackColor, hovering_color=langColor)
        quitButton = pygamebutton.Button(image=blueButton, pos=(750, 550), text_input="Quit",
                                         font=smallFont, base_color=blackColor, hovering_color=relaColor)

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
    pygame.draw.circle(display, color, pos, 7)


def trivia(lst_qa, ran_lst, category):
    questions = lst_qa[0]
    answerFinal = lst_qa[1]

    choice_one = ran_lst[0]
    choice_two = ran_lst[1]
    choice_three = ran_lst[2]
    choice_four = ran_lst[3]

    match category:
        case "employment":
            pygame.display.set_caption("Employment")
            window = employCard
        case "culture":
            pygame.display.set_caption("Culture")
            window = cultCard
        case "relationships":
            pygame.display.set_caption("Relationships")
            window = relateCard
        case "language":
            pygame.display.set_caption("Language")
            window = langCard
        case _:
            raise ValueError("Case should be a string of either employment, culture, relationships, or language")

    while True:
        triviaScreen.blit(window, (0, 0))
        triviaMousePos = pygame.mouse.get_pos()

        questionText = cardFont.render(questions, True, blackColor)
        questionRect = questionText.get_rect(center=(280, 100))

        choiceOneText = mediumFont.render(choice_one, True, blackColor)
        choiceOneRect = choiceOneText.get_rect(center = (350, 200))

        choiceTwoText = mediumFont.render(choice_two, True, blackColor)
        choiceTwoRect = choiceTwoText.get_rect(center=(350, 350))

        choiceThreeText = mediumFont.render(choice_three, True, blackColor)
        choiceThreeRect = choiceThreeText.get_rect(center=(350, 500))

        choiceFourText = mediumFont.render(choice_four, True, blackColor)
        choiceFourRect = choiceFourText.get_rect(center=(350, 650))

        answerOneButton = pygamebutton.Button(image=pinkButtonA, pos=(280, 200), text_input='A',
                                              font=mediumFont, base_color=blackColor, hovering_color=cultColor)
        answerTwoButton = pygamebutton.Button(image=purpleButtonA, pos=(280, 350), text_input='B',
                                              font=mediumFont, base_color=blackColor, hovering_color=employColor)
        answerThreeButton = pygamebutton.Button(image=greenButtonA, pos=(280, 500), text_input='C',
                                                font=mediumFont, base_color=blackColor, hovering_color=langColor)
        answerFourButton = pygamebutton.Button(image=blueButtonA, pos=(280, 650), text_input='D',
                                               font=mediumFont, base_color=blackColor, hovering_color=relaColor)

        for button in [answerOneButton, answerTwoButton, answerThreeButton, answerFourButton]:
            button.changeColor(triviaMousePos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if answerOneButton.checkForInput(triviaMousePos):
                    return answerShow(choice_one, answerFinal, window)
                if answerTwoButton.checkForInput(triviaMousePos):
                    return answerShow(choice_two, answerFinal, window)
                if answerThreeButton.checkForInput(triviaMousePos):
                    return answerShow(choice_three, answerFinal, window)
                if answerFourButton.checkForInput(triviaMousePos):
                    return answerShow(choice_four, answerFinal, window)

        screen.blit(questionText, questionRect)
        screen.blit(choiceOneText, choiceOneRect)
        screen.blit(choiceTwoText, choiceTwoRect)
        screen.blit(choiceThreeText, choiceThreeRect)
        screen.blit(choiceFourText, choiceFourRect)

        pygame.display.update()


def answerShow(choice, answerFinal, window):
    pygame.display.set_caption("Answer")
    triviaScreen.blit(window, (0,0))

    while True:
        answerText = cardFont.render(answerFinal, True, blackColor)
        answerRect = answerText.get_rect(center=(280, 100))

        screen.blit(answerText, answerRect)

        pygame.display.update()

        pygame.time.delay(15000)

        return choice == answer

def board(boardArr):
    while True:
        playScreen.blit(background, (0,0))
        for point in boardArr:
            draw_circle(point, blackColor, playScreen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


# menu()
#play_one()
board(boardArr)

