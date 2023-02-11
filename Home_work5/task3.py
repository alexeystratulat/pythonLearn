"""
Написати функцію, яка обчислює площу та об'єм конуса за його радіусом та висотою.
Функція має повертати два значення.
"""

import math


def cone_square_and_volume(r, h):
    volume = (math.pi * r ** 2) / 3
    area = math.pi * r * h + (math.pi * r ** 2)
    return area, volume


r = float(input("введіть радiус "))
h = float(input("тепер- висоту "))
print("Площа поверхншi конуса = ", cone_square_and_volume(r, h)[0], "Периметр конуса = ", cone_square_and_volume(r, h)[1])
