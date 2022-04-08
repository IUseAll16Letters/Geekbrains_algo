def read_file():
    with open('input.txt', 'r', encoding='utf-8') as F:
        volume = int(F.readline().split()[1])
        array = tuple(map(int, F.readline().split()))
    return array, volume


def fnc(k, arr):
    lst = sorted(arr)
    print(lst)
    d = {}
    smm = sum(lst[:k])
    for i in range(len(lst)-k):
        print(i)
        smm += lst[i+k]
        print(smm, 'smm')
        sb, se = 0, smm
        for p in range(k+1):
            print(p, 'p')
            v = lst[i+p]
            print(v, 'v')
            se -= v
            sum_dist = (p*v - sb) + (se - (k-p)*v)
            if v not in d or sum_dist < d[v]:
                d[v] = sum_dist
            sb += v
        smm -= lst[i]
    for v in list(arr):
        print(str(d.get(v)), end=' ')


def main():
    a, v = read_file()
    fnc(v, a)


main()
