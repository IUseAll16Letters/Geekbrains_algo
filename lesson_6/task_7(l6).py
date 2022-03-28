"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""
from random import randint
import numpy as np
from sum_used_oop import SumMem


# Option 1: go through the list comparing items
values_1 = [randint(-100, 100) for _ in range(50)]
print(values_1)

# Pop with 0 index - iq55 solution
min_1 = values_1.pop(0)
min_2 = values_1.pop(0)
min_1, min_2 = min([min_1, min_2]), max([min_1, min_2])

for value in values_1:
    if value <= min_1:
        min_1, min_2 = value, min_1
    elif value < min_2:
        min_2 = value

print(min_1, min_2)

if __name__ == '__main__':
    sum_mem_1 = SumMem()
    sum_mem_1.parse_locals(locals())
    print(sum_mem_1)

# Total memory used: 1932 kb
#  <class 'list'>: references: 1, size: 504 kb
#  <class 'int'>: references: 51, size: 1428 kb


# Option 2: 2 subsequent pop-s + numpy
# Обкладываемся экземплярами класса
sum_mem_2 = SumMem()

values_1 = [randint(-100, 100) for _ in range(50)]
sum_mem_2.add_one(values_1)
print(values_1)

min_index = np.argmin(values_1)
min_1 = values_1.pop(min_index)
min_index = np.argmin(values_1)
min_2 = values_1.pop(min_index)
sum_mem_2.add_many(min_1, min_2, min_index)
print(min_1, min_2)
print(sum_mem_2)

# Total memory used: 1992 kb
#  <class 'list'>: references: 1, size: 504 kb
#  <class 'int'>: references: 52, size: 1456 kb
#  <class 'numpy.int64'>: references: 1, size: 32 kb
