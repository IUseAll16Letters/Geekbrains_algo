from random import randint


def pick_sort(ls: list) -> list:
    a = ls.copy()
    for i in range(len(ls)):
        idxMin = i
        for j in range(1 + i, len(ls)):
            if a[j] < a[idxMin]:
                idxMin = j
            j += 1
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
        i += 1
    return a


if __name__ == '__main__':
    list_ = [randint(-100, 100) for _ in range(20)]
    print(list_)
    print(sorted(list_) == pick_sort(list_))
