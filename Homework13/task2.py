"""
Створити два класи:
Круг і Точка (на площині -- тобто є тільки дві осі координат).
Створити в класі Круг метод, що, в якості параметра, приймає екземпляр Точки, перевіряє, чи дана точка знаходиться всередині круга, і повертає, відповідне булеве значення.
"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def location_of_point(self, point):
        distance_between_circle_and_point =self.r - (round(math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2), 2))
        return distance_between_circle_and_point >= 0


def main():
    circle1 = Circle(10, 10, 3)
    point = Point(5, 5)
    print(circle1.location_of_point(point))


if __name__ == "__main__":
    main()
