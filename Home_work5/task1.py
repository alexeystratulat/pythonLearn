"""
Написати функцію, яка буде переводити градуси в радіани (без використання math.radians).
Використовуючи цю функцію, вивести на екран значення косинусів кутів 60, 45 та 40 градусів.
"""

from math import pi, cos


def degrees2radians(degrees):
    radians = degrees * pi / 180
    return radians


result_first = cos(degrees2radians(60))
result_second = cos(degrees2radians(45))
result_third = cos(degrees2radians(40))

print("cos 60°:", result_first)
print("cos 45°:", result_second)
print("cos 40°:", result_third)






















































"""from bs4 import BeautifulSoup
import requests


def cos_table(degree):
    url = 'https://calc-best.ru/matematicheskie/trigonometriya/kosinus-ugla'
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'html.parser')
    table = soup.find("table", {"class": "t_a_c"})
    objects = {}

    for i in table.find_all('td'):
        objects[int(i.text.split("=")[0].replace('cos(', '').replace(')', ''))] = i.text.split("=")[1]
    return objects.get(degree)


def degrees_to_radians(degree):
    print(degree, "° равно ", degree * 0.175, " радиан")
    print("косинус", degree, "° равен", cos_table(degree))


degrees_to_radians(int(input("сколько градусов ? ")))
"""
