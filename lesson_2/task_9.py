"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""


def natural_max_by_digit_sum():
    digit = {'number': 0,
             'digit sum': 0}

    while True:
        user_number = int(input('Enter natural number: '))
        temp_number = user_number
        temp_sum = 0
        while temp_number:
            temp_sum += temp_number % 10
            temp_number //= 10
        if temp_sum > digit['digit sum']:
            digit['digit sum'] = temp_sum
            digit['number'] = user_number
        print(f"current max: {digit.get('number')}, with sum: {digit.get('digit sum')}. ")


natural_max_by_digit_sum()
