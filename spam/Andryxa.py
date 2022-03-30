
def read_input():
    f = open("input.txt")
    f.readline()
    volumes_str = f.readline()
    f.close()
    return tuple(map(int, volumes_str.split()))


def andruxa(array):
    for i in range(len(array)-1):
        if array[i] > array[i + 1]:
            return -1

    return array[-1] - array[0]


print(andruxa(read_input()))

