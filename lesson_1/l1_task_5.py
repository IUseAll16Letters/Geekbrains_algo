"""5. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят и сколько между ними находится букв."""


first_letter = input('letter 1: ')
second_letter = input('letter 2: ')

first_letter_pos = ord(first_letter) - 96
second_letter_pos = ord(second_letter) - 96

# optional
# first_letter_pos = ord(first_letter) - ord('a') + 1
# second_letter_pos = ord(second_letter) - ord('a') + 1

print(f"Letter '{first_letter}' is at {first_letter_pos} position, "
      f"letter '{second_letter}' is at {second_letter_pos} position.")
print(f"There are {abs(second_letter_pos - first_letter_pos) - 1} letters "
      f"between '{first_letter}' and '{second_letter}'.")
