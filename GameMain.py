import GameFunctions


def play_game():
    dice_val = 6  # Constant
    board_length = 49  # Constant
    counter = 0

    while 1:
        if counter >= board_length:
            break
        print(counter)
        roll = GameFunctions.roll_dice(dice_val)
        print(roll)
        word = GameFunctions.check_spot(roll, counter)
        print(word)

        statement = GameFunctions.switch_dict(word)
        print(statement)
        lst_qa = statement[0]
        ran_lst = statement[1]
        print(lst_qa[0])
        print(ran_lst)
        print("What is the Answer?")
        user_val = input("Enter a Number 1 - 4")
        if ran_lst[int(user_val) - 1] == lst_qa[int(user_val) - 1]:
            counter += roll
            continue
        else:
            continue

    return 0


def main():
    play_game()
    return 0


if __name__ == "__main__":
    main()
