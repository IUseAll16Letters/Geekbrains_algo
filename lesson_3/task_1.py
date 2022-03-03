"""1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

num_list = [0] * 8


# Option 1: full check
for natural_number in range(2, 100):
    for digit in range(2, 10):
        if natural_number % digit == 0:
            num_list[digit-2] += 1

print(num_list)
print('-' * 15)

# Option 2: part check
nm_list = [None] * 8
for i in range(2, 10):
    lim = 99
    nm_list[i-2] = int(lim // i)

print(nm_list)
