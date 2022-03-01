"""7. Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число."""


def natural_multiplicity_summation(n: int) -> bool:
    cycle_summation = 0
    for number in range(1, n+1):
        cycle_summation += number
    forumla_result = n * (n + 1) / 2

    print(cycle_summation, forumla_result)

    return cycle_summation == forumla_result


print(natural_multiplicity_summation(15))
