"""
Виконати попереднє завдання, але функція має враховувати рішення квадратного рівняння в комплексній площині.
Тобто з використанням комплексних чисел, квадратне рівняння завжди матиме рішення.
"""
import math


def solve_quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    sqrtr = math.sqrt(abs(d * -1))
    x1 = (-b + sqrtr) / (2 * a)
    x2 = (-b - sqrtr) / (2 * a)
    return x1, x2


def main():
    a = float(input('1st number: '))
    b = float(input('2nd number: '))
    c = float(input('3rd number: '))

    if a == 0:
        print("a != 0")

    else:
        print(solve_quadratic_equation(a, b, c))


if __name__ == '__main__':
    main()
