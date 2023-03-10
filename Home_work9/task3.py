"""
Розширити функцію copydeep() з попереднього домашнього завдання, щоб вона також правильно копіювала dict.

Не можна використовувати deepcopy з модулю copy
Вважати, що можливі лише ці типи об'єктів та іхніх можливих вкладених елементів, які можуть бути передані у функцію: str, int, float, bool, list, tuple, dict
Для спрощення завдання вважати, що вхідні колекції (tuple, list, dict) не матимуть рекурсивних елементів, тобто не міститимуть самі себе на будь-якій глибині.
Якщо редагується будь-яка частина чи вкладений на довільній глибині елемент оригінального списку, то в копії не має нічого змінюватися.
"""

from typing import Union


def copydeep(
    obj: Union[str, int, float, bool, list, tuple, dict]
):
    if isinstance(obj, (int, float, str, bool)):
        return obj

    if isinstance(obj, tuple):
        return tuple(copydeep(x) for x in obj)

    if isinstance(obj, list):
        return [copydeep(x) for x in obj]

    if isinstance(obj, dict):
        return {copydeep(key): copydeep(value) for key, value in obj.items()}


def main():
    dict_1 = {1: "a", 2: 1, 3: 2.0, 4: ["b"]}
    dict_2 = copydeep(dict_1)
    dict_1[1] = 33
    error_msg = "Result must be '{1: 'a', 2: 1, 3: 2.0, 4: ['b']}'"
    assert dict_2 == {1: "a", 2: 1, 3: 2.0, 4: ["b"]}, error_msg
    print(dict_2)



if __name__ == "__main__":
    main()