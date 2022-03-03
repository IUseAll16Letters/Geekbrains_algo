"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""
from random import randint


values_1 = [randint(-100, 100) for _ in range(50)]
print(values_1)

# Option 1: using generator
value = max(i for i in values_1 if i < 0)
print(value, values_1.index(value))


# Option 2
max_negative = float('-inf')
max_negative_idx = 0
for order, item in enumerate(values_1):
    if 0 > item > max_negative:
        max_negative = item
        max_negative_idx = order

print(max_negative, max_negative_idx)
