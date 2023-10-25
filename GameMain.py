import GameFunctions


def play_game():
    dice_val = 6  # Constant
    board_length = 49  # Constant
    counter = 0

    while 1:
        if counter >= board_length:
            break

        roll = GameFunctions.roll_dice(dice_val)
        word = GameFunctions.check_spot(roll, counter)

        statement = GameFunctions.switch_dict(word)
        lst_qa = statement[0]
        ran_lst = statement[1]
        print(ran_lst)


        counter += roll
