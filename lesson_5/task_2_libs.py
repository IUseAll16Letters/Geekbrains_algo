"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""

from collections import deque
from random import randint

hex_numbers = {hex(i).replace('0x', ''): i for i in range(16)}
dec_numbers = hex_numbers
hex_numbers = list(hex_numbers)


def sum_hex(first, second):
    first, second = first.copy(), second.copy()
    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))
    result = deque()
    remainder = 0

    for i in range(len(first) - 1, -1, -1):
        first_num = dec_numbers[first[i]]
        second_num = dec_numbers[second[i]]
        result_num = first_num + second_num + remainder

        if result_num >= 16:
            remainder = 1
            result_num -= 16
        else:
            remainder = 0

        result.appendleft(hex_numbers[result_num])

    if remainder:
        result.appendleft('1')

    return result


# Hellish recursion
def mult_hex(first, second):
    first, second = first.copy(), second.copy()
    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))
    result = deque('0')

    for i in range(len(first) - 1, -1, -1):
        second_num = dec_numbers[second[i]]
        remainder = deque('0')
        for _ in range(second_num):
            remainder = sum_hex(remainder, first)

        remainder.extend('0' * (len(first) - i - 1))
        result = sum_hex(result, remainder)
    return result


if __name__ == '__main__':
    for i in range(10):
        a = randint(1, 1000)
        b = randint(1, 1000)
        hex_a, hex_b = map(lambda i: deque(hex(i).replace('0x', '')), (a, b))

        sum_1 = hex(a + b)
        sum_2 = sum_hex(hex_a, hex_b)
        mult_1 = hex(a * b)
        mult_2 = mult_hex(hex_a, hex_b)
        hex_a, hex_b, sum_2, mult_2 = map(lambda i: '0x' + ''.join(tuple(i)), (hex_a, hex_b, sum_2, mult_2))

        print(f"numbers: {hex_a:<5}, {hex_b:<5}; sum: [{sum_1:<6}|{sum_2:>6}] "
              f"mult: [{mult_1:<8}|{mult_2:>8}] "
              f"is_identical: \033[95m{sum_1 == sum_2 and mult_1 == mult_2}\033[0m")

# numbers: 0x1ba, 0x1cc; sum: [0x386 | 0x386] mult: [0x31a38 | 0x31a38] is_identical: True
# numbers: 0x262, 0x25 ; sum: [0x287 | 0x287] mult: [0x582a  |  0x582a] is_identical: True
# numbers: 0x2ec, 0xf5 ; sum: [0x3e1 | 0x3e1] mult: [0x2cbdc | 0x2cbdc] is_identical: True
# numbers: 0x13a, 0xb8 ; sum: [0x1f2 | 0x1f2] mult: [0xe1b0  |  0xe1b0] is_identical: True
# numbers: 0x362, 0x26e; sum: [0x5d0 | 0x5d0] mult: [0x8381c | 0x8381c] is_identical: True
# numbers: 0x13 , 0x2c2; sum: [0x2d5 | 0x2d5] mult: [0x3466  |  0x3466] is_identical: True
# numbers: 0xb2 , 0x138; sum: [0x1ea | 0x1ea] mult: [0xd8f0  |  0xd8f0] is_identical: True
# numbers: 0x117, 0x2b0; sum: [0x3c7 | 0x3c7] mult: [0x2edd0 | 0x2edd0] is_identical: True
# numbers: 0x332, 0x3d7; sum: [0x709 | 0x709] mult: [0xc44fe | 0xc44fe] is_identical: True
# numbers: 0x163, 0xdd ; sum: [0x240 | 0x240] mult: [0x13277 | 0x13277] is_identical: True