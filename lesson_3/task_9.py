"""9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""
from random import randint


matrix = []
for row in range(5):
    matrix.append([randint(1, 50) for _ in range(5)])

print(*matrix, sep='\n')

max_min_value = 0
for row in zip(*matrix):
    if min(row) > max_min_value:
        max_min_value = min(row)

print(f"Biggest value among matrix rows' minimums is: {max_min_value}")
