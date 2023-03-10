"""
Розширити функцію copydeep() з попереднього домашнього завдання, щоб вона також коректно працювала на рекурсивних структурах данних.

Не можна використовувати deepcopy з модулю copy
УВАГА: Вважати, що кортежі, тобто tuple ніколи не будуть присутні в данних! Їх не треба обробляти -- інакше це безкінечно збільшить складність вашої функції
Вважати, що можливі лише ці типи об'єктів та іхніх можливих вкладених елементів, які можуть бути передані у функцію: str, int, float, bool, list, dict
Якщо редагується будь-яка частина чи вкладений на довільній глибині елемент оригінального списку, то в копії не має нічого змінюватися.
Алгоритм може бути такий:
Потрібно завести об'єкт memory, як на лекції
На початку функції перевірити чи об'єкт obj вже присутній в memory за його id. Якщо так -- повернути його з memory, не копіювати
Перед копіюванням списку/словника, створити порожній список/словник, додати його в memory за ключем, що є id оригінального списку/словника
Далі в відповідному циклі for копіювати і давати елементи в копію спика/словника, що створена на попередньому кроці
Повернути копію списка/словника
УВАГА: не намагайтеся для рішення використати list-comprehension, dict-comprehension чи generator expression: рішення не вийде, а ви себе заведете в тупик
Перевіряйте на такому прикладі:

test_data = [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658]}, 2.0, {'e': 0}]
test_data[3]['d'] = test_data
test_data[-1]['f'] = test_data[-1]
copy = copydeep(test_data)
print(test_data)
# [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658], 'd': [...]}, 2.0, {'e': 0, 'f': {...}}]
print(copy)
# [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658], 'd': [...]}, 2.0, {'e': 0, 'f': {...}}]
print(copy[3]['c'] is not test_data[3]['c'])  # True
print(copy[3]['d'] is not test_data[3]['d'])  # True
print(copy[3]['d'] is copy)  # True
print(copy[-1] is not test_data[-1])  # True
print(copy[-1] is copy[-1]['f'])  # True
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