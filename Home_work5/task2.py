"""
Користувач вводить довжини катетів прямокутного трикутника.
Написати функцію, яка обчислить площу та периметр цього трикутника. Функція має повертати пару значень.

"""
import math


def triangle(a, b):
    perimetr = a + b + (math.sqrt(a ** 2 + b ** 2))
    area = (a * b) / 2

    return area, perimetr


a = float(input("введіть довжиру першого катета "))
b = float(input("тепер- другого "))
print("Площа трикутника = ", triangle(a, b)[0], "Периметр = ", triangle(a, b)[1])
