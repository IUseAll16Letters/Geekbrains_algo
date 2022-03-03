"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
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

values_1[max_value_index], values_1[min_value_index] = values_1[min_value_index], values_1[max_value_index]
print(values_1)
