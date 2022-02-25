"""8. Определить, является ли год, который ввел пользователем, високосным или невисокосным."""


year_input = int(input('Enter year (YYYY): '))

if year_input % 4 != 0 or (year_input % 100 == 0 and year_input % 400 != 0):
    print(f"{year_input} is normal year. ")
else:
    print(f"{year_input} is a Leap year. ")

