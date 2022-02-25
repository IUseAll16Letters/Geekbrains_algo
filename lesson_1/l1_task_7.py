"""7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, 
составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, 
равнобедренным или равносторонним."""


a = float(input('enter a: '))
b = float(input('enter b: '))
c = float(input('enter c: '))

if a >= b + c or b >= a + c or c >= a + b:
    print("Triangle doesn't exist.")
elif a != b and b != c and c != a:
    print("Triangle is scalene.")
elif a == b == c:
    print('Triangle is equilateral.')
else:
    print('Triangle is isosceles.')

