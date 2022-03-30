from random import randint


def insert_sort(ls: list) ->list:
    a = ls.copy()
    for i in range(len(ls)):
        temp = a[i]
        j = i
        while a[j - 1] > temp and j > 0:
            a[j] = a[j-1]
            j -= 1
        a[j] = temp
        print(a)
    return a


if __name__ == '__main__':
    list_ = [randint(1, 100) for _ in range(10)]
    print(insert_sort(list_))
    print(sorted(list_))
