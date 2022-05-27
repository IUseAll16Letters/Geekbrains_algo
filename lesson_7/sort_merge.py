"""2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""
from random import randint, random


def merge_sort(array: list) -> list:

    if len(array) == 1:
        return array

    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    left = merge_sort(array[:len(array) >> 1])
    right = merge_sort(array[len(array) >> 1:])

    i, j = 0, 0

    while len(left) > i and len(right) > j:

        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        array[i + j] = left[i]
        i += 1

    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


if __name__ == '__main__':
    list_1 = [random() * randint(0, 49) for _ in range(15)]
    print(list_1)
    print(merge_sort(list_1))


