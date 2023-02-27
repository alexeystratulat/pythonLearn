"""
Дано довільний список. Створити функцію index(lst, elem), що повертатиме індекс elem в списку lst, або, якщо елемент відсутній, то None.
Не можна використовувати метод list().index().

def index(lst, elem):  # returns integer or None
    pass
"""


def index(lst, elem):  # returns integer or None
    for i in range(0, len(lst)):
        if lst[i] == elem:
            return i




def main():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print(index(numbers, 50))


if __name__ == '__main__':
    main()
