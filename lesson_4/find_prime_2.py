"""алгоритм нахождения i-го по счёту простого числа.
   Без использования «Решета Эратосфена» """
import cProfile
import time

# Prime number theorem
primes_rows = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1229: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7
               }


def find_prime(n: int) -> int:
    # defining the range of primes maximum value
    if n < 5:
        return [2, 3, 5, 7][n - 1]

    for key in primes_rows.keys():
        if n <= key:
            limit = primes_rows[key]
            break
    else:
        print(f'Value to big')
        return -1

    # O(n) - list creation
    nums = [_ for _ in range(8, limit) if _ % 2 != 0]
    prime_ord = 4

    for num in nums:
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                break
        else:
            prime_ord += 1
            if prime_ord == n:
                return num


if __name__ == '__main__':
    for i in range(2, 6):
        start = time.perf_counter()
        find_prime(10 ** i)
        end = time.perf_counter()
        print(end - start)

    cProfile.run('find_prime(100000)')

# 100    0.00025290000000000035
# 1000   0.0050412999999999986
# 10000  0.1840367
# 100000 5.2931602


# 6 function calls in 5.267 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.046    0.046    5.267    5.267 <string>:1(<module>)
#         1    4.632    4.632    5.220    5.220 find_prime_2.py:19(find_prime)
#         1    0.588    0.588    0.588    0.588 find_prime_2.py:33(<listcomp>)
#         1    0.000    0.000    5.267    5.267 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
