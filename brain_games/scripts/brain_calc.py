import random
import prompt


def calc(user_name, num_of_attempts, difficulty):
    oper_sym = ('+', '-', '*')  # three operators are available
    print('What is the result of the expression?')
    scores = 0
    while scores < num_of_attempts:
        num1 = random.randint(0, difficulty)
        num2 = random.randint(0, difficulty)
        oper_type = random.randint(0, 2)  # three operators are available
        print('Question: ', str(num1), ' ', oper_sym[oper_type], ' ', str(num2))

        if oper_type == 0:  # 'plus'
            correct_answer = num1 + num2
        elif oper_type == 1:  # 'minus'
            correct_answer = num1 - num2
        else:  # 'multiply'
            correct_answer = num1 * num2

        answer = int(prompt.string('Your answer: '))

        if answer == correct_answer:
            scores += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.\
                Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            scores = num_of_attempts + 1 #  stop the game
    if scores == num_of_attempts:
        print(f'Congratulations, {user_name}!')

if __name__ == '__main__':
    calc("test", 3, 99)
