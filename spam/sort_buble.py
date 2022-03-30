"""1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее)."""


from random import randint as rn


def bb_sort(array: list, reverse=False) -> list:
    # Optional: reverse = bool(reverse) * 2 - 1 replace check sign '>' with '<'
    reverse = -1 if reverse else 1
    idx = 1

    while idx < len(array):
        # Оптимизация по отсортированности
        is_sorted = True

        for i in range(len(array) - idx):
            if array[i] * reverse > array[i+1] * reverse:
                array[i], array[i+1] = array[i+1], array[i]
                is_sorted = False

        if is_sorted:
            break
        idx += 1

    return array


if __name__ == '__main__':
    lim = 100
    for _ in range(5):
        print(values := [rn(-lim, lim) for i in range(10)])
        rev = rn(0, 1)
        s = sorted(values, reverse=bool(rev))
        f = bb_sort(values, reverse=bool(rev))
        print(f's: {s}\nf: {f}\nis_equal: {s == f}')
        print('*' * 10)


# [-8, -97, 94, -78, 43, 39, 43, -60, -38, -15]
# s: [-97, -78, -60, -38, -15, -8, 39, 43, 43, 94]
# f: [-97, -78, -60, -38, -15, -8, 39, 43, 43, 94]
# is_equal: True
# **********
# [67, -39, 31, -47, -23, 77, -54, -48, 52, -77]
# s: [77, 67, 52, 31, -23, -39, -47, -48, -54, -77]
# f: [77, 67, 52, 31, -23, -39, -47, -48, -54, -77]
# is_equal: True
# **********
# [-94, 86, -83, 96, -29, 72, -71, -44, 12, 21]
# s: [-94, -83, -71, -44, -29, 12, 21, 72, 86, 96]
# f: [-94, -83, -71, -44, -29, 12, 21, 72, 86, 96]
# is_equal: True
# **********
# [82, 52, -1, -2, -92, -62, -29, -60, 18, -43]
# s: [-92, -62, -60, -43, -29, -2, -1, 18, 52, 82]
# f: [-92, -62, -60, -43, -29, -2, -1, 18, 52, 82]
# is_equal: True
# **********
# [-90, -24, 10, 29, 7, -47, 92, 26, -69, -25]
# s: [-90, -69, -47, -25, -24, 7, 10, 26, 29, 92]
# f: [-90, -69, -47, -25, -24, 7, 10, 26, 29, 92]
# is_equal: True
