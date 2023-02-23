"""
Дано довільний список. Створити функцію index(lst, elem), що повертатиме індекс elem в списку lst, або, якщо елемент відсутній, то None.
Не можна використовувати метод list().index().

def index(lst, elem):  # returns integer or None
    pass
"""


def index(lst, elem):  # returns integer or None
    for i in range(0, len(lst)):
        if i == elem:
            return i

    return None


def main():
    numbers = [0, 1, 2, 3, 4, 5, 6, 5, 8, 9]
    print(index(numbers, 5))


if __name__ == '__main__':
    main()
