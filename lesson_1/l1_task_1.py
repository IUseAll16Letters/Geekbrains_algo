"""1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""


# P.s. Не уловил нужна ли проверка валидности ввода. Сделал проверку только для первого задания.
while True:
    user_input = input('Enter a 3 digit natural number: ')
    try:
        user_input = abs(int(user_input))
        if user_input // 1000 >= 1 or user_input // 100 == 0:
            raise ValueError
        else:
            break
    except ValueError:
        print(f'Incorrect input value. Input must be 3 digit natural int.')
print(f'User number is: {user_input}.')

# Вариант 1. При помощи 3х констант с сохранением исходного значения
a = user_input // 100
b = (user_input // 10) % 10
c = user_input % 10
print(f"sum: {a + b + c}, mult: {a * b * c}")

# Вариант 2. Через while. Без сохранения исходного значения. Кушаем место в памяти
sum_result = 0
mult_result = 1

while user_input:
    sum_result += user_input % 10
    mult_result *= user_input % 10
    user_input //= 10
print(f"sum: {sum_result}, mult: {mult_result}.")
