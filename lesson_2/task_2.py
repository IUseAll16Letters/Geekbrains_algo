"""2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""


def odd_even_calculation(number: int):
    odd = 0
    even = 0
    while number:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        number //= 10
    return f"odds: {odd}, evens: {even}"


print(odd_even_calculation(34560))
