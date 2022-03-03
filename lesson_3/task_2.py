"""2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа."""
from random import randint


values_1 = [randint(1, 30) for _ in range(randint(10, 30))]
print(values_1)


def get_even_indexes(values: list) -> list:
    return [index for index, _ in enumerate(values) if _ % 2 == 0]


print(get_even_indexes(values_1))
