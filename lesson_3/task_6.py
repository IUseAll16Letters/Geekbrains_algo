"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""
from random import randint


values_1 = [randint(1, 30) for _ in range(randint(10, 30))]
print(values_1)

min_value_index = 0
max_value_index = 0
for index, number in enumerate(values_1):
    if number < values_1[min_value_index]:
        min_value_index = index
    if number > values_1[max_value_index]:
        max_value_index = index

if min_value_index > max_value_index:
    min_value_index, max_value_index = max_value_index, min_value_index

print(sum(values_1[min_value_index + 1: max_value_index]))
