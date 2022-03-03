"""4. Определить, какое число в массиве встречается чаще всего."""
from random import randint


values_1 = [randint(1, 30) for _ in range(50)]
print(values_1)


# Option 1
def get_max(values_list: list) -> tuple:
    max_value = [0]
    max_value_count = [0]
    i_count = [0]
    for i in set(values_list):
        i_count[0] = values_list.count(i)
        if i_count[0] > max_value_count[0]:
            max_value[0] = i
            max_value_count[0] = i_count[0]
    return max_value[0], max_value_count[0]


print(get_max(values_1))


# Option 2
def get_max_dict(values_list: list):
    items_count = {}
    for i in values_list:
        if i not in items_count.keys():
            items_count[i] = 1
        else:
            items_count[i] += 1

    for key, value in items_count.items():
        if value == max(items_count.values()):
            print(f'{key}, ', end='')
    print(f'has(have) seen {max(items_count.values())} times')


get_max_dict(values_1)
