"""
Створити функцію copydeep(obj), що створює і повертає глибоку копію переданого об'єкту obj. Умови:

Не можна використовувати deepcopy з модулю copy
Вважати, що можливі лише ці типи об'єктів та іхніх можливих вкладених елементів,
які можуть бути передані у функцію: str, int, float, list, tuple
Для спрощення завдання вважати, що вхідні колекції (tuple, list) не матимуть рекурсивних елементів,
тобто не міститимуть самі себе на будь-якій глибині.
Якщо редагується будь-яка частина чи вкладений на довільній глибині елемент оригінального списку, то в копії не має нічого змінюватися.
Наприклад:
lst1 = ['a', 1, 2.0, ['b']]
lst2 = copydeep(lst1)
lst1[3].append(0)
print(lst1[3], lst2[3])  # ['b', 0] ['b']
"""
from typing import Union


def copydeep(obj: Union[str, int, float, bool, list, tuple]):
    if isinstance(obj, (str, int, float, bool)):
        return obj

    if isinstance(obj, tuple):
        return tuple(copydeep(x) for x in obj)

    if isinstance(obj, list):
        return [copydeep(x) for x in obj]


def main():
    lst1 = ['a', 1, 2.0, ['b']]
    lst2 = copydeep(lst1)
    lst1[3].append(0)
    print(lst1, lst2)  # ['b', 0] ['b']


if __name__ == '__main__':
    main()
