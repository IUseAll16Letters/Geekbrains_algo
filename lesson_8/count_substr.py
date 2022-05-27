"""1. 1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""


# example: abracadabra -> 'a', 'ab', 'abr', 'abra', 'abrac' ... 'b', 'br', 'bra' ... 'ra' ... 'a' <- not included
def count_sub(string: str):
    hash_set = set()

    for i in range(len(string) - 1):
        for j in range(i + 1, len(string) + 1):
            hash_set.add(hash(string[i:j]))
    print(hash_set)
    counter = len(hash_set)
    return counter


def main():
    for i in ('abracadabra', 'hello world!', 'division bell'):
        input_string = i
        print(count_sub(input_string))


main()
