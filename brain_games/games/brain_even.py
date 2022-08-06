import prompt
from brain_games.brain_go import NUM_OF_ATTEMPTS,\
    hello, check_and_print_answer, even


def main():
    user_name = hello()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    scores = 0
    while scores < NUM_OF_ATTEMPTS:
        (question_string, correct_answer) = even()
        print(question_string)
        answer = str.lower(prompt.string('Your answer: '))
        if check_and_print_answer(answer, correct_answer):
            scores += 1
        else:
            scores = NUM_OF_ATTEMPTS + 1  # stop the game
    if (scores == NUM_OF_ATTEMPTS):  # check if win a game
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")


if __name__ == '__main__':
    main()
