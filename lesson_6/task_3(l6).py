"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
from random import randint
from sum_used_oop import SumMem


values_1 = [randint(1, 30) for _ in range(50)]
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


if __name__ == '__main__':
    sum_mem = SumMem()
    sum_mem.parse_locals(locals())
    print(sum_mem)

# Using locals()
# Total memory used: 2016 kb
#  <class 'list'>: references: 1, size: 504 kb
#  <class 'int'>: references: 54, size: 1512 kb
