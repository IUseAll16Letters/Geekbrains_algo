"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего."""

from collections import namedtuple


Company = namedtuple('Company', ['name', 'quart_profit', 'profit'])
print(f'Created tuple, named "{Company.__name__}" with following fields available: ', Company._fields)

companies_amnt = int(input('Enter amount of companies: '))
companies = []
overall_profit = 0
for _ in range(companies_amnt):
    name = input('Enter company name: ')

    income_quarters = []
    profit = 0
    for quarter in range(4):
        income_quarters.append(int(input(f'Income for {quarter + 1} quarter: ')))
        profit += income_quarters[quarter]

    overall_profit += profit
    companies.append(Company._make((name, tuple(income_quarters), profit)))

avg_profit = overall_profit / companies_amnt

print(f'Companies with income above average: ')
for company in companies:
    if company.profit >= avg_profit:
        print(f'{company.name}, with profit: {company.profit}')

print(f'Companies with income below average: ')
for company in companies:
    if company.profit < avg_profit:
        print(f'{company.name}, with profit: {company.profit}')
