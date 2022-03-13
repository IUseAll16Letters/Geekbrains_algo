"""алгоритм нахождения i-го по счёту простого числа.
   Используя алгоритм «Решето Эратосфена»"""
import cProfile
import time


# Prime number theorem
primes_rows = {4:      10,
               25:     10 ** 2,
               168:    10 ** 3,
               1229:   10 ** 4,
               9592:   10 ** 5,
               78498:  10 ** 6,
               664579: 10 ** 7
               }


# O(n * log(log n)) as worst case
def eratosfen(n: int) -> int:
    # defining the range of primes maximum value
    for key in primes_rows.keys():
        if n <= key:
            limit = primes_rows[key]
            break
    else:
        print(f'Value to big')
        return -1

    # let values is bool list
    values = [1 for _ in range(limit)]
    count_prime = 0

    for index in range(2, limit):
        if values[index]:
            count_prime += 1

            if count_prime == n:
                return index

            for j in range(index ** 2, limit, index):
                values[j] = 0


if __name__ == '__main__':
    for i in range(2, 6):
        start = time.perf_counter()
        eratosfen(10 ** i)
        end = time.perf_counter()
        print(end - start)

    cProfile.run('eratosfen(100000)')

#100    0.00016930000000000417
#1000   0.0019497000000000056
#10000  0.14066
#100000 1.6765683

# 6 function calls in 1.679 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.017    0.017    1.679    1.679 <string>:1(<module>)
#         1    1.232    1.232    1.662    1.662 eratosfen_1.py:20(eratosfen)
#         1    0.430    0.430    0.430    0.430 eratosfen_1.py:31(<listcomp>)
#         1    0.000    0.000    1.679    1.679 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
