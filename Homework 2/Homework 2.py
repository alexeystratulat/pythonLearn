import requests
import datetime
# import this
# import antigravity
# import __hello__
# from __future__ import braces
from bs4 import BeautifulSoup
from art import *

from math import sqrt


def currensy():
    url = 'https://minfin.com.ua/currency/nbu'
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'html.parser')
    table = soup.find("table", {"class": "sc-1x32wa2-1 dYkgjk"})
    tr = table.find("p", {"class": "sc-1x32wa2-9 glerpA"})
    tr = tr.text[:5]
    tr = tr.replace(",", ".")
    tr = float(tr)
    return (tr)


def task2a():
    a = 1
    b = 5
    c = 4

    x = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(x)
    x = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(x)


task2a()


def task2b():
    a = 2
    b = 5
    c = 2

    x = (-b + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    print(x)
    x = (-b - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    print(x)


task2b()


def task3():
    a = str(input("Введіть ваше ім'я: "))

    print('Привіт,', a)


task3()


def task4():
    now = datetime.datetime.now()
    a = (input("Cкiльки у Вас гривень ? "))
    result = int(a) / (currensy())
    print('Станом на ', now.date(), 'це становить ', result, 'доларiв США')


task4()


def task5():
    tprint("alex", font="rnd-xlarge")


task5()
