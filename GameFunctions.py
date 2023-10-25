import Culture
import Language
import Relationships
import Employment
import random


def roll_dice(max_num):
    """ roll_dice takes in an int and will return a random number between 1 and max_num """
    num = random.randrange(1, max_num)
    return num


def check_spot(dice_roll, current_count):
    """Check_spot will determine whether the spot is meant to be culture, language, relationships,
    or employment for trivia"""
    count = current_count + dice_roll

    if count % 4 == 0:
        return "employment"
    elif count % 4 == 1:
        return "culture"
    elif count % 4 == 2:
        return "relationships"
    else:
        return "language"


def randomize_list_order(lst):
    """Takes in a parameter lst which is a list and creates a copy and randomly sorts it"""
    ran_lst = lst.copy()
    ran_lst = random.sample(ran_lst, len(ran_lst))

    return ran_lst


def switch_dict(str_category):
    """This will pass a dictionary into a function and return the tuple from that function based on the case it
    hits"""
    match str_category:
        case "employment":
            lst_qa = dict_to_lst(Employment.employ_dict)
            ran_lst = get_lst_from_answer_dict(Employment.employ_ans_dict, lst_qa[1])
            return lst_qa, ran_lst
        case "culture":
            lst_qa = dict_to_lst(Culture.culture_dict)
            ran_lst = get_lst_from_answer_dict(Culture.culture_ans_dict, lst_qa[1])
            return lst_qa, ran_lst
        case "relationships":
            lst_qa = dict_to_lst(Relationships.relation_dict)
            ran_lst = get_lst_from_answer_dict(Relationships.relation_ans_dict, lst_qa[1])
            return lst_qa, ran_lst
        case "language":
            lst_qa = dict_to_lst(Language.language_dict)
            ran_lst = get_lst_from_answer_dict(Language.language_ans_dict, lst_qa[1])
            return lst_qa, ran_lst
        case _:
            raise ValueError("Case should be a string of either employment, culture, relationships, or language")


def dict_to_lst(dict_trivia):
    num = random.randrange(0, len(dict_trivia))
    keys = list(dict_trivia.keys())
    question = keys[num]
    answer = dict_trivia[num]

    lst_qa = [question, answer]
    return lst_qa


def get_lst_from_answer_dict(dict_trivia, answer):
    ran_lst = dict_trivia[answer]
    ran_lst = randomize_list_order(ran_lst)
    return ran_lst
