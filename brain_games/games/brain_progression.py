import random
import prompt
from brain_games.brain_servicelib import check_and_print_answer, hello


# constants
MAXIMUM_STEP_OF_PROGRESSION = 10  # maximum step of arifmetical progression
MIN_LEN_OF_PROGRESSION = 5  # minimum quantity of numbers of progression
REC_LEN_OF_PROGRESSION = 10  # recommended numbers of progression to generate


def generate_progss(init, step, length):
    """Generate 'length' elements of arifmetical progression from 'init'"""
    res = [init]
    i = 1
    while i < length:
        res.append(init + step * i)
        i += 1
    return res


def miss_and_print(progression):
    """Print elements form 'progression' exept one random\
        replaced by '...', return missing element"""
    missing_element_position = random.randint(0, len(progression) - 1)
    i = 0
    result_string = 'Question:'
    while i <= len(progression) - 1:
        if i == missing_element_position:
            result_string = result_string + '... '
        else:
            result_string = result_string + str(progression[i]) + ' '
        i += 1
    print(result_string)
    return progression[missing_element_position]


def progss(num_of_attempts=3, max_init=20):
    # (num_of_attempts=3, max_init=20, max_step=10, min_len=5, rec_len=10):
    user_name = hello()

    print('What number is missing in the progression?')
    scores = 0
    while scores < num_of_attempts:
        init = random.randrange(0, max_init)
        step = random.randrange(1, MAXIMUM_STEP_OF_PROGRESSION)
        len = random.randrange(MIN_LEN_OF_PROGRESSION, REC_LEN_OF_PROGRESSION)

        # generate progression, print it, return missing number
        correct_answer = miss_and_print(generate_progss
                                        (init, step, len))

        answer = prompt.integer('Your answer: ')

        if check_and_print_answer(answer, correct_answer):
            scores += 1
        else:
            scores = num_of_attempts + 1  # stop the game

    if (scores == num_of_attempts):  # check if win a game
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")


if __name__ == '__main__':
    progss()
