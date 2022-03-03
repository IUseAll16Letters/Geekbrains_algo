"""8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу."""


# Option 1
matrix = []
for row in range(5):
    matrix.append([int(input(f'Enter any digit for row: {row + 1}, pos: {order}: '))
                   for order, _ in enumerate(range(4), 1)])
    matrix[row].append(sum(matrix[row]))

print(*matrix, sep='\n')


# Option 2. The same, but using cycle instead of list comprehension
