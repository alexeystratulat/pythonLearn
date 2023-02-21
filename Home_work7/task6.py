"""
Створити функцію, що приймає натуральне число і повертає число з послідовності Фібоначі, позиція якого відповідає введеному числу.
Розрахунок відповідного числа з послідовності має відбуватися за допомогою циклу, не рекурсії!

Кожне наступне число послідовности Фібоначі -- це сума двох попередніх чисел. Тобто:

0 1 1 2 3 5 8 13 21 34 55 89 і т.д.

Отже, якщо в функцію передадуть число 5, то вона має повернути 5те число з послідовности, тобто 3.
Якщо введуть 10, то має повернути 10те число, тобто 34.

Розрахувати за допомогою цієї функції та вивести на екран 20те число з послідовності Фібоначі.

Примітка: на ваш вибір прийняти, з яких чисел починається послідовність: або з 0 та 1, або з 1 та 1.
"""


def fibonachi_number(number):
    fibonachi = [0, 1]

    if number > 2:
        for i in range(2, number):
            fibonachi.append(fibonachi[i - 1] + fibonachi[i - 2])

    return fibonachi[number - 1]


def main():
    number = int(input("Input the number :"))
    print(fibonachi_number(number))


def test():
    assert fibonachi_number(2) == 1
    assert fibonachi_number(10) == 34


if __name__ == "__main__":
    main()
    test()
