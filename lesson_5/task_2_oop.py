"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого это цифры числа. 
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""

from random import randint
hex_nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')


class Hex:
    def __init__(self, value):
        self.value = list(value)

    def __str__(self):
        return '0x' + f"{''.join(self.value)}"

    def __format__(self, format_spec):
        return str(self)

    def __add__(self, other):
        first, second = self.value, other.value
        max_size = max((len(first), len(second)))
        first, second = ['0'] * (max_size - len(first)) + first, \
                        ['0'] * (max_size - len(second)) + second

        result, remainder = [], 0
        for idx in range(max_size - 1, - 1, -1):
            sum_res = hex_nums.index(first[idx]) + hex_nums.index(second[idx]) + remainder
            if sum_res >= 16:
                remainder = 1
                sum_res -= 16
            else:
                remainder = 0
            result.append(hex_nums[sum_res - 16])

        if remainder:
            result.append(hex_nums[remainder])

        return Hex(result[::-1])

    def __mul__(self, other):
        if len(self.value) >= len(other.value):
            first, second = tuple(reversed(other.value)), tuple(reversed(self.value))
        else:
            first, second = tuple(reversed(self.value)), tuple(reversed(other.value))

        result = Hex('0')
        for division, digit in enumerate(first):
            if digit != '0':
                remainder = 0
                temp_res = []
                for j in second:
                    calc = hex_nums.index(digit) * hex_nums.index(j) + remainder
                    temp_res.append(hex_nums[calc % 16])
                    remainder = calc // 16
                if remainder:
                    temp_res.append(hex_nums[remainder])
                result = result + Hex(temp_res[::-1] + ['0'] * division)

        return result


if __name__ == '__main__':
    for _ in range(10):
        num_1 = randint(1, 5000)
        num_2 = randint(1, 5000)
        sum_1 = hex(num_1 + num_2)
        mult_1 = hex(num_1 * num_2)

        num_1 = Hex(hex(num_1).replace('0x', ''))
        num_2 = Hex(hex(num_2).replace('0x', ''))
        sum_2 = '0x' + ''.join((num_1 + num_2).value)
        mult_2 = '0x' + ''.join((num_1 * num_2).value)

        print(f'numbers: {str(num_1):>7}, {str(num_2):>7}; '
              f'[{sum_1:<7}|{sum_2:>7}]; [{mult_1:<10}|{mult_2:>10}]; '
              f'is_identical: \033[95m{sum_1 == sum_2 and mult_1 == mult_2}\033[0m')

# numbers:    0x7e,   0x1f4; [0x272  |  0x272]; [0xf618    |    0xf618]; is_identical: True
# numbers:   0xbe0,   0x1eb; [0xdcb  |  0xdcb]; [0x16c6a0  |  0x16c6a0]; is_identical: True
# numbers:   0xdf3,   0x5a5; [0x1398 | 0x1398]; [0x4ebc9f  |  0x4ebc9f]; is_identical: True
# numbers:  0x117a,   0x1fc; [0x1376 | 0x1376]; [0x22ae18  |  0x22ae18]; is_identical: True
# numbers:   0x44b,   0x50d; [0x958  |  0x958]; [0x15aecf  |  0x15aecf]; is_identical: True
# numbers:   0xd8b,  0x121a; [0x1fa5 | 0x1fa5]; [0xf5261e  |  0xf5261e]; is_identical: True
# numbers:   0x813,   0x663; [0xe76  |  0xe76]; [0x339159  |  0x339159]; is_identical: True
# numbers:   0x2ef,    0xcb; [0x3ba  |  0x3ba]; [0x25385   |   0x25385]; is_identical: True
# numbers:   0xd82,   0x7a6; [0x1528 | 0x1528]; [0x67504c  |  0x67504c]; is_identical: True
# numbers:   0x31a,   0x779; [0xa93  |  0xa93]; [0x172d4a  |  0x172d4a]; is_identical: True
