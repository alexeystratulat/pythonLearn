"""
Написати функцію, що відповідає на питання, чи перетинають два заданих кола на площині. Кожне коло задається координатами центра та радіусом.

def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
    pass
"""

import math


def circles_intersect(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d <= r1 + r2

def main():
    x1, y1, r1, x2, y2, r2 = map(int, input("Введи 6 значений: ").split())

    print("intersects" if circles_intersect(x1, y1, r1, x2, y2, r2) else " Don't intersect ")


if __name__ == '__main__':
    main()