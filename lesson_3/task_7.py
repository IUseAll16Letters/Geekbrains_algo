"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""
from random import randint
import numpy as np


# Option 1: go through the list comparing items
values_1 = [randint(-100, 100) for _ in range(50)]
print(values_1)

min_1 = values_1.pop(0)
min_2 = values_1.pop(0)
min_1, min_2 = min([min_1, min_2]), max([min_1, min_2])

for value in values_1:
    if value <= min_1:
        min_1, min_2 = value, min_1
    elif value < min_2:
        min_2 = value

print(min_1, min_2)


# Option 2: 2 subsequent pop-s + numpy
values_1 = [randint(-100, 100) for _ in range(50)]
print(values_1)

min_index = np.argmin(values_1)
min_1 = values_1.pop(min_index)
min_index = np.argmin(values_1)
min_2 = values_1.pop(min_index)

print(min_1, min_2)
