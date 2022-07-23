import random
import prompt


def generate_progss(init, step, length):
    """Generate 'length' elements of arifmetical progression from 'init'"""
    res = [init]
    i = 1
    while i < length:
        res.append(init + step * i)
        i += 1
    return res


def miss_and_print(progression):
    """Print elements form 'progression' exept one random replaced by '...', return missing element"""
    missing_element_position = random.randint(0, len(progression) - 1)
    i = 0
    result_string = 'Question: '
    while i <= len(progression) - 1:
        if i == missing_element_position:
            result_string = result_string + '... '
        else:
            result_string = result_string + str(progression[i]) + ' '
        i += 1
    print(result_string)
    return progression[missing_element_position]


def progss(user_name, num_of_attempts, difficulty, maximum_step_of_progression, len_of_progression):
    print('What number is missing in the progression?')
    scores = 0
    while scores < num_of_attempts:
        init = random.randint(0, difficulty)
        step = random.randint(1, maximum_step_of_progression)

        # generate progression, print it, return missing number ('correct_answer')
        correct_answer = miss_and_print(generate_progss(init, step, len_of_progression))

        answer = prompt.integer('Your answer: ')
        if answer == correct_answer:
            scores += 1
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            scores = num_of_attempts + 1  # stop the game
    if scores == num_of_attempts:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    progss("test", 3, 99, 10, 10)
