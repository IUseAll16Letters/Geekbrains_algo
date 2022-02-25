"""4. Написать программу, которая генерирует в указанных пользователем границах: 
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, 
если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно."""
import random


start_value = input('Enter first value: ')
end_value = input('Enter second value: ')
option = input(f'Select option:\n1. Random natural number\n2. Random float\n3. Random letter\n')

if option == '1':
    print(f'Random natural number between {start_value} and {end_value}:')
    start_value = int(start_value)
    end_value = int(end_value)
    result = random.randint(start_value, end_value)

elif option == '2':
    print('Random float between {start_value} and {end_value}')
    start_value = float(start_value)
    end_value = float(end_value)
    result = random.uniform(start_value, end_value)

elif option == '3':
    print('Random letter between {start_value} and {end_value}')
    start_value = ord(start_value)
    end_value = ord(end_value)
    result = chr(random.randint(start_value, end_value))

else:
    result = 'Undefined option'

print(result)
