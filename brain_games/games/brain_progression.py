import random


# constants
MAXIMUM_STEP_OF_PROGRESSION = 10  # maximum step of arifmetical progression
MIN_LEN_OF_PROGRESSION = 5  # minimum quantity of numbers of progression
REC_LEN_OF_PROGRESSION = 10  # recommended numbers of progression to generate


def progss(max_init):
    '''Progression. Generate arifmetical progression.
        Return 'rule_string, 'question_string'
        and 'correct_answer' (missing element, string)'''

    rule_string = 'What number is missing in the progression?'

    # generate progression
    init = random.randrange(0, max_init)
    step = random.randrange(1, MAXIMUM_STEP_OF_PROGRESSION)
    lenght = random.randrange(MIN_LEN_OF_PROGRESSION, REC_LEN_OF_PROGRESSION)
    progression = [init]
    i = 1
    while i < lenght:
        progression.append(init + step * i)
        i += 1

    # make one element missing
    missing_element_position = random.randint(0, len(progression) - 1)
    i = 0
    question_string = 'Question: '
    while i <= len(progression) - 1:
        if i == missing_element_position:
            question_string = question_string + '.. '
        else:
            question_string = question_string + str(progression[i]) + ' '
        i += 1

    return (rule_string,
            question_string,
            str(progression[missing_element_position]))
