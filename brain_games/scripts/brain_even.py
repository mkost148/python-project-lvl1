import prompt
import random


def is_even(num):
    '''Check if num is even or odd'''
    return (num % 2) == 0


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, ', user_name, '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    scores = 0
    while scores < 3:
        num = random.randint(0, 65535)
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
            scores = 99
    if scores == 3:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
