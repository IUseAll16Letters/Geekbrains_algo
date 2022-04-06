"""2. Закодируйте любую строку из трех слов по алгоритму Хаффмана."""

from collections import Counter


# Classes: Node if has children, else Leaf
class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def walk(self, code, mem):
        self.left.walk(code, mem + '0')
        self.right.walk(code, mem + '1')


class Leaf:
    def __init__(self, char):
        self.char = char

    def walk(self, code, mem):
        code[self.char] = mem or '0'


# Sieve item up, if heap not invariant
def sieve_up(heap, end_pos, newitem_pos):
    item = heap[newitem_pos]

    while newitem_pos > end_pos:
        parent_pos = (newitem_pos-1) >> 1
        parent = heap[parent_pos]
        if item < parent:
            heap[newitem_pos] = parent
            newitem_pos = parent_pos
            continue
        break
    heap[newitem_pos] = item


# Sieve item down, if heap not invariant
def sieve_down(heap, i):
    end = len(heap)
    start = i
    newitem = heap[i]
    childpos = (i << 1) + 1

    while childpos < end:
        rightchild = childpos + 1
        if rightchild < end and heap[childpos] > heap[rightchild]:
            childpos = rightchild
        heap[i] = heap[childpos]
        i = childpos
        childpos = (i << 1) + 1
    heap[i] = newitem
    sieve_up(heap, start, i)


# get last item of heap, then seive down
def heap_pop(heap):
    last = heap.pop()

    if heap:
        item = heap[0]
        heap[0] = last
        sieve_down(heap, 0)
        return item
    return last


def heap_push(heap, i):
    heap.append(i)
    sieve_up(heap, 0, len(heap) - 1)


def heapify(heap):
    n = len(heap)
    for i in reversed(range(n >> 1)):
        sieve_down(heap, i)


def huffman_encode(string):
    heap = []
    for ch, frequency in Counter(string).items():
        heap.append((frequency, len(heap), Leaf(ch)))
    heapify(heap)

    count = len(heap)
    # Assembling the core Node
    while len(heap) > 1:
        cnt1, _c1, left = heap_pop(heap)
        cnt2, _c2, right = heap_pop(heap)
        heap_push(heap, ((cnt1 + cnt2), count, Node(left, right)))
        count += 1

    code = {}
    if heap:
        root = heap[0][2]
        root.walk(code, '')
    return code


def huffman_decode(coded_str, table):
    decode_table = {v: k for k, v in table.items()}
    result = []
    i = 0
    while i < len(coded_str):
        j = i + 1
        while coded_str[i:j] not in decode_table.keys():
            j += 1
        result.append(decode_table[coded_str[i:j]])
        i = j
    return 'In: ' + ''.join(result)


def begin():
    strings = [ 'beep boop beer', 'guaka-maka-moule', '...become comfortably numb', 'hello world!']
    for string in strings:
        code = huffman_encode(string)
        encoded = ''.join(code[ch] for ch in string)

        for char, amount in sorted(code.items(), key=lambda i: i[0]):
            print(f'{char}: {code.get(char)}')
        print(f"In: '{string}':\nOut: {encoded}")
        print(huffman_decode(encoded, code))
        print('-' * 50)


if __name__ == '__main__':
    begin()
