import random
import prompt


def is_prime(number):
    """Check if 'number' is prime. Returns boolean"""
    if abs(number) <= 3:
        return True
    i = 2
    max_i = number // 2
    while i <= max_i:
        if number % i == 0:
            # uncomment the following for test
            # print('can be divided by ', str(i)) 
            return False
        i += 1
    return True


def prime(user_name, num_of_attempts, difficulty):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    scores = 0
    while scores < num_of_attempts:

        number = random.randint(2, difficulty)  # '1' is not prime nor combined number
        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print('Question: ', str(number))
        answer = str.lower(prompt.string('Your answer: '))

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
    prime("test", 3, 99)
