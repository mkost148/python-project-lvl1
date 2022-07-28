import prompt


def hello():
    """Ask for user name"""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def check_and_print_answer(answer, correct_answer):
    """Return (answer == correct answer) and print corresponding message"""
    if answer == correct_answer:
        print('Correct!')
    else:
        print("'", answer, "' is wrong answer ;(."
              " Correct answer was '", correct_answer, "'."
              )
    return (answer == correct_answer)


def main():
    return


if __name__ == '__main__':
    main()
