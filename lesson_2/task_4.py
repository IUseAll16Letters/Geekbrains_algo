"""4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры."""


def recur_elements_summation(n: int):
    while n:
        return 1 / ((-2) ** (n-1)) + recur_elements_summation(n-1)
    return 0


def normal_elements_summation(n: int):
    item = 1
    summary = 0
    for i in range(n):
        summary += item
        item /= -2
    return summary


if __name__ == '__main__':
    row_length = int(input('Enter the length of summarized row: '))
    print(recur_elements_summation(row_length))
    print(normal_elements_summation(row_length))
