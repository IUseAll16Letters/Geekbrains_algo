"""1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы
с наиболее эффективным использованием памяти."""


class SumMem:
    def __init__(self):
        self._sum_memory = 0
        self._variables_types = {}

    def __str__(self):
        mem = f'Total memory used: \033[34m{self._sum_memory}\033[0m kb'
        types = ' '.join(
            f'{k}: references: {v[0]}, size: \033[34m{v[1]}\033[0m kb \n' for k, v in self._variables_types.items())
        return mem + '\n' + types

    def add_many(self, *objects):
        for item in objects:
            self.add_one(item)

    def add_one(self, item):
        obj_type, obj_size = item.__class__, item.__sizeof__()
        self._sum_memory += obj_size
        if obj_type in self._variables_types:
            self._variables_types[obj_type][0] += 1
            self._variables_types[obj_type][1] += obj_size
        else:
            self._variables_types[obj_type] = [1] * 2
            self._variables_types[obj_type][1] = obj_size

        if hasattr(item, '__iter__'):
            if hasattr(item, 'items'):
                for key, val in item.items():
                    self.add_one(key)
                    self.add_one(val)
            elif not isinstance(item, str):
                for i in item:
                    self.add_one(i)

    def parse_locals(self, local_items):
        """parsing py.file locals() dict"""
        locals_ = local_items.copy()
        for item in locals_:
            if item.startswith('__'):
                print(f'{item} \033[93m is magic\033[0m')
            elif hasattr(locals_.get(item), '__loader__') or hasattr(locals_.get(item), '__call__'):
                print(f'{item} \033[96m is module or func\033[0m')
            else:
                if not isinstance(locals_.get(item), SumMem):
                    self.add_one(locals_.get(item))


if __name__ == '__main__':
    string_ = 'string'
    integer_ = 123
    float_ = 12.56
    list_ = [0, 1, 2, 3, 4]
    dict_ = {'1': 14, '2': 15}
    tuple_ = (2, 3, 4, 5, 6)
    bytes_ = b'type something'
    set_ = {1, 2, 3, 4, 5}

    calc_mem_1 = SumMem()
    calc_mem_1.add_many(string_, integer_, float_, list_, dict_, tuple_, bytes_, set_)
    print(calc_mem_1)
    print('-' * 50)

    calc_mem_2 = SumMem()
    calc_mem_2.parse_locals(locals())
    print(calc_mem_2)

# Total memory used: 2190 kb
#  <class 'str'>: references: 3, size: 155 kb
#  <class 'int'>: references: 32, size: 892 kb
#  <class 'float'>: references: 1, size: 24 kb
#  <class 'list'>: references: 1, size: 80 kb
#  <class 'dict'>: references: 1, size: 216 kb
#  <class 'tuple'>: references: 1, size: 64 kb
#  <class 'bytes'>: references: 1, size: 47 kb
#  <class 'set'>: references: 1, size: 712 kb
