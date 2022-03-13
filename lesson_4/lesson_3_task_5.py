"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""
from random import randint
from time import perf_counter
import cProfile


# Option 1: using generator
# O(n) for value + O(n) for .index
def find_max_negative_1(values: list) -> tuple:
    value = max(i for i in values if i < 0)
    return value, values.index(value)

# Timings for find_max_negative_1
# 1.1099999999999999e-05
# 0.00023779999999999635
# 0.000444900000000005
# 0.004041099999999992
# 0.04186630000000002


# Option 2 using variables:
# O(n)
def find_max_negative_2(values: list) -> tuple:
    max_negative = float('-inf')
    max_negative_idx = 0
    for order, item in enumerate(values):
        if 0 > item > max_negative:
            max_negative = item
            max_negative_idx = order

    return max_negative, max_negative_idx

# Timings for find_max_negative_2
# 1.3900000000011126e-05
# 5.2399999999952485e-05
# 0.0005836000000000174
# 0.006048899999999913
# 0.05734510000000004


# Do not repeat yourself
def generate_list(size):
    return [randint(-100, 100) for _ in range(size)]


def iter_test(func):
    for i in range(2, 7):
        numbers = generate_list(10 ** i)
        start_time = perf_counter()
        func(numbers)
        end_time = perf_counter()
        print(end_time - start_time)

    cProfile.run(f'{func.__name__}(generate_list(100000))')


if __name__ == '__main__':
    iter_test(find_max_negative_1)
    iter_test(find_max_negative_2)


