import random


# constants
MAXIMUM_STEP_OF_PROGRESSION = 10  # maximum step of arifmetical progression
MIN_LEN_OF_PROGRESSION = 5  # minimum quantity of numbers of progression
REC_LEN_OF_PROGRESSION = 10  # recommended numbers of progression to generate


def make_progss(initial_term, common_difference, length):
    """Generates an arithmetic progression"""
    progression = [initial_term]
    i = 1
    while i < length:
        progression.append(initial_term + common_difference * i)
        i += 1
    return progression


def stringify(progression, missing_element_position):
    """Print elements from 'progression' exept one\
        at 'missing_element_position' wich replaced by '..'. Return string"""
    i = 0
    result_string = ''
    while i <= len(progression) - 1:
        if i == missing_element_position:
            result_string = result_string + '.. '
        else:
            result_string = result_string + str(progression[i]) + ' '
        i += 1
    return result_string


def progss(max_init):
    '''Progression. Generate arifmetical progression.
        Return 'rule_string, 'question_string'
        and 'correct_answer' (missing element, string)'''

    rule_string = 'What number is missing in the progression?'

    # generate progression
    init = random.randrange(0, max_init)
    diff = random.randrange(1, MAXIMUM_STEP_OF_PROGRESSION)
    length = random.randrange(MIN_LEN_OF_PROGRESSION, REC_LEN_OF_PROGRESSION)
    progression = make_progss(init, diff, length)

    # make one element missing
    missing_element_position = random.randint(0, len(progression) - 1)
    question_string = stringify(progression, missing_element_position)

    return (rule_string,
            question_string,
            str(progression[missing_element_position]))  # correct answer
