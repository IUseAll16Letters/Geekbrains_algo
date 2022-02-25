"""6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква."""


user_letter = int(input('Enter alphabet letter order number: '))

print(f"Chosen number is {user_letter}.",
      f"{'Letter ' + chr(user_letter + 96).upper() + ' of english alphabet &' if user_letter < 27 else ''}",
      f"{'Буква ' + chr(user_letter + 1071).upper() + ' русского алфавита.'}", )
