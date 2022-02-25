"""9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)."""


a = int(input('value a: '))
b = int(input('value b: '))
c = int(input('value c: '))

if b < a < c or b > a > c:
    print('a is middle number. ')
elif a > b > c or a < b < c:
    print('b is middle number. ')
else:
    print('c is middle number. ')