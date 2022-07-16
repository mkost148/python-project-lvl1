"""Import something..."""
import prompt


"""Describe something"""


def welcome_user():
    return prompt.string('May I have your name? ')


if __name__ == '__main__':
    welcome_user()
