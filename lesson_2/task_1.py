"""1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа
должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления
на ноль, если он ввел 0 в качестве делителя."""
operations = {'+': lambda a, b: a + b,
              '-': lambda a, b: a - b,
              '*': lambda a, b: a * b,
              '/': lambda a, b: a / b}

while True:
    print('-' * 15)
    num_one = int(input('enter int # 1: '))
    num_two = int(input('enter int # 2: '))
    expression = input("'+' for summation,\n'-' for subtraction,\n'*' for multiplication,\n"
                       "'/' for division,\n '0' to exit: ")

    if expression == '0':
        break

    if num_two == 0:
        print('Zero Division Error')
        continue
    if expression not in (operations.keys()):
        print('Unknown operation. ')
    else:
        print(f"result of '{expression}' expression is: {operations[expression](num_one, num_two)}")
