"""
Написати програму, що вираховує суму усіх цифр трьохзначного числа введеного користувачем через input(). Виконати програму в двох варіантах:

a) З використанням рядків (тобто після input заборонено приводити введене число до int/float/Decimal безпосередньо). Підказка: щоб отримати один символ рядку, треба використати квадратні дужки та індекс цього символу, індекси починаються з нуля: 'abcde'[2] == 'c'.
b) Без використання обробки рядків (після input() одразу приведіть текст до int() та не переводьте в рядок назад, а працюйте з цим числом)

"""

def task2a():

    print("Введите 3х значное число ")

    a=(input())

    if len(a)==3:
        b=0;
        for x in range(len(a)):
            b+= int(a[x])
        print(b)
    else:
        print("Ты ввел чет не то, попробуй еще раз ")
        task2a()

task2a()





