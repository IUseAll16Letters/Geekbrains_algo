"""6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
 Если за 10 попыток число не отгадано, то вывести загаданное число."""
from random import randint


def guess_quizz():
    number_to_guess = randint(1, 100)

    for attempt in range(1, 11):
        user_input = int(input('Try to guess a number between 1 and 100: '))
        if user_input == number_to_guess:
            print(f"Congrants, guessed number was {number_to_guess} you've won after {attempt} attempt")
            break
        if user_input > number_to_guess:
            print(f"Your number is bigger than guessed one. You have {10 - attempt} tries left. ")
        else:
            print(f'Your number is smaller than guessed one. You have {10 - attempt} left. ')


if __name__ == '__main__':
    guess_quizz()