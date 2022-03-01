"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""


def count_digits_in_number(number: int, digit: int):
    number, digit = map(int, (number, digit))
    digit_counter = 0
    while number:
        if number % 10 == digit:
            digit_counter += 1
        number //= 10
    return f"There {'are' if digit_counter > 1 else 'is'} " \
           f"{digit_counter} '{digit}' digit{'s' if digit_counter > 1 else ''} in entered number."


def string_counter(number, digit):
    return f"There are {number.count(digit)} digit(s) in number {number}. "


if __name__ == '__main__':
    user_number = input('Enter number where you want to calculate digits: ')
    user_digit = input('Enter digit you want to calculate: ')
    print(count_digits_in_number(int(user_number), int(user_digit)))
    print(string_counter(user_number, user_digit))