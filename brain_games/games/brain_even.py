import random
import prompt


def is_even(num):
    """Check if 'num' is even or odd"""
    return (num % 2) == 0


def even(user_name, num_of_attempts, difficulty):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    scores = 0
    while scores < num_of_attempts:
        num = random.randint(0, difficulty)
        print('Question: ', str(num))

        if is_even(num):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        answer = str.lower(prompt.string('Your answer: '))

        if answer == correct_answer:
            scores += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.\
                Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            scores = num_of_attempts + 1  # stop the game
    if scores == num_of_attempts:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    even("test", 3, 99)
