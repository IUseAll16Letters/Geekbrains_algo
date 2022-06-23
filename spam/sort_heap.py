from random import randint


def sift_up(heap, index, heapsize):
    max_item_index = index
    if (index * 2 + 1) < heapsize and heap[index * 2 + 1] > heap[max_item_index]:
        max_item_index = index * 2 + 1
    if (index * 2 + 2) < heapsize and heap[index * 2 + 2] > heap[max_item_index]:
        max_item_index = index * 2 + 2
    if max_item_index != index:
        heap[index], heap[max_item_index] = heap[max_item_index], heap[index]
        sift_up(heap, max_item_index, heapsize)


def heapify(array, heapsize=None):
    if heapsize is None:
        heapsize = len(array) - 1

    for i in range((len(array) - 2) >> 1, -1, -1):
        sift_up(array, i, heapsize)


def heap_sort(heap):
    heapify(heap)
    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift_up(heap, 0, i)


def main():
    for _ in range(5000):
        array = [randint(1, 5000) for __ in range(1500)]
        heap_sort(array)
        for idx, item in enumerate(array[1:], 1):
            if array[idx - 1] > item:
                print('\033[31mLIAR\033[0m', array[idx], item, idx)


if __name__ == '__main__':
    main()
