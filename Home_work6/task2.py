"""
Написати функцію для рішення квадратних рівнянь.

def solve_quadratic_equation(a, b, c):
    # always returns 2(!) values: either 2 roots, 1 root and None or 2 Nones
    pass
Написати програму, що отримує ввід від користувача (коефіцієнти a, b, c) та використовує написану функцію, щоб вивести користувачу результат на екран.
Якщо рівняння має два рішення, то вивести їх як "x1" та "x2", якщо лише один корінь, то вивести, як "x".
Якщо коренів немає, то вивести текст, що рішень немає.

Примітка 1: загально прийнятим (і технічно більш правильним) буде порівнювати з None не через оператор рівности ==, а через оператор is.
Тобто не "x1 == None", а "x1 is None".

Примітка 2: В функції роз'язання рівняння не робимо ввід або вивід!
Ця функція має повністю відповідати запропонованій сигнатурі, приймати відповідні параметри, розраховувати результат і лише повертати його (не виводити на екран!).
Ввід та вивід має виконуватися в main()
Примітка 3:

Це перше ваше використання спеціального значення None.
"""
import math


def solve_quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    sqrtr = math.sqrt(abs(d))
    if d > 0:
        x1 = (-b + sqrtr) / (2 * a)
        x2 = (-b - sqrtr) / (2 * a)
        return x1, x2

    elif d == 0:
        x3 = -b / (2 * a)
        return x3, None

    else:
        return None, None


def tests():
    assert solve_quadratic_equation(2, 6, 4) == (-1.0, -2.0)
    assert solve_quadratic_equation(1, -6, 9) == (3.0, None)
    assert solve_quadratic_equation(3, -4, 2) == (None, None)


def main():
    a = float(input('1st number: '))
    b = float(input('2nd number: '))
    c = float(input('3rd number: '))
    print(solve_quadratic_equation(a, b, c))


if __name__ == "__main__":
    tests()
    main()
