"""3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану."""

"""Hoare no-sort quickselect algorithm for median search
(can also find any other item of unsorted collection based on pos as if collection is sorted)"""
import random


def quickselect(array, k):

    if len(array) == 1:
        return array[0]

    pivot = random.choice(array)

    lows = [item for item in array if item < pivot]
    highs = [item for item in array if item > pivot]
    pivots = [item for item in array if item == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

if __name__ == '__main__':
    for i in range(15):
        list_1 = [random.randint(1, 250) for _ in range(random.randrange(11, 55, 2))]
        search_item = (len(list_1) >> 1) + 1
        print(sorted(list_1)[search_item] == quickselect(list_1, search_item))
