from random import randint


def max_heapify(lst: list, item: int, lim=0):
    ln = lim or len(lst)
    left, right = (item << 1) + 1, (item << 1) + 2
    largest = item
    if left < ln and lst[left] > lst[largest]:
        largest = left
    if right < ln and lst[right] > lst[largest]:
        largest = right

    if largest != item:
        lst[item], lst[largest] = lst[largest], lst[item]
        max_heapify(lst, largest, lim)


def build_max_heap(lst: list):
    ln = len(lst)
    for i in reversed(range((ln >> 1) + 1)):
        max_heapify(lst, i)


def heap_sort(lst: list):
    build_max_heap(lst)
    heap_size = len(lst)
    for idx in reversed(range(heap_size)):
      heap_size -= 1
      if heap_size == 0:
            return ''
      lst[0], lst[idx] = lst[idx], lst[0]
      max_heapify(lst, 0, heap_size)


def main():
    for _ in range(10000):
        arr = [randint(1, 5000) for z in range(500)]
        _arr = arr.copy()
        heap_sort(arr)
        if sorted(_arr) != arr:
            print('LIAR')


if __name__ == '__main__':
    main()
    
    
