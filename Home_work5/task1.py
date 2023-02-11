"""
Написати функцію, яка буде переводити градуси в радіани (без використання math.radians).
Використовуючи цю функцію, вивести на екран значення косинусів кутів 60, 45 та 40 градусів.
"""

from bs4 import BeautifulSoup
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
