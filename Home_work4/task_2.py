""""
Даний рядок вигляду 'Taras Shevchenko*1814-03-09*1861-03-10', тобто вказане ім'я, прізвище та дати народження та смерті. Написати програму,
що отримуючи такий рядок через input() виводить на екран окремими рядками ім'я та прізвище людини та її вік в роках.
Для простоти при розрахунку віку можете ігнорувати число місяця та місяць. Тобто для рядку 'Taras Shevchenko*1814-03-09*1861-03-10' програма має вивести:
Name: Taras Schevchenko
Age: 47 years
"""

x = input().split("*")
print('name: ', x[0])
print('Age: ', int(x[2][:4]) - int(x[1][:4]), ' years')
