import prompt
from brain_games.brain_go import NUM_OF_ATTEMPTS,\
    hello, check_and_print_answer, gcd


def main():
    user_name = hello()
    print('Find the greatest common divisor of given numbers.')
    scores = 0
    while scores < NUM_OF_ATTEMPTS:
        (question_string, correct_answer) = gcd()
        print(question_string)
        answer = int(prompt.string('Your answer: '))
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
