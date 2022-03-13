"""алгоритм нахождения i-го по счёту простого числа.
   Без использования «Решета Эратосфена» """
import cProfile
import time


def prime(n: int) -> int:
    count = 1
    current_number = 2

    # O(n) for while
    while count < n:
        current_number += 1
        # O(m√n) for range - Но это неточно!
        for div in range(2, int(current_number ** 0.5) + 1):
            if current_number % div == 0:
                break
        else:
            count += 1

    return current_number


if __name__ == '__main__':
    for i in range(2, 6):
        start = time.perf_counter()
        prime(10 ** i)
        end = time.perf_counter()
        print(end - start)

    cProfile.run('prime(100000)')

#100    0.0003937999999999997
#1000   0.0080806
#10000  0.1562735
#100000 5.0368057

# 4 function calls in 5.157 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    5.157    5.157 <string>:1(<module>)
#         1    5.157    5.157    5.157    5.157 find_prime.py:8(prime)
#         1    0.000    0.000    5.157    5.157 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
